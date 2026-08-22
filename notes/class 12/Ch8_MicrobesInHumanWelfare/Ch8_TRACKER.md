# Ch8 Microbes in Human Welfare (Class 12) — Chapter Tracker

**Status: ▶️ IN PROGRESS — Pass 1 is COMPLETE and **GATE 1 IS GREEN** (frozen inventory, 207 rows `F001`..`F207`, all counts machine-derived). Pass 2 has not started, so this chapter still does not enter the Done tally.**

**Gate 1 green does not mean the chapter is done.** There is still no
`Ch8_MicrobesInHumanWelfare.py` and no generated PDF; every row in the inventory
is **unticked**, which is the correct state before Pass 2. The next gate is
Gate 2 (`check_pdf.py` exits 0), and it cannot be judged until the script renders.

This is a per-chapter tracker; it is the detail layer under the repo-wide
`CHAPTER_TRACKER.md` and `CHAPTER_STATUS.md` roll-ups. Where those disagree with
this file about Class 12 Ch8, **this file is the one that gets re-derived from
disk and wins** — but any correction must be written into all three in the same
session (§7 rule 8, atomic closure).

**Naming hazard, recorded deliberately:** `CHAPTER_STATUS.md` already contains a
section headed `## Chapter 8 — Cell: The Unit of Life`, which is **Class 11**
Ch8. This chapter is **Class 12** Ch8. Any new roll-up entry for this chapter
must be titled `Chapter 8 (Class 12) — Microbes in Human Welfare` so the two
cannot be conflated. Assets also collide by name in conversation only —
class 11's are `fig_8_*` too — so always qualify with the class.

Nothing in this file may be updated from memory. **Re-run, don't recall.**

---

## 1. Protocol selected, and why

**12 source pages**, **6** numbered sections (§8.1–§8.6) plus Summary and
Exercises. That is **under** the big-chapter threshold, so Ch8 runs the
**single-pass protocol**, not Ch5's `1a`/`1b` split:

    1 → [GATE 1] → 2 → [GATE 2] → 3 → [GATE 3] → deliver

The `-S` / `-H` / `-O` / `-F` / `-Z` sweep split still applies — each sweep is
the sole deliverable of the session that closes on it. Folding a sweep into
another is the Ch9 D9 failure mode.

`-F` (figures) ran first here because it is fully independent of the prose
sweeps: it reads artwork geometry, not sentences.

### Verified source map

| Item | Value | Verified how |
|---|---|---|
| Source PDF | `Chapter/class 12/Chapter 8 - Microbes in Human Welfare.pdf` | opened by machine |
| Pages | **12** | `doc.page_count` |
| Page box | **568.8 × 777.6 pt** | `doc[0].rect` |
| Figure-bearing pages | **2, 4, 6, 7, 8** | `Figure 8.\d+` regex scan of every page's text |
| Numbered figures | **8** (8.1 … 8.8) | same scan; no 8.9+ exists |
| Assets produced | **9** | 8.2 splits into `8_2a` + `8_2c` |

### Verified section map (banner page located by machine, not guessed)

The **contents list on p1 repeats all six section titles**, so a naive scan
double-counts every banner. The page below is the **in-body banner**, which is
the one a sweep follows.

| Section | Banner page |
|---|---|
| §8.1 Microbes in Household Products | 3 |
| §8.2 Microbes in Industrial Products | 3 |
| §8.2.1 Fermented Beverages | 4 |
| §8.2.2 Antibiotics | 4 |
| §8.2.3 Chemicals, Enzymes and other Bioactive Molecules | 5 |
| §8.3 Microbes in Sewage Treatment | 5 |
| §8.4 Microbes in Production of Biogas | 7 |
| §8.5 Microbes as Biocontrol Agents | 8 |
| §8.6 Microbes as Biofertilisers | 9 |
| SUMMARY | 10 |
| EXERCISES | 11 |

**6 numbered sections + 3 sub-sections = 9 heading banners**, plus the chapter
title, Summary and Exercises. p1 is the opener/contents page and p12 is the
tail — the prose sweep runs **pp. 3–11**.

---

## 2. Session ledger

