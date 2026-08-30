import pymupdf
SRC='Chapter/class 11/Chapter 18 - Neural Control and Coordination.pdf'
doc=pymupdf.open(SRC)
for pno, rect in [(3,(60,48,264,452)),(4,(88,44,520,190)),(6,(80,425,490,692))]:
    page=doc[pno-1]; print('\nPAGE',pno,'RECT',rect)
    r=pymupdf.Rect(*rect)
    for w in page.get_text('words'):
        wr=pymupdf.Rect(*w[:4])
        if not (wr&r).is_empty: print('WORD',tuple(round(v,1) if isinstance(v,float) else v for v in w[:5]))
    print('drawings center-inside extents:')
    for d in page.get_drawings():
        dr=d['rect']; cx,cy=(dr.x0+dr.x1)/2,(dr.y0+dr.y1)/2
        if dr.width>.2 and dr.height>.2 and dr.width<480 and dr.height<420 and rect[0]<=cx<=rect[2] and rect[1]<=cy<=rect[3]:
            print(tuple(round(v,1) for v in (dr.x0,dr.y0,dr.x1,dr.y1)))
