import os
import pymupdf
from PIL import Image, ImageDraw, ImageFont

SRC = 'Chapter/class 11/Chapter 17 - Locomotion and Movement.pdf'
PAGES = [3, 4, 5, 6, 7, 8, 9, 10]
OUT = 'scratch/ch17_figs/quad_grid'
os.makedirs(OUT, exist_ok=True)
doc = pymupdf.open(SRC)
for pno in PAGES:
    page = doc[pno - 1]
    dpi = 440  # exactly 4x the prior 110-dpi grid
    z = dpi / 72
    pix = page.get_pixmap(dpi=dpi, alpha=False)
    img = Image.frombytes('RGB', (pix.width, pix.height), pix.samples)
    d = ImageDraw.Draw(img)
    # Five-point PDF grid spacing gives four times finer coordinate resolution.
    for x in range(0, int(page.rect.width) + 1, 5):
        xx = x * z
        d.line([(xx, 0), (xx, img.height)], fill=(175, 215, 255), width=1)
        if x % 20 == 0:
            d.text((xx + 2, 2), str(x), fill=(235, 0, 0))
    for y in range(0, int(page.rect.height) + 1, 5):
        yy = y * z
        d.line([(0, yy), (img.width, yy)], fill=(175, 215, 255), width=1)
        if y % 20 == 0:
            d.text((2, yy + 2), str(y), fill=(235, 0, 0))
    out = f'{OUT}/p{pno:02d}.png'
    img.save(out, compress_level=1)
    print(f'p{pno:02d}: dpi={dpi} size={img.size} page_rect={tuple(page.rect)} -> {out}')
doc.close()
