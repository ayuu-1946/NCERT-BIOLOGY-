"""Animal Kingdom (Class 11) figure extraction, §4.4.

Every rectangle is in source-PDF points. Rectangles are intentionally tight: they include
all artwork, leader lines, in-figure labels, and subfigure markers, with about 8–12 pt
clearance where the page layout permits, while excluding captions and neighboring prose.
The output is rendered at 300 dpi, converted to true grayscale, and autocontrasted.
Captions are excluded (Ch4 rewrites captions in prose). Where a foreign element shares
a figure's crop band but is separated in the other axis, it is white-masked after the
crop via MASKS rather than clipped (clipping would take real artwork with it).
"""
from pathlib import Path
import pymupdf
from PIL import Image, ImageOps

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
SRC = ROOT / 'Chapter' / 'class 11' / 'Chapter 04 - Animal Kingdom.pdf'
ASSETS = HERE / 'assets'
DPI = 300

# (asset_id, source page, (x0,y0,x1,y1), rationale)
FIGURES = [
    ('4_1a', 2, (98,108,246,268), 'p2 radial symmetry; includes organism and radial guide lines; stops above caption'),
    ('4_1b', 2, (58,286,290,492), 'p2 bilateral symmetry; 4x-grid repin right 276->290: crab art ends at x288.2 (old 276 clipped right claw/legs 12pt); caption sits at y491.3+ (below y1=492), so excluded'),
    ('4_2ab', 2, (58,510,302,681), 'p2 corrected right edge: extends beyond the right cross-section and retains all germ-layer labels and (a)/(b); excludes caption'),
    ('4_3abc', 3, (278,164,532,408), 'p3 coelom/pseudocoelom/acoelomate three-panel diagram; includes headings and (a)/(b)/(c), stops before caption'),
    ('4_4', 4, (58,96,534,342), 'p4 corrected bottom edge: stops below the classification diagram and above the footnote/caption'),
    ('4_5abc', 4, (60,426,290,681), 'p4 4x-grid repin, composite dropped: plain rect verified clean by render. Spongilla true right extent is x282.5 and prose column does not start until x306.7, so right=290 keeps all artwork with a ~17pt prose gap; (c) panel-label artwork sits above y681 while the printed "Figure 4.5 ..." caption begins at y688.4 (below y1=681, excluded). Old (65,420,315,674)+3-subcrop hack clipped (c) left 15pt and bottom ~7pt'),
    ('4_6ab', 5, (84,204,430,432), 'p5 Cnidaria polyp/medusa plate; includes both forms and (a)/(b), excludes caption'),
    ('4_7', 5, (416,470,510,618), 'p5 cnidoblast diagram; includes complete leader/label structure, excludes caption'),
    ('4_8', 6, (54,96,220,355), 'p6 corrected top edge: includes the complete Pleurobrachia ctenophore tip with compact upper padding'),
    ('4_9ab', 6, (170,486,506,694), 'p6 tapeworm/liver-fluke plate; includes both specimens and (a)/(b), excludes caption'),
    ('4_10', 7, (300,99,506,332), 'p7 4x-grid repin top 108->99: female worm head tip is at y101.3 (old top=108 clipped head 5.5pt); top=99 gives ~2pt margin; Male/Female labels kept; caption "Figure 4.10 ..." at y331.5+ (below y1=332, excluded)'),
    ('4_11ab', 7, (310,356,512,687), 'p7 4x-grid repin: Nereis antennae top at y359.5 so top=356 keeps them (old 368 clipped ~7pt); tail setae extend to y683.8 so bottom=687 (old 670 clipped ~13pt); right=512. The ONE foreign element in this y-band is fig 4.10\'s "Roundworm" caption at x[412,470] y[353.6,363.1] (top-right corner) -- erased by MASKS below, not by clipping the antennae, since caption and antennae share the y-band but are separated in x'),
    ('4_12abcd', 8, (54,112,300,366), 'p8 four Arthropoda specimens; includes all four part markers and specimen boundaries'),
    ('4_13ab', 8, (62,430,300,688), 'p8 Pila/Octopus plate; includes both specimens and (a)/(b), excludes caption'),
    ('4_14ab', 9, (340,94,510,328), 'p9 Asterias/Ophiura plate; includes both specimens and (a)/(b), excludes caption'),
    ('4_15', 9, (342,438,526,670), 'p9 labelled Balanoglossus; includes Proboscis, Collar, Trunk leaders and artwork'),
    ('4_16', 10, (54,106,292,222), 'p10 Chordata characteristics; includes Nerve cord, Notochord, Gill slits, Post-anal part'),
    ('4_17', 10, (136,398,250,620), 'p10 Ascidia specimen; includes full specimen and part label area, excludes caption'),
    ('4_18', 11, (280,384,526,462), 'p11 corrected left edge: starts beyond the neighboring prose column while retaining the complete Petromyzon specimen'),
    ('4_19ab', 11, (280,500,526,680), 'p11 corrected left edge: excludes neighboring prose while retaining full Scoliodon/Pristis artwork and (a)/(b)'),
    ('4_20ab', 12, (54,96,255,336), 'p12 4x-grid repin right 248->255: fish is raster (no vector drawings); prose column starts at x264, so right=255 extends past the clipped fish edge (old 248 clipped 1.8pt) while keeping a ~9pt gap to prose'),
    ('4_21ab', 12, (54,440,250,666), 'p12 Salamandra/Rana plate; includes both specimens and (a)/(b), excludes caption'),
    ('4_22abcd', 13, (32,94,540,288), 'p13 four Reptilia specimens; includes all four specimens and (a)-(d), excludes caption'),
    ('4_23abcd', 14, (34,92,540,275), 'p14 four bird specimens; includes all four specimens and (a)-(d), excludes caption'),
    ('4_24abcd', 14, (46,512,540,692), 'p14 four mammal specimens; includes all four specimens and (a)-(d), excludes caption'),
    ('vertebrata_chart', 11, (104,126,474,336), 'p11 bonus unnumbered Vertebrata division chart; included because it is a printed diagram without a figure caption'),
]

