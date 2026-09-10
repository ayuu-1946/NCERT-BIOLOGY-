#!/usr/bin/env python3
"""Session 1-S helper — resolve the subscript digits OCR flattens to "F,".

RapidOCR returns every printed F1 / F2 in the scanned chapter as the single
token "F," — the subscript digit comes back as a comma.  F1 vs F2 is the most
heavily examined distinction in the chapter, so it is resolved mechanically:

  1. Render reference glyphs (F, 0-9) in Times New Roman with reportlab,
     rasterise, crop to a tight binary bitmap.
  2. Locate every "F" in a scanned line by FFT template matching over a small
     range of heights and vertical offsets, taking IoU local maxima.
  3. Take the connected component hanging below the baseline just to the right
     of each F — that is the subscript.  (The descender of g/p/q/y is part of
     its own letter above the baseline, so it never appears here.)
  4. Classify it by IoU against the rendered digits, aspect ratio preserved.

Every glyph is written out as ASCII art in `subscripts.json` so the call can be
audited by eye without re-running anything.
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
_D = "0123456789"
_TMPL = None


def _render(ch, size=200, dpi=200):
    tmp = "/tmp/_tmpl.pdf"
    c = canvas.Canvas(tmp, pagesize=(400, 400))
    c.setFont("Times-Roman", size)
    c.drawString(50, 100, ch)
    c.save()
    doc = pymupdf.open(tmp)
    pix = doc[0].get_pixmap(dpi=dpi, colorspace=pymupdf.csGRAY)
    a = np.frombuffer(pix.samples, np.uint8).reshape(pix.height, pix.width)
    ink = a < 140
    if not ink.any():
        return None
    ys, xs = np.where(ink)
    return ink[ys.min():ys.max() + 1, xs.min():xs.max() + 1].astype(np.float32)


def templates():
    global _TMPL
    if _TMPL is None:
        _TMPL = {ch: _render(ch) for ch in "F" + _D}
    return _TMPL


def _resize(t, h):
    th, tw = t.shape
    w = max(1, int(round(tw * h / th)))
    img = Image.fromarray((t * 255).astype(np.uint8)).resize((w, int(h)), Image.BILINEAR)
    return (np.array(img) > 127).astype(np.float32)


def iou_map(ink, t):
    """IoU of template t at every placement; index [dy, dx] = template's top-left."""
    th, tw = t.shape
    H, W = ink.shape
    inter = fftconvolve(ink, t[::-1, ::-1], mode="full")[th - 1:th - 1 + H, tw - 1:tw - 1 + W]
    area = fftconvolve(ink, np.ones_like(t), mode="full")[th - 1:th - 1 + H, tw - 1:tw - 1 + W]
    union = t.sum() + area - inter
    with np.errstate(divide="ignore", invalid="ignore"):
        m = np.where(union > 0, inter / np.maximum(union, 1e-6), 0.0)
    return m


def find_glyph(ink, tmpl, heights, y_lo, y_hi, thresh=0.55):
    """Local maxima of IoU over the given heights / vertical offsets."""
    H, W = ink.shape
    best = np.zeros((H, W), np.float32)
    bestinfo = {}
    for h in heights:
        t = _resize(tmpl, h)
        th, tw = t.shape
        if th < 3 or tw < 2 or th > H or tw > W:
            continue
        m = iou_map(ink, t)
        # the match is recorded at the template's top-left corner
        for dy in range(max(0, y_lo), max(1, min(H - th, y_hi))):
            row = m[dy]
            idx = np.where(row >= thresh)[0]
            for x in idx:
                if row[x] > best[dy, x]:
                    best[dy, x] = row[x]
                    bestinfo[(dy, x)] = (h, th, tw)
    # non-maximum suppression
    hits = []
    for (dy, x), v in sorted(bestinfo.items(), key=lambda kv: -best[kv[0]]):
        if best[dy, x] < thresh:
            continue
        h, th, tw = bestinfo[(dy, x)]
        if any(abs(x - px) < 0.6 * tw and abs(dy - py) < 0.6 * th for px, py, _, _ in hits):
            continue
        hits.append((x, dy, th, tw))
        hits[-1] = (x, dy, th, tw)
        hits = [(a, b, c, d) for (a, b, c, d) in hits]
        # store score too
        hits[-1] = (x, dy, th, tw)
    out = []
    for (x, dy, th, tw) in hits:
        out.append(dict(x=int(x), y=int(dy), h=int(th), w=int(tw),
                        score=float(best[dy, x])))
    out.sort(key=lambda d: d["x"])
    return out


