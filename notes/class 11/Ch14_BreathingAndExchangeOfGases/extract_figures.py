"""§4.4 figure extraction for Ch14 Breathing and Exchange of Gases.

Rectangles are in PDF points, pinned from the 4× grid overlays and cross-checked
against the source page's drawing and text-layer geometry. Captions are excluded;
the inventory carries the verbatim caption text separately. Every output is true
monochrome (L) with autocontrast.
"""
import os
import sys
import pymupdf
from PIL import Image, ImageOps

SRC = 'Chapter/class 11/Chapter 14 - Breathing and Exchange of Gases.pdf'
OUT_DIR = 'notes/class 11/Ch14_BreathingAndExchangeOfGases/assets'
RENDER_DPI = 300

# (asset_id, 1-indexed PDF page, (x0, y0, x1, y1))
FIGS = [
    # p4: diagram and all leader-line labels; caption begins at y685.8 and is excluded.
    ('14_1', 4, (105, 414, 530, 675)),
    # p6 upper panel: top boundary begins below the running header; lower boundary ends above panel (b).
    ('14_2a', 6, (52, 96, 296, 315)),
    # p6 lower panel: includes the full expiration panel and its in-figure labels, not the shared caption.
    ('14_2b', 6, (52, 330, 296, 562)),
    # p8: full gas-exchange circulation diagram; caption begins at y412.4 and is excluded.
    ('14_3', 8, (82, 86, 510, 408)),
    # p8: artwork ends before caption words at y666.3; y1=660 excludes caption while retaining all meaningful diagram labels; a small lower vector tail is documented in the audit note.
    ('14_4', 8, (52, 510, 318, 660)),
    # p9: graph frame, axes, curve, tick labels, and axis titles; caption begins at y585.5.
    ('14_5', 9, (292, 358, 507, 579)),
]

def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    doc = pymupdf.open(SRC)
    try:
        for fid, pno, rect in FIGS:
            page = doc[pno - 1]
            clip = pymupdf.Rect(*rect) & page.rect
            pix = page.get_pixmap(clip=clip, dpi=RENDER_DPI, alpha=False)
            img = ImageOps.autocontrast(Image.frombytes('RGB', (pix.width, pix.height), pix.samples).convert('L'), cutoff=1)
            out = os.path.join(OUT_DIR, f'fig_{fid}.png')
            img.save(out)
            print(f'fig_{fid}: page {pno} rect={rect} size={img.size} mode={img.mode} -> {out}')
    finally:
        doc.close()

if __name__ == '__main__':
    sys.exit(main())
