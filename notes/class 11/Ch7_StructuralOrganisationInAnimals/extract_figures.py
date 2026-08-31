"""Caption-free high-density extraction for Class 11 Biology Chapter 7.
The notes convention excludes printed captions. Each numbered figure is kept as one
complete asset so all panels, labels, arrows, leader lines, and terminal marks remain
together. Rectangles were re-pinned from the mandatory 440-DPI/5-point grids.
"""
import os, sys, pymupdf
SRC='Chapter/class 11/Chapter 07 - Structural Organisation in Animals.pdf'
OUT_DIR='notes/class 11/Ch7_StructuralOrganisationInAnimals/assets'
RENDER_DPI=600
FIGS=[
 ('7_1',2,(65,300,520,462)), ('7_2',3,(70,105,330,232)), ('7_3',3,(105,320,302,423)),
 ('7_4',4,(60,85,542,248)), ('7_5',4,(350,305,542,665)), ('7_6',5,(65,88,265,450)),
 ('7_7',6,(65,100,520,288)), ('7_8',6,(270,495,545,672)),
 ('7_14',8,(90,460,545,692)), ('7_15',9,(70,450,565,688)),
 ('7_16',10,(290,100,525,368)), ('7_17',10,(295,385,475,688)),
 ('7_18',12,(140,95,545,538)), ('7_19',13,(84,455,285,590)),
 ('7_20',14,(120,95,470,425)), ('7_21',16,(305,105,545,325)),
 ('7_22',16,(295,350,545,690)),
]
def main():
 os.makedirs(OUT_DIR,exist_ok=True)
 with pymupdf.open(SRC) as doc:
  for fid,pno,box in FIGS:
   pix=doc[pno-1].get_pixmap(clip=pymupdf.Rect(*box)&doc[pno-1].rect,dpi=RENDER_DPI,alpha=False)
   out=os.path.join(OUT_DIR,f'fig_{fid}.png'); pix.save(out)
   print(f'fig_{fid}: p{pno} box={box} size={pix.width}x{pix.height} -> {out}')
if __name__=='__main__': sys.exit(main())
