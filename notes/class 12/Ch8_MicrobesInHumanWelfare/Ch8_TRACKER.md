# Ch8 Microbes in Human Welfare (Class 12) — Chapter Tracker

**Status: ✅ DONE — All three passes COMPLETE. **GATE 1 GREEN** (frozen inventory, now 209 rows: `F001`..`F207` from the 1-Z freeze plus `F055a` and `F085a` added by Pass 3). **GATE 2 GREEN** (`check_pdf.py` exit 0, 0 fail / 1 inspected WARN, **200/200 Facts rows ticked**, 12-page A4 PDF, **content-deterministic** rebuild — same text SHA-256, timestamps aside). **GATE 3 GREEN** (bidirectional read done both directions; 3 defects found and fixed; visual render check done on the reflowed pages). This chapter now enters the Done tally.**

**Gate 3 confirmed the rule again.** Gate 2 was green on a PDF that was missing
two NCERT sentences and contained one self-contradicting statement. Gate 2 is a
*mechanical* gate: it proves the rows were written and the labels appear
somewhere in the text, not that they are correct, in the right place, or free of
drift. Every chapter in this repo that ran Pass 3 found real defects **after** a
green Gate 2 — Ch9 found 3, Ch10 found 3, Ch12 found 4, Ch13 found 7, and **Ch8
found 3**. Critically, **2 of Ch8's 3 came from direction 2 only** (source ->
inventory) and were structurally invisible to direction 1, because a row that
was never created cannot be reported as missing.

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
| 2 | `1-S` | prose facts, steps 1–3 | ✅ **done** | prose/caption/term/name/number/question/crossref rows — **169 rows** (the 198 Facts rows *at the freeze* minus 15 heading, 14 opener) |
| 3 | `1-H` | headings only | ✅ **done** | heading rows — **15** (9 numbered + 6 unnumbered) |
| 4 | `1-O` | section openers only | ✅ **done** | opener rows — **14** |
| 5 | `1-Z` | steps 7–9, freeze | ✅ **done** | 4 exercise-gap terms, 18 summary sentences classified (16 BODY-PRESENT / 2 SUMMARY-UNIQUE), inventory frozen at **207 rows** |
| 6 | Pass 2 | script + PDF, Gate 2 | ✅ **done** | `Ch8_MicrobesInHumanWelfare.py` + 12-page PDF, 198/198 Facts rows ticked, `check_pdf.py` exit 0 (0 fail / 1 inspected WARN) |
| 7 | Pass 3 session 1 | 3(a) visual + 3(b) direction 1 | ✅ **done** | 12/12 PDF pages and 9/9 assets inspected; all 207 rows checked present-and-faithful in the PDF |
| 8 | Pass 3 session 2 | 3(b) direction 2, Gate 3 | ✅ **done** | source pp. 3–11 read start to finish under the grep prohibition; **3 defects found and fixed**; 2 rows added (`F055a`, `F085a`) → **209 rows / 200 Facts**; Gate 3 CLOSED |
| 9 | Closure | atomic doc reconciliation | ✅ **done** | Gate 2 re-verified from disk (200/200 ticked, exit 0); all three trackers brought onto the post-Pass-3 counts in one edit |
| 10 | Gate 1 re-derivation (2026-08-24) | audit only — no content authority | ✅ **done** | venv rebuilt (absent again at session start); `scratch/ch8_gate1_reaudit/audit.py` re-parsed every Gate 1 number from the frozen file, trusting nothing written in it — **52 / 52 assertions green, 0 corrections to this chapter**; `check_pdf.py` re-run from disk (0 fail / 1 inspected WARN, 200/200 ticked, 17/17 labels in text). One defect found **outside** the chapter: `CHAPTER_TRACKER.md`'s Class 12 footer read 5 / 13 against a machine-counted 6 / 13 — fixed |

**All nine build sessions ran and each reported its own machine-derived count**, which
is itself a Gate 1 criterion. Every count above was re-parsed from the finished
inventory file, not tallied by hand — see "Gate 1 validation" below.

