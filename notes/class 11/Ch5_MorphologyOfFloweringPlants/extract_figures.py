"""Hand-pinned NCERT figure extraction for Class 11 Chapter 5.

Rects are PDF points. Each crop uses a tight artwork box plus approximately
10 pt breathing room so labels, leader lines, brackets, and panel edges remain
visible without carrying neighboring prose or excessive white space.
"""
import os
import pymupdf
from PIL import Image, ImageOps

SRC = "Chapter/class 11/Chapter 05 - Morphology of Flowering Plants.pdf"
OUT_DIR = "notes/class 11/Ch5_MorphologyOfFloweringPlants/assets"
RENDER_DPI = 300

# Figure, 1-indexed PDF page, compact 10pt-padded rect.
FIGS = [
    ("5_1", 4, (78, 95, 315, 405)),    # p4: full flowering-plant diagram; left/right leader labels retained, caption excluded
    ("5_2", 4, (78, 420, 555, 665)),   # p4: all three root photographs and their (a)-(c) labels, caption excluded
    ("5_3", 5, (292, 120, 505, 325)),   # p5: root-tip diagram; right edge stops before prose column
    ("5_4", 6, (45, 95, 278, 435)),   # p6: labelled leaf parts and venation panels a-c
    ("5_5", 6, (48, 515, 282, 650)),  # p6: pinnate/palmate compound-leaf panels and labels
    ("5_6", 7, (275, 85, 505, 335)),   # p7: three phyllotaxy examples with labels
    ("5_7", 7, (275, 405, 515, 675)),   # p7: racemose inflorescence, including lower flower cluster and labels
    ("5_8", 8, (50, 95, 278, 245)),    # p8: cymose inflorescence diagram
    ("5_9", 8, (62, 480, 515, 660)),   # p8: four ovary-position panels with labels a-d
    ("5_10", 9, (42, 565, 510, 685)),  # p9: labelled parts of a flower
    ("5_11", 10, (125, 95, 475, 305)), # p10: four aestivation panels and labels a-d
    ("5_12", 11, (378, 85, 520, 735)),# p11: six placentation diagrams and labels
    ("5_13", 12, (188, 90, 505, 265)), # p12: mango/coconut fruit panels with labels
    ("5_14", 12, (48, 465, 285, 605)),# p12: dicotyledonous seed diagram and labels
    ("5_15", 13, (72, 90, 485, 345)),# p13: monocotyledonous seed diagram and labels
    ("5_16", 13, (335, 445, 515, 710)),# p13: floral diagram and formula; outer ring and labels retained
    ("5_17", 14, (102, 455, 475, 690)),# p14: Solanum nigrum twig, flower, fruit, and floral diagram
]

def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    doc = pymupdf.open(SRC)
    for fid, pno, rect in FIGS:
        page = doc[pno - 1]
        clip = pymupdf.Rect(*rect) & page.rect
        pix = page.get_pixmap(clip=clip, dpi=RENDER_DPI, alpha=False)
        img = ImageOps.autocontrast(
            Image.frombytes("RGB", (pix.width, pix.height), pix.samples).convert("L"), cutoff=1
        )
        out = os.path.join(OUT_DIR, f"fig_{fid}.png")
        img.save(out, dpi=(RENDER_DPI, RENDER_DPI), optimize=True)
        print(f"fig_{fid}: p{pno} rect={tuple(rect)} size={img.size} mode={img.mode} -> {out}")

if __name__ == "__main__":
    main()
