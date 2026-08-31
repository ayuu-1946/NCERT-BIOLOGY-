# Chapter 13 — Plant Growth and Development Tracker

## Current status

**Figure extraction stage:** Complete. Eleven numbered NCERT figures were identified and extracted as eleven standalone assets. All assets are present under `assets/`, are true grayscale PNGs (`mode=L`), and were individually checked through the final contact sheet and targeted full-resolution reviews.

**Three-part crop audit:** Complete. Check A (text-layer word grazing) is clean for all eleven assets. Check B (drawing-extent overflow) is clean for the vector-bearing assets; Figures 13.4 and 13.10 are raster artwork for which the drawing check is not applicable. Check C (6-point border-band ink) is clean for all eleven assets. Figure 13.1 required a documented bottom-edge exception because the lowest root artwork extends into the source caption band; the final crop includes the root tips instead of clipping them.

**Scope:** This task covers figure extraction and documentation only. Full rewritten chapter PDF generation, facts inventory, and chapter replacement gates have not been started by this task.

## Re-pin log

| Asset | Final change | Reason |
|---|---|---|
| `fig_13_1.png` | Final rectangle `(55, 95, 515, 389)` | First crop clipped the lowest root tips. Source geometry confirmed the artwork overlaps the caption baseline; the crop was extended to retain all roots, with the exception recorded in the inventory. |
| `fig_13_2.png` | Final `y1=377` | The lower “Root apical meristem” label and leader line were clipped in the first crop. |
| `fig_13_4.png` | Final `y0=300` | The first crop included the preceding “Growth Rates” prose. The final crop begins at the first figure artwork and retains all three parts and the legend. |
| `fig_13_5.png` | Final `x0=45` | The first crop clipped the vertical “Height of the plant” axis label. |
| `fig_13_6.png` | Final `y1=660` | The initial crop grazed the “Time” axis label; the final crop retains it completely while remaining above the caption. |
| `fig_13_8.png` | Final `y0=78` | The first crop trimmed the top “Cell Division” and “Death” labels and the outer frame. |
| `fig_13_9.png` | Final `y0=425` | The first crop grazed the preceding paragraph; the final crop begins below the prose. |
| `fig_13_10.png` | Final `(52, 525, 295, 660)` | The first crop grazed the preceding heading/prose and produced a right-edge ink warning; the final crop retains all four panels and clears the warning. |
| `fig_13_11.png` | Final `y1=290` | The first crop left the lowest root tips too close to the edge; the final crop gives them a small safety margin while remaining above the caption. |

## Reproduction commands

From the repository root, using the available local environment:

```bash
python3 'notes/class 11/Ch13_PlantGrowthAndDevelopment/extract_figures.py'
python3 'notes/class 11/Ch13_PlantGrowthAndDevelopment/audit_figures.py'
```

The mandatory source grids were rendered at 440 dpi with 5-point coordinate spacing by `scratch/render_ch13_grids.py` and are stored in `scratch/ch13_figs/grid_4x/`.

## Deliverables

The chapter folder contains `extract_figures.py`, `audit_figures.py`, `Ch13_PlantGrowthAndDevelopment_inventory.md`, this tracker, and eleven monochrome PNG assets under `assets/`. Supporting geometry reports, audit logs, grid overlays, the contact sheet, and visual-review findings remain under `scratch/`.

## References

[1]: `../../../../SUPREME COMMAND PROMPT.md` "Repository SUPREME COMMAND PROMPT"
[2]: `../../../../skills/ncert-figure-extraction/SKILL.md` "NCERT figure-extraction skill"
[3]: `../../../../Chapter/class 11/Chapter 13 - Plant Growth and Development.pdf` "NCERT Class 11 Chapter 13 source PDF"