**Row counts moved at Pass 3 and the ledger says so on purpose.** Sessions 1–6
worked against a **207-row / 198-Facts** inventory; direction 2 then found two
genuinely uninventoried NCERT sentences, so the live counts are **209 rows /
200 Facts** from session 8 onward. Historical rows above are left at the numbers
that were true when they ran, and are marked *at the freeze* where they restate a
total. Anything describing the **current** state reads 209/200.

---

## 3. What is actually on disk

    notes/class 12/Ch8_MicrobesInHumanWelfare/
      Ch8_MicrobesInHumanWelfare_inventory.md   FROZEN — 209 rows (F001..F207 + F055a + F085a), 200/200 Facts rows TICKED
      Ch8_MicrobesInHumanWelfare.py             51,656 B — the Pass 2 script
      Ch8_MicrobesInHumanWelfare.pdf            2,020,000 B — 12 pp A4, 9 embedded mono images
      Ch8_TRACKER.md                            this file
      extract_figures.py                        hand-pinned rects + 4-part crop gate
      assets/                                   9 verified mono PNGs

The script and PDF now exist, which is what made Gate 2 judgeable. Rebuild with:

    cd /vercel/share/v0-project && /vercel/share/neetenv/bin/python \
      "notes/class 12/Ch8_MicrobesInHumanWelfare/Ch8_MicrobesInHumanWelfare.py"

**`check_pdf.py` takes the chapter folder, not two file paths** — passing the PDF
and the inventory as separate positional arguments makes argparse reject the
second one, and the shell then reports `EXIT=0` from `echo`, which reads exactly
like a pass. This wasted a cycle in the Gate 2 session. The correct invocation is:

    /vercel/share/neetenv/bin/python check_pdf.py "notes/class 12/Ch8_MicrobesInHumanWelfare"

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
| Facts rows | **200** (`F001`..`F198` + `F055a` + `F085a`) + **9** figure-label rows (`F199`..`F207`) = **209** — was 198 + 9 = 207 until the two Pass 3 additions |

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
| Total rows / ID contiguity | 207 rows, `F001`..`F207`, contiguous, 0 duplicates *(at the freeze; **209** now, `F055a`/`F085a` added at Pass 3)* |
| Facts vs matrix split | 198 + 9 *(at the freeze; **200 + 9** now)* |
| `check_pdf.py._extract_labels` run against the inventory | **17 labels across 5 figure rows**; **no doubling**; **no phantom `Fig #` row** |
| Heading rows | 15 = 9 numbered + 6 unnumbered |
| Opener rows | 14 |
| Caption rows | 8 (one per numbered figure) |
| `Type` vocabulary | 10 values, all lowercase, no strays |
| Summary sentences | 18 = 16 BODY-PRESENT + 2 SUMMARY-UNIQUE, both folded into body rows |
| Exercise-gap terms | 4, each with a planned home |
| Manifest `Mono`/`Verified` | 9/9 `yes yes` |

### Gate 1 re-validation (independent, later session)

Gate 1 was **re-verified from disk** in a later session rather than trusted from
this file, per the §0.2 rule that a handoff's account of *why* is a hypothesis.
`/vercel/share/neetenv` was absent (the expected state) and was rebuilt to the
same known-good versions: reportlab 5.0.1, pymupdf 1.28.2, Pillow 12.3.0,
numpy 2.5.2 on CPython 3.13.

All 14 machine criteria re-ran **PASS** — 207 rows, `F001`..`F207` contiguous,
0 duplicates, 198 facts + 9 matrix rows (**the pre-Pass-3 state; 209 rows / 200
facts after `F055a` and `F085a`**), 15 heading / 14 opener / 8 caption rows,
`Type` vocabulary 10 values all lowercase, 17 labels across 5 parsed figure rows,
no doubling, no phantom `Fig #` row, all rows unticked. The 9 numbered in-body
banners were re-derived from the source PDF independently and match the section
map above; 9/9 assets re-confirmed `mode=L` on disk.

