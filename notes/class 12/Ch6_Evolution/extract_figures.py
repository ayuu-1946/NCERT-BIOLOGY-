"""4.4 figure extraction for Ch6 Evolution.
Rects are in PDF points (page is 612 x 820.8 -- measured from the source,
not the usual 612 x 792; every y value below is on that taller page).

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
    # p3: Miller's experiment apparatus. RE-PINNED (was 214,103,531,499).
    # The y1=499 pin was derived from a wrong row reading: the caption band is
    # NOT at y502-535, it is at y=362-390, and y1=499 therefore shipped the
    # caption PLUS the first five lines of body prose ("...lysaccharides, etc.).
    # These capsules reproduced..." at y404-497) inside the crop. Caught by eye
    # on the contact sheet, not by the numeric gate -- full-width prose lines
    # look exactly like figure ink to an extent probe.
    # Measured at 300 dpi: artwork ink x 229.3-514.9, y 106.0-356.1 (last row
    # is the "Liquid water in trap" label), then dead white y357-365, caption
    # band y~366-390, prose from y404. y1=359 splits artwork from caption;
    # x0/x1 also tightened from 214/531, which left ~15pt of dead margin
    # each side once the prose was gone.
    ("6_1", 3, (226, 102, 519, 359)),

    # p5: dinosaur family tree (NOTE: this is Figure 6.2, not 6.3 -- the
    # page-thumbnail reading was wrong; the printed caption says 6.2).
    # Full-width plate, no neighbouring prose. Ink 91.7-534.2 x 119.0-512.6.
    # Row profile: plate ink ends y=512, then y=513-545 is COMPLETELY blank
    # before the caption at y=555. An earlier y1=545 shipped 33pt of dead
    # whitespace, so y1=515 trims to the artwork. Edge-bands clean.
    ("6_2", 5, (89, 110, 540, 515)),

    # p6: homologous organs (a) Plants -- Bougainvillea (w/ Thorn) + Cucurbita
    # (w/ Tendril). Figure sits to the RIGHT of a prose column -- the classic
    # failure this skill exists to prevent. The figure is WIDE: it spans the
    # full text-block width, NOT just the right half. Prose ends x~260 with a
    # gutter at x=262-278; per-10pt column profile over the artwork rows shows
    # figure ink from x~280 (Bougainvillea stem/Thorn label) out to x~517
    # (Cucurbita). An earlier x0=392 pin sliced the entire Bougainvillea +
    # Thorn panel off, leaving only Cucurbita. x0=272 clears the gutter and
    # keeps both plants and the "(a)" label; y106-242 art + label below.
    ("6_3a", 6, (272, 103, 522, 278)),

    # p6: homologous organs (b) Animals -- Man/Cheetah/Whale/Bat + forelimbs.
    # Same wide span as 6_3a. Forelimb-row column profile shows FOUR ink
    # clusters: x280-320 (Man), x330-360 (Cheetah), x390-420 (Whale),
    # x450-505 (Bat). An earlier x0=392 pin cut off Man and Cheetah entirely,
    # leaving only Whale + Bat. x0=272 clears the prose gutter and keeps all
    # four animals and their forelimb skeletons. Row profile: "(b)" label at
    # y=552-560, caption band starts y=572, so y1=566 keeps the label and
    # drops the caption. Right edge to x=535 keeps the full Bat wing.
    ("6_3b", 6, (272, 288, 535, 566)),

    # p7: moth (a) unpolluted -- raster photo panel. Ink 78.2-308.2 x
    # 104.6-231.4 incl. the "(a)" label. Right band hit is panel (b) next
    # door (deliberately excluded); top band hit is page furniture.
    ("6_4a", 7, (76, 101, 310, 236)),

    # p7: moth (b) polluted. Column profile x520-570 shows photo ink through
    # x=548 then the decorative border band from x~551, so x1=550 stops just
    # inside it (first pin at 547 clipped the photo, and the reported R-band
    # ink was the band itself, not artwork). Left band hit is panel (a).
    # y1 RE-PINNED 236 -> 242: the "(b)" panel label sits at y=229-238,
    # x=431-441, so y1=236 sliced it in half. Only ~9 dark px/row, far under
    # the edge-band cluster threshold, so the numeric gate passed it clean --
    # caught by eye on the contact sheet. Panel (a)'s "(a)" label is y228-235
    # and was already inside its rect. Caption band starts y=249.
    ("6_4b", 7, (316, 101, 550, 242)),

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
    # x0 RE-PINNED 126 -> 120: the rounded frame's left arc bulges out to
    # x=123.0 at its mid-height (column profile: x123 carries ink y316-637,
    # x122 and left are empty), so x0=126 sliced a flat notch out of the
    # figure's own border. Surfaced only after BAND_TOL dropped 40 -> 12;
    # at 40 the 25px arc read as "clean".
    ("6_8", 11, (120, 268, 549, 686)),

    # p13: plant evolution through geological periods. Ink 78.7-546.7 x
    # 106.1-504.0 (era bar leftmost, "Angiosperms (flowering plants)"
    # rightmost). Caption at y=545. T band hit is page furniture.
    ("6_9", 13, (76, 102, 549, 508)),

    # p14: vertebrate evolutionary history. Ink 67.7-532.8 x 101.8-600.5
    # ("Quaternary" label leftmost, Mammals/Pelycosaurs art rightmost,
    # "Early reptiles (extinct)" lowest). Caption at y=615.
    # x0 RE-PINNED 65 -> 57: the era-axis label "Carboniferous" reaches
    # x=59.5-61.0 (it is the longest word in that column and outdents past the
    # others), so x0=65 shaved its leading "C" off -- visible on the contact
    # sheet as "arboniferous". Only ~55 dark px at 200 dpi in the 6pt left
    # band, under the cluster threshold, so the numeric gate passed it.
    # Measured ink at 300 dpi over x50-560: x 61.0-533.4, y 102.1-600.8;
    # nothing at all left of x=59, so x0=57 is safe margin.
    ("6_10", 14, (57, 99, 536, 604)),

    # p16: skull comparison. An earlier (148,98,478,518) pin clipped the middle
    # skull's occiput on the left (380px L-band hit) and left ~46pt of dead
    # space on the right. y0 re-pinned 96 -> 102: the row profile shows the
    # decorative top-right leaf/branch page furniture inking x=488-496 down to
    # y=97, so y0=96 pulled a sliver of it into the crop's corner (audit A'
    # read T slack 0.0, i.e. ink flush to the top edge). Real artwork -- the
    # top skull -- starts at y=106, so y0=102 clears the furniture with ~4pt
    # of margin; the furniture now sits in the T band and is declared in
    # audit_figures.py EXPLAINED.
    # x1 re-pinned 497 -> 435 in the same fix. The old rect comment claimed
    # ink ran to x=494.3, but that measurement had swallowed the same leaf
    # furniture; with the furniture excluded the column profile shows artwork
    # ending at x=431.7 and then dead white all the way to x=560. y0=102 is
    # what exposed this -- audit A' immediately reported R+65.5pt of wasted
    # margin. Measured artwork ink (200 dpi): x 139.0-431.7, y 106.3-513.1.
    ("6_11", 16, (136, 102, 435, 516)),
]


def main():
    doc = pymupdf.open(SRC)
    os.makedirs(OUT_DIR, exist_ok=True)
    for fid, pno, rect in FIGS:
        page = doc[pno - 1]
        pix = page.get_pixmap(clip=pymupdf.Rect(*rect) & page.rect, dpi=RENDER_DPI)
        # SUPREME §4.4 pipeline: clip-render -> convert("L") -> autocontrast.
        # The convert("L") is NOT optional and NOT cosmetic: the first version
        # of this script autocontrasted the RGB pixmap directly, so all 13
        # assets shipped mode=RGB. §4.4/§0.4 demand true monochrome (mode "L"),
        # and autocontrast on RGB stretches each channel independently, which
        # can shift hues rather than maximise ink contrast.
        img = ImageOps.autocontrast(
            Image.frombytes("RGB", (pix.width, pix.height), pix.samples).convert("L"),
            cutoff=1,
        )
        out = os.path.join(OUT_DIR, f"fig_{fid}.png")
        img.save(out)
        print(f"fig_{fid}: p{pno} {rect} {img.size} mode={img.mode} -> {out}")


if __name__ == "__main__":
    sys.exit(main())
