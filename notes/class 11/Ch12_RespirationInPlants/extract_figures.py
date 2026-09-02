"""§4.4 figure extraction for Class 11 NCERT Chapter 12: Respiration in Plants.

Rectangles are in PDF points. They were pinned from mandatory 440-dpi/5-point
source grids, then cross-checked against raster color bounds, drawing extents,
and caption word coordinates. Captions are excluded; the inventory carries them.
A 6-point perimeter is used wherever possible so the assets are tight rather
than surrounded by excessive white space, while all labels and leader lines
remain visible. Every output is true grayscale with autocontrast.
"""
import os
import sys
import pymupdf
from PIL import Image, ImageOps

SRC = 'Chapter/class 11/Chapter 12 - Respiration in Plants.pdf'
OUT_DIR = 'notes/class 11/Ch12_RespirationInPlants/assets'
RENDER_DPI = 300

# Per-figure render DPI override. RENDER_DPI (300) is the default and is what
# every figure that renders AT OR BELOW its 300 dpi natural width needs. A figure
# that is deliberately displayed WIDER than its 300 dpi natural width needs more
# source pixels, or neet_template.figure()'s no-upscale cap silently pins it back
# to the natural width and the requested enlargement does nothing at all.
#
# fig_12_2 is the one such case (operator instruction, this revision: it is
# enlarged to fill the space freed by moving 12.4 to its own page). Raising its
# render DPI is honest here rather than cosmetic because 169 vector drawings and
# ZERO text/raster-only labels sit inside its crop - all of its labels, arrows and
# leader lines are vector artwork, so they re-render genuinely sharper at a higher
# DPI. Only the flat colour panel behind them comes from the page's 294 dpi
# raster; it is greyscaled anyway and carries no fine detail. Numbers: §2 of
# figure_layout_decisions.md.
FIG_DPI = {"12_2": 440}

# (asset_id, 1-indexed PDF page, (x0, y0, x1, y1))
FIGS = [
    # p4: raster green glycolysis panel bbox≈(60.6,154.9)-(293.0,577.3);
    # The artwork panel ends near x293; x1=296 leaves a small safety margin while
    # excluding the neighboring prose column. y1=584 stops before the caption.
    ('12_1', 4, (54, 149, 296, 584)),
    # p5: raster yellow panel bbox≈(281.6,396.0)-(513.4,642.7); 6pt padding
    # retains both fermentation branches and all NAD labels; caption starts y652.7.
    ('12_2', 5, (275, 389, 520, 648)),
    # p7: drawing/text-label union reaches x279.6..509.1, y103.2..321.7;
    # 6pt padding retains outer Pyruvate/CoA and right NADH+H+ labels; caption y346.9.
    ('12_3', 7, (274, 97, 516, 328)),
    # p8: full bordered diagram, not only the saturated inner artwork. Border and
    # headings span≈(57,83)-(321,539); 4-6pt padding retains all leader labels;
    # caption starts y545.2.
    ('12_4', 8, (51, 77, 327, 541)),
    # p9: colored artwork bbox≈(331.4,130.6)-(449.5,296.2), but labels/arrows
    # extend left/right to≈289..466; this tight box keeps all labels and ends before caption y303.7.
    ('12_5', 9, (283, 124, 472, 299)),
    # p11: drawing union≈(47.2,102.4)-(506.2,456.3); 6pt padding retains the
    # full metabolic-pathway panel and its outer edges, stopping before caption y468.3.
    ('12_6', 11, (41, 96, 512, 462)),
]


def main() -> int:
    os.makedirs(OUT_DIR, exist_ok=True)
    doc = pymupdf.open(SRC)
    try:
        for fid, pno, rect in FIGS:
            page = doc[pno - 1]
            clip = pymupdf.Rect(*rect) & page.rect
            dpi = FIG_DPI.get(fid, RENDER_DPI)
            pix = page.get_pixmap(clip=clip, dpi=dpi, alpha=False)
            img = ImageOps.autocontrast(
                Image.frombytes('RGB', (pix.width, pix.height), pix.samples).convert('L'),
                cutoff=1,
            )
            out = os.path.join(OUT_DIR, f'fig_{fid}.png')
            img.save(out, optimize=True)
            print(f'fig_{fid}: page={pno} rect={rect} dpi={dpi} '
                  f'size={img.size} mode={img.mode} -> {out}')
    finally:
        doc.close()
    return 0


if __name__ == '__main__':
    sys.exit(main())
