"""§4.4 figure extraction for Ch3 Reproductive Health (Class 12).

Rects are in PDF points. Source page is 568.8 x 777.6 pt (NCERT reprint 2026-27).

Page geometry notes (measured, not guessed):
  p4 text column starts at x = 238.3; the left figure column is x ~56-232.
  p4 captions: Fig 3.1(a) y 210.3-219.8, Fig 3.1(b) y 340.4-349.9, Fig 3.2 y 591.5-601.0
  p5 left text column ends at x = 330.5; caption Fig 3.3 y 218.3-227.8
  p5 captions: Fig 3.4(a) y 694.2-703.7 (x 79.0-201.1), Fig 3.4(b) y 699.2-708.7 (x 313.9-437.5)
  p5 page furniture: orange "45" tab, x 476.6-567.8 y ~605-670 (full-bleed page-edge tab)
  Both Fig 3.4 labels are TEXT-LAYER words, all other figures carry no in-figure text.
"""
import os
import sys

import pymupdf
from PIL import Image, ImageOps

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
SRC = os.path.join(REPO, "Chapter", "class 12", "Chapter 3 - Reproductive Health.pdf")
OUT_DIR = os.path.join(REPO, "notes", "class 12", "Ch3_ReproductiveHealth", "assets")
RENDER_DPI = 300

# (asset_id, 1-indexed artwork page, (x0, y0, x1, y1), why the rect is where it is)
FIGS = [
    ("3_1a", 4, (68, 158, 232, 204),
     "line-art condom: ink bbox (77.6,165.9)-(200.0,200.5) at thr 230; caption 3.1(a) at y=210.3; text column starts x=238.3"),
    ("3_1b", 4, (50, 236, 232, 337),
     "photo condom: ink bbox (56.5,241.0)-(225.7,332.7); caption 3.1(a) above ends y=219.8, caption 3.1(b) starts y=340.4; text column x>=238.3"),
    ("3_2", 4, (50, 375, 232, 585),
     "photo Copper T: ink bbox (56.2,379.2)-(225.4,578.9) at thr 230; caption Fig 3.2 at y=591.5; text column x>=238.3"),
    ("3_3", 5, (334, 79, 518, 213),
     "photo implants: ink bbox (342.3,83.2)-(512.2,207.0); left text column ends x=330.5; caption Fig 3.3 at y=218.3; BIOLOGY header ends y=67.6"),
    ("3_4a", 5, (36, 486, 252, 680),
     "vasectomy line-art + its text label: ink x 39.2-249.9 y 491.2-673.0; caption Fig 3.4(a) at y=694.2; empty seam runs x 249.9-269.6"),
    ("3_4b", 5, (264, 486, 490, 695),
     "tubectomy line-art + its text label: right ovary/fimbriae reach x=485.0 at y 496-540, so the "
     "right edge is 490; the orange '45' full-bleed page-number tab (x>=476.6, y 610-650) that this "
     "edge now includes is page furniture, not figure artwork, and is white-washed in place below "
     "(see TAB_WHITEOUT). tinted band y 694.9-699.1 (mean 248) and the caption strip from y=699.2 are excluded"),
]

# Page furniture that a rect has to include because real artwork reaches past it.
# fig_3_4b's right ovary reaches x=485 while NCERT's orange "45" page-number tab
# starts at x=476.6 - no rectangular crop can hold one without the other. The tab
# is page furniture (not figure artwork), so it is painted out after extraction and
# the removal is asserted below; nothing inside this box is figure ink.
TAB_WHITEOUT = {
    "3_4b": (476.6, 604.0, 490.0, 695.0),
}

# Unnumbered/decorative plates deliberately NOT extracted for this chapter:
#   p1 chapter-opening artwork (framed uterus-with-IUD illustration + QR code) -
#   adopted convention from the sibling chapter Ch2_HumanReproduction: chapter-opening
#   decorative plates are covered by the title-block motif and are not embedded as
#   figures. Recorded in the inventory Coverage note, not silently dropped.


def main():
    doc = pymupdf.open(SRC)
    os.makedirs(OUT_DIR, exist_ok=True)
    for fid, pno, rect, why in FIGS:
        page = doc[pno - 1]
        pix = page.get_pixmap(clip=pymupdf.Rect(*rect) & page.rect, dpi=RENDER_DPI, alpha=False)
        img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
        z = RENDER_DPI / 72.0
        if fid in TAB_WHITEOUT:
            bx0, by0, bx1, by1 = TAB_WHITEOUT[fid]
            # guard: nothing dark other than the orange tab may sit in this box
            inner = img.crop((int((bx0 - rect[0]) * z) + 1, int((by0 - rect[1]) * z) + 1,
                              int((bx1 - rect[0]) * z) - 1, int((by1 - rect[1]) * z) - 1))
            px = inner.convert("RGB").getdata()
            non_tab = sum(1 for r, g, b in px if not (r > 150 and b < 150 and r - b > 60) and (0.299 * r + 0.587 * g + 0.114 * b) < 200)
            print(f"          tab-whitout guard: {non_tab} non-tab dark px (must be 0) "
                  f"in {int(inner.width)}x{int(inner.height)}px box")
            assert non_tab == 0, f"fig_{fid}: TAB_WHITEOUT box contains unexpected artwork - fix the rect"
            img.paste((255, 255, 255), (int((bx0 - rect[0]) * z), int((by0 - rect[1]) * z),
                                        int((bx1 - rect[0]) * z), int((by1 - rect[1]) * z)))
        img = ImageOps.autocontrast(img.convert("L"), cutoff=1)
        out = os.path.join(OUT_DIR, f"fig_{fid}.png")
        img.save(out)
        print(f"fig_{fid}: p{pno} {rect} -> {img.size} mode={img.mode} {os.path.getsize(out)//1024} KB")
        print(f"          why: {why}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
