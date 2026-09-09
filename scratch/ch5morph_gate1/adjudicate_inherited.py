"""Adjudicate the *inherited* Ch5 crop rectangles by machine.

The re-pin log must state which inherited rectangles genuinely clipped something,
and the count must be derived rather than asserted. The first draft of that log
was wrong in both directions: it claimed "14 of 17" while listing 16 defect IDs,
and it recorded a Fig 5.14 defect (D11) inferred from the very watermark-polluted
`get_drawings()` union that this session went on to reject.

Method, per figure, for a given rectangle:
  * content extent = dark-ink bbox (< 215, so the grey 230-245 watermark is
    excluded) over a generous band around the plate, unioned with the bboxes of
    the plate's raster images (a photo's light background makes ink under-report
    its edge) and of the text-layer words that are the plate's labels or panel
    markers (a label cropped away entirely leaves no ink inside the rect).
  * a rectangle CLIPS if the content extent is not contained in it. The printed
    caption is excluded from the content extent, since the standard is that the
    caption is typeset by the script.

Run from the repository root:
    /vercel/share/neetenv/bin/python scratch/ch5morph_gate1/adjudicate_inherited.py
"""
import importlib.util
import re

import numpy as np
import pymupdf
from PIL import Image

SRC = "Chapter/class 11/Chapter 05 - Morphology of Flowering Plants.pdf"
EXTRACT = "notes/class 11/Ch5_MorphologyOfFloweringPlants/extract_figures.py"
DPI = 200
DARK_INK = 215

# The rectangles inherited from the previous figure-extraction task (git HEAD).
INHERITED = {
    "5.1": (4, (78, 95, 315, 405)),
    "5.2": (4, (78, 420, 555, 665)),
    "5.3": (5, (285, 112, 520, 345)),
    "5.4": (6, (45, 95, 278, 435)),
    "5.5": (6, (45, 505, 265, 750)),
    "5.6": (7, (275, 85, 505, 335)),
    "5.7": (7, (275, 405, 515, 675)),
    "5.8": (8, (50, 95, 278, 245)),
    "5.9": (8, (62, 480, 515, 660)),
    "5.10": (9, (42, 565, 510, 685)),
    "5.11": (10, (125, 95, 475, 305)),
    "5.12": (11, (378, 85, 520, 735)),
    "5.13": (12, (188, 90, 505, 265)),
    "5.14": (12, (48, 465, 285, 605)),
    "5.15": (13, (72, 90, 485, 345)),
    "5.16": (13, (335, 445, 515, 710)),
    "5.17": (14, (102, 455, 475, 690)),
}

# Generous search band per figure: the page region the plate lives in, bounded by
# its neighbours (page header, adjacent prose column, the next plate).
BANDS = {
    "5.1": (60, 82, 328, 409),
    "5.2": (45, 428, 552, 684),
    "5.3": (280, 82, 545, 336),
    "5.4": (44, 82, 278, 459),
    "5.5": (44, 506, 281, 677),
    "5.6": (270, 80, 545, 334),
    "5.7": (268, 400, 545, 688),
    "5.8": (40, 80, 286, 240),
    "5.9": (58, 474, 545, 680),
    "5.10": (36, 567, 545, 694),
    "5.11": (118, 80, 480, 311),
    "5.12": (370, 80, 540, 632),
    "5.13": (185, 80, 494, 245),
    "5.14": (40, 470, 302, 616),
    "5.15": (55, 80, 500, 309),
    "5.16": (328, 448, 552, 686),
    "5.17": (95, 448, 480, 688),
}

doc = pymupdf.open(SRC)
spec = importlib.util.spec_from_file_location("ef", EXTRACT)
ef = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ef)
CURRENT = {fid.replace("_", "."): (pno, tuple(rect)) for fid, pno, rect in ef.FIGS}


