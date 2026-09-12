"""Ch3 Reproductive Health - mandatory three-part crop audit (skill §4).

A) text-layer word grazing   B) dark-ink extent overflow (supersedes the
get_drawings() union per LEARNINGS.md - NCERT's page watermark is vector art and
mis-measures unions)   C) unexplained dark ink in the 6pt border band.
"""
import importlib.util
import os
import sys

import numpy as np
import pymupdf
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("ef", os.path.join(HERE, "extract_figures.py"))
ef = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ef)

doc = pymupdf.open(ef.SRC)
DPI = 150
Z = DPI / 72
BAND = 6.0
DARK = 110
INK_THR = 215


def ink_bbox(page, rect, thr=INK_THR):
    r = pymupdf.Rect(*rect) & page.rect
    pix = page.get_pixmap(clip=r, dpi=DPI, alpha=False)
    a = np.array(Image.frombytes("RGB", (pix.width, pix.height), pix.samples).convert("L"))
    ys, xs = np.nonzero(a < thr)
    if len(xs) == 0:
        return None
    return (r.x0 + xs.min() / Z, r.y0 + ys.min() / Z, r.x0 + xs.max() / Z, r.y0 + ys.max() / Z)


print("--- A) text-layer word grazing (words crossing a rect edge) ---")
for fid, pno, rect, _ in ef.FIGS:
    page = doc[pno - 1]
    r = pymupdf.Rect(*rect)
    cut, inside = [], []
    for w in page.get_text("words"):
        wr = pymupdf.Rect(*w[:4])
        inter = wr & r
        if inter.is_empty:
            continue
        f = inter.get_area() / max(1e-6, wr.get_area())
        (inside if f > 0.9 else cut).append(f"{w[4]}({f:.2f})")
    print(f"  fig_{fid}: words_inside={len(inside)} {inside} | GRAZING {cut}" if cut
          else f"  fig_{fid}: words_inside={len(inside)} {inside} | no grazing")

print("--- B) dark-ink extent overflow ---")
for fid, pno, rect, _ in ef.FIGS:
    page = doc[pno - 1]
    x0, y0, x1, y1 = rect
    ib = ink_bbox(page, (x0 - 1, y0 - 1, x1 + 1, y1 + 1))
    if ib is None:
        print(f"  fig_{fid}: NO INK in/near rect (!!)")
        continue
    ov = (max(0, x0 - ib[0]), max(0, y0 - ib[1]), max(0, ib[2] - x1), max(0, ib[3] - y1))
    print(f"  fig_{fid}: ink bbox=({ib[0]:.1f},{ib[1]:.1f},{ib[2]:.1f},{ib[3]:.1f}) "
          + (f"OVERFLOW L{ov[0]:.1f} T{ov[1]:.1f} R{ov[2]:.1f} B{ov[3]:.1f}" if max(ov) > 3 else "ok (>=3pt margin all round)"))

print("--- C) unexplained dark ink in the 6pt border band ---")
for fid, pno, rect, _ in ef.FIGS:
    page = doc[pno - 1]
    x0, y0, x1, y1 = rect
    words = [pymupdf.Rect(*w[:4]) for w in page.get_text("words")]
    hits = []
    for side, b in {"L": (x0 - BAND, y0, x0, y1), "R": (x1, y0, x1 + BAND, y1),
                    "T": (x0, y0 - BAND, x1, y0), "B": (x0, y1, x1, y1 + BAND)}.items():
        r = pymupdf.Rect(*b) & page.rect
        if r.is_empty or r.width < 0.5 or r.height < 0.5:
            continue
        pix = page.get_pixmap(clip=r, dpi=DPI, alpha=False)
        a = np.array(Image.frombytes("RGB", (pix.width, pix.height), pix.samples).convert("L"))
        keep, sample, mags = 0, None, []
        for py, px in zip(*np.nonzero(a < DARK)):
            X, Y = r.x0 + px / Z, r.y0 + py / Z
            if any(w.x0 - 1 <= X <= w.x1 + 1 and w.y0 - 1 <= Y <= w.y1 + 1 for w in words):
                continue
            keep += 1
            mags.append(int(a[py, px]))
            if sample is None:
                sample = (round(X, 1), round(Y, 1))
        if keep > 40:
            hits.append(f"{side}:{keep}px@{sample} min={min(mags)}")
    print(f"  fig_{fid}: " + (f"EDGE-INK {hits}" if hits else "clean"))
