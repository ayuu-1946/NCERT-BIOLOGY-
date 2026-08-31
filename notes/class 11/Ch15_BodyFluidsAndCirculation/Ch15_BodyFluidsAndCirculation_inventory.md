# Chapter 15 Figure Inventory: Body Fluids and Circulation

## Figure extraction status

**Source PDF:** `Chapter/class 11/Chapter 15 - Body Fluids and Circulation.pdf`  
**Figure census:** 4 numbered source figures → 4 extracted assets.  
**Extraction status:** Complete for the figure-extraction scope. All four assets were rendered at 300 dpi, converted to true monochrome (`mode=L`) with autocontrast, visually reviewed, and audited with the mandatory three-part crop checks.  
**Extraction script:** `extract_figures.py`  
**Audit record:** `Ch15_figure_audit.md`

The source chapter has twelve PDF pages. Numbered figure artwork appears on PDF pages 2, 6, 9, and 10. PDF page 7 contains a textual continuation/reference to Figure 15.2 but no additional figure artwork. No table, page furniture, caption, or neighboring body-text column was included in the assets.

## Figure manifest

| Figure | Verbatim source caption | PDF page | Asset | Status |
|---|---|---:|---|---|
| 15.1 | Diagrammatic representation of formed elements in blood | 2 | `assets/fig_15_1.png` | Extracted, true monochrome, visually verified |
| 15.2 | Section of a human heart | 6 | `assets/fig_15_2.png` | Extracted with all leader-line labels, true monochrome, visually verified |
| 15.3 | Diagrammatic presentation of a standard ECG | 9 | `assets/fig_15_3.png` | Extracted with P–T labels and full waveform, true monochrome, visually verified |
| 15.4 | Schematic plan of blood circulation in human | 10 | `assets/fig_15_4.png` | Extracted with all circulation, vessel, and capillary labels, true monochrome, visually verified |

## Figure-label matrix

The labels below were checked against the final rendered PNG assets during individual visual review. The matrix is intentionally explicit so that every in-figure label can be carried into any later rewritten chapter text.

| Figure | In-figure labels verified in asset |
|---|---|
| 15.1 | R B C; Platelets; Eosinophil; Basophil; Neutrophil; Monocyte; T lymphocyte; B lymphocyte |
| 15.2 | Vena cava; Sino-atrial node; Right atrium; Atrio-ventricular node; Chordae tendinae; Right ventricle; Aorta; Pulmonary artery; Pulmonary veins; Left atrium; Bundle of His; Left ventricle; Interventricular septum; Apex |
| 15.3 | P; Q; R; S; T |
| 15.4 | Lungs; Pulmonary artery; Pulmonary Vein; Vena cava (great veins); RA; RV; LA; LV; Heart; Dorsal aorta; Body parts; Smooth muscle; Lumen; Vein; Capillary; Artery |

## Crop and spacing notes

The rectangles in `extract_figures.py` were pinned from 440 dpi, 5-point grid overlays in `scratch/ch15_figs/grid_4x/` and cross-checked against source-PDF text-layer coordinates and vector drawing extents. Captions were excluded from all assets. Crops use a restrained approximately 8–10 point visual margin around the meaningful outer artwork and labels; no large page whitespace was carried into the assets.

Figure 15.2 was re-pinned after the first visual review: the initial right boundary clipped the right-side label bank and the initial top boundary clipped upper vessel artwork. The final rectangle `(130, 390, 525, 690)` retains the complete heart, vessel tips, leader lines, and all labels while stopping above the caption.

Figures 15.2–15.4 report zero words inside the crop on the text-layer audit because the source labels are vector artwork rather than text-layer glyphs. This is expected and is not treated as an audit pass by itself; drawings extent, border-band ink, and visual review provide the remaining gates.

## Reproducibility

Run from the repository root with the dedicated environment:

```bash
/home/ubuntu/neetenv/bin/python 'notes/class 11/Ch15_BodyFluidsAndCirculation/extract_figures.py'
/home/ubuntu/neetenv/bin/python /home/ubuntu/audit_ch15.py
```

## References

[1]: `../../../../Chapter/class 11/Chapter 15 - Body Fluids and Circulation.pdf` "NCERT Biology, Class 11, Chapter 15: Body Fluids and Circulation"
[2]: `../../../../SUPREME COMMAND PROMPT.md` "Repository SUPREME COMMAND prompt"
[3]: `../../../../skills/ncert-figure-extraction/SKILL.md` "ncert-figure-extraction workflow"
