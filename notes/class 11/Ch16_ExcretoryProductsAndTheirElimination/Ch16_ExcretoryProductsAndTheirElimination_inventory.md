# Chapter 16 — Excretory Products and their Elimination

## Figure extraction status

**Source PDF:** `Chapter/class 11/Chapter 16 - Excretory Products and their Elimination.pdf`  
**Figure census:** 6 numbered source figures  
**Extraction status:** Complete; all assets rendered at 300 dpi, converted to true grayscale (`L`) with autocontrast, and visually inspected.  
**Extraction script:** `extract_figures.py`  
**Audit record:** `scratch/ch16_figs/audit_results_final.txt`

## Figure manifest

| Figure | Caption | PDF page | Asset | Status |
|---|---|---:|---|---|
| 16.1 | Human Urinary system | 2 | `assets/fig_16_1.png` | Extracted, grayscale, visually verified |
| 16.2 | Longitudinal section (Diagrammatic) of Kidney | 3 | `assets/fig_16_2.png` | Extracted, grayscale, visually verified |
| 16.3 | A diagrammatic representation of a nephron showing blood vessels, duct and tubule | 3 | `assets/fig_16_3.png` | Extracted, grayscale, visually verified |
| 16.4 | Malpighian body (renal corpuscle) | 4 | `assets/fig_16_4.png` | Extracted, grayscale, visually verified |
| 16.5 | Reabsorption and secretion of major substances at different parts of the nephron (Arrows indicate direction of movement of materials.) | 6 | `assets/fig_16_5.png` | Extracted, grayscale, visually verified |
| 16.6 | Diagrammatic representation of a nephron and vasa recta showing counter current mechanism | 7 | `assets/fig_16_6.png` | Extracted, grayscale, visually verified |

## Figure-label matrix

The labels below were harvested by opening and reading the rendered assets, not by relying on PDF text extraction. They are the labels that must be represented in the chapter’s running text or explicitly referenced in the figure discussion.

| Figure | In-figure labels verified in asset |
|---|---|
| 16.1 | Inferior vena cava; adrenal gland; renal artery; renal vein; kidney; dorsal aorta; ureter; urinary bladder; urethra; pelvis; medulla; cortex |
| 16.2 | Renal column; medullary pyramid; calyx; renal artery; renal vein; renal pelvis; ureter; cortex; renal capsule |
| 16.3 | Afferent arteriole; efferent arteriole; glomerulus; Bowman’s capsule; proximal convoluted tubule; distal convoluted tubule; descending limb of loop of Henle; ascending limb of loop of Henle; Henle’s loop; vasa recta; collecting duct |
| 16.4 | Afferent arteriole; efferent arteriole; Bowman’s capsule; proximal convoluted tubule |
| 16.5 | Proximal convoluted tubule; distal convoluted tubule; NaCl; nutrients; H₂O; HCO₃⁻; K⁺; H⁺; NH₃; descending limb of loop of Henle; thick segment of ascending limb; thin segment of ascending limb; collecting duct; cortex; medulla; urea |
| 16.6 | Afferent arteriole; efferent arteriole; Bowman’s capsule; glomerulus; H₂O; NaCl; urea; cortex; outer medulla; inner medulla; vasa recta; nephron; 300 mOsmol L⁻¹; 600 mOsmol L⁻¹; 900 mOsmol L⁻¹; 1200 mOsmol L⁻¹; 200; 300; 400; 600; 800; 900; 1000; 1200 |

## Crop and audit notes

The rectangles were pinned from 110 dpi grid overlays and cross-checked against PDF geometry. Figure 16.1 required a narrowed right edge to exclude neighboring prose. Figure 16.2 required expansion at the top and left to restore the “medullary pyramid” and “renal capsule” labels, followed by narrowing the left edge to exclude the prose column. Figure 16.4 required a higher top edge to restore the “afferent arteriole” label.

The text-layer audit reports zero words for Figures 16.2, 16.3, 16.5, and 16.6 inside the artwork rectangles, which is expected because their labels are vector artwork rather than text-layer glyphs. Figure 16.2’s drawings-extent warning is attributable to the source page’s large watermark/page-furniture vector extent; the actual figure was visually checked and is complete, and the border-band ink check is clean. Figure 16.1’s crop was corrected after visual review: the bottom boundary now ends above the caption baseline, so the asset contains the complete diagram and labels without caption text.
