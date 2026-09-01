"""SUPREME COMMAND §4.4 figure extraction for Ch11 Photosynthesis in Higher Plants.

Rects are in source-PDF points (page is 576.0 x 784.8). Every rect was pinned
against the mandatory 440 dpi / 5-point coordinate grids in
`scratch/ch11_figs/grid_4x/p<NN>.png`, then cross-checked numerically against
`page.get_drawings()` extents, `page.get_image_rects()` (raster plates) and
`page.get_text("words")` (caption and neighbour-column boundaries).

Gate-1 session 1-F, 2026-09-01: five rects were found clipped when every asset
was opened and read for the figure-label matrix. Those are marked [REPIN] with
the measurement that pinned them.

fig_11_3b is NOT produced from a rect: it is the user-approved reference asset
preserved on disk (848 x 532, converted to true monochrome in place). The
script skips it so a re-run can never overwrite it.
"""
import os
import pymupdf
from PIL import Image, ImageOps

SRC = "Chapter/class 11/Chapter 11 - Photosynthesis in Higher Plants.pdf"
OUT_DIR = "notes/class 11/Ch11_PhotosynthesisInHigherPlants/assets"
RENDER_DPI = 300

# asset id, source page, rect; comments record the geometric pinning.
FIGS = [
    # [REPIN] p4 Priestley plate: drawings extent x 63.7-266.2 y 106.4-442.9;
    # the (c)/(d) panel markers are text-layer words at y 444.5-454.4 and were
    # sheared off by the old y1=435. Caption "Figure 11.1" starts y 459.4, so
    # y1=457 keeps both markers and still excludes the caption.
    ("11_1", 4, (61, 104, 269, 457)),
    # p6 chloroplast: drawings x 92.7-428.8, label words run to x 508.1 and to
    # y 681.6 ("Lipid droplet"). The body line "light-dependent." ends y 492.7,
    # so y0=493 is the highest edge that excludes prose.
    ("11_2", 6, (85, 493, 512, 686)),
    # p7 (a) absorption-spectrum panel: ends immediately after the (a) marker,
    # before the (b) panel that begins below y 300.
    ("11_3a", 7, (290, 135, 520, 285)),
    # p7 (b) action-spectrum panel: PRESERVED user-approved reference asset,
    # 848 x 532; rect recorded for provenance only, never re-rendered.
    ("11_3b", 7, (290, 300, 520, 444)),
    # [REPIN] p7 (c) superimposed panel: the graph frame's top rule reads off
    # the 4x grid at y 424.5 (old y0=430 sliced it); drawings extent
    # x 305.9-514.6, max y1 577.3; the (b) marker above ends y 419 and the
    # Figure 11.3a caption below starts y 600.6.
    ("11_3c", 7, (302, 421, 520, 590)),
    # [REPIN] p8 light-harvesting complex: label words reach x 284.1
    # ("molecules") and drawings reach y 483.3 - the old (60,285,285,475) cut
    # both. Body column starts x 296.4, caption at y 497.1.
    ("11_4", 8, (63, 292, 289, 490)),
    # p9 Z scheme: includes both LHCs and the lower water-splitting line,
    # stopping before the caption.
    ("11_5", 9, (280, 100, 525, 325)),
    # p10 cyclic photophosphorylation: complete, caption excluded.
    ("11_6", 10, (60, 105, 275, 305)),
    # [REPIN] p11 chemiosmosis is a raster plate: get_image_rects returns
    # exactly (77, 105, 456, 396); the old y1=395 clipped the bottom
    # "ADP + Pi -> ATP" row. Caption starts y 403.5.
    ("11_7", 11, (74, 102, 459, 398)),
    # p14 Calvin cycle: raster plate, complete through "Sucrose, starch".
    ("11_8", 14, (105, 100, 480, 515)),
    # [REPIN] p16 Hatch and Slack: raster plate rect is
    # (192.8, 329.6, 487.4, 696.3) - the old y1=690 clipped 6pt off the
    # bundle-sheath cell outline. Caption starts y 700.2.
    ("11_9", 16, (190, 327, 490, 698)),
    # [REPIN] p19 light-intensity graph: the x-axis title "Light intensity" is
    # a text-layer word at y 656.2-665.1, cut by the old y1=655; the y-axis
    # title starts x 297.3, drawings reach x 515.8, caption starts y 688.4.
    ("11_10", 19, (292, 473, 522, 670)),
]

PRESERVED = {"11_3b"}

def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    doc = pymupdf.open(SRC)
    for fid, pno, rect in FIGS:
        out = os.path.join(OUT_DIR, f"fig_{fid}.png")
        if fid in PRESERVED and os.path.exists(out):
            im = Image.open(out)
            print(f"fig_{fid}: preserved reference asset {im.size} mode={im.mode} -> {out}")
            continue
        page = doc[pno - 1]
        clip = pymupdf.Rect(*rect) & page.rect
        pix = page.get_pixmap(clip=clip, dpi=RENDER_DPI, alpha=False)
        img = ImageOps.autocontrast(
            Image.frombytes("RGB", (pix.width, pix.height), pix.samples).convert("L"),
            cutoff=1,
        )
        img.save(out, optimize=True)
        print(f"fig_{fid}: p{pno} {rect} {img.size} mode={img.mode} -> {out}")

if __name__ == "__main__":
    main()
