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
| 1.12 | `fig_1_12a`…`fig_1_12e` | **two horizontal rows**: (a)\|(b)\|(c) then (d)\|(e) — **changed 2026-09-23, see D5** | five self-labelled panels; operator instruction: a b c on one line, then d and e |
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

## D5 — Fig 1.12 split into two rows + caption bands removed from all whole-plate assets (2026-09-23)

Operator instruction 2026-09-23: **stack 1.12's (a)(b)(c) together on one
line, then (d)(e) on the next line; use precise grids; captions must NOT be
in the figure assets because captions are written by the template rule.**

### 1.12 layout (two rows, one caption)

`compact_figure_row` gained `caption_text=None` (returns the bare row). The
Fig 1.12 block is now

```
KeepTogether([
    compact_figure_row([fig_1_12a, fig_1_12b, fig_1_12c], None),   # row 1: a b c
    compact_figure_row([fig_1_12d, fig_1_12e], None),              # row 2: d e
    Paragraph("Fig. 1.12 — ...", STYLES["Caption"]),               # one caption
])
```

Measured on the p16 4× grid (`scratch/ch1_figs/grid_4x/p16.png`): the NCERT
"Figure 1.12 …" caption box (cream background) sits at source y≈470–543 pt,
**below all five panel regions** (panels end at y≤430), so no 1.12 asset ever
contained the caption. The text "Longitudinal section of a flower showing
growth of pollen tube" under panel (c) is an **in-figure label** (sits inside
the (c) panel, above the "(c)" marker) and is retained — the template
caption rule writes the "Figure 1.12 …" line, not in-figure labels.

### Caption bands removed from the 13 whole-plate assets

Audit of every asset's bottom strip found the NCERT "Figure 1.x …" caption
line (on the cream caption box) baked into **all 13 committed whole plates** —
1.1, 1.2, 1.3, 1.4, 1.6, 1.7, 1.8, 1.9, 1.10, 1.12, 1.13, 1.14, 1.15 — while
the template also prints its own caption below each figure: every whole-plate
figure in the PDF had a doubled caption. The sub-panel assets (1.5 set,
1.9a–c, 1.11a–b, 1.12a–e, 1.14a–b, 1.15a–b) were verified caption-free and
left untouched.

Method (per the "precise grids" instruction, with the registered-raster
caveat): a fresh render of the current source raster was compared against
the committed assets — the current raster is **registration-shifted**
(fig 1.1's "Style" label starts x≈165 in the current raster but fits at
x≥180 in the verified committed raster), so re-rendering at the same rects
would clip labels. The committed raster is the verified record, so each
whole plate was **bottom-cropped in place** at a pixel-precise line measured
from the asset's own row-ink profile (dense text-row detection, central
window, cream-box-top detection), 10 px above the first caption line (or
3 px above the cream box top where the box padding extends above the text):

| asset | new height (px) | cut removes |
|---|---|---|
| fig_1_1 | 1368 | 1-line caption |
| fig_1_2 | 1452 | 2-line caption + partial prose line below it |
| fig_1_3 | 1650 | 2-line caption ("(c)" letter kept) |
| fig_1_4 | 566 | 1-line caption |
| fig_1_6 | 733 | 1-line caption |
| fig_1_7 | 1271 | 3-line caption ((a)–(d) letters kept) |
| fig_1_8 | 1692 | 3-line caption + cream box top (Micropylar end/(c) labels kept) |
| fig_1_9 | 2224 | 3-line caption + the page-number "12" box + grey margin bars |
| fig_1_10 | 1360 | 2-line caption + partial prose line below it |
| fig_1_12 | 1599 | 5-line caption ((d)/(c) letters kept) |
| fig_1_13 | 1048 | 2-line caption ((a)/(b) letters kept) |
| fig_1_14 | 1998 | 3-line caption ("(b)" letter + Coleorhiza kept) |
| fig_1_15 | 2067 | 1-line caption ("Mesocarp"/(b) kept) |

Audit: 0 dark ink in the final 20 px above each new bottom edge (no glyph
clipped); all 13 new bottom edges visually verified (contact sheet
`scratch/ch1_gate1/final_bottoms.png`); all 10 embedded whole plates checked
in PDF context (caption zones `scratch/ch1_gate1/v2_caption_zones.png` —
single template caption, no cream sliver, no page furniture). Pre-crop
backup: `scratch/ch1_gate1/assets_backup_precaption/`. Top/left/right edges
unchanged (bottom-only crop ⇒ upper content structurally identical).

`extract_figures.py`'s rect list intentionally still records the
**source-side** geometry (y1 down to the caption); the shipped whole-plate
assets sit a few points inside the rect bottom after the trim.

### Rebuild (2026-09-23)

18 A4 pages; `check_pdf.py` **exit 0 — 0 fail / 0 warn**; 108/108 labels;
255/255 ticked; smallest glyph 6.0 pt; 107 plates no collision; 67 banners
no orphan. Fig 1.12 renders on PDF p12 (rows a|b|c / d|e + one caption),
Fig 1.15 on PDF p16 (stacked whole plate, caption-free plate + one caption).

## Non-figure placements (context)

- The p2 Panchanan Maheshwari portrait and the p3 decorative chapter plate are
  **not extracted** (no person photograph is ever embedded — §4.4 hard no; the
  p3 plate carries zero facts).
- `compact_figure_row` uses 5 pt internal cell padding and a 0.5 pt `#555555`
  box per cell; row is wrapped with its caption in `KeepTogether`.
