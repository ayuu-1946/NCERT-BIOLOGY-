# Class 11 Biology — Chapter 5: Morphology of Flowering Plants

## Figure extraction inventory

This inventory records the 17 numbered NCERT figures extracted from the source chapter PDF. The source page number is the PDF page index, not the printed textbook page number. Each rectangle is in PDF points and was hand-pinned from the mandatory **440 dpi / 5-point grid overlay**. Crops use a compact margin of approximately **10 PDF points** around the artwork; neighboring prose and page furniture are excluded unless the caption is necessary to preserve the figure’s printed identity.

| Asset | Source PDF page | Caption / subject | Rect `(x0, y0, x1, y1)` | Visible labels or panels | Status |
|---|---:|---|---|---|---|
| `fig_5_1.png` | 4 | Parts of a flowering plant | `(78, 95, 315, 405)` | Flower, fruit, stem, leaf, node, internode, bud, primary root, secondary root, shoot/root-system brackets | Extracted, visually checked |
| `fig_5_2.png` | 4 | Different types of roots | `(78, 420, 555, 665)` | Main root, laterals, fibrous roots, adventitious roots; panels (a)–(c) | Extracted, visually checked |
| `fig_5_3.png` | 5 | The regions of the root-tip | `(292, 120, 505, 325)` | Root hair, root cap, region of maturation, elongation, and meristematic activity | Extracted, visually checked |
| `fig_5_4.png` | 6 | Structure of a leaf | `(45, 95, 278, 435)` | Lamina, stipule, petiole, leaf base, axillary bud; panels (a)–(c) | Extracted, visually checked |
| `fig_5_5.png` | 6 | Compound leaves | `(48, 515, 282, 650)` | Rachis; pinnately and palmately compound leaf panels (a)–(b) | Extracted, visually checked |
| `fig_5_6.png` | 7 | Different types of phyllotaxy | `(275, 85, 505, 335)` | China rose, Guava, Alstonia; panels (a)–(c) | Extracted, visually checked |
| `fig_5_7.png` | 7 | Racemose inflorescence | `(275, 405, 515, 675)` | Complete racemose inflorescence photograph | Extracted, visually checked |
| `fig_5_8.png` | 8 | Cymose inflorescence | `(50, 95, 278, 245)` | Complete cymose branching diagram | Extracted, visually checked |
| `fig_5_9.png` | 8 | Position of floral parts on thalamus | `(62, 480, 515, 660)` | Four panels (a)–(d): hypogynous, perigynous, and epigynous positions | Extracted, visually checked |
| `fig_5_10.png` | 9 | Parts of a flower | `(42, 565, 510, 685)` | Androecium, gynoecium, corolla, calyx, pedicel; isolated calyx/corolla/androecium/gynoecium | Extracted, visually checked |
| `fig_5_11.png` | 10 | Types of aestivation in corolla | `(125, 95, 475, 305)` | Valvate, twisted, imbricate, vexillary; panels (a)–(d) | Extracted, visually checked |
| `fig_5_12.png` | 11 | Types of placentation | `(378, 85, 520, 735)` | Marginal, axile, parietal, free central, basal; panels (a)–(e) | Extracted, visually checked |
| `fig_5_13.png` | 12 | Parts of a fruit | `(188, 90, 505, 265)` | Epicarp, mesocarp, seed, endocarp; mango and coconut panels (a)–(b) | Extracted, visually checked |
| `fig_5_14.png` | 12 | Structure of dicotyledonous seed | `(48, 465, 285, 605)` | Seed coat, cotyledon, hilum, micropyle, plumule, radicle | Extracted, visually checked |
| `fig_5_15.png` | 13 | Structure of a monocotyledonous seed | `(72, 90, 485, 345)` | Seed coat and fruit-wall, aleurone layer, endosperm, scutellum, coleoptile, plumule, radicle, coleorhiza, embryo | Extracted, visually checked |
| `fig_5_16.png` | 13 | Floral diagram with floral formula | `(335, 445, 515, 710)` | Floral diagram, mother-axis dot, whorl symbols, and floral formula | Extracted, visually checked |
| `fig_5_17.png` | 14 | *Solanum nigrum* (makoi) plant | `(102, 455, 475, 690)` | Flowering twig, flower, L.S. of flower, stamens, carpel, floral diagram; panels (a)–(f) | Extracted, visually checked |

## Production specifications

All assets are PNG files rendered at **300 dpi**, converted to true grayscale with `Image.convert("L")`, and contrast-normalized with Pillow autocontrast. The extraction script is stored beside this inventory so every asset is reproducible. The source PDF was not modified.

The first crop pass was rejected because several boxes captured page headers, adjacent prose, or the wrong vertical region. The final rectangles were repinned from full-page visual inspection and then tightened so that the figure’s artwork, labels, arrows, panel boundaries, and terminal marks remain present without large blank margins. The dense right-column Figure 5.12 was extended only far enough to retain the complete printed caption instead of visibly truncating it.

## Three-part audit record

The mechanical audit was run after the final regeneration using `audit_figures.py`.

| Audit | Result | Interpretation |
|---|---|---|
| A — text-layer word grazing | No unexplained prose cuts for the artwork regions; caption words are present where the crop intentionally retains the printed caption. | Text-layer checks are vacuous for artwork-only labels on Figures 5.3, 5.7, and similar raster/vector regions, so they were not treated as sufficient by themselves. |
| B — drawings-extent overflow | No material uncaptured drawing extent; reported small residuals are within the intentional compact margin or arise from mixed page geometry. | The full artwork boundaries were confirmed visually against the source pages. |
| C — border-band ink | Clean for all final crops except two explained boundary probes: Figure 5.3’s right-edge ink and Figure 5.5’s top-edge ink are artwork immediately adjacent to the chosen compact boundary. | No unexplained neighboring prose or clipped artwork remained after visual review. |
| D — print asset check | 17/17 assets are `mode=L`, rendered at approximately 300 dpi. | Meets the repository’s monochrome asset requirement. |

## Visual confirmation

Every emitted PNG was reviewed through a full asset contact sheet, followed by individual full-resolution inspection of the densest vertical Figure 5.12. The final review confirmed that all 17 figures are present, the label-bearing diagrams retain their callouts, and no first-pass header/prose bleed remains. The review contact sheet is saved at `scratch/ch5_figs/assets_contact_sheet_final_1788141206.png` for audit reference.

## References

[1]: `../../../Chapter/class 11/Chapter 05 - Morphology of Flowering Plants.pdf` — NCERT Class 11 Biology, Chapter 5 source PDF.
[2]: `../../../../ncert-figure-extraction/SKILL.md` — NCERT Figure Extraction skill, including 440 dpi grid pinning, three-part audit, and visual confirmation requirements.
[3]: `../../../SUPREME%20COMMAND%20PROMPT.md` — Repository production prompt and chapter deliverable conventions.
