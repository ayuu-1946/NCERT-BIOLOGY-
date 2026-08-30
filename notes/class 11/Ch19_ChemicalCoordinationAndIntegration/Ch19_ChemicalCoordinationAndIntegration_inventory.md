# Frozen Inventory — Class 11 Biology, Chapter 19: Chemical Coordination and Integration

Source: `Chapter/class 11/Chapter 19 - Chemical Coordination and Integration.pdf` (14 pages; supplied high-quality source `kebo119.pdf`) | Frozen: 2026-08-30 | Rows: 7 (`F001-F007` figure-label rows)

Tick legend: `x` = entered in the extraction record, asset exists, and the rendered asset was opened and visually verified.

## Scope and status

This inventory records the **figure-extraction deliverables** for Chapter 19. The source chapter is not being rewritten into a standalone NEET replacement PDF in this task, so the running-text coverage gate for a generated replacement PDF is not applicable here. The figure-label rows below are nevertheless recorded in the exact machine-parseable format required by SUPREME COMMAND v6, and every label was harvested by opening the rendered PNG rather than relying on PDF text extraction.

The 4× refinement used the canonical high-density settings: 440 dpi rendering, 5-point grid spacing, coordinate labels every 20 PDF points, grayscale conversion with `convert("L")`, and `autocontrast`. Every final asset was opened individually after the final extraction run.

## Facts

| ID | Section | Type | Exact original wording | Ticked |
|---|---|---|---|---|
| F001 | Fig 19.1 | caption | Figure labels: "Hypothalamus"; "Pituitary"; "Pineal"; "Thyroid and Parathyroid"; "Thymus"; "Pancreas"; "Adrenal"; "Ovary (in female)"; "Testis (in male)" | x |
| F002 | Fig 19.2 | caption | Figure labels: "Hypothalamus"; "Hypothalamic neurons"; "Portal circulation"; "Posterior pituitary"; "Anterior pituitary" | x |
| F003 | Fig 19.3 (a) | caption | Figure (a) labels: "Vocal cord"; "Thyroid"; "Trachea" | x |
| F004 | Fig 19.3 (b) | caption | Figure (b) labels: "Parathyroid glands" | x |
| F005 | Fig 19.4 (a)/(b) | caption | Figure labels: "Adrenal gland"; "Kidney"; "Adrenal cortex"; "Adrenal medulla" | x |
| F006 | Fig 19.5 (a) | caption | Figure (a) labels: "Hormone (e.g., FSH)"; "Receptor"; "Ovarian cell membrane"; "Response 1"; "(Generation of second messenger)"; "(Cyclic AMP or Ca++)"; "Biochemical responses"; "Physiological responses (e.g., ovarian growth)" | x |
| F007 | Fig 19.5 (b) | caption | Figure (b) labels: "Hormone (e.g., estrogen)"; "Uterine cell membrane"; "Nucleus"; "Genome"; "mRNA"; "Proteins"; "Hormone-receptor complex"; "Physiological responses (Tissue growth and differentiation)" | x |

## Figure-label matrix note

The matrix exists in exactly one place: the `## Facts` table above. Each row begins with `Figure labels:` or `Figure (a)/(b) labels:` in the wording column, matching the `_extract_labels` parser used by `check_pdf.py`. There is no duplicate pipe-delimited label table elsewhere in this inventory, so labels are not double-counted and no phantom separator row is created.

## Summary classification

| Summary sentence | Classification | Folded into |
|---|---|---|
| N/A — this deliverable is an extraction inventory, not a rewritten chapter manuscript. | N/A | N/A |

## Exercise-gap terms

| Term/fact assumed by exercises | Explained where |
|---|---|
| N/A — exercise-gap analysis belongs to the separate replacement-chapter Pass 1 inventory and was not silently invented for this extraction-only deliverable. | N/A |

## Figure manifest

| Fig # | Caption (verbatim) | Asset file | Source page | Mono | Verified |
|---|---|---|---:|---|---|
| Fig 19.1 | Location of endocrine glands | `assets/fig_19_1.png` | 2 | yes | yes |
| Fig 19.2 | Diagrammatic representation of pituitary and its relationship with hypothalamus | `assets/fig_19_2.png` | 3 | yes | yes |
| Fig 19.3 (a) | Diagrammatic view of the position of thyroid and parathyroid — ventral side | `assets/fig_19_3a.png` | 4 | yes | yes |
| Fig 19.3 (b) | Diagrammatic view of the position of thyroid and parathyroid — dorsal side | `assets/fig_19_3b.png` | 4 | yes | yes |
| Fig 19.4 (a)/(b) | Diagrammatic representation of adrenal gland above kidney and section showing two parts of adrenal gland | `assets/fig_19_4.png` | 6 | yes | yes |
| Fig 19.5 (a) | Mechanism of hormone action — protein hormone | `assets/fig_19_5a.png` | 10 | yes | yes |
| Fig 19.5 (b) | Mechanism of hormone action — steroid hormone | `assets/fig_19_5b.png` | 11 | yes | yes |

## Extraction record and audit trail

The reproducible extractor is `extract_figures.py`. The canonical 4× grid renderer is `scratch/ch19_render_quad_grids.py`, and its page overlays are stored in `scratch/ch19_figs/grid_4x/`. The three-part mechanical audit is `scratch/audit_ch19.py`; focused source-coordinate checks are in `scratch/focus_ch19.py` and `scratch/probe_ch19_rects.py`; the final visual review is recorded in `scratch/ch19_figs/visual_findings.md`.

Figure 19.4 is intentionally delivered as one combined asset because its two panels are interleaved horizontally. A rectangular crop that isolates either panel cuts the kidney, labels, or connector; the combined crop preserves both panels, the connector, all labels, and both panel markers.

Figures 19.5a and 19.5b are cropped tightly to their existing rectangular box borders. No new box was drawn and no figure content was altered; only the outside white margin was removed.

All seven emitted assets are high-resolution grayscale PNGs (`mode=L`) generated with autocontrast. The final visual gate was completed by opening every final PNG individually and confirming correct figure identity, complete labels and leader lines, no accidental neighboring prose/figure capture, print-legible detail, and monochrome output. The mechanical audit reports clean border-band checks for all seven assets; the vector-extent check is not applicable to the raster artwork in Figure 19.4.

## Gate 1 record

The figure-only extraction gate is green: all seven manifest entries are present, all seven are marked `Mono: yes` and `Verified: yes`, the figure-label matrix has seven contiguous `F001-F007` rows, labels were harvested from opened rendered assets, and the source-to-asset count reconciles as 7 manifest assets. A generated replacement PDF and its running-text label-coverage gate were outside this extraction-only task.
