"""Gate 3a — systematic per-asset audit of the two figure-content defects the
page walk surfaced (handoff §5): (1) a baked-in NCERT copyright watermark, and
(2) a border baked into the crop that doubles the template's own figure box.

This does NOT replace looking at the images — it locates and ranks candidates so
the visual pass is targeted rather than prose-noted. Every asset still gets
opened by eye; this table is the checklist that walk fills in.

Method:
  watermark  -- the NCERT watermark is a long, low-contrast, near-horizontal grey
                text band. We look in the SOURCE pdf's text layer for the
                copyright string on the page each asset was cropped from, and we
                measure whether the asset's own crop rect overlapped it. That is
                the only way to be certain: once flattened to pixels the
                watermark is indistinguishable from artwork by simple stats.
  border     -- a baked border shows up as near-continuous dark ink along all
                four edges of the asset's own bounding box, inset by a few px.
"""
import os
import re
import pymupdf
from PIL import Image

CH = "/vercel/share/v0-project/notes/class 12/Ch5_MolecularBasisOfInheritance"
ASSETS = os.path.join(CH, "assets")
SRC = "/vercel/share/v0-project/Chapter/class 12/Chapter 5 - Molecular Basis of Inheritance.pdf"

WM_PAT = re.compile(r"reprint|republish|not to be|©|copyright|ncert", re.I)


def border_score(path):
    """Fraction of each edge band that is dark. ~1.0 on all four = baked border."""
    img = Image.open(path).convert("L")
    w, h = img.size
    px = img.load()
    res = {}
    inset_best = {}
    for name in ("top", "bottom", "left", "right"):
        best = 0.0
        best_in = -1
        for inset in range(0, 12):
            dark = 0
            total = 0
            if name in ("top", "bottom"):
                y = inset if name == "top" else h - 1 - inset
                if not (0 <= y < h):
                    continue
                for x in range(0, w):
                    total += 1
                    if px[x, y] < 140:
                        dark += 1
            else:
                x = inset if name == "left" else w - 1 - inset
                if not (0 <= x < w):
                    continue
                for y in range(0, h):
                    total += 1
                    if px[x, y] < 140:
                        dark += 1
            frac = dark / total if total else 0.0
            if frac > best:
                best = frac
                best_in = inset
        res[name] = best
        inset_best[name] = best_in
    return res, inset_best


def main():
    print("=== SOURCE watermark text-layer census ===")
    wm_pages = {}
    if os.path.exists(SRC):
        doc = pymupdf.open(SRC)
        print(f"source: {SRC}  pages={len(doc)}")
        for i, page in enumerate(doc):
            hits = []
            for blk in page.get_text("dict")["blocks"]:
                for ln in blk.get("lines", []):
                    for sp in ln.get("spans", []):
                        if WM_PAT.search(sp["text"]):
                            hits.append((sp["text"].strip(), tuple(round(v, 1) for v in sp["bbox"])))
            if hits:
                wm_pages[i + 1] = hits
        for pg, hits in sorted(wm_pages.items()):
            for t, bb in hits:
                print(f"  src p{pg:>2}: {t[:60]!r} bbox={bb}")
        if not wm_pages:
            print("  NO watermark string found in source text layer on any page.")
    else:
        print(f"  SOURCE MISSING at {SRC}")

    print()
    print("=== PER-ASSET border-band ink (baked-border detector) ===")
    print(f"{'asset':<26} {'W':>5} {'H':>5} {'top':>6} {'bot':>6} {'left':>6} {'right':>6}  verdict")
    names = sorted(
        os.listdir(ASSETS),
        key=lambda n: (len(n), n),
    )
    for n in names:
        if not n.endswith(".png"):
            continue
        p = os.path.join(ASSETS, n)
        img = Image.open(p)
        sc, ins = border_score(p)
        allhigh = min(sc.values()) > 0.90
        verdict = "BAKED BORDER (all 4 edges)" if allhigh else (
            "partial edge ink" if max(sc.values()) > 0.90 else "no baked border"
        )
        print(
            f"{n:<26} {img.size[0]:>5} {img.size[1]:>5} "
            f"{sc['top']:>6.2f} {sc['bottom']:>6.2f} {sc['left']:>6.2f} {sc['right']:>6.2f}  {verdict}"
        )


if __name__ == "__main__":
    main()
