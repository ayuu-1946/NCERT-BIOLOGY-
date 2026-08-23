"""Raster-ink audit gate for Ch6 Evolution figure rects.

WHY THIS FILE EXISTS (read before "fixing" it):
The Ch6 source PDF is 100% scanned raster -- every page is one full-page
image. Verified: get_text("words") == [] and get_drawings() == [] on all 17
pages. Therefore the skill's three-part audit degrades to nothing:

  check A (text-layer word grazing) -> 0 words in every rect. The skill
      itself warns that a word-grazing audit over a rect with no words
      "cannot fail. That is the worst possible property for a gate."
  check B (drawings-extent overflow) -> "no drawings" for every rect.
  check C (border-band ink)          -> works, but its word-exclusion clause
      is inert, so scanned prose/captions fire as edge ink and must be
      triaged by eye rather than auto-explained.

Replacement gate, both computed from page pixels:

  A' INTERIOR SLACK -- ink extent inside the rect vs. the rect edges.
     Slack < 0 means ink is flush against the edge (likely clipped).
     Large positive slack means wasted margin / possibly the wrong region.

  B' EDGE-BAND PROBE -- dark pixels in an 8pt band just outside each edge.
     Every hit must be explained in EXPLAINED below, naming what the ink is.
     An unexplained hit fails the gate.

Run: /vercel/share/neetenv/bin/python "notes/class 12/Ch6_Evolution/audit_figures.py"
"""
import importlib.util
import os
import sys

import numpy as np
import pymupdf
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("ef", os.path.join(HERE, "extract_figures.py"))
ef = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ef)

DPI = 150
Z = DPI / 72
BAND = 8.0
DARK = 110
BAND_TOL = 40     # px at 150 dpi before a band counts as a hit

# Slack tolerances, in points.
#
# SLACK_MIN is NEGATIVE on purpose. Rect edges are converted to pixel indices,
# which quantises each edge by up to one pixel (0.48pt at 150 dpi), so the
# measured ink extent can land marginally outside the rect even when nothing is
# clipped. Verified by re-measuring six figures at 150/200/300/400 dpi: the
# apparent "L-0.2" readings oscillated around zero (+0.08, -0.16, +0.08, +0.02)
# instead of staying negative, which is the signature of quantisation noise
# rather than real clipping. One pixel of tolerance absorbs that.
#
# Real clipping is still caught: it shows up as slack of several points that
# stays negative at every DPI (as fig_6_11's clipped occiput did before the
# rect was re-pinned), and it also trips the B' edge-band probe.
SLACK_MIN = -0.5
SLACK_MAX = 22.0  # more margin than this suggests a mis-pinned edge

# Every edge-band hit must be named here, or the gate fails.
# side -> what the ink actually is (verified by rendering the band).
EXPLAINED = {
    "6_1":  {"L": "body prose in the left margin of the text column",
             "R": "body prose / watermark to the right",
             "B": "caption band 'Figure 6.1 ...' + body prose below it"},
    "6_3a": {"L": "prose column (gutter at x=377-389)",
             "T": "page-furniture leaf/branch graphic",
             "B": "sub-figure (b) artwork below"},
    "6_3b": {"L": "prose column (gutter at x=377-389)",
             "T": "sub-figure (a) artwork above",
             "B": "caption band 'Figure 6.3 ...'"},
    "6_4a": {"R": "moth panel (b) -- separate asset",
             "T": "page-furniture leaf/branch graphic"},
    "6_4b": {"L": "moth panel (a) -- separate asset",
             "R": "decorative page border band (starts x~551)",
             "B": "'(b)' sub-label tail / caption band"},
    "6_5":  {"L": "'EVOLUTION' running header",
             "T": "page-furniture leaf/branch graphic"},
    "6_7":  {"T": "page-furniture leaf/branch graphic",
             "B": "caption band 'Figure 6.7 ...'",
             "R": "body prose column (starts x~320)"},
    "6_8":  {"R": "page-number tab + decorative border band outside the frame",
             "T": "body prose line above the panel"},
    "6_9":  {"T": "page-furniture leaf/branch graphic"},
    "6_10": {"T": "page-furniture leaf/branch graphic"},
    "6_11": {"L": "watermark text", "B": "caption band 'Figure 6.11 ...'"},
    "6_2":  {},
    "6_6":  {},
}


