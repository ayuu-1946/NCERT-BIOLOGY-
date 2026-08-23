# Frozen Inventory — Chapter 7: Human Health and Disease (Class XII)

**Status: PASS 1 INCOMPLETE — Gate 1 NOT met.**

This file currently holds the output of **session 1-F only** (figure extraction).
It is a partial inventory, deliberately published in this state so that the work
already done is durable and auditable. Four of the five mandatory Pass 1 sessions
have **not** run. See "Session log" and "What is missing" below before using this
file for anything.

Source PDF: `Chapter/class 12/Chapter 7 - Human Health and Disease.pdf` (22 pages).

---

## Session log — Pass 1

| Session | Scope | State |
|---|---|---|
| **1-F** | Figures: census, rect pinning, extraction, three-part audit, label matrix | **complete** (2026-08-23) |
| 1-S | Source read + Facts inventory (`F###` rows) | **not started** |
| 1-H | Structural census (heading sweep) | **not started** |
| 1-O | Section-opener census | **not started** |
| 1-Z | Independent re-verification / count derivation | **not started** |

Session 1-F was executed across two sittings. The first (previous chat) pinned the
rects, ran the audit and reviewed a contact sheet, but **ran out of budget before
writing any inventory file** and did not commit its audit script. The second
(this session) rebuilt the environment, re-derived every machine claim from
scratch, re-opened all 11 assets, and wrote this file.

### What is missing

`§6` requires Pass 1 to span **five** sessions, each with its own machine-derived
row count. Gate 1 cannot be claimed until 1-S, 1-H, 1-O and 1-Z have each run as
their own session. Specifically absent from this file:

- the **Facts table** (`F###` rows) — the substance of the chapter
- **Header counts** and the step-10 **count derivation**
- **Structural census** (headings) and **opener census**
- **Summary classification** (BODY-PRESENT vs SUMMARY-UNIQUE)
- **Exercise-gap terms**
- any **Gate 1 checklist**

Do not treat the figure work below as evidence that the chapter is inventoried.

---

## Re-derivation notes (this session)

Per `§6`, a handoff's findings are **claims to re-derive**, not facts to inherit.
Everything below was re-measured in this session against the source PDF; nothing
was copied forward on trust. Three discrepancies with the inherited account were
found and are recorded honestly rather than smoothed over:

1. **The extract script's own comment for fig 7.10 quotes stale overflow numbers.**
   It records "Check B still reports L2.8/T14.3/R7.6". Against the *current*
   (re-pinned) rect the same underlying gradient extents give **L4.8/T9.3/R11.6**.
   The old figures were measured against the *pre-re-pin* rect `(348, 224, 460, 366)`.
   Same shapes, same conclusion — the comment's arithmetic is just one revision behind.
2. **`fig_7_5` overflows left by 24.8 pt** under a raster-extent check. The
   inherited audit table never recorded this. Verified harmless this session: the
   silhouette raster's bbox starts at x=29.2 but its **first inked column is
   x=57.9** (300 dpi probe, thr 205), and the rect's left edge at x=54 clears
   real ink by 4.1 pt. It is the raster's own white margin.
3. **`fig_7_8` and `fig_7_11` had NO working mechanical edge check.** Both plates
   are rendered as thousands of sub-pixel scanline tiles (~6 x 0.2 pt each), so
   check B finds 0 drawings and check B2's 3 pt size floor discards every tile.
   Both reported clean only because they were **vacuous**. A new **check B3**
   (tile union, no size floor) was written to give them real coverage; both pass.

A fourth item is not a discrepancy but is worth stating: the previous session's
reproducibility claim was re-tested properly. Re-running `extract_figures.py`
regenerates all 11 PNGs **byte-identical** to the committed ones (verified via
`git status` on the assets directory, after a first attempt at this check was
caught being vacuous — a `sed` had stripped the md5 hashes and compared only
filenames).

---

## Figure manifest

