# Ch5 Morphology of Flowering Plants (Class 11) — Tracker

**Status: ▶️ GATE 1 CLOSED (2026-09-09). Pass 2 not started.**

Gate 1 closed is **not** chapter closed. There is no script, no PDF, and all 280 inventory
rows are unticked. This chapter must not appear in any "Done" tally — Done requires Gate 3.

| Gate | State |
|---|---|
| **Gate 1** — frozen, machine-validated inventory | ✅ **CLOSED 2026-09-09** |
| **Gate 2** — `check_pdf.py` exits 0 | ⬜ not started (no script, no PDF) |
| **Gate 3** — zero confirmed defects | ⬜ not started |

## Environment (section 1 preamble)

The venv was **absent at session start** — the expected state, since the sandbox resets
between sessions — and was rebuilt and version-verified **before anything was diagnosed**:

```
Python 3.13.15 @ /vercel/share/neetenv · reportlab 5.0.1 · pdfplumber OK
pymupdf 1.28.2 · Pillow 12.3.0
```

This matches the known-good baseline. `numpy` was additionally installed for this chapter's
`audit_figures.py` (carry-over 8 in the inventory).

## Starting state

`CHAPTER_TRACKER.md` listed this chapter as "⬜ Not done". On disk, session **1-F** had
already run in a prior task: 17 assets `fig_5_1.png`…`fig_5_17.png`, a re-pin log, and a
three-part crop audit recorded as clean.

The inventory, however, was **extraction-only**. It held a figure table and production notes
but **no Facts table, no heading sweep, no opener sweep, no summary classification, no
exercise-gap classification, and no figure-label matrix in the format `check_pdf.py`'s
`_extract_labels` parses**. Had a script ever been built against it, check 6 would have had
nothing to verify and check 7 nothing to tick.

This is the same shape previously hit on Ch12 (Respiration in Plants) and Ch6 (Anatomy of
Flowering Plants), where the standing decision is that a substandard inventory is **rebuilt
to the section-6 Gate 1 standard rather than patched**. That is what this session did.

## Pass 1 — all five sessions ran, each reporting its own machine-derived count

| Session | Work | Rows contributed |
|---|---|---|
| **1-S** | Full source read, then two independent prose sweeps over all 16 pages | **211** content rows |
| **1-H** | Heading sweep, walked as its own list | **30** `heading` rows (20 numbered + 4 structural + 6 unnumbered) |
| **1-O** | Opener sweep, first sentence of every section | **21** `opener` rows |
| **1-F** | Figures re-run: 17 assets re-pinned, regenerated, re-verified by opening | **11** `figure-labels` rows / **56** labels |
| **1-Z** | Exercise-gap scan, summary classification and folds, freeze, machine counts | **7** `summary-unique` fold rows |

Inventory **FROZEN at 280 rows, `F001`–`F280`** — contiguous, monotonic, 0 gaps, 0 duplicate
IDs, **0 ticked**. Type census: 14 values, all lowercase, summing to 280.

## Gate 1 closure — earned by machine

`scratch/ch5morph_gate1/gate1_close.py` returns **VERDICT GREEN, 37 pass / 0 fail**. It
imports `check_pdf.py`'s own `_extract_labels` rather than replicating it, and asserts:

- **Label parse:** **11 label-bearing figures / 56 in-figure labels, no doubling, no phantom
  `Fig #` row.** Per figure — 5.1=11 · 5.2=4 · 5.3=5 · 5.4=5 · 5.5=3 · 5.6=3 · 5.10=5 ·
  5.13=4 · 5.14=6 · 5.15=9 · 5.16=1.
- **ID integrity:** `F001`–`F280`, contiguous, monotonic, no gaps, no duplicates, 0 ticked.
- **Header agreement:** every count restated in the header block equals a re-parse of the
  Facts table, including each census total against the length of its own adjacent list.
- **Structure:** all 20 numbered source headings have a `heading` row *in source order*, and
  every numbered section plus the chapter intro has exactly one `opener` row.
- **Manifest agreement:** every manifest crop rect and source page equals
  `extract_figures.py`'s — the script that actually produced the assets on disk.
- **Assets:** 17/17 single-channel `mode=L` at 300 dpi, read off disk.

Also machine-derived: summary **20 sentences = 13 BODY-PRESENT + 7 SUMMARY-UNIQUE** (folds
`F273`–`F279`, each with a named body home) and exercises **10 exercises, 0 GAP, 10 COVERED,
0 overlooked**.

## Session 1-F re-verification — 12 of 17 inherited crops carried a defect

Every inherited asset was **opened and read**, not spot-checked, and every verdict is
machine-adjudicated by `scratch/ch5morph_gate1/adjudicate_inherited.py`, which measures each
inherited rectangle against its plate's ink-and-image extent:

