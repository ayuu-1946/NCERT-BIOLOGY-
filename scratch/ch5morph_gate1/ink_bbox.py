"""Watermark-robust ink bounding boxes for Ch5 figure pinning.

The naive approach -- union of `page.get_drawings()` rects -- is unreliable on
these NCERT pages: the diagonal "not to be republished" watermark and the (c)
mark are themselves vector artwork spanning most of the page, so the union
reports a figure as far wider than it is. (This produced a Fig 5.14 crop that
bled the neighbouring prose column, and a Fig 5.12 crop 40 pt too wide.)

Instead, render the page and measure *dark* ink. The watermark renders around
grey 230-245, page furniture tints lighter still, while figure outlines and
label text sit below 215. Thresholding therefore separates real artwork from
the watermark, and the reported bbox is in PDF points.
"""
import sys

import pymupdf
from PIL import Image

SRC = "Chapter/class 11/Chapter 05 - Morphology of Flowering Plants.pdf"
DPI = 200


def ink_bbox(page_no: int, band: tuple[float, float, float, float], threshold: int = 215):
    """Bbox of pixels darker than `threshold` inside `band`, in PDF points."""
    doc = pymupdf.open(SRC)
    page = doc[page_no - 1]
    scale = DPI / 72.0
    x0, y0, x1, y1 = band
    pix = page.get_pixmap(clip=pymupdf.Rect(x0, y0, x1, y1), dpi=DPI, alpha=False)
    img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples).convert("L")
    mask = img.point(lambda v: 255 if v < threshold else 0, mode="L")
    box = mask.getbbox()
    if box is None:
        return None
    return (
        round(x0 + box[0] / scale, 1),
        round(y0 + box[1] / scale, 1),
        round(x0 + box[2] / scale, 1),
        round(y0 + box[3] / scale, 1),
    )


if __name__ == "__main__":
    pno = int(sys.argv[1])
    band = tuple(float(v) for v in sys.argv[2:6])
    thr = int(sys.argv[6]) if len(sys.argv) > 6 else 215
    print(f"p{pno} band={band} thr={thr} -> ink bbox {ink_bbox(pno, band, thr)}")
