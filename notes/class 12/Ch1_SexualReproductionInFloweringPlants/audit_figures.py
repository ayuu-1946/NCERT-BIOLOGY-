"""Audit gate for Ch1 figure rects.

The source PDF is a raster scan, so two of the skill's three checks cannot
fire at all. This script proves that rather than assuming it, then substitutes
an ink-projection check for the missing coverage.

  A) text-layer word grazing  -> reported as VACUOUS (0 words on every page)
  B) drawings-extent overflow -> reported as VACUOUS (0 drawings on every page)
  C) border-band ink          -> works; any dark ink within BAND pt outside an
                                 edge is flagged. There is no text layer to
                                 excuse a hit, so every hit must be explained
                                 in writing or the rect must move.
  D) ink-projection margins   -> NEW. Measures the tight ink bbox inside each
                                 rect and asserts a whitespace margin on all
                                 four sides. A zero margin means ink runs to
                                 the crop edge, i.e. something is clipped.
                                 This is what replaces check B here.

Run from the repo root:
  /vercel/share/neetenv/bin/python "notes/class 12/Ch1_SexualReproductionInFloweringPlants/audit_figures.py"
"""

import importlib.util
import os
import sys

import numpy as np
import pymupdf
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
DPI = 150
Z = DPI / 72
BAND = 6.0        # pt, width of the border band inspected by check C
DARK = 110        # 0-255 grayscale; below this counts as ink
C_MIN_PX = 40     # cluster size at 150 dpi before check C complains
D_MIN_MARGIN = 1.0  # pt of whitespace required inside each edge

# Border-band hits that are real, understood, and deliberately excluded.
# Keyed by asset id -> explanation. A hit NOT listed here fails the gate.
EXPLAINED = {
    # 1.4 and 1.5 share page 7. 1.4's right band looks across the gutter at
    # 1.5's (a) tetrad circle; 1.5's left band looks back at 1.4's third SEM
    # photo and at the body-text column beneath it.
    "1_4": "R band sees fig 1.5(a) tetrad on the same page - separate figure",
    "1_5": "L band sees fig 1.4's third SEM photo + body prose - excluded",
    # Figures set beside a prose column: the band necessarily grazes the text
    # we are deliberately keeping out.
    "1_2": "L band sees the left body-text column on p5 - excluded",
    "1_9": "R band sees the right body-text column on p12 - excluded",
    "1_10": "L band sees the left body-text column on p13 - excluded",
    "1_11": "R band sees the right body-text column on p14 - excluded",
    "1_14": "L band sees the left body-text column on p19 - excluded",
    # Sub-panel crops are carved out of a plate, so their bands look at the
    # neighbouring panels of the same plate by construction.
    "1_9a": "bands see sibling panels of plate 1.9",
    "1_9b": "bands see sibling panels of plate 1.9",
    "1_9c": "bands see sibling panels + shared caption of plate 1.9",
    "1_11a": "bands see sibling panel (b) of plate 1.11",
    "1_11b": "bands see sibling panel (a) + shared caption of plate 1.11",
    "1_12a": "bands see sibling panels of plate 1.12",
    "1_12b": "bands see sibling panels of plate 1.12",
    "1_12c": "bands see sibling panels of plate 1.12",
    "1_12d": "bands see sibling panels + shared caption of plate 1.12",
    "1_12e": "bands see sibling panels + shared caption of plate 1.12",
    "1_14a": "bands see sibling panel (b) of plate 1.14",
    "1_14b": "bands see sibling panel (a) + shared caption of plate 1.14",
    "1_15a": "bands see sibling panel (b) of plate 1.15",
    "1_15b": "bands see sibling panel (a) + shared caption of plate 1.15",
    "1_3": "B band sees the body prose that follows the caption on p6",
    "1_7": "B band sees the body prose that follows the caption on p9",
    "1_13": "T band sees the paragraph above the plate on p18",
}


