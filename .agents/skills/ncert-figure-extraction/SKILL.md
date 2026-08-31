---
name: ncert-figure-extraction
description: >
  Extracts figures from an NCERT chapter PDF into cropped PNG assets using
  hand-pinned bounding boxes read off a grid overlay, then audits every box
  three ways (text-layer grazing, drawings-extent overflow, border-band ink)
  to guarantee no body text bleeds in and no artwork is clipped off.
  Use whenever a chapter's figures need to be (re-)extracted from its source
  PDF into notes/{class}/{chapter}/assets/. Triggers: "extract figures for
  chapter X", "figures came out wrong/cropped/useless", "redo Ch{N} assets".
---

# NCERT Figure Extraction

## Why this exists

Auto-detecting figure bounding boxes (clustering vector drawings, connected
components, etc.) fails silently on NCERT PDFs because **figures often sit
beside a body-text column, not just above/below one**. An auto-box will
happily include the neighboring paragraph. This produced unusable assets
for Ch5 (fig_5_4a shipped with a full column of prose bleeding in from the
left edge) before this workflow was adopted.

The fix that works reliably: **hand-pin every rect by reading it off a
rendered grid overlay, then mechanically audit the pinned rects** before
anything ships. This is slower per-figure than auto-detection but catches
defects at the gate rather than after a human opens the PNG.

Do not attempt to rebuild the auto-detection approach (drawings-clustering,
connected-components on an ink mask, etc.) as a shortcut. It was tried and
abandoned for this reason.

## The audit has three parts, and you need all three

This is the hardest-won lesson in this skill, so it comes before the
workflow. The original version of this procedure audited **only** text-layer
word grazing. Ch5 shipped through that audit "clean" with **two visibly
broken crops** — `fig_5_16` had its entire right-hand column and the left
edge of its crime-scene panel sliced off, and `fig_5_2` lost its `3'` / `HO`
terminal labels.

The reason is structural, not carelessness: **NCERT draws many in-figure
labels as vector artwork, not as text-layer glyphs.** `page.get_text("words")`
on Ch5 p29 returns *zero* words inside the plate region. A word-grazing audit
over a rect containing no words is vacuously clean — it reports success
because it found nothing to complain about. It cannot fail. That is the worst
possible property for a gate.

So the gate is three complementary checks:

| Check | Catches | Blind to |
|---|---|---|
| **A. Text-layer word grazing** | prose/caption bleeding into the crop | anything drawn as vector artwork |
| **B. Drawings-extent overflow** | artwork clipped off at an edge | raster-only (photo) figures |
| **C. Border-band ink** | any dark ink just outside the rect, whatever its origin | ink >6pt away; deliberately excluded neighbors |

Check A alone is not a gate. **Always run all three**, and always finish with
eyes on the PNG (step 5) — none of the three can catch a wrong-region crop.

## Prerequisites

```bash
uv venv /vercel/share/neetenv --python 3.13
uv pip install --python /vercel/share/neetenv/bin/python pymupdf Pillow numpy
```

Note `numpy` — check C needs it. Invoke every command through that
interpreter, never bare `python3`. The venv does **not** survive a session
boundary; `ls /vercel/share/neetenv/bin/python` is the first command of any
resumed session.

Locate:
- Source PDF: `Chapter/class <N>/Chapter <N> - <Title>.pdf`
- Target dir: `notes/class <N>/Ch<N>_<Slug>/assets/`
- Figure list: `notes/class <N>/Ch<N>_<Slug>/Ch<N>_<Slug>_inventory.md`
  (has a table of figure numbers, captions, and page numbers — use this to
  know which pages to render; don't guess from the PDF's own page numbers,
  front matter offsets them)

## Workflow

### 1. Render mandatory high-density grid overlays for every artwork page

For **every chapter update, new extraction, re-extraction, and crop-defect fix**, render each page listed in the inventory as containing a figure at **440 dpi** with coordinate gridlines every **5 PDF points** and coordinate labels every **20 PDF points** on both axes. This 4× high-density grid is mandatory for production pinning. Save the mandatory grids to `scratch/ch<N>_figs/grid_4x/p<NN>.png`.

