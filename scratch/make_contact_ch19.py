from PIL import Image, ImageDraw
import os
D='notes/class 11/Ch19_ChemicalCoordinationAndIntegration/assets'
order=['19_1','19_2','19_3a','19_3b','19_4','19_5a','19_5b']
CELL=520; COLS=2; rows=(len(order)+COLS-1)//COLS
sheet=Image.new('L',(COLS*CELL,rows*(CELL+32)),255); d=ImageDraw.Draw(sheet)
for i,fid in enumerate(order):
    im=Image.open(f'{D}/fig_{fid}.png'); im.thumbnail((CELL-18,CELL-28))
    x=(i%COLS)*CELL; y=(i//COLS)*(CELL+32)
    sheet.paste(im,(x+(CELL-im.width)//2,y+22))
    d.rectangle([x+2,y+18,x+CELL-3,y+CELL+16],outline=0)
    d.text((x+8,y+3),f'fig_{fid}',fill=0)
out='scratch/ch19_figs/contact_sheet_4x_final.png'; sheet.save(out); print(out,sheet.size)
