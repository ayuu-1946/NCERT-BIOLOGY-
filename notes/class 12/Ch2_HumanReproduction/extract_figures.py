"""§4.4 reproducible figure extraction for Class 12 Ch2 Human Reproduction.

Rectangles are source-PDF points, cross-checked against the fresh 4× grids.
Captions and page furniture are excluded. Outputs are rendered at 300 dpi,
converted to true grayscale, and tightened to approximately 10 pt padding
around meaningful printed figure ink. Figure 2.1a additionally removes the
adjacent prose strip while preserving every anatomical label.
"""
import os
import sys
import numpy as np
import pymupdf
from PIL import Image, ImageOps

SRC = 'Chapter/class 12/Chapter 2 - Human Reproduction.pdf'
OUT_DIR = 'notes/class 12/Ch2_HumanReproduction/assets'
RENDER_DPI = 300
PAD = round(10 / 72 * RENDER_DPI)

FIGS = [
    ('2_1a', 2, (195, 78, 545, 260)),
    ('2_1b', 2, (215, 315, 530, 525)),
    ('2_2', 3, (160, 82, 535, 345)),
    ('2_3a', 4, (35, 78, 500, 335)),
    ('2_3b', 4, (38, 465, 485, 675)),
    ('2_4', 5, (172, 445, 520, 680)),
    ('2_5', 6, (268, 355, 530, 555)),
    ('2_6', 7, (48, 82, 290, 350)),
    ('2_7', 8, (240, 78, 510, 270)),
    ('2_8', 8, (35, 340, 540, 565)),
    ('2_9', 9, (112, 78, 520, 480)),
    ('2_10', 10, (225, 430, 475, 665)),
    ('2_11', 11, (120, 400, 495, 645)),
    ('2_12', 12, (190, 465, 510, 680)),
]

# The requested set is tightened; 2.8 appeared twice in the user request.
TIGHT_IDS = {'2_8', '2_12', '2_1a', '2_3b', '2_3a', '2_11', '2_1b'}

def tighten(img, fid):
    a = np.asarray(img)
    ys, xs = np.where(a < 100)  # suppress faint watermark/page furniture
    if len(xs) == 0:
        return img
    x0 = max(0, int(xs.min()) - PAD)
    y0 = max(0, int(ys.min()) - PAD)
    x1 = min(img.width, int(xs.max()) + 1 + PAD)
    y1 = min(img.height, int(ys.max()) + 1 + PAD)
    if fid == '2_1a':
        # The source prose column touches the left raster edge; remove it
        # without cutting the first anatomical label.
        x0 = min(x1 - 1, max(x0, 82))
    return img.crop((x0, y0, x1, y1))

def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    doc = pymupdf.open(SRC)
    try:
        for fid, pno, rect in FIGS:
            page = doc[pno - 1]
            clip = pymupdf.Rect(*rect) & page.rect
            pix = page.get_pixmap(clip=clip, dpi=RENDER_DPI, alpha=False)
            img = Image.frombytes('RGB', (pix.width, pix.height), pix.samples).convert('L')
            img = ImageOps.autocontrast(img, cutoff=1)
            if fid in TIGHT_IDS:
                img = tighten(img, fid)
            out = os.path.join(OUT_DIR, f'fig_{fid}.png')
            img.save(out)
            print(f'fig_{fid}: page={pno} rect={rect} size={img.size} mode={img.mode} -> {out}')
    finally:
        doc.close()

if __name__ == '__main__':
    sys.exit(main())
