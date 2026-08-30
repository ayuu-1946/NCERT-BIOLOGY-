# Class 11 Biology — Chapter 19 Figure Inventory

The figures in Chapter 19 were extracted from the user-supplied high-quality source `kebo119.pdf`, copied reproducibly to `Chapter/class 11/Chapter 19 - Chemical Coordination and Integration.pdf`. Extraction used 440 dpi rendering with 5-point PDF grid spacing and coordinate labels every 20 points. Every final PNG was opened and eyeballed individually after the final extraction run.

| Figure | Source PDF page | Caption / panel | Asset |
|---|---:|---|---|
| 19.1 | 2 | Location of endocrine glands | `assets/fig_19_1.png` |
| 19.2 | 3 | Diagrammatic representation of pituitary and its relationship with hypothalamus | `assets/fig_19_2.png` |
| 19.3a | 4 | Diagrammatic view of the position of thyroid and parathyroid — ventral side | `assets/fig_19_3a.png` |
| 19.3b | 4 | Diagrammatic view of the position of thyroid and parathyroid — dorsal side | `assets/fig_19_3b.png` |
| 19.4 | 6 | Diagrammatic representation of adrenal gland above kidney and section showing two parts of adrenal gland — combined `(a)/(b)` asset | `assets/fig_19_4.png` |
| 19.5a | 10 | Mechanism of hormone action — protein hormone | `assets/fig_19_5a.png` |
| 19.5b | 11 | Mechanism of hormone action — steroid hormone | `assets/fig_19_5b.png` |

## Extraction record

The reproducible extractor is `extract_figures.py`. The 4× grid renderer is `scratch/ch19_render_quad_grids.py`, and its overlays are stored in `scratch/ch19_figs/grid_4x/`. The mechanical audit is `scratch/audit_ch19.py`. The final visual review is recorded in `scratch/ch19_figs/visual_findings.md`.

Figure 19.4 is intentionally delivered as one combined asset because its two panels are interleaved horizontally: a rectangular crop that isolates either panel cuts the kidney, labels, or connector. The combined crop preserves both complete panels, the connector, all labels, and both panel markers rather than shipping incomplete subfigures.

All seven emitted assets are high-resolution grayscale PNGs (`mode=L`) generated with autocontrast. The final audit reports clean text-layer and border-band checks for Figures 19.1, 19.2, 19.3a, 19.3b, 19.4, 19.5a, and 19.5b; the vector-extent check is not applicable to the raster artwork in Figure 19.4.
