#!/usr/bin/env python3
"""Session 1-S helper — read the F-subscripts the OCR flattens to "F,".

RapidOCR returns every printed "F1"/"F2" in the scanned chapter as the single
token "F," — the subscript digit is rendered as a comma.  F1 vs F2 is the most
examined distinction in the chapter, so it is resolved mechanically here:

  1. Render reference glyphs (F, 0-9, punctuation) in Times New Roman with
     reportlab, rasterise, crop to a tight binary bitmap.
  2. Locate every "F" in a scanned line by sliding the rendered F template over
     the line's cap band and taking IoU local maxima.
  3. Immediately to the right of and below each F, take the connected component
     that hangs under the baseline (the descender of g/p/q/y is part of its own
     letter above the baseline, so it never appears here).
  4. Classify that component by IoU against the rendered digit templates,
     scaled to the same height with aspect ratio preserved.

Every glyph is also emitted as ASCII art so the call can be audited by eye.
"""
import json
import os
import sys

import numpy as np
import pymupdf
from PIL import Image
from reportlab.pdfgen import canvas
from scipy import ndimage

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.abspath(os.path.join(HERE, "..", "..", "Chapter", "class 12",
                                   "Chapter 4 - Principles of Inheritance and Variation.pdf"))
DPI = 400
SC = DPI / 72.0
DIGITS = "0123456789"


# ---------------------------------------------------------------- templates
def render_template(ch, size=200, dpi=200):
    tmp = "/tmp/_t.pdf"
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
    return ink[ys.min():ys.max() + 1, xs.min():xs.max() + 1].astype(np.uint8)


TMPL = {}


def templates():
    if not TMPL:
        for ch in "F" + DIGITS + ".,;:'-":
            TMPL[ch] = render_template(ch)
    return TMPL


def resize(t, h):
    th, tw = t.shape
    w = max(1, int(round(tw * h / th)))
    img = Image.fromarray((t * 255).astype(np.uint8)).resize((w, int(h)), Image.BILINEAR)
    return (np.array(img) > 127).astype(np.uint8)


def iou_at(img, tmpl, x0, y0):
    """IoU of tmpl placed with its top-left at (y0,x0) of img."""
    h, w = tmpl.shape
    H, W = img.shape
    if x0 < 0 or y0 < 0 or x0 + w > W or y0 + h > H:
        return 0.0
    sub = img[y0:y0 + h, x0:x0 + w]
    inter = np.logical_and(sub, tmpl).sum()
    union = np.logical_or(sub, tmpl).sum()
    return inter / union if union else 0.0


def best_placement(comp, tmpl):
    """Best IoU of tmpl (scaled to comp height) anywhere over comp's bbox."""
    h = comp.shape[0]
    t = resize(tmpl, h)
    H, W = comp.shape
    th, tw = t.shape
    pad = np.zeros((H + th, W + tw), np.uint8)
    pad[:H, :W] = comp
    best = 0.0
    for dy in range(0, H + th - th + 1):
        for dx in range(0, W + tw - tw + 1):
            v = iou_at(pad, t, dx, dy)
            if v > best:
                best = v
    return best


# ---------------------------------------------------------------- line work
def line_image(page, r, padx=4.0, padtop=4.0, padbot=14.0):
    x0, y0, x1, y1 = r[0], r[1], r[2], r[3]
    clip = pymupdf.Rect(max(0, x0 - padx), max(0, y0 - padtop), x1 + padx, y1 + padbot)
    pix = page.get_pixmap(dpi=DPI, colorspace=pymupdf.csGRAY, clip=clip)
    a = np.frombuffer(pix.samples, np.uint8).reshape(pix.height, pix.width)
    return (a < 140).astype(np.uint8), int(padtop * SC), int((y1 - y0 + padtop) * SC)


def baseline_and_cap(ink, box_top, box_bot):
    lab, n = ndimage.label(ink, structure=np.ones((3, 3)))
    comps = []
    for i, sl in enumerate(ndimage.find_objects(lab), start=1):
        comps.append((sl[1].start, sl[0].start, sl[0].stop,
                      sl[1].stop - sl[1].start, sl[0].stop - sl[0].start))
    comps = [c for c in comps if c[4] >= 8 and c[1] >= box_top - 6 and c[2] <= box_bot + 6]
    if not comps:
        return None, None
    hs = sorted(c[4] for c in comps)
    cap = hs[min(len(hs) - 1, int(len(hs) * 0.9))]
    tall = [c for c in comps if c[4] >= 0.8 * cap]
    base = int(np.median([c[2] for c in tall])) if tall else int(np.median([c[2] for c in comps]))
    return base, cap


