import re
import pymupdf

SRC = 'Chapter/class 11/Chapter 18 - Neural Control and Coordination.pdf'
doc = pymupdf.open(SRC)
print('pages', len(doc), 'size', doc[0].rect)
for i, page in enumerate(doc):
    text = page.get_text()
    if re.search(r'Fig(?:ure)?\s*18\.', text, re.I) or page.get_drawings():
        refs = re.findall(r'.{0,90}Fig(?:ure)?\s*18\..{0,180}', text, re.I | re.S)
        if refs:
            print(f'PAGE {i+1}:', ' | '.join(r.replace('\n', ' ') for r in refs))
