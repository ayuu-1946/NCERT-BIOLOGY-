#!/usr/bin/env python3
"""Session 1-S helper — word-level OCR of the whole scanned chapter.

The chapter PDF is a pure page-image scan: 28 pages, each a single 1105x1482
DeviceRGB raster, `page.get_text()` empty on every page.  Whole-page OCR at
300 dpi reads the words but runs them together ("littleideaaboutthescientific")
and collapses the subscript digits that carry the F1/F2 distinction.

This script re-reads the source word by word:

  1. render the page at 400 dpi grey;
  2. for every line box found by the page pass, split it into words on the
     column-ink gaps (a gap wider than ~8 px at 400 dpi is a space);
  3. compose ~20 word crops into one vertical stack and OCR the stack once -
     detection on a 20-line block is far cheaper than 20 separate calls, and a
     single-word crop gives the recogniser the same pixels the eye would see;
  4. map every detection back to its word by row, and retry individually any
     word the stack pass lost.

Output: ocr_words.json  {page: [[ [x0_pt, text, score], ...] per line]}
        source_text_v2.txt  (one line of words per source line)

Re-run: /tmp/neetenv/bin/python scratch/ch4inh_gate1/word_ocr.py
"""
import json
import os
import sys
import time

import numpy as np
import pymupdf
from PIL import Image
from rapidocr_onnxruntime import RapidOCR

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.abspath(os.path.join(HERE, "..", "..", "Chapter", "class 12",
                                   "Chapter 4 - Principles of Inheritance and Variation.pdf"))
DPI = 400
SC = DPI / 72.0
UP = 2
GAP_PX = 8          # column gap that separates two words at 400 dpi
PAD_X = 8
PAD_TOP = int(4 * SC)
PAD_BOT = int(11 * SC)
MAX_W = 900         # px: stack canvas width cap


def line_crops(page, r):
    """Return [(x0px, word_image)] for one line box, left to right."""
    x0, y0, x1, y1 = r[0], r[1], r[2], r[3]
    clip = pymupdf.Rect(max(0, x0 - 3), max(0, y0 - 4), x1 + 3, y1 + 11)
    pix = page.get_pixmap(dpi=DPI, colorspace=pymupdf.csGRAY, clip=clip)
    a = np.frombuffer(pix.samples, np.uint8).reshape(pix.height, pix.width)
    ink = a < 140
    cols = ink.any(axis=0)
    # run-length of inked columns
    segs, start = [], None
    for i, v in enumerate(cols):
        if v and start is None:
            start = i
        elif not v and start is not None:
            if i - start > 1:
                segs.append((start, i))
            start = None
    if start is not None:
        segs.append((start, len(cols)))
    # merge segments separated by a small gap
    merged = []
    for s in segs:
        if merged and s[0] - merged[-1][1] <= GAP_PX:
            merged[-1] = (merged[-1][0], s[1])
        else:
            merged.append(list(s) if False else (s[0], s[1]))
            merged[-1] = (s[0], s[1])
    out = []
    img = Image.frombytes("L", (pix.width, pix.height), pix.samples)
    for (a0, a1) in merged:
        left = max(0, a0 - PAD_X)
        right = min(pix.width, a1 + PAD_X)
        out.append((x0 - 3 + left / SC, img.crop((left, 0, right, pix.height))))
    return out


def ocr_stack(ocr, words, pad=14):
    """OCR a list of word images composed vertically; return [text|None] each."""
    hs = [w.height for w in words]
    ws = [w.width for w in words]
    W = min(MAX_W, max(ws) + 2 * pad)
    row_h = max(hs) + pad
    canvas = Image.new("L", (W, row_h * len(words) + pad), 255)
    slots = []
    y = pad // 2
    for w in words:
        canvas.paste(w, (pad, y))
        slots.append((y, y + w.height))
        y += row_h
    big = canvas.resize((canvas.width * UP, canvas.height * UP), Image.LANCZOS)
    res, _ = ocr(np.array(big))
    out = [None] * len(words)
    if res:
        for box, txt, score in res:
            ys = [p[1] for p in box]
            cy = (min(ys) + max(ys)) / 2 / UP
            best, bestd = None, 1e9
            for i, (sy, ey) in enumerate(slots):
                d = 0 if sy <= cy <= ey else min(abs(cy - sy), abs(cy - ey))
                if d < bestd:
                    best, bestd = i, d
            if best is not None and bestd < row_h * 0.6:
                out[best] = (txt, round(float(score), 2))
    return out


def ocr_one(ocr, w):
    big = w.resize((w.width * UP, w.height * UP), Image.LANCZOS)
    res, _ = ocr(np.array(big))
    if not res:
        return None
    txt = " ".join(t for _b, t, _s in res)
    return (txt, round(float(max(s for _b, _t, s in res)), 2))


def main():
    raw = json.load(open(os.path.join(HERE, "ocr_raw.json")))
    doc = pymupdf.open(SRC)
    ocr = RapidOCR()
    result = {}
    txtlines = []
    t0 = time.time()
    for pno_s, rows in raw.items():
        pno = int(pno_s)
        page = doc[pno - 1]
        page_out = []
        # gather all words for this page, keeping (line_idx, word_idx)
        allwords, index = [], []
        for li, r in enumerate(rows):
            crops = line_crops(page, r)
            for wi, (xpt, im) in enumerate(crops):
                allwords.append(im)
                index.append((li, wi, xpt))
        # bucket by height so stacks stay compact
        order = sorted(range(len(allwords)), key=lambda i: allwords[i].height)
        done = [None] * len(allwords)
        B = 20
        for s in range(0, len(order), B):
            chunk = order[s:s + B]
            got = ocr_stack(ocr, [allwords[i] for i in chunk])
            for i, g in zip(chunk, got):
                done[i] = g
        missing = [i for i in range(len(allwords)) if done[i] is None]
        for i in missing:
            done[i] = ocr_one(ocr, allwords[i])
        for li in range(len(rows)):
            ws = [(index[i][2], done[i]) for i in range(len(allwords)) if index[i][0] == li]
            ws.sort()
            page_out.append([[round(x, 1), (t or ""), (sc or 0)]
                             for x, (t, sc) in [(x, (g if g else ("", 0))) for x, g in ws]])
        result[pno_s] = page_out
        for li, ws in enumerate(page_out):
            txtlines.append("p%02d L%-3d %s" % (pno, li, "  ".join(w[1] for w in ws)))
        print("p%s: %d words, %d stacks, %.0fs" %
              (pno_s, len(allwords), (len(allwords) + B - 1) // B, time.time() - t0), flush=True)
    json.dump(result, open(os.path.join(HERE, "ocr_words.json"), "w"), indent=1)
    open(os.path.join(HERE, "source_text_v2.txt"), "w").write("\n".join(txtlines) + "\n")
    print("total %.0fs" % (time.time() - t0))


if __name__ == "__main__":
    main()
