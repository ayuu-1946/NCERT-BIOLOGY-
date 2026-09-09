# Caption-Free Morphology Figures

A caption-free copy of every extracted morphology figure is available under `assets/caption_free/`. The original files under `assets/` are intentionally preserved as the source archive. The caption-free set removes printed figure captions only; in-figure labels, panel markers such as `(a)`–`(e)`, arrows, legends, floral formulae, and anatomical callouts are retained.

## Grid-based crop audit

The crops use source-image pixel coordinates in the form `(left, top, right, bottom)`. `None` means the extracted asset did not contain a separate printed caption region and was copied unchanged (with grayscale normalization).

| Figure | Caption-free crop | Result |
|---|---|---|
| 5.1 | unchanged | Labels retained |
| 5.2 | unchanged | Panel labels and root labels retained |
| 5.3 | `(0, 0, 980, 900)` | Root-cap label retained; printed Figure 5.3 caption removed |
| 5.4 | unchanged | Leaf-part labels and panel `(a)` retained |
| 5.5 | `(0, 0, 918, 720)` | `(a) Neem`, `(b) Silk Cotton`, and `Rachis` retained; printed caption removed |
| 5.6 | unchanged | Panel labels and plant names retained |
| 5.7 | unchanged | Photograph retained without an added caption |
| 5.8 | `(0, 0, 951, 570)` | Diagram retained; printed caption removed |
| 5.9 | unchanged | Panel markers retained |
| 5.10 | unchanged | Anatomical labels retained |
| 5.11 | unchanged | Panel markers retained |
| 5.12 | `(0, 0, 592, 2240)` | Panels `(a)`–`(e)` retained; printed caption removed |
| 5.13 | `(0, 0, 1322, 620)` | Anatomical labels and panel markers retained; printed caption removed |
| 5.14 | unchanged | Seed-part labels retained |
| 5.15 | `(0, 0, 1721, 850)` | Seed-part labels retained; printed caption removed |
| 5.16 | `(0, 0, 751, 900)` | Floral formula retained; printed caption removed |
| 5.17 | unchanged | Panel markers and floral diagram retained |

## Regeneration

Run the following from the repository root:

```bash
python3 "notes/class 11/Ch5_MorphologyOfFloweringPlants/remove_captions.py"
```

The script writes all outputs to `assets/caption_free/` and does not overwrite the original extracted assets.
