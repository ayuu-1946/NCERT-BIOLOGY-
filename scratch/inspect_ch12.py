import os
import re
import pymupdf

SRC = 'Chapter/class 11/Chapter 12 - Respiration in Plants.pdf'
OUT = 'scratch/ch12_figs/page_report.txt'
os.makedirs(os.path.dirname(OUT), exist_ok=True)

doc = pymupdf.open(SRC)
with open(OUT, 'w', encoding='utf-8') as f:
    f.write(f'file={SRC}\npages={len(doc)}\n')
    for pno, page in enumerate(doc, 1):
        text = page.get_text('text')
        hits = [ln.strip() for ln in text.splitlines() if re.search(r'Figure|Fig\\.?\\s*12|respiration|glycolysis|Krebs|fermentation|ETS|cycle', ln, re.I)]
        words = page.get_text('words')
        drawings = page.get_drawings()
        f.write(f'\n=== PAGE {pno} size={page.rect.width:.1f}x{page.rect.height:.1f} text_chars={len(text)} words={len(words)} drawings={len(drawings)} ===\n')
        if hits:
            f.write('HITS:\n' + '\n'.join(hits) + '\n')
        f.write('TEXT:\n' + text[:5000] + '\n')
        # compact drawing extents, excluding full-page furniture
        rs = []
        for d in drawings:
            r = d['rect']
            if 0.2 < r.width < 480 and 0.2 < r.height < 420:
                rs.append((r.x0, r.y0, r.x1, r.y1, r.width, r.height))
        f.write(f'DRAWING_EXTENTS_CANDIDATES={len(rs)}\n')
        for r in rs[:100]:
            f.write('  ' + ' '.join(f'{v:.1f}' for v in r) + '\n')
doc.close()
print(OUT)
