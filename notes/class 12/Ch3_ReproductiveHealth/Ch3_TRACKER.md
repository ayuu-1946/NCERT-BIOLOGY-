# Ch3 Reproductive Health — Tracker

Source: `Chapter/class 12/Chapter 3 - Reproductive Health.pdf` (10 pp: 8 body + SUMMARY + EXERCISES)
Unit: Class 12, Unit VI — Reproduction (chapters 2, 3, 4)

| Stage | State |
|---|---|
| Pass 1 | ✅ complete — five sessions (1-S, 1-H, 1-O, 1-F, 1-Z), all with machine-derived counts |
| **Gate 1** | ✅ **CLOSED (2026-09-12)** — inventory frozen at **162 rows `F001`–`F162`, contiguous, 0 gaps, 0 duplicate IDs**, 53/53 machine checks pass |
| Pass 2 | ⬜ not started |
| Gate 2 | ⬜ not started |
| Pass 3 | ⬜ not started |
| Gate 3 | ⬜ not started |
| Deliverables | ⬜ no `.pdf`, no `.py` yet — Gate 1 only |

**Gate 1 closed; Pass 2 not started.** Nothing here counts toward a "Done" tally.

---

## Environment (this sandbox)

`/vercel/share/neetenv` does **not** exist in this container and `uv` is not installed, so the
standard preamble from GATE_1_PASS_1_SOURCE_MASTERY.md §1 cannot be run as written. The equivalent
environment was built once at the repo root and reused for every command:

```bash
python3 -m venv .venv                       # Python 3.11.2
.venv/bin/pip install reportlab pdfplumber pymupdf Pillow numpy
# reportlab 5.0.1 · pymupdf 1.28.2 · Pillow 12.3.0 · numpy 2.4.6
```

`numpy` is required by the mandatory border-band check (skill §4, check C); the standard
four-package list omits it. Every Python command in this chapter was run through
`.venv/bin/python`. This is the only deviation from the documented preamble, and it is
environmental, not a workaround for a missing library.

---

## Pass 1 — the five sessions (each session's own machine-derived count)

| Session | Work | Machine-derived deliverable |
|---|---|---|
| **1-S** | Steps 1–3: full chapter read (8 body pages, 143 sentences walked one by one against the row set), then facts inventory | **140 content rows** |
| **1-H** | Step 4: heading sweep — headings walked as their own list, prose ignored | **10 rows** = 8 `heading` + 1 `title` + 1 `contents` |
| **1-O** | Step 5: opener sweep — first sentence of every section, headings ignored | **6 opener rows** [F004, F012, F032, F101, F120, F135] |
| **1-F** | Step 6 / §4.4: 6 assets extracted, monochrome-converted, three-part audited, individually opened; label harvest by open — **not** text extraction | **6 figure rows** (2 label-bearing, **2 genuine in-figure labels**; 4 documented label-free) |
| **1-Z** | Steps 7–10: summary classification, exercise-gap scan, freeze, machine-derived counts | **18 summary sentences classified** (15 BODY-PRESENT + 3 SUMMARY-UNIQUE) + **18 exercise parts over 12 exercises** (15 COVERED + 3 GAP) + freeze at 162 rows |

## Gate 1 — the frozen inventory

`Ch3_ReproductiveHealth_inventory.md` — **162 rows**, IDs contiguous `F001`–`F162`.

- **Type census (11 values, all lower-case):** `fact` 103 · `number` 17 · `term` 14 · `heading` 8 ·
  `caption` 6 · `opener` 6 · `process` 3 · `definition` 2 · `contents` 1 · `exception` 1 · `title` 1 = 162.
- **Headings (8):** 3.0 (unnumbered chapter intro) · 3.1 · 3.2 · 3.3 · 3.4 · 3.5 · SUMMARY · EXERCISES,
  plus the `title` and `contents` rows that carry the cover and the page-1 contents box.
- **Openers (6):** the unnumbered intro + 3.1–3.5. Two of them define the term used in their own
  section's heading (3.3 "medical termination of pregnancy or induced abortion"; 3.4 "sexually
  transmitted infections (STI) or venereal diseases (VD) or reproductive tract infections (RTI)") —
  the Ch9 D9 class, both caught here.
- **Figures (6 assets / 4 numbered figures):** 3.1(a), 3.1(b), 3.2, 3.3, 3.4(a), 3.4(b); all
  `Mono: yes`, `Verified: yes`. See `Ch3_figure_audit.md`.
- **Figure labels: 2** — `Vas deferens tied and cut` (Fig 3.4a) and `Fallopian tubes tied and cut`
  (Fig 3.4b). Both are **vector artwork absent from the PDF text layer**: a text-layer harvest
  returns an empty set and would have passed check 6 vacuously (the Ch12 failure mode). The other
  four assets were each opened and confirmed genuinely label-free.
