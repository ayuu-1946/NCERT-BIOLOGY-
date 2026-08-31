# Ch14 Breathing and Exchange of Gases — Tracker

## Pass / gate status

**Pass 1: COMPLETE — GATE 1 CLOSED (2026-08-31).**
- Inventory **FROZEN at 139 rows, `F001`–`F139`, contiguous, 0 gaps, 0 duplicate IDs, 0 ticked** (machine re-parsed from the finished table).
- Blocks: 107 Facts (`1-S`) + 14 heading (`1-H`) + 12 opener (`1-O`) + 0 summary-unique (`1-Z`) + 6 figure-label matrix (`1-F`) = **139**, equal to the highest ID.
- Type census (10 lowercase values, machine-derived, sums to 139): `concept` 47 · `definition` 27 · `number` 18 · `heading` 14 · `opener` 12 · `process` 9 · `figure-label` 6 · `example` 3 · `name` 2 · `list` 1.
- Heading census **10 numbered + 4 unnumbered = 14**; openers **12**.
- Summary classification **18 sentences = 18 BODY-PRESENT + 0 SUMMARY-UNIQUE** — nothing to fold into the body.
- Exercise-gap scan: **14 exercises / 3 genuine gaps** (hypoxia definition, high-altitude respiratory effect, sigmoid-curve reason), each with a planned home noted in the inventory.
- Figure-label matrix machine-checked: `check_pdf.py`'s own `_extract_labels` returns **47 labels across 6 figure rows, no doubling, no phantom `Fig #` row**.

**Pass 2: NOT STARTED** — no `Ch14….py` script and no generated PDF, so `check_pdf.py` (Gate 2) cannot run. This chapter is **excluded from the Done tally.**
**Pass 3 / Gate 3: NOT STARTED.**

## Current status (figure extraction — completed in a prior task)

**Figure extraction stage:** Complete.  
**Figure census:** 5 numbered figures → 6 assets, with Figure 14.2 split into `(a)` and `(b)`.  
**Assets:** 6/6 present, all `mode=L`, all individually visually reviewed.  
**Three-part crop audit:** Complete. Checks A and C are clean for all assets; check B is clean for five assets. Figure 14.4 retains one explained 8.7-point source-PDF vector-tail warning below the meaningful visible artwork; no label or diagram edge is clipped and the caption is excluded.  
**Full chapter replacement/PDF gate:** Not started by this figure-extraction task; no chapter notes PDF was generated.

## Re-pin log

| Asset | Change | Reason |
|---|---|---|
| `fig_14_2b.png` | Final top boundary set to `y0=330` | Earlier visual preview included the neighboring upper-panel `(a)` marker; the final crop begins below it while retaining the “Air expelled from lungs” label. |
| `fig_14_5.png` | Left boundary set to `x0=292` | The first crop grazed the graph’s left tick labels; the boundary was expanded to include all tick labels and then passed the text-layer check. |
| `fig_14_4.png` | Bottom boundary tightened to `y1=660` | Earlier crop included caption text. The final asset excludes the caption and retains all meaningful diagram content; the residual vector tail is documented in `Ch14_figure_audit.md`. |

## Reproduction commands

From the repository root:

```bash
/vercel/share/neetenv/bin/python 'notes/class 11/Ch14_BreathingAndExchangeOfGases/extract_figures.py'
/vercel/share/neetenv/bin/python scratch/audit_ch14_figures.py
```

## Deliverables

The chapter folder contains the reproducible extraction script, the frozen inventory with the per-figure label matrix, the detailed audit, and six grayscale PNG assets under `assets/`. The raw grid overlays, extraction log, audit output, geometry probes, and visual-review notes remain in `scratch/ch14_figs/` and `scratch/ch14_visual_findings.md` for re-audit.

## References

[1]: `../../../../SUPREME COMMAND PROMPT.md` "Repository SUPREME COMMAND prompt"
[2]: `../../../../skills/ncert-figure-extraction/SKILL.md` "ncert-figure-extraction workflow"
