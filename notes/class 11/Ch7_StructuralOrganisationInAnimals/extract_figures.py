"""§4.4 figure extraction for Class 11 Chapter 7: Structural Organisation in Animals.

Source is the exact user-supplied 19-page NCERT chapter PDF, PDF pages 1–19
(printed pages 104–122; page size 612 x 785.4 PDF points). Its visible figure
census is Figures 7.1–7.8 and 7.14–7.22 (17 figures); this edition contains
no Figures 7.9–7.13. Rectangles were hand-pinned from the mandatory 440-DPI /
5-point source grids and cross-checked against source text, raster images, and
vector drawings. Printed captions are excluded. Every output is 300-DPI true
greyscale with autocontrast.
"""
import os
import pymupdf
from PIL import Image, ImageDraw, ImageOps

SRC = 'Chapter/class 11/Chapter 07 - Structural Organisation in Animals.pdf'
OUT_DIR = 'notes/class 11/Ch7_StructuralOrganisationInAnimals/assets'
CONTACT_SHEET = 'scratch/ch7_figs/contact_sheet.png'
RENDER_DPI = 300
FIGURE_DPI = {'7_3': 520}  # vector crop; higher density supports larger 300-dpi-effective placement

# (asset_id, 1-indexed source PDF page, (x0, y0, x1, y1) in PDF points)
FIGS = [
    # p2: all four simple-epithelium panels and labels; top begins below body
    # prose. The B-audit union reaches beyond this box because the pale diagonal
    # page watermark is many small vector paths; grid/PNG show it is not art.
    # Caption starts y=472.46; complete figure ends above this crop boundary.
    ('7_1', 2, (41, 293, 525, 471.7)),
    # p3: both glandular-epithelium panels and leader labels; keep the adjacent
    # body-text column to the right out; caption starts y=238.70.
    ('7_2', 3, (65, 98, 333, 235)),
    # p3: compound epithelium drawing plus the right-side multi-layered-cells
    # label; separate box from Fig 7.2; caption starts y=436.70.
    ('7_3', 3, (105, 323, 310, 425)),
    # p4: areolar/adipose panels; leftmost macrophage label begins near x=60;
    # right labels reach x=530.9; all content is above caption y=256.46.
    ('7_4', 4, (55, 90, 538, 253)),
    # p4: two dense-connective-tissue panels and collagen-fibre label;
    # caption begins y=674.78.
    ('7_5', 4, (350, 305, 542, 670)),
    # p5 Figure 7.6(a): cartilage art, (a), and both right-side leader labels;
    # x1 clears label text at x248.9 but avoids prose beginning at x264.
    ('7_6a', 5, (65, 85, 253, 211.3)),
    # p5 Figure 7.6(b): complete bone panel and (b), with clearance from (a)/(c).
    ('7_6b', 5, (78, 214, 177, 327)),
    # p5 Figure 7.6(c): RBC, WBC, platelets and (c); caption begins y=453.74.
    # B reports a path bbox 11.3 pt above y=328 from the RBC; the 600-dpi
    # clean source detail shows the visible silhouette starts below this edge.
    ('7_6c', 5, (92, 328, 231, 442)),
    # p6: skeletal, smooth and cardiac muscle panels; outer labels fit before
    # the caption at y=298.94.
    ('7_7', 6, (65, 100, 535, 294)),
    # p6: raster neuron micrograph and four leader labels; raster bbox is
    # x=332.2..533.6 / y=511.5..684.3; caption y=689.66.
    ('7_8', 6, (280, 505, 540, 687)),
    # p8: raster cockroach plus external labels; image bbox ends y=694.3;
    # caption begins y=700.22.
    ('7_14', 8, (175, 480, 540, 697)),
    # p9: head and mouthpart subfigures, all leaders/labels; caption y=701.66.
    ('7_15', 9, (60, 459, 555, 698)),
    # p10: right-column alimentary-canal art/labels; left edge follows the
    # neighboring prose column; caption y=371.42.
    ('7_16', 10, (295, 100, 538, 369)),
    # p10: open-circulatory-system art and outer labels; caption y=698.78.
    ('7_17', 10, (292, 382, 520, 695)),
    # p12 Figure 7.18(a): male body, all left/right labels and the (a) marker;
    # y1 clears the adjacent female panel, whose visible artwork starts y=327.44.
    # B's 12.5-pt overflow is the reciprocal colored-body path overlap described
    # for (b); clean source-grid review confirms the visible (a) panel is whole.
    ('7_18a', 12, (148, 80, 443, 326.5)),
    # p12 Figure 7.18(b): female system, leftmost label at x=102.87 and right
    # genital-pouch bracket/text ending x=486.04; caption begins y=540.86.
    # B's 12.5-pt top overflow is the reciprocal colored-body path overlap;
    # clean source-grid review confirms this crop excludes marker (a) and is whole.
    ('7_18b', 12, (98, 327, 492, 537)),
    # p13: frog artwork/labels; raster bbox ends y=592.3 and the caption starts
    # at y=598.46, so bottom margin is deliberately tight.
    ('7_19', 13, (70, 460, 285, 594)),
    # p14: complete frog internal-organ drawing with all leader labels;
    # caption starts y=435.74.
    ('7_20', 14, (88, 100, 530, 432)),
    # p16: male reproductive system; raster bbox ends y=327.1; caption y=331.34.
    ('7_21', 16, (305, 100, 540, 329.5)),
    # p16: female reproductive system; raster ends y=680.2, outer labels end
    # y=686.4, and caption begins y=697.10.
    ('7_22', 16, (298, 425, 540, 691)),
]


