from pathlib import Path
from PIL import Image, ImageDraw
base=Path('notes/class 11/Ch11_PhotosynthesisInHigherPlants/assets')
files=sorted(base.glob('fig_*.png'))
W=520; H=390; cols=3; rows=(len(files)+cols-1)//cols
sheet=Image.new('RGB',(W*cols,H*rows),'#dddddd')
for i,p in enumerate(files):
    im=Image.open(p).convert('L'); im.thumbnail((W-20,H-45))
    card=Image.new('RGB',(W,H),'white'); card.paste(im,((W-im.width)//2,30))
    ImageDraw.Draw(card).text((10,8),p.stem,fill='black')
    sheet.paste(card,((i%cols)*W,(i//cols)*H))
sheet.save('scratch/ch11_figs/assets_contact_sheet.png')
print('created',len(files),'asset contact sheet')
