import pymupdf
SRC='Chapter/class 11/Chapter 18 - Neural Control and Coordination.pdf'
doc=pymupdf.open(SRC); page=doc[3]
for w in page.get_text('words'):
    if w[4] in ['Figure','18.2','Diagrammatic','representation','axon','(at','points','A','and','B)']:
        print(tuple(round(v,2) if isinstance(v,float) else v for v in w[:5]))
# print drawings with meaningful extents in expected figure band
for d in page.get_drawings():
    r=d['rect']
    if r.width>2 and r.height>2 and r.width<480 and r.height<420:
        if r.y0<430 and r.y1>80:
            print('DRAW',tuple(round(v,1) for v in (r.x0,r.y0,r.x1,r.y1)), 'w/h',round(r.width,1),round(r.height,1))
