# Chapter 13 — Plant Growth and Development: Figure Inventory

**Status:** Figure-extraction inventory complete and frozen for the figure-only task. The source is the NCERT Class 11 Chapter 13 PDF. Eleven numbered NCERT figures were identified and extracted as eleven standalone monochrome assets. Captions are documented here rather than generally embedded in the PNGs. Figure 13.1 is the documented exception: the lowest root artwork overlaps the caption band in the source PDF, so the crop extends through the caption baseline to prevent root-tip clipping.

## Figure manifest

| Asset | Source PDF page | Verbatim NCERT caption | Crop rectangle (PDF points) | Notes |
|---|---:|---|---|---|
| `fig_13_1.png` | 2 | **Figure 13.1** Germination and seedling development in bean | `(55, 95, 515, 389)` | Full bean plate; all roots and labels retained. Caption-band overlap is intentional and documented. |
| `fig_13_2.png` | 3 | **Figure 13.2** Diagrammatic representation of locations of root apical meristem, shoot apical meristem and vascular cambium. Arrows exhibit the direction of growth of cells and organ | `(52, 94, 270, 377)` | Separate upper-left diagram; lower “Root apical meristem” label retained. |
| `fig_13_3.png` | 3 | **Figure 13.3** Detection of zones of elongation by the parallel line technique. Zones A, B, C, D immediately behind the apex have elongated most. | `(52, 515, 270, 660)` | Separate lower diagram; all zones A–G and leader lines retained. |
| `fig_13_4.png` | 4 | **Figure 13.4** Diagrammatic representation of : (a) Arithmetic (b) Geometric growth and (c) Stages during embryo development showing geometric and arithmetic phases | `(72, 300, 505, 670)` | One multi-part asset; preceding prose excluded; legend retained. |
| `fig_13_5.png` | 5 | **Figure 13.5** Constant linear growth, a plot of length L against time t | `(45, 108, 270, 355)` | Complete graph frame, axes, points, diagonal, and “Height of the plant” label retained. |
| `fig_13_6.png` | 5 | **Figure 13.6** An idealised sigmoid growth curve typical of cells in culture, and many higher plants and plant organs | `(82, 465, 270, 660)` | Complete sigmoid graph and phase labels retained. |
| `fig_13_7.png` | 6 | **Figure 13.7** Diagrammatic comparison of absolute and relative growth rates. Both leaves A and B have increased their area by 5 cm² in a given time to produce leaves A¹, B¹ leaves. | `(105, 101, 520, 305)` | All superscripts, area values, outlines, and labels retained. |
| `fig_13_8.png` | 8 | **Figure 13.8** Sequence of the developmental process in a plant cell | `(50, 78, 515, 285)` | Full outer frame plus top “Cell Division” and “Death” labels retained. |
| `fig_13_9.png` | 8 | **Figure 13.9** Heterophylly in (a) larkspur and (b) buttercup | `(90, 425, 490, 695)` | Single two-panel asset; juvenile/adult and terrestrial/water-habitat labels retained. |
| `fig_13_10.png` | 9 | **Figure 13.10** Experiment used to demonstrate that tip of the coleoptile is the source of auxin. Arrows indicate direction of light | `(52, 525, 295, 660)` | All four panels a–d and light-direction arrows retained. |
| `fig_13_11.png` | 11 | **Figure 13.11** Apical dominance in plants : (a) A plant with apical bud intact (b) A plant with apical bud removed Note the growth of lateral buds into branches after decapitation. | `(52, 98, 305, 290)` | Both treatments, central explanatory artwork, roots, and panel letters retained. |

## Per-figure label matrix

The following matrix records the labels that were explicitly checked during visual review. A “complete” entry means the listed in-figure labels, arrows, brackets, axes, panel markers, and outer artwork were visually checked against the 440 dpi source grid.

| Figure | Label-bearing content checked | Verification |
|---|---|---|
| 13.1 | Seed coat; Soil line; Cotyledon; Cotyledons; Epicotyl hook; Epicotyl; Hypocotyl; complete root systems | Complete |
| 13.2 | Shoot apical meristem; Shoot; Root; Vascular cambium (shoot and root); Root apical meristem; growth arrows | Complete |
| 13.3 | Zone labels A, B, C, D, E, F, G; parallel leader lines; seedling/root-tip artwork | Complete |
| 13.4 | (a) Arithmetic; (b) Geometric; (c); Zygote divided; Geometric phase: all cells divide; Arithmetic phase; both legend entries | Complete |
| 13.5 | Height of the plant; Time; axis arrows; graph frame; ticks; plotted points; initial-length bracket | Complete |
| 13.6 | Lag phase; Exponential phase; Stationary phase; Size/weight of the organ; Time; axes and curve | Complete |
| 13.7 | A, A¹, B, B¹; 5 cm²; 10 cm²; 50 cm²; 55 cm²; dashed comparison outlines | Complete |
| 13.8 | Cell Division; Death; MERISTEMATIC CELL; Plasmatic growth; Differentiation; Expansion (Elongation); Maturation; MATURE CELL; SENESCENCE | Complete |
| 13.9 | Juvenile; Adult; (a); Terrestrial habitat; Water habitat; (b) | Complete |
| 13.10 | Panel markers a, b, c, d; all four coleoptile treatments; light-direction arrows; tip treatments | Complete |
| 13.11 | Panel markers (a), (b); intact apical bud; removed apical bud; lateral branches; connecting leader/arc; central explanatory structure | Complete |

## Crop and layout decisions

The assets were rendered from hand-pinned rectangles read from the mandatory **440 dpi grid overlays with 5-point coordinate spacing**. The working crop margin is intentionally compact rather than padded with large white borders; approximately 10 PDF points or less is used where needed to protect an outer label, arrow, root, bracket, or leader line. Neighboring prose columns, section headings, and captions were excluded wherever this was possible without clipping meaningful figure artwork.

All emitted images are true grayscale PNGs (`mode=L`) rendered at 300 dpi from the source PDF and passed through `autocontrast`. The source PDF was not modified. The 440 dpi grids, extraction logs, audit output, and visual findings remain in `scratch/ch13_figs/` and `scratch/ch13_visual_findings.md` for re-audit.

## References

[1]: `../../../../SUPREME COMMAND PROMPT.md` "Repository SUPREME COMMAND PROMPT"
[2]: `../../../../skills/ncert-figure-extraction/SKILL.md` "NCERT figure-extraction skill"
[3]: `../../../../Chapter/class 11/Chapter 13 - Plant Growth and Development.pdf` "NCERT Class 11 Chapter 13 source PDF"
