"""
Ch8 Microbes in Human Welfare - figure extraction + monochrome conversion
(SUPREME COMMAND PROMPT S4.4; procedure per skills/ncert-figure-extraction).

Why the rects are pinned by hand
--------------------------------
This chapter is raster-dominant: figures 8.1-8.7 are photographs/micrographs
placed as embedded images, and 8.8 is vector artwork.  In BOTH families the
in-figure callout labels ("Flagella", "Rod-shaped bacterium", "Head", "Collar",
"Tail", "Plate", "Pins", "Prongs", "Compact Rod-shaped viruses", "Fungal
colony", "Gas", "Gas-holder", "Dung", "Water", "Sludge", "Digester") are drawn
as artwork, NOT as text-layer glyphs -- page.get_text("words") inside these
plates returns only the panel letters "(a)/(b)/(c)" and nothing else.  That is
exactly the vacuous-audit trap the skill warns about, so every rect below was
read off a 20 pt coordinate grid (scratch/ch8_figs/grid/pNN.png) and then
cross-checked against per-figure raster/drawings extents plus the neighbouring
prose column's x boundary.

NCERT sets most of these plates *beside* a body-text column (p4, p6, p7, p8),
so an automatic ink bounding box would sweep the adjacent paragraph into the
crop.  Captions are deliberately EXCLUDED (the notes rewrite each caption in
running text), so each bottom edge stops short of the "Figure 8.N ..." line
whose y0 is recorded per rect below.

Pipeline per asset:
  1. page.get_pixmap(clip=rect, dpi=300)   -> high-res clip render of the plate
  2. Image.convert("L")                    -> true single-channel greyscale
  3. ImageOps.autocontrast(cutoff=1)       -> restore contrast lost with hue
                                              (these plates are printed in
                                              colour: red rods, blue cocci,
                                              green phage, orange digester)
  4. save assets/fig_<id>.png              -- only the converted file is embedded

Rects are in PDF points on the artwork page; page box is 568.8 x 777.6.

Run:
  /vercel/share/neetenv/bin/python \
    "notes/class 12/Ch8_MicrobesInHumanWelfare/extract_figures.py"
"""

import os
import sys

import pymupdf
from PIL import Image, ImageOps

SRC = "Chapter/class 12/Chapter 8 - Microbes in Human Welfare.pdf"
OUT_DIR = "notes/class 12/Ch8_MicrobesInHumanWelfare/assets"
RENDER_DPI = 300

