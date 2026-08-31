import pymupdf
import numpy as np
from PIL import Image

SRC='Chapter/class 11/Chapter 12 - Respiration in Plants.pdf'
REGIONS={
 '12_1':(4,(40,140,310,590)),
 '12_2':(5,(260,300,530,650)),
 '12_4':(8,(40,80,330,545)),
 '12_5':(9,(270,120,530,300)),
}
doc=pymupdf.open(SRC)
try:
 for fid,(pno,reg) in REGIONS.items():
  page=doc[pno-1]; clip=pymupdf.Rect(*reg)
  pix=page.get_pixmap(clip=clip,dpi=150,alpha=False)
  a=np.array(Image.frombytes('RGB',(pix.width,pix.height),pix.samples))
  sat=a.max(2)-a.min(2)
  mask=sat>8
  ys,xs=np.where(mask)
  z=150/72
  print(fid,'saturated bbox in PDF pts',tuple(round(v,1) for v in (reg[0]+xs.min()/z,reg[1]+ys.min()/z,reg[0]+(xs.max()+1)/z,reg[1]+(ys.max()+1)/z)),'pixels',len(xs))
finally: doc.close()
