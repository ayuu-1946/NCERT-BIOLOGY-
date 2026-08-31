# Chapter 12 Figure Extraction Audit

## Scope and method

This audit covers the six numbered figures in the Class 11 NCERT chapter **Respiration in Plants**. The source pages were rendered at the mandatory 440 dpi with 5-point gridlines and 20-point coordinate labels. Rectangles were hand-pinned from those grids and cross-checked against raster color bounds, source drawing extents, and caption word coordinates. Each final PNG was rendered at 300 dpi, converted to true grayscale using Pillow `convert('L')` plus `autocontrast`, and reviewed individually.

The crops intentionally use only a small perimeter margin, generally 3–8 PDF points around the artwork. Captions and adjacent prose are excluded. Figure 12.4 retains its printed outer border because it is part of the diagram.

## Mechanical gate

| Asset | Text-layer grazing | Drawing extent | Border-band ink | Grayscale | Disposition |
|---|---|---|---|---|---|
| `fig_12_1.png` | 56 words; no grazing after right-edge repin | No drawings; raster panel | Clean | `L` | Pass |
| `fig_12_2.png` | 0 words; vector-label case | Clean | Clean | `L` | Pass; text-layer check vacuous and covered by visual review |
| `fig_12_3.png` | 40 words; no grazing | Clean | Clean | `L` | Pass |
| `fig_12_4.png` | 0 words; vector/raster composite case | No bounded drawings detected; visual border check completed | Clean | `L` | Pass; text-layer and drawing checks limited by source artwork representation |
| `fig_12_5.png` | 0 words; raster/vector composite case | No bounded drawings detected; visual label check completed | Clean | `L` | Pass; text-layer and drawing checks limited by source artwork representation |
| `fig_12_6.png` | 0 words; vector/text artwork case | Clean | Clean | `L` | Pass; text-layer check vacuous and covered by visual review |

The raw output is retained at `scratch/ch12_figs/audit_results.txt`. The initial Figure 12.1 rectangle included neighboring prose at the right edge; the boundary was tightened from `x1=299` to `x1=296`, after which the text-grazing gate reported `ok` and the image was re-reviewed.

## Individual visual review

All six final assets were opened individually. Figure 12.1 retains every glycolysis intermediate, ATP/ADP mark, NAD label, H₂O mark, arrow, and terminal pyruvic-acid label. Figure 12.2 retains both lactic-acid and ethanol+CO₂ branches and their NAD+/NADH+H⁺ labels. Figure 12.3 retains the complete citric-acid cycle, including the top entry labels and the lower GDP/GTP and FADH₂/FAD⁺ marks. Figure 12.4 retains the complete bordered ETS panel, membrane headings, complexes I–IV, proton counts, cytochromes, quinones, ATP synthase, electrochemical gradient, and leader labels. Figure 12.5 retains the complete ATP-synthase diagram and all nine surrounding labels. Figure 12.6 retains the complete metabolic-pathway network, including all three input classes and all connecting lines and arrows.

The final contact sheet is `scratch/ch12_figs/contact_sheet_final.png`; the persistent visual notes are `scratch/ch12_figs/grid_findings.md`.

## Final asset dimensions

| Asset | Pixel dimensions | Mode |
|---|---:|---|
| `fig_12_1.png` | 1009 × 1814 | L |
| `fig_12_2.png` | 1022 × 1080 | L |
| `fig_12_3.png` | 1009 × 963 | L |
| `fig_12_4.png` | 1151 × 1935 | L |
| `fig_12_5.png` | 788 × 730 | L |
| `fig_12_6.png` | 1964 × 1525 | L |

## Reproduction commands

From the repository root:

```bash
python3 'notes/class 11/Ch12_RespirationInPlants/extract_figures.py'
python3 scratch/ch12_figs/audit_ch12.py
```

## References

[1]: `../../../../Chapter/class 11/Chapter 12 - Respiration in Plants.pdf` "NCERT Biology, Class 11, Chapter 12: Respiration in Plants"
[2]: `../../../../SUPREME COMMAND PROMPT.md` "Repository SUPREME COMMAND prompt"
[3]: `../../../../skills/ncert-figure-extraction/SKILL.md` "ncert-figure-extraction workflow"
