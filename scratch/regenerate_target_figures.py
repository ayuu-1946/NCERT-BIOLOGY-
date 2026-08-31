import os
import importlib.util
import pymupdf
from PIL import Image, ImageOps

BASE = os.path.dirname(os.path.dirname(__file__))
script_path = os.path.join(BASE, 'notes/class 11/Ch11_PhotosynthesisInHigherPlants/Ch11_PhotosynthesisInHigherPlants_extract_figures.py')
spec = importlib.util.spec_from_file_location('extractor', script_path)
extractor = importlib.util.module_from_spec(spec)
spec.loader.exec_module(extractor)

targets = {'11_3a', '11_3b', '11_5'}
doc = pymupdf.open(os.path.join(BASE, extractor.SRC))
out_dir = os.path.join(BASE, extractor.OUT_DIR)
os.makedirs(out_dir, exist_ok=True)
for fid, pno, rect in extractor.FIGS:
    if fid not in targets:
        continue
    page = doc[pno - 1]
    pix = page.get_pixmap(clip=pymupdf.Rect(*rect) & page.rect, dpi=extractor.RENDER_DPI, alpha=False)
    img = ImageOps.autocontrast(Image.frombytes('RGB', (pix.width, pix.height), pix.samples).convert('L'), cutoff=1)
    out = os.path.join(out_dir, f'fig_{fid}.png')
    img.save(out, optimize=True)
    print(f'fig_{fid}: p{pno} {rect} {img.size} mode={img.mode} -> {out}')