| # | Session | Scope | State | Sole deliverable |
|---|---|---|---|---|
| 1 | `1-F` | **whole chapter** figures | ✅ **done** | 9 verified mono assets + `extract_figures.py` with hand-pinned rects + figure manifest + label matrix — **9 assets / 17 labels** |
| 2 | `1-S` | prose facts, steps 1–3 | ✅ **done** | prose/caption/term/name/number/question/crossref rows — **169 rows** (198 Facts rows minus 15 heading, 14 opener) |
| 3 | `1-H` | headings only | ✅ **done** | heading rows — **15** (9 numbered + 6 unnumbered) |
| 4 | `1-O` | section openers only | ✅ **done** | opener rows — **14** |
| 5 | `1-Z` | steps 7–9, freeze | ✅ **done** | 4 exercise-gap terms, 18 summary sentences classified (16 BODY-PRESENT / 2 SUMMARY-UNIQUE), inventory frozen at **207 rows** |

**All five sessions ran and each reported its own machine-derived count**, which
is itself a Gate 1 criterion. Every count above was re-parsed from the finished
inventory file, not tallied by hand — see "Gate 1 validation" below.

---

## 3. What is actually on disk

    notes/class 12/Ch8_MicrobesInHumanWelfare/
      Ch8_MicrobesInHumanWelfare_inventory.md   FROZEN — 207 rows F001..F207, all unticked
      Ch8_TRACKER.md                            this file
      extract_figures.py                        hand-pinned rects + 4-part crop gate
      assets/                                   9 verified mono PNGs

No `Ch8_MicrobesInHumanWelfare.py` and no generated `.pdf`. **Correct at this
point:** Pass 2 has not started.

A `__pycache__/extract_figures.cpython-313.pyc` was created by the audit
importing the extraction module and was **deleted** before commit — bytecode is
not a deliverable under §0.5, and Ch3 previously shipped two such files by
mistake.

Working aids **outside** the chapter folder, not deliverables (§0.5 permits a
scratch directory):

    scratch/ch8_figs/grid/p{02,04,06,07,08}.png   110 dpi grid overlays used to hand-pin the rects
    scratch/ch8_figs/audit.py                    the four-part crop gate
    scratch/ch8_figs/contact_sheet_*.png         visual confirmation sheets
    scratch/ch8_figs/probe_81_top.png            the y 58-100 strip that identified the page-header motif

### Machine-derived asset state

Re-derived this session, not recalled:

| Metric | Value |
|---|---|
| Asset files | **9** (`fig_8_1`, `fig_8_2a`, `fig_8_2c`, `fig_8_3`, `fig_8_4`, `fig_8_5`, `fig_8_6`, `fig_8_7`, `fig_8_8`) |
| Colour mode | **9/9 `mode=L`** |
| Render DPI | 300, `ImageOps.autocontrast(cutoff=1)` |
| Numbered figures covered | **8/8** — 8.1 … 8.8, none missing |
| Split figures | **Figure 8.2 → 2 assets** (`a`+`b` panels together; `c` separate) |
| Unnumbered/bonus plates | **0** — none exist in this chapter, so the denominator is 9 everywhere |
| Vector vs raster | 1 vector schematic (8.8); 8 raster/micrograph plates |
| Facts rows | **198** (`F001`..`F198`) + **9** figure-label rows (`F199`..`F207`) = **207** |

Re-derive with:

    /vercel/share/neetenv/bin/python - <<'EOF'
    import importlib.util, os
    from PIL import Image
    s=importlib.util.spec_from_file_location("ef","notes/class 12/Ch8_MicrobesInHumanWelfare/extract_figures.py")
    ef=importlib.util.module_from_spec(s); s.loader.exec_module(ef)
    print("rects pinned:", len(ef.FIGS))
    for fid,pno,rect in ef.FIGS:
        p=os.path.join(ef.OUT_DIR,f"fig_{fid}.png"); im=Image.open(p)
        print(f"  fig_{fid}: p{pno} {rect} {im.size} mode={im.mode}")
    EOF

### Environment

`/vercel/share/neetenv` was **absent** at session start — the expected §0.2
state, checked before anything else — and was rebuilt: CPython 3.13,
pymupdf, Pillow, numpy, all import-verified under that interpreter. `numpy` is
required by crop-gate check C. **Every future session re-checks
`ls /vercel/share/neetenv/bin/python` first**; sandboxes lose it.

---

## 4. The `1-F` sweep — what was done and what it cost

Followed `skills/ncert-figure-extraction/SKILL.md`: render 110 dpi grid
overlays → read each rect off the grid by eye → **cross-check numerically
against page geometry** → pin in `extract_figures.py` with a comment recording
what pinned it → run the mechanical gate → look at every PNG.

### This chapter is the skill's worst case for check A

