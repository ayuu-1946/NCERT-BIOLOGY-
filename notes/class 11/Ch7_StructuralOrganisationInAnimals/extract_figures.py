"""Reproducible tight extraction for Class 11 Biology Chapter 7.
Rects are PDF points. Each box includes the complete artwork, labels, panel markers,
and caption with a small margin, while excluding neighboring prose columns.
"""
import os, sys
import pymupdf
from PIL import Image, ImageOps
SRC='Chapter/class 11/Chapter 07 - Structural Organisation in Animals.pdf'
OUT_DIR='notes/class 11/Ch7_StructuralOrganisationInAnimals/assets'
RENDER_DPI=300
# Pinning notes: boxes were read from scratch/ch7_figs/grid_4x (440 dpi, 5 pt grid)
FIGS=[
 ('7_1',2,(40,238,520,492)),       # p2: all four simple-epithelium panels and caption; excludes prose below
 ('7_2',3,(70,100,340,257)),       # p3: two glandular panels plus left-side labels and caption; stops before right prose
 ('7_3',3,(105,320,310,456)),      # p3: compound epithelium artwork, label, and caption
 ('7_4',4,(60,85,542,270)),        # p4: areolar/adipose panels and all leader labels/caption
 ('7_5',4,(350,305,542,700)),       # p4: dense regular/irregular panels, collagen label, caption
 ('7_6',5,(65,88,265,485)),         # p5: cartilage, bone, blood panels with labels and caption
 ('7_7',6,(65,100,485,320)),        # p6: all three muscle panels, labels, and caption
 ('7_8',6,(270,495,545,715)),       # p6: neural tissue micrograph plus Axon/Cell body/Dendrite/Neuroglia labels/caption
 ('7_14',8,(90,460,545,720)),      # p8: external cockroach figure and caption
 ('7_15',9,(70,450,565,720)),        # p9: head and mouthparts panels, labels, caption
 ('7_16',10,(290,100,525,390)),      # p10: alimentary canal and caption, excludes prose
 ('7_17',10,(295,385,445,718)),      # p10: open circulatory system and caption
 ('7_18',12,(140,95,545,560)),       # p12: male/female reproductive system and caption
 ('7_19',13,(84,455,285,620)),      # p13: external frog figure, labels, and caption
 ('7_20',14,(120,95,470,465)),       # p14: internal frog organs and caption
 ('7_21',16,(305,105,530,350)),      # p16: male reproductive system and every right/left label
 ('7_22',16,(295,350,545,720)),      # p16: female reproductive system and every right-side label/caption
]
def main():
    os.makedirs(OUT_DIR,exist_ok=True)
    with pymupdf.open(SRC) as doc:
        for fid,pno,box in FIGS:
            page=doc[pno-1]; clip=pymupdf.Rect(*box) & page.rect
            pix=page.get_pixmap(clip=clip,dpi=RENDER_DPI,alpha=False)
            im=Image.frombytes('RGB',(pix.width,pix.height),pix.samples)
            # Preserve source colors and labels; only normalize contrast gently.
            im=ImageOps.autocontrast(im,cutoff=1)
            out=os.path.join(OUT_DIR,f'fig_{fid}.png'); im.save(out,optimize=True)
            print(f'fig_{fid}: p{pno} box={box} size={im.size} -> {out}')
if __name__=='__main__': sys.exit(main())
