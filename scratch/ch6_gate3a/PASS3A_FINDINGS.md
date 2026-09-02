# Ch6 Anatomy of Flowering Plants — Gate 3, Pass 3(a) Visual Render Check

**Session:** Gate 3(a) for Ch6 (Pass 1 + Pass 2 inherited complete and gated; Gate 3(b) already PASS in a prior session on 2026-09-02). This session closes the one remaining gate condition — the whole-chapter visual render — and, with 3(b) already clean, closes full Gate 3.
**Method:** `pymupdf` rendered **every page** of the *final rebuilt* PDF at 150 dpi (colour) and again at a 1-bit B&W threshold (global cutoff 200). Each page inspected directly (not sampled).

## Environment re-established first (§0.2 discipline)

- `/vercel/share/neetenv/bin/python` was **absent** at session start (expected — the venv does not survive a session boundary). Rebuilt with `uv venv /vercel/share/neetenv --python 3.13` + `uv pip install reportlab pdfplumber pymupdf Pillow`.
- Verified interpreter: **Python 3.13.11 @ `/vercel/share/neetenv`; reportlab 5.0.1, pymupdf 1.28.2, Pillow 12.3.0** — matches the known-good Ch12 baseline.
- Rebuilt the PDF from the committed script (`Ch6_AnatomyOfFloweringPlants.py`, 4596 KB output), then re-ran `check_pdf.py`: **VERDICT WARN (0 fail, 1 warn)** = green gate. Checks 1–3 and 5–10 all PASS: 132/132 Facts rows ticked, 45/45 figure labels in running text, all 5 embedded images monochrome, geometry (7× A4 portrait 595×842pt), bands, 6.0pt legibility floor, 41 badge plates clear, 26 banner headings none orphaned. The lone WARN is check 4's known portrait-heuristic false positive: the substring **"photo"** inside the text of F106 ("…carry out **photo**synthesis…"), F126 and S3 ("…minerals and **photo**synthates…"). No person photograph is embedded — check 3 confirms all 5 images are monochrome and these are text rows, not images. Accepted, matching the Ch12/tracker baseline.

## Reproducibility fingerprint (Gate 3 condition 5)

Rebuilt from the final committed script: **7 pages · 5 embedded monochrome image refs · 14,034 extracted characters.** Stable across rebuilds (only the embedded creation timestamp differs byte-wise).

## Page-by-page render inspection — 7/7 pages

| Page | Contents | Layout / style | Verdict |
|---|---|---|---|
| 1 | DNA-motif title block + "Anatomy of Flowering Plants"; intro prose; keyterm bullet (Anatomy); H1 `6.1 The Tissue System`; H2 `6.1.1 Epidermal Tissue System`; epidermis/appendages/stomata bullets | Title rule clean; H1 solid-black banner + H2 grey banner both with legible reversed white text and section-number badge; keyterm filled-circle icon distinct; body bold-run emphasis consistent | CLEAN |
| 2 | keyterm (Stomatal apparatus); Fig 6.1 (a/b, bordered + captioned); NOTE box (Fig 6.1 labels verbatim); H2 `6.1.2 Ground Tissue`, `6.1.3 Vascular Tissue`; open/closed + radial/conjoint bullets; Fig 6.2 (a/b/c, bordered + captioned); NOTE box (Fig 6.2 labels); H1 `6.2 Anatomy of Dicot & Monocot Plants` | Both figures inside border box at correct aspect, not squashed; both NOTE boxes render with the `!`-circle icon + grey fill + double rule; two H2 badges + one H1 badge all legible | CLEAN |
| 3 | tail prose; H3 `6.2.1 Dicot Root`; epiblema/cortex/endodermis/pericycle/conjunctive/pith bullets; keyterm (Stele); H3 `6.2.2 Monocot Root`; polyarch bullets; Fig 6.3 (a/b dicot+monocot root, bordered + captioned); NOTE box (Fig 6.3 labels, wraps 2 lines); H3 `6.2.3 Dicot Stem` | Fig 6.3 correct aspect; multi-line NOTE box wraps cleanly inside its border; three H3 badges legible; keyterm icon consistent with p1/p2 | CLEAN |
| 4 | dicot-stem bullets (hypodermis…pith); H3 `6.2.4 Monocot Stem`; monocot-stem bullets | Section ends mid-page; trailing whitespace because Fig 6.4's `KeepTogether` block pushed it to p5 — normal pagination, not a defect | CLEAN |
| 5 | Fig 6.4 (a/b dicot+monocot stem, bordered + captioned); NOTE box (Fig 6.4 labels, wraps 3 lines); H3 `6.2.5 Dorsiventral Leaf`; epidermis/mesophyll bullets | Large 2×2 figure not squashed; 3-line NOTE box wraps inside border; H3 badge legible | CLEAN |
| 6 | mesophyll/vascular bullets; H3 `6.2.6 Isobilateral Leaf`; keyterm (Bulliform cells); bulliform/venation bullets; Fig 6.5 (a/b dicot+monocot leaf, bordered + captioned); NOTE box (Fig 6.5 labels, wraps 2 lines); Recap banner `Quick Recap` + 5 summary bullets | Fig 6.5 correct aspect; NOTE box clean; keyterm icon consistent; "Recap" badge banner legible | CLEAN |
| 7 | Exercises banner `Terms Used in the Exercises` (Q badge); Q6 heading + 3 answer bullets | Exercises `Q`-badge banner legible; chapter ends with trailing whitespace — normal final page | CLEAN |