11 numbered figures, 7.1-7.11, on artwork pages 6, 7, 9, 12, 13, 16, 17. All 11
assets are single-channel greyscale (`PIL` mode `L`), verified mechanically this
session, so the monochrome check is satisfied by construction. Captions verbatim
from the PDF text layer.

| Fig # | Caption (verbatim) | Asset file | Src page | Mono | Opened |
|---|---|---|---|---|---|
| Figure 7.1 | Stages in the life cycle of Plasmodium | `assets/fig_7_1.png` | 6 | yes (L) | yes |
| Figure 7.2 | Diagram showing inflammation in one of the lower limbs due to elephantiasis | `assets/fig_7_2.png` | 7 | yes (L) | yes |
| Figure 7.3 | Diagram showing ringworm affected area of the skin | `assets/fig_7_3.png` | 7 | yes (L) | yes |
| Figure 7.4 | Structure of an antibody molecule | `assets/fig_7_4.png` | 9 | yes (L) | yes |
| Figure 7.5 | Diagrammatic representation of Lymph nodes | `assets/fig_7_5.png` | 12 | yes (L) | yes |
| Figure 7.6 | Replication of retrovirus | `assets/fig_7_6.png` | 13 | yes (L) | yes |
| Figure 7.7 | Chemical structure of Morphine | `assets/fig_7_7.png` | 16 | yes (L) | yes |
| Figure 7.8 | Opium poppy | `assets/fig_7_8.png` | 16 | yes (L) | yes |
| Figure 7.9 | Skeletal structure of cannabinoid molecule | `assets/fig_7_9.png` | 17 | yes (L) | yes |
| Figure 7.10 | Leaves of Cannabis sativa | `assets/fig_7_10.png` | 17 | yes (L) | yes |
| Figure 7.11 | Flowering branch of Datura | `assets/fig_7_11.png` | 17 | yes (L) | yes |