- **Summary:** 18 sentences — 15 BODY-PRESENT, 3 SUMMARY-UNIQUE, each folded into a named body row
  with an explicit `[SUMMARY-UNIQUE fold: …]` note at the point of use:
  - "the first nation in the world" (stronger than the body's "amongst the first countries") → F012
  - "assistance to infertile couples" added to the indicators of improvement → F030
  - the "**even after 2 years** of unprotected sexual cohabitation" criterion → F136
- **Exercises:** 12 exercises / 18 numbered parts — **15 COVERED + 3 GAP, 0 overlooked.**
  Gaps answered in the planned "Terms used in the exercises" appendix: **Q7** (removal of gonads),
  **Q11(a)** (spontaneous abortion), **Q12(c)** (oral pills among rural women).

### Machine validation

`scratch/ch3/validate_gate1.py` re-parses the **saved inventory file** (not the generator's
in-memory rows) and asserts every Gate-1 criterion — **53/53 PASS**:

- IDs contiguous, no gaps/dupes; `Type` casing normalised; every row unticked at freeze.
- every header census equals a re-parse of the table, and the two `numpy`-free census lists
  ([heading IDs], [opener IDs], [figure IDs]) each equal their stated total.
- `_extract_labels` **imported from `check_pdf.py`, never replicated** → **2 labels / 2 figures
  (3.4a, 3.4b), no doubling, no phantom `Fig #` row**.
- manifest: 6 rows, all `Mono`/`Verified` yes, every asset present on disk in true `mode="L"`.
- summary arithmetic, exercise arithmetic, and every SUMMARY-UNIQUE fold note.
- all seven fixed Coverage-note headings present.

Reproduce with:

```bash
.venv/bin/python scratch/ch3/freeze_inventory.py     # regenerate the frozen inventory from the row set
.venv/bin/python scratch/ch3/validate_gate1.py       # 53/53 PASS
```

## Carry-overs for Pass 2 (found while looking at something else)

1. **The seven contraceptive categories must survive as named categories** — NCERT groups them
   "Natural/Traditional, Barrier, IUDs, Oral contraceptives, Injectables, Implants and Surgical
   methods". A comparison table is the natural home, but the category *names* are examinable.
2. **The 3.2 heading is inconsistent in the source itself**: contents box and summary say
   "Population Explosion and Birth Control"/"explosive growth", the page-43 heading says
   "POPULATION STABILISATION AND BIRTH CONTROL". Both wordings are in the inventory (F031 heading,
   F033 explosive-growth row) — carry both, do not silently pick one.
3. **Source typo class**: NCERT prints "aminocentesis" (3.1) and "haemoplilia" for haemophilia, and
   the amniocentesis sentence is garbled ("...etc., determine the survivability of the foetus").
   Reproduce the facts; do not import the garbling into running text, and do not "fix" the source
   in the inventory's verbatim column. Recorded under Source problems.
4. **Check 4 will fire on this chapter** for a legitimate reason: NCERT's IVF/ART and MTP material
   uses no scientist portrait, but the row wordings contain no portrait keywords either — if check 4
   reports anything here it is a true-negative to be inspected, not "fixed".
5. **check_pdf.py check 6 needs both Fig 3.4 labels in running text.** They are the chapter's only
   two in-figure labels and they must appear in the vasectomy/tubectomy prose verbatim.
6. **`fig_3_4b.png` is not a raw crop**: its right edge carries a white-washed page tab. Do not
   re-extract it with a narrower rect — that clips the right ovary (the defect this session fixed).
   The rect and the guard live in `extract_figures.py` (`TAB_WHITEOUT`).
7. **numpy is part of this chapter's toolchain** (check C of the crop audit). The documented venv
   command list in the three GATE files omits it.
8. **Documentation defect found in passing (not fixed here, and not this chapter's):**
   `CHAPTER_STATUS.md`'s overview table had **no row at all** for Class 12 Ch3 (this session added
   one, in chapter order, after Ch2). While checking that, the same absence was found for
   **Class 12 Ch8 Microbes in Human Welfare**, which `CHAPTER_TRACKER.md` marks ✅ Done — so a
   completed chapter is invisible in the status table. Ch1 Sexual Reproduction in Flowering Plants
   has no row either, but that one is consistent with the table's convention of listing only
   chapters that have started. Ch8's missing row is a live propagation gap from another session's
   closure; it is flagged here rather than fixed, because its evidence was not re-derived this
   session and §9.2 forbids correcting a claim you have not re-verified.
9. **`scratch/ch3/` is the audit trail, not scratch paper to delete.** `freeze_inventory.py`
   regenerates the frozen inventory from `ch3_rows.py` (so a count fix is a regenerate, never a
   hand edit), and `validate_gate1.py` re-earns Gate 1 from the saved file.

## Files at Gate 1

```
notes/class 12/Ch3_ReproductiveHealth/
  Ch3_ReproductiveHealth_inventory.md   ← THE GATE 1 DELIVERABLE (162 rows, unticked)
  Ch3_figure_audit.md                   ← 1-F evidence: census, rects, audit, defects fixed
  Ch3_TRACKER.md                        ← this file
  extract_figures.py                    ← pinned rects + monochrome conversion (+ tab guard)
  audit_figures.py                      ← three-part crop audit
  assets/fig_3_1a.png, fig_3_1b.png, fig_3_2.png, fig_3_3.png, fig_3_4a.png, fig_3_4b.png
scratch/ch3/
  ch3_rows.py                           ← the row set (session-tagged, one tuple per row)
  freeze_inventory.py                   ← derives every count; assigns contiguous IDs
  validate_gate1.py                     ← 53/53 Gate 1 machine checks
  ch3_source.txt, sentences.txt         ← extracted source text + the 143-sentence walk
  figs/grid_4x/p01,p04,p05,p06.png      ← mandatory 440 dpi / 5-point grids
  figs/contact_sheet.png, figs/seam/…   ← visual verification evidence
```
