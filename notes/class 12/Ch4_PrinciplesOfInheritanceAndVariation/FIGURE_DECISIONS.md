# Figure decisions — Principles of Inheritance and Variation (Class 12, Ch4)

Chapter folder: `notes/class 12/Ch4_PrinciplesOfInheritanceAndVariation/`
Decision date: 2026-09-10 (Pass 1, session 1-F)
Status: **frozen with the inventory**

## 1. The decision

**No figure in this chapter is extracted, converted or embedded.** All 18
numbered plates stay out of the PDF. This is §4.4's *third state* — operator
omission, not extraction failure.

## 2. Why

1. **The source PDF is a page-image scan.** Every one of the 28 pages is a
   single 1105x1482 DeviceRGB raster; `page.get_text()` returns an empty string
   on every page. There is no vector artwork to clip cleanly and no text layer
   to audit a crop against.
2. **Every plate would reproduce as a low-contrast bitmap.** The scan is about
   130 dpi. At that resolution the printed diagrams — Punnett squares, pedigree
   trees, karyotype plates — come out as grey mush, and converting them to
   monochrome (`convert("L")` + `autocontrast`) makes them worse, not better.
   A figure that prints illegibly is worse than no figure, because it takes a
   page and delivers nothing.
3. **The operator directed it explicitly** (session brief 2026-09-10): "No
   figure Extraction because it's exceptional case all figures are useless".

## 3. What the decision does and does not permit

Permitted — and required — because the third state says the omission is only
licensed once *every fact in the figure's caption and labels is carried in
prose*:

* every caption is a `Type: caption` Facts row, verbatim;
* every in-figure label is a `Type: figure-labels` Facts row (163 distinct
  labels after deduplication, listed per figure in the inventory);
* Pass 2 must put all 163 labels into the running text — Punnett squares and
  cross diagrams become real `data_table` grids, the pedigree-symbol plate
  becomes a two-column symbol/meaning table, and the rest get a short verbatim
  "Read the plate" note — or `check_pdf.py` check 6 fails.

Not permitted:

* **no** "Figures requiring manual attention" heading in the PDF. That heading
  promises a reader a diagram that should have been there; using it for plates
  dropped on purpose is a false alarm, and Rule 6 keeps the PDF from explaining
  itself.
* no silent gap between the manifest and the PDF. The manifest above annotates
  every row "not extracted (operator decision 2026-09-10)" precisely so it
  cannot be mistaken for a broken promise.

## 4. Per-plate record

| Plate | Printed on | Decision | Where its facts now live |
|---|---|---|---|
| Fig 4.1 Seven pairs of contrasting traits | p4 | omitted | caption row + 22 labels; the seven pairs are also Table 4.1's rows |
| Fig 4.2 Steps in making a cross in pea | p5 | omitted | caption row + 10 labels (emasculation / pollination) |
| Fig 4.3 Diagrammatic representation of monohybrid cross | p6 | omitted | caption row + 6 labels (`F<sub>1</sub> generation`, `F<sub>2</sub> generation`, Selfing) |
| Fig 4.4 Punnett square, monohybrid cross | p7 | omitted | caption row + 12 labels; Pass 2 renders the square as a `data_table` |
| Fig 4.5 Test cross | p9 | omitted | caption row + 8 labels |
| Fig 4.6 Snapdragon monohybrid cross | p10 | omitted | caption row + 13 labels |
| Fig 4.7 Dihybrid cross | p13 | omitted | caption row + 25 labels; Pass 2 renders the 4x4 square as a `data_table` |
| Fig 4.8 Meiosis and germ cell formation | p15 | omitted | caption row + 6 labels |
| Fig 4.9 Independent assortment of chromosomes | p16 | omitted | caption row + 7 labels — **the only colour-carrying plate**: orange, green, red and yellow are named in the running text |
| Fig 4.10 *Drosophila melanogaster* (a) Male (b) Female | p17 | omitted | caption row; labels are bare panel markers `(a)`/`(b)`, which carry no fact |
| Fig 4.11 Linkage — Cross A and Cross B | p17-p18 | omitted | caption row + 16 labels (98.7 / 1.3 / 62.8 / 37.2 per cent); Pass 2 renders both crosses as small tables |
| Fig 4.12 Determination of sex by chromosomal differences | p20 | omitted | caption row + 4 labels (XX / XY / ZW / ZZ) |
| Fig 4.13 (first) Sex determination in honey bee | p21 | omitted | caption row + 9 labels; Pass 2 renders Parents / Gametes / F<sub>1</sub> with 32 and 16 as a table |
| Fig 4.13 (second) Symbols used in the human pedigree analysis | p22 | omitted — **NCERT prints the number 4.13 twice**; both are kept as printed | caption row + 9 labels; Pass 2 renders a two-column symbol/meaning table |
| Fig 4.14 Representative pedigree analysis | p23 | omitted | caption row; labels are bare panel markers `(a)`/`(b)` |
| Fig 4.15 Micrograph and beta-chain amino acid composition | p24 | omitted | caption row + 8 labels (the two peptide sequences, GAG/GUG, CTC/CAC) |
| Fig 4.16 Down's syndrome individual and chromosomes | p26 | omitted | caption row + 6 labels (the clinical features) |
| Fig 4.17 Klinefelter / Turner sex-chromosome composition | p26 | omitted | caption row + 2 labels (the two character sets) |
| Scientist plates, "JAMES WATSON" / "FRANCIS CRICK" | p2 | **never embeddable** — §4.4 hard no on photographs of people, independent of this decision | profile rows F011-F026, text only |

## 5. Consequences for `check_pdf.py`

| Check | Effect of this decision |
|---|---|
| 3. embedded images grayscale | passes trivially — no image is embedded |
| 4. no person photograph | no portrait row exists (the profile caption row is worded to avoid the portrait keywords) and no image is embedded at all |
| 6. figure-label coverage | **still active and still demanding** — 163 labels must all reach the running text |
| 7. inventory fully ticked | unaffected |

## 6. Reversing the decision

If a later session obtains a text-layered or high-resolution copy of this
chapter, the plates can be extracted then. The manifest rows, the caption rows
and the label rows are all already in place, so the only work would be
`scratch/`-style extraction plus `figure()` calls — no inventory row would need
to change. Until then the omission stands and must not be "fixed" by embedding
a bad crop.
