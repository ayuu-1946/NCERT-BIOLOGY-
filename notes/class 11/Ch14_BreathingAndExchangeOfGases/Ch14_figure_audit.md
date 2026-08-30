# Ch14 Figure Extraction Audit

## Scope and method

This audit covers the six PNG assets extracted from the five numbered figures in the Class 11 NCERT chapter “Breathing and Exchange of Gases.” Figure 14.2 is represented by two separate assets because the source labels its inspiration and expiration panels as `(a)` and `(b)`. Each asset was rendered from the source PDF at 300 dpi and converted to true grayscale with Pillow `convert('L')` followed by autocontrast.

The mandatory crop audit was run before the individual image review. It included text-layer word grazing, vector-drawing extent overflow, and unexplained dark ink in the six-point border band. The raw final output is retained at `scratch/ch14_figs/audit_results.txt`.

## Mechanical audit result

| Asset | Text-layer grazing | Drawing extent | Border-band ink | Disposition |
|---|---|---|---|---|
| `fig_14_1.png` | 17 words, no grazing | Clean | Clean | Pass |
| `fig_14_2a.png` | 0 words; vector-label case | Clean | Clean | Pass with vacuous text-layer check documented |
| `fig_14_2b.png` | 0 words; vector-label case | Clean | Clean | Pass with vacuous text-layer check documented |
| `fig_14_3.png` | 0 words; vector-label case | Clean | Clean | Pass with vacuous text-layer check documented |
| `fig_14_4.png` | 0 words, no grazing | 8.7-point bottom vector-tail warning | Clean | Accepted after individual visual confirmation; meaningful artwork complete and caption excluded |
| `fig_14_5.png` | 17 words, no grazing | Clean | Clean | Pass |

The zero-word results for Figures 14.2a, 14.2b, and 14.3 are expected because the source places their labels in vector artwork rather than the text layer. The skill explicitly requires that such cases not be considered proven by check A alone; checks B, C, and individual visual inspection were completed.

## Visual-review record

Every final asset was opened individually from a uniquely named copy to avoid the documented image-view cache behavior. Figure 14.1 is complete and correctly oriented, with the respiratory-system diagram and all labels intact. Figures 14.2a and 14.2b are complete separate panels; the lower panel was re-pinned after an earlier preview exposed a residual upper-panel `(a)` marker. Figure 14.3 contains the full alveolar-to-tissue circulation diagram, gas arrows, and pressure labels. Figure 14.4 contains the complete alveolus/capillary cross-section and all leader-line labels; its remaining vector warning corresponds to a non-meaningful source-PDF tail below the visible diagram, while its caption is excluded. Figure 14.5 contains the complete oxygen dissociation curve, axes, tick labels, and axis titles.

## Monochrome verification

All six files were checked with Pillow and reported `mode=L`. Their final rendered sizes are listed below.

| Asset | Final pixel size | Mode |
|---|---:|---|
| `fig_14_1.png` | 1772 × 1088 | L |
| `fig_14_2a.png` | 1018 × 913 | L |
| `fig_14_2b.png` | 1018 × 967 | L |
| `fig_14_3.png` | 1784 × 1342 | L |
| `fig_14_4.png` | 1109 × 625 | L |
| `fig_14_5.png` | 897 × 922 | L |

## References

[1]: `../../../../Chapter/class 11/Chapter 14 - Breathing and Exchange of Gases.pdf` "NCERT Biology, Class 11, Chapter 14: Breathing and Exchange of Gases"
[2]: `../../../../SUPREME COMMAND PROMPT.md` "Repository SUPREME COMMAND prompt"
[3]: `../../../../skills/ncert-figure-extraction/SKILL.md` "ncert-figure-extraction workflow"
