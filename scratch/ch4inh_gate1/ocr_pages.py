#!/usr/bin/env python3
"""Session 1-S helper — OCR the scanned Ch4 source PDF.

The source PDF `Chapter/class 12/Chapter 4 - Principles of Inheritance and
Variation.pdf` is a pure page-image scan: 28 pages, every page a single
1105x1482 DeviceRGB raster, `page.get_text()` returns '' on every page.

So there is no text layer to read. Every subsequent Pass-1 step is built on
this OCR output. Re-run with:

    /tmp/neetenv/bin/python scratch/ch4inh_gate1/ocr_pages.py

Output: scratch/ch4inh_gate1/ocr_raw.json  -> {page: [[x0,y0,x1,y1,text,score], ...]}
Coordinates are in PDF points (page space), converted from the render dpi.
"""
import json
import os
import sys

import pymupdf
from rapidocr_onnxruntime import RapidOCR

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.abspath(os.path.join(HERE, "..", "..", "Chapter", "class 12",
                                   "Chapter 4 - Principles of Inheritance and Variation.pdf"))
OUT = os.path.join(HERE, "ocr_raw.json")
DPI = 300

PAGE_FURNITURE = {
    "BIOLOGY", "Reprint 2026-27", "Reprint2026-27", "2026-27",
}


def main():
    doc = pymupdf.open(SRC)
    ocr = RapidOCR()
    scale = 72.0 / DPI  # px -> pt
    out = {}
    for i, page in enumerate(doc):
        pno = i + 1
        pix = page.get_pixmap(dpi=DPI, colorspace=pymupdf.csGRAY)
        tmp = "/tmp/ch4_p%02d.png" % pno
        pix.save(tmp)
        res, _ = ocr(tmp)
        rows = []
        if res:
            for box, txt, score in res:
                xs = [p[0] for p in box]
                ys = [p[1] for p in box]
                x0, x1 = min(xs) * scale, max(xs) * scale
                y0, y1 = min(ys) * scale, max(ys) * scale
                rows.append([round(x0, 1), round(y0, 1), round(x1, 1), round(y1, 1),
                             txt, round(float(score), 3)])
        rows.sort(key=lambda r: (r[1], r[0]))
        out[str(pno)] = rows
        print("p%02d  %d lines" % (pno, len(rows)), file=sys.stderr)
    with open(OUT, "w") as fh:
        json.dump(out, fh, indent=1)
    print("wrote", OUT, "pages:", len(out))


if __name__ == "__main__":
    main()
