"""Three-part figure-rect audit for Ch8 (per skills/ncert-figure-extraction S4).

A) text-layer word grazing   - prose/caption bleeding into the crop
B) drawings-extent overflow  - vector artwork clipped at an edge
C) border-band ink           - any dark ink just outside the rect

Ch8 is raster-dominant, so B is expected to report "no drawings" for the
photographic plates; C and the eyeball carry the gate there.
"""
import importlib.util

import numpy as np
import pymupdf
from PIL import Image

EF = "notes/class 12/Ch8_MicrobesInHumanWelfare/extract_figures.py"
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
    for w in page.get_text("words"):
        wr = pymupdf.Rect(*w[:4])
        inter = wr & rect
        if inter.is_empty:
            continue
        if inter.get_area() / max(1e-6, wr.get_area()) <= 0.9:
            cut.append(w[4])
    n = sum(1 for w in page.get_text("words")
            if not (pymupdf.Rect(*w[:4]) & rect).is_empty)
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

print("--- B2) raster-image overflow (centre-inside, furniture excluded) ---")
FURN = [(-18.0, -38.9, 586.7, 816.5), (45.7, 191.1, 507.5, 652.9),
        (-21.6, -22.0, 590.5, 75.2)]


def isfurn(b):
    return any(abs(b[0] - f[0]) < 2 and abs(b[1] - f[1]) < 2
               and abs(b[2] - f[2]) < 2 and abs(b[3] - f[3]) < 2 for f in FURN)


for fid, pno, (x0, y0, x1, y1) in ef.FIGS:
    page = doc[pno - 1]
    xs, ys = [], []
    for im in page.get_image_info():
        b = im["bbox"]
        if isfurn(b) or b[2] - b[0] < 3 or b[3] - b[1] < 3:
            continue
        cx, cy = (b[0] + b[2]) / 2, (b[1] + b[3]) / 2
        if not (x0 <= cx <= x1 and y0 <= cy <= y1):
            continue
        xs += [b[0], b[2]]
        ys += [b[1], b[3]]
    if not xs:
        print(f"  fig_{fid}: no rasters (vector figure)")
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
    for side, b in {"L": (x0 - BAND, y0, x0, y1), "R": (x1, y0, x1 + BAND, y1),
                    "T": (x0, y0 - BAND, x1, y0), "B": (x0, y1, x1, y1 + BAND)}.items():
        r = pymupdf.Rect(*b) & page.rect
        if r.is_empty or r.width < 0.5 or r.height < 0.5:
            continue
        pix = page.get_pixmap(clip=r, dpi=DPI)
        a = np.array(Image.frombytes("RGB", (pix.width, pix.height), pix.samples).convert("L"))
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
