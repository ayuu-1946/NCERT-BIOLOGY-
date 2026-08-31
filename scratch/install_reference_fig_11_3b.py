from pathlib import Path
from PIL import Image

src = Path('/home/ubuntu/upload/1000107125.jpg')
out = Path('notes/class 11/Ch11_PhotosynthesisInHigherPlants/assets/fig_11_3b.png')
if not src.exists():
    raise FileNotFoundError(src)
im = Image.open(src)
# Preserve the user-supplied reference appearance and dimensions exactly; only change container format.
im.save(out, format='PNG', optimize=True)
print(f'{out}: size={im.size} mode={im.mode} source={src}')
