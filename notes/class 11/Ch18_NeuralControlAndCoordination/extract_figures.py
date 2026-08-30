"""§4.4 figure extraction for Ch18 Neural Control and Coordination.
Rects are in PDF points on pages 576 x 784.8. They were hand-pinned from
440-dpi 5-point grid overlays and cross-checked against vector extents or,
for the raster brain plate, the visible outermost ink and caption y-position.
"""
import os
import sys
import pymupdf
from PIL import Image, ImageOps

SRC = "Chapter/class 11/Chapter 18 - Neural Control and Coordination.pdf"
OUT_DIR = "notes/class 11/Ch18_NeuralControlAndCoordination/assets"
RENDER_DPI = 440

FIGS = [
    # p3: neuron labels/artwork; top starts below the running header/page number,\n    # right edge leaves a small margin beyond the outer branch, caption begins at y=464.
    ("18_1", 3, (60, 84, 270, 452)),
    # p4: vector axon diagram; figure labels begin at y=112 and the visible\n    # axon ends near x=368/y=196; top excludes the running header/page number.
    ("18_2", 4, (90, 104, 420, 205)),
    # p5: boxed synapse artwork; get_drawings extent x=154.7..477.6 y=447.0..683.4;
    # box includes right-side labels and stops before caption near y=690.
    ("18_3", 5, (150, 442, 486, 687)),
    # p6: raster brain plate; no usable vector drawings; box follows visible ink,
    # includes all labels, and stops before caption at y=696.8.
    ("18_4", 6, (80, 425, 490, 692)),
]

def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    doc = pymupdf.open(SRC)
    for fid, pno, rect in FIGS:
        page = doc[pno - 1]
        clip = pymupdf.Rect(*rect) & page.rect
        pix = page.get_pixmap(clip=clip, dpi=RENDER_DPI, alpha=False)
        img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples).convert("L")
        img = ImageOps.autocontrast(img, cutoff=1)
        out = os.path.join(OUT_DIR, f"fig_{fid}.png")
        img.save(out, optimize=True)
        print(f"fig_{fid}: p{pno} {rect} {img.size} mode={img.mode} -> {out}")

if __name__ == "__main__":
    sys.exit(main())
