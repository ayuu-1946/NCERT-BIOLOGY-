"""Re-render and reformat the user-requested Chapter 7 plates.
All source rectangles exclude printed captions. Each half is rendered directly
from the PDF at 600 DPI, with intentional overlap at split lines so labels are
not clipped. The halves are then placed horizontally on a white canvas.
"""
from pathlib import Path
import pymupdf
from PIL import Image
SRC='Chapter/class 11/Chapter 07 - Structural Organisation in Animals.pdf'
D=Path('notes/class 11/Ch7_StructuralOrganisationInAnimals/assets'); D.mkdir(exist_ok=True)
DPI=600

def render(doc,pno,box):
 p=doc[pno-1]; pix=p.get_pixmap(clip=pymupdf.Rect(*box)&p.rect,dpi=DPI,alpha=False)
 return Image.frombytes('RGB',(pix.width,pix.height),pix.samples)

def horiz(a,b,gap=40):
 h=max(a.height,b.height); aa=a.resize((round(a.width*h/a.height),h)); bb=b.resize((round(b.width*h/b.height),h))
 out=Image.new('RGB',(aa.width+gap+bb.width,h),'white'); out.paste(aa,(0,0)); out.paste(bb,(aa.width+gap,0)); return out

with pymupdf.open(SRC) as doc:
 # 7.14 is one continuous broad labeled plate; splitting its body would destroy the central anatomy.
 render(doc,8,(90,475,545,692)).save(D/'fig_7_14.png',optimize=True)
 # 7.18, 7.17, 7.20: split vertically with overlap, then stack side-by-side.
 a=render(doc,12,(140,95,545,325)); b=render(doc,12,(80,315,545,538)); horiz(a,b).save(D/'fig_7_18.png',optimize=True)
 a=render(doc,10,(295,385,545,545)); b=render(doc,10,(295,535,545,688)); horiz(a,b).save(D/'fig_7_17.png',optimize=True)
 a=render(doc,14,(120,95,470,265)); b=render(doc,14,(120,255,470,425)); horiz(a,b).save(D/'fig_7_20.png',optimize=True)
 # 7.5: preserve both panels together but put them horizontally.
 a=render(doc,4,(350,305,542,490)); b=render(doc,4,(350,475,542,665)); horiz(a,b).save(D/'fig_7_5.png',optimize=True)
 # 7.6: panels (a)+(b) together; panel (c) is a separate asset.
 render(doc,5,(65,88,265,330)).save(D/'fig_7_6.png',optimize=True)
 render(doc,5,(65,325,265,450)).save(D/'fig_7_6c.png',optimize=True)
print('Re-rendered requested assets directly from source at 600 DPI.')
