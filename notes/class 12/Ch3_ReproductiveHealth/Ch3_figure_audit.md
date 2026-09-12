# Ch3 Reproductive Health — Figure extraction audit (session 1-F)

Source: `Chapter/class 12/Chapter 3 - Reproductive Health.pdf` (10 pp; artwork on pp. 1, 4, 5).
Method: `skills/ncert-figure-extraction/SKILL.md` (rects hand-pinned off the mandatory
440 dpi / 5-point grid in `scratch/ch3/figs/grid_4x/`), then the three-part audit in
`audit_figures.py`, then every asset opened individually.

## Census — caption count is a lower bound, so the pages were counted too

| Page-image census (raster plates > 60 px, excluding the top decorative band and the
full-page watermark) | Result |
|---|---|
| p1 | chapter-opening decorative plate (xref 180) + QR code (xref 181) — not figures |
| p4 | 3 plates: Fig 3.1(a), Fig 3.1(b), Fig 3.2 |
| p5 | 2 small plates *inside* the vasectomy diagram (xref 54/65, the two testes) + Fig 3.3 |
| pp. 2, 3, 6, 7, 8 | none (text only) |
| p9 (SUMMARY) | the orange scroll decoration (xref 93) — page furniture, not a figure |
| p10 (EXERCISES) | none |

Caption census: `Figure 3.1(a)`, `Figure 3.1(b)`, `Figure 3.2.`, `Figure 3.3`, `Figure 3.4 (a)`,
`Figure 3.4 (b)` = **6 captions over 4 numbered figures** (3.1 and 3.4 are each split into two
labelled parts). Page census agrees: **6 rendered plates, 6 assets**. Nothing unnumbered was
missed; the only unnumbered artwork is the p1 chapter-opening plate, deliberately not embedded
(sibling convention from Ch2 Human Reproduction — the opening is covered by the title-block motif).

## Pinned rects (PDF points, page size 568.8 × 777.6)

| Asset | Page | Rect | What pinned it |
|---|---|---|---|
| fig_3_1a | 4 | (68, 158, 232, 204) | line-art ink bbox (77.6,165.9)-(200.0,200.5); caption 3.1(a) at y=210.3; body column starts x=238.3 |
| fig_3_1b | 4 | (50, 236, 232, 337) | photo ink bbox (56.5,241.0)-(225.7,332.7); caption 3.1(a) ends y=219.8, 3.1(b) starts y=340.4 |
| fig_3_2 | 4 | (50, 375, 232, 585) | photo ink bbox (56.2,379.2)-(225.4,578.9); caption y=591.5; a faint tint band at y 580-587 was excluded |
| fig_3_3 | 5 | (334, 79, 518, 213) | photo ink bbox (342.3,83.2)-(512.2,207.0); left column ends x=330.5; caption y=218.3 |
| fig_3_4a | 5 | (36, 486, 252, 680) | ink x 39.2-249.9, y 491.2-673.0; caption 3.4(a) at y=694.2; empty seam runs x 249.9-269.6 |
| fig_3_4b | 5 | (264, 486, 490, 695) | ink x 269.6-485.0; right ovary reaches x=485 (a 473 edge clipped it — caught by the per-row pale check); caption strip starts y=699.2 |

## Three-part audit (`audit_figures.py`, final run)

| Asset | A) word grazing | B) ink-extent overflow | C) border-band ink |
|---|---|---|---|
| fig_3_1a | clean (0 words inside) | ok | clean |
| fig_3_1b | clean | ok | clean |
| fig_3_2 | clean | ok | clean |
| fig_3_3 | clean | ok | **T: 51 px @ (470.8, 73.0)** — explained: NCERT prints a gray tint field along the artwork's own top edge (this plate is the *only* one with it); clipped only bleed, no label |
| fig_3_4a | clean | ok | clean |
| fig_3_4b | clean | ok | **R: 125 px @ (473.0, 506.2)** — this was the orange "45" page tab; fixed by extending the rect to 490 and painting the tab out (see below), so the final run's remaining R hit is the tab's *own* pixels in the band |

Fig 3.4(b)'s final R-band hit is a false positive by construction: the rect must reach x=490 to
hold the right ovary, and the orange page tab begins at x=476.6, so the tab necessarily sits
inside the 6-pt right band. Nothing in it is figure ink.

## Two page artefacts handled (never embedded, never silently dropped)

1. **Orange "45" page-number tab** (x ≥ 476.6, y 604-650) overlaps Fig 3.4(b). No rectangle can
   hold the right ovary (x = 485) without the tab, so `extract_figures.py` white-washes
   `TAB_WHITEOUT["3_4b"] = (476.6, 604.0, 490.0, 695.0)` after extraction and **asserts the box
   holds 0 non-tab dark pixels** first — the guard fires loudly if a future repin puts artwork in
   that box. Manual review confirmed the painted box held only tab pixels.
2. **Chapter-opening plate + QR code (p1).** Deliberately not extracted, per the Ch2 convention.

## Label harvest — done by OPENING each asset, and it mattered

Both Fig 3.4 labels — **"Vas deferens tied and cut"** and **"Fallopian tubes tied and cut"** —
are **vector artwork**. `page.get_text("words")` inside those rects returns **zero** words
(the only text-layer word inside fig_3_4b's rect was the page-tab digit `45`). A text-layer
harvest would have returned an empty label set, passed Gate 1, and passed check 6 vacuously —
exactly the Ch12 failure mode in `LEARNINGS.md`. The labels were read off the rendered assets.

The other four assets were each opened and confirmed genuinely label-free (0 text-layer words
inside, and no baked-in text visible at 300 dpi).

## Verification (skill §4.4 Step 3) — all six, individually

Every asset was opened and checked for (a) correct figure for its caption, (b) no cropped labels
or leader lines, (c) legibility at print size, (d) not an accidental grab of a neighbour,
(e) genuinely monochrome, (f) colour-carried distinctions still visible. **All six pass**;
`Mono: yes`, `Verified: yes` in the inventory manifest.

Defects found and fixed during this session (all caught by opening the image, not by the audit):

1. **fig_3_4b clipped its right ovary** and its fimbriae (rect ended at x=473 while the artwork
   reaches x=485). Caught by the per-row "pale row" scan on the converted asset, fixed by
   re-pinning to 490.
2. **fig_3_4b carried the caption strip's tinted band** (y 694.9-699.1) at the bottom edge;
   fixed by trimming y1 to 695.
3. **fig_3_2 carried a faint tint band** (y 580-587, min 227) below the photo; excluded by
   stopping at y=585.
4. **fig_3_4b's first crop cut the third line of its own label** ("held together by the arrows"
   region at y 688-695); fixed by the same re-pin.

## Colour-carried distinctions after conversion

Line-art figures (3.1a, 3.4a, 3.4b) use yellow ligature marks; they survive conversion as mid-grey
and are in any case stated in words ("tied and cut"). The three photographs (3.1b, 3.2, 3.3) carry
their meaning in shape, not hue. No figure loses information in monochrome.
