import os
import pymupdf

SRC = 'Chapter/class 11/Chapter 06 - Anatomy of Flowering Plants.pdf'
OUT = 'scratch/ch6_figs'
os.makedirs(OUT, exist_ok=True)
doc = pymupdf.open(SRC)
print('pages', len(doc), 'size', doc[0].rect)
for pno, page in enumerate(doc, 1):
    text = page.get_text('text')
    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
    caps = [ln for ln in lines if ('Figure' in ln or 'Fig.' in ln or 'figure' in ln)]
    print(f'--- p{pno} ---')
    if caps:
        print('captions:', ' | '.join(caps))
    print('text:', ' || '.join(lines[:8]))
    ds = [d['rect'] for d in page.get_drawings() if d['rect'].width > 0.2 and d['rect'].height > 0.2 and d['rect'].width < 480 and d['rect'].height < 420]
    if ds:
        print('drawings:', len(ds), 'extent:', (min(r.x0 for r in ds), min(r.y0 for r in ds), max(r.x1 for r in ds), max(r.y1 for r in ds)))
