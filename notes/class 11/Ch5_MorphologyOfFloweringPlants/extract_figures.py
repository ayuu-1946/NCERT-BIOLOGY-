"""Hand-pinned NCERT figure extraction for Class 11 Chapter 5.

Rects are PDF points in the source mediabox (0, 0, 576, 784.8). Every rectangle
was pinned against the mandatory 440 dpi / 5-PDF-point grid overlays in
`scratch/ch5_figs/grid_4x/` and then confirmed numerically against the page's
own geometry: the union of vector-drawing rects, raster-image bboxes and
text-line bboxes for the plate's labels and panel markers.

Standard: an asset holds the complete artwork, every in-figure label, every
leader line and every panel marker, and **excludes the printed caption** --
captions are typeset by the chapter script from the inventory's `caption` rows,
so a caption baked into the plate would print twice. This matches the
convention used by the closed chapters (e.g. Ch6 Anatomy of Flowering Plants).

Re-pinned at Gate 1 (session 1-F re-verification) after opening every inherited
asset and reading it: twelve of the seventeen inherited rectangles clipped a
label, a panel marker or a caption row. See `Ch5_TRACKER.md` for the defect log.
"""
import os

import pymupdf
from PIL import Image, ImageOps

SRC = "Chapter/class 11/Chapter 05 - Morphology of Flowering Plants.pdf"
OUT_DIR = "notes/class 11/Ch5_MorphologyOfFloweringPlants/assets"
RENDER_DPI = 300

# (figure id, 1-indexed PDF page, rect) -- artwork + labels + panel markers, caption excluded.
#
# Each rect = the plate's measured content extent, padded by ~8 pt and then clamped
# by the nearest neighbour (printed caption, adjacent prose column, page header).
# Content extent = dark-ink bbox from `scratch/ch5morph_gate1/ink_bbox.py`, union'd
# with the text-layer bboxes of the plate's labels/panel markers and, for the
# photographic plates, with the raster image bbox (a photo's light background makes
# the ink bbox under-report its true edge).
FIGS = [
    ("5_1", 4, (88, 98, 325, 404)),
    ("5_2", 4, (55, 445, 543, 663)),
    ("5_3", 5, (283, 128, 525, 334)),
    ("5_4", 6, (50, 97, 267, 456)),
    ("5_5", 6, (54, 506, 279, 676)),
    ("5_6", 7, (294, 85, 520, 332)),
    ("5_7", 7, (280, 421, 495, 678)),
    ("5_8", 8, (54, 97, 280, 237)),
    ("5_9", 8, (72, 480, 522, 674)),
    ("5_10", 9, (38, 569, 522, 690)),
    ("5_11", 10, (129, 97, 466, 300)),
    ("5_12", 11, (394, 95, 497, 630)),
    ("5_13", 12, (204, 96, 490, 241)),
    ("5_14", 12, (54, 478, 286, 608)),
    ("5_15", 13, (84, 97, 471, 303)),
    ("5_16", 13, (333, 452, 525, 681)),
    ("5_17", 14, (112, 466, 468, 680)),
]


def main() -> None:
    os.makedirs(OUT_DIR, exist_ok=True)
    doc = pymupdf.open(SRC)
    for fid, pno, rect in FIGS:
        page = doc[pno - 1]
        clip = pymupdf.Rect(*rect) & page.rect
        pix = page.get_pixmap(clip=clip, dpi=RENDER_DPI, alpha=False)
        rgb = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
        # Step 2 of section 4.4: true single-channel greyscale, then autocontrast to
        # recover the separation that hue was carrying. autocontrast is not optional.
        img = ImageOps.autocontrast(rgb.convert("L"), cutoff=1)
        out = os.path.join(OUT_DIR, f"fig_{fid}.png")
        img.save(out, dpi=(RENDER_DPI, RENDER_DPI), optimize=True)
        print(f"fig_{fid}: p{pno} rect={tuple(rect)} size={img.size} mode={img.mode} -> {out}")


if __name__ == "__main__":
    main()
