# Chapter 7 extraction tracker

| Gate | Result | Evidence |
| :--- | :--- | :--- |
| Source PDF identified | Complete | `Chapter/class 11/Chapter 07 - Structural Organisation in Animals.pdf` |
| Artwork pages rendered | Complete | 440 DPI, 5-point grid overlays in `scratch/ch7_figs/grid_4x/` |
| Figure assets extracted | Complete | 17 numbered figure assets in `assets/` |
| Labels preserved | Complete | Final visual review of `contact_sheet_final_20260831_v2.png` |
| Whitespace control | Complete | Tight hand-pinned boxes with small margins; neighboring prose excluded where possible |
| Three-part audit | Complete with documented exceptions | `audit_report.txt` |
| Reproducible scripts | Complete | `render_grids.py`, `extract_figures.py`, `audit_figures.py`, `probe_geometry.py` |

## Audit interpretation

The text-layer grazing report contains expected hits because NCERT places many figure labels and captions in the PDF text layer; those words are intentionally inside the figure boxes. Figures 7.8, 7.14, and 7.22 are raster-dominant, so the drawing-extent check correctly reports “no drawings.” The border-band hit on Figure 7.19 is the frog’s leftmost intended artwork/label touching the pinned boundary; it is not neighboring prose or an accidental crop defect. The mechanical checks were supplemented by visual inspection of the final contact sheet, where all 17 figure regions, labels, panel markers, and captions are present.

Figures 7.9–7.13 do not appear in the supplied 19-page source PDF: the text-layer inventory jumps from Figure 7.8 to Figure 7.14, and the omitted pages contain no artwork. They are therefore not fabricated or inferred as assets.
