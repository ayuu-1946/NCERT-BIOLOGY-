"""Gate 3a — CORRECTED per-asset watermark + baked-border audit.

Why v1 (audit_watermark.py) was wrong, recorded deliberately:
  v1 hunted the watermark in the SOURCE PDF's *text layer* and found only the
  short "Reprint 2026-27" footer at y755-766, which no crop rect reaches. It
  therefore concluded "no watermark" -- and direct visual inspection of
  fig_5_5 / fig_5_6 immediately disproved that. The real "(C) NCERT / not to be
  republished" watermark is a VECTOR/GRAPHIC overlay, not a text span, so a
  text-layer sweep is blind to it. This is precisely the silent-failure class
  SUPREME COMMAND S4.4 warns about ("text extraction does not error -- it
  returns an empty set"). Never audit a picture through the text layer.

Corrected method -- measure the artwork itself:
  The watermark prints as a large, pale-grey, smoothly-shaded diagonal glyph
  run. Against NCERT line art (near-black strokes on white) it occupies a
  distinctive MID-GREY band that clean line art barely populates. So:
    mid_frac = fraction of pixels in the pale/mid-grey window [150, 245]
  A clean line-art plate is overwhelmingly near-white + near-black and has a
  small mid_frac; a watermarked plate carries a large connected mid-grey mass.
  We also report the largest connected mid-grey component as a share of the
  image, because shaded artwork (e.g. fig_5_6's grey helix ribbons) also raises
  mid_frac but in many small pieces rather than one sprawling diagonal blob.

  Verdict here is a RANKING to target the eye, never a substitute for it.
  Every asset is still opened and judged visually.

Also re-checks the baked border, at multiple insets, since fig_5_6 visibly
carries one that v1 only caught on a single edge.
"""
import os
from collections import deque

from PIL import Image

CH = "/vercel/share/v0-project/notes/class 12/Ch5_MolecularBasisOfInheritance"
ASSETS = os.path.join(CH, "assets")

MID_LO, MID_HI = 150, 245


def analyse(path):
    img = Image.open(path).convert("L")
    # downsample for the connected-component pass (speed), keep aspect
    w, h = img.size
    scale = max(1, int(max(w, h) / 500))
    small = img.resize((w // scale, h // scale)) if scale > 1 else img
    sw, sh = small.size
    px = small.load()

    mid = [[MID_LO <= px[x, y] <= MID_HI for x in range(sw)] for y in range(sh)]
    total = sw * sh
    mid_count = sum(sum(1 for v in row if v) for row in mid)

    # largest connected mid-grey blob
    seen = [[False] * sw for _ in range(sh)]
    best = 0
    for y0 in range(sh):
        for x0 in range(sw):
            if not mid[y0][x0] or seen[y0][x0]:
                continue
            n = 0
            q = deque([(x0, y0)])
            seen[y0][x0] = True
            while q:
                x, y = q.popleft()
                n += 1
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < sw and 0 <= ny < sh and mid[ny][nx] and not seen[ny][nx]:
                        seen[ny][nx] = True
                        q.append((nx, ny))
            best = max(best, n)

    return mid_count / total, best / total, img.size


def border_edges(path):
    """Return how many of the 4 edges carry a near-continuous dark rule at ANY
    inset 0..14 -- a baked-in frame around the crop."""
    img = Image.open(path).convert("L")
    w, h = img.size
    px = img.load()
    hits = []
    for name in ("top", "bottom", "left", "right"):
        best = 0.0
        best_inset = -1
        for inset in range(0, 15):
            if name in ("top", "bottom"):
                y = inset if name == "top" else h - 1 - inset
                if not (0 <= y < h):
                    continue
                dark = sum(1 for x in range(w) if px[x, y] < 150)
                frac = dark / w
            else:
                x = inset if name == "left" else w - 1 - inset
                if not (0 <= x < w):
                    continue
                dark = sum(1 for y in range(h) if px[x, y] < 150)
                frac = dark / h
            if frac > best:
                best, best_inset = frac, inset
        hits.append((name, best, best_inset))
    return hits


def main():
    names = [n for n in os.listdir(ASSETS) if n.endswith(".png")]
    names.sort(key=lambda n: (len(n), n))
    print(f"{'asset':<26} {'midfrac':>8} {'blob':>7}  {'edges>=0.85':>11}  watermark-rank")
    rows = []
    for n in names:
        mf, blob, size = analyse(os.path.join(ASSETS, n))
        edges = border_edges(os.path.join(ASSETS, n))
        nedge = sum(1 for _, f, _ in edges if f >= 0.85)
        rows.append((n, mf, blob, nedge, edges, size))

    for n, mf, blob, nedge, edges, size in sorted(rows, key=lambda r: -r[2]):
        rank = "HIGH" if blob > 0.02 else ("med" if blob > 0.005 else "low")
        print(f"{n:<26} {mf:8.3f} {blob:7.3f}  {nedge:>11}  {rank}")

    print()
    print("=== baked-border detail (edges with >=0.85 continuous dark ink) ===")
    for n, mf, blob, nedge, edges, size in rows:
        strong = [(e, round(f, 2), i) for e, f, i in edges if f >= 0.85]
        if strong:
            print(f"  {n:<26} {size[0]}x{size[1]}  {strong}")
    print()
    print("NOTE: midfrac/blob RANK candidates for the eye; they do not clear or")
    print("condemn any asset on their own. Visual confirmation is mandatory.")


if __name__ == "__main__":
    main()