**Asset count reconciliation:** 11 numbered NCERT figures -> **11** asset files.
No figure in this chapter is split into separately-captioned sub-plates, and there
is no unnumbered bonus diagram (unlike Ch5's central-dogma schematic). The
denominator is **11** everywhere it appears.

**Crop convention:** captions are excluded from every crop, because this project's
notes restate each caption in running text. Every rect's bottom edge stops short
of its caption's `y0`.

### Deliberate exclusions (census re-derived this session)

A page-by-page sweep of all 22 pages for non-furniture rasters and sizeable
drawings returns ink-bearing regions on exactly the 7 artwork pages above, plus
four regions that are **not** assets:

| Page | Region | Why excluded |
|---|---|---|
| 2 | M.S. Swaminathan portrait photograph, `(57, 272, 166, 395)` | `§5` item 3 / `§4.4` "Hard no": a scientist portrait is never embedded, greyscaled or not. |
| 3 | Chapter-opener title plate, `(344, 56, 525, 213)` + QR thumbnail | Page furniture / title block. The tilted thumbnail merely re-prints fig 7.4's antibody artwork; it carries no fact of its own. |
| 21 | Orange wheat-ear motif beside SUMMARY box, `(407, 439, 455, 705)` | Decoration. |
| 22 | Same motif, `(126, 84, 174, 265)` | Decoration. |

All other pages (1, 4, 5, 8, 10, 11, 14, 15, 18, 19, 20) carry only the 1-2
furniture drawings — the header band and the full-page
"(c) NCERT / not to be republished" watermark.

### Rects, as frozen by session 1-F

Rects are in PDF points on the artwork page; page box is 568.8 x 777.6. Pinned by
hand off a 20 pt coordinate grid (`scratch/ch7_figs/grid/pNN.png`), because — see
the label matrix below — **every** in-figure label in this chapter is artwork, so
no text-layer method can find the plate boundaries.

| Asset | Src page | Rect (pt) | Kind |
|---|---|---|---|
| `fig_7_1` | 6 | (53, 83, 536, 610) | vector + raster, full-page plate |
| `fig_7_2` | 7 | (325, 79, 513, 351) | raster illustration |
| `fig_7_3` | 7 | (267, 414, 508, 533) | raster photograph |
| `fig_7_4` | 9 | (213, 290, 521, 530) | vector panel + raster tint |
| `fig_7_5` | 12 | (54, 80, 206, 302) | raster silhouette + vector labels |
| `fig_7_6` | 13 | (84, 81, 469, 532) | pure vector schematic |
| `fig_7_7` | 16 | (122, 545, 298, 696) | vector skeletal formula |
| `fig_7_8` | 16 | (374, 538, 495, 694) | raster-tile illustration |
| `fig_7_9` | 17 | (50, 215, 263, 366) | vector skeletal formula |
| `fig_7_10` | 17 | (350, 219, 456, 364) | vector panel, mid-tone fills |
| `fig_7_11` | 17 | (326, 395, 515, 586) | raster-tile illustration |

NCERT sets 7.2, 7.3, 7.4, 7.5 and 7.11 *beside* a body-text column, so an
automatic ink box would sweep the neighbouring paragraph in; each of those rects
is clipped against the prose column's own x boundary taken from `get_text("words")`.

---

## Figure-label matrix

Eleven rows, one per asset. Rows for the six assets with no descriptive callouts
are worded so they do **not** begin `Figure labels`, because `check_pdf.py`'s
`_extract_labels` falls back to semicolon-splitting an unquoted body — a row
reading "Figure labels: (none)" would manufacture a phantom label that no running
text could ever satisfy. The column header is worded the same way, for the same
reason. The parser reads column index 3, so this table's shape is load-bearing.

Labels were harvested by **opening each rendered asset** in this session, never by
text extraction. This chapter is the textbook case for that rule: a
`page.get_text("words")` sweep returns **zero** words inside all 11 rects (see the
audit table below) even though figs 7.1, 7.4, 7.5 and 7.6 carry 30 callouts
between them. Every label is baked into the artwork.

| ID | Fig # | Type | Label row wording | Ticked |
|----|-------|------|-------------------|--------|
| — | Fig 7.1 | label | Figure labels: "Sporozoites"; "Salivary glands"; "Mosquito Host"; "Human Host"; "Gametocytes"; "Male"; "Female" | x |
| — | Fig 7.2 | label | No in-figure labels — unlabelled illustration of a seated man with elephantiasis of the lower limbs | x |
| — | Fig 7.3 | label | No in-figure labels — unlabelled photograph of a ringworm lesion on the chin and jaw | x |
| — | Fig 7.4 | label | Figure labels: "Antigen binding site"; "Light chain"; "Heavy chain" | x |
| — | Fig 7.5 | label | Figure labels: "Lymph nodes"; "Thymus"; "Lymphatic vessels" | x |
| — | Fig 7.6 | label | Figure labels: "Retrovirus"; "Viral RNA core"; "Viral protein coat"; "Animal cell"; "Plasma membrane"; "Cytoplasm"; "Nucleus"; "DNA" | x |
| — | Fig 7.7 | label | No descriptive callouts — skeletal formula bearing only atom/group symbols (HO, O, H, N, CH3) | x |
| — | Fig 7.8 | label | No in-figure labels — unlabelled illustration of an opium poppy plant | x |
| — | Fig 7.9 | label | No descriptive callouts — skeletal formula bearing only atom/group symbols (OH, O, H) | x |
| — | Fig 7.10 | label | No in-figure labels — unlabelled framed illustration of a Cannabis sativa leaf | x |
| — | Fig 7.11 | label | No in-figure labels — unlabelled illustration of a flowering Datura branch | x |

**Parsed label total: 21** (7 + 3 + 3 + 8), across 4 labelled assets. The seven
non-`Figure labels` rows contribute 0 and are invisible to the parser by design.

`F###` IDs are left as `—` because the Facts table does not exist yet; session 1-S
must assign them and 1-Z must reconcile this matrix against them.

### Labels deliberately NOT quoted, and the obligations they create

Three sets of in-figure text are real but are **not** quoted above, because
quoting them would create check-6 requirements that are either unsatisfiable or
meaningless. Each becomes an explicit Pass 2 obligation instead:

- **fig 7.4's chain-terminus markers `N` and `C`.** Single characters.
  `_coverage_ratio` strips tokens of length 1, then falls back to a bare `\bn\b`
  word-boundary search — which any stray "n" in the notes would satisfy, so the
  check would be noise either way. **Obligation:** the antibody passage must name
  the amino (N) and carboxyl (C) termini of the chains in running text.
- **The `S-S` disulfide-bridge markers in fig 7.4.** Numerous, and not a
  descriptive callout. **Obligation:** the passage must state that the chains are
  held together by disulfide bonds.
- **The process-arrow sentences in figs 7.1 and 7.6.** These are full sentences,
  not labels ("When the mosquito bites another human, sporozoites are injected
  with bite.", "Viral DNA is produced by reverse transcriptase", the in-plate
  "NOTE: Infected cell can survive while viruses are being replicated and
  released", and 11 others). Listing them as labels would misuse the mechanism.
  **Obligation:** their content must be carried by the Facts rows for the malaria
  life cycle and HIV replication, which session 1-S must create. **This is the
  single biggest carry-over from 1-F and must not be lost.**

---

## Extraction gate record (five-part audit, session 1-F)

Run: `/vercel/share/neetenv/bin/python scratch/ch7_figs/audit.py`
(script rebuilt and committed this session; the previous sitting's copy was lost).

| Asset | A) word grazing | B) drawings overflow | B2) raster overflow | B3) tile union | C) dark border ink | C2) light border ink |
|---|---|---|---|---|---|---|
| `fig_7_1` | **vacuous** (0 words) | ok (1250 shapes) | ok | ok (4276 tiles) | clean | explained (page-number tab) |
| `fig_7_2` | **vacuous** (0 words) | no drawings | ok (1 raster) | ok | clean | explained (corner motif) |
| `fig_7_3` | **vacuous** (0 words) | no drawings | ok (1 raster) | ok | clean | clean |
| `fig_7_4` | **vacuous** (0 words) | ok (1180 shapes) | ok | ok (81 tiles) | clean | clean |
| `fig_7_5` | **vacuous** (0 words) | ok (35 shapes) | OVERFLOW L24.8 — **explained** | OVERFLOW L24.8 — **explained** | clean | explained (corner motif) |
| `fig_7_6` | **vacuous** (0 words) | ok (4944 shapes) | no rasters | no tiles (pure vector) | clean | clean |
| `fig_7_7` | **vacuous** (0 words) | ok (26 shapes) | ok | ok (59 tiles) | clean | clean |
| `fig_7_8` | **vacuous** (0 words) | **vacuous** (0 drawings) | **vacuous** (3x3 px tile only) | ok (1804 tiles) | clean | clean |
| `fig_7_9` | **vacuous** (0 words) | ok (16 shapes) | ok | ok (59 tiles) | clean | clean |
| `fig_7_10` | **vacuous** (0 words) | OVERFLOW L4.8 T9.3 R11.6 — **explained** | **vacuous** (5x3 px tile only) | ok (582 tiles) | clean | clean |
| `fig_7_11` | **vacuous** (0 words) | **vacuous** (0 drawings) | **vacuous** (0 rasters) | ok (4878 tiles) | clean | clean |

