# Frozen Inventory — Biodiversity and Conservation (Class 12, Chapter 13)
Source: `Chapter/class 12/Chapter 13 - Biodiversity and Conservation.pdf` (13 pp) | Started: 2026-08-21 | Rows: **NOT YET FROZEN**

Tick legend: `x` = written into the script and verified present in the generated PDF.

> ## ⛔ GATE 1 STATUS: **OPEN — NOT PASSED. HARD STOP IN FORCE.**
> This session was scoped to **the figures half of Pass 1 only**, on explicit instruction. What is complete and what is not:
>
> | Pass 1 artifact | State |
> |---|---|
> | Environment (§0.2–0.3) re-established | ✅ done — venv `/vercel/share/neetenv`, CPython 3.13.11, reportlab 5.0.1 · pdfplumber OK · pymupdf 1.28.2 · Pillow 12.3.0 (matches the §0.3 reference set) |
> | Figure census (every figure in the source located) | ✅ done — **2 numbered figures, both found**; census method and negative evidence recorded below |
> | Figure extraction → mono conversion → per-figure visual verification (§4.4 Steps 1–3) | ✅ done — 2/2 assets, each opened and read, `mode == "L"`, 0 colour pixels |
> | Figure manifest | ✅ done |
> | Figure-label matrix (23 in-figure labels, harvested by reading the images) | ✅ done — **provisional IDs, see the renumbering warning** |
> | Numbered fact inventory (F001…) — three source reads | ❌ **NOT STARTED** |
> | Summary classification table | ❌ **NOT STARTED** |
> | Exercise-gap terms table | ❌ **NOT STARTED** |
> | Heading / opener row census | ❌ **NOT STARTED** |
>
> **Therefore Pass 2 may not begin.** No chapter script, no PDF, and no `check_pdf.py` run may be attempted against this chapter until the fact inventory is frozen and Gate 1 is closed. Anything claiming otherwise is a violation of §6.
>
> **⚠️ RENUMBERING WARNING (must be actioned before Gate 1 closes).** The two figure-label rows below carry provisional IDs `FIG-1` / `FIG-2` because the F-series does not exist yet. Per §6 Pass 1 the label matrix must live in the **Facts table** as rows whose wording begins `Figure labels:`, and it must exist in **exactly one place** in this file. When the facts are frozen: move both rows into the Facts table, give them real contiguous `Fnnn` IDs, and delete the provisional table — do not leave a second copy behind. A duplicated matrix makes `_extract_labels` count every label twice and turns the markdown separator into a phantom `Fig #` figure, producing check-6 FAILs that cannot be fixed by editing prose.

---

## Facts

**NOT STARTED.** To be built over three source reads per §6 Pass 1, contiguous from `F001`.

| ID | Section | Type | Exact original wording | Ticked |
|----|---------|------|------------------------|--------|
| — | — | — | *(pending Pass 1 fact inventory)* | |

## Figure-label matrix (PROVISIONAL IDs — fold into the Facts table before Gate 1 closes)

Harvested by **opening each rendered asset and reading it**, never by text extraction (§4.4). 23 label strings across 2 figures, all 23 distinct.

| ID | Fig # | Type | Figure labels (one row per figure; every in-figure label listed) | Ticked |
|----|-------|------|------------------------------------------------------------------|--------|
| FIG-1 | Fig 13.1 | Caption | Figure labels: "Invertebrates"; "Other animal groups"; "Crustaceans"; "Molluscs"; "Insects"; "Vertebrates"; "Fishes"; "Mammals"; "Birds"; "Reptiles"; "Amphibians"; "Plants"; "Mosses"; "Ferns and allies"; "Fungi"; "Angiosperms"; "Algae"; "Lichens" | |
| FIG-2 | Fig 13.2 | Caption | Figure labels: "Species richness"; "Area"; "S = CA^Z"; "Log S = log C + Z log A"; "log-log scale" | |

Per-figure label counts: Fig 13.1 = **18** (Invertebrates panel 5, Vertebrates panel 6, Plants panel 7) · Fig 13.2 = **5**. Total **23**.

**Text-layer cross-check (the §4.4 self-concealing-failure test).** `page.get_text()` on source pp. 3 and 5 returns the captions and the body prose but **zero** in-figure labels — all 23 are baked into the artwork as vector strokes. A text-extraction harvest here would have returned an empty label set and passed Gate 1 and check 6 trivially. Both rows above were read off the 300 dpi renders by eye.

## Summary classification

**NOT STARTED** — the p10–11 SUMMARY block has not been sentence-classified yet.

| Summary sentence | Classification | Folded into |
|---|---|---|
| — | *(pending)* | |

## Exercise-gap terms

**NOT STARTED** — the exercises on pp. 11–13 have not been read for assumed terms yet.

| Term/fact assumed by exercises | Explained where |
|---|---|
| — | *(pending)* |

## Figure manifest

| Fig # | Caption (verbatim) | Asset file | Source page | Mono | Verified |
|---|---|---|---|---|---|
| Fig 13.1 | "Representing global biodiversity: proportionate number of species of major taxa of plants, invertebrates and vertebrates" | `assets/fig_13_1.png` | p3 (book p218) | yes | yes |
| Fig 13.2 | "Showing species area relationship. Note that on log scale the relationship becomes linear" | `assets/fig_13_2.png` | p5 (book p220) | yes | yes |

