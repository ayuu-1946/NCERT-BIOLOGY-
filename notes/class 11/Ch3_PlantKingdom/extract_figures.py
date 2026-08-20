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
# Measured extents (PDF points, page coords) -- re-measured at 400 dpi with a
# threshold<150 ink scan (rejects the faint NCERT watermark):
#   (a-i)  artwork  x  95-235  y 112-245   + "(a-i)"  label below it
#   (a-ii) artwork  x 330-390  y 112-266   + "(a-ii)" label x 354.2-385.2 y ..281.8
#   row (b)  y 274-491, full x 69-486
#     (b-i)   x  69-159   frond tip starts y=274.7 (x 92.0-112.3) | label y ..484.2
#     (b-ii)  x 186-337   artwork from y=300.8    | label y ..484.2
#     (b-iii) x 353-486   artwork from y=309.2    | label x 401.2-453.6 y 468-490
#                         "Stipe" label x 415-461.3 y 450-473.9
#   row (c) artwork x  91-443, (c-ii) top ink y=469.0
#     (c-i)   x 104-234  (rises into y491+ at x 313.3-344.1)
#     (c-ii)  x 295-443  (intrudes into row (b) at x 345.4-374.1, y 469+)
#
# TWO genuine collisions, both handled:
#   1. Rows (a)/(b) have NO horizontal gutter. "(a-ii)" ends y=281.8 at x 354-385
#      while (b-i)'s frond tip starts y=282 at x 92-111 -- they are separated
#      horizontally, not vertically. Top edge y=282 therefore takes all of (b-i)
#      and none of "(a-ii)". (An earlier y=290 clipped the frond tip; a still
#      earlier y=274 dragged "(a-ii)" in.)
#   2. (c-ii) Polysiphonia is tall enough to reach up into row (b)'s y-band, but
#      it does so at x 345.4-374.1 -- in the gutter between (b-ii) and (b-iii),
#      NOT under (b-iii)'s labels. x376-400 is zero-ink across y455-500, so one
#      scrub of x 344-377 / y 469-491 removes it cleanly.
# Right edge 490 keeps (b-iii)'s "Frond" leader + label (ends x=485.9) intact.
# Row (c)'s own crop starts at y=484 and is unaffected by either collision.
FIGURES = [
    # Figure 3.1 Algae -- one crop per NCERT caption sub-part, because the body text
    # itself cites "(Figure 3.1a)", "(Figure 3.1b)" and "(Figure 3.1c)" separately at
    # the end of 3.1.1, 3.1.2 and 3.1.3 respectively.
    # Row (a): measured ink x 93.5-385.1, y 112.6-289.4 (the left bound is the
    # "Daughter colony"/"Parent colony" leader text, not the Volvox artwork, and the
    # lower bound is the "(a-i)"/"(a-ii)" part labels). Padded to clear both.
    # One scrub: (b-i)'s Laminaria frond tip rises to y=274.7 (x 92.0-112.3), inside
    # row (a)'s y-band, so it lands in the bottom-left corner of this crop. The
    # y255-273 band is entirely clear and x112-344 is clear through y283, so (a-i)'s
    # own artwork/label is nowhere near that corner; scrubbing x 88-114 / y 274-293
    # removes only the row-(b) intruder.
    ("fig_3_1a", 3, (88.0, 106.0, 392.0, 293.0), [(88.0, 274.0, 114.0, 293.0)]),
    # Row (b): top edge y=274. There is NO clean horizontal gutter between rows (a)
    # and (b) -- a 400 dpi 1-pt row scan of x88-200 / y255-293 shows (b-i)'s Laminaria
    # frond tip beginning at y=274.7 (x 92.0-112.3) and running unbroken downward,
    # while row (a)'s "(a-ii)" label occupies x 354.2-385.2 down to y=281.8. In the
    # y274-283 band those are the ONLY two ink bodies (x112-344 is zero-ink), so the
    # two rows are separated HORIZONTALLY, not vertically. y=274 therefore takes the
    # whole frond tip; the "(a-ii)" tail it also admits is removed by the third scrub
    # below. An earlier y=290 top edge sliced ~16 pt off the frond tip, and an
    # intermediate y=282 fix still lost its top ~8 pt.
    # Bottom edge y=491: measured part-label extents are (b-i)/(b-ii) y..484.2 and
    # (b-iii) y 468.0-490.0, so y=491 clears all three (an earlier y=478/482 cut
    # sliced them). Nothing of row (b) exists below y=491.
    # Right edge 490 keeps (b-iii)'s "Frond" leader + label (ends x=485.9) intact;
    # an earlier 470 edge clipped it. x470-500 holds only that leader (y342.5-348.8).
    # Row (b) needs TWO scrubs, one per row-(c) intruder that breaks into its box.
    # Scrub 1 -- (c-ii) Polysiphonia's top-right intrusion, RE-MEASURED:
    # a 1-pt row scan of x344-378 / y462-496 puts the intruder's first ink at
    # y=469.0 and its horizontal span at x 345.4-374.1, i.e. it sits in the gap
    # BETWEEN (b-ii) and (b-iii), well left of (b-iii)'s labels. x376-400 is a
    # zero-ink gutter over the whole y455-500 band, and (b-iii)'s own ink in this
    # y-range is its "Stipe" label (x 415-461.3, y 450-473.9) plus the "(b-iii)"
    # part label (x 401.2-453.6, y 468-490). Scrubbing x 344-377 / y 469-491 therefore
    # removes the intrusion and nothing else.
    # NB: the previous scrub rect (383, 469, 468, 491) was wrong on BOTH axes -- it
    # painted out a clear gutter (x383-400) plus (b-iii)'s "Stipe" and "(b-iii)"
    # labels, while leaving the real intruder at x344-376 fully intact.
    (
        "fig_3_1b",
        3,
        (64.0, 274.0, 490.0, 491.0),
        [
            (344.0, 469.0, 377.0, 491.0),
            # Third scrub -- the cost of the y=274 top edge: row (a)'s "(a-ii)" part
            # label tail, measured at x 359.5-378.0 / y 274.4-281.7. Row (b)'s own
            # topmost ink in this x-range is (b-iii)'s artwork, which does not begin
            # until y=309.2, and x112-344 is zero-ink through y283, so scrubbing
            # x 350-390 / y 274-284 removes the label tail and nothing of row (b).
            (350.0, 274.0, 390.0, 284.0),
            # Second, much smaller intrusion: (c-i) Porphyra's topmost frond tip
            # breaks the y=491 bottom edge. Measured at 600 dpi over x305-345 /
            # y483-491, its true bbox is x 318.80-329.36 / y 489.12-490.92 -- i.e.
            # a ~10.5 x 1.8 pt sliver, and everything above y=489.1 in that strip
            # is clear. Scrub x313-334 / y486-491 covers it with margin on all four
            # sides (a tighter x317-329 rect leaves 3 stray px at x~329.1-329.4).
            # Row (b)'s nearest own content is the "(b-ii)" part label, which ends
            # at x=273.2 / y=484.2, so this scrub touches nothing that belongs.
            (313.0, 486.0, 334.0, 491.0),
        ],
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
    # Bottom edge y=469 keeps both part labels while excluding the caption, whose
    # first ink begins below y=470; the earlier y=488 crop included caption text.
    ("fig_3_5ab", 12, (219.0, 271.0, 501.0, 469.0), []),
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