```python
import pymupdf
from PIL import Image, ImageDraw
doc = pymupdf.open(SRC)
page = doc[pno - 1]
DPI = 440; STEP = 5; LABEL_STEP = 20; z = DPI / 72
pix = page.get_pixmap(dpi=DPI)
img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
d = ImageDraw.Draw(img)
for x in range(0, int(page.rect.width) + 1, STEP):
    d.line([(x*z, 0), (x*z, img.height)], fill=(175, 215, 255), width=1)
    if x % LABEL_STEP == 0: d.text((x*z + 2, 2), str(x), fill=(220, 0, 0))
for y in range(0, int(page.rect.height) + 1, STEP):
    d.line([(0, y*z), (img.width, y*z)], fill=(175, 215, 255), width=1)
    if y % LABEL_STEP == 0: d.text((2, y*z + 2), str(y), fill=(220, 0, 0))
img.save(f"scratch/ch{N}_figs/grid_4x/p{pno:02d}.png")
```

### 2. Read each figure's rect off its grid image — and cross-check numerically

#### Mandatory high-density completeness rule

Use the **440 dpi / 5-point grid** before every initial pinning and every repinning. The finer grid improves coordinate precision, but it does not replace visual judgment: the rectangle must include the complete figure, including every panel, arrow, in-figure label, terminal mark, bracket, and leader line. Stop the crop before the caption or neighboring prose unless the chapter convention explicitly embeds captions.

After every extraction run, **open every emitted PNG individually**, not only a contact sheet. Compare each image against the source grid page and confirm that no panel, label, arrow, charge mark, bracket, or outer edge is missing. A passing mechanical audit is insufficient when the wrong region was selected or when a multi-panel figure was mistaken for a single panel. If any element is absent, return to the 4× overlay, repin the rectangle, regenerate, rerun all three audits, and eyeball the corrected PNG again. Record the correction in the chapter inventory or audit notes.

Example 4× grid renderer:

```python
DPI = 440                 # mandatory production grid
STEP = 5                  # mandatory PDF-point spacing
for x in range(0, int(page.rect.width) + 1, STEP):
    d.line([(x*z, 0), (x*z, img.height)], fill=(175, 215, 255), width=1)
    if x % 20 == 0:
        d.text((x*z + 2, 2), str(x), fill=(220, 0, 0))
for y in range(0, int(page.rect.height) + 1, STEP):
    d.line([(0, y*z), (img.width, y*z)], fill=(175, 215, 255), width=1)
    if y % 20 == 0:
        d.text((2, y*z + 2), str(y), fill=(220, 0, 0))
```

The refinement is especially important for multi-panel diagrams. For example, a crop that captures only the upper state of a two-panel figure may pass a word-grazing check while silently omitting the lower state. Use the source page’s text-layer coordinates and drawing extents to locate the true bottom of the artwork, then leave a small margin before the caption.

#### Current canonical 4× grid script

The following is the current renderer used for Chapter 18. Keep the page-point spacing, DPI, line colors, label cadence, and output naming convention unchanged when reproducing the high-density grid. Change only `SRC`, `PAGES`, and `OUT` for another chapter.

```python
import os
import pymupdf
from PIL import Image, ImageDraw

SRC = 'Chapter/class 11/Chapter 18 - Neural Control and Coordination.pdf'
PAGES = [2, 3, 4, 5, 6, 7]
OUT = 'scratch/ch18_figs/grid_4x'
DPI = 440  # mandatory production grid
STEP = 5   # mandatory PDF-point spacing
LABEL_STEP = 20

os.makedirs(OUT, exist_ok=True)
doc = pymupdf.open(SRC)
for pno in PAGES:
    page = doc[pno - 1]
    z = DPI / 72
    pix = page.get_pixmap(dpi=DPI, alpha=False)
    img = Image.frombytes('RGB', (pix.width, pix.height), pix.samples)
    d = ImageDraw.Draw(img)
    for x in range(0, int(page.rect.width) + 1, STEP):
        xx = x * z
        d.line([(xx, 0), (xx, img.height)], fill=(175, 215, 255), width=1)
        if x % LABEL_STEP == 0:
            d.text((xx + 2, 2), str(x), fill=(220, 0, 0))
    for y in range(0, int(page.rect.height) + 1, STEP):
        yy = y * z
        d.line([(0, yy), (img.width, yy)], fill=(175, 215, 255), width=1)
        if y % LABEL_STEP == 0:
            d.text((2, yy + 2), str(y), fill=(220, 0, 0))
    img.save(f'{OUT}/p{pno:02d}.png')
```