### Figure census — how "only 2 figures" was established (negative evidence)

A two-figure chapter is exactly the kind of suspiciously thin result §4.4 says to distrust, so the census was run four independent ways and all four agree:

1. **Caption sweep** — every text block on all 13 pages beginning `Figure`: two hits only, p3 (`Figure 13.1`) and p5 (`Figure 13.2`).
2. **In-text reference sweep** — every `Fig…13.n` mention in the extracted text: `Figure 13.1` (p3 body + caption) and `Figure13.2` / `Figure 13.2` (p5 body + caption). **No reference to any 13.3 or higher exists**, so no figure is missing its caption.
3. **Vector-drawing density per page** — pages carrying a diagram stand out sharply: p3 = 93,887 drawing ops (the three pie charts), p5 = 72 (the species–area graph). Every other page sits at 4–18 ops, the same baseline as figure-free p4, so no undetected vector diagram exists.
4. **Raster-image census** — every embedded raster on every page resolves to page furniture, not content: the 2480×3508 page background and 1894×1894 `© NCERT / not to be republished` watermark (all 13 pp), the 1275×203 header band, the p1 chapter-opener QR code (275×280) and its tilted decorative thumbnail of Fig 13.1 (177×177), and the 200×1108 decorative grain strip on pp10–11.

**Consequence for §7's person-photograph check: this chapter contains no photograph of any kind, and no scientist portrait.** The p1 decorative thumbnail is a rotated miniature of Fig 13.1 itself — it is page furniture, deliberately **not** extracted, and must not be embedded as a figure.

### Per-figure verification record (§4.4 Step 3 — every figure, not a spot-check)

Both assets were extracted as **300 dpi clip renders** (`page.get_pixmap(clip=rect, dpi=300)`) rather than embedded-object grabs, because Fig 13.1 is pure vector (93,887 ops) and Fig 13.2 mixes vector strokes with vector text — an object extraction would have mangled both. Each was then `convert("L")` + `autocontrast(cutoff=1)` and **re-opened and read**.

| Check (a–f) | Fig 13.1 | Fig 13.2 |
|---|---|---|
| (a) correct figure for its caption | yes — three pie charts of taxa proportions | yes — species-richness vs area curve |
| (b) no label or leader line cropped | yes — clip taken at the rounded panel border; all 18 labels and all 4 leader arrows (Other animal groups, Crustaceans, Molluscs, Insects) fully inside | yes — clip taken at the outer tint box; both axis labels, both curve labels and the "log-log scale" in-line label fully inside |
| (c) legible at print size | yes | yes |
| (d) not a grab of a neighbouring figure/table/text | yes — caption sits below the clip (caption bbox starts y=581, clip ends y=578) | yes — caption sits below the clip (caption bbox starts y=463, clip ends y=458) |
| (e) genuinely monochrome | yes — `mode == "L"`, **0 colour pixels** sampled, greys span the full 0–255 range | yes — `mode == "L"`, **0 colour pixels** sampled, greys span 0–255 |
| (f) colour-carried distinctions survive | yes — see note below | yes — see note below |

- **Fig 13.1**, asset 1501×1434 px (≈12.7 × 12.1 cm at 300 dpi), sha256 `b4ecdb3378fd…`. The original separates pie wedges by hue; after conversion every wedge is separated by **both** a distinct grey level **and** a black boundary stroke, and every wedge is additionally named by its own text label, so no wedge identity rests on tone alone. NCERT prints **no numeric percentages inside this figure** — the proportions live in the running text (>70% animals, ≤22% plants, >70% of animals are insects), which is where the replacement chapter must carry them.
- **Fig 13.2**, asset 1117×959 px (≈9.5 × 8.1 cm at 300 dpi), sha256 `fd385c5e622f…`. The original distinguishes the two plots by colour — a blue arithmetic-scale curve and a crimson log-log straight line. After conversion they are **mid-grey (curve) vs near-black (straight line)**, still tell-apart-able, and each carries its own text label (`S = CA^Z` on the curve, `Log S = log C + Z log A` on the line, plus `log-log scale` written along the line). **Mandatory carry-over into Pass 2:** the caption and running text must state in words that the curve is the rectangular hyperbola on an arithmetic scale and the straight line is the same relationship on a log-log scale — the reader must never need the lost hue to tell which plot is which.

**Figures requiring manual attention: none.** Both extracted and converted cleanly on the first attempt; no figure was skipped, and no bad crop was accepted.

**Residual source artefact (not a defect, recorded so a later pass does not "fix" it):** the NCERT `© NCERT / not to be republished` diagonal watermark is part of the source page and therefore appears faintly across both crops — heavily over Fig 13.1, at the right edge of Fig 13.2. It obscures no label or stroke in either figure. Every previously delivered chapter in this repo carries the same artefact.

---

## Next session — resume here

1. Read the whole chapter start to finish, no note-taking (§6 Pass 1 step 1).
2. Second and third reads: build the contiguous `F001…` fact table, the heading/opener census, the summary classification and the exercise-gap terms.
3. **Fold `FIG-1`/`FIG-2` into the Facts table with real F-IDs and delete the provisional table** (see the renumbering warning at the top).
4. Only then declare Gate 1 and begin Pass 2.
