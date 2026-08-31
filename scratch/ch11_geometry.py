import pymupdf
SRC='Chapter/class 11/Chapter 11 - Photosynthesis in Higher Plants.pdf'
PAGES=[4,6,7,8,9,10,11,14,16,19]
doc=pymupdf.open(SRC)
for pno in PAGES:
    page=doc[pno-1]
    print(f'\n=== PAGE {pno} ===')
    for w in page.get_text('words'):
        if 'Figure' in w[4] or w[4].startswith('11.') or w[4] in ['Priestley’s','Priestley\'s','experiment','Graph','Diagrammatic','scheme','synthesis','Pathway']:
            print('WORD',w[4],tuple(round(v,1) for v in w[:4]))
    # Print compact drawing clusters by y-band, excluding page-furniture full bands.
    rows=[]
    for d in page.get_drawings():
        r=d['rect']
        if r.width<=0.2 or r.height<=0.2 or r.width>480 or r.height>420: continue
        rows.append((r.y0,r.y1,r.x0,r.x1,r.width,r.height))
    rows.sort()
    for row in rows[:120]:
        print('DRAW',tuple(round(v,1) for v in row))