def line_image(page, r, padx=4.0, padtop=4.0, padbot=14.0):
    x0, y0, x1, y1 = r[0], r[1], r[2], r[3]
    clip = pymupdf.Rect(max(0, x0 - padx), max(0, y0 - padtop), x1 + padx, y1 + padbot)
    pix = page.get_pixmap(dpi=DPI, colorspace=pymupdf.csGRAY, clip=clip)
    a = np.frombuffer(pix.samples, np.uint8).reshape(pix.height, pix.width)
    return (a < 140).astype(np.float32), int(padtop * SC), int((y1 - y0 + padtop) * SC)


def baseline_and_cap(ink, box_top, box_bot):
    lab, n = ndimage.label(ink > 0.5, structure=np.ones((3, 3)))
    comps = []
    for i, sl in enumerate(ndimage.find_objects(lab), start=1):
        comps.append((sl[1].start, sl[0].start, sl[0].stop,
                      sl[1].stop - sl[1].start, sl[0].stop - sl[0].start))
    comps = [c for c in comps if c[4] >= 8 and c[1] >= box_top - 6 and c[2] <= box_bot + 6]
    if not comps:
        return None, None
    hs = sorted(c[4] for c in comps)
    cap = hs[min(len(hs) - 1, int(len(hs) * 0.95))]
    tall = [c for c in comps if c[4] >= 0.85 * cap]
    base = int(np.median([c[2] for c in tall])) if tall else int(np.median([c[2] for c in comps]))
    return base, cap


def subscript_at(ink, base, cap, fx, fw):
    H, W = ink.shape
    x0 = max(0, fx + fw - 6)
    x1 = min(W, fx + fw + int(1.0 * cap))
    y0 = min(H, base + 1)
    y1 = min(H, base + int(1.15 * cap))
    win = np.asarray(ink[y0:y1, x0:x1] > 0.5, dtype=np.uint8)
    if win.size == 0 or not win.any():
        return None
    lab, n = ndimage.label(win, structure=np.ones((3, 3)))
    best, bestarr = None, None
    for i, sl in enumerate(ndimage.find_objects(lab), start=1):
        arr = (lab[sl] == i).astype(np.uint8)
        h = sl[0].stop - sl[0].start
        w = sl[1].stop - sl[1].start
        if h < 0.30 * cap or h > 1.0 * cap or w > 1.7 * h:
            continue
        if best is None or h > best:
            best, bestarr = h, arr
    return bestarr


def classify(comp, digits=_D):
    T = templates()
    scores = {}
    for ch in digits:
        t = T.get(ch)
        if t is None:
            continue
        tt = _resize(t, comp.shape[0])
        m = iou_map(comp.astype(np.float32), tt)
        # best placement
        scores[ch] = round(float(m.max()), 3)
    best = max(scores, key=lambda k: scores[k])
    return best, scores


def art(comp):
    return "\n".join("".join("#" if v else "." for v in row) for row in comp)


def main():
    raw = json.load(open(os.path.join(HERE, "ocr_raw.json")))
    doc = pymupdf.open(SRC)
    out = []
    for pno_s, rows in raw.items():
        pno = int(pno_s)
        page = doc[pno - 1]
        for idx, r in enumerate(rows):
            if not ("F," in r[4] or "F." in r[4]):
                continue
            ink, box_top, box_bot = line_image(page, r)
            base, cap = baseline_and_cap(ink, box_top, box_bot)
            rec = dict(page=pno, line=idx, text=r[4], base=base, cap=cap,
                       expected=r[4].count("F,") + r[4].count("F."), glyphs=[])
            if base is None:
                out.append(rec)
                continue
            heights = range(max(8, int(cap * 0.82)), int(cap * 1.04) + 1, 2)
            hits = find_glyph(ink, templates()["F"], heights,
                              max(0, base - int(cap * 1.05)), base - int(cap * 0.7),
                              thresh=0.52)
            rec["nF"] = len(hits)
            for h in hits:
                comp = subscript_at(ink, base, cap, h["x"], h["w"])
                if comp is None:
                    rec["glyphs"].append(dict(x=h["x"], Fscore=h["score"], digit=None))
                    continue
                ch, sco = classify(comp)
                rec["glyphs"].append(dict(x=h["x"], Fscore=round(h["score"], 2), digit=ch,
                                          score=sco[ch], scores=sco, art=art(comp)))
            out.append(rec)
    json.dump(out, open(os.path.join(HERE, "subscripts.json"), "w"), indent=1)
    for rec in out:
        g = [x for x in rec["glyphs"] if x.get("digit")]
        s = " ".join("%s(%.2f/%.2f)" % (x["digit"], x["score"], x["Fscore"]) for x in g)
        print("p%02d L%-3d nF=%d/%d  %-40s %s" %
              (rec["page"], rec["line"], len(rec["glyphs"]), rec["expected"],
               rec["text"][:40], s))


if __name__ == "__main__":
    main()