**One real defect was found and fixed — a count restatement, not a row.** The
inventory's *Count derivation* section and its *Gate 1 checklist* both claimed
`_extract_labels` confirmed "**9** figure rows / 17 labels". The parser returns
**5** figure rows, because the four `No in-figure labels` rows (`F203`-`F206`) are
invisible to it by design. The inventory's own matrix note (`across 5 labelled
assets`) and this tracker both already stated it correctly, so the file
contradicted itself — precisely the "header disagrees with its own table" failure
step 10 exists to prevent. Both restatements now read "17 labels across 5 parsed
figure rows (9 matrix rows; 4 unlabelled contribute 0 by design)", the post-edit
stale-claim sweep returned zero live survivors, and the full re-parse was re-run
against the finished file. **No frozen row was touched and no count of rows,
headings, openers, labels or assets changed** — the underlying inventory was
correct throughout; only its description of the parser's output was wrong.

### Gate 1 re-derivation #2 (2026-08-24) — post-Pass-3 state, clean

The re-validation above ran against the **pre-Pass-3** inventory (207 rows / 198
Facts, all rows unticked). It has now been re-run against the **current** file, so
the post-Pass-3 counts are independently verified too and no criterion rests on a
verdict carried forward across the Pass 3 edits.

Audit: `scratch/ch8_gate1_reaudit/audit.py`, written fresh rather than reused, and
deliberately structured as *derived vs claimed* on every line so a green run is
evidence and not a restatement. It imports `check_pdf.py`'s real `_extract_labels`
instead of reimplementing it. `/vercel/share/neetenv` was **absent again** at
session start — the third consecutive session to find it gone, which is the
expected state, not an anomaly — and was rebuilt first, before any diagnosis
(reportlab 5.0.1, pymupdf 1.28.2, Pillow 12.3.0 on CPython 3.13.11).

**Result: 52 / 52 assertions PASS, zero corrections to this chapter.** Verified
independently: 200 Facts + 9 matrix = 209 rows; `F001`..`F207` contiguous, zero
gaps, zero duplicates; `F055a`/`F085a` the only suffixed IDs; **0 unticked**; type
census `fact 97, name 29, term 19, heading 15, opener 14, caption 8, question 7,
crossref 6, number 5`, all inside the 10-value lowercase vocabulary; 17 labels
across 5 parsed figure rows with no doubling and no phantom `Fig #` row, and the
per-figure distribution `8.1:2, 8.2(a):6, 8.2(c):1, 8.3:1, 8.8:7` matching the
matrix row by row; 18 summary sentences (16 + 2) with `F195`/`F196` confirmed to
exist as real rows; 4 exercise-gap terms each with a home; 9 manifest rows all
`Mono: yes`/`Verified: yes`, filenames matching the 9 PNGs on disk, all `mode=L`.
Both censuses were checked against *their own lists and the rows*: heading
`9 + 6 = 15` and opener `14`, with every census ID confirmed to be a real row of
that type in both directions (no census-only IDs, no row-only IDs). `check_pdf.py`
re-run from disk: 0 fail, 1 accepted WARN, 200/200 ticked, 17/17 labels in text.

**The Ch12 label trap is documented in this chapter and did not fire.** Executing
the parser is the only way to know that, and it was executed — a warning carried
forward describes a risk, never a finding.

**The one defect found was outside this chapter.** `CHAPTER_TRACKER.md`'s Class 12
footer read "5 / 13" while its own header read "6/13"; counting the ✅ rows returns
**6**, so Ch8's own closure had been recorded in the header and in its row but never
propagated to the footer. Fixed with the corrected value plus a history note, and
the roll-ups were re-derived by parsing rows per class section rather than
incremented: Class 11 **6 / 19**, Class 12 **6 / 13**, total **12 / 32**. This is
exactly the silent-drift class the closure rules predict, and it appeared without
anyone touching Ch8.

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

## 6. Gate 2 — how it was judged (CLOSED, green)