### Notes on this chapter's audit

- **Check A is vacuous for all 11 assets.** Zero text-layer words fall inside any
  rect — not even a panel letter. Check A therefore provides **no** evidence
  whatsoever about crop quality in this chapter and must never be cited as if it
  did. B/B2/B3/C/C2 plus the eyeball carried this gate.
- **Check C2 (light threshold, grey < 205) was required.** The skill's standard C
  uses grey < 110, but the fig 7.10 cannabis leaf is mid-green (luma ~177) inside
  a pale grey frame, i.e. the entire plate sits *above* the dark threshold. C
  passed on it while the crop was in fact clipping the panel border. All three
  surviving C2 hits are page furniture, each identified by coordinate:
  `fig_7_1` bottom = the orange page-number tab ("132", ink from y=611.8, x 53-92);
  `fig_7_2` top = the top-right leaf/corner motif at y~73, x 469-502;
  `fig_7_5` top = the top-left corner motif at y~74. `fig_7_10`'s top band is now
  **clean**, which is the mechanical confirmation that the re-pin worked.
- **Check B3 was added this session** and is not optional for Ch7. Figures 7.8 and
  7.11 are stipple/scanline artwork built from ~1800 and ~4900 sub-pixel raster
  tiles; B (drawings) and B2 (rasters >= 3 pt) are both blind to them. Before B3
  those two plates had **no** mechanical edge check at all and were passing
  vacuously. With B3 the tile unions land at
  `x 373.0-491.2, y 541.0-694.1` (fig 7.8, inside its rect to within 1.0 pt) and
  `x 330.6-510.1, y 395.9-580.1` (fig 7.11, comfortably inside).
