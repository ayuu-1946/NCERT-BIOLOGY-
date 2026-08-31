# Chapter 11 — Photosynthesis in Higher Plants

## Extraction documentation

This deliverable contains the extracted NCERT figures from `Chapter/class 11/Chapter 11 - Photosynthesis in Higher Plants.pdf`. The source PDF was not modified. The extraction follows the repository workflow in [`ayuu-1946/ncert-figure-extraction`](https://github.com/ayuu-1946/ncert-figure-extraction) and the project specification in [`SUPREME COMMAND PROMPT.md`](https://github.com/ayuu-1946/NCERT-BIOLOGY-/blob/main/SUPREME%20COMMAND%20PROMPT.md).

The PDF-derived assets are rendered at 300 dpi from hand-pinned PDF rectangles, converted to true grayscale with Pillow `convert("L")`, and passed through `autocontrast`. Figure 11.3b is the exception: after user review, the exact supplied 848 × 532 reference image is preserved as the authoritative PNG asset so its background, framing, and visible `(b)` marker match the requested target exactly. The crop rectangles were first pinned against mandatory 440 dpi coordinate grids with 5-point spacing and 20-point coordinate labels. Captions and neighboring prose were excluded from the assets wherever possible; labels, arrows, panel markers, axes, terminal marks, brackets, and leader lines were retained.

## Environment record

| Item | Verified result |
|---|---|
| Python executable | `/usr/bin/python3` |
| Python version | 3.12.3 |
| Python prefix | `/usr` |
| Working directory | `/home/ubuntu/ncert-figure-work/NCERT-BIOLOGY-` |
| Working directory writable | Yes |
| PyMuPDF | 1.28.2 |
| Pillow | 12.3.0 |
| NumPy | 2.5.1 |
| pdfplumber | 0.11.10 |
| ReportLab | 5.0.0 |
| Repository skill installation | Completed project-scoped under `.agents/skills/ncert-figure-extraction` |

## Figure census and crop register

| Asset | Source page | Crop rectangle `(x0, y0, x1, y1)` in PDF points | Content and label-preservation note |
|---|---:|---|---|
| `fig_11_1.png` | 4 | `(50, 105, 275, 435)` | Four-panel Priestley experiment: bell jars, mouse, candles, plant, arrows, and `(a)`–`(d)` markers. |
| `fig_11_2.png` | 6 | `(85, 495, 525, 685)` | Chloroplast diagram with the complete oval, internal structures, and labels from Outer membrane through Lipid droplet. |
| `fig_11_3a.png` | 7 | `(290, 135, 520, 285)` | Absorption spectrum panel with y-axis, curves, Chlorophyll *a*, Chlorophyll *b*, Carotenoids, and `(a)`, ending before the next panel. |
| `fig_11_3b.png` | 7 | User-supplied reference | Exact 848 × 532 reference-matching action-spectrum panel with complete y-axis label, full curve and graph rectangle, pale page background, watermark, and `(b)` marker; no Figure 11.3c fragment. |
| `fig_11_3c.png` | 7 | `(290, 430, 520, 595)` | Superimposed action/absorption panel with legend, y-axis, wavelength axis, tick labels, and `(c)`. |
| `fig_11_4.png` | 8 | `(60, 285, 285, 475)` | Light-harvesting complex: Photon, pigment molecules, reaction centre, primary acceptor, and arrows. |
| `fig_11_5.png` | 9 | `(280, 100, 525, 325)` | Complete Z scheme: Photosystems II/I, both electron acceptors, both LHCs, electron transport system, ATP/ADP+iP, NADPH/NADP+, water-splitting annotation, and arrows. |
| `fig_11_6.png` | 10 | `(60, 105, 275, 305)` | Cyclic photophosphorylation: Light, Photosystem I, electron acceptor, electron transport system, ADP+iP/ATP, Chlorophyll P700, and arrows. |
| `fig_11_7.png` | 11 | `(70, 90, 505, 395)` | Chemiosmosis: thylakoid membrane, stroma/lumen, PS II/P680, cytochrome b6f, PS I/P700, carriers, H+ marks, NADP(H), ATP synthase, and gradients. |
| `fig_11_8.png` | 14 | `(105, 100, 480, 515)` | Calvin cycle: Atmosphere, CO2+H2O, RuBP, 3-phosphoglycerate, triose phosphate, carboxylation, reduction, regeneration, ATP/NADPH products, arrows, and stage circles 1–3. |
| `fig_11_9.png` | 16 | `(160, 330, 520, 690)` | Hatch and Slack pathway: mesophyll and bundle-sheath compartments, membranes, cell wall, plasmodesmata, C4/C3 acids, PEP, fixation, transport, decarboxylation, regeneration, Calvin-cycle fixation, and arrows. |
| `fig_11_10.png` | 19 | `(285, 470, 525, 655)` | Light-intensity graph with axes, curve, dashed guides, and labels A–E. |

The chapter therefore contains **12 extracted assets**: Figures 11.1, 11.2, 11.3a–c, and Figures 11.4–11.10. Page 22 refers back to Figure 11.10 and contains no new figure plate.

## Validation record

The mechanical audit in `figure_audit.txt` ran three complementary checks. Text-layer grazing was clean for all crops except the legitimate in-figure `LHC` label in Figure 11.5. Drawing-extent checks showed only small edge intersections for complex vector strokes at Figure 11.1, Figure 11.2, and Figure 11.3c; visual inspection confirmed that no visible panel, label, arrow, or terminal mark was clipped. Border-band ink reports are conservative because the source pages contain diagonal watermark artwork and vector strokes adjacent to figure edges; they were reviewed against the final contact sheet rather than treated as standalone failure signals. The image-mode check passed for the 11 PDF-derived assets, which are mode `L` (true grayscale). Figure 11.3b intentionally preserves the user-supplied RGB reference appearance at 848 × 532. The focused reference crop was verified by exact dimensions and visual comparison with the supplied image.

### Targeted rework record

The three requested assets were regenerated independently after targeted visual review. Figure 11.3a now ends immediately after the `(a)` marker; Figure 11.3b now ends immediately after the `(b)` marker; and Figure 11.5 now extends through both LHCs and the lower water-splitting annotation while stopping before the caption. The focused contact sheet at `review/target_contact_sheet.png` was reviewed after regeneration. The targeted regeneration script and log are saved as `scratch/regenerate_target_figures.py` and `target_regeneration_log.txt`.

The main quality controls requested for this chapter are satisfied: the crops use compact geometry rather than large page regions, spacing is kept close to the artwork with approximately 10-point safety margins where feasible, and all figure labels and panel markers are retained in the final assets. The final visual contact sheet is included as a supporting review artifact.

## Reproducibility

Run the following from the repository root to regenerate the assets:

```bash
python3 "notes/class 11/Ch11_PhotosynthesisInHigherPlants/Ch11_PhotosynthesisInHigherPlants_extract_figures.py"
python3 "notes/class 11/Ch11_PhotosynthesisInHigherPlants/audit_figures.py"
```

The mandatory grid renderer is saved at `scratch/render_ch11_grids.py`, and its outputs are in `scratch/ch11_figs/grid_4x/`. The final visual review is `scratch/ch11_figs/assets_contact_sheet.png`.

## References

[1]: https://github.com/ayuu-1946/ncert-figure-extraction "ayuu-1946/ncert-figure-extraction repository"
[2]: https://github.com/ayuu-1946/NCERT-BIOLOGY- "ayuu-1946/NCERT-BIOLOGY- repository"
[3]: https://github.com/ayuu-1946/NCERT-BIOLOGY-/blob/main/SUPREME%20COMMAND%20PROMPT.md "NCERT Biology Supreme Command Prompt"


### Reference-matching revision — Figure 11.3b

After user review, `fig_11_3b.png` was replaced with the exact supplied `1000107125.jpg` reference, converted losslessly to PNG at 848 × 532 pixels. It retains the complete vertical axis label, graph rectangle, plotted curve, cream/pale background, watermark, and `(b)` marker while removing the Figure 11.3c fragment. The replacement is reproducible with `scratch/install_reference_fig_11_3b.py`; the main extractor preserves this authoritative reference asset when the source attachment is available.
