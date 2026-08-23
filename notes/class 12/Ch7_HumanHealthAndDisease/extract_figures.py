"""
Ch7 Human Health and Disease - figure extraction + monochrome conversion
(SUPREME COMMAND PROMPT S4.4; procedure per skills/ncert-figure-extraction).

Census (enumerated from the rendered page images, not from caption strings)
--------------------------------------------------------------------------
11 numbered figures, 7.1 - 7.11, on artwork pages 6, 7, 9, 12, 13, 16, 17
of the 22-page source PDF.  Three further ink-bearing regions were inspected
and deliberately EXCLUDED:

  * p2  - the M.S. Swaminathan portrait photograph (scientist profile).
          S5 item 3 / S4.4 "Hard no": a portrait is never embedded, greyscaled
          or not.  Not an asset, by rule.
  * p3  - the chapter-opener title plate (QR code + a tilted decorative
          thumbnail that merely re-prints fig 7.4's antibody artwork).  Page
          furniture / title block, carries no fact of its own.
  * p21, p22 - the orange wheat-ear motif beside the SUMMARY box.  Decoration.

So the on-disk asset count is 11, and there is no bonus unnumbered plate in
this chapter (unlike Ch5's central-dogma schematic).

Why the rects are pinned by hand
--------------------------------
Every in-figure label in this chapter is artwork, not text-layer glyphs:
page.get_text("words") inside the fig 7.1 plate on p6 returns ZERO words even
though the diagram carries ten callouts ("Sporozoites", "Salivary glands",
"Mosquito Host", "Human Host", "Gametocytes", "Male", "Female", ...).  Same
for 7.4's "Antigen binding site"/"Light chain"/"Heavy chain", 7.5's "Lymph
nodes"/"Thymus"/"Lymphatic vessels" and every callout in 7.6.  That is exactly
the vacuous-audit trap the skill warns about, so each rect below was read off
a 20 pt coordinate grid (scratch/ch7_figs/grid/pNN.png) and then cross-checked
numerically against a 150 dpi ink bounding box (pixels < 150 grey) measured in
a window that deliberately excludes the page furniture: the dark green header
band (y < 76), the brown/orange corner motif, the right-margin decorative
band, the page-number tab, and the diagonal "(c) NCERT / not to be
republished" watermark raster at (46, 191, 508, 653) which is present on
EVERY page and is light enough to fall above the 150 threshold.

A FOURTH check was needed here.  The skill's border-band check C uses a dark
threshold (grey < 110), and two of this chapter's plates are drawn entirely in
mid-tone colour -- the fig 7.10 cannabis leaf (fill 0.65/0.81/0.22, luma ~177)
inside a pale grey frame.  Check C passed on it while the crop was in fact
clipping the frame.  So every rect was also re-probed with a light threshold
(grey < 205) on the same 6 pt border bands.  Surviving hits, all explained:
  * fig 7.1 bottom  - the orange page-number tab ("132"), ink starts y=611.8,
                      x 53-92; the plate's own ink ends before y=606.
  * fig 7.2 top     - the page's top-right leaf/corner motif at y~73,
                      x 469-502; the figure raster starts at y=82.9.
  * fig 7.5 top     - the top-left brown/orange corner motif at y~74.
  * fig 7.10 top    - REAL: the panel border.  Rect re-pinned, see below.

NCERT sets 7.2, 7.3, 7.4, 7.5 and 7.11 *beside* a body-text column, so an
automatic ink box would sweep the neighbouring paragraph in; each of those
rects is clipped against the prose column's own x boundary taken from
get_text("words").  Captions are EXCLUDED throughout (this project's
convention: the notes rewrite each caption in running text), so every bottom
edge stops short of its "Figure 7.N ..." line, whose y0 is recorded per rect.

Pipeline per asset:
  1. page.get_pixmap(clip=rect, dpi=300)   -> high-res clip render of the plate
  2. Image.convert("L")                    -> true single-channel greyscale
  3. ImageOps.autocontrast(cutoff=1)       -> restore contrast lost with hue
                                              (these plates are printed in
                                              colour: pink Plasmodium cycle,
                                              cyan/yellow/magenta antibody
                                              chains, green cannabis leaf)
  4. save assets/fig_<id>.png              -- only the converted file is embedded

Rects are in PDF points on the artwork page; page box is 568.8 x 777.6.

Run:
  /vercel/share/neetenv/bin/python \
    "notes/class 12/Ch7_HumanHealthAndDisease/extract_figures.py"
"""