def extract():
    os.makedirs(OUT_DIR, exist_ok=True)
    os.makedirs(os.path.dirname(CONTACT_SHEET), exist_ok=True)
    doc = pymupdf.open(SRC)
    try:
        order = []
        for fid, pno, rect in FIGS:
            page = doc[pno - 1]
            clip = pymupdf.Rect(*rect) & page.rect
            render_dpi = FIGURE_DPI.get(fid, RENDER_DPI)
            pix = page.get_pixmap(clip=clip, dpi=render_dpi, alpha=False)
            img = ImageOps.autocontrast(
                Image.frombytes('RGB', (pix.width, pix.height), pix.samples).convert('L'),
                cutoff=1,
            )
            out = os.path.join(OUT_DIR, f'fig_{fid}.png')
            if fid in {'7_3', '7_6a', '7_6b', '7_6c', '7_18a', '7_18b'}:
                img.save(out, dpi=(render_dpi, render_dpi))
            else:
                img.save(out)
            order.append(fid)
            print(f'fig_{fid}: page={pno} rect={rect} size={img.size} mode={img.mode} -> {out}')

        # Side-by-side composites retain each panel's native 300-dpi pixel
        # size (no resampling); centre on the tallest panel and use a 24-px
        # white gutter. The individual letter-suffixed crops remain available.
        for base, suffixes in [('7_6', 'abc'), ('7_18', 'ab')]:
            panel_paths = [os.path.join(OUT_DIR, f'fig_{base}{suffix}.png') for suffix in suffixes]
            panels = [Image.open(path).convert('L') for path in panel_paths]
            gap = 24
            stack = Image.new('L', (sum(panel.width for panel in panels) + gap * (len(panels) - 1),
                                    max(panel.height for panel in panels)), 255)
            x = 0
            for panel in panels:
                y = (stack.height - panel.height) // 2
                stack.paste(panel, (x, y))
                x += panel.width + gap
            stack_path = os.path.join(OUT_DIR, f'fig_{base}.png')
            stack.save(stack_path, dpi=(RENDER_DPI, RENDER_DPI))
            order.append(base)
            letters = '-'.join(suffixes)
            print(f'fig_{base}: horizontal ({letters}), size={stack.size} mode={stack.mode} -> {stack_path}')

        cell, cols = 360, 4
        rows = (len(order) + cols - 1) // cols
        sheet = Image.new('L', (cols * cell, rows * (cell + 24)), 255)
        draw = ImageDraw.Draw(sheet)
        for i, fid in enumerate(order):
            im = Image.open(os.path.join(OUT_DIR, f'fig_{fid}.png'))
            im.thumbnail((cell - 10, cell - 10))
            cx, cy = (i % cols) * cell, (i // cols) * (cell + 24)
            sheet.paste(im, (cx + 5, cy + 18))
            draw.rectangle([cx + 1, cy + 16, cx + cell - 2, cy + cell + 16], outline=0)
            draw.text((cx + 6, cy + 3), f'fig_{fid}', fill=0)
        sheet.save(CONTACT_SHEET)
        print(f'contact sheet -> {CONTACT_SHEET} ({len(order)} assets)')
    finally:
        doc.close()


if __name__ == '__main__':
    extract()