Pass 2 ran as specified: `Ch8_MicrobesInHumanWelfare.py` was written **linearly
from the frozen inventory** in Content Order, importing `neet_template.py`, with
rows ticked **as they were written** rather than reconciled afterwards. All six
binding rules carried over from the Pass 1 handoff were honoured — the
interpreter was rebuilt first, Pass 1 was never re-opened, no frozen row was
edited, all 17 artwork labels were transcribed from `F199`..`F207`, the banned
glyphs were written as plain ASCII, all 9 assets were embedded, and the 4
exercise-gap NOTE boxes are visibly marked as beyond the body text.

### Full check results

| # | Check | Result |
|---|---|---|
| 1 | Footer/header band | **PASS** — no text in the top/bottom margin bands |
| 2 | Legibility floor | **PASS** — smallest rendered text **6.0pt** (fail <5.0, warn <6.0) |
| 3 | Grayscale-only images | **PASS** — all **9** embedded images monochrome |
| 4 | No person photograph | **WARN** — 9 heuristic hits, all inspected; see below |
| 5 | Banned glyphs | **PASS** — no Unicode arrows, sub/superscripts, Greek or emoji |
| 6 | Figure-label coverage | **PASS** — **17/17** labels fully in text, 0 partial, 0 missing |
| 7 | Frozen inventory ticked | **PASS** — all **198** Facts rows ticked at Gate 2; **200/200** on the post-Pass-3 rebuild, re-verified from disk at the closure session |
| 8 | Page geometry | **PASS** — all **12** pages A4 portrait 595x842pt |
| 9 | Orphaned headings | **PASS** — **37** banner headings all followed by content |
| 10 | Badge/banner collision | **PASS** — **88** filled plates all clear of neighbours |

**VERDICT: WARN — 0 fail, 1 warn, exit 0. Gate 2 is green.**

### The check-4 WARN is accepted, with a decision recorded

Check 4 is titled "scientist profile is text-only" and greps the manifest for
portrait/photo wording. It fired **9 times**: on `F050` (a crossref whose text
contains the word "photograph"), on `F203`–`F206` (the four
`No in-figure labels — unlabelled photograph …` rows), and on the four
`raster photograph` rows in the figure manifest. **Every one of these is the
check matching the literal word "photograph", not detecting a face.**

All four plates were opened and looked at:

| Asset | What it actually shows | People? |
|---|---|---|
| `fig_8_4` | fermentor vessels | **none** |
| `fig_8_5` | fermentation plant, wide industrial shot | **two incidental workers** — one on the walkway, one crouched at the base |
| `fig_8_6` | aeration tank | **none** |
| `fig_8_7` | aerial view of a sewage plant | **none** |

`fig_8_5` was escalated rather than decided silently, because the hard rule says
"no photograph of a person" while the check's own title scopes it to a *scientist
profile*. **The user's explicit decision is to keep it embedded**: it is NCERT
Figure 8.5 itself, the workers are incidental scale-figures in an industrial
photograph rather than a portrait, and dropping it would break the 9-asset
denominator that every count in this tracker rests on.

**Do not "fix" this WARN.** Removing `fig_8_5`, or rewording `F050`/`F203`–`F206`
to dodge the grep, would silently falsify the figure census. The WARN is expected
on every future run of this chapter.

### Binding rules that were honoured, kept for reference

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

All six were satisfied. Gate 2 is closed.

---

## 7. Gate 3 — how it was judged (CLOSED, green)

**Pass 3 is complete and Gate 3 is GREEN. There is no next session for this
chapter.** This section used to be a forward-looking "NEXT SESSION" brief; it was
rewritten at closure because a stale instruction is more dangerous than a stale
number — numbers get re-derived, instructions get obeyed.

### 3(a) visual render check — done

All **12 PDF pages** and all **9 assets** were opened and looked at. No clipped
badges, no orphaned captions, no plate/banner collisions, no figure rendered at
unreadable scale. `check_pdf.py` checks 9 and 10 cover only the mechanical subset
and were green independently (37 banners followed by content, 88 plates clear).