**Check A (text-layer word grazing) is vacuous for 5 of 9 assets and
near-vacuous for the other 4.** `page.get_text("words")` returns **zero** words
inside the rects for figures 8.4–8.7, and only the `(a)/(b)/(c)` panel letters
for the rest. Every real callout — `Flagella`, `Head`, `Collar`, `Tail`,
`Plate`, `Pins`, `Prongs`, `Gas`, `Sludge`, `Digester` — is **drawn as
artwork**, not set as text.

So an audit built on check A alone would have reported this entire chapter clean
while shipping clipped plates. It nearly did: **the first pinning of `fig_8_1`
and `fig_8_3` both passed check A and were both visibly broken.**

### A fourth check was added: B2, raster-extent overflow

Standard check B measures `get_drawings()` extents, and correctly reports
`no drawings (raster figure)` for figures **8.4, 8.5, 8.6 and 8.7** — four
photographic plates that consequently had **no mechanical edge-clipping check at
all**. `scratch/ch8_figs/audit.py` therefore adds **B2**, the same
centre-inside overflow test run over `get_image_info()` boxes.

**Page furniture must be excluded from every extent measurement** or it swallows
the result — this chapter carries three such rects on every page:

| Rect (pt) | What it is |
|---|---|
| `(-18.0, -38.9, 586.7, 816.5)` | full-page watermark |
| `(45.7, 191.1, 507.5, 652.9)` | decorative band |
| `(-21.6, -22.0, 590.5, 75.2)` | page-header band (leaf/logo motif) |

Page 2 additionally carries **thousands of 1-px gradient slivers**; any raster
enumeration must filter on a minimum dimension or the output is unreadable.

### Rects re-pinned, with the reason

| Asset | Was | Now | Found by | Why |
|---|---|---|---|---|
| `fig_8_1` | `(82, 78, 224, 372)` | `(56, 76, 224, 372)` | check B overflow `L23.7` **+ eyeball** | the left-hand flagellum of panel (c) was sliced off; dark-ink union for the band starts at x=58.3 (the `(0.96,0.97,0.92)` wash at x=58.7 is background, not ink) |
| `fig_8_3` | `(148, 474, 540, 666)` | `(93, 474, 540, 666)` | check C `149px` L-band **+ eyeball** | petri dish (a) was clipped at the left; dark-drawings union starts at x=95.7. New edge is still right of the orange "150" page tab at x 53.8–78.5 |

Both were re-extracted, re-audited clean, and re-confirmed on a **fresh** contact
sheet — the `view` tool caches by path, so the sheet filename carries a
timestamp.

### Gate results after re-pinning

**A clean · B clean or explained · B2 clean or explained · C clean or explained**,
and all 9 PNGs opened. Three hits are **explained and deliberately accepted** —
they are recorded in the rect comments in `extract_figures.py` so a future
session does not "fix" them:

| Asset | Hit | Disposition |
|---|---|---|
| `fig_8_1` | C, `T:46px@(98.7,70.0)` | the **page-header leaf/logo motif** ending at y=75.2. Rendering the y 58–100 strip confirms panel (a)'s own border begins below it. The top edge at y=76 is correct; **do not raise it** |
| `fig_8_2a` | B, `B68.3` | rect `(273.4,143.1,326.1,313.3)` — the tall leader/bracket artwork belonging to **fig 8.2(c) below**, a deliberately separate asset |
| `fig_8_2c` | B, `T48.9 / B52.9` | the shared leader line running up into panels (a)/(b), and the **caption's tinted panel** below (to y=440.9) |
| `fig_8_8` | B2, `B4.1` | the **caption's own tinted background raster** (to y=354.1). Including it would drag the caption text into the crop; check B (the actual diagram) is clean at that edge |

**Do not re-raise these four.** Each is either page furniture, a neighbouring
figure's artwork, or a caption background — none is clipped figure content.

---

## 5. Gate 1 validation — how it was judged

Gate 1 is a **machine-checked** gate, so nothing below is a claim; each line is
the output of re-parsing the finished inventory file.

| Criterion | Result |
|---|---|
| Total rows / ID contiguity | 207 rows, `F001`..`F207`, contiguous, 0 duplicates |
| Facts vs matrix split | 198 + 9 |
| `check_pdf.py._extract_labels` run against the inventory | **17 labels across 5 figure rows**; **no doubling**; **no phantom `Fig #` row** |
| Heading rows | 15 = 9 numbered + 6 unnumbered |
| Opener rows | 14 |
| Caption rows | 8 (one per numbered figure) |
| `Type` vocabulary | 10 values, all lowercase, no strays |
| Summary sentences | 18 = 16 BODY-PRESENT + 2 SUMMARY-UNIQUE, both folded into body rows |
| Exercise-gap terms | 4, each with a planned home |
| Manifest `Mono`/`Verified` | 9/9 `yes yes` |

