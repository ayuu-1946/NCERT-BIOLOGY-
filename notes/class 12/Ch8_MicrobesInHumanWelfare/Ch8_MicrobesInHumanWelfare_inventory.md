# Ch8 — Microbes in Human Welfare — Inventory

**Status: figure extraction complete (§4.4). Fact inventory and notes PDF NOT yet started.**

Source: `Chapter/class 12/Chapter 8 - Microbes in Human Welfare.pdf` (12 pages, page box 568.8 × 777.6 pt)
Extraction script: `extract_figures.py`
Assets: `assets/` — **9 PNG files** (8 numbered NCERT figures; 8.2 split into two assets)

---

## Figure manifest

Captions below are the NCERT caption text, and each was **checked against the
rendered PNG** (not merely against the figure number) per the extraction
skill's step 6 — the Ch5 `fig_5_3` failure (row existed, caption described a
different plate) is what this column guards against.

Caption strings were additionally **re-extracted verbatim from the source text
layer** and matched character-for-character against the table below, with their
own bounding boxes recorded so the crop's bottom edge could be pinned relative
to them:

| NCERT caption | Caption bbox (pt) | On page |
|---|---|---|
| `Figure 8.1 Bacteria: (a) Rod-shaped, magnified 1500X; …` | y 374.4–440.6, x 58.8–371.8 | 2 |
| `Figure 8.2 Viruses: (a) A bacteriophage; …` | y 392.7–447.8, x 282.5–525.4 | 2 |
| `Figure 8.3 (a) Colonies of bacteria growing in a petri dish; …` | y 681.9–702.7, x 141.8–429.9 | 2 |
| `Figure 8.4 Fermentors` | y 255.6–265.2, x 109.2–220.8 | 4 |
| `Figure 8.5 Fermentation Plant` | y 460.6–470.2, x 83.3–233.3 | 4 |
| `Figure 8.6 Secondary treatment` | y 271.0–280.6, x 98.4–256.6 | 6 |
| `Figure 8.7 An aerial view of a sewage plant` | y 226.4–235.9, x 298.3–509.1 | 7 |
| `Figure 8.8 A typical biogas plant` | y 354.0–363.6, x 128.9–289.7 | 8 |

**Convention followed:** captions are **excluded** from every crop (the Ch5
convention), because the notes restate captions as text. Each rect's bottom
edge therefore stops short of its caption's `y0`.

**One edge worth recording:** the Figure 8.1 caption block's bbox is 313 pt wide
(x 58.8–371.8) and so *overlaps fig_8_2c's* column in x, at y 374–441. A
word-level check of the y 368–394 band returns exactly **one** word on the whole
page — fig 8.2's own `(c)` panel letter at x 361.0, `frac=1.00` inside the rect.
The wide bbox is a multi-line block artifact, not caption text sitting in the
crop, so `fig_8_2c`'s bottom edge at y=388 is safe.

| Asset | NCERT figure | Caption (as printed) | Src page | Rect (pt) | Kind | Verified content |
|---|---|---|---|---|---|---|
| `fig_8_1.png` | Figure 8.1 | Bacteria: (a) Rod-shaped, magnified 1500X; (b) Spherical shaped, magnified 1500X; (c) A rod-shaped bacterium showing flagella, magnified 50,000X | 2 | (56, 76, 224, 372) | raster ×3 panels | Three stacked panels: red rods (a), blue cocci (b), flagellated rod (c) with in-figure labels "Flagella" and "Rod-shaped bacterium" |
| `fig_8_2a.png` | Figure 8.2 (a)+(b) | Viruses: (a) A bacteriophage; (b) Adenovirus which causes respiratory infections | 2 | (276, 80, 534, 245) | raster ×2 panels | Bacteriophage with labels "Head", "Collar", "Tail", "Plate", "Pins", "Prongs"; adenovirus icosahedron |
| `fig_8_2c.png` | Figure 8.2 (c) | ... (c) Rod-shaped Tobacco Mosaic Virus (TMV). Magnified about 1,00,000–1,50,000X | 2 | (274, 248, 548, 388) | raster | TMV rod micrograph + label "Compact Rod-shaped viruses" |
| `fig_8_3.png` | Figure 8.3 | (a) Colonies of bacteria growing in a petri dish; (b) Fungal colony growing in a petri dish | 2 | (93, 474, 540, 666) | raster ×2 panels | Bacterial colony plate (a); fungal colony plate (b) with label "Fungal colony" |
| `fig_8_4.png` | Figure 8.4 | Fermentors | 4 | (55, 80, 278, 252) | raster (photo) | Photograph of a row of industrial stainless-steel fermentor vessels |
| `fig_8_5.png` | Figure 8.5 | Fermentation Plant | 4 | (55, 277, 278, 456) | raster (photo) | Photograph of a fermentation plant interior with piping and columns |
| `fig_8_6.png` | Figure 8.6 | Secondary treatment | 6 | (54, 81, 300, 267) | raster (photo) | Photograph of an aeration tank / secondary treatment stage at a sewage works |
| `fig_8_7.png` | Figure 8.7 | An aerial view of a sewage plant | 7 | (295, 80, 517, 223) | raster (photo) | Aerial photograph showing circular settling tanks |
| `fig_8_8.png` | Figure 8.8 | A typical biogas plant | 8 | (54, 80, 370, 350) | **vector** | Cross-section schematic, labels "Gas", "Gas-holder", "( CH₄ + CO₂ + ----- )", "Dung", "Water", "Sludge", "Digester" |

