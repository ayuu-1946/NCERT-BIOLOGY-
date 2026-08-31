"""§4.4 figure extraction for Ch11 Photosynthesis in Higher Plants.

Rectangles are in source-PDF points (page size 576 x 784.8). Each crop is
pinned from the mandatory 440 dpi / 5-point grid and leaves approximately
10 PDF points of safety around the outermost artwork while excluding captions
and neighboring prose.
"""
import os
import pymupdf
from PIL import Image, ImageOps

SRC = "Chapter/class 11/Chapter 11 - Photosynthesis in Higher Plants.pdf"
OUT_DIR = "notes/class 11/Ch11_PhotosynthesisInHigherPlants/assets"
RENDER_DPI = 300

# asset id, source page, rect; comments record the visual/geometric pinning.
FIGS = [
    ("11_1", 4, (50, 105, 275, 435)),   # p4: 2x2 plate; x kept before prose column, bottom above caption y~389
    ("11_2", 6, (85, 495, 525, 685)),   # p6: chloroplast oval + all right labels; bottom above caption y~625
    ("11_3a", 7, (290, 135, 520, 285)),  # p7: top absorption graph; includes pigment labels and axes
    ("11_3b", 7, (290, 300, 520, 444)), # p7: middle action-spectrum graph; includes y-axis and curve
    ("11_3c", 7, (290, 430, 520, 595)), # p7: bottom superimposed graph; includes legend and wavelength axis
    ("11_4", 8, (60, 285, 285, 475)),   # p8: light-harvesting complex; right edge before prose, bottom above caption
    ("11_5", 9, (280, 100, 525, 325)),   # p9: Z scheme; right-column diagram, caption begins below y~265
    ("11_6", 10, (60, 105, 275, 305)),   # p10: cyclic photophosphorylation; left-column diagram, caption below
    ("11_7", 11, (70, 90, 505, 395)),   # p11: complete chemiosmosis diagram; bottom above caption y~350
    ("11_8", 14, (105, 100, 480, 515)),  # p14: Calvin cycle; includes all stage labels/arrows, caption below
    ("11_9", 16, (160, 330, 520, 690)), # p16: full Hatch-Slack two-compartment plate; bottom above caption y~650
    ("11_10", 19, (285, 470, 525, 655)),# p19: light-intensity graph with A-E and axes; caption below
]

def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    doc = pymupdf.open(SRC)
    for fid, pno, rect in FIGS:
        page = doc[pno - 1]
        clip = pymupdf.Rect(*rect) & page.rect
        pix = page.get_pixmap(clip=clip, dpi=RENDER_DPI, alpha=False)
        img = ImageOps.autocontrast(
            Image.frombytes("RGB", (pix.width, pix.height), pix.samples).convert("L"),
            cutoff=1,
        )
        out = os.path.join(OUT_DIR, f"fig_{fid}.png")
        img.save(out, optimize=True)
        print(f"fig_{fid}: p{pno} {rect} {img.size} mode={img.mode} -> {out}")

if __name__ == "__main__":
    main()
