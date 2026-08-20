"""
Ch9 Biomolecules — figure extraction + monochrome conversion
(SUPREME COMMAND PROMPT §4.4, run during Pass 1).

Pipeline per asset:
  1. Clip-render the figure's bounding box from the source chapter PDF at 300 dpi
     (page.get_pixmap(clip=rect, dpi=300)). Every figure in this chapter is vector
     artwork whose in-figure labels ("Glycine", "Alpha- Helix", "Transition state",
     "Km", ...) are drawn as part of the plate, so a clip render is the only way to
     keep the labels attached to the drawing. (NCERT sets the secondary-structure
     labels with an en dash and a space -- "Alpha- Helix", "Beta-pleated sheet";
     the inventory's label matrix records them verbatim.)
  2. Image.convert("L")              -> true single-channel greyscale
  3. ImageOps.autocontrast(cutoff=1) -> recover contrast lost when hue disappears
     (NCERT prints Figure 9.1 in pink and Figure 9.4 in magenta/red; both go grey)
  4. Save to assets/<name>.png       -- only the converted file is ever embedded.

Sub-part splitting (§4.4 placement rule — each part is placed inline at its own topic):
  * Figure 9.1 is one full-page plate covering six unrelated topics (sugars, amino
    acids, lipids, nitrogen bases, nucleosides, nucleotide). The chapter cites it four
    times from three different sections — twice in §9.1 ("the kind of organic
    (Figure 9.1) ... constituents", and "Three of the twenty are shown in Figure 9.1"),
    once in §9.2 ("categories of compounds shown in Figure 9.1"), and once in §9.6
    ("As you notice in Figure 9.1, the heterocyclic compounds ... purines ...
    pyrimidines") — so it is cropped into its six labelled groups.
  * Figure 9.3 is cited whole in §9.4 ("linked by peptide bonds as shown in
    Figure 9.3") and then part-by-part in §9.7 — "(Figure 9.3 a)", "(Fig. 9.3 b)",
    "(Fig. 9.3 c)", "(Fig. 9.3 d)" — so it is cropped into four panels.
  * Figure 9.5 is cited twice in §9.8.4 — once for pH/temperature (a, b) and once for
    substrate concentration (c) — so its three panels are cropped separately.
  * Figures 9.2 and 9.4 are single figures and are cropped whole.

Coordinates are PDF points (x0, y0, x1, y1), measured from a 110 dpi coordinate-gridded
render of each source page, with the bottom edge of every crop fixed by the caption
line's own text-layer box:
  p4  "Figure 9.1" caption starts y=684.6 -> bottom edge of the 9.1 crops <= 676
  p7  "Figure 9.2" caption starts y=692.3 -> fig_9_2  bottom 684
  p9  "Figure 9.3" caption starts y=418.7 -> fig_9_3d bottom 412
  p12 "Figure 9.4" caption starts y=320.0 -> fig_9_4  bottom 314
  p13 "Figure 9.5" caption starts y=683.4 -> the 9.5 crops bottom 682

Run from anywhere:  python extract_figures.py
"""

import os

import pymupdf
from PIL import Image, ImageOps

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "assets")

# Walk up to the repo root (the directory holding neet_template.py) to find Chapter/.
_root = HERE
while _root != os.path.dirname(_root) and not os.path.exists(
    os.path.join(_root, "neet_template.py")
):
    _root = os.path.dirname(_root)
SRC = os.path.join(_root, "Chapter", "class 11", "Chapter 09 - Biomolecules.pdf")

DPI = 300

