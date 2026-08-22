"""
Ch5 Molecular Basis of Inheritance - figure extraction + monochrome conversion
(SUPREME COMMAND PROMPT S4.4, redo of the first pass).

Why the rects are pinned by hand
--------------------------------
Every figure in this chapter is vector/composite artwork whose in-figure labels
("Base pairs", "Sugar phosphate backbone", "H1 histone", "Discontinuous
synthesis", "Number of short tandem repeats", ...) are drawn as part of the
plate, so a clip-rect render at 300 dpi is the only way to keep the labels
attached to the drawing.  NCERT sets most of these plates *beside* a narrow
body-text column (p5, p13, p20, p21, p25) or between wrap-around prose (p4,
p15, p16), so an automatic "ink bounding box" sweeps the neighbouring
paragraph into the crop -- that is exactly how the first pass produced
unusable images (fig_5_4a carried the whole left-hand paragraph).
Each rect below was therefore read off a 50 pt coordinate grid rendered over
the page (scratch/ch5_figs/grid/pNN.png) and then verified by opening the
emitted PNG.

Pipeline per asset:
  1. page.get_pixmap(clip=rect, dpi=300)   -> high-res clip render of the plate
  2. Image.convert("L")                    -> true single-channel greyscale
  3. ImageOps.autocontrast(cutoff=1)       -> restore contrast lost with hue
                                              (NCERT prints these plates in
                                              red/green/blue/orange)
  4. save assets/fig_<id>.png              -- only the converted file is embedded

Rects are in PDF points on the artwork page; page box is 568.8 x 777.6 and
captions are deliberately excluded (the note rewrites each caption in text).

Run:
  /vercel/share/neetenv/bin/python \
    "notes/class 12/Ch5_MolecularBasisOfInheritance/extract_figures.py"
"""

import os
import sys

import pymupdf
from PIL import Image, ImageOps

SRC = "Chapter/class 12/Chapter 5 - Molecular Basis of Inheritance.pdf"
OUT_DIR = "notes/class 12/Ch5_MolecularBasisOfInheritance/assets"
RENDER_DPI = 300

# (asset id, 1-indexed artwork page, clip rect x0, y0, x1, y1)
FIGS = [
    # p2: full-width plate under the last text line, above the caption.
    # RE-PINNED (Gate 3b figure-clipping fix): the original (108,575,528,676)
    # box clipped real artwork -- the vector glyphs of the "3' hydroxyl" label
    # run out to x=529.13 and the lowest base box reaches y=677.68, so the old
    # right/bottom edges cut ~1.1pt and ~1.7pt of ink respectively.  Rect is
    # now pinned ~2-4pt outside the drawings extent in the figure's y-band
    # (x 117.07-529.13, y 580.43-677.68, page-number block at x<93 excluded).
    # Bottom still stops well short of the caption band (caption drawing row
    # starts y=688.40, the words "Figure 5.1 ..." at y=693.8), and the top
    # clears the last body line above (ends y=568.2).
    ("5_1", 2, (108, 573, 532, 682)),
    # p4: full-width plate at the top of the page.  Its labels ("3'", "HO",
    # "5'") are vector, not text-layer, so the drawings extent (x 89.6-514.9,
    # y 84.1-275.4) is what pins this rect; the caption starts at y=291.3.
    ("5_2", 4, (86, 80, 519, 280)),
    # p4: helix + base-pair legend, left column only.  The wrap-around prose
    # column starts at x=314.88, so the right edge is pinned just short of it.
    ("5_3", 4, (50, 308, 313, 594)),
    # p4: unnumbered "Central dogma" diagram NCERT prints at the foot of p4
    ("5_central_dogma", 4, (245, 618, 536, 712)),
    # p5: nucleosome sits right of the body column (which ends x~306)
    ("5_4a", 5, (310, 156, 524, 308)),
    # p5: EM micrograph, same right-hand column
    ("5_4b", 5, (300, 336, 518, 490)),
    # p8: full-width Hershey-Chase flow chart
    ("5_5", 8, (116, 234, 538, 582)),
    # p10: framed plate in the left column (prose column starts x~398)
    ("5_6", 10, (54, 252, 254, 574)),
    # p11: framed full-width plate
    ("5_7", 11, (38, 380, 516, 606)),
    # p13: replicating fork right of the body column (which ends x~295)
    ("5_8", 13, (298, 80, 524, 314)),
    # p14: framed full-width plate
    ("5_9", 14, (64, 300, 512, 434)),
    # p15: three-stage plate, left-aligned under the prose
    ("5_10", 15, (50, 452, 392, 674)),
    # p16: capping/splicing/polyadenylation plate
    ("5_11", 16, (136, 406, 540, 674)),
    # p20: tRNA plate left of the narrow right-hand prose column (starts
    # x=435.6).  Its caption sits at y=449.7, so the bottom stops at 448.
    ("5_12", 20, (78, 296, 432, 448)),
    # p21: ribosome plate right of the narrow left-hand prose column (ends x~229)
    ("5_13", 21, (234, 76, 518, 264)),
    # p23: lac operon, both panels
    ("5_14", 23, (70, 82, 466, 354)),
    # p25: HGP montage right of the narrow prose column (ends x~217)
    ("5_15", 25, (224, 456, 468, 682)),
    # p29: DNA fingerprinting schematic.  This plate carries NO text-layer
    # words at all (every label is vector artwork), so the word-grazing audit
    # is silent here -- the rect must instead be pinned off the page's
    # get_drawings() extent, which is x 59.3-491.4 / y 83.6-499.7.
    ("5_16", 29, (57, 81, 494, 502)),
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
            path = os.path.join(OUT_DIR, name)
            raw = path + ".raw.png"
            pix.save(raw)
            img = ImageOps.autocontrast(Image.open(raw).convert("L"), cutoff=1)
            img.save(path)
            os.remove(raw)
            print(f"{name}: p{pno} ({x0},{y0})-({x1},{y1}) "
                  f"{img.width}x{img.height}px mode={img.mode} -> {path}")
        except Exception as exc:
            raise RuntimeError(f"FIGURE EXTRACTION FAILED for {name} on page {pno}: {exc}")
    doc.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
