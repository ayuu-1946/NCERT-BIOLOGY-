# Chapter 17 Figure Extraction — Locomotion and Movement

This folder contains the extracted NCERT figures for Class 11 Biology, Chapter 17, “Locomotion and Movement.” The workflow follows the repository’s hand-pinned extraction method: source pages were rendered with mandatory 440-dpi, 5-point grid overlays; crop rectangles were pinned in PDF points; each crop was rendered at 440 dpi; and every image was converted to true grayscale with Pillow before saving.

The chapter contains **ten numbered figures**, including the two-part Figures 17.2 and 17.3 and the separate Figures 17.7–17.10 on shared pages. The authoritative per-figure label record, captions, source pages, crop coordinates, and correction notes are in `Ch17_LocomotionAndMovement_inventory.md`. The exact reusable renderer is `extract_figures.py`.

Every emitted PNG was opened individually during quality review. The review specifically checked that all in-figure labels, leader lines, brackets, arrows, panels, and terminal marks remain visible. Boundary defects found during review were corrected before final regeneration, including header/prose bleed, the clipped Figure 17.4 “Myosin head” label, the Figure 17.8 “Floating ribs” label, and the lower Figure 17.10 foot/Phalanges region.

For any downstream notes PDF, use a bordered figure box with **10 pt padding** and no additional oversized spacer. Captions should be typeset from the inventory rather than baked into the PNGs. This keeps the layout compact while preserving legibility and strict label visibility at print size.

## Files

| File or directory | Purpose |
|---|---|
| `assets/fig_17_1.png` through `assets/fig_17_10.png` | Final high-resolution monochrome figure assets |
| `extract_figures.py` | Exact reproducible extraction script with pinned rectangles and documented exceptions |
| `Ch17_LocomotionAndMovement_inventory.md` | Frozen manifest, label matrix, setup record, and audit notes |
| `../../scratch/render_ch17_grids.py` | Mandatory 440-dpi grid-overlay renderer |
| `../../scratch/audit_ch17.py` | Three-part mechanical audit and asset-mode check |
| `../../scratch/audit_ch17_results.txt` | Raw audit output |

## Reproduction

From the repository root, run:

```bash
python3 "notes/class 11/Ch17_LocomotionAndMovement/extract_figures.py"
python3 scratch/render_ch17_grids.py
python3 scratch/audit_ch17.py
```

The verified environment used for this run was `/usr/bin/python3` (Python 3.12.3), with PyMuPDF 1.28.2, Pillow 12.3.0, NumPy 2.5.1, pdfplumber 0.11.10, and ReportLab 5.0.0.
