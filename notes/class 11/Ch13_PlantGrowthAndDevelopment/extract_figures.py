"""§4.4 figure extraction for Class 11 Chapter 13: Plant Growth and Development.

Rectangles are in PDF points, pinned from the mandatory 440 dpi / 5-point grid
and checked against page text and drawing geometry. Captions are excluded from
assets; captions are documented verbatim in the inventory. Outputs are true
monochrome PNGs with autocontrast. A compact ~10 pt outer margin is retained
where needed to preserve labels, leader lines, arrows, and outer artwork.
"""
import os
import sys
import pymupdf
from PIL import Image, ImageOps, ImageDraw

SRC = 'Chapter/class 11/Chapter 13 - Plant Growth and Development.pdf'
OUT_DIR = 'notes/class 11/Ch13_PlantGrowthAndDevelopment/assets'
RENDER_DPI = 300

# (asset_id, 1-indexed PDF page, (x0, y0, x1, y1))
FIGS = [
    # p2: full bean plate; lowest root artwork extends into the caption band, so y1=389 preserves all root tips and the caption is documented as an intentional overlap exception.
    ('13_1', 2, (55, 95, 515, 389)),
    # p3: upper left diagram; right edge stays inside the prose-column boundary.
    ('13_2', 3, (52, 94, 270, 377)),
    # p3: lower parallel-line diagram; includes A-G zone labels and leader lines.
    ('13_3', 3, (52, 515, 270, 660)),
    # p4: one multi-part figure (a), (b), and (c), including legend and phase labels.
    ('13_4', 4, (72, 300, 505, 670)),
    # p5: plot frame, axes, line, points, and axis labels; caption begins y367.8.
    ('13_5', 5, (45, 108, 270, 355)),
    # p5: complete sigmoid graph and labels; caption begins y663.9.
    ('13_6', 5, (82, 465, 270, 660)),
    # p6: complete two-leaf comparison; caption begins y310.4.
    ('13_7', 6, (105, 101, 520, 305)),
    # p8: upper flow diagram; caption begins y290.5.
    ('13_8', 8, (50, 78, 515, 285)),
    # p8: lower two-panel heterophylly plate; caption begins y700.4.
    ('13_9', 8, (90, 425, 490, 695)),
    # p9: all four coleoptile panels and light-direction arrows; caption begins y667.1.
    ('13_10', 9, (52, 525, 295, 660)),
    # p11: both apical-dominance treatments and central artwork; caption begins y290.3.
    ('13_11', 11, (52, 98, 305, 290)),
]

def extract():
    os.makedirs(OUT_DIR, exist_ok=True)
    doc = pymupdf.open(SRC)
    try:
        order = []
        for fid, pno, rect in FIGS:
            page = doc[pno - 1]
            clip = pymupdf.Rect(*rect) & page.rect
            pix = page.get_pixmap(clip=clip, dpi=RENDER_DPI, alpha=False)
            img = ImageOps.autocontrast(
                Image.frombytes('RGB', (pix.width, pix.height), pix.samples).convert('L'),
                cutoff=1,
            )
            out = os.path.join(OUT_DIR, f'fig_{fid}.png')
            img.save(out)
            order.append(fid)
            print(f'fig_{fid}: page {pno} rect={rect} size={img.size} mode={img.mode} -> {out}')
        cell, cols = 360, 4
        rows = (len(order) + cols - 1) // cols
        sheet = Image.new('L', (cols * cell, rows * (cell + 24)), 255)
        d = ImageDraw.Draw(sheet)
        for i, fid in enumerate(order):
            im = Image.open(os.path.join(OUT_DIR, f'fig_{fid}.png'))
            im.thumbnail((cell - 10, cell - 10))
            cx, cy = (i % cols) * cell, (i // cols) * (cell + 24)
            sheet.paste(im, (cx + 5, cy + 18))
            d.rectangle([cx + 1, cy + 16, cx + cell - 2, cy + cell + 16], outline=0)
            d.text((cx + 6, cy + 3), f'fig_{fid}', fill=0)
        sheet.save('scratch/ch13_figs/contact_sheet_v1.png')
    finally:
        doc.close()

if __name__ == '__main__':
    extract()
