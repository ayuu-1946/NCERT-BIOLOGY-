import pymupdf
from PIL import Image
SRC='Chapter/class 11/Chapter 18 - Neural Control and Coordination.pdf'
doc=pymupdf.open(SRC); page=doc[3]
for w in page.get_text('words'):
    if w[4] in ['A','B','Na']:
        print(w[:5])
# focused render around the diagram
clip=pymupdf.Rect(70,90,450,270)
pix=page.get_pixmap(clip=clip,dpi=880,alpha=False)
im=Image.frombytes('RGB',(pix.width,pix.height),pix.samples)
im.save('scratch/ch18_figs/fig18_2_focus_880_wide.png')
print('saved',im.size)
