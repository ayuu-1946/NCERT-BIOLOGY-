import pymupdf

SRC = 'Chapter/class 11/Chapter 12 - Respiration in Plants.pdf'
REGIONS = {
    '12_1': (4, (40, 140, 300, 590)),
    '12_2': (5, (260, 300, 530, 650)),
    '12_3': (7, (260, 80, 530, 345)),
    '12_4': (8, (40, 80, 330, 545)),
    '12_5': (9, (270, 120, 530, 300)),
    '12_6': (11, (40, 80, 530, 465)),
}
doc = pymupdf.open(SRC)
try:
    for fid, (pno, reg) in REGIONS.items():
        page = doc[pno-1]
        x0,y0,x1,y1 = reg
        xs=[]; ys=[]
        for d in page.get_drawings():
            r=d['rect']
            if r.width <= .2 or r.height <= .2 or r.width > 480 or r.height > 420: continue
            cx=(r.x0+r.x1)/2; cy=(r.y0+r.y1)/2
            if x0 <= cx <= x1 and y0 <= cy <= y1:
                xs += [r.x0,r.x1]; ys += [r.y0,r.y1]
        print(f'FIG {fid} page={pno} drawing_union=', (min(xs),min(ys),max(xs),max(ys)) if xs else None)
        print('words in/near region:')
        for w in page.get_text('words'):
            if w[1] >= y0-20 and w[3] <= y1+30 and w[0] >= x0-20 and w[2] <= x1+20:
                print(' ', tuple(round(v,1) if isinstance(v,float) else v for v in w[:5]))
finally:
    doc.close()
