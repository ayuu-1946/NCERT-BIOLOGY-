# Class 11 Chapter 7 — Structural Organisation in Animals Tracker

## Current status

**Figure extraction: Complete for the user-supplied 19-page PDF.** The exact attachment has replaced the short source edition in `Chapter/class 11/Chapter 07 - Structural Organisation in Animals.pdf`. A complete-page visual census and caption check identified **17 numbered figures** (7.1–7.8 and 7.14–7.22); the supplied edition contains no Figures 7.9–7.13. The assets folder contains **22** 300-dpi, single-channel monochrome PNGs: one per numbered figure, with Figures 7.6 and 7.18 delivered as horizontal composites plus five independently extracted panel crops in total (three for 7.6, two for 7.18). The manifest records each exact caption and PDF page. The checker-compatible Facts-table matrix has one row per figure and records the visible labels. Every `Mono`/`Verified` manifest value was earned only after opening the asset.

**Crop audit: Complete.** All 20 A checks are clean; raster Figure 7.14 has zero text-layer words and is supported by B/C and visual review. B reports explained source-vector extent cases for Figure 7.1's pale diagonal watermark, Figure 7.6(c)'s upper RBC path bounding box, and the reciprocal 12.5-pt extents where Figures 7.18(a)/(b) abut. The 440-dpi grids and clean source details confirm complete artwork in each isolated panel and exclusion of the neighboring panel/caption. B is not applicable to raster Figures 7.8, 7.14, and 7.22. All C border-band checks are clean. Figure 7.1's top edge was moved below neighboring prose; Figure 7.4's right edge was extended to include its labels and leader-line ends; Figures 7.6 and 7.18 were split at their source-panel boundaries and recomposed horizontally without resampling. All five panel crops and both composites were individually reviewed after generation.

This is a **figures-only deliverable**. It does not claim chapter-wide Pass 1 / Gate 1, Pass 2 / Gate 2, or Pass 3 / Gate 3 completion; no chapter notes PDF/script or prose inventory was requested or produced. The global chapter-completion ledger is unchanged.

## Reproduction

Run from repository root with the skill-required Python 3.13 environment:

```bash
/vercel/share/neetenv/bin/python scratch/ch7_figs/render_grids.py
/vercel/share/neetenv/bin/python 'notes/class 11/Ch7_StructuralOrganisationInAnimals/extract_figures.py'
/vercel/share/neetenv/bin/python 'notes/class 11/Ch7_StructuralOrganisationInAnimals/audit_figures.py'
```

## Deliverables

- `Chapter/class 11/Chapter 07 - Structural Organisation in Animals.pdf` — exact source attachment.
- `extract_figures.py` — hand-pinned crops for the 17 numbered figures, five split-panel crops for Figures 7.6 and 7.18, both horizontal assemblies, and contact sheet generation.
- `audit_figures.py` / `audit_report.txt` — mandatory crop checks and saved final output.
- `Ch7_StructuralOrganisationInAnimals_inventory.md` — exact 17-figure manifest, per-figure label matrix, crop rectangles, audit findings, and source edition scope.
- `assets/fig_7_1.png` through `assets/fig_7_8.png`, plus `fig_7_14.png` through `fig_7_22.png` — 17 individually reviewed monochrome figure outputs; `fig_7_6.png` is the horizontal `(a) (b) (c)` assembly.
- `assets/fig_7_6a.png`, `fig_7_6b.png`, `fig_7_6c.png`, `fig_7_18a.png`, `fig_7_18b.png` — five additional independently extracted, audited, and reviewed source-panel PNGs.
- `scratch/ch7_figs/render_grids.py` and `grid_4x/` — required 440-dpi source grids for every artwork page.
- `scratch/ch7_figs/contact_sheet.png` — final asset overview.
