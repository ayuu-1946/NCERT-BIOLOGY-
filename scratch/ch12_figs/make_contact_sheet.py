from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

D=Path('notes/class 11/Ch12_RespirationInPlants/assets')
files=sorted(D.glob('fig_12_*.png'))
CELL_W=420; CELL_H=520; COLS=3; LABEL_H=30
rows=(len(files)+COLS-1)//COLS
sheet=Image.new('L',(COLS*CELL_W,rows*(CELL_H+LABEL_H)),255)
d=ImageDraw.Draw(sheet)
for i,p in enumerate(files):
    im=Image.open(p).convert('L')
    im.thumbnail((CELL_W-20,CELL_H-20))
    x=(i%COLS)*CELL_W; y=(i//COLS)*(CELL_H+LABEL_H)
    d.text((x+8,y+5),p.stem,fill=0)
    px=x+(CELL_W-im.width)//2; py=y+LABEL_H+(CELL_H-im.height)//2
    sheet.paste(im,(px,py))
    d.rectangle((x+1,y+LABEL_H+1,x+CELL_W-2,y+LABEL_H+CELL_H-2),outline=0)
out='scratch/ch12_figs/contact_sheet_final_v2.png'
sheet.save(out)
print(out)
