# Ch12 — Respiration in Plants — Figure Extraction Tracker

| Gate | Status | Evidence |
|---|---|---|
| Source PDF located | Done | `Chapter/class 11/Chapter 12 - Respiration in Plants.pdf` |
| Mandatory 440-dpi/5-point grids | Done | `scratch/ch12_figs/grid_4x/p04.png`, `p05.png`, `p06.png`, `p07.png`, `p08.png`, `p09.png`, `p11.png` |
| Numbered figure inventory | Done | `Ch12_RespirationInPlants_inventory.md`; six numbered figures |
| Reproducible extraction script | Done | `extract_figures.py` |
| Three-part crop audit | Pass | `scratch/ch12_figs/audit_results.txt`; all border bands clean, no remaining grazing, no drawing overflow |
| Individual visual review | Pass | `scratch/ch12_figs/grid_findings.md`; all six PNGs opened individually |
| Monochrome conversion | Pass | All six assets report Pillow mode `L` |
| Documentation | Done | Inventory, tracker, and `Ch12_figure_audit.md` |

## Current deliverables

The chapter contains **6 figure assets** under `assets/`: `fig_12_1.png` through `fig_12_6.png`. Each crop excludes its caption and neighboring prose, uses tight spacing rather than a large white border, and preserves the source’s in-figure labels and arrows.

## Repin history

Figure 12.1 was repinned once after the first mechanical audit detected neighboring prose grazing the right edge. Its right boundary changed from `x1=299` to `x1=296`; the corrected asset passed the text-layer gate and was visually confirmed complete. No other rectangle required correction.

## Environment record

The active interpreter was `/usr/bin/python3` (Python 3.12.3), and `/home/ubuntu/NCERT-BIOLOGY-` was writable. Required packages were installed and verified in that interpreter: PyMuPDF 1.28.2, Pillow 12.3.0, NumPy 2.5.1, pdfplumber 0.11.10, and ReportLab 5.0.0. The reusable setup note is `setup_environment.md` at the repository root.

## References

[1]: `../../../../SUPREME COMMAND PROMPT.md` "Repository SUPREME COMMAND prompt"
[2]: `../../../../skills/ncert-figure-extraction/SKILL.md` "ncert-figure-extraction workflow"