def main():
    doc = pymupdf.open(ef.SRC)
    cache = {}

    def arr(pno):
        if pno not in cache:
            pix = doc[pno - 1].get_pixmap(dpi=DPI)
            cache[pno] = np.array(
                Image.frombytes("RGB", (pix.width, pix.height), pix.samples).convert("L")
            )
        return cache[pno]

    # Prove the premise: this PDF really has no text layer and no vector art.
    words = sum(len(doc[i].get_text("words")) for i in range(len(doc)))
    draws = sum(len(doc[i].get_drawings()) for i in range(len(doc)))
    print(f"PREMISE: total text-layer words={words}, total drawings={draws}")
    print("  -> skill checks A and B are inert; using raster gate A'/B'.\n")

    failures = []

    print("--- A') interior ink slack (rect edge -> nearest ink) ---")
    for fid, pno, (x0, y0, x1, y1) in ef.FIGS:
        a = arr(pno)
        ix0, iy0, ix1, iy1 = int(x0 * Z), int(y0 * Z), int(x1 * Z), int(y1 * Z)
        sub = a[iy0:iy1, ix0:ix1] < 150
        rows = np.nonzero(sub.any(axis=1))[0]
        cols = np.nonzero(sub.any(axis=0))[0]
        if len(rows) == 0:
            print(f"  fig_{fid}: EMPTY RECT")
            failures.append(f"{fid}: empty rect")
            continue
        sl = {
            "L": (ix0 + cols[0]) / Z - x0,
            "T": (iy0 + rows[0]) / Z - y0,
            "R": x1 - (ix0 + cols[-1]) / Z,
            "B": y1 - (iy0 + rows[-1]) / Z,
        }
        bad = [f"{k}{v:+.1f}" for k, v in sl.items() if v < SLACK_MIN or v > SLACK_MAX]
        txt = " ".join(f"{k}{v:.1f}" for k, v in sl.items())
        if bad:
            print(f"  fig_{fid}: {txt}   <-- CHECK {bad}")
            failures.append(f"{fid}: slack {bad}")
        else:
            print(f"  fig_{fid}: {txt}   ok")

    print("\n--- B') edge-band ink just outside the rect (must be explained) ---")
    for fid, pno, (x0, y0, x1, y1) in ef.FIGS:
        a = arr(pno)
        hits = []
        bands = {
            "L": (x0 - BAND, y0, x0, y1),
            "R": (x1, y0, x1 + BAND, y1),
            "T": (x0, y0 - BAND, x1, y0),
            "B": (x0, y1, x1, y1 + BAND),
        }
        for side, b in bands.items():
            bx0, by0, bx1, by1 = [int(v * Z) for v in b]
            bx0, by0 = max(0, bx0), max(0, by0)
            bx1, by1 = min(a.shape[1], bx1), min(a.shape[0], by1)
            if bx1 <= bx0 or by1 <= by0:
                continue
            n = int((a[by0:by1, bx0:bx1] < DARK).sum())
            if n > BAND_TOL:
                hits.append((side, n))
        parts = []
        for side, n in hits:
            why = EXPLAINED.get(fid, {}).get(side)
            if why:
                parts.append(f"{side}:{n}px [{why}]")
            else:
                parts.append(f"{side}:{n}px [UNEXPLAINED]")
                failures.append(f"{fid}: unexplained {side}-band ink ({n}px)")
        print(f"  fig_{fid}: " + ("; ".join(parts) if parts else "clean"))

    print()
    if failures:
        print(f"GATE FAILED ({len(failures)}):")
        for f in failures:
            print("  -", f)
        return 1
    print(f"GATE PASSED: {len(ef.FIGS)} figures, slack in range, all edge ink explained.")
    print("NOTE: a numeric pass still cannot catch a wrong-region crop -- view the PNGs.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
