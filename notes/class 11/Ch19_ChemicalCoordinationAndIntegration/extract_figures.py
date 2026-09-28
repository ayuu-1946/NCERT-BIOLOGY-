"""§4.4 figure extraction for Ch19 Chemical Coordination and Integration.
Rects are in PDF points on pages 571.68 x 780.48. They were hand-pinned from
440-dpi 5-point grid overlays and cross-checked against source geometry.
Captions and neighboring prose are excluded; subfigures are separate assets.
"""
import os
import sys
import pymupdf
from PIL import Image, ImageOps

SRC = "Chapter/class 11/Chapter 19 - Chemical Coordination and Integration.pdf"
OUT_DIR = "notes/class 11/Ch19_ChemicalCoordinationAndIntegration/assets"
RENDER_DPI = 440

FIGS = [
    # p2: endocrine-gland location plate; widened to preserve every left/right\n    # label, with the neighboring prose column beginning beyond the right edge.
    ("19_1", 2, (45, 110, 325, 442)),
    # p3: pituitary/hypothalamus plate; widened on both sides to preserve\n    # anterior/posterior pituitary and hypothalamic/portal-circulation labels.
    ("19_2", 3, (285, 80, 525, 365)),
    # p4: thyroid ventral subfigure; upper artwork occupies x=58..264 y=209..421.
    ("19_3a", 4, (50, 202, 255, 428)),
    # p4: thyroid dorsal/parathyroid subfigure; lower artwork occupies x=58..264 y=433..642.
    ("19_3b", 4, (50, 425, 263, 648)),
    # p6: the two adrenal subfigures are interleaved horizontally; a single
    # combined crop preserves both complete panels, labels, and connector.
    ("19_4", 6, (135, 235, 520, 518)),
    # p10: protein-hormone mechanism panel (a), cropped to the existing box border.
    ("19_5a", 10, (74, 370, 531, 624)),
    # p11: steroid-hormone mechanism panel (b), cropped to the existing box border.
    ("19_5b", 11, (39, 87, 483, 421)),
]

def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    doc = pymupdf.open(SRC)
    saved = {}
    for fid, pno, rect in FIGS:
        page = doc[pno - 1]
        clip = pymupdf.Rect(*rect) & page.rect
        pix = page.get_pixmap(clip=clip, dpi=RENDER_DPI, alpha=False)
        img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples).convert("L")
        img = ImageOps.autocontrast(img, cutoff=1)
        out = os.path.join(OUT_DIR, f"fig_{fid}.png")
        img.save(out, optimize=True)
        saved[fid] = img
        print(f"fig_{fid}: p{pno} {rect} {img.size} mode={img.mode} -> {out}")

    # Generate horizontally merged fig_19_3.png
    if "19_3a" in saved and "19_3b" in saved:
        img_a = saved["19_3a"]
        img_b = saved["19_3b"]
        gap_px = 60
        total_w = img_a.width + gap_px + img_b.width
        total_h = max(img_a.height, img_b.height)
        merged = Image.new("L", (total_w, total_h), 255)
        y_a = (total_h - img_a.height) // 2
        y_b = (total_h - img_b.height) // 2
        merged.paste(img_a, (0, y_a))
        merged.paste(img_b, (img_a.width + gap_px, y_b))
        out_3 = os.path.join(OUT_DIR, "fig_19_3.png")
        merged.save(out_3, optimize=True)
        print(f"fig_19_3 (merged a+b): {merged.size} mode={merged.mode} -> {out_3}")

if __name__ == "__main__":
    sys.exit(main())
