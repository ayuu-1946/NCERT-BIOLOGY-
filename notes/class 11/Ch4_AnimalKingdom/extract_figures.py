"""Animal Kingdom (Class 11) figure extraction, §4.4.

Every rectangle is in source-PDF points. Rectangles are intentionally tight: they include
all artwork, leader lines, in-figure labels, and subfigure markers, with about 8–12 pt
clearance where the page layout permits, while excluding captions and neighboring prose.
The output is rendered at 300 dpi, converted to true grayscale, and autocontrasted.
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
    ('4_1b', 2, (58,286,276,492), 'p2 bilateral symmetry; includes full crab, bilateral guide line, and part label; stops above caption'),
    ('4_2ab', 2, (58,510,302,681), 'p2 corrected right edge: extends beyond the right cross-section and retains all germ-layer labels and (a)/(b); excludes caption'),
    ('4_3abc', 3, (278,164,532,408), 'p3 coelom/pseudocoelom/acoelomate three-panel diagram; includes headings and (a)/(b)/(c), stops before caption'),
    ('4_4', 4, (58,96,534,342), 'p4 corrected bottom edge: stops below the classification diagram and above the footnote/caption'),
    ('4_5abc', 4, (58,408,315,672), 'p4 corrected right edge: includes the complete Spongilla artwork and markers; the separate prose strip at x300–315 is scrubbed after rendering'),
    ('4_6ab', 5, (84,204,430,432), 'p5 Cnidaria polyp/medusa plate; includes both forms and (a)/(b), excludes caption'),
    ('4_7', 5, (416,470,510,618), 'p5 cnidoblast diagram; includes complete leader/label structure, excludes caption'),
    ('4_8', 6, (54,96,220,355), 'p6 corrected top edge: includes the complete Pleurobrachia ctenophore tip with compact upper padding'),
    ('4_9ab', 6, (170,486,506,694), 'p6 tapeworm/liver-fluke plate; includes both specimens and (a)/(b), excludes caption'),
    ('4_10', 7, (300,108,506,332), 'p7 male/female roundworm pair; includes Male/Female labels and part caption-side label, excludes printed caption'),
    ('4_11ab', 7, (310,368,512,670), 'p7 Nereis/Hirudinaria plate; includes both specimens and (a)/(b), excludes caption'),
    ('4_12abcd', 8, (54,112,300,366), 'p8 four Arthropoda specimens; includes all four part markers and specimen boundaries'),
    ('4_13ab', 8, (62,430,300,688), 'p8 Pila/Octopus plate; includes both specimens and (a)/(b), excludes caption'),
    ('4_14ab', 9, (340,94,510,328), 'p9 Asterias/Ophiura plate; includes both specimens and (a)/(b), excludes caption'),
    ('4_15', 9, (342,438,526,670), 'p9 labelled Balanoglossus; includes Proboscis, Collar, Trunk leaders and artwork'),
    ('4_16', 10, (54,106,292,222), 'p10 Chordata characteristics; includes Nerve cord, Notochord, Gill slits, Post-anal part'),
    ('4_17', 10, (136,398,250,620), 'p10 Ascidia specimen; includes full specimen and part label area, excludes caption'),
    ('4_18', 11, (280,384,526,462), 'p11 corrected left edge: starts beyond the neighboring prose column while retaining the complete Petromyzon specimen'),
    ('4_19ab', 11, (280,500,526,680), 'p11 corrected left edge: excludes neighboring prose while retaining full Scoliodon/Pristis artwork and (a)/(b)'),
    ('4_20ab', 12, (54,96,248,336), 'p12 final right edge: retains complete Catla artwork and (a)/(b) while excluding the adjacent prose column'),
    ('4_21ab', 12, (54,440,250,666), 'p12 Salamandra/Rana plate; includes both specimens and (a)/(b), excludes caption'),
    ('4_22abcd', 13, (32,94,540,288), 'p13 four Reptilia specimens; includes all four specimens and (a)-(d), excludes caption'),
    ('4_23abcd', 14, (34,92,540,275), 'p14 four bird specimens; includes all four specimens and (a)-(d), excludes caption'),
    ('4_24abcd', 14, (46,512,540,692), 'p14 four mammal specimens; includes all four specimens and (a)-(d), excludes caption'),
    ('vertebrata_chart', 11, (104,126,474,336), 'p11 bonus unnumbered Vertebrata division chart; included because it is a printed diagram without a figure caption'),
]

def main():
    ASSETS.mkdir(parents=True, exist_ok=True)
    doc = pymupdf.open(SRC)
    for fid, pno, box, rationale in FIGURES:
        page = doc[pno - 1]
        rect = pymupdf.Rect(*box) & page.rect
        pix = page.get_pixmap(clip=rect, dpi=DPI, alpha=False)
        img = Image.frombytes('RGB', (pix.width, pix.height), pix.samples).convert('L')
        img = ImageOps.autocontrast(img, cutoff=1)
        # Figure 4.5c touches the neighboring prose column in the source layout.
        # Extend the crop to keep the artwork complete, then remove only the prose strip.
        if fid == '4_5abc':
            k = DPI / 72.0
            # The prose column begins beyond x=266; the full Spongilla artwork ends
            # before that boundary. Whiten only the confirmed prose strip.
            img.paste(255, (int((266-box[0])*k), 0, img.width, img.height))
        out = ASSETS / f'fig_{fid}.png'
        img.save(out)
        print(f'{out.name}: p{pno} rect={tuple(box)} size={img.size} mode={img.mode}')
    doc.close()

if __name__ == '__main__':
    main()
