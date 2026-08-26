"""Probe ink profiles around a rect edge to find a real whitespace gap.

Usage:
  probe.py <page> <x0> <y0> <x1> <y1> <axis> <lo> <hi>

axis is 'x' (column profile, to place a left/right edge) or 'y' (row profile,
to place a top/bottom edge). lo..hi is the coordinate range to profile, and the
OTHER axis is taken from the rect. Prints ink-pixel counts per point so a run
of zeros identifies a safe edge position.
"""
import sys

import numpy as np
import pymupdf
from PIL import Image

SRC = "Chapter/class 12/Chapter 1 - Sexual Reproduction in Flowering Plants.pdf"
DPI = 150
Z = DPI / 72
DARK = 110


def main():
    pno = int(sys.argv[1])
    x0, y0, x1, y1 = (float(v) for v in sys.argv[2:6])
    axis = sys.argv[6]
    lo, hi = float(sys.argv[7]), float(sys.argv[8])

    doc = pymupdf.open(SRC)
    page = doc[pno - 1]
    if axis == "x":
        r = pymupdf.Rect(lo, y0, hi, y1) & page.rect
    else:
        r = pymupdf.Rect(x0, lo, x1, hi) & page.rect
    pix = page.get_pixmap(clip=r, dpi=DPI)
    a = np.array(Image.frombytes("RGB", (pix.width, pix.height), pix.samples).convert("L"))
    mask = a < DARK
    prof = mask.sum(axis=0) if axis == "x" else mask.sum(axis=1)

    print(f"p{pno} axis={axis} range={lo}..{hi} other=({x0},{y0},{x1},{y1})")
    step = max(1, int(round(Z)))          # ~1 pt buckets
    for i in range(0, len(prof), step):
        v = int(prof[i:i + step].sum())
        coord = lo + i / Z
        bar = "#" * min(40, v)
        print(f"  {coord:7.1f}  {v:5d} {bar}")


if __name__ == "__main__":
    sys.exit(main())
