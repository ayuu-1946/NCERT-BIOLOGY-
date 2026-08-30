import os
import pymupdf

src = 'Chapter/class 12/Chapter 2 - Human Reproduction.pdf'
doc = pymupdf.open(src)
print('source:', src)
print('pages:', doc.page_count)
for i, page in enumerate(doc, 1):
    text = page.get_text('text') or ''
    drawings = page.get_drawings()
    images = page.get_images(full=True)
    if text.strip() or drawings or images:
        print(f'p{i}: text_chars={len(text)} drawings={len(drawings)} images={len(images)}')
        print('  text:', ' '.join(text.split())[:260])
