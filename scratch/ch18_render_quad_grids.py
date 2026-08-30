import os
import pymupdf
from PIL import Image, ImageDraw, ImageFont

SRC = 'Chapter/class 11/Chapter 18 - Neural Control and Coordination.pdf'
PAGES = [2, 3, 4, 5, 6, 7]
OUT = 'scratch/ch18_figs/grid_4x'
DPI = 440  # exactly 4× the prior 110-dpi grid
STEP = 5   # PDF-point spacing; four times finer than 20pt grid
LABEL_STEP = 20
os.makedirs(OUT, exist_ok=True)
doc = pymupdf.open(SRC)
for pno in PAGES:
    page = doc[pno - 1]
    z = DPI / 72
    pix = page.get_pixmap(dpi=DPI, alpha=False)
    img = Image.frombytes('RGB', (pix.width, pix.height), pix.samples)
    d = ImageDraw.Draw(img)
    for x in range(0, int(page.rect.width) + 1, STEP):
        xx = x * z
        d.line([(xx, 0), (xx, img.height)], fill=(175, 215, 255), width=1)
        if x % LABEL_STEP == 0:
            d.text((xx + 2, 2), str(x), fill=(220, 0, 0))
    for y in range(0, int(page.rect.height) + 1, STEP):
        yy = y * z
        d.line([(0, yy), (img.width, yy)], fill=(175, 215, 255), width=1)
        if y % LABEL_STEP == 0:
            d.text((2, yy + 2), str(y), fill=(220, 0, 0))
    path = f'{OUT}/p{pno:02d}.png'
    img.save(path)
    print(path, img.size)
