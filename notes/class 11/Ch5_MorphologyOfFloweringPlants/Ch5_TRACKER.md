## Current status

**Figure extraction stage:** Complete.

**Figure census:** 17 numbered figures → 17 assets. No bonus unnumbered plates were added.

**Assets:** 17/17 present under `assets/`; all are true grayscale (`mode=L`), rendered at approximately 300 dpi, and visually reviewed through a contact sheet with individual full-resolution inspection of the densest asset.

**Three-part crop audit:** Complete. The extraction was repinned after the first pass exposed header/prose bleed and incorrect vertical offsets. The final audit recorded no unexplained edge-ink clusters. Small residual drawing-extent warnings for Figures 5.3, 5.8, 5.12, 5.14, and 5.16 are documented as source-PDF geometry tails within the compact crop boundary; visual review confirmed no label or meaningful artwork edge is clipped. Figure 5.2’s `Laterals` word is an in-figure label and is intentionally retained. Figure 5.8’s caption words and Figure 5.17’s caption words are retained as printed figure identification, not neighboring prose.

**Full chapter replacement/PDF gate:** Not started by this figure-extraction task; no chapter notes PDF was generated.

## Re-pin log

| Asset | Final change | Reason |
|---|---|---|
| `fig_5_1.png` | Moved to `(78, 95, 315, 405)` | Removed the page header and restored the full plant, root-system brackets, and right-side labels. |
| `fig_5_2.png` | Moved to `(78, 420, 555, 665)` | Captured the complete three-panel root plate and labels instead of the upper prose region. |
| `fig_5_3.png` | Final rect `(285, 112, 520, 345)` | User review found the root-hair leader slightly tight; the final crop adds label margin and preserves the full root cap and caption while the audit remains clean. |
| `fig_5_4.png` | Moved to `(45, 95, 278, 435)` | Captured all leaf-part and venation panels with callouts. |
| `fig_5_5.png` | Final rect `(45, 505, 265, 750)` | User review found the upper leaf edge and lower panel/caption lines cut off; the final crop restores them and tightens the right edge away from prose. |
| `fig_5_6.png` | Moved to `(275, 85, 505, 335)` | Restored all three phyllotaxy examples and plant-name labels. |
| `fig_5_7.png` | Moved to `(275, 405, 515, 675)` | Recentered the racemose inflorescence photograph. |
| `fig_5_8.png` | Moved to `(50, 95, 278, 245)` | Recentered the cymose diagram and removed the page header. |
| `fig_5_9.png` | Moved to `(62, 480, 515, 660)` | Removed the preceding prose line and retained all four floral-position panels. |
| `fig_5_10.png` | Moved to `(42, 565, 510, 685)` | Tightened around the complete flower-parts plate. |
| `fig_5_11.png` | Moved to `(125, 95, 475, 305)` | Removed the page header while preserving all four aestivation panels. |
| `fig_5_12.png` | Moved to `(378, 85, 520, 735)` | Extended the lower boundary enough to preserve panel (e), the complete label list, and the printed caption. |
| `fig_5_13.png` | Moved to `(188, 90, 505, 265)` | Recentered the mango/coconut fruit plate. |
| `fig_5_14.png` | Moved to `(48, 465, 285, 605)` | Recentered both dicot-seed views and all callout labels. |
| `fig_5_15.png` | Moved to `(72, 90, 485, 345)` | Restored both monocot-seed views and the complete label set. |
| `fig_5_16.png` | Moved to `(335, 445, 515, 710)` | Removed left-column prose and retained the complete floral diagram and formula. |
| `fig_5_17.png` | Moved to `(102, 455, 475, 690)` | Restored all six Solanum panels and their labels in one compact plate. |

## Reproduction commands

From the repository root:

```bash
/vercel/share/neetenv/bin/python 'notes/class 11/Ch5_MorphologyOfFloweringPlants/extract_figures.py'
/vercel/share/neetenv/bin/python audit_figures.py
```

The mandatory source grids are in `scratch/ch5_figs/grid_4x/`. The final visual-review contact sheet is in `scratch/ch5_figs/assets_contact_sheet_final_1788141206.png`.

## Deliverables

The chapter folder contains the reproducible extraction script, the frozen inventory with the figure-label matrix, this tracker, and 17 grayscale PNG assets under `assets/`. The source PDF remains untouched.

## References

[1]: `../../../../SUPREME COMMAND PROMPT.md` "Repository SUPREME COMMAND prompt"
[2]: `../../../../skills/ncert-figure-extraction/SKILL.md` "ncert-figure-extraction workflow"