- **`fig_7_5`'s L24.8 overflow is the raster's own white margin,** not a clip: the
  silhouette raster bbox begins at x=29.2, but a 300 dpi column scan (thr 205)
  puts the first inked column at **x=57.9**, and the rect's left edge is x=54.
  The `Lymph nodes` / `Thymus` / `Lymphatic vessels` labels are vector and run
  right to x=201.7, which is why the box must span to x=206.
- **`fig_7_10`'s B overflow is explained by clipping, not truncation:** the leaf's
  gradient shapes are *defined* out to `x 345.2-467.6, y 209.7`, but they are
  clipped by the panel's own clip path, so no ink renders outside the frame. The
  thr-205 probe, check C2, and the opened asset all agree the frame is intact.
- **Page furniture excluded from every measurement:** the full-page watermark
  (~`(46, 191, 508, 653)` raster, present on every page), the dark green header
  band (y < 76), the brown/orange corner motifs, the right-margin decorative band,
  and the orange page-number tab.

### Rects re-pinned during session 1-F

| Asset | Was | Now | Why |
|---|---|---|---|
| `fig_7_10` | (348, 224, 460, 366) | (350, 219, 456, 364) | Check B flagged T14.3 overflow and the eyeball confirmed ~1.5 pt of the panel's top border was sliced off. The dark-ink probe had reported the plate starting at y=230.2 only because the whole figure is mid-tone; a thr-205 re-probe put the panel at `x 352.3-454.6, y 222.5-361.0` (shadow included). Rect widened to clear it by ~2 pt. |

### Visual verification

All 11 assets were opened and inspected at full size in this session (not merely
contact-sheeted). Each renders complete: fig 7.1 shows all ten callouts and both
host loops; fig 7.4 shows the rounded panel with `N` at top and both `C` termini at
bottom; fig 7.6 shows the outer panel and the in-plate NOTE line; fig 7.10 shows
all four panel borders plus the drop shadow, confirming the re-pin. No crop clips
artwork and none admits body text.

One cosmetic observation, recorded and dismissed: `fig_7_5` includes a faint grey
horizontal rule at its very bottom edge (the caption block's top rule, `y0=306.0`
vs the rect's bottom at 302). It is a rule, not text, and carries no content.

---

## Carry-over to later sessions

1. **1-S must create the Facts table**, and must cover the 14 process-arrow
   sentences in figs 7.1 and 7.6 plus the three unquoted label sets listed above.
2. **1-Z must assign `F###` IDs** to the 11 label-matrix rows and reconcile them.
3. **`check_pdf.py` check 6 cannot pass meaningfully until 1-S exists** — there is
   no running text yet for the 21 parsed labels to be found in.
4. The `extract_figures.py` docstring's stale fig 7.10 overflow numbers
   (`L2.8/T14.3/R7.6`, measured against the superseded rect) should be corrected
   to `L4.8/T9.3/R11.6` when that file is next touched, so a future session does
   not mistake the mismatch for a regression.
