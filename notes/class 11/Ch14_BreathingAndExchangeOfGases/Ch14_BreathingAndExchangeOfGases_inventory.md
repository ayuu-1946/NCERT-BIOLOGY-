# Ch14 Breathing and Exchange of Gases — Figure Inventory

## Figure extraction status

**Source PDF:** `Chapter/class 11/Chapter 14 - Breathing and Exchange of Gases.pdf`  
**Figure census:** 5 numbered source figures, extracted as 6 assets because Figure 14.2 has two labeled sub-figures.  
**Extraction status:** Complete for the figure-extraction scope. All six assets were rendered at 300 dpi, converted to true grayscale (`mode=L`) with autocontrast, opened individually, and audited with the mandatory three-part crop checks.  
**Extraction script:** `extract_figures.py`  
**Audit record:** `Ch14_figure_audit.md`  

The source chapter has twelve PDF pages. The artwork pages are PDF pages 4, 6, 8, and 9. PDF page 7 contains a reference to Figure 14.3 and Table 14.1, but no additional figure artwork; therefore the table was intentionally excluded from the figure-asset census.

## Figure manifest

| Figure | Verbatim source caption | PDF page | Asset | Status |
|---|---|---:|---|---|
| 14.1 | Diagrammatic view of human respiratory system (sectional view of the left lung is also shown) | 4 | `assets/fig_14_1.png` | Extracted, grayscale, visually verified |
| 14.2a | Mechanism of breathing showing: (a) inspiration | 6 | `assets/fig_14_2a.png` | Extracted as separate labeled sub-figure, grayscale, visually verified |
| 14.2b | Mechanism of breathing showing: (b) expiration | 6 | `assets/fig_14_2b.png` | Extracted as separate labeled sub-figure, grayscale, visually verified |
| 14.3 | Diagrammatic representation of exchange of gases at the alveolus and the body tissues with blood and transport of oxygen and carbon dioxide | 8 | `assets/fig_14_3.png` | Extracted, grayscale, visually verified |
| 14.4 | A Diagram of a section of an alveolus with a pulmonary capillary. | 8 | `assets/fig_14_4.png` | Extracted, grayscale, visually verified |
| 14.5 | Oxygen dissociation curve | 9 | `assets/fig_14_5.png` | Extracted, grayscale, visually verified |

## Figure-label matrix

The labels below were checked against the rendered PNG assets during the individual visual review. They are the in-figure labels that should be represented in the chapter’s running text or explicitly referenced in its figure discussion.

| Figure | In-figure labels verified in asset |
|---|---|
| 14.1 | Epiglottis; Larynx; Trachea; Bronchus; Cut end of rib; Lung; heart; Diaphragm; Pleural membranes; Alveoli; Pleural fluid; Bronchiole |
| 14.2a | Air entering lungs; Ribs and sternum raised; Rib cage; Diaphragm contracted; Volume of thorax increased; (a) |
| 14.2b | Air expelled from lungs; Ribs and sternum returned to original position; Volume of thorax decreased; Diaphragm relaxed and arched upwards; (b) |
| 14.3 | Inspired air; Expired air; Alveolar air; pO₂ = 104 mmHg; pCO₂ = 40 mmHg; Alveolus; CO₂; O₂; Pulmonary artery; Pulmonary vein; Systemic veins (carrying deoxygenated blood); pO₂ = 40 mm Hg; pCO₂ = 45 mm Hg; Systemic arteries (carrying oxygenated blood); pO₂ = 95 mm Hg; pCO₂ = 40 mm Hg; Body tissues |
| 14.4 | Air; Squamous epithelium of alveolar wall (one-celled thick); Alveolar cavity; Basement substance; Endothelium of blood capillary; Blood capillary; Red blood cell |
| 14.5 | Percentage saturation of haemoglobin with oxygen; Partial pressure of oxygen (mm Hg); 0, 20, 40, 60, 80, 100 tick labels; oxygen dissociation curve |

## Crop and audit notes

The rectangles in `extract_figures.py` were pinned from the canonical 4× grid overlays in `scratch/ch14_figs/grid_4x/` and cross-checked against the source PDF’s text-layer words and vector drawing extents. Captions were excluded from all assets. Figure 14.2 was split into two assets because its `(a)` and `(b)` panels are separately labeled source sub-figures. During visual review, the lower panel was re-pinned to remove a residual upper-panel `(a)` marker; the corrected asset was regenerated and passed the full audit.

The audit’s text-layer check reports zero words for Figures 14.2a, 14.2b, and 14.3 because their labels are vector artwork rather than text-layer glyphs; this is expected and is not treated as a clean result on that check alone. Figure 14.4 has a small source-PDF vector-extent tail below the meaningful visible artwork, but its caption is excluded, no label or diagram edge is clipped, and the final asset was visually confirmed complete. All border-band checks are clean, and every emitted PNG is `mode=L`.

## Reproducibility

Run the extraction from the repository root with the dedicated environment:

```bash
/vercel/share/neetenv/bin/python 'notes/class 11/Ch14_BreathingAndExchangeOfGases/extract_figures.py'
/vercel/share/neetenv/bin/python scratch/audit_ch14_figures.py
```

## References

[1]: `../../../../Chapter/class 11/Chapter 14 - Breathing and Exchange of Gases.pdf` "NCERT Biology, Class 11, Chapter 14: Breathing and Exchange of Gases"
[2]: `../../../../SUPREME COMMAND PROMPT.md` "Repository SUPREME COMMAND prompt"
[3]: `../../../../skills/ncert-figure-extraction/SKILL.md` "ncert-figure-extraction workflow"
