"""Figure extraction for Class 12 Ch1 - Sexual Reproduction in Flowering Plants.

SOURCE IS A RASTER SCAN. Unlike Ch5, this PDF has NO text layer and NO vector
drawings: every page is a single full-page image (1105x1482 px, ~130 dpi
native). Consequences for the skill's three-part audit:

  * Check A (text-layer word grazing) is VACUOUS -- page.get_text("words")
    returns [] on every page.
  * Check B (drawings-extent overflow) is VACUOUS -- page.get_drawings()
    returns [] on every page.
  * Check C (border-band ink) still works, and is extended in audit_figures.py
    by an ink-projection check that measures the tight ink bbox INSIDE each
    rect and asserts a whitespace margin on all four sides. That margin is
    what proves nothing was clipped, since B cannot say so here.

Rects are in PDF points. Pages 1-20 and 22-25 are 612.0 x 820.8; page 21 is
595.4 x 842.4 (A4) -- do not reuse a page-20 x-coordinate on page 21.

Conventions for this chapter:
  * Captions ARE included in the crop (the "Figure 1.N ..." line sits inside
    the rect), so an asset is self-describing.
  * The chapter-opening plate on p3 is deliberately NOT extracted -- it is
    decorative heading artwork, not a numbered figure.
  * The Panchanan Maheshwari portrait on p2 is NOT extracted -- it belongs to
    the biography sidebar, not the figure sequence.
  * Multi-panel plates: the full plate is always emitted. Sub-panels are
    additionally emitted ONLY where the panels are cleanly separable, i.e.
    physically gapped with no leader line, arrow, or label straddling the
    boundary. Plates 1.2, 1.3, 1.7, 1.8 and 1.13 are therefore NOT split --
    their panels share label columns or are joined by flow arrows.
"""

import os
import sys

import pymupdf
from PIL import Image, ImageOps

SRC = "Chapter/class 12/Chapter 1 - Sexual Reproduction in Flowering Plants.pdf"
OUT_DIR = "notes/class 12/Ch1_SexualReproductionInFloweringPlants/assets"
RENDER_DPI = 300

