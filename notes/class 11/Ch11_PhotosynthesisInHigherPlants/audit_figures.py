import importlib.util
import os
import pymupdf
import numpy as np
from PIL import Image

BASE = os.path.dirname(__file__)
SCRIPT = os.path.join(BASE, 'Ch11_PhotosynthesisInHigherPlants_extract_figures.py')
spec = importlib.util.spec_from_file_location('ef', SCRIPT)
ef = importlib.util.module_from_spec(spec); spec.loader.exec_module(ef)
doc = pymupdf.open(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(BASE))), ef.SRC))
DPI = 150; z = DPI / 72; BAND = 6.0; DARK = 110
print('--- A) text-layer word grazing ---')
for fid,pno,(x0,y0,x1,y1) in ef.FIGS:
    page=doc[pno-1]; rect=pymupdf.Rect(x0,y0,x1,y1); cut=[]
    inside=[]
    for w in page.get_text('words'):
        wr=pymupdf.Rect(*w[:4]); inter=wr & rect
        if inter.is_empty: continue
        inside.append(w[4])
        if inter.get_area()/max(1e-6,wr.get_area()) <= .9: cut.append(w[4])
    print(f'fig_{fid}: words_in_rect={len(inside)}' + (f' GRAZING {cut}' if cut else ' ok'))
print('--- B) drawings-extent overflow ---')
for fid,pno,(x0,y0,x1,y1) in ef.FIGS:
    page=doc[pno-1]; xs=[]; ys=[]
    for d in page.get_drawings():
        r=d['rect']
        if r.width<=.2 or r.height<=.2 or r.width>480 or r.height>420: continue
        cx,cy=(r.x0+r.x1)/2,(r.y0+r.y1)/2
        if not (x0<=cx<=x1 and y0<=cy<=y1): continue
        xs += [r.x0,r.x1]; ys += [r.y0,r.y1]
    if not xs: print(f'fig_{fid}: no drawings (raster figure)'); continue
    ov=[max(0,x0-min(xs)),max(0,y0-min(ys)),max(0,max(xs)-x1),max(0,max(ys)-y1)]
    print(f'fig_{fid}: ' + (f'OVERFLOW L{ov[0]:.1f} T{ov[1]:.1f} R{ov[2]:.1f} B{ov[3]:.1f}' if max(ov)>3 else 'ok'))
print('--- C) unexplained dark ink in border band ---')
for fid,pno,(x0,y0,x1,y1) in ef.FIGS:
    page=doc[pno-1]; words=[pymupdf.Rect(*w[:4]) for w in page.get_text('words')]; hits=[]
    for side,b in {'L':(x0-BAND,y0,x0,y1),'R':(x1,y0,x1+BAND,y1),'T':(x0,y0-BAND,x1,y0),'B':(x0,y1,x1,y1+BAND)}.items():
        r=pymupdf.Rect(*b)&page.rect
        if r.is_empty: continue
        pix=page.get_pixmap(clip=r,dpi=DPI)
        a=np.array(Image.frombytes('RGB',(pix.width,pix.height),pix.samples).convert('L'))
        keep=0
        for py,px in zip(*np.nonzero(a<DARK)):
            X=r.x0+px/z; Y=r.y0+py/z
            if any(w.x0-1<=X<=w.x1+1 and w.y0-1<=Y<=w.y1+1 for w in words): continue
            keep+=1
        if keep>40: hits.append(f'{side}:{keep}px')
    print(f'fig_{fid}: ' + (f'EDGE-INK {hits}' if hits else 'clean'))
print('--- D) emitted image mode and blank-margin estimate ---')
for fid,_,_ in ef.FIGS:
    p=os.path.join(BASE,'assets',f'fig_{fid}.png'); im=Image.open(p)
    a=np.array(im.convert('L')); ink=a<245
    ys,xs=np.where(ink)
    if len(xs):
        margin=(xs.min(),ys.min(),im.width-1-xs.max(),im.height-1-ys.max())
    else: margin=('empty',)*4
    print(f'fig_{fid}: mode={im.mode} size={im.size} ink_bbox_margins={margin}')
