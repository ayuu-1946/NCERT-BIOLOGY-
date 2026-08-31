import pymupdf, os
from PIL import Image
src='Chapter/class 11/Chapter 07 - Structural Organisation in Animals.pdf'
out='scratch/ch7_figs/grid_4x'; os.makedirs(out,exist_ok=True)
with pymupdf.open(src) as doc:
 for pno in [7,15]:
  pix=doc[pno-1].get_pixmap(dpi=440,alpha=False)
  Image.frombytes('RGB',(pix.width,pix.height),pix.samples).save(f'{out}/p{pno:02d}.png')
  print('page',pno,doc[pno-1].get_text())
