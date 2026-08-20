"""
Ch10 Cell Cycle and Cell Division — figure extraction + monochrome conversion
(SUPREME COMMAND PROMPT §4.4).

Pipeline per asset:
  1. Clip-render the figure's bounding box from the source chapter PDF at 300 dpi
     (page.get_pixmap(clip=rect, dpi=300)). Every figure in this chapter is raster
     artwork with its in-figure labels ("Early Prophase", "Metaphase 1", ...) baked
     into the raster -- they are NOT in the page text layer, so a clip render is the
     only way to keep the labels attached to the drawing.
  2. Image.convert("L")              -> true single-channel greyscale
  3. ImageOps.autocontrast(cutoff=1) -> recover contrast lost when hue disappears
  4. Save to assets/<name>.png       -- only the converted file is ever embedded.

Sub-part splitting: NCERT's own running text cites "Figure 10.2 a", "(Figure 10.2 b)",
"(Figure 10.2 c)", "(Figure 10.2 d)" and "(Figure 10.2 e)" at five different points in
the chapter, so Figure 10.2 is cropped as five separate assets and each is placed
inline at its own topic (§4.4 placement rule). Figures 10.1, 10.3 and 10.4 are single
figures in the source and are cropped whole.

Run from anywhere:  python extract_figures.py
"""

import os

import pymupdf
from PIL import Image, ImageOps

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "assets")

# Walk up to the repo root (the directory holding neet_template.py) to find Chapter/.
_root = HERE
while _root != os.path.dirname(_root) and not os.path.exists(
    os.path.join(_root, "neet_template.py")
):
    _root = os.path.dirname(_root)
SRC = os.path.join(
    _root, "Chapter", "class 11", "Chapter 10 - Cell Cycle and Cell Division.pdf"
)

DPI = 300

# (asset_name, 1-based source page, clip rect, scrub rects)
# Rects are PDF points (x0, y0, x1, y1) in page coordinates. Boundaries were measured
# from a 110 dpi coordinate-gridded render of each page plus the page text layer's own
# word boxes for the caption line, which fixes the bottom edge of every crop:
#   p2  "Figure 10.1"      caption starts y=332.9  -> fig_10_1  bottom 330
#   p4  "Figure 10.2"      caption starts y=688.4  -> fig_10_2b bottom 680
#   p5  "Figure 10.2"      caption starts y=679.8  -> fig_10_2e bottom 672
#   p8  "Figure 10.3"      caption starts y=334.2  -> fig_10_3  bottom 330
#   p9  "Figure 10.4"      caption starts y=364.2  -> fig_10_4  bottom 360
FIGURES = [
    # Fig 10.1 -- the circular cell-cycle wheel. get_image_info() reports the artwork
    # raster at exactly (317.3, 117.0, 495.2, 312.7); the crop is widened left to x=298
    # to take in the vertical "M Phase" label (text-layer box x 304.9-314.5,
    # y 195.1-223.1) which sits outside the raster, and stops at y=330 to exclude the
    # caption line at y=332.9.
    ("fig_10_1", 2, (298.0, 110.0, 502.0, 330.0), []),
    # Fig 10.2 (a) -- Early Prophase + Late Prophase, the two panels above the "(a)"
    # part label. The (a)/(b) split sits at y=384.5: a first cut at y=392 left the top
    # arc of the next ("Transition to Metaphase") circle hanging in (a)'s bottom edge
    # AND sliced that same circle's crown off the top of (b). Re-measured from the two
    # test crops, the "(a)" label ends at y~382 and the circle's topmost ink begins at
    # y~386, so 384/385 is the only line that keeps both parts whole.
    ("fig_10_2a", 4, (340.0, 100.0, 512.0, 385.0), []),
    # Fig 10.2 (b) -- Transition to Metaphase + Metaphase. Top edge 384 (not 392) so
    # the "Transition to Metaphase" circle keeps its crown.
    ("fig_10_2b", 4, (340.0, 384.0, 512.0, 680.0), []),
    # Fig 10.2 (c) -- Anaphase panel, left column of page 5.
    ("fig_10_2c", 5, (56.0, 102.0, 230.0, 284.0), []),
    # Fig 10.2 (d) -- Telophase panel. Bottom edge 475 (not 470): at 470 the "(d)"
    # part label was sliced in half and its lower half landed at the top of (e).
    ("fig_10_2d", 5, (56.0, 284.0, 230.0, 475.0), []),
    # Fig 10.2 (e) -- the cytokinesis/Interphase panel that closes the mitosis plate.
    # Top edge 476 clears the "(d)" label that a y=470 start dragged in.
    ("fig_10_2e", 5, (56.0, 476.0, 230.0, 672.0), []),
    # Fig 10.3 -- Stages of Meiosis I, one wide band across the top of page 8.
    ("fig_10_3", 8, (40.0, 102.0, 522.0, 330.0), []),
    # Fig 10.4 -- Stages of Meiosis II, one wide band across the top of page 9.
    ("fig_10_4", 9, (54.0, 98.0, 540.0, 360.0), []),
]


def main():
    os.makedirs(ASSETS, exist_ok=True)
    doc = pymupdf.open(SRC)
    print(f"source: {SRC}\npages: {doc.page_count}\n")

    for entry in FIGURES:
        name, page_no, box, scrub = entry[:4]
        white_point = entry[4] if len(entry) > 4 else None
        page = doc[page_no - 1]
        rect = pymupdf.Rect(*box)
        out = os.path.join(ASSETS, f"{name}.png")

        # Step 1 -- high-resolution clip render.
        page.get_pixmap(clip=rect, dpi=DPI).save(out)

        # Steps 2-3 -- true monochrome + contrast recovery.
        img = Image.open(out).convert("L")

        if white_point is not None:
            img = img.point(
                lambda v, wp=white_point: 255 if v >= wp else int(v * 255 / wp)
            )

        img = ImageOps.autocontrast(img, cutoff=1)

        if scrub:
            k = DPI / 72.0
            for sx0, sy0, sx1, sy1 in scrub:
                img.paste(
                    255,
                    (
                        max(0, int((sx0 - box[0]) * k)),
                        max(0, int((sy0 - box[1]) * k)),
                        min(img.width, int((sx1 - box[0]) * k)),
                        min(img.height, int((sy1 - box[1]) * k)),
                    ),
                )

        img.save(out)

        check = Image.open(out)
        print(
            f"{name:12s} p{page_no:<3d} {check.size[0]:5d}x{check.size[1]:<5d} "
            f"mode={check.mode} extrema={check.getextrema()}"
        )

    doc.close()


if __name__ == "__main__":
    main()
