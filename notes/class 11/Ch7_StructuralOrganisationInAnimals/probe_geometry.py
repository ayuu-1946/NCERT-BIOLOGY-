import pymupdf,re
src='Chapter/class 11/Chapter 07 - Structural Organisation in Animals.pdf'
with pymupdf.open(src) as doc:
  for pno in [2,3,4,5,6,8,9,10,11,12,13,14,16]:
    p=doc[pno-1]; words=p.get_text('words')
    print(f'\nPAGE {pno} size={p.rect.width:.1f}x{p.rect.height:.1f}')
    for w in words:
      if re.match(r'(Figure|7\.\d)', w[4], re.I): print('WORD',tuple(round(v,1) if isinstance(v,float) else v for v in w[:4]),w[4])
    # drawings grouped by coarse y bands, excluding page furniture
    ds=[]
    for d in p.get_drawings():
      r=d['rect']
      if r.width>0.2 and r.height>0.2 and r.width<480 and r.height<420 and r.y0>40 and r.y1<p.rect.height-40: ds.append(r)
    bands=[]
    for r in sorted(ds,key=lambda r:r.y0):
      if not bands or r.y0-bands[-1][1]>18: bands.append([r.y0,r.y1,r.x0,r.x1])
      else: bands[-1][1]=max(bands[-1][1],r.y1); bands[-1][2]=min(bands[-1][2],r.x0); bands[-1][3]=max(bands[-1][3],r.x1)
    print('BANDS', [tuple(round(x,1) for x in b) for b in bands])
