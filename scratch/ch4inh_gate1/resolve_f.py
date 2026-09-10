#!/usr/bin/env python3
"""Session 1-S helper — read every F-subscript in the chapter off the pixels.

RapidOCR flattens every printed F1 / F2 in the scan to the token "F,".  This
script re-reads each of them: it crops a tight window around the place the
line-level OCR puts the "F", renders it at 400 dpi and upscales 3x, at which
scale the recogniser returns the subscript as its own digit.

It prints one row per occurrence with the reading and its confidence, and marks
anything it could not resolve so the operator can widen the window by hand.
"""
import json
import os
import re
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


def main():
    raw = json.load(open(os.path.join(HERE, "ocr_raw.json")))
    doc = pymupdf.open(SRC)
    ocr = RapidOCR()
    out = []
    for pno_s, rows in raw.items():
        pno = int(pno_s)
        page = doc[pno - 1]
        for idx, r in enumerate(rows):
            hits = [m.start() for m in re.finditer(r"F[,.]", r[4])]
            if not hits:
                continue
            x0, y0, x1, y1 = r[0], r[1], r[2], r[3]
            span = x1 - x0
            n = max(1, len(r[4]))
            readings = []
            for k, hpos in enumerate(hits):
                frac = (hpos + 0.5) / n
                cx = x0 + span * frac
                box = (max(0, cx - 14), max(0, y0 - 3), cx + 26, y1 + 7)
                pix = page.get_pixmap(dpi=DPI, colorspace=pymupdf.csGRAY,
                                      clip=pymupdf.Rect(*box))
                img = Image.frombytes("L", (pix.width, pix.height), pix.samples)
                big = img.resize((img.width * UP, img.height * UP), Image.LANCZOS)
                res, _ = ocr(np.array(big))
                toks = [(t, round(float(s), 2)) for _b, t, s in (res or [])]
                joined = "".join(t for t, _s in toks)
                m = re.search(r"F\s*([0-9])", joined) or re.search(r"F\s*([0-9])",
                                                                   " ".join(t for t, _s in toks))
                readings.append(dict(char=hpos, digit=(m.group(1) if m else None),
                                     toks=toks[:6]))
            out.append(dict(page=pno, line=idx, text=r[4], readings=readings))
            line = " ".join("%s:%s" % (rd["char"], rd["digit"] or "?")
                            for rd in readings)
            print("p%02d L%-3d %-4s %s" % (pno, idx, line, r[4][:70]), flush=True)
    json.dump(out, open(os.path.join(HERE, "f_readings.json"), "w"), indent=1)


if __name__ == "__main__":
    main()
