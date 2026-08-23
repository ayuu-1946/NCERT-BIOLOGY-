"""4.4 figure extraction for Ch6 Evolution.
Rects are in PDF points (page is 612 x 792).

IMPORTANT -- this chapter's PDF is 100% SCANNED RASTER. Every page is a single
full-page image: page.get_text("words") returns [] and page.get_drawings()
returns [] on all 17 pages. That means the skill's audit checks A (text-layer
word grazing) and B (drawings-extent overflow) are BOTH inert here:
  - A would report words_in_rect=0 for every figure -> a vacuous pass.
  - B would report "no drawings (raster figure)" for every figure.
So the numeric gate for this chapter is raster-ink based instead
(see audit_figures.py): ink-extent slack inside the rect + an edge-band probe
just outside it. Do not "restore" checks A/B here; they cannot work on a
scanned PDF.

Captions are EXCLUDED (Ch5 convention -- notes rewrite captions in text).
Sub-figures get separate rects/assets (skill rule).
"""
import os
import sys

import pymupdf
from PIL import Image, ImageOps

SRC = "Chapter/class 12/Chapter 6 - Evolution.pdf"
OUT_DIR = "notes/class 12/Ch6_Evolution/assets"
RENDER_DPI = 300

# (asset_id, 1-indexed artwork page, (x0, y0, x1, y1))
FIGS = [
    # p3: Miller's experiment apparatus. Artwork's last row is the
    # "Liquid water in trap" label; row profile shows artwork ink ending
    # y=497 and the caption band running y=502-535, so y1=499 splits them.
    # First pin had y1=548 and swallowed the caption PLUS 7 lines of body
    # prose and the "6.2 Evolution of Life Forms" heading.
    ("6_1", 3, (214, 103, 531, 499)),

    # p5: dinosaur family tree (NOTE: this is Figure 6.2, not 6.3 -- the
    # page-thumbnail reading was wrong; the printed caption says 6.2).
    # Full-width plate, no neighbouring prose. Ink 91.7-534.2 x 119.0-512.6.
    # Row profile: plate ink ends y=512, then y=513-545 is COMPLETELY blank
    # before the caption at y=555. An earlier y1=545 shipped 33pt of dead
    # whitespace, so y1=515 trims to the artwork. Edge-bands clean.
    ("6_2", 5, (89, 110, 540, 515)),

    # p6: homologous organs (a) Plants. Figure sits to the RIGHT of a prose
    # column -- the classic failure this skill exists to prevent. Column
    # profile over y100-280 shows a zero-ink gutter at x=377-389, so prose
    # ends x~373 and figure ink starts x=393. Ink 394.9-517.3 x 106.2-272.2;
    # x0=392 keeps the Bougainvillea stem and the "(a)" label, which an
    # earlier x0=415 pin sliced off.
    ("6_3a", 6, (392, 103, 522, 278)),

    # p6: homologous organs (b) Animals -- Man/Cheetah/Whale/Bat + forelimbs.
    # Same gutter as 6_3a on the left. Row profile: "(b)" label at y=552-560,
    # caption band starts y=572, so y1=566 keeps the label and drops the
    # caption. Ink 394.9-530.3 x 296.3-(579.6 incl. caption).
    ("6_3b", 6, (392, 288, 535, 566)),

    # p7: moth (a) unpolluted -- raster photo panel. Ink 78.2-308.2 x
    # 104.6-231.4 incl. the "(a)" label. Right band hit is panel (b) next
    # door (deliberately excluded); top band hit is page furniture.
    ("6_4a", 7, (76, 101, 310, 236)),

    # p7: moth (b) polluted. Column profile x520-570 shows photo ink through
    # x=548 then the decorative border band from x~551, so x1=550 stops just
    # inside it (first pin at 547 clipped the photo, and the reported R-band
    # ink was the band itself, not artwork). Left band hit is panel (a).
    ("6_4b", 7, (316, 101, 550, 236)),

    # p8: finch beaks. Ink 102.7-498.7 x 105.1-183.8 incl. numerals 1-4.
    # Left band hit is the "EVOLUTION" running header, top is page furniture.
    ("6_5", 8, (100, 101, 502, 188)),

    # p8: marsupial adaptive radiation. Ink 69.1-500.2 x 397.0-707.5;
    # "Marsupial rat" label is the right-most element, "Wombat" the lowest.
    # Edge-band probe clean on all four sides.
    ("6_6", 8, (65, 392, 504, 710)),

    # p9: convergent evolution table, bordered box in the LEFT column with
    # prose starting x~320. Table border ink 78.2-305.3 x 104.2-547.2
    # (incl. the "Placental mammals / Australian marsupials" header row).
    # T band hit = leaf page furniture, B band hit = caption. Both excluded.
    ("6_7", 9, (76, 100, 308, 550)),

    # p11: natural-selection panel (a)/(b)/(c) kept as ONE asset -- the three
    # sub-panels share a single rounded frame and the arrows between them
    # carry the meaning, so splitting would destroy the figure.
    # Rounded frame + y-axis label ink 127.7-547.2 x 270.2-683.0.
    # R band hit is the page-number tab outside the frame (excluded).
    ("6_8", 11, (126, 268, 549, 686)),

    # p13: plant evolution through geological periods. Ink 78.7-546.7 x
    # 106.1-504.0 (era bar leftmost, "Angiosperms (flowering plants)"
    # rightmost). Caption at y=545. T band hit is page furniture.
    ("6_9", 13, (76, 102, 549, 508)),

    # p14: vertebrate evolutionary history. Ink 67.7-532.8 x 101.8-600.5
    # ("Quaternary" label leftmost, Mammals/Pelycosaurs art rightmost,
    # "Early reptiles (extinct)" lowest). Caption at y=615.
    ("6_10", 14, (65, 99, 536, 604)),

    # p16: skull comparison. True ink 139.0-494.3 x 94.7-513.0. An earlier
    # (148,98,478,518) pin clipped the middle skull's occiput on the left
    # (380px L-band hit) and left ~46pt of dead space on the right.
    ("6_11", 16, (136, 96, 497, 516)),
]


def main():
    doc = pymupdf.open(SRC)
    os.makedirs(OUT_DIR, exist_ok=True)
    for fid, pno, rect in FIGS:
        page = doc[pno - 1]
        pix = page.get_pixmap(clip=pymupdf.Rect(*rect) & page.rect, dpi=RENDER_DPI)
        img = ImageOps.autocontrast(
            Image.frombytes("RGB", (pix.width, pix.height), pix.samples), cutoff=1
        )
        out = os.path.join(OUT_DIR, f"fig_{fid}.png")
        img.save(out)
        print(f"fig_{fid}: p{pno} {rect} {img.size} mode={img.mode} -> {out}")


if __name__ == "__main__":
    sys.exit(main())
