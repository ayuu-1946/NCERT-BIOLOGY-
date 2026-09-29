import sys, os
from PIL import Image, ImageOps
src, dst = sys.argv[1], sys.argv[2]   # src dir of zip PNGs, dst = chapter assets/
for f in sorted(os.listdir(src)):
    if f.lower().endswith('.png'):
        im = ImageOps.autocontrast(Image.open(os.path.join(src, f)).convert('L'))
        im.save(os.path.join(dst, f.lower().replace('fig_', 'fig_')), dpi=(300, 300)); print(f, im.size)