- **8 of 17 clipped artwork, an in-figure label or a panel marker** — Figs 5.1, 5.2, 5.4, 5.5,
  5.6, 5.9, 5.10, 5.16.
- **4 of 17 cut the printed caption through its glyph row** — Figs 5.3, 5.8, 5.12, 5.17.
- **12 of 17 therefore carried at least one defect.** Five were clean: Figs 5.7, 5.11, 5.13,
  5.14, 5.15.

The inherited three-part audit had passed the whole set as clean, and the inherited tracker
specifically recorded Fig 5.2's `Laterals` as "intentionally retained" — the asset in fact
rendered it as "erals".

The label and marker losses are the marks-critical ones. The largest: **Fig 5.2's `Laterals`
cut off entirely** (14.6 pt), **Fig 5.4's `(b)` and `(c)` panel markers absent altogether**
(14.9 pt), **Fig 5.9's `(a)`–`(d)` cut mid-glyph** (6.2 pt), and **Fig 5.10's `Gynoecium`
clipped** (4.0 pt) — the last of these baked into the raster artwork rather than present in the
text layer, so no text-based check could have seen it. Figs 5.1 and 5.16 lost under a point
each, but of a label and of the floral diagram's outermost whorl respectively. The worst
caption cut was Fig 5.17, with only 11% of its caption line inside the rect.

**Three further defects were introduced by this session's own first re-pin** and caught before
the freeze — Fig 5.14 bleeding the neighbouring prose column, Fig 5.5 bleeding Fig 5.4's
caption tail, and Fig 5.13 clipping markers baked into the artwork. Two of the three came from
trusting the watermark-polluted drawings union; they are logged rather than quietly corrected.

An earlier draft of this tracker claimed "15 defects" and attributed a right-edge clip to
Fig 5.14. That was wrong on both counts: the number was asserted rather than derived, and the
Fig 5.14 claim rested on the very `get_drawings()` union this session went on to reject — its
inherited rect was clean. The numbers above are re-derived by machine.

All 17 were re-pinned and regenerated, then **re-opened and read again**; the adjudicator
confirms the current rectangles clip **nothing**. The full re-pin log, with the measured extent
behind every rectangle, is in the inventory's `### Session 1-F re-verification and re-pin log`.

### Why the inherited audit was green

Two independent reasons, both now recorded so they are not rediscovered:

1. **The audit's blind spot.** Checks A (text-layer word grazing) and C (border-band ink)
   both *discount text-layer words* — A only reports a word it can see is partly outside, and
   C deletes any dark pixel a word explains. Neither can see a label cropped away
   **entirely**: `Laterals` sat outside the rect, so no word grazed the boundary and no
   unexplained ink remained. Only opening every rendered asset catches this class.
2. **A watermark that measures like artwork.** NCERT's diagonal "not to be republished" and
   (c) marks are **vector artwork drawn across the whole page**, so `page.get_drawings()`
   attributes their strokes to whichever plate sits behind them. Pinning Fig 5.14 from a
   drawings union reported its right edge at `x=299.9` when the real ink ends at `x=276.9`
   and the prose column starts at `x=303.1` — a 23 pt phantom that left no room for a margin.
   Fig 5.12's union was 40 pt too wide the same way.

The fix was to measure **dark ink** instead: the watermark renders around grey 230–245 while
figure outlines and label text sit below 215, so thresholding separates them.
`scratch/ch5morph_gate1/ink_bbox.py` does this, and `audit_figures.py` gained check **B2
(ink-extent overflow)** as the authoritative version of check B.

## Three-part crop audit + print-asset check

Run by `audit_figures.py`; full output in `Ch5_figure_audit.txt`.

| Audit | Result |
|---|---|
| A — text-layer word grazing | **0 across all 17.** Rotated spans excluded: page 11 carries a rotated, non-rendering duplicate `(a)` from the watermark layer, reported against Fig 5.12 on the first run as a true negative. |
| B — drawings-extent overflow | 4 reports (Figs 5.3, 5.8, 5.14, 5.15) — **all watermark artefacts**, adjudicated by B2. No longer authoritative. |
| B2 — ink-extent overflow | **Clean for all 17.** Proves B's four reports are not clipping. |
| C — border-band ink | **Clean for all 17.** |
| D — print-asset check | **17/17** `mode=L`, single channel, 300 dpi. |

No figure failed extraction, none is deliberately omitted, and none is a photograph of a
person — so the PDF needs no "Figures requiring manual attention" block. The one
human-subject image in the source, the **Katherine Esau portrait on page 2, is never
embedded** (section 4.4 hard no); its caption is preserved as a text-only row and the profile
facts as `F014`–`F022`.

## Figure census

Caption census (Fig 5.1–Fig 5.17) and page-image census **agree at 17**, and no additional
unnumbered plate exists. Every artwork page was rendered and inspected, so the census is not
resting on caption numbers alone.

