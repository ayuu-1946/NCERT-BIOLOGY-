import os
import pymupdf
from PIL import Image, ImageDraw

src = 'Chapter/class 12/Chapter 2 - Human Reproduction.pdf'
out_dir = 'scratch/human_pages'
os.makedirs(out_dir, exist_ok=True)
doc = pymupdf.open(src)
thumbs = []
for pno, page in enumerate(doc, 1):
    pix = page.get_pixmap(dpi=72, alpha=False)
    im = Image.frombytes('RGB', (pix.width, pix.height), pix.samples)
    path = os.path.join(out_dir, f'p{pno:02d}.png')
    im.save(path)
    thumb = im.copy()
    thumb.thumbnail((284, 389))
    canvas = Image.new('RGB', (300, 425), 'white')
    canvas.paste(thumb, ((300-thumb.width)//2, 28))
    ImageDraw.Draw(canvas).text((10, 8), f'Page {pno}', fill='black')
    thumbs.append(canvas)
cols = 3
rows = (len(thumbs)+cols-1)//cols
sheet = Image.new('RGB', (cols*300, rows*425), '#dddddd')
for i, im in enumerate(thumbs):
    sheet.paste(im, ((i%cols)*300, (i//cols)*425))
sheet.save('scratch/human_pages_contact.png')
print('rendered', len(thumbs), 'pages')