**Result: 7/7 pages CLEAN.** Zero layout, orphaned-heading, overflow, clipping, table-run-off, squashed-figure, or misaligned-component defects.

## Cross-page style consistency (≥3 instances per element type)

Because styles are imported from the frozen `neet_template.py`, this confirms the template held rather than hunting hand-typed drift. Each recurring element type resolved to one identical signature:

- **H1 banner** (solid dark bar, reversed white bold text, section badge): p1 `6.1`, p2 `6.2` — identical height/fill/badge.
- **H2 banner** (grey bar): p1 `6.1.1`, p2 `6.1.2`, `6.1.3` — identical.
- **H3 banner** (grey bar): p3 `6.2.1`/`6.2.2`/`6.2.3`, p4 `6.2.4`, p5 `6.2.5`, p6 `6.2.6` — identical across 6 instances.
- **Section-number badge**: smallest rendered text 6.0pt (check_pdf check 2), above the 5.0pt FAIL floor and at the 6.0pt WARN band — legible.
- **Figure box + caption**: Fig 6.1–6.5 (5 instances) — identical 0.5pt border, italic centred caption below.
- **NOTE box**: p2 (×2), p3, p5, p6 (5 instances) — identical `!`-circle icon, grey fill, double rule; wraps cleanly at 2 and 3 lines.
- **keyterm bullet** (filled-circle definition icon): p1 (×2), p2, p3, p6 — identical icon at identical size.

## B&W 1-bit print-safety check

Every page re-rendered at a hard 1-bit global threshold (cutoff 200):

- **All meaning-bearing design elements survive:** heading banners keep their reversed white-on-black text; section-number badges, the `Recap` and `Q` badges stay legible; NOTE-box borders and figure-box borders survive as crisp rules; captions, figure labels, and leader lines all remain readable (labels sit **outside** the figure fill on white ground, so they never merge into it).
- **No fill lighter than `#D9D9D9` is the sole carrier of meaning anywhere** — the NOTE box's grey fill is backed by its border + `!` icon; the grey heading banners are backed by shape + reversed text; nothing relies on a light tint alone.
- **Observed artifact, not a defect:** the mid-grey tissue fills of the NCERT micrograph figures (Fig 6.2 b/c, Fig 6.4 a/b) collapse toward solid black under this deliberately aggressive global 200 cutoff. This is a property of hard 1-bit thresholding, **not** of real halftone printing — the figures are embedded as grayscale (`mode=L`, confirmed by check_pdf check 3), which a printer/photocopier reproduces via halftoning that preserves internal tone. The figure **labels and leader lines stay legible** because they live outside the fill. This matches how every prior chapter's greyscale micrographs behave under the same test and required no change.

## Verdict

**Pass 3(a): 7/7 pages inspected, 0 confirmed defects.** `check_pdf.py` green on the final rebuild; reproducibility fingerprint stable. Combined with the already-PASS Gate 3(b) (bidirectional full read, recorded in the inventory), **all five Gate 3 conditions now hold and Gate 3 is CLOSED with zero confirmed defects.** No `.py`, Fact, caption, or asset edit was required to close 3(a).
