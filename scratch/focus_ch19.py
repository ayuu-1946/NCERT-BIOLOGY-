import os
import pymupdf
from PIL import Image
SRC='Chapter/class 11/Chapter 19 - Chemical Coordination and Integration.pdf'
doc=pymupdf.open(SRC)
items={'fig19_1':(2,(0,80,360,445)),'fig19_2':(3,(0,90,540,370)),'fig19_3':(4,(0,190,300,650)),'fig19_4':(6,(120,220,540,520))}
os.makedirs('scratch/ch19_figs',exist_ok=True)
for name,(pno,rect) in items.items():
 pix=doc[pno-1].get_pixmap(clip=pymupdf.Rect(*rect),dpi=660,alpha=False)
 im=Image.frombytes('RGB',(pix.width,pix.height),pix.samples)
 out=f'scratch/ch19_figs/{name}_focus.png'; im.save(out); print(out,im.size)
