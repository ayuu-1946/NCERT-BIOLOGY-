#!/usr/bin/env python3
"""Session 1-S helper — find and read page ink the line pass did not cover.

The page-level OCR only returns boxes for text lines it detects.  Displayed
formulas, vertical labels and callouts inside artwork often carry no box at
all, so they never reach the inventory.  This script masks out everything the
line boxes already explain, finds what ink is left over, groups it into
regions, and OCRs each region at high upscale.

Anything it reports has to be checked by hand against the page: a residual band
can also be a rule, a figure border or the page furniture.
"""
import json
import os
import sys

import numpy as np
import pymupdf
from PIL import Image
from rapidocr_onnxruntime import RapidOCR
from scipy import ndimage

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.abspath(os.path.join(HERE, "..", "..", "Chapter", "class 12",
                                   "Chapter 4 - Principles of Inheritance and Variation.pdf"))
DPI = 300
SC = DPI / 72.0
MIN_INK = 400          # residual ink pixels in one component before we bother


def main(pages=None, show_art=False):
    raw = json.load(open(os.path.join(HERE, "ocr_raw.json")))
    doc = pymupdf.open(SRC)
    ocr = RapidOCR()
    for pno_s, rows in raw.items():
        pno = int(pno_s)
        if pages and pno not in pages:
            continue
        page = doc[pno - 1]
        pix = page.get_pixmap(dpi=DPI, colorspace=pymupdf.csGRAY)
        a = np.frombuffer(pix.samples, np.uint8).reshape(pix.height, pix.width)
        ink = a < 140
        mask = np.zeros_like(ink)
        for r in rows:
            x0 = max(0, int((r[0] - 2) * SC)); x1 = min(pix.width, int((r[2] + 2) * SC))
            y0 = max(0, int((r[1] - 2) * SC)); y1 = min(pix.height, int((r[3] + 5) * SC))
            mask[y0:y1, x0:x1] = True
        resid = ink & ~mask
        # ignore the page furniture bands
        resid[:int(60 * SC), :] = False
        resid[int(760 * SC):, :] = False
        lab, n = ndimage.label(resid, structure=np.ones((3, 3)))
        print("########## page %d : %d residual px in %d components" % (pno, resid.sum(), n))
        boxes = []
        for i, sl in enumerate(ndimage.find_objects(lab), start=1):
            arr = (lab[sl] == i)
            if arr.sum() < MIN_INK:
                continue
            boxes.append((sl[1].start, sl[0].start, sl[1].stop, sl[0].stop, int(arr.sum())))
        # merge boxes that are close / overlapping
        merged = []
        for b in sorted(boxes):
            if merged and b[0] <= merged[-1][2] + 20 and abs(b[1] - merged[-1][1]) < 40:
                m = merged[-1]
                merged[-1] = (min(m[0], b[0]), min(m[1], b[1]), max(m[2], b[2]), max(m[3], b[3]),
                              m[4] + b[4])
            else:
                merged.append(b)
        for (x0, y0, x1, y1, area) in merged:
            box = (x0 / SC - 4, y0 / SC - 4, x1 / SC + 4, y1 / SC + 4)
            pix2 = page.get_pixmap(dpi=400, colorspace=pymupdf.csGRAY,
                                   clip=pymupdf.Rect(*box))
            img = Image.frombytes("L", (pix2.width, pix2.height), pix2.samples)
            big = img.resize((img.width * 3, img.height * 3), Image.LANCZOS)
            res, _ = ocr(np.array(big))
            toks = [t for _b, t, _s in (res or [])]
            print("  [%5.0f %5.0f %5.0f %5.0f] area=%-7d %s" %
                  (box[0], box[1], box[2], box[3], area, " | ".join(toks)[:140]))
            if show_art and not toks:
                for row in np.array(img) < 140:
                    print("      " + "".join("#" if v else "." for v in row))


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    main(pages=[int(a) for a in args] if args else None, show_art="--art" in sys.argv)