`view` each grid page and trace the figure's outermost ink (artwork +
in-image labels + caption line if you're including it) as `(x0, y0, x1, y1)`
in PDF points.

**Then confirm the eyeballed box against the page's own geometry** rather
than trusting the read. Grid-reading is accurate to a few points at best,
and a few points is exactly the error that lops a `3'` off an edge:

```python
# union bbox of the artwork's vector drawings in the figure's y-band
dx, dy = [], []
for d in page.get_drawings():
    r = d["rect"]
    if r.y0 > Y_TOP and r.y1 < Y_BOT and r.width > 0.2 and r.height > 0.2 \
       and r.width < 480 and r.height < 420:   # skip page-furniture bands
        dx += [r.x0, r.x1]; dy += [r.y0, r.y1]
print("drawings extent x", min(dx), max(dx), "y", min(dy), max(dy))
```

Pin the rect a couple of points *outside* that extent. The width/height
caps matter: NCERT pages carry a full-page watermark rect and decorative
border bands that otherwise swallow the measurement.

Rules of thumb:
- Include the "Figure N.M <caption>" line only if the chapter's convention
  is to embed captions. If the notes rewrite captions in text (Ch5's
  convention), exclude it — and then confirm the caption's own `y0` from
  `get_text("words")` so the bottom edge stops just short of it.
- Exclude adjacent body-text columns even when visually close. Read the
  neighbor column's boundary from `get_text("words")` and clip just inside it.
- Two labeled sub-figures on a page (e.g. 5.4a / 5.4b) get separate rects
  and separate asset files, never one combined crop.
