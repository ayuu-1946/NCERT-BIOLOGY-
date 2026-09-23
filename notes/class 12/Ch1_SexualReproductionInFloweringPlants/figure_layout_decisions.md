# Figure Layout Decisions — Ch1 (Class 12) Sexual Reproduction in Flowering Plants

Operator instruction (2026-09-22, Gate 1 session): **stack figures horizontally
wherever possible** — source-preserving panels sit side by side in a
`compact_figure_row` whenever the NCERT panels are cleanly separable, instead of
one tall whole-plate stack. Decisions below are binding for Pass 2/3 re-builds;
any deviation needs a row here with before/after numbers.

## Placement table (15 numbered figures)

| Fig | Assets embedded | Placement | Why |
|-----|-----------------|-----------|-----|
| 1.1 | `fig_1_1` | single whole plate, full width | single centred diagram (L.S. of a flower); nothing to pair |
| 1.2 | `fig_1_2` | single whole plate, full width | (a) stamen and (b) anther already sit **side by side inside** the NCERT plate |
| 1.3 | `fig_1_3` | single whole plate, full width | (a)+(b) joined by an orange flow arrow; (c) below; panels share label columns — not cleanly separable (see `extract_figures.py` rect comments) |
| 1.4 | `fig_1_4` | single whole plate, full width | three SEM photos already in one row inside the plate; no (a)/(b)/(c) sub-labels, so no split |
| 1.5 | `fig_1_5a`, `fig_1_5b_top`, `fig_1_5b_lower` | **horizontal row**: (a) tetrad \| [stages stacked in right cell] | panels physically gapped; (b)'s three stages share one leader column, so they stay stacked inside their own cell |
| 1.6 | `fig_1_6` | single whole plate, full width | one photographic product band |
| 1.7 | `fig_1_7` | single whole plate, full width | (a)–(d) already side by side inside the plate; (b)'s "Syncarpous ovary" label overlaps (a)'s x-range — a per-panel rect would cut it |
| 1.8 | `fig_1_8` | single whole plate, full width | three rows sharing y-bands with leader lines running between them — not cleanly separable |
| 1.9 | `fig_1_9a`, `fig_1_9b`, `fig_1_9c` | **horizontal row**: (a)\|(b)\|(c) | three physically gapped panels, each self-labelled |
| 1.10 | `fig_1_10` | single whole plate, full width | single tall diagram (wind-pollinated plant); pairs with nothing (next figure is a different topic) |
| 1.11 | `fig_1_11a`, `fig_1_11b` | **horizontal row**: (a)\|(b) | (a) line drawing on pale field, (b) photo below it in source; cleanly separable |
| 1.12 | `fig_1_12a`…`fig_1_12e` | **horizontal row**: (a)\|(b)\|(c)\|(d)\|(e) | five self-labelled panels, two rows in source; each cleanly separable |
| 1.13 | `fig_1_13` | single whole plate, full width | (a) fertilised embryo sac + (b) dicot embryo stages form one continuous developmental sequence; wide plate (ratio ≈1.67) |
| 1.14 | `fig_1_14a`, `fig_1_14b` | **horizontal row**: (a)\|(b) | (a) dicot embryo above, (b) grass L.S. below in source; cleanly separable |
| 1.15 | `fig_1_15` | single whole plate, full width (a stacked over b) | the 2026-09-22 horizontal row (D3) was **reverted 2026-09-23** per operator instruction — keep 1.15 stacked (see D4); the panels stay cleanly separable if that ever changes |

Whole-plate assets `fig_1_9`, `fig_1_12`, `fig_1_14`, `fig_1_15` remain on disk
(valid extractions) but are **not embedded** where the sub-panel rows replace
them — this is the §4.4 third state (extracted, deliberately not embedded as
whole plates); every fact in each plate is carried by its sub-panel assets plus
the running-text label walk-throughs, and the manifest's sub-panel note lists
them.

## D3 — Fig 1.15 moved from whole plate to horizontal row (2026-09-22)

**SUPERSEDED 2026-09-23 — see D4.** The change below was made, rebuilt and
documented, then reverted in full per operator instruction. The measured
numbers are kept for the record.

