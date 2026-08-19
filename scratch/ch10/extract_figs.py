"""Pass 1 §4.4 Step 1-2: clip-render every Ch10 figure at 300 dpi, then convert to
true monochrome (convert("L") + autocontrast). Only converted files reach assets/.

Fig 10.1 note: the source photograph includes the fingers of a hand holding the cotton
bolls. §4.4's hard no ("no photograph of a person, ever") is honoured by clipping the
frame above the fingers, keeping both bolls and the (a)/(b) labels intact.

[VERIFICATION FIX - Pass 3(a)] The NCERT source pages carry two full-bleed overlay
rasters: a 2480x3508 page background and a 1894x1894 diagonal "Reprinted" watermark.
Clip-rendering the COMPOSITED page baked that watermark into every extracted figure --
in Fig 10.1 it ran straight across the mature white boll, i.e. across the very feature
the (b) label points at. Both overlays are now deleted from an in-memory copy of the
page before the clip is rendered, so the figure is clean while the vector (a)/(b)
labels, which are page text and not part of the photo, still survive. The source PDF on
disk is never modified (§0.5).
"""
import os
import pymupdf
from PIL import Image, ImageOps

SRC = "/vercel/share/v0-project/Chapter/class 12/Chapter 10 - Biotechnology and its Applications.pdf"
OUT = "/vercel/share/v0-project/notes/class 12/Ch10_BiotechnologyAndItsApplications/assets"
RAW = "/vercel/share/v0-project/scratch/ch10/raw"
os.makedirs(OUT, exist_ok=True)
os.makedirs(RAW, exist_ok=True)

doc = pymupdf.open(SRC)

# page index, output name, clip rect (PDF points), search anchor for sanity
JOBS = [
    # Fig 10.1 - cotton boll photo on page 3; the bottom band carrying the fingers of
    # the hand holding the bolls is trimmed off in the crop step below.
    (3, "fig_10_1.png", (196.9, 192.7, 502.0, 396.1), "Figure  10.1"),
    (4, "fig_10_2.png", (101.2, 83.7, 448.7, 254.6), "Figure  10.2"),
    (5, "fig_10_3.png", (57.4, 84.0, 237.4, 229.0), "Figure  10.3"),
]

# trim fraction taken off the bottom of the rendered clip (removes the hand in 10.1)
BOTTOM_TRIM = {"fig_10_1.png": 0.26}

# [VERIFICATION FIX] native pixel dims of the two full-bleed overlays that must be
# suppressed before rendering: the page background and the diagonal "Reprinted" mark.
OVERLAY_DIMS = {(2480, 3508), (1894, 1894)}


def strip_overlays(page):
    """Delete the page-background and watermark rasters so a clip render is clean.

    Matched on native pixel dimensions rather than placed rectangle: the watermark is
    placed at only 462pt tall, so a "taller than 600pt" geometric guard silently misses
    it -- which is exactly how the watermark reached the delivered figures.
    """
    removed = []
    for img in page.get_images(full=True):
        xref, width, height = img[0], img[2], img[3]
        if (width, height) in OVERLAY_DIMS:
            page.delete_image(xref)
            removed.append((xref, width, height))
    return removed


def image_bbox(page):
    """Largest content image block on the page (excludes the tiny decorative bands)."""
    best = None
    for b in page.get_text("dict")["blocks"]:
        if b["type"] != 1:
            continue
        r = pymupdf.Rect(b["bbox"])
        if r.width < 60 or r.height < 60:
            continue
        if r.width > 400 and r.height > 600:        # full-page watermark
            continue
        if best is None or r.get_area() > best.get_area():
            best = r
    return best


for pno, name, clip, anchor in JOBS:
    page = doc[pno]
    rect = pymupdf.Rect(clip) if clip else image_bbox(page)
    if rect is None:
        raise RuntimeError(f"NO FIGURE REGION FOUND for {name} on page {pno}")
    stripped = strip_overlays(page)          # [VERIFICATION FIX] before any render
    if not stripped:
        raise RuntimeError(
            f"{name}: expected to strip the page background + watermark overlays on "
            f"page {pno} but found none -- refusing to render a possibly watermarked clip"
        )
    pix = page.get_pixmap(clip=rect, dpi=300)
    raw_path = os.path.join(RAW, name)
    pix.save(raw_path)

    img = Image.open(raw_path)
    rgb = img.convert("RGB")
    cols = rgb.getcolors(maxcolors=4_000_000) or []
    colourful = sum(c for c, (r, g, b) in cols if max(r, g, b) - min(r, g, b) > 25)

    trim = BOTTOM_TRIM.get(name)
    if trim:
        w, h = img.size
        img = img.crop((0, 0, w, int(h * (1 - trim))))

    mono = ImageOps.autocontrast(img.convert("L"), cutoff=1)
    mono.save(os.path.join(OUT, name))
    print(f"{name}: page {pno} clip {tuple(round(v,1) for v in rect)} "
          f"raw {rgb.size} -> mono {mono.size} mode {mono.mode} "
          f"| source colour pixels: {colourful} "
          f"| overlays stripped: {[x for x, _, _ in stripped]}")