- An unnumbered/uncaptioned diagram NCERT still printed (e.g. a "Central
  dogma" schematic) is fine to extract as a bonus asset — name it
  `fig_<N>_<description>.png` and mark it unnumbered in the inventory.

### 3. Pin the rects in extract_figures.py

Follow the per-chapter convention (see
`notes/class 12/Ch5_MolecularBasisOfInheritance/extract_figures.py` for the
reference example — its comments record *why* each rect is where it is,
which is what makes a later re-audit cheap).

```python
"""§4.4 figure extraction for Ch<N> <Title>.
Rects are in PDF points (page is <W> x <H>)."""
import os, sys
import pymupdf
from PIL import Image, ImageOps

SRC = "Chapter/class <N>/Chapter <N> - <Title>.pdf"
OUT_DIR = "notes/class <N>/Ch<N>_<Slug>/assets"
RENDER_DPI = 300

# (asset_id, 1-indexed artwork page, (x0, y0, x1, y1))
FIGS = [
    ("N_1", 2, (108, 575, 528, 676)),
    # p4: labels are vector, not text-layer -- rect pinned off the
    # get_drawings() extent (x 89.6-514.9, y 84.1-275.4), caption at y=291.3
    ("N_2", 4, (86, 80, 519, 280)),
]

def main():
    doc = pymupdf.open(SRC)
    os.makedirs(OUT_DIR, exist_ok=True)
    for fid, pno, rect in FIGS:
        page = doc[pno - 1]
        pix = page.get_pixmap(clip=pymupdf.Rect(*rect) & page.rect, dpi=RENDER_DPI)
        img = ImageOps.autocontrast(
            Image.frombytes("RGB", (pix.width, pix.height), pix.samples).convert("L"),
            cutoff=1)
        out = os.path.join(OUT_DIR, f"fig_{fid}.png")
        img.save(out)
        print(f"fig_{fid}: p{pno} {rect} {img.size} mode={img.mode} -> {out}")

if __name__ == "__main__":
    sys.exit(main())
```

**Write a one-line comment per rect recording what pinned it** (drawings
extent, neighbor column x, caption y). When a rect is later found wrong,
that comment is the difference between a two-minute fix and re-deriving the
whole page.

Run it. It should complete without errors and print one line per figure.

### 4. Mandatory three-part audit — run before looking at a single image

```python
import pymupdf, importlib.util, numpy as np
from PIL import Image

spec = importlib.util.spec_from_file_location("ef", "path/to/extract_figures.py")
ef = importlib.util.module_from_spec(spec); spec.loader.exec_module(ef)
doc = pymupdf.open(ef.SRC)
DPI = 150; z = DPI / 72; BAND = 6.0; DARK = 110

print("--- A) text-layer word grazing ---")
for fid, pno, (x0, y0, x1, y1) in ef.FIGS:
    page = doc[pno - 1]; rect = pymupdf.Rect(x0, y0, x1, y1)
    cut = []
    for w in page.get_text("words"):
        wr = pymupdf.Rect(*w[:4]); inter = wr & rect
        if inter.is_empty: continue
        if inter.get_area() / max(1e-6, wr.get_area()) <= 0.9: cut.append(w[4])
    n = sum(1 for w in page.get_text("words")
            if not (pymupdf.Rect(*w[:4]) & rect).is_empty)
    print(f"  fig_{fid}: words_in_rect={n}" + (f" GRAZING {cut}" if cut else " ok"))

print("--- B) drawings-extent overflow ---")
for fid, pno, (x0, y0, x1, y1) in ef.FIGS:
    page = doc[pno - 1]; xs = []; ys = []
    for d in page.get_drawings():
        r = d["rect"]
        if r.width <= 0.2 or r.height <= 0.2 or r.width > 480 or r.height > 420: continue
        cx, cy = (r.x0 + r.x1) / 2, (r.y0 + r.y1) / 2
        if not (x0 <= cx <= x1 and y0 <= cy <= y1): continue   # centre-inside only
        xs += [r.x0, r.x1]; ys += [r.y0, r.y1]
    if not xs:
        print(f"  fig_{fid}: no drawings (raster figure)"); continue
    ov = [max(0, x0 - min(xs)), max(0, y0 - min(ys)),
          max(0, max(xs) - x1), max(0, max(ys) - y1)]
    print(f"  fig_{fid}: " + (f"OVERFLOW L{ov[0]:.1f} T{ov[1]:.1f} R{ov[2]:.1f} B{ov[3]:.1f}"
                              if max(ov) > 3 else "ok"))

print("--- C) unexplained dark ink in border band ---")
for fid, pno, (x0, y0, x1, y1) in ef.FIGS:
    page = doc[pno - 1]
    words = [pymupdf.Rect(*w[:4]) for w in page.get_text("words")]
    hits = []
    for side, b in {"L": (x0-BAND, y0, x0, y1), "R": (x1, y0, x1+BAND, y1),
                    "T": (x0, y0-BAND, x1, y0), "B": (x0, y1, x1, y1+BAND)}.items():
        r = pymupdf.Rect(*b) & page.rect
        if r.is_empty or r.width < 0.5 or r.height < 0.5: continue
        pix = page.get_pixmap(clip=r, dpi=DPI)
        a = np.array(Image.frombytes("RGB", (pix.width, pix.height), pix.samples).convert("L"))
        keep = 0; sample = None
        for py, px in zip(*np.nonzero(a < DARK)):
            X = r.x0 + px / z; Y = r.y0 + py / z
            if any(w.x0-1 <= X <= w.x1+1 and w.y0-1 <= Y <= w.y1+1 for w in words):
                continue   # legit prose/caption, deliberately excluded
            keep += 1
            if sample is None: sample = (round(X, 1), round(Y, 1))
        if keep > 40: hits.append(f"{side}:{keep}px@{sample}")
    print(f"  fig_{fid}: " + (f"EDGE-INK {hits}" if hits else "clean"))
```

Reading the output:

- **A.** `frac > 0.9` (word almost wholly inside) is a caption or in-figure
  label — fine. `frac <= 0.9` means the rect cuts a word belonging to
  something else; tighten that edge. **Also read `words_in_rect`**: if it is
  `0`, check A proved *nothing* about this figure and B/C are carrying the
  whole gate. Do not record such a figure as "audited" on A alone.
- **B.** Uses **centre-inside** membership so a neighboring column's rules
  don't join the union. Overflow >3pt on any side means real artwork is
  outside the crop. `no drawings` means a raster/photo figure — B cannot
  help; lean on C and the eyeball.
- **C.** Any surviving cluster (>40 px at 150 dpi) is dark ink just outside
  the rect that is not explained by a text-layer word. Render the reported
  coordinate and look: either it is figure artwork you clipped (extend the
  edge) or it is a genuinely separate element you meant to exclude (a
  different figure, a page-number tab, a decorative band) — in which case
  note it in the rect's comment and move on. Do not blanket-raise the
  threshold to silence it.

Target: A clean, B clean, C either clean or every hit explained in writing.

### 5. Visual confirmation (still required; the audit does not replace it)

The audit cannot catch a wrong crop region, a mirrored render, or illegible
contrast. `view` every emitted PNG.

Fastest reliable way: build one **contact sheet** of all assets and read it
in a single view, then open individually only what looks off.

```python
from PIL import Image, ImageDraw
CELL, COLS = 340, 5
rows = (len(order) + COLS - 1) // COLS
sheet = Image.new("L", (COLS*CELL, rows*(CELL+18)), 255)
d = ImageDraw.Draw(sheet)
for i, fid in enumerate(order):
    im = Image.open(f"{D}/fig_{fid}.png"); im.thumbnail((CELL-8, CELL-8))
    cx, cy = (i % COLS)*CELL, (i // COLS)*(CELL+18)
    sheet.paste(im, (cx+4, cy+16))
    d.rectangle([cx+1, cy+14, cx+CELL-2, cy+CELL+14], outline=0)
    d.text((cx+5, cy+3), f"fig_{fid}", fill=0)
sheet.save("scratch/ch<N>_figs/contact_sheet.png")
```

**`view` caches by path.** After re-running extraction, a `view` of the same
asset path will hand you back the *old* image — verified behavior, not a
theory. Copy to a unique path first (`cp fig.png scratch/fig_$(date +%s).png`)
and view that. The contact sheet gets this for free, since its filename
changes whenever you rebuild it. If two `view` calls on a file you just
rewrote return an identical image URL hash, that is the cache, not a
successful no-op.

A figure is done only when the audit is clean **and** you have looked at the
rendered PNG.

### 6. Update inventory and tracker

- `Ch<N>_..._inventory.md`: confirm each manifest row's caption matches what
  is actually **in** the asset. Check this explicitly against the image, not
  against the figure number — Ch5 shipped with `fig_5_3` captioned "Central
  dogma" while the asset was the DNA double helix, and the mismatch survived
  a full extraction redo plus a merged PR because every reviewer checked
  that a row *existed* rather than that it was *right*.
- Reconcile the **asset count** everywhere it appears (session log, header
  counts, gate rows, tracker status, on-disk listing). A bonus unnumbered
  asset changes the denominator; leaving one file at the old number is how
  the next session inherits a contradiction.
- `Ch<N>_TRACKER.md`: mark extraction done per the chapter's status
  convention, and record any rect that was re-pinned along with the reason.

### 7. Commit

One commit per chapter. Include the regenerated assets, `extract_figures.py`,
and the inventory/tracker updates together — assets without the rects that
produced them are not reproducible.

## Common failure modes and fixes

| Symptom | Cause | Fix |
|---|---|---|
| **Audit passes, crop is visibly wrong** | Figure's labels are vector artwork, so the text-layer word audit had zero words to inspect and passed vacuously | Run checks B and C; pin the rect off the `get_drawings()` extent. Always print `words_in_rect` so a vacuous pass is visible |
| Body text column bleeds into crop edge | Figure sits beside prose; rect didn't account for the column | Read the neighbor column's boundary from `get_text("words")` and clip just inside it |
| Artwork clipped at an edge, no text lost | Eyeballed rect off by a few points | Check B; extend past the drawings extent by ~2pt |
| Caption text cut off at bottom | `y1` stops mid-caption | Extend `y1` past the caption's `y1` (or below its `y0` if excluding captions) |
| Two sub-figures merged into one crop | Single rect spanned both | Split into two rects/assets |
| Check B reports absurd overflow | A full-page watermark or border band got into the union | Keep the `width > 480 / height > 420` caps and the centre-inside test |
| Check C fires on a neighbor figure or page tab | Correctly detected, deliberately excluded element | Explain it in the rect's comment; don't raise the threshold |
| Inventory caption doesn't match asset content | Nothing cross-checks caption text against the image | Diff caption vs. image explicitly in step 6 |
| `view` shows old image after re-running extraction | Tool caches by path | Copy to a unique path (or rebuild the contact sheet) before viewing |
| `ModuleNotFoundError` / interpreter confusion | Sandbox `pip` is aliased to `uv`; `python3` on PATH is externally managed | Use the `/vercel/share/neetenv` venv interpreter for every command; rebuild it at session start |
