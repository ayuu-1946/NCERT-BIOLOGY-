import pymupdf
SRC='Chapter/class 11/Chapter 19 - Chemical Coordination and Integration.pdf'
doc=pymupdf.open(SRC)
for pno in [2,3,4,6,10,11]:
    page=doc[pno-1]
    print('\nPAGE',pno)
    for w in page.get_text('words'):
        if w[4] in ['Figure','19.1','19.2','19.3','19.4','19.5','(a)','(b)']:
            print('WORD',tuple(round(v,1) if isinstance(v,float) else v for v in w[:5]))
    ys=[]; xs=[]
    for d in page.get_drawings():
        r=d['rect']
        if r.width>.2 and r.height>.2 and r.width<480 and r.height<420:
            if r.y0>80 and r.y1<700:
                xs += [r.x0,r.x1]; ys += [r.y0,r.y1]
    print('DRAWINGS broad extent', (min(xs),min(ys),max(xs),max(ys)) if xs else 'none')