# (asset_id, 1-indexed page, (x0, y0, x1, y1))
FIGS = [
    # ---- full plates -------------------------------------------------------
    # p4: single centred diagram. x0=180 clears the "Style" leader label
    # (starts x~184); x1=545 clears "Filament" (ends x~540). y1=445 keeps the
    # one-line caption (y~433-440) and stops above the italic body text at
    # y~455.
    ("1_1", 4, (180, 98, 545, 445)),
    # p5: figure sits in the RIGHT column beside prose. x0=310 is the binding
    # constraint -- the left text column's longest line ends at x~308, so this
    # clips just inside it. Caption block runs y~494-524, hence y1=532.
    ("1_2", 5, (310, 145, 542, 532)),
    # p6: full-width plate, (a)+(b) top row joined by an orange flow arrow,
    # (c) below. NOT split: the arrow crosses the (a)/(b) gap and "Middle
    # layers" labels (a) from x~79 while (b)'s labels run to x~539.
    ("1_3", 6, (74, 98, 546, 520)),
    # p7: three SEM photos in one row under a single caption (no (a)/(b)/(c)
    # sub-labels, so not split). x1=428 stops well short of fig 1.5's (a)
    # tetrad circle, which starts at x~448.
    ("1_4", 7, (56, 96, 428, 252)),
    # p7: right-column stack, shares the page with 1.4. x0=368 sits between
    # the body text (ends x~360) and the "Generative cell" label (x~375).
    ("1_5", 7, (368, 143, 543, 630)),
    # p8: full-width photo band. Caption is centred at y~360-372.
    ("1_6", 8, (76, 183, 560, 378)),
    # p9: four panels (a)-(d). NOT split -- (b)'s "Syncarpous ovary" label is
    # set to the LEFT of (b), overlapping (a)'s x-range, so a per-panel rect
    # would either cut that label or steal (a)'s artwork.
    ("1_7", 9, (56, 98, 543, 442)),
    # p10: full-width plate, three rows. NOT split -- (b) and (c) sit side by
    # side sharing a y-band with leader lines running between them.
    ("1_8", 10, (84, 105, 545, 558)),
    # p12: LEFT column, prose in the right column starts at x~300, so x1=295
    # clips just inside it. Tall rect: (a)/(b) photos then the (c) drawing,
    # caption at y~687-720.
    ("1_9", 12, (74, 98, 295, 725)),
    # p13: RIGHT-side figure. x0=295 clears the left text column (ends x~283).
    # y0=105 keeps the magnifier circle that overlaps the text column's edge.
    ("1_10", 13, (295, 105, 545, 472)),
    # p14: LEFT column. The (a) panel's pale blue background ends at x~367 and
    # the right text column starts at x~393, so x1=372 sits in the gutter.
    ("1_11", 14, (76, 101, 372, 620)),
    # p16: full-width plate, five panels. Caption is four lines, y~484-543.
    ("1_12", 16, (76, 98, 558, 548)),
    # p18: plate sits BELOW a full-width paragraph that ends at y~295, so
    # y0=306 is inside the gap. Caption two lines at y~558-579.
    ("1_13", 18, (90, 306, 557, 585)),
    # p19: RIGHT column, (a) over (b). x0=376 clears the left text column
    # (ends x~365). Caption is three narrow lines, y~582-618.
    ("1_14", 19, (376, 103, 550, 625)),
    # p21: A4 page (595.4 x 842.4), NOT 612 x 820.8. Full-width plate; the
    # apple in (b) reaches x~29, hence x0=24.
    ("1_15", 21, (24, 106, 537, 622)),

    # ---- cleanly separable sub-panels --------------------------------------
    # 1.9: three physically gapped panels, each with its own (a)/(b)/(c) tag
    # and no shared leader lines.
    ("1_9a", 12, (128, 100, 248, 250)),
    ("1_9b", 12, (110, 258, 254, 403)),
    ("1_9c", 12, (74, 404, 292, 660)),
    # 1.11: (a) line drawing on a pale blue field, (b) photo below it.
    ("1_11a", 14, (94, 103, 372, 335)),
    ("1_11b", 14, (95, 336, 315, 585)),
    # 1.12: five panels, two rows, each self-labelled.
    ("1_12a", 16, (78, 103, 222, 330)),
    ("1_12b", 16, (250, 103, 376, 330)),
    ("1_12c", 16, (382, 100, 557, 330)),
    ("1_12d", 16, (88, 336, 272, 476)),
    ("1_12e", 16, (349, 333, 501, 476)),
    # 1.14: (a) dicot embryo above, (b) grass embryo L.S. below.
    ("1_14a", 19, (378, 105, 548, 303)),
    ("1_14b", 19, (378, 308, 548, 578)),
    # 1.15: (a) seed-structure row block, (b) false-fruit row block.
    ("1_15a", 21, (78, 108, 535, 400)),
    ("1_15b", 21, (25, 402, 535, 595)),
]


def main():
    doc = pymupdf.open(SRC)
    os.makedirs(OUT_DIR, exist_ok=True)
    for fid, pno, rect in FIGS:
        page = doc[pno - 1]
        clip = pymupdf.Rect(*rect) & page.rect
        pix = page.get_pixmap(clip=clip, dpi=RENDER_DPI)
        img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
        # Colour is load-bearing in this chapter (stained sections, photos),
        # so keep RGB and only lift contrast slightly.
        img = ImageOps.autocontrast(img, cutoff=0.5)
        out = os.path.join(OUT_DIR, f"fig_{fid}.png")
        img.save(out)
        print(f"fig_{fid}: p{pno} {rect} {img.size} mode={img.mode} -> {out}")


if __name__ == "__main__":
    sys.exit(main())
