"""Extract the 7 NCERT figures of Class 12 Chapter 12 (Ecosystem) per SS4.4.

Pipeline per figure: clip-render at 300 dpi -> RGB -> convert("L") -> autocontrast
-> trim surrounding white -> save single-channel PNG into assets/.

Clips are set GENEROUSLY (a little slack on every side) and then trimmed
programmatically, so a few points of drift in the hand-measured box cannot
decapitate a label. Every clip stops ABOVE the printed caption: captions are
re-typeset by the template via figure(), never baked into the image, and never
cropped in half.

The NCERT source is in colour; colour carries meaning in Fig 12.4 (each trophic
level's bar is a different hue), so the trophic labels (P / PC / SC / TC) and the
printed values are what must stay legible after greyscale conversion. Each clip is
asserted to carry real chroma before conversion, so a mis-measured clip that
grabbed blank paper cannot silently pass.
"""
import os

import pymupdf
from PIL import Image as PILImage, ImageChops, ImageOps

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = HERE
while not os.path.exists(os.path.join(ROOT, "neet_template.py")):
    ROOT = os.path.dirname(ROOT)

SRC = os.path.join(ROOT, "Chapter", "class 12", "Chapter 12 - Ecosystem.pdf")
ASSETS = os.path.join(HERE, "assets")
os.makedirs(ASSETS, exist_ok=True)

DPI = 300

# (asset name, 0-based page index, clip rect in PDF points, human label)
#
# Clip bounds were re-measured against pymupdf page geometry (568.8 x 777.6 pt),
# using each figure's caption text block as the hard lower anchor:
#   12.1 caption y=478.8 | 12.2 y=693.6 | 12.3 y=608.4
#   12.4a y=352.1 | 12.4b y=562.8 | 12.4c y=679.0 | 12.4d y=261.6
#
# Three clips were corrected after visual inspection of the extracted assets:
#   * 12.1 and 12.3 previously started ABOVE the figure box's decorative
#     coloured header strip (12.1: y 84.8-97.7; 12.3: y 318.0-332.0), baking a
#     dead grey band into the asset. The template's own figure() border is the
#     only frame the output should carry (SS4.4), so both now start below it.
#   * 12.3 previously ended at y=598, 8 pt short of the artwork's true bottom
#     edge at y=606 - a genuine bottom crop.
#   * 12.4d previously used x1=600, which is PAST the 568.8 pt page edge, so the
#     clip was clamped to the page and swallowed NCERT's decorative corner logo
#     (x>440, y<75) as a stray smudge. Artwork really ends at x=379.
FIGURES = [
    ("fig_12_1.png",  3, (57, 98, 532, 472), "Figure 12.1 decomposition cycle"),
    ("fig_12_2.png",  5, (100, 386, 535, 682), "Figure 12.2 trophic levels"),
    ("fig_12_3.png",  6, (36, 332, 517, 607), "Figure 12.3 energy flow"),
    ("fig_12_4a.png", 7, (92, 172, 508, 348), "Figure 12.4 (a) pyramid of numbers"),
    ("fig_12_4b.png", 7, (92, 382, 508, 558), "Figure 12.4 (b) pyramid of biomass"),
    ("fig_12_4c.png", 7, (195, 592, 425, 662), "Figure 12.4 (c) inverted pyramid of biomass"),
    ("fig_12_4d.png", 8, (100, 80, 395, 253), "Figure 12.4 (d) pyramid of energy"),
]


def chroma_of(img_rgb):
    """Max per-pixel channel spread - proves the clip really carries colour."""
    r, g, b = img_rgb.split()
    return max(
        ImageChops.difference(r, g).getextrema()[1],
        ImageChops.difference(g, b).getextrema()[1],
        ImageChops.difference(r, b).getextrema()[1],
    )


def trim_white(img_l, pad=10, thresh=246):
    """Trim uniform near-white margin, then re-pad so nothing touches the border."""
    mask = img_l.point(lambda p: 0 if p >= thresh else 255)
    box = mask.getbbox()
    if box is None:
        return img_l
    x0, y0, x1, y1 = box
    x0 = max(0, x0 - pad)
    y0 = max(0, y0 - pad)
    x1 = min(img_l.width, x1 + pad)
    y1 = min(img_l.height, y1 + pad)
    return img_l.crop((x0, y0, x1, y1))


def main():
    doc = pymupdf.open(SRC)
    for name, page_index, clip, label in FIGURES:
        page = doc[page_index]

        # A clip that runs past the page edge is silently CLAMPED by pymupdf, so
        # it quietly grabs whatever furniture sits in the margin (this is exactly
        # how 12.4d picked up the decorative corner logo). Fail loudly instead.
        rect = pymupdf.Rect(*clip)
        assert rect in page.rect, (
            "%s: clip %s escapes page rect %s - it would be clamped and pull in "
            "page furniture" % (name, rect, page.rect))

        pix = page.get_pixmap(dpi=DPI, clip=rect)
        raw_path = os.path.join(ASSETS, "_raw_" + name)
        pix.save(raw_path)

        colour = PILImage.open(raw_path).convert("RGB")
        chroma = chroma_of(colour)
        assert chroma > 0, "%s: clip carries no colour - clip is probably blank paper" % name

        mono = trim_white(ImageOps.autocontrast(colour.convert("L")))
        out_path = os.path.join(ASSETS, name)
        mono.save(out_path)
        os.remove(raw_path)

        check = PILImage.open(out_path)
        assert check.mode == "L", "%s is not single-channel greyscale" % name
        print("%-16s p%-2d chroma=%-4d %-5s %sx%s  %s"
              % (name, page_index + 1, chroma, check.mode, check.width, check.height, label))
    doc.close()
    print("\n%d figures written to %s" % (len(FIGURES), ASSETS))


if __name__ == "__main__":
    main()