# (asset_name, 1-based source page, clip rect)
FIGURES = [
    # ---- Figure 9.1, page 4: six labelled groups of the small-molecule plate ----
    # (i) "Sugars (Carbohydrates)" — glucose + ribose rings, group label at y~207.
    # Left edge 40 (not 62): at 62 the glucose ring's own "HO" substituent and the
    # leading "C" of the "C6H12O6 (Glucose)" label were sliced off.
    ("fig_9_1a", 4, (40.0, 92.0, 268.0, 218.0)),
    # (ii) "Amino acids" — glycine, alanine, serine, group label at y~208.
    ("fig_9_1b", 4, (280.0, 92.0, 520.0, 218.0)),
    # (iii) "Fats and oils (lipids)" — palmitic acid, glycerol, triglyceride,
    # phospholipid (lecithin) and cholesterol; group label at y~443.
    ("fig_9_1c", 4, (58.0, 232.0, 520.0, 456.0)),
    # (iv) "Nitrogen bases" — adenine (purine) and uracil (pyrimidine), left column.
    # Right edge 212 (not 228): at 228 the leading "H" of the nucleoside column's
    # "HOCH2" hung in the right margin of this crop.
    ("fig_9_1d", 4, (60.0, 450.0, 212.0, 676.0)),
    # (v) "Nucleosides" — adenosine and uridine, middle column. Left edge 214 so
    # uridine's "HOCH2", which starts left of adenosine's, keeps its own "H".
    ("fig_9_1e", 4, (214.0, 450.0, 336.0, 676.0)),
    # (vi) "Nucleotide" — adenylic acid, right column.
    ("fig_9_1f", 4, (336.0, 450.0, 524.0, 676.0)),
    # ---- Figure 9.2, page 7: the whole glycogen cartoon ----
    # Left edge 42 (not 55): at 55 the leftmost glucose hexagon of the branch chain,
    # which carries the "O" glycosidic-oxygen label, lost its left face.
    ("fig_9_2", 7, (42.0, 390.0, 530.0, 684.0)),
    # ---- Figure 9.3, page 9: four panels of protein structure ----
    # The plate sits in the left column only: the "(a)"/"(b)"/"(c)"/"(d)" part labels
    # start at x=57 and the widest in-figure label ("Beta-pleated sheet") ends at
    # x=318, while the body-text column begins at x=343. Hence x 52 -> 332 for all
    # four panels: a right edge of 500 dragged the running text into every crop and a
    # left edge of 74 sliced the "(a)"/"(c)" part labels off.
    # (a) Primary — extended polypeptide + ball-and-stick chain, "Polypeptide" label.
    ("fig_9_3a", 9, (52.0, 96.0, 332.0, 180.0)),
    # (b) Secondary — alpha-helix and beta-pleated sheet. Bottom 259 (not 252): at 252
    # the "Alpha-Helix" and "Beta-pleated sheet" labels, which sit on y 245-256, were
    # sliced in half and their lower halves reappeared at the top of (c).
    ("fig_9_3b", 9, (52.0, 180.0, 332.0, 259.0)),
    # (c) Tertiary — folded globule with "Hydrogen bond"/"Disulphide bond" callouts.
    # Top 259 to match (b)'s bottom; the globule's own ink starts just below it.
    ("fig_9_3c", 9, (52.0, 259.0, 332.0, 331.0)),
    # (d) Quaternary — multi-subunit assembly.
    ("fig_9_3d", 9, (52.0, 331.0, 332.0, 412.0)),
    # ---- Figure 9.4, page 12: activation-energy graph ----
    # Left edge 279, measured from the page text layer: the body-text column in this
    # band ends at x=277.7 and the rotated "Potential Energy" axis label occupies
    # x 280.4-290.7. 276 pulled running text in; 286 sliced the axis label.
    ("fig_9_4", 12, (279.0, 96.0, 545.0, 314.0)),
    # ---- Figure 9.5, page 13: three enzyme-activity panels ----
    # Bottom 682 (not 677): the "Km" tick label on panel (c) has a text-layer box of
    # y 669.0-681.0, so 677 clipped its subscript. The caption starts at y=683.4.
    ("fig_9_5a", 13, (50.0, 520.0, 200.0, 682.0)),
    ("fig_9_5b", 13, (200.0, 520.0, 335.0, 682.0)),
    ("fig_9_5c", 13, (335.0, 512.0, 562.0, 682.0)),
]


def main():
    os.makedirs(ASSETS, exist_ok=True)
    doc = pymupdf.open(SRC)
    print(f"source: {SRC}\npages: {doc.page_count}\n")

    for name, page_no, box in FIGURES:
        page = doc[page_no - 1]
        out = os.path.join(ASSETS, f"{name}.png")

        # Step 1 — high-resolution clip render.
        page.get_pixmap(clip=pymupdf.Rect(*box), dpi=DPI).save(out)

        # Steps 2-3 — true monochrome + contrast recovery.
        img = Image.open(out).convert("L")
        img = ImageOps.autocontrast(img, cutoff=1)
        img.save(out)

        check = Image.open(out)
        print(
            f"{name:12s} p{page_no:<3d} {check.size[0]:5d}x{check.size[1]:<5d} "
            f"mode={check.mode} extrema={check.getextrema()}"
        )

    doc.close()


if __name__ == "__main__":
    main()
