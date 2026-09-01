"""SUPREME COMMAND §4.4 Step 1 figure extraction — Ch11 Photosynthesis in Higher Plants.

Rectangles are in source-PDF points (page box 576 x 784.8) and were pinned
against the mandatory 440 dpi / 5-point coordinate grids in
`scratch/ch11_figs/grid_4x/`, then validated three ways by `audit_figures.py`
(text-layer grazing, drawings-extent overflow, border-band ink).

Pinning method per rect (Gate 1 session 1-F repin, 2026-09-01):
  * lower bound  = machine-measured drawings/raster extent of the artwork,
                   restricted to the figure's own halo and with the page-scale
                   "Reprint 2026-27" watermark and full-page background raster
                   excluded (they span the whole page and otherwise swallow
                   every extent measurement);
  * upper bound  = first neighbouring text baseline (caption line, adjacent
                   prose column, or the next panel's marker), minus clearance.
Every rect therefore encloses all artwork, all in-figure labels and all panel
markers, and stops short of the NCERT caption and of the body-prose column.
"""
import os

import pymupdf
from PIL import Image, ImageOps

SRC = "Chapter/class 11/Chapter 11 - Photosynthesis in Higher Plants.pdf"
OUT_DIR = "notes/class 11/Ch11_PhotosynthesisInHigherPlants/assets"
RENDER_DPI = 300

# asset id, source page, rect. Comments record the measured pinning evidence.
FIGS = [
    # p4 2x2 Priestley plate. Artwork drawings reach y442.9 and the "(c)"/"(d)"
    # panel markers occupy y444.5-454.4; caption "Figure 11.1" starts y459.4.
    # The old y1=435 sheared both bottom markers off, so the bottom moves to 456.
    # Right edge 272 keeps clear of the prose column at x285.1.
    ("11_1", 4, (61.0, 103.0, 272.0, 456.0)),
    # p6 chloroplast. The artwork's own outer frame begins at exactly y488.0
    # (measured), the right-hand label stack runs to x508.1 ("Outer membrane")
    # and ends y681.6 ("Lipid droplet"), and the caption starts y693.0. The
    # last prose line "light-dependent." occupies y482.2-492.7 at x174-257.3,
    # i.e. it overlaps the artwork's y-band, so no horizontal cut can exclude
    # it and keep the frame: the top is pinned at the frame itself (488.0) and
    # the audit's residual grazing report on that one word is expected and
    # was confirmed by eye to leave no legible prose in the crop.
    ("11_2", 6, (85.0, 488.0, 514.0, 686.0)),
    # p7 absorption spectrum (a). Graph box y149.0-266.1, y-axis label from
    # x307.3, "(a)" marker y269.9-279.5; panel (b)'s y-axis label starts y294.5.
    ("11_3a", 7, (303.0, 145.0, 518.0, 283.0)),
    # p7 action spectrum (b). y-axis label from y294.5, graph box y306.8-395.9,
    # "(b)" marker y411.6-421.0; panel (c)'s graph frame starts y428.8.
    ("11_3b", 7, (303.0, 290.0, 518.0, 424.0)),
    # p7 superimposed (c). Graph frame top y428.8 (legend box inside at
    # y434.4) — old y0=430 clipped the frame; content ends with the "(c)"
    # marker and the "Wavelength of light in nanometres (nm)" axis title at
    # y579.9. Panel (b)'s marker ends y421.0.
    ("11_3c", 7, (303.0, 425.0, 518.0, 584.0)),
    # p8 light-harvesting complex. Drawings (89.0,296.9,236.4,483.3) plus the
    # "Pigment molecules" label to x284.1/y448.8; caption starts y497.1; prose
    # column starts x296.4. Old rect (60,285,285,475) clipped the label block.
    ("11_4", 8, (63.0, 292.0, 290.0, 490.0)),
    # p9 Z scheme. Drawings (277.9,129.9,481.5,309.7); in-figure text reaches
    # x515.7 ("NADPH") and y312.9; caption starts y333.5.
    ("11_5", 9, (274.0, 113.0, 520.0, 320.0)),
    # p10 cyclic photophosphorylation. Drawings (59.9,134.6,267.0,299.2),
    # "Photosystem I" label from y119.8, "Chlorophyll P 700" ends y295.1;
    # caption starts y312.6.
    ("11_6", 10, (57.0, 115.0, 272.0, 305.0)),
    # p11 chemiosmosis. Single raster plate, bbox (77.0,105.0,456.0,396.0);
    # caption starts y403.5. Old y1=395 shaved 1pt off the ATP/H+ row.
    ("11_7", 11, (72.0, 100.0, 461.0, 399.0)),
    # p14 Calvin cycle. Raster bbox (122.0,121.2,461.4,491.6) with vector text
    # labels from y107.6 ("Atmosphere") to y503.9 ("Sucrose, starch") and
    # x132.2-454.8; caption starts y516.6.
    ("11_8", 14, (117.0, 103.0, 466.0, 509.0)),
    # p16 Hatch and Slack. Raster bbox (192.8,329.6,487.4,696.3); caption
    # starts y700.2. Old rect cut 6.3pt off the bottom and carried ~30pt of
    # empty left margin.
    ("11_9", 16, (188.0, 325.0, 492.0, 698.0)),
    # p19 light-intensity graph. Drawings (317.6,477.7,515.8,645.5) plus the
    # rotated "Rate of photosynthesis" y-axis title at x297.3 and the "Light
    # intensity" x-axis title y656.2-665.1; caption starts y688.4; prose
    # column ends x283.9. Old y1=655 cut the x-axis title.
    ("11_10", 19, (292.0, 473.0, 520.0, 670.0)),
]


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    try:
        doc = pymupdf.open(SRC)
    except Exception as exc:  # noqa: BLE001 - loud, named failure per §4.4
        raise SystemExit(f"cannot open source PDF {SRC!r}: {exc}") from exc

    for fid, pno, rect in FIGS:
        page = doc[pno - 1]
        clip = pymupdf.Rect(*rect) & page.rect
        pix = page.get_pixmap(clip=clip, dpi=RENDER_DPI, alpha=False)
        # §4.4 Step 2 — true monochrome, then autocontrast so hue-carried
        # distinctions (the four pigment curves, the two spectra) survive.
        img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples).convert("L")
        img = ImageOps.autocontrast(img, cutoff=1)
        out = os.path.join(OUT_DIR, f"fig_{fid}.png")
        img.save(out, optimize=True)
        print(f"fig_{fid}: p{pno} {rect} {img.size} mode={img.mode} -> {out}")


if __name__ == "__main__":
    main()
