#!/usr/bin/env python3
"""Session 1-S helper — read every F-subscript in the chapter off the pixels.

RapidOCR flattens every printed F1 / F2 in the scan to the token "F," — the
subscript digit comes back as a comma, and F1 vs F2 is the single most examined
distinction in this chapter.

Method (no template matching for position, so nothing to mis-localise):
  * crop the OCR line box with room below it, at 400 dpi;
  * find the baseline from the letter bodies;
  * take every connected component that sits entirely below the baseline and
    starts within half a cap-height of it.  A subscript digit is such a
    component.  The descender of g/p/q/y is not (it is attached to its own
    letter above the baseline), commas/full stops are too small to pass the
    height filter, and the next line's ascenders start further down than the
    band allows;
  * the components come out in x order, so the Nth one belongs to the Nth "F,"
    in the line's OCR text;
  * classify each by best-placement IoU against Times digits rendered with
    reportlab, and print ASCII art wherever the call is not clear-cut.

Output: f_digits.json  + a one-line-per-occurrence report.
"""
import json
import os
import sys

import numpy as np
import pymupdf
from PIL import Image
from reportlab.pdfgen import canvas
from scipy import ndimage
from scipy.signal import fftconvolve

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.abspath(os.path.join(HERE, "..", "..", "Chapter", "class 12",
                                   "Chapter 4 - Principles of Inheritance and Variation.pdf"))
DPI = 400
SC = DPI / 72.0
_T = None


def templates():
    global _T
    if _T is None:
        _T = {}
        for ch in "0123456789":
            tmp = "/tmp/_dt.pdf"
            c = canvas.Canvas(tmp, pagesize=(300, 300))
            c.setFont("Times-Roman", 160)
            c.drawString(40, 80, ch)
            c.save()
            doc = pymupdf.open(tmp)
            pix = doc[0].get_pixmap(dpi=200, colorspace=pymupdf.csGRAY)
            a = np.frombuffer(pix.samples, np.uint8).reshape(pix.height, pix.width)
            ink = a < 140
            ys, xs = np.where(ink)
            _T[ch] = ink[ys.min():ys.max() + 1, xs.min():xs.max() + 1].astype(np.float32)
    return _T


def resize(t, h):
    th, tw = t.shape
    w = max(1, int(round(tw * h / th)))
    img = Image.fromarray((t * 255).astype(np.uint8)).resize((w, int(h)), Image.BILINEAR)
    return (np.array(img) > 127).astype(np.float32)


def iou_map(ink, t):
    th, tw = t.shape
    H, W = ink.shape
    inter = fftconvolve(ink, t[::-1, ::-1], mode="full")[th - 1:th - 1 + H, tw - 1:tw - 1 + W]
    area = fftconvolve(ink, np.ones_like(t), mode="full")[th - 1:th - 1 + H, tw - 1:tw - 1 + W]
    union = t.sum() + area - inter
    return np.where(union > 0, inter / np.maximum(union, 1e-6), 0.0)


def best_placement(comp, t):
    tt = resize(t, comp.shape[0])
    try:
        return float(iou_map(comp.astype(np.float32), tt).max())
    except ValueError:
        return 0.0


def art(comp):
    return "\n".join("".join("#" if v else "." for v in row) for row in comp)


def line_image(page, r):
    x0, y0, x1, y1 = r[0], r[1], r[2], r[3]
    clip = pymupdf.Rect(max(0, x0 - 4), max(0, y0 - 4), x1 + 4, y1 + 14)
    pix = page.get_pixmap(dpi=DPI, colorspace=pymupdf.csGRAY, clip=clip)
    a = np.frombuffer(pix.samples, np.uint8).reshape(pix.height, pix.width)
    ink = (a < 140).astype(np.uint8)
    box_top = int(4 * SC)
    box_bot = int((y1 - y0 + 4) * SC)
    return ink, box_top, box_bot


def baseline_cap(ink, box_top, box_bot):
    lab, n = ndimage.label(ink, structure=np.ones((3, 3)))
    comps = []
    for i, sl in enumerate(ndimage.find_objects(lab), start=1):
        comps.append((sl[1].start, sl[0].start, sl[0].stop,
                      sl[1].stop - sl[1].start, sl[0].stop - sl[0].start))
    comps = [c for c in comps if c[4] >= 8 and c[1] >= box_top - 8 and c[2] <= box_bot + 8]
    if not comps:
        return None, None
    hs = sorted(c[4] for c in comps)
    cap = hs[min(len(hs) - 1, int(len(hs) * 0.95))]
    tall = [c for c in comps if c[4] >= 0.85 * cap]
    base = int(np.median([c[2] for c in tall])) if tall else int(np.median([c[2] for c in comps]))
    return base, cap


def main(show_all=False):
    raw = json.load(open(os.path.join(HERE, "ocr_raw.json")))
    doc = pymupdf.open(SRC)
    T = templates()
    out = []
    for pno_s, rows in raw.items():
        pno = int(pno_s)
        page = doc[pno - 1]
        for idx, r in enumerate(rows):
            n_f = r[4].count("F,") + r[4].count("F.")
            if not n_f:
                continue
            ink, box_top, box_bot = line_image(page, r)
            base, cap = baseline_cap(ink, box_top, box_bot)
            rec = dict(page=pno, line=idx, text=r[4], expected=n_f, base=base, cap=cap, glyphs=[])
            if base is None:
                out.append(rec)
                print("p%02d L%-3d !! no baseline  %s" % (pno, idx, r[4][:60]))
                continue
            H, W = ink.shape
            y0 = base + 1
            y1 = min(H, base + int(0.62 * cap))
            band = ink[y0:y1, :]
            lab, n = ndimage.label(band, structure=np.ones((3, 3)))
            cands = []
            for i, sl in enumerate(ndimage.find_objects(lab), start=1):
                arr = (lab[sl] == i).astype(np.uint8)
                h = sl[0].stop - sl[0].start
                w = sl[1].stop - sl[1].start
                if h < 0.35 * cap or h > 0.95 * cap:
                    continue
                if w > 1.6 * h or w < 0.15 * h:
                    continue
                if arr.sum() < 0.18 * h * w:
                    continue                      # too thin to be a digit
                cands.append((sl[1].start, arr))
            cands.sort()
            if len(cands) != n_f:
                rec["warn"] = "found %d glyphs for %d F-occurrences" % (len(cands), n_f)
            for (x, arr) in cands:
                scores = {ch: round(best_placement(arr, t), 3) for ch, t in T.items()}
                order = sorted(scores.items(), key=lambda kv: -kv[1])
                rec["glyphs"].append(dict(x=int(x), digit=order[0][0],
                                          score=order[0][1], runner=order[1],
                                          art=art(arr)))
            out.append(rec)
            summ = " ".join("%s%s" % (g["digit"], "" if g["score"] >= 0.5 else "?")
                            for g in rec["glyphs"])
            print("p%02d L%-3d [%d/%d] %-6s %s" %
                  (pno, idx, len(cands), n_f, summ, r[4][:58]))
            for g in rec["glyphs"]:
                if show_all or g["score"] < 0.55 or (g["score"] - g["runner"][1]) < 0.12:
                    print("      x=%-4d best=%s(%.2f) next=%s(%.2f)" %
                          (g["x"], g["digit"], g["score"], g["runner"][0], g["runner"][1]))
                    for row in g["art"].splitlines():
                        print("        " + row)
    json.dump(out, open(os.path.join(HERE, "f_digits.json"), "w"), indent=1)
    print("wrote f_digits.json")


if __name__ == "__main__":
    main(show_all="--all" in sys.argv)