def content_extent(fig: str) -> pymupdf.Rect:
    """Ink bbox unioned with the plate's raster image bboxes.

    Text-layer word bboxes are deliberately *not* unioned in. Text renders as ink,
    so the ink bbox already covers every label -- including one that the rect crops
    away, because the extent is measured over a band chosen independently of the
    rect. Unioning words as well only drags in the neighbouring prose column (it put
    Fig 5.1's extent at x=330.0, the left edge of page 4's right-hand column) and the
    rotated, non-rendering watermark duplicate `(a)` on page 11.
    """
    pno, _ = INHERITED[fig]
    page = doc[pno - 1]
    band = pymupdf.Rect(*BANDS[fig])
    scale = DPI / 72.0

    pix = page.get_pixmap(clip=band, dpi=DPI, alpha=False)
    img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples).convert("L")
    arr = np.array(img)
    ys, xs = np.nonzero(arr < DARK_INK)
    ext = None
    if len(xs):
        ext = pymupdf.Rect(
            band.x0 + xs.min() / scale, band.y0 + ys.min() / scale,
            band.x0 + xs.max() / scale, band.y0 + ys.max() / scale,
        )

    # A photograph's light background makes ink under-report its true edge, so union
    # the raster image bboxes that lie wholly inside the band.
    for info in page.get_image_info():
        r = pymupdf.Rect(info["bbox"])
        if r.is_empty or not band.contains(r):
            continue
        ext = r if ext is None else ext | r
    return ext


print(f"{'Fig':>5}  {'inherited rect':>26}  {'content extent':>28}  clipped by (pt)")
print("-" * 96)
clipped, clean = [], []
for fig in sorted(INHERITED, key=lambda f: float(f)):
    _, rect = INHERITED[fig]
    r = pymupdf.Rect(*rect)
    ext = content_extent(fig)
    over = {
        "L": round(max(0.0, r.x0 - ext.x0), 1),
        "T": round(max(0.0, r.y0 - ext.y0), 1),
        "R": round(max(0.0, ext.x1 - r.x1), 1),
        "B": round(max(0.0, ext.y1 - r.y1), 1),
    }
    bad = {k: v for k, v in over.items() if v > 0.5}
    verdict = ", ".join(f"{k}{v}" for k, v in bad.items()) if bad else "-- clean --"
    (clipped if bad else clean).append(fig)
    ex = f"({ext.x0:.1f}, {ext.y0:.1f}, {ext.x1:.1f}, {ext.y1:.1f})"
    print(f"{fig:>5}  {str(rect):>26}  {ex:>28}  {verdict}")

print()
print(f"inherited rects that CLIPPED artwork/labels: {len(clipped)} of {len(INHERITED)}"
      f"  -> {', '.join(sorted(clipped, key=float))}")
print(f"inherited rects clean on the artwork test:   {len(clean)} of {len(INHERITED)}"
      f"  -> {', '.join(sorted(clean, key=float))}")

# A caption cut through its own glyph row is a separate defect family: the artwork
# is intact, but the plate prints half a line of type.
print()
print("--- inherited rects that cut the printed caption through its glyph row ---")
cap_cut = []
for fig in sorted(INHERITED, key=float):
    pno, rect = INHERITED[fig]
    r = pymupdf.Rect(*rect)
    page = doc[pno - 1]
    for block in page.get_text("dict")["blocks"]:
        for line in block.get("lines", []):
            txt = "".join(sp["text"] for sp in line["spans"]).strip()
            if not re.match(rf"Figure\s+{re.escape(fig)}\b", txt):
                continue
            cr = pymupdf.Rect(*line["bbox"])
            inter = cr & r
            if not inter.is_empty and inter.get_area() / cr.get_area() < 0.98:
                frac = inter.get_area() / cr.get_area()
                cap_cut.append(fig)
                print(f"  {fig:>5}  caption {[round(v, 1) for v in cr]}  "
                      f"only {frac * 100:.0f}% inside the rect")
print(f"  -> {len(cap_cut)} of {len(INHERITED)}: {', '.join(cap_cut) or '(none)'}")

both = sorted(set(clipped) | set(cap_cut), key=float)
print()
print(f"TOTAL inherited rects with at least one defect: {len(both)} of {len(INHERITED)}"
      f"  -> {', '.join(both)}")
print(f"TOTAL inherited rects fully clean:              "
      f"{len(INHERITED) - len(both)} of {len(INHERITED)}"
      f"  -> {', '.join(f for f in sorted(INHERITED, key=float) if f not in both)}")

print()
print("--- same test applied to the CURRENT rects (must be clean for all) ---")
still = []
for fig in sorted(CURRENT, key=lambda f: float(f)):
    r = pymupdf.Rect(*CURRENT[fig][1])
    ext = content_extent(fig)
    over = max(r.x0 - ext.x0, r.y0 - ext.y0, ext.x1 - r.x1, ext.y1 - r.y1)
    if over > 0.5:
        still.append((fig, round(over, 1)))
print(f"current rects that clip content: {len(still)}  {still or '(none)'}")