## Source notes carried into Pass 2

Four findings about the **source**, not defects in the inventory. Full detail in the
inventory's `## Source notes`.

- **SRC-1** — section 5.5.1.4 names **six** placentation types ("marginal, axile, parietal,
  basal, central and free central") but defines and figures only **five**. "Central
  placentation" is named and never explained, which makes exercise Q7 impossible to answer
  exhaustively from the chapter. Logged rather than opened as a Rule 2 GAP because closing it
  would need a definition from outside this chapter, which Rule 5 forbids. **Pass 2 must
  reproduce the six-name list verbatim and must not silently "correct" it to five.**
- **SRC-2** — section 5.9 has two titles: "Description of Some Important Families" in the
  contents box, "SOLANACEAE" in the body. Both preserved.
- **SRC-3** — the source prints "bicarpellary **obligately** placed" (standard term:
  *obliquely*). Rule 4 bans term drift, so it is preserved exactly. Same for "physiologial",
  "adaptions", "encyclopediac", "leafbase", "monoadelphous", "placentaion", "exogeneously".
- **SRC-4** — the floral-formula symbols are **invisible to text extraction**: `get_text()`
  drops the male, female, bisexual and zygomorphic glyphs entirely and cannot distinguish the
  two `G` variants. The symbol key (`F192`) and the Solanaceae formula (`F251`) were read off
  the page images at 250–280 dpi. The printed distinction is **G underlined = superior
  ovary**, **G overlined = inferior ovary**.

## Carry-overs for Pass 2 / Pass 3

Eight numbered carry-overs are in the inventory's `## Carry-over list`. The two most likely
to bite:

- **The four section 5.5.1.x headings are typographically invisible to a colour-based heading
  sweep.** Every other heading in the chapter is cyan (colour int 44783); `5.5.1.1 Calyx`
  through `5.5.1.4 Gynoecium` are 10.5 pt `Bookman-LightItalic` in colour int 7171953, each
  drawn **five times** to fake a bold weight. A sweep keyed on the heading colour silently
  drops all four — a whole level of the flower section. Do not re-derive the heading set from
  styling alone.
- **Captions are now typeset by the script, not baked into assets.** No asset contains a
  printed caption any more, so nothing double-prints; the corollary is that a figure with no
  typeset caption will have none at all.

## Reproduction commands

From the repository root, with the venv rebuilt per the section-1 preamble:

```bash
/vercel/share/neetenv/bin/python 'notes/class 11/Ch5_MorphologyOfFloweringPlants/extract_figures.py'
/vercel/share/neetenv/bin/python 'notes/class 11/Ch5_MorphologyOfFloweringPlants/audit_figures.py'
/vercel/share/neetenv/bin/python scratch/ch5morph_gate1/build_inventory.py
/vercel/share/neetenv/bin/python scratch/ch5morph_gate1/gate1_close.py   # must print VERDICT GREEN
```

`gate1_close.py` must be re-run after **any** edit to the inventory — documentation can
degrade a gate it only describes.

The mandatory 440 dpi / 5-PDF-point grid overlays are in `scratch/ch5_figs/grid_4x/`
(16 pages, 3520x4796 px each, verified at 440.0 dpi).

## Deliverables present

| File | State |
|---|---|
| `Ch5_MorphologyOfFloweringPlants_inventory.md` | ✅ frozen, 280 rows |
| `assets/fig_5_1.png` … `fig_5_17.png` | ✅ 17/17 `mode=L` @ 300 dpi, all verified |
| `extract_figures.py` | ✅ reproducible, re-pinned rects |
| `audit_figures.py` + `Ch5_figure_audit.txt` | ✅ audit + output on disk |
| `Ch5_TRACKER.md` | ✅ this file |
| `Ch5_MorphologyOfFloweringPlants.py` | ⬜ Pass 2 |
| `Ch5_MorphologyOfFloweringPlants.pdf` | ⬜ Pass 2 |

`Ch5_MorphologyOfFloweringPlants_assets.zip` was **deleted** this session: it held the 17
pre-re-pin assets, so it had become a stale copy of superseded, defective crops sitting
beside the corrected ones. It is not one of the four per-chapter deliverables.
`Ch5_extraction.log` was deleted for the same reason — it logged the superseded rects.

## References

[1]: `../../../Chapter/class 11/Chapter 05 - Morphology of Flowering Plants.pdf` — source PDF (16 pages).
[2]: `../../../GATE_1_PASS_1_SOURCE_MASTERY.md` — Gate 1 criteria, five-session Pass 1 split.
[3]: `../../../skills/ncert-figure-extraction/SKILL.md` — grid pinning, three-part audit, visual confirmation.
[4]: `../../../scratch/ch5morph_gate1/` — Pass 1 build evidence and the Gate 1 closure check.
