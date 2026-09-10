#!/usr/bin/env python3
"""Session 1-S helper — targeted re-OCR of any region of the scanned source.

The chapter PDF is a pure page-image scan (no text layer), so every uncertain
word has to be settled by re-reading the pixels.  This tool re-renders a region
at 400 dpi, upscales 3x, and runs RapidOCR on it; with `--art` it prints the
region as ASCII art instead, which is how subscript/superscript glyphs are read
(this session has no image viewing).

Usage:
  /tmp/neetenv/bin/python scratch/ch4inh_gate1/verify.py line 7 40
  /tmp/neetenv/bin/python scratch/ch4inh_gate1/verify.py region 22 60 400 553 460
  /tmp/neetenv/bin/python scratch/ch4inh_gate1/verify.py art 7 400 420 460 450
  /tmp/neetenv/bin/python scratch/ch4inh_gate1/verify.py line 7 40 --art
Coordinates are PDF points (page space), origin top-left of the page.
"""
import json
import os
import sys

import numpy as np
import pymupdf
from PIL import Image
from rapidocr_onnxruntime import RapidOCR

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.abspath(os.path.join(HERE, "..", "..", "Chapter", "class 12",
                                   "Chapter 4 - Principles of Inheritance and Variation.pdf"))
DPI = 400
UP = 3


def grab(pno, box):
    doc = pymupdf.open(SRC)
    page = doc[pno - 1]
    clip = pymupdf.Rect(*box)
    pix = page.get_pixmap(dpi=DPI, colorspace=pymupdf.csGRAY, clip=clip)
    return Image.frombytes("L", (pix.width, pix.height), pix.samples)


def ocr_img(img):
    ocr = RapidOCR()
    big = img.resize((img.width * UP, img.height * UP), Image.LANCZOS)
    res, _ = ocr(np.array(big))
    return [(t, round(float(s), 2)) for _b, t, s in (res or [])]


def art_img(img, thresh=140):
    a = np.array(img)
    out = []
    for row in a:
        out.append("".join("#" if v < thresh else "." for v in row))
    return "\n".join(out)


def main():
    mode = sys.argv[1]
    if mode == "line":
        pno, idx = int(sys.argv[2]), int(sys.argv[3])
        raw = json.load(open(os.path.join(HERE, "ocr_raw.json")))
        r = raw[str(pno)][idx]
        print("line:", r)
        img = grab(pno, (r[0] - 3, r[1] - 3, r[2] + 3, r[3] + 3))
    elif mode in ("region", "art"):
        pno = int(sys.argv[2])
        box = tuple(float(v) for v in sys.argv[3:7])
        img = grab(pno, box)
    else:
        raise SystemExit(__doc__)
    print("crop px:", img.size)
    if mode == "art" or "--art" in sys.argv:
        print(art_img(img))
        return
    for t, s in ocr_img(img):
        print("%-6.2f %s" % (s, t))


if __name__ == "__main__":
    main()
