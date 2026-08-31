"""Extract Figures 6.1–6.5 from the NCERT Anatomy of Flowering Plants PDF.

All rectangles are PDF points. They were pinned from the mandatory 440 dpi / 5-point
page grids and cross-checked against visible artwork, labels, and caption positions.
The crops intentionally use about 10 pt of breathing room around the outermost
artwork/leader lines, but exclude captions and neighboring prose.
"""
import os
import sys
import pymupdf
from PIL import Image, ImageOps

SRC = "Chapter/class 11/Chapter 06 - Anatomy of Flowering Plants.pdf"
OUT_DIR = "notes/class 11/Ch6_AnatomyOfFloweringPlants/assets"
RENDER_DPI = 300

# (asset_id, 1-indexed artwork page, (x0, y0, x1, y1))
FIGS = [
    # p2: full two-panel stomata plate; x1 clears the right leader ends, y1 stops above caption.
    ("6_1", 2, (60, 337, 530, 448)),
    # p3: full three-part vascular-bundle plate; y1 includes (c) and stops above caption.
    ("6_2", 3, (320, 80, 520, 482)),
    # p4: both dicot and monocot root panels; x1 clears all label leaders, y1 stops above caption.
    ("6_3", 4, (75, 78, 320, 558)),
    # p5: all four images in the two-row stem plate; caption begins just below y=625.
    ("6_4", 5, (55, 235, 550, 700)),
    # p6: both leaf panels and labels; y1 includes lower (b) marker and stops above caption.
    ("6_5", 6, (55, 285, 320, 690)),
]


def main() -> int:
    os.makedirs(OUT_DIR, exist_ok=True)
    try:
        doc = pymupdf.open(SRC)
    except Exception as exc:
        print(f"ERROR opening source PDF: {exc}", file=sys.stderr)
        return 2
    for fid, pno, rect_tuple in FIGS:
        try:
            page = doc[pno - 1]
            rect = pymupdf.Rect(*rect_tuple) & page.rect
            if rect.is_empty:
                raise ValueError(f"empty clipped rectangle {rect_tuple}")
            pix = page.get_pixmap(clip=rect, dpi=RENDER_DPI, alpha=False)
            img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples).convert("L")
            img = ImageOps.autocontrast(img, cutoff=1)
            out = os.path.join(OUT_DIR, f"fig_{fid}.png")
            img.save(out, format="PNG", optimize=True)
            print(f"fig_{fid}: p{pno} rect={rect_tuple} size={img.size} mode={img.mode} -> {out}")
        except Exception as exc:
            print(f"ERROR fig_{fid}: {exc}", file=sys.stderr)
            return 3
    return 0


if __name__ == "__main__":
    sys.exit(main())
