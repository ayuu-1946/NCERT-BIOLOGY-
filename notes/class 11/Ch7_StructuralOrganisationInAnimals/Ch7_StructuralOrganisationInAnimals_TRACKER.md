# Chapter 7 extraction tracker — corrected redo

| Gate | Result | Evidence |
| :--- | :--- | :--- |
| Caption convention applied | Complete | Printed captions are excluded from all 17 assets |
| High-density grid | Complete | Mandatory 440 DPI, 5-point grid overlays in `scratch/ch7_figs/grid_4x/` |
| Pixel density | Complete | Final assets rendered at 600 DPI |
| Figure completeness | Complete | Each numbered figure remains one complete asset with all panels and labels |
| Label visibility | Complete | Fresh visual review of `scratch/ch7_figs/contact_sheet_redo_600dpi_20260831.png` |
| Whitespace control | Complete | Boxes stop before captions and neighboring prose, with only small safety margins |
| Three-part audit | Complete with explained expected hits | `audit_report.txt`; vector labels and raster figures are documented |
| Reproducibility | Complete | `extract_figures.py`, grid renderers, geometry probe, audit script, logs |

## Corrections from the previous commit

The prior extraction incorrectly included captions, used overly broad whole-page-style crops for several figures, and failed to preserve complete labels when figures were visually inspected only as combined regions. The corrected redo removes captions, increases output density from 300 DPI to 600 DPI, and re-pins the crop boundaries to include the full figure artwork and every label/leader line while excluding adjacent prose. Multi-panel figures are retained as complete numbered figures so no label shared across a panel boundary is lost.

Figures 7.9–7.13 are not present in the supplied 19-page PDF. The source jumps from Figure 7.8 to Figure 7.14, so those assets are intentionally absent.