### 3(b) bidirectional content cross-check — done, both directions

- **Direction 1** — all **207** then-existing inventory rows were confirmed
  present in the PDF *and* saying what the row says. A ticked box only proves
  someone believed they wrote it, so each was read.
- **Direction 2** — the **source PDF, pp. 3–11, read start to finish** under an
  explicit **grep prohibition**, with a per-section reading claim recorded. This
  is the direction that found every defect below, as it did in Ch12 and Ch13.

### The 3 confirmed defects, all fixed

| # | Kind | What was wrong | Fix |
|---|---|---|---|
| D1 | **UNINVENTORIED** | the household-scale curd/idli/dosa framing sentence was never inventoried | row **`F055a`** added, prose written into §8.1 |
| D2 | **UNINVENTORIED** | NCERT's sewage-disposal question ("where is this huge quantity of sewage … disposed off daily?") plus its "you can understand why" nudge | row **`F085a`** added, rendered as prose in §8.3 |
| D3 | **DRIFTED** | the Exercise-Q11 lead-in said the samples were "collected before water treatment", which contradicts the table's own secondary-effluent row | lead-in rewritten to match the data |

0 MISSING · 0 FABRICATED. **Both additions are a real Pass 1 gap and are logged
as such — never back-dated into the freeze.** They took the inventory from 207 to
**209 rows** and the Facts count from 198 to **200**. Both are the same family
Ch13 hit seven times: NCERT's rhetorical questions and framing sentences, which
read as connective tissue and get skipped by a sweep looking for facts.

### Post-fix verification

- `check_pdf.py "notes/class 12/Ch8_MicrobesInHumanWelfare"` → **exit 0, 0 fail,
  1 WARN**, the same inspected check-4 portrait WARN as §6. Re-run **from disk at
  the closure session**, not trusted from the handoff.
- **200/200 Facts rows ticked** on the post-fix rebuild (re-parsed, not recalled).
- All three fixes re-confirmed in the rebuilt PDF's text layer, and pages 5, 6 and
  12 — the three that reflowed — re-rendered and re-inspected.
- **Reproducibility:** rebuilt twice more; both builds give the **same 12 pages,
  same page count and the same text-layer SHA-256** (`1fb7a3b1…`) as the committed
  PDF, at an identical file size. Only the embedded PDF timestamps/IDs differ, so
  the build is **content-deterministic, not byte-deterministic** — a rebuild will
  always show as a modified binary in `git status`. That is expected; do not chase
  it as a defect.

### Standing facts for anyone who reopens this chapter

1. The **check-4 WARN is permanent and accepted** (§6). Do not remove `fig_8_5`
   and do not reword `F050`/`F203`–`F206` to dodge the grep.
2. The live counts are **209 rows / 200 Facts / 9 figure-label matrix rows**.
   Anything still saying 207/198 is describing the pre-Pass-3 freeze and should
   say so explicitly.
3. The asset denominator is **9 assets / 8 figure numbers** (8.2 is split). Report
   either one with its basis.
4. If a further defect ever surfaces, add an `a`-suffixed row, fix **every**
   restatement of **every** affected count in the same edit, re-run the parse, and
   reconcile this file, `CHAPTER_TRACKER.md` and `CHAPTER_STATUS.md` together.

**Gate 3 is closed. All three gates are green, so the chapter is delivered and
now counts in the Done tally.**

---

## 8. Reusable procedure

`skills/ncert-figure-extraction/SKILL.md`. Two findings from this chapter are
worth folding back into it if it is ever revised:

1. **Check B is blind to raster-only figures**, and NCERT chapters like this one
   are majority-raster. A **B2 raster-extent check** should be part of the
   standard gate, not a per-chapter addition.
2. **Near-white vector fills must be excluded** when deriving a "dark ink"
   extent. Panel background washes (here `(0.96,0.97,0.92)`) otherwise appear as
   real overflow and push a rect outward into page furniture.
