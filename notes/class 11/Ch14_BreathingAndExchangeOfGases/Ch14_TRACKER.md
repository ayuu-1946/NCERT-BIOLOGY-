# Ch14 Breathing and Exchange of Gases — Figure Extraction Tracker

## Current status

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
