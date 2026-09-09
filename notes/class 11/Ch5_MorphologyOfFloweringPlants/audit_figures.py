"""Three-part crop audit for the Ch5 figure assets, plus a print-asset check.

Checks
------
A  text-layer word grazing -- any text-layer word only partly inside the rect.
B  drawings-extent overflow -- vector rects whose centre is inside the rect but
   whose edges spill outside. **Unreliable on these pages**: NCERT's diagonal
   "not to be republished" watermark and the (c) mark are vector artwork drawn
   across the whole page, so their strokes are attributed to whichever figure
   they happen to sit behind. Kept for continuity with the earlier audit, and
   adjudicated by B2.
B2 ink-extent overflow -- the authoritative version of B. Measures *dark* ink
   (< DARK_INK) in a band just outside the rect, ignoring the printed caption's
   own words. The watermark renders around grey 230-245, so thresholding
   separates real clipped artwork from watermark strokes.
C  border-band ink -- dark pixels in the border band that are not accounted for
   by a text-layer word.
D  print-asset check -- every emitted PNG is single-channel `mode=L` at 300 dpi.

Known blind spot (recorded as a Gate 1 carry-over): checks A and C both discount
text-layer words, so **neither can see a clipped in-figure label** -- exactly the
Fig 5.2 `Laterals` defect that the inherited audit passed as clean. Only opening
every rendered asset and reading it catches that class, which is why section 4.4
Step 3 makes the visual pass mandatory rather than optional.
"""
import importlib.util
import os

import numpy as np
import pymupdf
from PIL import Image

SPEC = "notes/class 11/Ch5_MorphologyOfFloweringPlants/extract_figures.py"
DPI = 150
BAND = 6.0
DARK = 110
DARK_INK = 215

spec = importlib.util.spec_from_file_location("ef", SPEC)
ef = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ef)
doc = pymupdf.open(ef.SRC)
z = DPI / 72


print("--- A) text-layer word grazing ---")
for fid, pno, (x0, y0, x1, y1) in ef.FIGS:
    page = doc[pno - 1]
    rect = pymupdf.Rect(x0, y0, x1, y1)
    cut, inside = [], []
    # Rotated spans belong to the watermark layer and do not render in place; a
    # rotated glyph clipped by the rect is not a clipped figure label.
    rotated = set()
    for block in page.get_text("dict")["blocks"]:
        for line in block.get("lines", []):
            if abs(line["dir"][1]) > 1e-6:
                rotated.update(s["text"].strip() for s in line["spans"] if s["text"].strip())
    for w in page.get_text("words"):
        wr = pymupdf.Rect(*w[:4])
        inter = wr & rect
        if inter.is_empty:
            continue
        inside.append(w[4])
        if inter.get_area() / max(1e-6, wr.get_area()) <= 0.9 and w[4] not in rotated:
            cut.append(w[4])
    print(f"fig_{fid}: words_in_rect={len(inside)}" + (f" GRAZING {cut}" if cut else " ok"))


print("--- B) drawings-extent overflow (watermark-polluted; adjudicated by B2) ---")
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
        print(f"fig_{fid}: no drawings (raster/text image)")
        continue
    ov = [max(0, x0 - min(xs)), max(0, y0 - min(ys)), max(0, max(xs) - x1), max(0, max(ys) - y1)]
    verdict = f"OVERFLOW L{ov[0]:.1f} T{ov[1]:.1f} R{ov[2]:.1f} B{ov[3]:.1f}" if max(ov) > 3 else "ok"
    print(f"fig_{fid}: {verdict}")


print("--- B2) ink-extent overflow (authoritative) ---")
for fid, pno, (x0, y0, x1, y1) in ef.FIGS:
    page = doc[pno - 1]
    words = [pymupdf.Rect(*w[:4]) for w in page.get_text("words")]
    hits = []
    bands = {
        "L": (x0 - BAND, y0, x0, y1),
        "R": (x1, y0, x1 + BAND, y1),
        "T": (x0, y0 - BAND, x1, y0),
        "B": (x0, y1, x1, y1 + BAND),
    }
    for side, b in bands.items():
        r = pymupdf.Rect(*b) & page.rect
        if r.is_empty or r.width < 0.5 or r.height < 0.5:
            continue
        pix = page.get_pixmap(clip=r, dpi=DPI)
        arr = np.array(Image.frombytes("RGB", (pix.width, pix.height), pix.samples).convert("L"))
        keep = 0
        for py, px in zip(*np.nonzero(arr < DARK_INK)):
            X, Y = r.x0 + px / z, r.y0 + py / z
            if any(w.x0 - 1 <= X <= w.x1 + 1 and w.y0 - 1 <= Y <= w.y1 + 1 for w in words):
                continue
            keep += 1
        if keep > 40:
            hits.append(f"{side}:{keep}px")
    print(f"fig_{fid}: " + (f"INK-OUTSIDE {hits}" if hits else "clean"))


print("--- C) unexplained dark ink in border band ---")
for fid, pno, (x0, y0, x1, y1) in ef.FIGS:
    page = doc[pno - 1]
    words = [pymupdf.Rect(*w[:4]) for w in page.get_text("words")]
    hits = []
    bands = {
        "L": (x0 - BAND, y0, x0, y1),
        "R": (x1, y0, x1 + BAND, y1),
        "T": (x0, y0 - BAND, x1, y0),
        "B": (x0, y1, x1, y1 + BAND),
    }
    for side, b in bands.items():
        r = pymupdf.Rect(*b) & page.rect
        if r.is_empty or r.width < 0.5 or r.height < 0.5:
            continue
        pix = page.get_pixmap(clip=r, dpi=DPI)
        arr = np.array(Image.frombytes("RGB", (pix.width, pix.height), pix.samples).convert("L"))
        keep, sample = 0, None
        for py, px in zip(*np.nonzero(arr < DARK)):
            X, Y = r.x0 + px / z, r.y0 + py / z
            if any(w.x0 - 1 <= X <= w.x1 + 1 and w.y0 - 1 <= Y <= w.y1 + 1 for w in words):
                continue
            keep += 1
            sample = sample or (round(X, 1), round(Y, 1))
        if keep > 40:
            hits.append(f"{side}:{keep}px@{sample}")
    print(f"fig_{fid}: " + (f"EDGE-INK {hits}" if hits else "clean"))


print("--- D) print-asset check (mode / dpi) ---")
for fid, _, _ in ef.FIGS:
    im = Image.open(os.path.join(os.path.dirname(SPEC), "assets", f"fig_{fid}.png"))
    dpi = tuple(round(v) for v in im.info.get("dpi", (0, 0)))
    ok = "ok" if im.mode == "L" and dpi == (300, 300) else "CHECK"
    print(f"fig_{fid}: mode={im.mode} dpi={dpi} size={im.size} {ok}")
