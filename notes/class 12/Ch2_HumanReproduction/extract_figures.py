"""4x-reviewed figure extraction for Class 12 Chapter 2: Human Reproduction.
Rects are in source-PDF points; captions are excluded because they are rendered in the notes text.
"""
import os
import pymupdf
from PIL import Image, ImageOps

SRC = 'Chapter/class 12/Chapter 2 - Human Reproduction.pdf'
OUT_DIR = 'notes/class 12/Ch2_HumanReproduction/assets'
RENDER_DPI = 300

FIGS = [
    ('2_1a', 2, (180, 78, 568, 288)),  # p2: upper male-pelvis diagram; right prose column begins at x<205; caption begins below y~300
    ('2_1b', 2, (215, 315, 535, 550)),  # p2: lower male reproductive-system diagram; bottom edge above page-number furniture
    ('2_2', 3, (160, 82, 535, 360)),  # p3: seminiferous-tubule plate; caption begins below y~360
    ('2_3a', 4, (35, 70, 540, 350)),  # p4: upper female-pelvis plate; caption begins below y~350
    ('2_3b', 4, (38, 385, 535, 690)),  # p4: lower female-system plate; caption begins below y~690
    ('2_4', 5, (172, 455, 520, 690)),  # p5: mammary gland; caption begins below y~690
    ('2_5', 6, (275, 355, 530, 582)),  # p6: enlarged seminiferous tubule; caption begins below y~605
    ('2_6', 7, (48, 72, 255, 380)),  # p7: sperm structure; caption begins below y~385
    ('2_7', 8, (240, 70, 545, 297)),  # p8: ovary section; caption begins below y~315
    ('2_8', 8, (35, 340, 545, 595)),  # p8: combined spermatogenesis/oogenesis schematic; preserve shared central annotations
    ('2_9', 9, (105, 78, 525, 475)),  # p9: full menstrual-cycle chart; caption begins below y~475
    ('2_10', 10, (245, 390, 545, 700)),  # p10: ovum and sperm diagram; caption begins below y~700
    ('2_11', 11, (45, 370, 545, 680)),  # p11: connected multi-stage transport/fertilisation/implantation figure
    ('2_12', 12, (180, 435, 545, 700)),  # p12: foetus within uterus; caption begins below y~700
]

def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    doc = pymupdf.open(SRC)
    for fid, pno, rect in FIGS:
        page = doc[pno - 1]
        clip = pymupdf.Rect(*rect) & page.rect
        pix = page.get_pixmap(clip=clip, dpi=RENDER_DPI, alpha=False)
        img = Image.frombytes('RGB', (pix.width, pix.height), pix.samples).convert('L')
        img = ImageOps.autocontrast(img, cutoff=1)
        out = os.path.join(OUT_DIR, f'fig_{fid}.png')
        img.save(out)
        print(f'fig_{fid}: p{pno} {rect} {img.size} mode={img.mode} -> {out}')

if __name__ == '__main__':
    main()
