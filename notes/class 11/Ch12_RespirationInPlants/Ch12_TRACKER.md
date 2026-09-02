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

## Layout revision — SS12.4 page break + Fig 12.2 / Fig 12.3 resize (operator instruction)

| Item | Status | Evidence |
|---|---|---|
| SS12.4 moved wholly to page 5 | Done | Explicit `PageBreak()` before `heading("12.4", ...)`; heading + intro + both process-flow steps verified on one page |
| Fig 12.2 enlarged 8.65 cm to 11.0 cm | Done | Fills the page-4 space vacated by SS12.4; below the 12.68 cm 300-dpi natural width of the PR #192 high-DPI asset, so no upscaling; all of SS12.3 still completes on page 4 (first try at 12.2 cm overflowed SS12.3's last paragraph and was rejected) |
| Fig 12.3 reduced 9.0 cm to 8.2 cm | Done | The SS12.4.2 sentence "...oxygen acts as the final hydrogen acceptor" now completes on the same page as Fig 12.3 (page 6) instead of stranding its last line on page 7 |
| Page count | Unchanged | 10 pages before and after |
| Gate 2 (`check_pdf.py`) | Green | 0 FAIL, 1 WARN — the WARN is check 4's keyword scan matching the word "photosynthesis" in inventory prose; check 3 confirms all 6 embedded images are monochrome figure plates, no person photo embedded |
| Pass 3a visual review | Pass | Pages 4, 5, 6 rendered and individually reviewed after Gate 2 + documentation; full-document page-by-page sweep re-confirmed no regression on the untouched pages |

## Repin history

Figure 12.1 was repinned once after the first mechanical audit detected neighboring prose grazing the right edge. Its right boundary changed from `x1=299` to `x1=296`; the corrected asset passed the text-layer gate and was visually confirmed complete. No other rectangle required correction.

## Environment record

The active interpreter was `/usr/bin/python3` (Python 3.12.3), and `/home/ubuntu/NCERT-BIOLOGY-` was writable. Required packages were installed and verified in that interpreter: PyMuPDF 1.28.2, Pillow 12.3.0, NumPy 2.5.1, pdfplumber 0.11.10, and ReportLab 5.0.0. The reusable setup note is `setup_environment.md` at the repository root.

## References

[1]: `../../../../SUPREME COMMAND PROMPT.md` "Repository SUPREME COMMAND prompt"
[2]: `../../../../skills/ncert-figure-extraction/SKILL.md` "ncert-figure-extraction workflow"
