"""§4.4 figure extraction for Class 12 Ch2 Human Reproduction.

Rectangles are source-PDF points, freshly cross-checked against the 4× grid
rendered from the current source PDF. Captions and page furniture are excluded.
All output assets are rendered at 300 dpi and converted to true grayscale with
Pillow autocontrast.
"""
import os
import sys
import pymupdf
from PIL import Image, ImageOps

SRC = 'Chapter/class 12/Chapter 2 - Human Reproduction.pdf'
OUT_DIR = 'notes/class 12/Ch2_HumanReproduction/assets'
RENDER_DPI = 300

# (asset_id, 1-indexed PDF page, (x0, y0, x1, y1))
FIGS = [
    # p2 upper male-pelvis diagram; clears prose column and caption below y300.
    ('2_1a', 2, (235, 78, 545, 260)),
    # p2 lower male reproductive-system diagram; bottom clears page furniture.
    ('2_1b', 2, (215, 315, 530, 525)),
    # p3 seminiferous-tubule plate; caption begins below the artwork.
    ('2_2', 3, (160, 82, 535, 345)),
    # p4 upper female-pelvis plate; caption begins below y350.
    ('2_3a', 4, (35, 78, 500, 335)),
    # p4 lower female-system plate; caption begins below y690.
    ('2_3b', 4, (38, 465, 485, 675)),
    # p5 mammary-gland diagram; caption begins below y690.
    ('2_4', 5, (172, 445, 520, 680)),
    # p6 enlarged seminiferous tubule; caption begins below y605.
    ('2_5', 6, (268, 355, 530, 555)),
    # p7 sperm structure; caption begins below y385.
    ('2_6', 7, (48, 82, 290, 350)),
    # p8 ovary section; caption begins below y315.
    ('2_7', 8, (240, 78, 510, 270)),
    # p8 combined spermatogenesis/oogenesis schematic with shared annotations.
    ('2_8', 8, (35, 340, 540, 565)),
    # p9 full menstrual-cycle chart; caption begins below y475.
    ('2_9', 9, (112, 78, 520, 480)),
    # p10 ovum and sperm diagram; caption begins below y700.
    ('2_10', 10, (225, 430, 475, 665)),
    # p11 connected multi-stage transport/fertilisation/implantation figure.
    ('2_11', 11, (120, 400, 495, 645)),
    # p12 foetus within uterus; caption begins below y700.
    ('2_12', 12, (190, 465, 470, 680)),
]

def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    doc = pymupdf.open(SRC)
    try:
        for fid, pno, rect in FIGS:
            page = doc[pno - 1]
            clip = pymupdf.Rect(*rect) & page.rect
            pix = page.get_pixmap(clip=clip, dpi=RENDER_DPI, alpha=False)
            img = ImageOps.autocontrast(Image.frombytes('RGB', (pix.width, pix.height), pix.samples).convert('L'), cutoff=1)
            out = os.path.join(OUT_DIR, f'fig_{fid}.png')
            img.save(out)
            print(f'fig_{fid}: page {pno} rect={rect} size={img.size} mode={img.mode} -> {out}')
    finally:
        doc.close()

if __name__ == '__main__':
    sys.exit(main())
