"""Figure extraction for NCERT Class 12 Ch11 - Organisms and Populations.

Pass 1, step 4 of SUPREME COMMAND PROMPT v6 (§4.4):
  clip-render at 300 dpi -> convert("L") -> autocontrast -> save to assets/.
Only the converted monochrome file is ever embedded in the notes PDF.
"""

import os
import sys

import pymupdf
from PIL import Image, ImageOps

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "assets")
SRC = os.path.abspath(
    os.path.join(HERE, "..", "..", "..", "Chapter", "class 12",
                 "Chapter 11 - Organisms and Populations.pdf")
)

# (asset name, 1-based source page, clip rect in PDF points)
FIGURES = [
    ("fig_11_1.png", 5, (98, 80, 531, 168)),
    ("fig_11_2.png", 6, (38, 254, 510, 531)),
    ("fig_11_3.png", 7, (53, 360, 271, 523)),
    ("fig_11_4a.png", 14, (38, 374, 215, 540)),
    ("fig_11_4b.png", 14, (216, 374, 476, 540)),
    ("fig_11_5.png", 15, (56, 334, 246, 538)),
]


def main():
    if not os.path.exists(SRC):
        raise SystemExit("SETUP ERROR: source PDF not found: %s" % SRC)
    os.makedirs(ASSETS, exist_ok=True)
    doc = pymupdf.open(SRC)
    for name, pageno, box in FIGURES:
        page = doc[pageno - 1]
        rect = pymupdf.Rect(*box)
        pix = page.get_pixmap(clip=rect, dpi=300)
        raw = os.path.join(ASSETS, "_raw_" + name)
        pix.save(raw)
        img = Image.open(raw).convert("L")          # true greyscale, one channel
        img = ImageOps.autocontrast(img, cutoff=1)  # recover contrast lost with hue
        out = os.path.join(ASSETS, name)
        img.save(out)
        os.remove(raw)
        chk = Image.open(out)
        print("%-16s page %2d  %4dx%-4d  mode=%s" % (name, pageno, chk.width, chk.height, chk.mode))
        if chk.mode != "L":
            print("  FAIL: not single-channel greyscale", file=sys.stderr)
    doc.close()


if __name__ == "__main__":
    main()
