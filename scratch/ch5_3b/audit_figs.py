"""Three-part figure-crop audit (skill: in-repo-ncert-figure-extraction, step 4)
for Ch5 MBI.  A) text-layer word grazing  B) drawings-extent overflow
C) unexplained dark ink in the 6pt border band.
Run: /vercel/share/neetenv/bin/python scratch/ch5_3b/audit_figs.py
"""
import importlib.util

import numpy as np
import pymupdf
from PIL import Image

EF = "notes/class 12/Ch5_MolecularBasisOfInheritance/extract_figures.py"
spec = importlib.util.spec_from_file_location("ef", EF)
ef = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ef)

doc = pymupdf.open(ef.SRC)
DPI = 150
z = DPI / 72
BAND = 6.0
DARK = 110

print("--- A) text-layer word grazing ---")
for fid, pno, (x0, y0, x1, y1) in ef.FIGS:
    page = doc[pno - 1]
    rect = pymupdf.Rect(x0, y0, x1, y1)
    cut = []
    words = page.get_text("words")
    for w in words:
        wr = pymupdf.Rect(*w[:4])
        inter = wr & rect
        if inter.is_empty:
            continue
        if inter.get_area() / max(1e-6, wr.get_area()) <= 0.9:
            cut.append(w[4])
    n = sum(1 for w in words if not (pymupdf.Rect(*w[:4]) & rect).is_empty)
    print(f"  fig_{fid}: words_in_rect={n}" + (f" GRAZING {cut}" if cut else " ok"))

print("--- B) drawings-extent overflow ---")
for fid, pno, (x0, y0, x1, y1) in ef.FIGS:
    page = doc[pno - 1]
    xs, ys = [], []
    for d in page.get_drawings():
        r = d["rect"]
        if r.width <= 0.2 or r.height <= 0.2 or r.width > 480 or r.height > 420:
            continue
        cx, cy = (r.x0 + r.x1) / 2, (r.y0 + r.y1) / 2
        if not (x0 <= cx <= x1 and y0 <= cy <= y1):
            continue
        xs += [r.x0, r.x1]
        ys += [r.y0, r.y1]
    if not xs:
        print(f"  fig_{fid}: no drawings (raster figure)")
        continue
    ov = [max(0, x0 - min(xs)), max(0, y0 - min(ys)),
          max(0, max(xs) - x1), max(0, max(ys) - y1)]
    print(f"  fig_{fid}: " + (f"OVERFLOW L{ov[0]:.1f} T{ov[1]:.1f} R{ov[2]:.1f} B{ov[3]:.1f}"
                              if max(ov) > 3 else "ok"))

print("--- C) unexplained dark ink in border band ---")
for fid, pno, (x0, y0, x1, y1) in ef.FIGS:
    page = doc[pno - 1]
    words = [pymupdf.Rect(*w[:4]) for w in page.get_text("words")]
    hits = []
    bands = {"L": (x0 - BAND, y0, x0, y1), "R": (x1, y0, x1 + BAND, y1),
             "T": (x0, y0 - BAND, x1, y0), "B": (x0, y1, x1, y1 + BAND)}
    for side, b in bands.items():
        r = pymupdf.Rect(*b) & page.rect
        if r.is_empty or r.width < 0.5 or r.height < 0.5:
            continue
        pix = page.get_pixmap(clip=r, dpi=DPI)
        a = np.array(Image.frombytes("RGB", (pix.width, pix.height),
                                     pix.samples).convert("L"))
        keep = 0
        sample = None
        for py, px in zip(*np.nonzero(a < DARK)):
            X = r.x0 + px / z
            Y = r.y0 + py / z
            if any(w.x0 - 1 <= X <= w.x1 + 1 and w.y0 - 1 <= Y <= w.y1 + 1 for w in words):
                continue
            keep += 1
            if sample is None:
                sample = (round(X, 1), round(Y, 1))
        if keep > 40:
            hits.append(f"{side}:{keep}px@{sample}")
    print(f"  fig_{fid}: " + (f"EDGE-INK {hits}" if hits else "clean"))
