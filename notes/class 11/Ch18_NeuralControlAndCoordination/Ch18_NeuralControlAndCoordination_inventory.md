# Frozen Inventory — Class 11 Biology, Chapter 18: Neural Control and Coordination

Source: `Chapter/class 11/Chapter 18 - Neural Control and Coordination.pdf` | Frozen: 2026-08-30 | Rows: 4 (`F001-F004` figure-label rows)

Tick legend: `x` = entered in the extraction record, asset exists, and the rendered asset was opened and visually verified.

## Scope and status

This inventory records the **figure-extraction deliverables** for Chapter 18. The source chapter is not being rewritten into a standalone NEET replacement PDF in this task, so running-text coverage for a generated replacement PDF is not applicable here. The figure-label rows are nevertheless recorded in the exact machine-parseable format required by SUPREME COMMAND v6. Labels were harvested by opening each final rendered PNG, not by relying on PDF text extraction.

The extraction used the canonical high-density 4× workflow: 440 dpi rendering, 5-point PDF grid spacing, coordinate labels every 20 PDF points, grayscale conversion with `convert("L")`, and `autocontrast`. Every final asset was opened individually after the final extraction run.

## Facts

| ID | Section | Type | Exact original wording | Ticked |
|---|---|---|---|---|
| F001 | Fig 18.1 | caption | Figure labels: "Dendrites"; "Nissl’s granules"; "Cell body"; "Nucleus"; "Schwan cell"; "Axon"; "Myelin sheath"; "Node of Ranvier"; "Axon terminal"; "Synaptic knob" | x |
| F002 | Fig 18.2 | caption | Figure labels: "A"; "Na"; "B" | x |
| F003 | Fig 18.3 | caption | Figure labels: "Axon"; "Axon terminal"; "Synaptic vesicles"; "Pre-synaptic membrane"; "Synaptic cleft"; "Post-synaptic membrane"; "Receptors"; "Neurotransmitters"; "Synapse" | x |
| F004 | Fig 18.4 | caption | Figure labels: "Forebrain"; "Cerebrum"; "Cerebral hemisphere"; "Corpus callosum"; "Thalamus"; "Hypothalamus"; "Midbrain"; "Hindbrain"; "Pons"; "Cerebellum"; "Medulla"; "Spinal cord"; "Cerebral aqueduct" | x |

## Figure-label matrix note

The matrix exists in exactly one place: the `## Facts` table above. Each row begins with `Figure labels:` in the wording column, matching the `_extract_labels` parser used by `check_pdf.py`. The repeated `Na` marking in Figure 18.2 is one label wording occurring at two positions in the diagram; it is represented once because the matrix audits label vocabulary, not repeated spatial occurrences. There is no duplicate pipe-delimited label table elsewhere in this inventory, so labels are not double-counted and no phantom separator row is created.

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
| Fig 18.1 | Structure of a neuron | `assets/fig_18_1.png` | 3 | yes | yes |
| Fig 18.2 | Diagrammatic representation of impulse conduction through an axon (at points A and B) | `assets/fig_18_2.png` | 4 | yes | yes |
| Fig 18.3 | Diagram showing axon terminal and synapse | `assets/fig_18_3.png` | 5 | yes | yes |
| Fig 18.4 | Diagram showing sagittal section of the human brain | `assets/fig_18_4.png` | 6 | yes | yes |

## Extraction record and audit trail

The reproducible extractor is `extract_figures.py`. The canonical 4× grid renderer is `scratch/ch18_render_quad_grids.py`, and its page overlays are stored in `scratch/ch18_figs/grid_4x/`. The mechanical audit is `scratch/audit_ch18.py`, and the final visual review is recorded in `scratch/ch18_figs/grid_findings.md`. The opened-image label harvest is preserved in `scratch/ch18_figs/doc_label_harvest.md`.

All four emitted assets are high-resolution grayscale PNGs (`mode=L`) generated with autocontrast. Figure 18.2 was repinned after visual review so the complete lower panel, arrows, charge marks, `A`/`B` markers, and both `Na` labels are retained. Figure 18.4 was repinned to remove preceding body text while preserving the complete brain plate, bracket, and labels.

The final visual gate was completed by opening every final PNG individually and confirming correct figure identity, complete labels and leader lines, no accidental neighboring prose or figure capture, print-legible detail, and monochrome output. The final audit reports clean border-band checks for all four assets. The vector drawing-extent check is not applicable to the raster artwork in Figure 18.4.

## Gate 1 record

The figure-only extraction gate is green: all four manifest entries are present, all four are marked `Mono: yes` and `Verified: yes`, the figure-label matrix has four contiguous `F001-F004` rows, labels were harvested from opened rendered assets, and the source-to-asset count reconciles as four manifest assets. A generated replacement PDF and its running-text label-coverage gate were outside this extraction-only task.
