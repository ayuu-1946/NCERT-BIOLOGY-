#!/usr/bin/env python3
"""Session 1-S helper — second, higher-resolution OCR pass over every line.

The first pass (ocr_raw.json) ran RapidOCR on the whole page at 300 dpi.  At
that scale tightly-kerned words merge ("littleideaaboutthescientific")
and subscript digits collapse to commas.  Re-cropping each detected line and
upscaling 3x before recognition fixes both: at strip scale the recogniser
separates the words and frequently returns the subscript digit correctly.

Two independent OCR passes over the same pixels are the only cross-check
available for a source with no text layer; where they disagree, the line goes
on the manual-review list.

Re-run: /tmp/neetenv/bin/python scratch/ch4inh_gate1/ocr_v2.py
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
UP = 2
SC = DPI / 72.0


def main():
    raw = json.load(open(os.path.join(HERE, "ocr_raw.json")))
    doc = pymupdf.open(SRC)
    ocr = RapidOCR()
    out = {}
    t0 = time.time()
    for pno_s, rows in raw.items():
        pno = int(pno_s)
        page = doc[pno - 1]
        res_lines = []
        for idx, r in enumerate(rows):
            x0, y0, x1, y1 = r[0], r[1], r[2], r[3]
            clip = pymupdf.Rect(max(0, x0 - 3), max(0, y0 - 3), x1 + 3, y1 + 3)
            pix = page.get_pixmap(dpi=DPI, colorspace=pymupdf.csGRAY, clip=clip)
            img = Image.frombytes("L", (pix.width, pix.height), pix.samples)
            img = img.resize((img.width * UP, img.height * UP), Image.LANCZOS)
            res, _ = ocr(np.array(img))
            words = []
            if res:
                for box, txt, score in res:
                    xs = [p[0] for p in box]
                    words.append([round(min(xs) / (SC * UP) + x0 - 3, 1),
                                  txt, round(float(score), 3)])
                words.sort()
            res_lines.append(words)
            print("p%02d L%-3d %d words: %s" %
                  (pno, idx, len(words), " ".join(w[1] for w in words)[:90]),
                  flush=True)
        out[pno_s] = res_lines
    json.dump(out, open(os.path.join(HERE, "ocr_v2.json"), "w"), indent=1)
    print("done in %.1f s" % (time.time() - t0))


if __name__ == "__main__":
    main()
