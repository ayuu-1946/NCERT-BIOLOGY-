from pathlib import Path
from PIL import Image, ImageDraw
base=Path('notes/class 11/Ch11_PhotosynthesisInHigherPlants/assets')
files=[base/'fig_11_3a.png',base/'fig_11_3b.png',base/'fig_11_5.png']
W=700; H=500
sheet=Image.new('RGB',(W*3,H),'#dddddd')
for i,p in enumerate(files):
    im=Image.open(p).convert('L'); im.thumbnail((W-20,H-45))
    card=Image.new('RGB',(W,H),'white'); card.paste(im,((W-im.width)//2,30))
    ImageDraw.Draw(card).text((10,8),p.stem,fill='black')
    sheet.paste(card,(i*W,0))
sheet.save('notes/class 11/Ch11_PhotosynthesisInHigherPlants/review/target_contact_sheet.png')
