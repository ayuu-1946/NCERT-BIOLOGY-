import os
import re
import pymupdf

SRC = 'Chapter/class 11/Chapter 12 - Respiration in Plants.pdf'
PAGES = [4, 5, 7, 8, 9, 11]
OUT = 'scratch/ch12_figs/geometry_report.txt'
os.makedirs(os.path.dirname(OUT), exist_ok=True)

doc = pymupdf.open(SRC)
try:
    with open(OUT, 'w', encoding='utf-8') as f:
        for pno in PAGES:
            page = doc[pno - 1]
            f.write(f'\n=== PAGE {pno} {page.rect.width:.1f}x{page.rect.height:.1f} ===\n')
            words = page.get_text('words')
            for w in words:
                if re.search(r'Figure|12\\.[1-6]', w[4], re.I):
                    f.write('WORD ' + ' '.join(str(v) for v in w[:5]) + '\n')
            f.write('DRAWINGS (bounded candidates):\n')
            for i, d in enumerate(page.get_drawings()):
                r = d['rect']
                if 0.2 < r.width < 480 and 0.2 < r.height < 420:
                    f.write(f'{i:03d} {r.x0:.1f} {r.y0:.1f} {r.x1:.1f} {r.y1:.1f} w={r.width:.1f} h={r.height:.1f}\n')
finally:
    doc.close()
print(OUT)
