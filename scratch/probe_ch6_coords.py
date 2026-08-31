import pymupdf
SRC='Chapter/class 11/Chapter 06 - Anatomy of Flowering Plants.pdf'
doc=pymupdf.open(SRC)
for pno in [2,3,4,5,6]:
    page=doc[pno-1]
    print(f'--- p{pno} words near figure bands ---')
    for w in page.get_text('words'):
        x0,y0,x1,y1,text,*_=w
        if pno==2 and 320<y0<470: print(round(x0,1),round(y0,1),round(x1,1),round(y1,1),repr(text))
        if pno==3 and 50<y0<520 and x0>300: print(round(x0,1),round(y0,1),round(x1,1),round(y1,1),repr(text))
        if pno==4 and x0<300 and 50<y0<580: print(round(x0,1),round(y0,1),round(x1,1),round(y1,1),repr(text))
        if pno==5 and 600<y0<760: print(round(x0,1),round(y0,1),round(x1,1),round(y1,1),repr(text))
        if pno==6 and x0<300 and 200<y0<700: print(round(x0,1),round(y0,1),round(x1,1),round(y1,1),repr(text))
