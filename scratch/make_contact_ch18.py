from PIL import Image, ImageDraw
import os
D='notes/class 11/Ch18_NeuralControlAndCoordination/assets'
order=['18_1','18_2','18_3','18_4']
CELL=560; COLS=2; rows=2
sheet=Image.new('L',(COLS*CELL,rows*(CELL+34)),255); d=ImageDraw.Draw(sheet)
for i,fid in enumerate(order):
    im=Image.open(f'{D}/fig_{fid}.png'); im.thumbnail((CELL-20,CELL-30))
    x=(i%COLS)*CELL; y=(i//COLS)*(CELL+34)
    sheet.paste(im,(x+(CELL-im.width)//2,y+24))
    d.rectangle([x+2,y+20,x+CELL-3,y+CELL+18],outline=0)
    d.text((x+8,y+4),f'fig_{fid}',fill=0)
out='scratch/ch18_figs/contact_sheet_4x.png'; sheet.save(out); print(out,sheet.size)
