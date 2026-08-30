"""Figure extraction for NCERT Class 11 Chapter 16.
Rectangles are in PDF points, pinned from grid overlays and cross-checked against PDF geometry.
Captions are intentionally excluded because the chapter inventory carries caption text separately.
"""
import os
import sys
import pymupdf
from PIL import Image, ImageOps

SRC = 'Chapter/class 11/Chapter 16 - Excretory Products and their Elimination.pdf'
OUT_DIR = 'notes/class 11/Ch16_ExcretoryProductsAndTheirElimination/assets'
RENDER_DPI = 300

# (asset_id, 1-indexed PDF page, (x0, y0, x1, y1))
FIGS = [
    ('16_1', 2, (60, 385, 312, 638)),  # right edge stops before adjacent prose; bottom ends above caption baseline at y641.6 while retaining urethra label
    ('16_2', 3, (270, 100, 550, 315)),  # left boundary clears prose at x260.9 while retaining the Renal capsule label; top retains pyramid label
    ('16_3', 3, (50, 395, 480, 670)),  # drawings extent x60.8-433.5/y408.5-661.8; caption ~688
    ('16_4', 4, (108, 98, 312, 325)),  # top expanded to retain Afferent arteriole label; right edge stays before neighboring prose
    ('16_5', 6, (100, 100, 510, 498)),  # full green figure panel; caption starts ~499
    ('16_6', 7, (48, 280, 515, 689)),  # artwork extent x52.5-509.6/y285.2-688.3; caption ~691
]

def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    doc = pymupdf.open(SRC)
    try:
        for fid, pno, rect in FIGS:
            page = doc[pno - 1]
            clip = pymupdf.Rect(*rect) & page.rect
            pix = page.get_pixmap(clip=clip, dpi=RENDER_DPI, alpha=False)
            img = Image.frombytes('RGB', (pix.width, pix.height), pix.samples).convert('L')
            img = ImageOps.autocontrast(img, cutoff=1)
            out = os.path.join(OUT_DIR, f'fig_{fid}.png')
            img.save(out)
            print(f'fig_{fid}: page {pno} rect={rect} size={img.size} mode={img.mode} -> {out}')
    finally:
        doc.close()

if __name__ == '__main__':
    sys.exit(main())
