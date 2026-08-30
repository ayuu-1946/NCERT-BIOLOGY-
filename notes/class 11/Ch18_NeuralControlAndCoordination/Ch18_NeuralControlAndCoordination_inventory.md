# Class 11 Biology — Chapter 18 Figure Inventory

The four NCERT figures in Chapter 18 were extracted from the source PDF using hand-pinned rectangles read from 440-dpi overlays with 5-point grid spacing, equivalent to a 4× refinement over the repository’s original 110-dpi, 20-point grid. Assets are rendered at 440 dpi, converted to grayscale, and autocontrasted.

| Figure | Source PDF page | Caption | Asset |
|---|---:|---|---|
| 18.1 | 3 | Structure of a neuron | `assets/fig_18_1.png` |
| 18.2 | 4 | Diagrammatic representation of impulse conduction through an axon (at points A and B) | `assets/fig_18_2.png` |
| 18.3 | 5 | Diagram showing axon terminal and synapse | `assets/fig_18_3.png` |
| 18.4 | 6 | Diagram showing sagital section of the human brain | `assets/fig_18_4.png` |

## Extraction and audit record

The extraction script is `extract_figures.py`. The 4× grid overlays are in `scratch/ch18_figs/grid_4x/`, and the cache-safe final contact sheet is `scratch/ch18_figs/contact_sheet_4x_final.png`. The three-part audit was run by `scratch/audit_ch18.py`. Text-layer hits in Figures 18.2 and 18.4 are legitimate in-figure labels (`Na` and `Forebrain`); Figure 18.3 contains no text-layer words because its labels are vector artwork. The border-band audit is clean for all four assets. Figure 18.4 is a raster plate, so the vector drawing-extent check is not applicable. All emitted assets are mode `L` grayscale PNGs.
