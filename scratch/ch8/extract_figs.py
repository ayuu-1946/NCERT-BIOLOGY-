"""Ch8 figure extraction — SUPREME COMMAND PROMPT v6 §4.4 Step 1 + Step 2.

Clip-renders each NCERT figure region at 300 dpi (survives vector diagrams and
mixed text/graphic figures that raw embedded-image extraction mangles), then
converts every one to true monochrome (convert("L") + autocontrast) before it is
ever allowed near the PDF.

Bounding boxes are in PDF points on the source page (page rect 576 x 784.8) and
were derived from the rendered pages plus the "Figure 8.N" caption anchors, so
each clip stops above its caption and never grabs a neighbouring figure/table.
"""

import os

import pymupdf
from PIL import Image as PILImage, ImageOps

SRC = "/vercel/share/v0-project/Chapter/class 11/Chapter 08 - Cell The Unit of Life.pdf"
OUT = "/vercel/share/v0-project/notes/class 11/Ch8_CellTheUnitOfLife/assets"
RAW = "/vercel/share/v0-project/scratch/ch8/raw"

# fig id -> (page index, x0, y0, x1, y1)
FIGS = {
    "fig_8_1":  (4,  60,  88, 545, 452),   # different shapes of cells (whole plate)
    "fig_8_2":  (5,  55, 100, 293, 315),   # eukaryotic cell vs other organisms
    "fig_8_3a": (7, 100,  95, 525, 425),   # plant cell (through its bottom label row)
    "fig_8_3b": (7, 110, 428, 520, 695),   # animal cell
    "fig_8_4":  (8,  60, 440, 520, 700),   # fluid mosaic model
    "fig_8_5":  (10, 285, 100, 545, 445),  # endoplasmic reticulum
    "fig_8_6":  (10, 300, 460, 545, 695),  # golgi apparatus
    "fig_8_7":  (12,  55, 100, 400, 290),  # mitochondrion LS
    "fig_8_8":  (13,  55, 100, 330, 252),  # chloroplast sectional view
    "fig_8_9":  (13,  45, 505, 235, 610),  # ribosome
    "fig_8_10": (14,  45, 100, 500, 305),  # cilia/flagella section (a)+(b)
    "fig_8_11": (15,  55, 290, 320, 462),  # nucleus
    "fig_8_12": (16, 370,  95, 520, 372),  # chromosome with kinetochore
    "fig_8_13": (16,  40, 448, 520, 690),  # types of chromosomes
}


def main() -> int:
    os.makedirs(OUT, exist_ok=True)
    os.makedirs(RAW, exist_ok=True)
    doc = pymupdf.open(SRC)
    for name, (pno, x0, y0, x1, y1) in FIGS.items():
        page = doc[pno]
        clip = pymupdf.Rect(x0, y0, x1, y1)
        pix = page.get_pixmap(clip=clip, dpi=300)
        raw_path = os.path.join(RAW, name + ".png")
        pix.save(raw_path)

        # §4.4 Step 2 — true monochrome, then autocontrast to recover the tonal
        # range that collapses when hue disappears.
        img = PILImage.open(raw_path).convert("L")
        img = ImageOps.autocontrast(img, cutoff=1)
        out_path = os.path.join(OUT, name + ".png")
        img.save(out_path)

        with PILImage.open(out_path) as chk:
            print(f"{name}: page {pno} {pix.width}x{pix.height} mode={chk.mode}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
