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
# `scrub` exists only because Figure 3.1's sub-parts are laid out as INTERLEAVED
# COLUMNS, not clean rows. All part artwork + labels are baked into one raster
# (page-3 image bbox x 68.8-494.7, y 102.0-672.3) with no text layer, so every
# boundary below was measured from a thresholded ink-profile/bbox scan of that
# raster at 200 dpi, then confirmed against a coordinate-gridded 150 dpi render.
#
# Measured extents (PDF points, page coords):
#   (a-i)  artwork  x  95-235  y 112-245   + "(a-i)"  label below it
#   (a-ii) artwork  x 330-390  y 112-266   + "(a-ii)" label x 353-390 y 270-287
#   row (b) artwork            y 296-479.5, full x 69-486
#     (b-i)   x  69-159   (b-ii)  x 186-337   (b-iii) x 353-486
#   row (c) artwork x  91-443  y 487.8-671.4
#     (c-i)   x 104-234   (c-ii)  x 295-443
#
# The single genuine collision: row (a)'s "(a-ii)" part label sits at
# x 353-390 / y 270-287, i.e. BELOW the full-width whitespace band at y=270-275
# and therefore inside any crop that starts at y=274. (b-iii) Dictyota's own
# artwork does not begin until y=309.6 and (b-i)/(b-ii) not until y=296, so
# starting row (b) at y=290 clears the "(a-ii)" label completely without
# touching a single pixel of row (b) -- no scrub rect is needed at all.
# Right edge 490 keeps (b-iii)'s "Frond" leader + label (ends x=486.2) intact.
# Row (c) is cleanly separated: nothing of row (b) reaches below y=479.5.
FIGURES = [
    # Figure 3.1 Algae -- one crop per NCERT caption sub-part, because the body text
    # itself cites "(Figure 3.1a)", "(Figure 3.1b)" and "(Figure 3.1c)" separately at
    # the end of 3.1.1, 3.1.2 and 3.1.3 respectively.
    # Row (a): measured ink x 93.5-385.1, y 112.6-289.4 (the left bound is the
    # "Daughter colony"/"Parent colony" leader text, not the Volvox artwork, and the
    # lower bound is the "(a-i)"/"(a-ii)" part labels). Padded to clear both.
    ("fig_3_1a", 3, (88.0, 106.0, 392.0, 293.0), []),
    # Row (b): starts at y=290 -- below row (a)'s "(a-ii)" label (ends y=287) and
    # above row (b)'s own topmost ink (y=296), so the neighbouring label is excluded
    # by the crop itself rather than painted out (an earlier y=274 top dragged the
    # "(a-ii)" label in). Ends at y=491, because the "(b-i)"/"(b-ii)"/"(b-iii)" part
    # labels themselves run to y=489 -- an earlier y=478/482 cut sliced them in half.
    # Right edge 490 keeps (b-iii)'s "Frond" leader + label (ends x=486.2) intact;
    # an earlier 470 edge clipped it.
    # The one scrub: (c-ii) Polysiphonia's topmost fronds reach up to y=468 in the
    # x 385-465 strip (it is a tall figure in the right-hand column), which is inside
    # row (b)'s y-band. (b-iii)'s own ink in that strip is its "Stipe" label, which
    # ends at y=466, and its artwork column ends at x=460 above y=466 -- so scrubbing
    # x 383-468 / y 469-491 removes only the (c-ii) intrusion. Verified against a
    # 400 dpi gridded render of the y 462-512 boundary strip.
    (
        "fig_3_1b",
        3,
        (64.0, 290.0, 490.0, 491.0),
        [(383.0, 469.0, 468.0, 491.0)],
    ),
    # Row (c): (c-i) Porphyra x=104-234 (incl. its "Frond" label), (c-ii)
    # Polysiphonia x=295-443 (incl. "Main axis"/"Branches"). An earlier crop started
    # at x=200, slicing (c-i) vertically and halving its "Frond" label (Step 3
    # defects (b)+(d)); another ended at y=666, clipping the "(c-ii)" part label
    # which runs to y=671.4.
    ("fig_3_1c", 3, (98.0, 484.0, 452.0, 675.0), []),
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
