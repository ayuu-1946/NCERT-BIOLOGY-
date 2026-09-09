# Horizontal Figure Composites

This directory contains horizontal, caption-free composites for two morphology figures. The source figures are retained unchanged in `assets/`; the generated files are separate outputs so the original extracted assets remain available.

## Outputs

| Source | Composite | Panels | Dimensions |
|---|---|---:|---:|
| `assets/fig_5_12.png` | `assets/fig_5_12_horizontal.png` | (a)–(e) | 2716 × 500 px |
| `assets/fig_5_4.png` | `assets/fig_5_4_horizontal.png` | (a)–(c) | 1830 × 843 px |

The original captions are excluded. Existing labels that belong to the panels, such as `(a)` through `(e)`, are preserved. The composites use white canvas padding and a 24-pixel gap between panels.

## Regeneration

From the repository root or this chapter directory, run:

```bash
python3 "notes/class 11/Ch5_MorphologyOfFloweringPlants/compose_horizontal_figures.py"
```

The crop coordinates are recorded directly in the script because the extracted source figures have different layouts: `fig_5_12.png` is a vertical stack of five panels, while `fig_5_4.png` has one upper panel and two lower side-by-side panels.