**Asset count reconciliation:** 8 numbered NCERT figures → 9 asset files, because
Figure 8.2 is split into `fig_8_2a.png` (panels a+b, top of the right column) and
`fig_8_2c.png` (panel c, below it). NCERT sets these as two physically separate
plates with the 8.2 caption spanning both, and the skill requires separately
labelled sub-figures to get separate rects/assets rather than one combined crop.
No unnumbered/bonus diagrams exist in this chapter, so the denominator is **9**
everywhere it appears.

---

## Figure-label → running-text matrix (§6 Pass 1)

Every in-figure label must appear in the notes' running text. **These labels are
vector/raster artwork, not text-layer glyphs**, so they cannot be recovered by
copy-paste and must be transcribed deliberately when the chapter script is
written. This table is the checklist for that; the right column stays unchecked
until the notes PDF exists.

| Asset | In-figure labels that must appear in running text | In text? |
|---|---|---|
| `fig_8_1` | Flagella; Rod-shaped bacterium | ☐ pending notes |
| `fig_8_2a` | Head; Collar; Tail; Plate; Pins; Prongs | ☐ pending notes |
| `fig_8_2c` | Compact Rod-shaped viruses | ☐ pending notes |
| `fig_8_3` | Fungal colony | ☐ pending notes |
| `fig_8_4` | (none — unlabelled photograph) | n/a |
| `fig_8_5` | (none — unlabelled photograph) | n/a |
| `fig_8_6` | (none — unlabelled photograph) | n/a |
| `fig_8_7` | (none — unlabelled photograph) | n/a |
| `fig_8_8` | Gas; Gas-holder; CH₄ + CO₂; Dung; Water; Sludge; Digester | ☐ pending notes |

---

## Extraction gate record (three-part audit)

Run: `/vercel/share/neetenv/bin/python scratch/ch8_figs/audit.py`

| Asset | A) word grazing | B) drawings overflow | B2) raster overflow | C) border ink |
|---|---|---|---|---|
| `fig_8_1` | ok (3 words: panel letters) | ok | ok | explained (page-header motif) |
| `fig_8_2a` | ok (2 words) | explained (8.2c leader artwork) | ok | clean |
| `fig_8_2c` | ok (1 word) | explained (shared leader + caption panel) | ok | clean |
| `fig_8_3` | ok (2 words) | ok | ok | clean |
| `fig_8_4` | **vacuous** (0 words) | no drawings (raster) | ok | clean |
| `fig_8_5` | **vacuous** (0 words) | no drawings (raster) | ok | clean |
| `fig_8_6` | **vacuous** (0 words) | no drawings (raster) | ok | clean |
| `fig_8_7` | **vacuous** (0 words) | no drawings (raster) | ok | clean |
| `fig_8_8` | **vacuous** (0 words) | ok | explained (caption tint panel) | clean |

### Notes on this chapter's audit

- **Check A is vacuous for 5 of 9 assets** (`words_in_rect = 0`) and near-vacuous
  for the rest — the only text-layer words inside any rect are the panel letters
  "(a)/(b)/(c)". Every real callout label is artwork. This is precisely the trap
  the skill documents, so **B/B2/C plus the eyeball carried the gate here**; check
  A must not be read as evidence of a good crop in this chapter.
- **A `B2` raster-overflow check was added** to `scratch/ch8_figs/audit.py`
  (centre-inside membership, page furniture excluded). Standard check B is
  drawings-only and reports "no drawings (raster figure)" for figures 8.4–8.7,
  which would have left four photographic plates with **no** mechanical
  edge-clipping check at all.
- **Page furniture excluded from all extent measurements:** the full-page
  watermark `(-18.0, -38.9, 586.7, 816.5)`, the decorative band
  `(45.7, 191.1, 507.5, 652.9)`, and the page-header band
  `(-21.6, -22.0, 590.5, 75.2)`.

### Rects re-pinned during this session

| Asset | Was | Now | Why |
|---|---|---|---|
| `fig_8_1` | (82, 78, 224, 372) | (56, 76, 224, 372) | Check B overflow L23.7 + eyeball: the left-hand flagellum of panel (c) was sliced off. Dark-ink union for the band starts at x=58.3; left edge moved to 56. |
| `fig_8_3` | (148, 474, 540, 666) | (93, 474, 540, 666) | Check C reported 149 px unexplained ink on the L band + eyeball: petri dish (a) was clipped. Dark-drawings union starts at x=95.7; left edge moved to 93, still right of the page-number tab. |

Both were re-extracted and re-audited clean, then re-confirmed on a fresh
contact sheet (new filename, to defeat the `view` path cache).

---

## Remaining work for this chapter

1. Fact inventory (§6 Pass 1) — three readings of the source, frozen fact list.
2. Chapter script `Ch8_MicrobesInHumanWelfare.py` importing `neet_template.py`,
   embedding these 9 assets via `figure()`.
3. Pass 2 gate — `check_pdf.py` green.
4. Pass 3 — human content-drift review, including the figure-label matrix above.
