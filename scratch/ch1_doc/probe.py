"""Ink-band probe for re-pinning Ch1 rects on a scanned page.

Usage:
  probe.py page x0 y0 x1 y1 [pad] [minink]

Prints contiguous ink bands (rows, then columns) inside a window that extends
`pad` pt beyond the rect on every side, with the rect's own edges marked. A
band list makes the whitespace gutters explicit, so an edge can be re-pinned by
number instead of by eye on a scanned page with no text layer.
"""
import sys

import numpy as np
import pymupdf
from PIL import Image

SRC = "Chapter/class 12/Chapter 1 - Sexual Reproduction in Flowering Plants.pdf"
DPI = 150
Z = DPI / 72
DARK = 110


def bands(profile, origin, minink):
    out = []
    run = None
    for i, n in enumerate(profile):
        if n >= minink:
            if run is None:
                run = [i, i, int(n)]
            else:
                run[1] = i
                run[2] = max(run[2], int(n))
        elif run is not None:
            out.append(run)
            run = None
    if run is not None:
        out.append(run)
    return [(origin + a / Z, origin + b / Z, peak) for a, b, peak in out]


def main():
    pno = int(sys.argv[1])
    x0, y0, x1, y1 = (float(v) for v in sys.argv[2:6])
    pad = float(sys.argv[6]) if len(sys.argv) > 6 else 20.0
    minink = int(sys.argv[7]) if len(sys.argv) > 7 else 2
    doc = pymupdf.open(SRC)
    page = doc[pno - 1]
    win = pymupdf.Rect(x0 - pad, y0 - pad, x1 + pad, y1 + pad) & page.rect
    pix = page.get_pixmap(clip=win, dpi=DPI)
    a = np.array(Image.frombytes("RGB", (pix.width, pix.height), pix.samples).convert("L"))
    mask = a < DARK
    print(f"page {pno} rect ({x0}, {y0}, {x1}, {y1})  window {tuple(round(v, 1) for v in win)}")
    print(f"minink={minink} px/line at {DPI} dpi")

    print(f"--- ink bands along y (rect y0={y0} y1={y1}) ---")
    for a0, a1, peak in bands(mask.sum(axis=1), win.y0, minink):
        tags = []
        if a0 <= y0 <= a1:
            tags.append("straddles y0")
        if a0 <= y1 <= a1:
            tags.append("straddles y1")
        print(f"  y {a0:7.1f} .. {a1:7.1f}  peak {peak:5d}  {' '.join(tags)}")

    print(f"--- ink bands along x (rect x0={x0} x1={x1}) ---")
    for a0, a1, peak in bands(mask.sum(axis=0), win.x0, minink):
        tags = []
        if a0 <= x0 <= a1:
            tags.append("straddles x0")
        if a0 <= x1 <= a1:
            tags.append("straddles x1")
        print(f"  x {a0:7.1f} .. {a1:7.1f}  peak {peak:5d}  {' '.join(tags)}")


if __name__ == "__main__":
    sys.exit(main())