def load_ef():
    spec = importlib.util.spec_from_file_location(
        "ef", os.path.join(HERE, "extract_figures.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def gray(page, rect):
    pix = page.get_pixmap(clip=rect, dpi=DPI)
    img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
    return np.array(img.convert("L"))


def main():
    ef = load_ef()
    doc = pymupdf.open(ef.SRC)
    failures = []

    print("=== A) text-layer word grazing ===")
    pages = sorted({p for _, p, _ in ef.FIGS})
    words_total = sum(len(doc[p - 1].get_text("words")) for p in pages)
    print(f"  words across all {len(pages)} artwork pages: {words_total}")
    print("  VACUOUS - raster scan has no text layer; check A proves nothing.")
    print("  Coverage for prose-bleed is carried by check C.")

    print("=== B) drawings-extent overflow ===")
    draw_total = sum(len(doc[p - 1].get_drawings()) for p in pages)
    print(f"  vector drawings across all {len(pages)} artwork pages: {draw_total}")
    print("  VACUOUS - raster scan has no vector art; check B proves nothing.")
    print("  Coverage for clipped artwork is carried by check D.")

    print("=== C) unexplained dark ink in border band ===")
    for fid, pno, (x0, y0, x1, y1) in ef.FIGS:
        page = doc[pno - 1]
        hits = []
        bands = {
            "L": (x0 - BAND, y0, x0, y1),
            "R": (x1, y0, x1 + BAND, y1),
            "T": (x0, y0 - BAND, x1, y0),
            "B": (x0, y1, x1, y1 + BAND),
        }
        for side, b in bands.items():
            r = pymupdf.Rect(*b) & page.rect
            if r.is_empty or r.width < 0.5 or r.height < 0.5:
                continue
            a = gray(page, r)
            n = int((a < DARK).sum())
            if n > C_MIN_PX:
                ys, xs = np.nonzero(a < DARK)
                sample = (round(r.x0 + xs[0] / Z, 1), round(r.y0 + ys[0] / Z, 1))
                hits.append(f"{side}:{n}px@{sample}")
        if not hits:
            print(f"  fig_{fid}: clean")
        elif fid in EXPLAINED:
            print(f"  fig_{fid}: EDGE-INK {hits}")
            print(f"      explained: {EXPLAINED[fid]}")
        else:
            print(f"  fig_{fid}: EDGE-INK {hits}  <-- UNEXPLAINED")
            failures.append(f"C/{fid}")

    print("=== D) ink-projection margins inside the rect ===")
    for fid, pno, (x0, y0, x1, y1) in ef.FIGS:
        page = doc[pno - 1]
        r = pymupdf.Rect(x0, y0, x1, y1) & page.rect
        a = gray(page, r)
        mask = a < DARK
        if not mask.any():
            print(f"  fig_{fid}: NO INK IN RECT  <-- wrong region?")
            failures.append(f"D/{fid}")
            continue
        ys, xs = np.nonzero(mask)
        left = xs.min() / Z
        right = (a.shape[1] - 1 - xs.max()) / Z
        top = ys.min() / Z
        bottom = (a.shape[0] - 1 - ys.max()) / Z
        tight = [round(v, 1) for v in (left, top, right, bottom)]
        if min(left, top, right, bottom) < D_MIN_MARGIN:
            print(f"  fig_{fid}: MARGINS L{tight[0]} T{tight[1]} "
                  f"R{tight[2]} B{tight[3]}  <-- INK AT EDGE, likely clipped")
            failures.append(f"D/{fid}")
        else:
            print(f"  fig_{fid}: ok  margins L{tight[0]} T{tight[1]} "
                  f"R{tight[2]} B{tight[3]}")

    print("=== RESULT ===")
    if failures:
        print(f"  FAIL ({len(failures)}): {', '.join(failures)}")
        return 1
    print(f"  PASS - {len(ef.FIGS)} rects; C clean-or-explained, D margins ok")
    print("  Step 5 (eyes on every PNG) is still required.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
