"""Figure-rect audit for Ch7 Human Health and Disease.

Re-derivation of session 1-F's extraction gate (skills/ncert-figure-extraction S4).
The prior session's audit script was not committed, so this rebuilds it from the
reference implementation (scratch/ch8_figs/audit.py) with the two Ch7-specific
additions that chapter's extract_figures.py documents:

  A)  text-layer word grazing    - prose/caption bleeding into the crop
  B)  drawings-extent overflow   - vector artwork clipped at an edge
  B2) raster-image overflow      - photographic plates clipped at an edge
                                   (Ch7 has 4 pure photos; B alone reports
                                   "no drawings" and would leave them unchecked)
  C)  border-band ink, DARK      - grey < 110, the skill's standard threshold
  C2) border-band ink, LIGHT     - grey < 205.  REQUIRED for this chapter: the
                                   fig 7.10 cannabis leaf is mid-green (luma
                                   ~177) inside a pale grey frame, so the whole
                                   plate sits ABOVE the dark threshold and C
                                   passed while the crop was clipping the frame.

Page furniture is excluded from every extent/ink measurement, otherwise the
watermark and header band swamp the result.  Ch7's furniture, as measured:
  - dark green header band, y < 76
  - "(c) NCERT / not to be republished" watermark raster ~(46, 191, 508, 653),
    present on EVERY page
  - brown/orange corner motifs, right-margin decorative band
  - the orange page-number tab

Run:
  /vercel/share/neetenv/bin/python scratch/ch7_figs/audit.py
"""
import importlib.util

import numpy as np
import pymupdf
from PIL import Image

EF = "notes/class 12/Ch7_HumanHealthAndDisease/extract_figures.py"
spec = importlib.util.spec_from_file_location("ef", EF)
ef = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ef)

doc = pymupdf.open(ef.SRC)
DPI = 150
z = DPI / 72
BAND = 6.0
DARK = 110
LIGHT = 205

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
    inside = [w[4] for w in page.get_text("words")
              if not (pymupdf.Rect(*w[:4]) & rect).is_empty]
    tag = f" GRAZING {cut}" if cut else (" VACUOUS (0 words)" if not inside else " ok")
    print(f"  fig_{fid}: words_in_rect={len(inside)}{tag} {inside[:8]}")

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


def isfurn(b):
    """Watermark raster: spans most of the page, present on every page."""
    return (b[2] - b[0]) > 400 and (b[3] - b[1]) > 400


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


print("--- B3) raster-TILE union overflow (no size floor) ---")
# REQUIRED for Ch7.  figs 7.8 and 7.11 are rendered as thousands of sub-pixel
# scanline tiles (~6 x 0.2 pt each), so B reports 0 drawings and B2's 3 pt size
# floor discards every tile -> both checks are VACUOUS for those two plates and
# they would otherwise have no mechanical edge check at all.  This drops the
# size floor and unions every non-furniture tile whose centre is in the rect.
for fid, pno, (x0, y0, x1, y1) in ef.FIGS:
    page = doc[pno - 1]
    xs, ys, n = [], [], 0
    for im in page.get_image_info():
        b = im["bbox"]
        if isfurn(b):
            continue
        cx, cy = (b[0] + b[2]) / 2, (b[1] + b[3]) / 2
        if not (x0 <= cx <= x1 and y0 <= cy <= y1):
            continue
        n += 1
        xs += [b[0], b[2]]
        ys += [b[1], b[3]]
    if not xs:
        print(f"  fig_{fid}: no tiles at all (pure vector)")
        continue
    ov = [max(0, x0 - min(xs)), max(0, y0 - min(ys)),
          max(0, max(xs) - x1), max(0, max(ys) - y1)]
    ext = "x %.1f-%.1f y %.1f-%.1f" % (min(xs), max(xs), min(ys), max(ys))
    verdict = ("OVERFLOW L%.1f T%.1f R%.1f B%.1f" % tuple(ov)) if max(ov) > 3 else "ok"
    print(f"  fig_{fid}: tiles={n:5d} extent {ext} -> {verdict}")


def band_ink(thr, minpx):
    for fid, pno, (x0, y0, x1, y1) in ef.FIGS:
        page = doc[pno - 1]
        words = [pymupdf.Rect(*w[:4]) for w in page.get_text("words")]
        hits = []
        for side, b in {"L": (x0 - BAND, y0, x0, y1), "R": (x1, y0, x1 + BAND, y1),
                        "T": (x0, y0 - BAND, x1, y0),
                        "B": (x0, y1, x1, y1 + BAND)}.items():
            r = pymupdf.Rect(*b) & page.rect
            if r.is_empty or r.width < 0.5 or r.height < 0.5:
                continue
            pix = page.get_pixmap(clip=r, dpi=DPI)
            a = np.array(
                Image.frombytes("RGB", (pix.width, pix.height), pix.samples).convert("L"))
            keep = 0
            sample = None
            for py, px in zip(*np.nonzero(a < thr)):
                X = r.x0 + px / z
                Y = r.y0 + py / z
                if any(w.x0 - 1 <= X <= w.x1 + 1 and w.y0 - 1 <= Y <= w.y1 + 1
                       for w in words):
                    continue
                keep += 1
                if sample is None:
                    sample = (round(X, 1), round(Y, 1))
            if keep > minpx:
                hits.append(f"{side}:{keep}px@{sample}")
        print(f"  fig_{fid}: " + (f"EDGE-INK {hits}" if hits else "clean"))


print(f"--- C) unexplained DARK ink in border band (grey<{DARK}) ---")
band_ink(DARK, 40)
print(f"--- C2) unexplained LIGHT ink in border band (grey<{LIGHT}) ---")
band_ink(LIGHT, 40)