def find_F(ink, base, cap):
    """Slide the rendered F template over the cap band; return x positions."""
    t = resize(templates()["F"], cap)
    th, tw = t.shape
    band = ink[max(0, base - cap - 2):base + 2, :]
    scores = []
    for x in range(0, band.shape[1] - tw):
        scores.append(iou_at(band, t, x, max(0, band.shape[0] - th)))
    scores = np.array(scores)
    hits = []
    if len(scores) == 0:
        return hits
    thr = max(0.42, scores.max() * 0.82)
    i = 0
    while i < len(scores):
        if scores[i] >= thr:
            j = i
            while j + 1 < len(scores) and scores[j + 1] >= thr:
                j += 1
            seg = scores[i:j + 1]
            x = i + int(np.argmax(seg))
            hits.append((x, int(tw), float(scores[x - i]), th))
            i = j + 1
        else:
            i += 1
    return hits


def subscript_at(ink, base, cap, fx, fw):
    """Largest component hanging below the baseline just right of the F."""
    H, W = ink.shape
    x0 = max(0, fx + fw - 8)
    x1 = min(W, fx + fw + int(0.9 * cap))
    y0 = min(H, base + 1)
    y1 = min(H, base + int(1.1 * cap))
    win = ink[y0:y1, x0:x1]
    if win.size == 0 or not win.any():
        return None
    lab, n = ndimage.label(win, structure=np.ones((3, 3)))
    best, bestcomp = None, None
    for i, sl in enumerate(ndimage.find_objects(lab), start=1):
        arr = (lab[sl] == i).astype(np.uint8)
        h = sl[0].stop - sl[0].start
        w = sl[1].stop - sl[1].start
        if h < 0.30 * cap or h > 0.95 * cap:
            continue
        if w > 1.6 * h:
            continue
        if best is None or h > best:
            best, bestcomp = h, arr
    return bestcomp


def classify(comp):
    T = templates()
    scores = {}
    for ch in DIGITS + ".,;:'-":
        t = T.get(ch)
        if t is None:
            continue
        scores[ch] = round(best_placement(comp, t), 3)
    best = max(scores, key=lambda k: scores[k])
    return best, scores[best], scores


def art(comp):
    return "\n".join("".join("#" if v else "." for v in row) for row in comp)


def main(show_art=False):
    raw = json.load(open(os.path.join(HERE, "ocr_raw.json")))
    doc = pymupdf.open(SRC)
    out = []
    for pno_s, rows in raw.items():
        pno = int(pno_s)
        page = doc[pno - 1]
        for idx, r in enumerate(rows):
            if "F," not in r[4] and "F." not in r[4]:
                continue
            ink, box_top, box_bot = line_image(page, r)
            base, cap = baseline_and_cap(ink, box_top, box_bot)
            rec = dict(page=pno, line=idx, text=r[4], base=base, cap=cap, glyphs=[])
            if base is None:
                out.append(rec)
                continue
            hits = find_F(ink, base, cap)
            rec["nF"] = len(hits)
            for (fx, fw, sc, th) in hits:
                comp = subscript_at(ink, base, cap, fx, fw)
                if comp is None:
                    rec["glyphs"].append(dict(x=fx, digit=None, art=None))
                    continue
                ch, sco, allsc = classify(comp)
                rec["glyphs"].append(dict(x=fx, digit=ch, score=sco,
                                          top4=sorted(allsc.items(), key=lambda kv: -kv[1])[:3],
                                          art=art(comp) if show_art else None))
            out.append(rec)
    json.dump(out, open(os.path.join(HERE, "f_subscripts.json"), "w"), indent=1)
    for rec in out:
        g = rec["glyphs"]
        s = " ".join("%s(%.2f)" % (x.get("digit"), x.get("score") or 0) for x in g)
        print("p%02d L%-3d nF=%d exp=%d  %-38s %s" %
              (rec["page"], rec["line"], rec.get("nF", -1),
               rec["text"].count("F,") + rec["text"].count("F."),
               rec["text"][:38], s))


if __name__ == "__main__":
    main(show_art="--art" in sys.argv)
