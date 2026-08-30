import pymupdf

SRC = 'Chapter/class 11/Chapter 18 - Neural Control and Coordination.pdf'
BANDS = {3: (40, 480), 4: (20, 230), 5: (330, 625), 6: (380, 660)}
doc = pymupdf.open(SRC)
for pno, (yt, yb) in BANDS.items():
    page = doc[pno - 1]
    xs=[]; ys=[]; rows=[]
    for d in page.get_drawings():
        r=d['rect']
        if r.width > 0.2 and r.height > 0.2 and r.width < 480 and r.height < 420 and r.y1 >= yt and r.y0 <= yb:
            xs += [r.x0, r.x1]; ys += [r.y0, r.y1]
    print(f'PAGE {pno} drawings extent in band {yt}-{yb}:', (min(xs), min(ys), max(xs), max(ys)) if xs else 'none')
    for w in page.get_text('words'):
        if w[1] >= yt-20 and w[1] <= yb+40:
            if any(k in w[4] for k in ['Figure','18.1','18.2','18.3','18.4']):
                print('  word',w[:5])
