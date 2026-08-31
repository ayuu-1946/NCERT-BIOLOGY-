# Frozen Figure Inventory — Locomotion and Movement

**Source:** `Chapter/class 11/Chapter 17 - Locomotion and Movement.pdf`  
**Class:** 11  
**Chapter:** 17  
**Figure assets:** 10  
**Frozen:** 2026-08-31  
**Author:** Manus AI

This inventory documents the complete extraction of Figures 17.1–17.10 from the NCERT source chapter. Each asset is rendered at 440 dpi, converted to grayscale with Pillow `convert("L")` and `ImageOps.autocontrast(cutoff=1)`, and visually opened individually. Captions are intentionally kept out of the PNG crops so they can be typeset cleanly in a downstream notes PDF; the crop rectangles stop immediately before the source captions wherever the page geometry permits.

## Facts and figure-label matrix

The label matrix is maintained here as one row per figure. Every visible in-figure label identified during individual asset review is listed in the corresponding row; this is the authoritative label record for documentation and downstream running-text coverage.

| ID | Section | Type | Exact original wording / figure-label record | Ticked |
|---|---|---|---|---|
| F001 | 17.1 | figure-labels | Figure labels: “Fascicle (muscle bundle)”; “Muscle fibre (muscle cell)”; “Sarcolemma”; “Blood capillary” | x |
| F002 | 17.2 | figure-labels | Figure labels: “Z line”; “A band”; “I band”; “H zone”; “Sarcomere”; “(a)”; “(b)” | x |
| F003 | 17.3 | figure-labels | Figure labels: “Troponin”; “Tropomyosin”; “F actin”; “Actin binding sites”; “ATP binding sites”; “Head”; “Cross arm”; “(a)”; “(b)” | x |
| F004 | 17.4 | figure-labels | Figure labels: “Actin filament”; “Myosin filament”; “P”; “ADP”; “ATP”; “Cross bridge”; “Myosin head”; “Sliding/rotation”; “(Breaking of cross bridge)”; “(Formation of cross bridge)” | x |
| F005 | 17.5 | figure-labels | Figure labels: “H zone”; “I band”; “A band”; “Relaxed”; “Contracting”; “Maximally Contracted”; “Z line”; “Two Sarcomeres” | x |
| F006 | 17.6 | figure-labels | Figure labels: “Parietal bone”; “Frontal bone”; “Temporal bone”; “Occipital bone”; “Occipital condyle”; “Sphenoid bone”; “Ethmoid bone”; “Lacrimal bone”; “Nasal bone”; “Zygomatic bone”; “Maxilla”; “Mandible”; “Hyoid bone” | x |
| F007 | 17.7 | figure-labels | Figure labels: “Cervical vertebra”; “Thoracic vertebra”; “Lumbar vertebra”; “Intervertebral disc”; “Sacrum”; “Coccyx” | x |
| F008 | 17.8 | figure-labels | Figure labels: “1”; “2”; “3”; “4”; “5”; “6”; “7”; “8”; “9”; “10”; “11”; “12”; “True ribs”; “False ribs”; “Floating ribs”; “Sternum”; “Ribs”; “Vertebral column” | x |
| F009 | 17.9 | figure-labels | Figure labels: “Clavicle”; “Scapula”; “Humerus”; “Radius”; “Ulna”; “Carpals”; “Metacarpals”; “Phalanges” | x |
| F010 | 17.10 | figure-labels | Figure labels: “Ilium”; “Pubis”; “Ischium”; “Coxal bone”; “Sacrum”; “Femur”; “Patella”; “Tibia”; “Fibula”; “Tarsals”; “Metatarsals”; “Phalanges” | x |

## Figure manifest