# Per-asset white-out rectangles, in source-PDF points, applied AFTER the crop.
# Used only to erase a provably-foreign element that shares a figure's crop band
# but is separated in the other axis (so it cannot be removed by tightening an
# edge without clipping real artwork). Each entry must cite what it erases.
MASKS = {
    # fig 4.10's printed "Roundworm" caption pokes into 4_11ab's top-right corner
    # (x[412,470] y[353.6,363.1]); the Nereis antennae are on the left (x[332,347]),
    # so clipping the top would lose antennae. Erase the caption box instead.
    '4_11ab': [(408, 352, 474, 365)],
}


def main():
    ASSETS.mkdir(parents=True, exist_ok=True)
    doc = pymupdf.open(SRC)
    k = DPI / 72.0
    for fid, pno, box, rationale in FIGURES:
        page = doc[pno - 1]
        rect = pymupdf.Rect(*box) & page.rect
        pix = page.get_pixmap(clip=rect, dpi=DPI, alpha=False)
        img = Image.frombytes('RGB', (pix.width, pix.height), pix.samples).convert('L')
        for mx0, my0, mx1, my1 in MASKS.get(fid, ()):  # white-out foreign elements
            px0 = int(round((mx0 - box[0]) * k)); py0 = int(round((my0 - box[1]) * k))
            px1 = int(round((mx1 - box[0]) * k)); py1 = int(round((my1 - box[1]) * k))
            px0, py0 = max(0, px0), max(0, py0)
            px1, py1 = min(img.width, px1), min(img.height, py1)
            if px1 > px0 and py1 > py0:
                img.paste(255, (px0, py0, px1, py1))
        img = ImageOps.autocontrast(img, cutoff=1)
        out = ASSETS / f'fig_{fid}.png'
        img.save(out)
        print(f'{out.name}: p{pno} rect={tuple(box)} size={img.size} mode={img.mode}')
    doc.close()

if __name__ == '__main__':
    main()
