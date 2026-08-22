"""Gate 3(b) Direction 2 -- independent clip audit of the 18 pinned figure boxes.

Doctrine test: if artwork ink sits in a thin band just OUTSIDE a box edge and is
contiguous with ink just INSIDE that edge, the crop is severing a stroke, i.e.
the shipped asset is clipped.

Text-layer glyphs (body prose, captions, page numbers, running footers) are NOT
artwork; they are masked out first so a nearby paragraph cannot masquerade as
clipped artwork.
"""
import importlib.util
import pymupdf
import numpy as np

SPEC = importlib.util.spec_from_file_location(
    "ef", "notes/class 12/Ch5_MolecularBasisOfInheritance/extract_figures.py")
EF = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(EF)

DPI = 200
S = DPI / 72.0
BAND = 3.0      # pt just outside the edge
INNER = 3.0     # pt just inside the edge
INK = 230       # < this grey value counts as ink


def page_ink_mask(page):
    """Full-page ink mask with every text-layer line blanked out."""
    pix = page.get_pixmap(dpi=DPI, colorspace=pymupdf.csGRAY)
    a = np.frombuffer(pix.samples, dtype=np.uint8).reshape(
        pix.height, pix.width).copy()
    for blk in page.get_text("dict")["blocks"]:
        if blk.get("type") != 0:
            continue
        for ln in blk["lines"]:
            # only mask lines that actually carry visible characters
            txt = "".join(sp["text"] for sp in ln["spans"]).strip()
            if not txt:
                continue
            b = ln["bbox"]
            x0 = max(int((b[0]) * S) - 2, 0)
            y0 = max(int((b[1]) * S) - 2, 0)
            x1 = int((b[2]) * S) + 2
            y1 = int((b[3]) * S) + 2
            a[y0:y1, x0:x1] = 255
    return a < INK


def frac(mask, x0, y0, x1, y1):
    """Fraction of ink pixels in a pt-space rect."""
    cx0 = max(int(x0 * S), 0)
    cy0 = max(int(y0 * S), 0)
    cx1 = min(int(x1 * S), mask.shape[1])
    cy1 = min(int(y1 * S), mask.shape[0])
    if cx1 <= cx0 or cy1 <= cy0:
        return 0.0
    sub = mask[cy0:cy1, cx0:cx1]
    return float(sub.mean())


def main():
    doc = pymupdf.open(EF.SRC)
    cache = {}
    print(f"{'figure':14}{'pg':>3}  {'outL':>6}{'inL':>6} {'outR':>6}{'inR':>6}"
          f" {'outT':>6}{'inT':>6} {'outB':>6}{'inB':>6}  verdict")
    flagged = []
    for fid, pno, (x0, y0, x1, y1) in EF.FIGS:
        page = doc[pno - 1]
        if pno not in cache:
            cache[pno] = page_ink_mask(page)
        m = cache[pno]

        oL = frac(m, x0 - BAND, y0, x0, y1)
        iL = frac(m, x0, y0, x0 + INNER, y1)
        oR = frac(m, x1, y0, x1 + BAND, y1)
        iR = frac(m, x1 - INNER, y0, x1, y1)
        oT = frac(m, x0, y0 - BAND, x1, y0)
        iT = frac(m, x0, y0, x1, y0 + INNER)
        oB = frac(m, x0, y1, x1, y1 + BAND)
        iB = frac(m, x0, y1 - INNER, x1, y1)

        bad = []
        for name, o, i in (("L", oL, iL), ("R", oR, iR),
                           ("T", oT, iT), ("B", oB, iB)):
            # ink both sides of the edge => a stroke is being cut
            if o > 0.002 and i > 0.002:
                bad.append(name)
        verdict = "CLIP:" + "".join(bad) if bad else "clean"
        if bad:
            flagged.append((fid, pno, bad))
        print(f"fig_{fid:10}{pno:>3}  {oL:6.3f}{iL:6.3f} {oR:6.3f}{iR:6.3f}"
              f" {oT:6.3f}{iT:6.3f} {oB:6.3f}{iB:6.3f}  {verdict}")

    print()
    print(f"boxes audited: {len(EF.FIGS)}   flagged: {len(flagged)}")
    for fid, pno, bad in flagged:
        print(f"  fig_{fid} (p{pno}) edges={','.join(bad)}")


if __name__ == "__main__":
    main()