| Fig # | Caption (verbatim) | Asset file | Source page | Crop rectangle (PDF points) | Mono | Verified |
|---|---|---|---:|---|---|---|
| Fig 17.1 | Diagrammatic cross sectional view of a muscle showing muscle bundles and muscle fibres | `assets/fig_17_1.png` | 3 | `(90,245,525,502)` | Yes | Yes |
| Fig 17.2 | Diagrammatic representation of (a) anatomy of a muscle fibre showing a sarcomere (b) a sarcomere | `assets/fig_17_2.png` | 4 | `(85,325,520,680)` | Yes | Yes |
| Fig 17.3 | (a) An actin (thin) filament (b) Myosin monomer (Meromyosin) | `assets/fig_17_3.png` | 5 | `(85,375,505,595)` | Yes | Yes |
| Fig 17.4 | Stages in cross bridge formation, rotation of head and breaking of cross bridge | `assets/fig_17_4.png` | 6 | `(65,275,565,545)` | Yes | Yes |
| Fig 17.5 | Sliding-filament theory of muscle contraction (movement of the thin filament) | `assets/fig_17_5.png` | 7 | `(65,90,510,425)` | Yes | Yes |
| Fig 17.6 | Diagrammatic view of human skull | `assets/fig_17_6.png` | 8 | `(95,295,525,570)` | Yes | Yes |
| Fig 17.7 | Vertebral column (right lateral view) | `assets/fig_17_7.png` | 9 | `(275,75,520,365)` | Yes | Yes |
| Fig 17.8 | Ribs and rib cage | `assets/fig_17_8.png` | 9 | `(240,425,520,675)` | Yes | Yes |
| Fig 17.9 | Right pectoral girdle and upper arm. (frontal view) | `assets/fig_17_9.png` | 10 | `(50,75,295,382)` | Yes | Yes |
| Fig 17.10 | Right pelvic girdle and lower limb bones (frontal view) | `assets/fig_17_10.png` | 10 | `(50,410,295,758)` | Yes | Yes |

## Extraction and verification notes

The mandatory production grids were rendered at 440 dpi with 5-point grid spacing and 20-point coordinate labels for source pages 3–10. The extracted PNGs were then opened individually, not only viewed as a contact sheet. Corrections were recorded during review: Figures 17.1, 17.2, 17.4, 17.5, 17.6, 17.8, and 17.10 were repinned or regenerated to remove prose/header bleed or restore clipped labels.

Figure 17.8 is the only source region where the neighboring prose column overlaps the left label zone. Its final crop retains the complete “Floating ribs” label; text-layer prose words are selectively removed after rendering, while the vector figure labels and artwork remain untouched. This exception is documented in the extraction script and was confirmed visually.

The final assets are all Pillow mode `L` images. The downstream notes layout must use **10 pt padding** around each bordered figure box, must avoid oversized blank areas, and must keep the complete label set visible at the actual rendered size. No crop includes a source caption; captions are available verbatim in the manifest above.

## Setup record

The active interpreter was `/usr/bin/python3`, Python 3.12.3, and the working directory `/home/ubuntu/work` was writable. Dependencies were installed and verified in that interpreter: PyMuPDF 1.28.2, Pillow 12.3.0, NumPy 2.5.1, pdfplumber 0.11.10, and ReportLab 5.0.0. The requested `npx skills add ayuu-1946/ncert-figure-extraction` command was run; its interactive installer required agent selection and was cancelled after the repository skill was confirmed locally. The checked-out skill is available at `ncert-figure-extraction/SKILL.md` and is followed by this extraction.

## Audit artifacts

The reusable production script is `extract_figures.py`. The mandatory grid renderer is `../../scratch/render_ch17_grids.py` relative to the repository root, and the three-part audit is `../../scratch/audit_ch17.py`. The raw audit output is stored at `../../scratch/audit_ch17_results.txt`.

The audit’s border-band check is clean for all ten assets, all emitted files exist, and all emitted files are mode `L`. The text-layer grazing and drawing-extent checks report two known source-PDF geometry conditions: Figure 17.8 overlaps the neighboring text column by design and is corrected by the documented text-layer mask; Figures 17.1 and 17.3 contain source vector extents that extend a few points beyond the conservative center-inside heuristic even though individual visual review confirms no artwork or label is clipped. These conditions are retained in the raw audit log rather than silently discarded.
