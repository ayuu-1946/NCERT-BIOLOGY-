"""§4.4 figure extraction for Ch15 Body Fluids and Circulation.

Rectangles are PDF-point coordinates, hand-pinned from 4× (440 dpi) grid
renders and cross-checked against source-page geometry. Captions are excluded;
all in-figure labels, leader lines, arrows, panels, and terminal artwork are
retained. Crops use a restrained ~8–10 pt margin rather than large whitespace.
Outputs are true monochrome (mode=L) with autocontrast for print safety.
"""
import os
import sys
import pymupdf
from PIL import Image, ImageOps

SRC = 'Chapter/class 11/Chapter 15 - Body Fluids and Circulation.pdf'
OUT_DIR = 'notes/class 11/Ch15_BodyFluidsAndCirculation/assets'
RENDER_DPI = 300

# (asset_id, 1-indexed PDF page, (x0, y0, x1, y1))
FIGS = [
    # p2: vector-drawing union x68.5–527.1/y588.7–683.1; 8–10 pt padding;
    # caption words begin at y696.6, so y1=688 excludes the caption.
    ('15_1', 2, (60, 580, 535, 688)),
    # p6: complete heart, upper vessel tips, and both banks of vector
    # leader-line labels; the upper raster artwork begins near y400 and the
    # rightmost label text reaches past x462, so x1=525 is required. The
    # artwork union ends near y683.8; caption begins at y699.9 and is excluded.
    ('15_2', 6, (130, 390, 525, 690)),
    # p9: ECG plot and P/Q/R/S/T labels; artwork union x282.6–515.5 and
    # y105.8–206.5; y1=210 keeps the baseline but stops before caption text.
    ('15_3', 9, (274, 98, 522, 210)),
    # p10: full pulmonary/systemic loop, heart, vessel cross-sections,
    # capillary panel, arrows and labels; drawing union x136.8–465.6 and
    # y178.3–404.1; caption begins at y412.4 and is excluded.
    ('15_4', 10, (126, 168, 476, 410)),
]


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    doc = pymupdf.open(SRC)
    try:
        for fid, pno, rect in FIGS:
            page = doc[pno - 1]
            clip = pymupdf.Rect(*rect) & page.rect
            pix = page.get_pixmap(clip=clip, dpi=RENDER_DPI, alpha=False)
            img = ImageOps.autocontrast(
                Image.frombytes('RGB', (pix.width, pix.height), pix.samples).convert('L'),
                cutoff=1,
            )
            out = os.path.join(OUT_DIR, f'fig_{fid}.png')
            img.save(out, optimize=True)
            print(f'fig_{fid}: page {pno} rect={rect} size={img.size} mode={img.mode} -> {out}')
    finally:
        doc.close()


if __name__ == '__main__':
    sys.exit(main())
