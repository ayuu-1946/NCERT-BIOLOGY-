import os, pymupdf
from PIL import Image, ImageDraw
SRC='Chapter/class 11/Chapter 07 - Structural Organisation in Animals.pdf'
PAGES=[2,3,4,5,6,8,9,10,11,12,13,14,16]
OUT='scratch/ch7_figs/grid_4x'; PRE='scratch/ch7_figs/page_previews'
os.makedirs(OUT,exist_ok=True); os.makedirs(PRE,exist_ok=True)
DPI=440; STEP=5; LABEL_STEP=20
with pymupdf.open(SRC) as doc:
    thumbs=[]
    for pno in PAGES:
        page=doc[pno-1]; z=DPI/72
        pix=page.get_pixmap(dpi=DPI,alpha=False)
        img=Image.frombytes('RGB',(pix.width,pix.height),pix.samples); d=ImageDraw.Draw(img)
        for x in range(0,int(page.rect.width)+1,STEP):
            xx=x*z; d.line([(xx,0),(xx,img.height)],fill=(175,215,255),width=1)
            if x%LABEL_STEP==0: d.text((xx+2,2),str(x),fill=(220,0,0))
        for y in range(0,int(page.rect.height)+1,STEP):
            yy=y*z; d.line([(0,yy),(img.width,yy)],fill=(175,215,255),width=1)
            if y%LABEL_STEP==0: d.text((2,yy+2),str(y),fill=(220,0,0))
        img.save(f'{OUT}/p{pno:02d}.png')
        pp=page.get_pixmap(dpi=110,alpha=False)
        t=Image.frombytes('RGB',(pp.width,pp.height),pp.samples).convert('RGB'); t.thumbnail((330,430)); thumbs.append((pno,t))
    cols=4; cellw,cellh=350,465
    sheet=Image.new('RGB',(cols*cellw,((len(thumbs)+cols-1)//cols)*cellh),'white'); sd=ImageDraw.Draw(sheet)
    for i,(pno,t) in enumerate(thumbs):
        x=(i%cols)*cellw; y=(i//cols)*cellh; sheet.paste(t,(x+10,y+25)); sd.text((x+10,y+5),f'PDF page {pno}',fill='black')
    sheet.save('scratch/ch7_figs/page_contact_sheet.png')