# (asset id, 1-indexed artwork page, clip rect x0, y0, x1, y1)
FIGS = [
    # ---- p2: three figures share the page in two columns ----
    # 8.1 (a)+(b)+(c) bacteria plate, LEFT column.  The "(a)/(b)/(c)" panel
    # letters sit at x 205.4-217.2 and the (c) flagella panel's blue artwork
    # reaches y=368.  Right edge pinned at 224 -- well clear of fig 8.2's
    # column, which starts at x=239.7 -- and bottom stops at 372, short of the
    # 8.1 caption block at y0=374.4.
    # RE-PINNED (audit check B + eyeball): the first box started at x=82, which
    # sliced the left-hand flagellum off panel (c) -- the dark-drawings union
    # for this band starts at x=58.3 (the near-white 0.96/0.97/0.92 panel wash
    # at x=58.7 is background, but the blue flagella strokes are real ink out
    # to x=58.3).  Left edge moved to 56 to clear it by ~2pt; that still sits
    # right of the decorative margin band and the page-number tab (x<54).
    # Audit check C reports T:46px@(98.7,70.0): EXPLAINED -- that is the NCERT
    # page-header band raster (-21.6,-22.0,590.5,75.2), i.e. the leaf/logo
    # motif, which is page furniture ending at y=75.2.  Rendering the strip
    # y 58-100 confirms panel (a)'s own border begins below it, so the top edge
    # at y=76 is correct and must NOT be raised to swallow the header.
    ("8_1", 2, (56, 76, 224, 372)),
    # 8.2 (a)+(b) virus micrographs, RIGHT column top.  Rasters are
    # x 279.0-393.6 and x 413.9-530.0, y 84.4-227.9; the vector callout labels
    # ("Head", "Collar", "Tail", "Plate", "Pins", "Prongs") are drawn to the
    # right of panel (a) and are NOT text-layer, so the box must span the full
    # column width.  Panel letters (a)/(b) at y 231.6-241.1 are included.
    # Audit check B reports B68.3 here: EXPLAINED -- the overflowing rect is
    # (273.4,143.1,326.1,313.3), the tall bracket/leader artwork belonging to
    # fig 8.2(c) below, which is a deliberately separate asset.  Not clipped
    # content of 8.2(a)/(b); confirmed on the contact sheet.
    ("8_2a", 2, (276, 80, 534, 245)),
    # 8.2 (c) TMV micrograph + its vector "Compact Rod-shaped viruses" label,
    # which runs out past the raster's right edge (drawings extent to x=545.8).
    # Plate raster measured x 278.7-458.1, y 253.1-364.9; the label artwork
    # extends right to x=545.8, hence the 548 right edge.  Panel letter (c) at
    # y 374.4-383.9 is included; bottom stops at 388, above the 8.2 caption
    # block at y0=392.7.
    # Audit check B reports T48.9/B52.9: EXPLAINED -- the union includes the
    # shared leader-line artwork that spans up into 8.2(a)/(b) (y from 199.1)
    # and the caption's tinted panel below (to y=440.9).  Neither is 8.2(c)
    # content; the crop was eyeballed and the label reads in full.
    ("8_2c", 2, (274, 248, 548, 388)),
    # 8.3 (a)+(b) petri-dish colonies, full width lower half.  Rasters
    # y 478.3-649.2 including the "Fungal colony" vector leader line to the
    # right; panel letters (a)/(b) at y 650.9-660.4.  Bottom 666 stops short of
    # the 8.3 caption at y0=681.9.
    # RE-PINNED (audit check C + eyeball): the first box started at x=148,
    # which cut the left edge off petri dish (a) -- check C reported 149px of
    # unexplained ink on the L band and the dark-drawings union for the band
    # starts at x=95.7.  Left edge moved to 93.  The orange page-number tab
    # ("150" text at x 53.8-78.5, y 615.3-629.3) and the decorative margin band
    # both sit left of x=93, so they stay excluded.
    ("8_3", 2, (93, 474, 540, 666)),
    # ---- p4: two photographs stacked in the LEFT column ----
    # 8.4 Fermentors photo: raster x 57.8-274.3, y 83.5-249.3.  Neighbouring
    # prose column ("8.2.1 Fermented Beverages") starts at x=290.2, so the
    # right edge at 278 clips safely inside it.  Caption at y0=255.6.
    ("8_4", 4, (55, 80, 278, 252)),
    # 8.5 Fermentation Plant photo: raster x 57.6-263.3, y 280.2-451.9.
    # Caption "Figure 8.5 Fermentation Plant" at y0=460.6, so bottom = 456.
    ("8_5", 4, (55, 277, 278, 456)),
    # ---- p6: one photograph, LEFT column ----
    # 8.6 Secondary treatment aeration tank: raster x 57.0-295.6, y 85.1-261.9
    # (drawings band to y=282.8 is the caption's tinted panel, excluded).
    # Prose column starts at x=309.1; caption at y0=271.0 -> bottom = 267.
    ("8_6", 6, (54, 81, 300, 267)),
    # ---- p7: one photograph, RIGHT column ----
    # 8.7 Aerial view of a sewage plant: raster x 298.4-512.8, y 83.8-219.9.
    # Left-hand prose column ends at x=280.1, caption at y0=226.4.
    ("8_7", 7, (295, 80, 517, 223)),
    # ---- p8: vector biogas-plant schematic, LEFT of the prose column ----
    # 8.8 A typical biogas plant.  Artwork extent x 57.3-361.1, y 84.3-354.1
    # and every label ("Gas", "Gas-holder", "Dung", "Water", "Sludge",
    # "Digester", "( CH4 + CO2 + ----- )") is vector, so the drawings extent is
    # what pins this rect.  The prose column's first word starts at x=373.7,
    # so the right edge at 370 sits between the "Gas" label and the prose.
    # Caption at y0=354.0 overlaps the artwork's bottom band, so the bottom is
    # pinned at 350 to keep the digester tank while dropping the caption line.
    # Audit check B2 reports B4.1: EXPLAINED and ACCEPTED -- the overflowing
    # raster is the caption's own tinted background panel, which NCERT runs to
    # y=354.1 underneath the "Figure 8.8 A typical biogas plant" line.  Pulling
    # the bottom edge down to include it would drag the caption text into the
    # crop; check B (vector artwork, the actual diagram) is clean at this edge,
    # and the eyeball confirms the digester tank is whole.
    ("8_8", 8, (54, 80, 370, 350)),
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
