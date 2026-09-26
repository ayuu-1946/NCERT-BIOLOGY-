# Chapter 2 Figure Tracker — Biological Classification (Class 11)

## Figure 2.4 — horizontal two-half layout

- **Status:** Complete; source panels (a)/(b) and (c)/(d) are grouped into two equal-size cells and placed side by side.
- **Source:** `Chapter/class 11/Chapter 02 - Biological Classification.pdf`, p. 6; coordinates and split point are documented in `extract_figures.py`.
- **Method:** Both halves were rendered directly from the source page at 300 dpi. The shorter lower half is centered on white to match the upper half’s dimensions; the composite is pixel-pasted with no resampling.
- **Verification:** A/B/C extraction audits pass; all four source panels and their (a)–(d) markers were visually checked in the source grid and composite.

## Figures 2.2 and 2.3 — shared page

- **Status:** Display widths reduced to 6.2 cm each; the original source assets and captions are unchanged.
- **Verification:** Both figures and captions appear complete and legible on A4 page 4 of the regenerated PDF; visual inspection confirms all figure labels remain readable.

## Figure 2.5 — horizontal layout

- **Status:** Complete; three source panels were extracted independently and recomposed horizontally.
- **Source:** `Chapter/class 11/Chapter 02 - Biological Classification.pdf`, p. 8.
- **Reproducible workflow:** `extract_figures.py` (440-dpi/5-pt grid pinning documented in the script; source crops rendered at 300 dpi).
- **Assets:** `assets/fig_2_5a.png` (Mucor), `assets/fig_2_5b.png` (Aspergillus), `assets/fig_2_5c.png` (Agaricus), and `assets/fig_2_5.png` (horizontal composite).
- **Verification:** A/B/C extraction audits pass; each panel is 676 px wide; composition pastes the original panel pixels without resizing; all panel markers and full panel edges were visually checked.
- **PDF placement:** Chapter generator uses the composite at its natural 300-dpi size (17.59 cm wide), within the page frame.
