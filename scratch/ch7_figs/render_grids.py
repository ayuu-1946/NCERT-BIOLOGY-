"""Render mandatory 440-DPI, 5-pt grid overlays for Class 11 Chapter 7."""
import os
import pymupdf
from PIL import Image, ImageDraw

SRC = 'Chapter/class 11/Chapter 07 - Structural Organisation in Animals.pdf'
PAGES = [2, 3, 4, 5, 6, 8, 9, 10, 12, 13, 14, 16]  # all pages containing Figures 7.1–7.8 and 7.14–7.22
OUT = 'scratch/ch7_figs/grid_4x'
DPI = 440
STEP = 5
LABEL_STEP = 20

os.makedirs(OUT, exist_ok=True)
doc = pymupdf.open(SRC)
try:
    for pno in PAGES:
        page = doc[pno - 1]
        z = DPI / 72
        pix = page.get_pixmap(dpi=DPI, alpha=False)
        img = Image.frombytes('RGB', (pix.width, pix.height), pix.samples)
        draw = ImageDraw.Draw(img)
        for x in range(0, int(page.rect.width) + 1, STEP):
            xx = x * z
            draw.line([(xx, 0), (xx, img.height)], fill=(175, 215, 255), width=1)
            if x % LABEL_STEP == 0:
                draw.text((xx + 2, 2), str(x), fill=(220, 0, 0))
        for y in range(0, int(page.rect.height) + 1, STEP):
            yy = y * z
            draw.line([(0, yy), (img.width, yy)], fill=(175, 215, 255), width=1)
            if y % LABEL_STEP == 0:
                draw.text((2, yy + 2), str(y), fill=(220, 0, 0))
        path = f'{OUT}/p{pno:02d}.png'
        img.save(path)
        print(f'p{pno:02d}: {img.size}, {DPI} dpi -> {path}')
finally:
    doc.close()
