# Anatomy of Flowering Plants — Figure Inventory

**Class:** 11  
**Chapter:** 6 — Anatomy of Flowering Plants  
**Source:** `Chapter/class 11/Chapter 06 - Anatomy of Flowering Plants.pdf`  
**Extraction standard:** hand-pinned rectangles from mandatory 440 dpi grids with 5 PDF-point grid spacing; final assets rendered at 300 dpi, converted to true grayscale with Pillow `convert("L")` and `autocontrast(cutoff=1)`.

## Coverage and figure manifest

Page-image inspection of artwork pages 2–7 identified five numbered NCERT figure plates and no additional unnumbered diagram plate. Captions were excluded from the PNG crops; the corresponding captions are documented here and can be embedded separately in the replacement chapter.

| Figure | Source page | Caption / subject | Asset | PDF crop rectangle (x0, y0, x1, y1) | Mono | Verified |
|---|---:|---|---|---|---|---|
| 6.1 | 2 | Diagrammatic representation of stomata: (a) bean-shaped guard cells; (b) dumb-bell-shaped guard cells | `assets/fig_6_1.png` | `(60, 337, 530, 448)` | yes | yes |
| 6.2 | 3 | Various types of vascular bundles: (a) radial; (b) conjoint closed; (c) conjoint open | `assets/fig_6_2.png` (a/b/c stacked horizontally) | `(320, 80, 520, 482)` | yes | yes |
| 6.3 | 4 | T.S. of root: (a) dicot root (primary); (b) monocot root | `assets/fig_6_3.png` (a/b stacked horizontally), plus `assets/fig_6_3a.png` and `assets/fig_6_3b.png` | `(75, 78, 320, 558)` | yes | yes |
| 6.4 | 5 | T.S. of stem: (a) dicot; (b) monocot | `assets/fig_6_4.png` | `(55, 235, 550, 700)` | yes | yes |
| 6.5 | 6 | T.S. of leaf: (a) dicot; (b) monocot | `assets/fig_6_5.png` (a/b stacked horizontally), plus `assets/fig_6_5a.png` and `assets/fig_6_5b.png` | `(55, 285, 320, 690)` | yes | yes |

## Figure-label matrix

Every label visible in the extracted plates is listed below so the chapter prose or an accompanying table can reproduce the label vocabulary. Labels were harvested by opening and reading each rendered asset, not by relying on the PDF text layer, because several labels are vector artwork or image content.

| Figure | Visible in-figure labels |
|---|---|
| 6.1 | Epidermal cells; Subsidiary cells; Chloroplast; Guard cells; Stomatal pore |
| 6.2 | Xylem; Phloem; Cambium |
| 6.3 | Root hair; Epidermis; Cortex; Endodermis; Pericycle; Protoxylem; Metaxylem; Pith; Phloem |
| 6.4 | Epidermal hair; Epidermis; Hypodermis; Parenchyma; Endodermis; Pericycle; Vascular bundle; Medullary rays; Pith; Collenchyma; Phloem; Cambium; Metaxylem; Protoxylem; Vascular bundles; Ground tissue |
| 6.5 | Bundle sheath; Xylem; Phloem; Adaxial epidermis; Palisade mesophyll; Air cavity; Spongy mesophyll; Sub-stomatal cavity; Stoma; Abaxial epidermis; Mesophyll |

## Crop and spacing notes

The crops use approximately 10 PDF points of intentional clearance where the artwork permits it, rather than the excessive page-level whitespace present in the source pages. Captions and adjacent body prose are excluded. Multi-panel plates remain single assets when the source uses one shared caption and one figure number; every panel, marker, leader line, terminal label, and anatomical region is retained inside the crop.

Figure 6.4 is a raster-dominant plate, so the drawings-extent check reports “no drawings (raster figure)” rather than treating the result as a failure. Figure 6.2 has no text-layer words inside the plate, confirming that its labels must be verified visually.

## Reformatting record

Figure 6.2 was trimmed on the right and reformatted into an equal-cell horizontal composite of panels (a), (b), and (c). Figures 6.3 and 6.5 were split into standalone (a) and (b) assets and then recombined horizontally into `fig_6_3.png` and `fig_6_5.png`. All reformatted outputs were individually checked against the mandatory 440 dpi / 5-point source-page grids.

## Verification record

The final audit was run with `audit_figures.py` after the last extraction. The text-layer grazing check reported no grazing words for all five assets; the drawings-extent check reported `ok` for Figures 6.1, 6.2, 6.3, and 6.5, and correctly identified Figure 6.4 as raster-dominant; the border-band ink check reported `clean` for all five assets. The emitted PNGs all exist, use one grayscale channel (`mode=L`), and were individually opened for visual confirmation of label visibility and panel completeness.

## Files

| File | Purpose |
|---|---|
| `extract_figures.py` | Reproducible hand-pinned clip extraction and monochrome conversion |
| `audit_figures.py` | Three-part mechanical crop gate plus image-mode check |
| `Ch6_extraction.log` | Final extraction output and image dimensions |
| `Ch6_figure_audit.txt` | Final A/B/C/D audit output |
| `assets/fig_6_1.png`, `assets/fig_6_2.png`, `assets/fig_6_3a.png`, `assets/fig_6_3b.png`, `assets/fig_6_4.png`, `assets/fig_6_5a.png`, `assets/fig_6_5b.png` | Final tightly cropped, grayscale figure assets; original combined 6.3/6.5 files retained |
| `../../scratch/ch6_figs/grid_4x/p02.png` through `p07.png` | Mandatory high-density pinning grids retained as audit evidence |

## References

[1]: `Chapter/class 11/Chapter 06 - Anatomy of Flowering Plants.pdf` — NCERT Biology source chapter in this repository.
[2]: `SUPREME COMMAND PROMPT.md` — repository-wide replacement-chapter and figure requirements.
[3]: `skills/ncert-figure-extraction/SKILL.md` — hand-pinned crop, three-part audit, and visual-verification procedure.
