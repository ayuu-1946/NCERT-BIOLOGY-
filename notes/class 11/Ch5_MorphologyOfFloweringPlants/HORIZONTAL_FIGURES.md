# Figure layout decisions — Ch5 Morphology of Flowering Plants

A decisions file, in the sense §4.4 uses the term: it records figure-layout
judgements so Pass 2 and Pass 3 inherit the reasoning rather than rediscovering it.
It is **not** a status document — Gate state lives in `Ch5_TRACKER.md`, and facts
live in the frozen inventory.

## Decision 1 — assets are artwork-only; captions are typeset by the script

Every rectangle in `extract_figures.py` **excludes the printed caption**. The
chapter script typesets each caption from the inventory's `caption` rows
(`Type: caption`, one per figure), so a caption baked into the plate would print
twice. This matches the convention in the closed chapters, e.g. Ch6 Anatomy of
Flowering Plants.

The corollary matters: **a figure with no typeset caption will have none at all.**
There is no longer a fallback copy inside the image.

*Superseded approach.* An earlier pass produced a parallel `assets/caption_free/`
tree via a `remove_captions.py` script that pixel-cropped the caption band off
each already-extracted PNG. That layer was removed at Gate 1 for three reasons:

1. **It carried the crop defects.** Its own record listed 10 of 17 figures as
   "unchanged", so `caption_free/fig_5_2.png` still rendered the in-figure label
   `Laterals` as "erals", and `caption_free/fig_5_4.png` was still missing its
   `(b)` and `(c)` panel markers. Cropping a caption off a defective plate leaves
   a defective plate.
2. **Its crop boxes were hardcoded pixel coordinates** measured against the
   pre-re-pin assets. Re-pinning changed every asset's dimensions — `fig_5_12.png`
   went from 684x2180 to 430x2230, for instance — so boxes such as
   `(0, 0, 592, 2240)` would now pad the image with black rather than trim it.
3. **It is subsumed.** Excluding the caption in the PDF rect is reproducible from
   source and strictly better than post-cropping a raster: it is one step instead
   of two, and it is what surfaced the 12 defective rectangles in the first place.

## Decision 2 — tall plates are re-flowed horizontally

Two figures cannot be placed at their native aspect ratio on an A4-portrait page.
§4.4 forbids squashing a plate to fit, so the panels are re-laid out instead,
each kept at its native scale:

| Source | Composite | Panels | Native | Composite |
|---|---|---:|---:|---:|
| `assets/fig_5_12.png` | `assets/fig_5_12_horizontal.png` | (a)–(e) | 430 x 2230 (1:5.2) | 1633 x 435 (3.75:1) |
| `assets/fig_5_4.png` | `assets/fig_5_4_horizontal.png` | (a)–(c) | 905 x 1496 | 1411 x 840 |

Panel markers are preserved, and the caption is excluded exactly as in Decision 1
— so the `caption` rows still supply the mapping from `(a)`…`(e)` to *Marginal*,
*Axile*, *Parietal*, *Free central*, *Basal*.

Both composites are **single-channel `mode="L"` at 300 dpi**, like every other
asset. This was a real defect in the previous version, which built its canvas as
`Image.new("RGB", ...)`: both committed composites were 3-channel, and
`check_pdf.py` check 3 fails any build that embeds a non-greyscale image, so they
could not have been used as they stood.

## Decision 3 — Fig. 5.7 and Fig. 5.8 share one horizontal plate

The racemose and cymose inflorescence plates are both label-free and were
originally stacked vertically. The final Pass 2 layout pairs them horizontally
in `assets/fig_5_7_5_8_horizontal.png`, preserving their aspect ratios while
reducing the combined vertical cost. The composite is a single-channel `mode="L"`
PNG at 300 dpi with dimensions **2661 x 1071**. Its caption explicitly maps the
left and right panels to Figs. 5.7 and 5.8, so the figure numbers remain visible
in the text layer.

### Panels are located by projection, not by hardcoded pixels

`compose_horizontal_figures.py` finds panel boundaries by projecting the image
onto its row axis and taking runs of non-blank rows. Two details make this work
on these particular plates, and both are worth keeping:

- **"Blank" means "holds no pixel darker than 215", not "is white".** NCERT's
  watermark renders around grey 230–245. A pure-white test treats every
  watermarked row as content, and the whole of Fig 5.12 then segments as a single
  band. This is the same threshold the Gate 1 ink measurements use.
- **Short bands are absorbed into a neighbouring panel, keyed on height rather
  than on the gap to the next band.** A gap rule cannot separate the two cases in
  Fig 5.12: panel (a) sits **1 px** above panel (b) and must stay separate, while
  each panel sits ~27 px above its own marker and must merge with it. Heights are
  unambiguous — markers run 33–37 px, panels 373–413 px. A short band that comes
  *first* attaches forwards instead, which is how Fig 5.4's `Lamina` label joins
  panel (a).

The previous version hardcoded pixel boxes, and several already reached past the
image bounds before the re-pin — it cropped `fig_5_12.png` to `y=2240` when that
asset was 2180 px tall.

## Regeneration

From the repository root, with the venv rebuilt per §1 of `GATE_1_PASS_1_SOURCE_MASTERY.md`:

```bash
# 1. the 17 primary assets, from the source PDF
/vercel/share/neetenv/bin/python 'notes/class 11/Ch5_MorphologyOfFloweringPlants/extract_figures.py'

# 2. the Fig. 5.12 and Fig. 5.4 composites, from those assets
/vercel/share/neetenv/bin/python 'notes/class 11/Ch5_MorphologyOfFloweringPlants/compose_horizontal_figures.py'

# 3. the Pass-2 Fig. 5.7–5.8 paired plate
/vercel/share/neetenv/bin/python 'notes/class 11/Ch5_MorphologyOfFloweringPlants/compose_layout_figures.py'
```

Step 2 must follow step 1: the composites are derived assets, and running them
against stale primaries is what produced the defect-carrying outputs this file
replaces. Both scripts assert their expected panel counts and exit non-zero if the
structure no longer matches, so a silent mis-segmentation is not possible.

## Status

The composites are **Pass-2 layout aids, not Gate 1 deliverables.** Gate 1 covers
the 17 primary assets, all `Mono: yes` / `Verified: yes` in the inventory's figure
manifest. Whether Pass 2 embeds the horizontal composite or the native plate for
Figs 5.4 and 5.12 is a layout decision for that pass; both forms are on disk, both
are monochrome, and both are reproducible. The Fig. 5.7–5.8 pairing is generated
by the chapter-local `compose_layout_figures.py` helper and is likewise reproducible.
