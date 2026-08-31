import os
import pymupdf
from PIL import Image, ImageDraw

SRC = 'Chapter/class 11/Chapter 11 - Photosynthesis in Higher Plants.pdf'
PAGES = [4, 6, 7, 8, 9, 10, 11, 14, 16, 19]
OUT = 'scratch/ch11_figs/grid_4x'
DPI = 440
STEP = 5
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
    img.save(f'{OUT}/p{pno:02d}.png')

# A readable contact sheet from the same rendered pages for quick orientation.
thumbs = []
for pno in PAGES:
    im = Image.open(f'{OUT}/p{pno:02d}.png').convert('RGB')
    im.thumbnail((360, 490))
    card = Image.new('RGB', (380, 530), 'white')
    card.paste(im, ((380-im.width)//2, 28))
    ImageDraw.Draw(card).text((10, 8), f'Chapter page {pno}', fill='black')
    thumbs.append(card)
sheet = Image.new('RGB', (380*2, 530*((len(thumbs)+1)//2)), '#dddddd')
for i, im in enumerate(thumbs):
    sheet.paste(im, ((i%2)*380, (i//2)*530))
sheet.save('scratch/ch11_figs/grid_contact_sheet.png')
print('Rendered', len(PAGES), 'pages to', OUT)