- **Before (measured from the pre-change PDF, p16 image bbox):** whole plate
  (2138×2151 px, (a) stacked over (b) inside one image) rendered at
  **15.50 cm × 15.59 cm** (439.4 pt wide). The (a) block spans the full plate
  width. It did not fit the page-15 tail after the §1.4.3 label walk-through,
  so `KeepTogether` stranded it alone on page 16 and left a large blank tail
  on page 15.
- **After (measured from the rebuilt PDF, p16 image bboxes):**
  `compact_figure_row(["fig_1_15a.png", "fig_1_15b.png"],
  fractions=[0.6, 0.4])` — (a) renders **9.19 cm × 5.87 cm** (260.4 pt), (b)
  renders **6.01 cm × 2.27 cm** (170.3 pt); row + 5-line caption ≈7 cm,
  fitting the page-15 tail.
- **Linear shrink of baked labels** (labels scale with rendered width): the
  (a) block now prints at **260.4/439.4 = 59%** of its old linear size, (b)
  at **170.3/439.4 = 39%**. Measured from the assets: the baked labels in
  both panels are ≈30 px cap-top-to-descender in the 300-dpi raster, i.e.
  ≈6.5–7 pt type at the old 15.5 cm plate width; after the split (a) ≈4 pt,
  (b) ≈2.5–3 pt. Both were legible on the 100-dpi page rendering done for
  this change, but (b) is at the edge of print legibility — the guard below
  and the Gate 3(a) adjudication exist precisely because of this.
- **Why 60/40:** (a) carries 13 of the 18 in-figure labels; (b) is the
  low-density false-fruit band with 5. §4.4: "cut the cheap figure first".
- **Legibility guard:** all 18 labels are enumerated in the body text
  immediately above the row (F243 walk-through) **and** in the caption, so the
  text stands alone if a photocopy flattens the small baked labels (§4.4 Step 4
  + photocopier rule). **Gate 3(a) must adjudicate baked-label legibility of
  both cells on the rendered page.** Documented fallback: revert the one
  `compact_figure_row` call to `figure("fig_1_15.png", ..., max_width_cm=15.5)`.
- **Rebuild impact (measured):** page count unchanged (18); p16 +1,206 chars /
  +1 image, p17 +131 chars, p18 −1,283 chars; `check_pdf.py` exit 0
  (0 fail / 0 warn) on the rebuilt PDF.

## D4 — Fig 1.15 reverted to the stacked whole plate (2026-09-23)

Operator instruction 2026-09-23: **do not place 1.15's (a) and (b) side by
side — keep 1.15 stacked.** The single `compact_figure_row([...],
fractions=[0.6, 0.4])` call was replaced with the original
`figure("fig_1_15.png", max_width_cm=15.5)` (the one-line fallback
documented in D3). The `fractions` parameter of `compact_figure_row`
remains in the template (default equal; unused by any call site after this
revert).

- **Rebuild impact (measured):** the rebuilt PDF is **page-for-page
  identical** to the pre-change PDF — 18 A4 pages, 0 per-page char/image
  deltas; `check_pdf.py` exit 0 (0 fail / 0 warn): 25 embedded mono images,
  108/108 labels, 255/255 ticked, smallest glyph 6.0 pt, 64 banners no
  orphan, 105 plates no collision.
- **Carry-over C2 (baked-label legibility) of the inventory Gate 1 record is
  resolved by this revert** — at the full 15.5 cm plate width both (a) and
  (b) labels print at ≈6.5–7 pt, and the Gate 3(a) inspection needs no
  special legibility adjudication for Fig 1.15.
- The sub-panel assets `fig_1_15a` / `fig_1_15b` remain on disk (valid
  extractions, label-verified) but are not embedded.

## Non-figure placements (context)

- The p2 Panchanan Maheshwari portrait and the p3 decorative chapter plate are
  **not extracted** (no person photograph is ever embedded — §4.4 hard no; the
  p3 plate carries zero facts).
- `compact_figure_row` uses 5 pt internal cell padding and a 0.5 pt `#555555`
  box per cell; row is wrapped with its caption in `KeepTogether`.
