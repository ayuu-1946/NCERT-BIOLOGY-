"""
Ch3 Plant Kingdom — figure extraction + monochrome conversion (SUPREME COMMAND PROMPT §4.4).

Pipeline per asset:
  1. Clip-render the figure's bounding box from the source chapter PDF at 300 dpi
     (page.get_pixmap(clip=rect, dpi=300)) -- a clip render survives the mixed
     vector-text + raster-artwork figures in this chapter, several of which carry
     in-figure labels baked into the raster (Fig 3.1 all parts, Fig 3.3a).
  2. Image.convert("L")            -> true single-channel greyscale
  3. ImageOps.autocontrast(cutoff=1) -> recover contrast lost when hue disappears
  4. Save to assets/<name>.png     -- only the converted file is ever embedded.

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
SRC = os.path.join(_root, "Chapter", "class 11", "Chapter 03 - Plant Kingdom.pdf")

DPI = 300

# (asset_name, 1-based source page, clip rect, scrub rects) -- all rects are in PDF
# points as (x0, y0, x1, y1) in *page* coordinates.
#
# `scrub` exists only because Figure 3.1's three caption sub-parts are NOT separated
# by clean horizontal whitespace in the source plate: (b-i) Laminaria starts at
# y=274.6 while row (a)'s "(a-ii)" label still runs to y=281.3, and (c-i) Porphyra
# starts at y=490.6 while (b-iii) Dictyota runs down to y=540.5. Any rectangle that
# captures all of row (b) therefore also catches a corner of row (a) or row (c).
# Each scrub rect whites out ONLY a neighbouring figure's intrusion -- measured from
# an ink-profile scan, never overlapping the target sub-part's own artwork or labels.
# Nothing belonging to the figure being extracted is ever painted over.
FIGURES = [
    # Figure 3.1 Algae -- one crop per NCERT caption sub-part, because the body text
    # itself cites "(Figure 3.1a)", "(Figure 3.1b)" and "(Figure 3.1c)" separately at
    # the end of 3.1.1, 3.1.2 and 3.1.3 respectively.
    ("fig_3_1a", 3, (111.0, 104.0, 406.0, 288.0), []),
    (
        "fig_3_1b",
        3,
        (68.0, 276.0, 492.0, 491.0),
        [
            (340.0, 276.0, 398.0, 297.0),  # row (a)'s "(a-ii)" label, which sits
            # above b-iii (b-iii's own artwork does not begin until y=315)
        ],
    ),
    ("fig_3_1c", 3, (200.0, 488.0, 470.0, 673.0), []),
    # Figure 3.2 Bryophytes -- grouped as NCERT's caption groups them:
    # (a)+(b) the liverwort Marchantia, (c)+(d) the mosses.
    ("fig_3_2ab", 6, (114.0, 227.0, 534.0, 425.0), []),
    ("fig_3_2cd", 6, (62.0, 425.0, 547.0, 672.0), []),
    # Figure 3.3 Pteridophytes -- (a)+(b) labelled diagrams, (c)+(d) habit photos.
    ("fig_3_3ab", 9, (48.0, 110.0, 500.0, 437.0), []),
    ("fig_3_3cd", 9, (62.0, 438.0, 478.0, 678.0), []),
    # Figure 3.4 Gymnosperms -- stacked in a narrow column in the source, so each
    # sub-part is cropped separately to stay legible at print size.
    ("fig_3_4a", 11, (314.0, 102.0, 520.0, 269.0), []),
    ("fig_3_4b", 11, (332.0, 269.0, 502.0, 500.0), []),
    ("fig_3_4c", 11, (315.0, 500.0, 520.0, 667.0), []),
    # Figure 3.5 Angiosperms -- (a) dicotyledon + (b) monocotyledon side by side.
    ("fig_3_5ab", 12, (219.0, 271.0, 501.0, 488.0), []),
]


def main():
    os.makedirs(ASSETS, exist_ok=True)
    doc = pymupdf.open(SRC)
    print(f"source: {SRC}\npages: {doc.page_count}\n")

    for name, page_no, box, scrub in FIGURES:
        page = doc[page_no - 1]
        rect = pymupdf.Rect(*box)
        out = os.path.join(ASSETS, f"{name}.png")

        # Step 1 -- high-resolution clip render.
        page.get_pixmap(clip=rect, dpi=DPI).save(out)

        # Steps 2-3 -- true monochrome + contrast recovery.
        img = Image.open(out).convert("L")
        img = ImageOps.autocontrast(img, cutoff=1)

        # Remove neighbouring-figure intrusions (see note on FIGURES above).
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

        # Report back what was written so the manifest can be filled honestly.
        check = Image.open(out)
        print(
            f"{name:12s} p{page_no:<3d} {check.size[0]:5d}x{check.size[1]:<5d} "
            f"mode={check.mode}"
        )

    doc.close()


if __name__ == "__main__":
    main()