import os
import sys

import pymupdf
from PIL import Image, ImageOps

SRC = "Chapter/class 12/Chapter 7 - Human Health and Disease.pdf"
OUT_DIR = "notes/class 12/Ch7_HumanHealthAndDisease/assets"
RENDER_DPI = 300

# (asset id, 1-indexed artwork page, clip rect x0, y0, x1, y1)
FIGS = [
    # ---- p6: fig 7.1 is a full-page plate, no prose on the page at all ----
    # Plasmodium life cycle.  Ink extent (thr 150) x 56.0-531.2, y 86.6-605.0;
    # the vector-drawings union agrees at x 55.6-531.5, y 112.2-605.2, and the
    # extra 86.6-112.2 band is the mosquito's wing artwork (confirmed by
    # rendering the strip y 84-125).  Every callout is artwork -- words in
    # this rect = 0.  Bottom stops at 610, above the "Figure 7.1 Stages in the
    # life cycle of Plasmodium" caption at y0=620.4, and above the orange
    # page-number tab ("132", y 615-635, x 16-92).
    ("7_1", 6, (53, 83, 536, 610)),

    # ---- p7: two rasters stacked in the RIGHT column, prose on the left ----
    # 7.2 elephantiasis limb photo.  Single raster x 328.4-508.4, y 82.9-348.1.
    # Left prose column's words end at x=309.6, so x0=325 sits in the gutter.
    # Top edge 79 is below the page's corner motif (ends y~65).  Caption block
    # "Figure 7.2 Diagram showing inflammation ..." at y0=353.0 -> bottom 351.
    ("7_2", 7, (325, 79, 513, 351)),
    # 7.3 ringworm skin photo.  Raster x 269.9-503.8, y 417.9-529.6 (ink
    # 272.6-503.9 / 418.2-528.6).  Prose column on this row ends at x=257.3.
    # Caption "Figure 7.3 Diagram showing ringworm ..." at y0=537.4 -> 533.
    ("7_3", 7, (267, 414, 508, 533)),

    # ---- p9: fig 7.4 antibody plate, RIGHT of a narrow prose column ----
    # Rounded panel + its four vector callouts.  Ink x 217.0-516.5,
    # y 293.7-524.1; drawings union x 217.0-515.1, y 293.6-523.0; the panel
    # raster is x 215.8-521.0.  Neighbouring prose ("The primary and secondary
    # immune responses...") ends at x=200.9, so x0=213 clears it.  The "N" and
    # "C" chain-terminal labels sit at the very top/bottom of the panel, hence
    # 2-6 pt of slack on both edges.  Caption at y0=536.5 -> bottom 530.
    ("7_4", 9, (213, 290, 521, 530)),

    # ---- p12: fig 7.5 lymph-node diagram, LEFT of the prose column ----
    # Body silhouette raster x 29.2-173.2 (white margin), real ink from x=57.8;
    # the "Lymph nodes"/"Thymus"/"Lymphatic vessels" labels are vector and run
    # right to x=201.7, so the box must span to 206.  Prose column's first word
    # starts at x=224.4.  Top 80 clears the corner motif (y < 76); caption
    # block "Figure 7.5 Diagrammatic representation of Lymph nodes" at
    # y0=306.4, so bottom 302 keeps the last leader line and drops the caption.
    ("7_5", 12, (54, 80, 206, 302)),

    # ---- p13: fig 7.6 retrovirus replication, full-width plate ----
    # All artwork: ink x 87.4-464.6, y 84.2-527.8 (drawings x 125.9-422.6 --
    # narrower, because the outer rounded panel exceeds the 480/420 size caps
    # and is filtered out of the drawings union; the ink box is authoritative
    # here).  Includes the in-plate "NOTE: Infected cell can survive while
    # viruses are being replicated and released" line, which is part of the
    # figure.  Caption "Figure 7.6 Replication of retrovirus" at y0=538.4.
    ("7_6", 13, (84, 81, 469, 532)),

    # ---- p16: 7.7 and 7.8 side by side under the prose, shared caption row --
    # 7.7 morphine skeletal formula, LEFT.  Ink (window y0=542, below the last
    # prose line at y=537) x 125.7-293.2, y 549.2-690.8.  The page-number tab
    # ("142", x 53.8-78.5, y 618.8-632.8) stays outside because x0=122.
    # Caption "Figure 7.7 Chemical structure of Morphine" at y0=700.7.
    ("7_7", 16, (122, 545, 298, 696)),
    # 7.8 opium poppy photo, RIGHT.  Ink x 379.2-489.1, y 542.5-688.9 measured
    # in the same y0=542 window; x0=374 leaves ~5 pt and still sits well right
    # of fig 7.7's box (ends x=293.2).  Caption "Figure 7.8 Opium poppy" at
    # y0=700.7 -> bottom 694.
    ("7_8", 16, (374, 538, 495, 694)),

    # ---- p17: 7.9 + 7.10 on one row, 7.11 beside the prose below ----
    # 7.9 cannabinoid skeletal formula, LEFT.  Ink x 53.9-258.4, y 219.2-354.6
    # (window y0=212, below the prose block that ends at y=207).  Caption
    # "Figure 7.9 Skeletal structure of cannabinoid molecule" at y0=372.0.
    ("7_9", 17, (50, 215, 263, 366)),
    # 7.10 Cannabis sativa leaf, RIGHT.  RE-PINNED: the first box (348, 224,
    # 460, 366) sliced ~1.5 pt off the panel's top border.  The dark-ink probe
    # (thr 150) had reported y0=230.2 because this plate's leaf is mid-green
    # (fill 0.65/0.81/0.22 -> luma ~177) and its frame is pale grey, i.e. the
    # whole figure sits ABOVE a 150 threshold; audit check B caught it
    # (OVERFLOW T14.3) and a thr-205 re-probe put the panel at x 352.3-454.6,
    # y 222.5-361.0 (shadow included).  Rect widened to clear that by ~2 pt.
    # Check B still reports L2.8/T14.3/R7.6 against the raw drawings union
    # (leaf gradient shapes defined out to x=464.0, y=210.5): EXPLAINED --
    # those shapes are clipped by the panel's own clip path, so no ink is
    # rendered outside the frame; the thr-205 probe and the eyeball agree.
    # Left edge 350 stays clear of fig 7.9's box (ends x=258.4); caption
    # "Figure 7.10 Leaves of Cannabis sativa" at y0=372.4.
    ("7_10", 17, (350, 219, 456, 364)),
    # 7.11 flowering Datura branch, RIGHT of the cocaine paragraph.  Ink
    # x 330.4-510.0, y 399.1-580.1; the prose column on those rows ends at
    # x=298.6, so x0=326 sits in the gutter.  Caption "Figure 7.11 Flowering
    # branch of Datura" at y0=592.0 -> bottom 586.
    ("7_11", 17, (326, 395, 515, 586)),
]


def main() -> int:
    doc = pymupdf.open(SRC)
    os.makedirs(OUT_DIR, exist_ok=True)
    for fid, pno, (x0, y0, x1, y1) in FIGS:
        name = f"fig_{fid}.png"
        try:
            page = doc[pno - 1]
            rect = pymupdf.Rect(x0, y0, x1, y1) & page.rect
            pix = page.get_pixmap(clip=rect, dpi=RENDER_DPI)
            img = ImageOps.autocontrast(
                Image.frombytes("RGB", (pix.width, pix.height), pix.samples).convert("L"),
                cutoff=1,
            )
            path = os.path.join(OUT_DIR, name)
            img.save(path)
            print(f"{name}: p{pno} ({x0},{y0})-({x1},{y1}) "
                  f"{img.width}x{img.height}px mode={img.mode} -> {path}")
        except Exception as exc:
            raise RuntimeError(f"FIGURE EXTRACTION FAILED for {name} on page {pno}: {exc}")
    doc.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
