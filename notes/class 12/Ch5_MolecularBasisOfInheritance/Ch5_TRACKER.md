# Ch5 Molecular Basis of Inheritance — Chapter Tracker

**Status: ▶️ IN PROGRESS — PASS 1 COMPLETE; GATE 1 CLOSED. Pass 2 not started. GATE 2 AND GATE 3 NEVER RUN.**
**All 9 Pass-1 ledger entries complete. 0 of 646 frozen inventory rows ticked. No script or PDF; 18 verified mono assets.**

**Post-merge crop re-verification (2026-08-22, after PR #85).** Two rects were still clipping their plates and have been re-pinned and re-rendered: `fig_5_16` (`86,78,422,502` → `57,81,494,502`) and `fig_5_2` (`108,80,526,272` → `86,80,519,280`). Both plates carry **zero text-layer words**, so the word-grazing audit that "cleared" PR #85 had nothing to inspect on them. The crop gate is now three-part — word grazing **+** `get_drawings()`-extent overflow **+** unexplained dark ink in a 6 pt border band — and all 18 assets pass it and have been re-opened visually. The `fig_5_3` manifest caption (mislabelled `Central dogma`; the asset is the DNA double helix) is corrected, and the unnumbered `fig_5_central_dogma` bonus plate is now a manifest row, taking the asset count from 17 to 18. Reusable procedure: `skills/ncert-figure-extraction/SKILL.md`.

**Gate 1 closed on 2026-08-22.** The final figure sweep produced 18 assets at 300 dpi, all individually opened after grayscale conversion and verified for identity, complete labels/leader lines, print legibility, and `L` mode. The Facts table now ends at `F646`, including 136 contiguous figure-label rows (`F511`–`F646`); `check_pdf.py`'s own `_extract_labels` returns 136 labels across 15 label-bearing figures, with no doubling and no phantom `Fig #` row. Figures `5.4b` and `5.15` are genuinely label-free. The inventory H1 is frozen; Pass 2 has not started.

This is a per-chapter tracker; it is the detail layer under the repo-wide `CHAPTER_TRACKER.md` and
`CHAPTER_STATUS.md` roll-ups. Where those two disagree with this file about Ch5, **this file is the
one that gets re-derived from disk and wins** — but any correction must be written into all three in
the same session (§7 rule 8, atomic closure).

Nothing in this file may be updated from memory. Every count below carries the command that produced
it, and the rule is: **re-run, don't recall.**

---

## 1. Protocol selected, and why

31 source pages, 10 numbered sections plus Summary and Exercises. That is over the big-chapter
threshold, so Ch5 runs the **5-pass protocol**:

    1a → 1b → [GATE 1] → 2a → 2b → [GATE 2] → 3 → [GATE 3] → deliver

Two axes operate independently and must not be conflated:

- **1a / 1b split the *source*** into halves.
- **-S / -H / -O / -F / -Z split the *kind of work*** so that each sweep is the sole deliverable of a
  session that closes on it. A sweep folded into another sweep is the Ch9 D9 failure mode.

`-F` (figures) and `-Z` (freeze) run **whole-chapter, not per half**, because a half-chapter figure
manifest cannot be checked for duplicate or missing `Fig #` across the seam, and a half-chapter
freeze is not a freeze.

### Verified source map

| Half | Source pages | Book pages | Content | Verified how |
|---|---|---|---|---|
| **1a** | pp. 1–17 | 79–95 | Chapter opener + §5.1–§5.5.3, ending at the `5.6 GENETIC CODE` banner | banner located at 13.0pt Bookman-Demi, **page 17**, mid-page |
| **1b** | pp. 17–31 | 95–109 | §5.6–§5.10 + Summary + Exercises | remainder |

The seam falls **mid-page 17**: p17 carries the tail of §5.5.3 *and* the §5.6 banner. Both halves
must read p17; `1b-S` starts at the banner, not at the top of the page.

---

## 2. Session ledger — 9 sessions

| # | Session | Scope | State | Sole deliverable |
|---|---|---|---|---|
| 1 | `1a-S` | 1a prose, steps 1–3 | ✅ **done** | 231 prose rows `F001..F231` |
| 2 | `1a-H` | 1a headings only | ✅ **done** | 17 heading rows `F232..F248` (16 in-body + chapter title; both unnumbered subs `F237`, `F238`) |
| 3 | `1a-O` | 1a section openers only | ✅ **done** | 16 opener rows `F249..F264` |
| 4 | `1b-S` | 1b prose, steps 1–3 | ✅ **done** | 218 prose rows `F265..F482` |
| 5 | `1b-H` | 1b headings only | ✅ **done** | 13 heading rows `F483..F495` (incl. `Goals of HGP`, `SUMMARY`, `EXERCISES`) |
| 6 | `1b-O` | 1b openers only | ✅ **done** | 11 opener rows `F496..F506` |
| 7 | `1-F` | **whole chapter** figures | ✅ **done** | 18 verified mono assets (17 numbered/split + 1 unnumbered) + manifest + 136 in-figure label rows `F511..F646` |
| 8 | `1-Z` | steps 7–9 whole chapter | ✅ **done** | exercise-gap scan (**17 rows**, 5 gaps), summary classification (33 = 29 + 4), 4 folded rows `F507..F510`, freeze |
| 9 | — | step 10 | ✅ **done and re-run after freeze** | machine re-parse: 646 rows, 0 gaps/dups, monotonic, 0 ticked |

**Why `1-Z` could run before `1-F`.** Steps 7, 8 and 10 read prose and count table rows, so they do
not depend on the figure sweep. Step 9 is different in kind: it asserts that the whole of Pass 1 is
finished. Running 7/8/10 early is efficient; running 9 early is a lie. If a later session sees
"`1-Z` done" written anywhere without a step list, treat it as unverified and re-check the H1.

**Order from here:** `1-F` → `1-Z` step 9 (freeze) → step 10 re-parse → *then* judge Gate 1.

**Two denominators, one state.** This ledger says **9** because row 9 (step 10, machine re-parse) is
its own row; the inventory's Session log says **8** because it lists sweeps only. 8 sweeps + 1
verification = 9. Report whichever you use *with its basis*, never a bare "1 of N".

Then Pass 2a/2b (script), Gate 2 (lint loop to exit 0 on all 8 checks), Pass 3 (dual verification),
Gate 3.

---

## 3. What is actually on disk

    notes/class 12/Ch5_MolecularBasisOfInheritance/
      Ch5_MolecularBasisOfInheritance_inventory.md   FROZEN, 646 rows
      Ch5_TRACKER.md                                 this file
      extract_figures.py                             hand-pinned rects + 3-part crop gate
      assets/                                        18 verified mono PNGs

No `Ch5_MolecularBasisOfInheritance.py` and no generated `.pdf`. **Correct at Gate 1 closure:** Pass 2 has not started.

One further Ch5 file is committed **outside** the chapter folder and is not a deliverable:

    scratch/ch5mbi/full_text.txt   66 KB, 1290 lines — pdfplumber dump of all 31 source pages,
                                   page-delimited `===== PAGE n =====`

It is a working aid only (§0.5 permits a scratch directory). It is **not** the source of truth: every
count is re-derived from the inventory and every page-level claim from the source PDF. Do not let a
future session promote it to a deliverable or read facts out of it instead of the PDF — the figures
and in-figure labels `1-F` needs do not exist in a text dump at all.

### Machine-derived state of the inventory

Re-parsed from the file this session, not recalled:

| Metric | Value |
|---|---|
| Facts rows | **646** |
| ID range | `F001..F646`, **0 gaps, 0 duplicates, monotonically increasing** |
| `Type` census | `concept` 264 · `figure-label` 136 · `definition` 56 · `number` 37 · `list` 33 · `question` 31 · `heading` 30 · `opener` 27 · `name` 18 · `example` 13 · `table` 1 |
| Census sums to | 264+136+56+37+33+31+30+27+18+13+1 = **646** ✓ matches row count |
| `Type: heading` | **30** — `1a-H` 17 + `1b-H` 13 ✓ |
| `Type: opener` | **27** — `1a-O` 16 + `1b-O` 11 ✓ |
| Figure-label rows | **136** (`F511..F646`); `5.4b` and `5.15` are genuinely label-free |
| Summary sentences classified | **33 = 29 BODY-PRESENT + 4 SUMMARY-UNIQUE**; the 4 unique facts folded in as `F507..F510` ✓ |
| Exercise-gap table rows | **17 (machine-parsed as the table's own length), 5 of them GAP** — each gap has a named inline home |
| Rows ticked | **0** — Pass 2 not started |
| `_extract_labels` (the linter's own parser) | **136 labels, 15 label-bearing figures, no doubling, no phantom `Fig #` row** |
| Frozen | **Yes.** H1 reads `# Frozen Inventory`; Gate 1 closed |

Re-derive with:

    /vercel/share/neetenv/bin/python - <<'EOF'
    import re, collections, importlib.util
    p="notes/class 12/Ch5_MolecularBasisOfInheritance/Ch5_MolecularBasisOfInheritance_inventory.md"
    t=open(p).read(); rows=[]
    for l in t.splitlines():
        if not l.strip().startswith("|"): continue
        c=[x.strip() for x in l.strip().strip("|").split("|")]
        if len(c)>=5 and re.fullmatch(r"F\d+[a-z]?", c[0]): rows.append(c)
    ids=[int(r[0][1:]) for r in rows]
    print("rows",len(rows),"gaps",[i for i in range(ids[0],ids[-1]+1) if i not in set(ids)],
          "dups",[k for k,v in collections.Counter(ids).items() if v>1])
    print(dict(collections.Counter(r[2] for r in rows)), "ticked", sum(1 for r in rows if r[4]=="x"))
    s=importlib.util.spec_from_file_location("cp","check_pdf.py"); m=importlib.util.module_from_spec(s); s.loader.exec_module(m)
    print("labels", len(m._extract_labels(t)))
    EOF

### Environment

`/vercel/share/neetenv` was **absent** at chapter start — the expected state per §0.2, checked before
anything was diagnosed — and was rebuilt: CPython 3.13.11, reportlab 5.0.1, pdfplumber OK,
pymupdf 1.28.2, Pillow 12.3.0, all imports verified under that interpreter. **Every future session
re-checks `ls /vercel/share/neetenv/bin/python` first**; sandboxes lose it.

---

## 4. NEXT SESSION — `1-F`, whole-chapter figures

**`1-F` is the only thing standing between this chapter and a Gate 1 judgement.** Everything in
this section below the horizontal rule is the **historical `1a-H` scoping record**, retained for
audit; it is **not** an instruction to any future session. `1a-H` closed long ago and the
inventory now stands at **510 rows (`F001..F510`)**, so **no session may append headings from
`F231`** — that ID has been occupied since `1a-S` closed.

### Scope of `1-F` — whole chapter, figures only

Figures run **whole-chapter, never per half** (§1): a half-chapter manifest cannot be checked for
duplicate or missing `Fig #` across the mid-page-17 seam. Prose, headings and openers are **already
swept and must not be re-read** — re-reading them is how sweeps contaminate each other.

**Census enumerated from source, not memory: 16 figure numbers ⇒ 17 assets**, because `Figure 5.4`
splits into `5.4a Nucleosome` and `5.4b EM picture — 'Beads-on-String'`.

| Half | Figures | Assets |
|---|---|---|
| First (pp. 1–17) | 5.1, 5.2, 5.3, **5.4a, 5.4b**, 5.5, 5.6, 5.7, 5.8, 5.9, 5.10, 5.11 | 12 |
| Second (pp. 17–31) | 5.12, 5.13, 5.14, 5.15, 5.16 | 5 |
| **Total** | **16 numbers** | **17 assets** |

The full trap list, per-asset requirements and label obligations live in §5 under **`1-F`** — read
that entry before starting. In brief: create `assets/` (it does not exist yet), clip-extract each
asset at 300 dpi, convert to true monochrome, **verify by actually opening each rendered file**
(`Mono: yes` / `Verified: yes` per manifest row), and append **one Facts row per in-figure label**
continuing from **`F511`** — including `Central dogma` (p4, per §6 correction) and `anticodon loop`
(p20). Touch no existing row.

### Acceptance criteria for `1-F`

- `assets/` exists and holds **17** verified monochrome assets for **16** figure numbers.
- Every manifest row asserts `Mono: yes` and `Verified: yes`, each backed by opening the file.
- One Facts row per in-figure label, IDs contiguous from `F511`; re-parse reports 0 gaps, 0 dups.
- `check_pdf.py`'s own `_extract_labels` returns the **expected figure count with no doubling and
  no phantom `Fig #` row** — it currently returns 0, which is the correct *pre*-`1-F` state, not a pass.
- `CHAPTER_TRACKER.md`, `CHAPTER_STATUS.md` and this file all updated in the **same** session.
- **Gate 1 stays OPEN when `1-F` closes.** `1-Z` step 9 (freeze) then a final step-10 re-parse must
  follow before Gate 1 may even be judged. Do not freeze inside `1-F`.

---

## 4a. HISTORICAL RECORD — `1a-H` scoping (session closed; do not action)

> **Superseded.** The text below was written as the forward brief for `1a-H` and is kept verbatim for
> auditability (§7: historical session records must remain auditable). `1a-H` **is done** — it
> delivered 17 heading rows `F232..F248`, and `1b-H` later added 13 more (`F483..F495`) for the
> machine-verified total of **30 `Type: heading` rows**. The "append from `F231`" instruction and the
> "next session" framing are **obsolete**. Read this only as evidence of how the headings were scoped.

### Target as scoped then: 17 heading lines on pp. 1–17 (16 in-body + the p1 chapter title)

Reconstructed from the PDF this session at line level (not span level — see trap 2):

| # | Heading | Page | Level |
|---|---|---|---|
| 1 | `MOLECULAR BASIS OF INHERITANCE` (chapter title) | 1 | chapter |
| 2 | `5.1 THE DNA` | 2 | section |
| 3 | `5.1.1 Structure of Polynucleotide Chain` | 2 | sub |
| 4 | `5.1.2 Packaging of DNA Helix` | 5 | sub |
| 5 | `5.2 THE SEARCH FOR GENETIC MATERIAL` | 6 | section |
| 6 | `Transforming Principle` | 6 | **unnumbered sub** |
| 7 | `Biochemical Characterisation of Transforming Principle` | 7 | **unnumbered sub** |
| 8 | `5.2.1 The Genetic Material is DNA` | 7 | sub |
| 9 | `5.2.2 Properties of Genetic Material (DNA versus RNA)` | 8 | sub |
| 10 | `5.3 RNA WORLD` | 10 | section |
| 11 | `5.4 REPLICATION` | 10 | section |
| 12 | `5.4.1 The Experimental Proof` | 10 | sub |
| 13 | `5.4.2 The Machinery and the Enzymes` | 12 | sub |
| 14 | `5.5 TRANSCRIPTION` | 13 | section |
| 15 | `5.5.1 Transcription Unit` | 13 | sub |
| 16 | `5.5.2 Transcription Unit and the Gene` | 14 | sub |
| 17 | `5.5.3 Types of RNA and the process of Transcription` | 15 | sub |

That table lists 17 lines because the chapter title is row 1; **16 is the in-body heading count and
17 the total including the chapter title.** *Outcome:* `1a-H` wrote **17** rows (`F232..F248`) on the
title-inclusive convention, and that convention still holds across the chapter — of the 30 heading
rows now on disk, 1 is the chapter title, so **in-body headings = 29**.

`5.6 GENETIC CODE` (p17) is the seam banner and was left to **`1b-H`**, which duly recorded it.

### Four traps found while scoping `1a-H` (still applicable to any heading re-audit)

1. **Running headers are bold full lines.** `BIOLOGY` and `MOLECULAR BASIS OF INHERITANCE` appear at
   **9.0pt Bookman-Demi on nearly every page** as running heads. A "bold full line" heuristic
   harvests ~16 phantom heading rows from them. Filter `size >= 10.5`, and treat the 9.0pt
   `MOLECULAR BASIS OF INHERITANCE` running head as distinct from the p1 chapter title.
2. **Heading text is split across spans by small caps.** `5.2 THE SEARCH FOR GENETIC MATERIAL` is
   **10 spans**; per-span reads return the truncated garbage `5.2 T`. Also seen: `5.1 T`, `5.3 RNA W`,
   `5.4 R`, `5.5 T`. **Join spans at line level before recording any heading string.**
3. **Figure captions are bold too**, at 9.5pt (`Figure 5.1 A Polynucleotide chain`). They are `1-F`
   deliverables, never heading rows. The 10.5pt floor in trap 1 also excludes these.
4. **CORRECTION to an earlier claim.** The `1a-S` carry-over list called `Central dogma` (p4) a
   "boxed heading" for `1a-H`. Re-checked: it is plain **Bookman-Light 10.5** text acting as the label
   on the DNA→RNA→Protein diagram, not a bold sub-heading. It is an **in-figure label owned by
   `1-F`**, and it must **not** become a heading row. The two genuine unnumbered sub-headings in the
   first half are rows 6 and 7 above, both 10.5pt full-bold, and nothing else.

### Acceptance criteria `1a-H` was held to — all met at close

- Every heading in pp. 1–17 has exactly one row; no heading absorbed into a prose row. ✓
- No row sourced from a 9.0pt running head, and no row sourced from a 9.5pt figure caption. ✓
- Every heading string is a full joined line, no `5.2 T` truncation. ✓
- IDs contiguous from `F232`; re-parse reports 0 gaps, 0 duplicates. ✓ (still true at 510 rows)
- Exit report stated the machine-derived `Type: heading` count and the title-inclusion convention. ✓
- `CHAPTER_TRACKER.md`, `CHAPTER_STATUS.md` and this file updated in the **same** session. ✓
- **Gate 1 stayed OPEN** — `1a-H` closing was not Gate 1 closing, and Gate 1 is **still open today**,
  blocked on `1-F` (§4).

---

## 5. Forward notes — only `1-F` and `1-Z` step 9 are still live

**`1a-O` — ✅ done; note retained for audit, not for action.** Openers only, pp. 1–17. The
load-bearing ones: the §5.5 opener is the only place *transcription* is defined, and the §5.5.2
opener is the only place *gene* is defined. Had those two openers been skipped, the chapter would
ship without defining its two central terms — the exact Ch9 D9 failure. **Both were confirmed to
have produced a row before `1a-O` closed**; openers now total **27** machine-verified rows
(`F249..F264` + `F496..F506`).

**`1-F` — ⬜ LIVE. The sole Gate 1 blocker; see §4 for the actionable brief.** Whole chapter.
Captions enumerated from source: **16 figure numbers but 17
assets**, because `Figure 5.4` is split into `5.4a Nucleosome` and `5.4b EM picture — 'Beads-on-String'`.
First half: 5.1, 5.2, 5.3, **5.4a, 5.4b**, 5.5, 5.6, 5.7, 5.8, 5.9, 5.10, 5.11 (12 assets).
Second half: 5.12, 5.13, 5.14, 5.15, 5.16 (5 assets). Two traps: the a/b pair is what makes a
duplicate-`Fig #` check fire falsely or hide a real dupe, and **`Figure 5.15`'s caption text sits on
a separate line from its number** (p25), so caption capture must not assume number and text share a
line. Each asset needs 300 dpi clip extraction, mono conversion, and **verification by actually
opening the rendered file** — `Mono: yes` / `Verified: yes` asserted per row, plus one Facts row per
in-figure label (including `Central dogma`, per trap 4).

**`1-Z` — ⚠️ partial: steps 7, 8 and 10 done; step 9 (freeze) still LIVE and deliberately withheld.**
The exercise-gap scan (**17 rows, 5 gaps**) and the summary classification (33 = 29 BODY-PRESENT + 4
SUMMARY-UNIQUE, folded as `F507..F510`) are complete. What remains is **step 9 — the freeze**: retitle
the inventory H1 from `# Working Inventory (NOT FROZEN)` to the frozen convention, **and it may not run
until `1-F` has closed.** Retitling early is a false completion signal — the H1 was already caught
reading `# Frozen Inventory` once while six sweeps were outstanding, where a `grep -i frozen` over
`notes/` would have counted Ch5 as frozen.

**Gate 1** is **OPEN today** and may only be *judged* after `1-F` closes and `1-Z` step 9 plus a final
step-10 re-parse have run. Completing `1b` was necessary but not sufficient. The judgement needs: a
complete inventory, `_extract_labels` clean (right figure count, no doubling, no phantom `Fig #` row),
every count matching a re-parse, all figures `Mono: yes` / `Verified: yes`, and each sweep traceable to
a session that closed on it. **Six landed sweeps do not close Gate 1.**

**Pass 2a/2b** — one script, `Ch5_MolecularBasisOfInheritance.py`, written linearly in Content Order
from the frozen inventory, importing `neet_template.py` with **no style re-declared**; both halves go
into the **same** script and rows are ticked **as each block is written**, not reconciled afterwards.
The deliverable is one merged PDF — **never two half-PDFs**.

---

## 6. Corrections log

| When | Correction |
|---|---|
| `1a-S` | Inventory H1 was `# Frozen Inventory`, copied from completed chapters, while line 3 said NOT FROZEN. Retitled `# Working Inventory (NOT FROZEN)`; frozen title now withheld until `1-Z` earns it. |
| `1a-S` scoping | `Central dogma` (p4) was mis-scoped to `1a-H` as a heading. It is a 10.5pt Light diagram label → reassigned to `1-F` as an in-figure label. |
| repo roll-up | Done tally re-derived by counting ✅ rows (`awk`) rather than incremented: 11 of 32 (Class 11: 6, Class 12: 5). Ch5's ▶️ row is excluded because Gate 1 is open. |
| stale-instruction audit (consistency-only session, **no sweep run, no state advanced, Gate 1 still OPEN**) | Environment first: `/vercel/share/neetenv` was **absent again** (expected, §0.2) and was rebuilt — CPython 3.13.11, reportlab 5.0.1, pdfplumber OK, pymupdf 1.28.2, Pillow 12.3.0, all imports verified. Every current-state fact then **re-derived, not recalled**: **510 rows / `F001..F510` / 0 gaps / 0 dups / monotonic / 0 ticked**; census `concept` 264 · `definition` 56 · `number` 37 · `list` 33 · `question` 31 · `heading` 30 · `opener` 27 · `name` 18 · `example` 13 · `table` 1 **= 510** ✓; the **real** `_extract_labels` imported from `check_pdf.py` returns **0 labels / 0 figures / no phantom `Fig #` row** (correct pre-`1-F`); exercise-gap table machine-measured at **17 data rows / 5 GAP rows** ✓ (confirms the previous session's 16→17 correction — not reverted); H1 still `# Working Inventory (NOT FROZEN)`; no `.py`, no `.pdf`, no `assets/`; Done tally still **11/32**. **Four genuinely stale *current-state* blocks found and fixed, all of them instructions that would have misdirected the next agent:** (a) tracker **§4 was still titled "NEXT SESSION — `1a-H`"** and told the reader to append heading rows continuing from **`F231`** — an ID occupied since `1a-S`; §4 is now **"NEXT SESSION — `1-F`"** with the real figure brief, and the entire `1a-H` scoping record was moved intact to a new **§4a marked HISTORICAL / do not action** (history preserved verbatim, imperatives neutralised, acceptance criteria re-cast as met-at-close); (b) tracker **§5 listed `1a-O` as a forward note** though it closed long ago, and its `1-Z` entry described the whole session as pending — both re-labelled with state, leaving `1-F` and `1-Z` step 9 as the only live items; (c) tracker §5's **"Gate 1 is judged only after `1b`"** was misleading now that `1b` is done but Gate 1 is open — restated as "necessary but not sufficient"; (d) the inventory's **Facts-table scope note still read "after session 1a-S: prose facts of the first half only"**, which would license a future agent to think headings/openers were still missing — restated to the real 510-row whole-chapter scope, with the old note kept as an explicitly superseded quote, plus the same "necessary but not sufficient" fix to the §6-protocol Gate 1 sentence. **No inventory Facts row was touched**, no history rewritten, freeze not run, Gate 1 not closed, Pass 2 not started. |
| tracker audit (consistency-only session, no sweep run) | Every Ch5 claim in this file, the inventory, `CHAPTER_TRACKER.md` and `CHAPTER_STATUS.md` re-derived from disk: **231 rows / F001..F231 / 0 gaps / 0 dups / 0 ticked** ✓ · `Type` census 149·28·16·15·11·9·3 = 231 ✓ · 0 heading, 0 opener, 0 figure-label rows ✓ · H1 still `# Working Inventory (NOT FROZEN)` ✓ · no `.py`, no `.pdf`, no `assets/` ✓ · source PDF `/Count 31` = 31 pp ✓ · `5.6 GENETIC CODE` banner on **p17**, confirming the mid-page seam ✓ · 10 section banners on pp. 2/6/10/10/13/17/20/21/24/27 ✓ · sub-headings on the exact pages §4 claims (5.1.1 p2, 5.1.2 p5, 5.2.1 p7, 5.2.2 p8, 5.4.1 p10, 5.4.2 p12, 5.5.1 p13, 5.5.2 p14, 5.5.3 p15), unnumbered subs p6/p7, `Central dogma` p4 ✓ · captions `Figure 5.1`–`5.16` **with 5.4a/5.4b present ⇒ 16 numbers / 17 assets** ✓ · repo Done tally re-counted = **11 ✅ rows** ✓. **Three inconsistencies found and fixed:** (a) §4 was headed "Target: 16 heading rows" above a 17-row table → retitled to state 17 lines = 16 in-body + chapter title; (b) inventory said "1 of 8" where this ledger says 9 → both now state their basis (§2 note); (c) `scratch/ch5mbi/full_text.txt` was committed but recorded nowhere → now listed in §3 as a non-deliverable working aid. **Caveat:** `/vercel/share/neetenv` is absent again (expected), so `_extract_labels` was not run under the venv — its parser logic was replicated with system `python3` and returns **0 label rows**, matching the claim; re-run it properly next session. |