Re-derive with:

    /vercel/share/neetenv/bin/python - <<'EOF'
    import re, importlib.util, collections
    p="notes/class 12/Ch8_MicrobesInHumanWelfare/Ch8_MicrobesInHumanWelfare_inventory.md"
    txt=open(p).read()
    rows=[[c.strip() for c in l.strip().strip("|").split("|")]
          for l in txt.splitlines() if l.strip().startswith("|")]
    rows=[r for r in rows if len(r)>=4 and re.fullmatch(r"F\d{3}", r[0])]
    n=sorted(int(r[0][1:]) for r in rows)
    print("rows", len(rows), "contiguous", n==list(range(1,len(n)+1)))
    print(collections.Counter(r[2] for r in rows))
    s=importlib.util.spec_from_file_location("cp","check_pdf.py")
    cp=importlib.util.module_from_spec(s); s.loader.exec_module(cp)
    labs=cp._extract_labels(txt)
    print("labels", len(labs), "figs", len({f for f,_ in labs}))
    EOF

### Two formatting traps this chapter hit, recorded so they are not re-introduced

1. **The prompt's own suggested matrix header is a phantom-label generator.** A
   header cell reading `Figure labels (one row per figure; every in-figure label
   listed)` **matches `_extract_labels`' own regex**, has no quoted strings, and so
   falls through to the semicolon fallback — manufacturing two phantom labels
   (`(one row per figure`, `every in-figure label listed)`) that no running text
   could ever satisfy. The header column is therefore worded **`Label row
   wording`**. Do not "restore" the documented wording.
2. **Unlabelled figures must not get a `Figure labels: (none)` row**, for the same
   reason. The four photographic plates (8.4–8.7) carry rows worded
   `No in-figure labels — ...`, which the parser skips by design, so each figure
   still has a row while contributing 0 labels. This is why the parse reports
   **9 matrix rows but 5 figure rows / 17 labels**, and the discrepancy is
   intentional.

The old duplicate label table was also **removed**: the inventory previously
restated the matrix as a second, 3-column table. It happened to be invisible to
the parser (fewer than 4 cells), but the §6 rule is one location only, and a later
edit adding a column would have silently doubled every label.

---

## 6. NEXT SESSION — Pass 2, write the script

**Gate 1 is green, so Pass 2 may begin.** Deliverable:
`Ch8_MicrobesInHumanWelfare.py`, importing `neet_template.py`, written **linearly
from the frozen inventory** in Content Order, with each row ticked in the
inventory file *as it is written* — not reconciled afterwards.

Binding rules for that session:

1. **Rebuild `/vercel/share/neetenv` first** (§0.2) — it is reliably absent, and a
   missing interpreter is this workflow's most-misdiagnosed failure.
2. **Do not re-open Pass 1.** The inventory is frozen. If a genuine omission
   surfaces, add the row *and* fix every restatement of every affected count in the
   same edit, then re-run the parse.
3. **All 17 in-figure labels must appear in running text** — `check_pdf.py` check 6
   fails the build otherwise. They are artwork and cannot be copy-pasted from the
   source PDF; transcribe them from rows `F199`..`F207`.
4. **Banned glyphs (check 5)** bite this chapter specifically: write `CO2`, `CH4`,
   `H2`, `B12` and `100 C` as plain ASCII, never as subscripts or with a degree
   sign. The inventory rows are already written that way — copy them verbatim.
5. **Embed all 9 assets via `figure()`**; the denominator is 9 assets / 8 figure
   numbers, because Figure 8.2 is split. Report either with its basis.
6. The 4 exercise-gap NOTE boxes must be **visibly marked as beyond the body text**,
   so exercise-support content is never mistaken for an NCERT sentence.

Then Gate 2 (`check_pdf.py` exits 0) → Pass 3 (bidirectional content cross-check +
visual render check) → Gate 3 → deliver.

---

## 6. Reusable procedure

`skills/ncert-figure-extraction/SKILL.md`. Two findings from this chapter are
worth folding back into it if it is ever revised:

1. **Check B is blind to raster-only figures**, and NCERT chapters like this one
   are majority-raster. A **B2 raster-extent check** should be part of the
   standard gate, not a per-chapter addition.
2. **Near-white vector fills must be excluded** when deriving a "dark ink"
   extent. Panel background washes (here `(0.96,0.97,0.92)`) otherwise appear as
   real overflow and push a rect outward into page furniture.
