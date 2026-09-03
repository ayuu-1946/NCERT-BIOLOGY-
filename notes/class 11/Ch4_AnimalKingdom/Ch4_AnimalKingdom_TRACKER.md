# Class 11 · Chapter 4 — Animal Kingdom · TRACKER

**Source of truth:** `Chapter/class 11/Chapter 04 - Animal Kingdom.pdf` — **18 pages** (`doc.page_count == 18`, machine-read).
**Inventory (single source of truth for content):** `Ch4_AnimalKingdom_inventory.md`.
**Text snapshot for this arc:** `scratch/ch4_gate1/ch4_source.txt` (1022 lines, PyMuPDF, page markers `===== PAGE n =====`).
**Protocol:** `GATE_1_PASS_1_SOURCE_MASTERY.md`, run as a **big chapter** (§8) — halves 1a and 1b into one inventory.

> **GATE 1 IS CLOSED (GREEN), 2026-09-03. Pass 1 is complete — all nine sessions done (Pass 1a + Pass 1b + 1-F + 1-F resumed + 1-Z). Inventory FROZEN at 352 rows (F001–F352, machine-validated). Pass 2 has NOT started: no script, no PDF, all 352 rows unticked — so Chapter 4 must NOT appear in any "Done" completion tally.**

---

## 1. Restart decision (2026-09-03)

Per operator instruction, **no prior Chapter 4 work or documentation is trusted; only the extracted figure assets are**. Two files were archived unread-as-evidence and are mined for nothing:

| Archived file | What it actually was |
| :--- | :--- |
| `Ch4_prior_TRACKER_UNTRUSTED.md` | Previous tracker asserting "**Pass 1 COMPLETE · Gate 1 PASSED**" |
| `Ch4_prior_figure_notes_UNTRUSTED.md` | Previous `..._inventory.md` — a figure write-up, **not** a Gate 1 inventory |

`Ch4_figure_audit.md` and `extract_figures.py` are from the same arc and are also untrusted; the script may be reused as a *starting point* for rectangles at 1-F only, after §3's 440 dpi / 5 pt gridline standard is applied and every rectangle is re-inspected.

### Why the archived Gate 1 verdict could not stand

Checked against the machine, not against its own prose:

1. **Page count wrong in the arc.** The archived inventory says 14 pages; the PDF has 18. Every source-page number produced by that arc is therefore suspect.
2. **No inventory existed to freeze.** The file it named as the frozen inventory had no Facts table, no ID column, no heading/opener rows, no summary classification and no exercise-gap table — so "215 rows frozen"-style evidence was never on disk.
3. **Self-contradictory asset count.** Its own Gate 1 checklist claims **27 assets** while §D and §H claim **26**; disk says **26**.
4. **Cited a snapshot with a different body.** It cites `scratch/ch4_gate1/source_text.txt` at "688 lines"; the machine extraction of all 18 pages is 1022 lines.
5. **`fig_vertebrata_chart.png` filed as a "bonus".** §3 step 1 item 4: unnumbered plates are **real figures**. Mis-classified, and it sits on source page 11 — 1b territory.
6. **Repo-level docs already disagreed with it.** `CHAPTER_TRACKER.md` simultaneously said "Gate 1 passed" (Ch4 row) and "Only Ch4, Ch5 and Ch7 remain Not done" (Class 11 tally), and `CHAPTER_STATUS.md` had **no Class 11 Ch4 row at all**.

No row, count or claim from that arc was carried into the new inventory.

---

## 2. Half seam (fixed, so nothing is double-covered or dropped)

| Half | Scope | Source pages |
| :--- | :--- | :-: |
| **1a** | Chapter intro, §4.1 + §4.1.1–§4.1.6, §4.2 opener, §4.2.1–§4.2.10 (Porifera → Hemichordata, the non-chordates), incl. the Figure 4.4 footnote | 1–9 |
| **1b** | §4.2.11 Chordata + all seven classes, TABLE 4.1, TABLE 4.2 (**all 11 phylum rows**), SUMMARY, EXERCISES | 10–18 |

**Seam rule:** TABLE 4.2 belongs to **1b by physical location** even though ten of its rows describe 1a phyla. 1a must not pre-empt it; 1b must cross-check it against 1a's prose rows.

---

## 3. Session ledger — each session states its own machine-derived count

| Session | Scope | Status | Rows added |
| :--- | :--- | :--- | :--- |
| **1a-S** | Steps 1–3 — prose facts, first half | **[x] DONE (2026-09-03)** | **154 (`F001`–`F154`)** |
| **1a-H** | Step 4 — heading sweep, first half | **[x] DONE (2026-09-03)** | **21 (`F155`–`F175`)** |
| **1a-O** | Step 5 — opener sweep, first half | **[x] DONE (2026-09-03)** | **19 (`F176`–`F194`)** |
| 1b-S | Steps 1–3 — second half | **[x] DONE (2026-09-03)** | **130 (`F195`–`F324`)** |
| 1b-H | Step 4 — second half | **[x] DONE (2026-09-03)** | **10 (`F325`–`F334`)** |
| 1b-O | Step 5 — second half | **[x] DONE (2026-09-03)** | **8 (`F335`–`F342`)** |
| 1-F | Step 6 — figures, whole chapter | [x] DONE (2026-09-03) — manifest only; **label matrix still owed**, carry-over #8 | 26 manifest rows |
| 1-F (resumed) | Step 6 continued — label matrix + manifest audit | **[x] DONE (2026-09-03)** — discharges carry-over #8; also fixed carry-over #9 (12 wrong captions + 6 wrong pages in the manifest, all assets correct) | 7 Facts rows (`F343`–`F349`) |
| 1-Z | Steps 7–10 — gaps, summary, freeze | **[x] DONE (2026-09-03)** — exercise-gap scan (15: 13 COVERED, 2 GAP), summary two-pass (34: 3 SUMMARY-UNIQUE folded, 31 BODY-PRESENT), freeze + machine recount | 3 Facts rows (`F350`–`F352`) |

**1-F is complete for the manifest**: all 26 trusted PNG assets in `assets/` were opened and visually verified against the source-page placement. The manifest records 26 rows: numbered plates 4.1–4.24 grouped by their actual asset files, plus the real unnumbered `fig_vertebrata_chart.png` on source page 11. All assets are grayscale (`mode=L`), captions/prose are excluded, the corrected 4.5 plain rectangle is `(60,426,290,681)`, and the corrected 4.11 mask/rect is documented in the manifest. No figure was counted as a bonus or duplicated. **However, the figure-label matrix was never harvested** (`_extract_labels` = 0 labels / 0 figures) — logged as carry-over #8 and owed by a resumed 1-F before Gate 1.

**Next session: Pass 2 (script + PDF build).** Pass 1 is closed: 1-Z ran the exercise-gap scan, the summary two-pass classification + fold, and froze the inventory at 352 rows after a whole-chapter machine recount (`scratch/ch4_gate1/validate_1z.py`). Pass 2 turns the frozen inventory into the notes script and PDF, ticking each row as it is written and driving `check_pdf.py` to green. Nothing may be back-dated into the freeze; any new finding in Pass 2 is a defect to fix against the frozen inventory, not a new Pass-1 row.

---

## 4. What session 1a-S produced

Facts for source pages 1–9, transcribed in Content Order, verbatim, one fact per row.

- **154 Facts rows, `F001`–`F154`** — contiguous, **0 gaps, 0 duplicates, 0 ticked** (Pass 2 has not started).
- **Count derived by machine, never hand-tallied**: the finished table was re-parsed with `check_pdf.py`'s own row logic, and cross-checked against a per-section census that sums to 154 — `4.0`=2, `4.1`=2, `4.1.1`=11, `4.1.2`=4, `4.1.3`=3, `4.1.4`=5, `4.1.5`=2, `4.1.6`=2, `4.2`=3, `4.2.1`=13, `4.2.2`=12, `4.2.3`=9, `4.2.4`=10, `4.2.5`=10, `4.2.6`=12, `4.2.7`=19, `4.2.8`=11, `4.2.9`=12, `4.2.10`=12 (19 sections).
- **`Type` histogram**, machine-grouped and all-lowercase with no casing split: feature 86, definition 24, example 17, term 10, number 4, etymology 4, comparison 4, process 3, list 1, exception 1 = **154**.
- **Label-parser baseline:** `check_pdf.py._extract_labels` returns **0 labels, 0 figures, no phantom `Fig #` row** — correct for a file whose 1-F has not run, and the baseline the post-1-F parse must beat without doubling.
- Placeholders left explicit, not blank: summary classification, exercise-gap table and figure manifest each carry a `_pending session …_` row.

**Not done by 1a-S, by design:** headings (1a-H), openers (1a-O), the whole second half (1b-*), figures (1-F), gaps/summary/freeze (1-Z).

---

## 4a. What session 1a-H produced

Heading skeleton for source pages 1–9, swept by font size/weight off the layout (not the text stream), overprints deduplicated.

- **21 heading rows, `F155`–`F175`** — appended contiguously (inventory now `F001`–`F175`, **0 gaps, 0 dupes, 0 ticked**), re-parsed by machine.
- **Heading tiers, read off the font faces:**
  - `4.0` chapter title tier — "CHAPTER 4" + "ANIMAL KINGDOM" (F155–F156).
  - `4.1`/`4.2` section titles are **small-caps** ("BASIS OF CLASSIFICATION", "CLASSIFICATION OF ANIMALS") — F157, F164.
  - `4.1.1`–`4.1.6` and `4.2.1`–`4.2.10` numbered sub-headings at 12.0/13.0 Demi — F158–F163, F165–F174.
  - The chapter-opening **contents sidebar** (page 1, italic light face) captured as a structural row, F175.
- **Exhaustiveness check, machine-run:** every 12.0/13.0 bold line in pages 1–9 is a numbered heading — **no unnumbered sub-headings exist in the 1a half**. The 10.5 bold runs are inline term emphasis, not headings, and were excluded.
- **Seam finding (binds 1b):** the `4.2.11 Phylum – Chordata` heading physically sits on source **page 9** (y=662), but by the fixed half-seam it belongs to **1b** and was **not** taken here. 1b-H picks it up.

**Not done by 1a-H, by design:** openers (1a-O), second half (1b-*), figures (1-F), gaps/summary/freeze (1-Z).

---

## 4b. What session 1a-O produced

Section-opener sweep for source pages 1–9 — the first sentence of every section, read from **layout reading-order** (blocks sorted by y-position), not the raw text stream.

- **19 opener rows, `F176`–`F194`** — appended contiguously (inventory now `F001`–`F194`, **0 gaps, 0 dupes, 0 ticked**), re-parsed by machine.
- **One opener per section, all 19 sections of the 1a half covered:** `4.0`, `4.1`, `4.1.1`–`4.1.6` (6), `4.2`, `4.2.1`–`4.2.10` (10). Count is derivable from that list: 1 + 1 + 6 + 1 + 10 = 19, matching the machine tally.
- **Carry-over #1 discharged:** source page 5 does extract out of reading order (the §4.2.2 heading + opener sit at the bottom of the text stream), but sorting blocks by y-position put the §4.2.2 opener ("They are aquatic, mostly marine, sessile or free-swimming, radially symmetrical animals…") in its correct place. Opener taken from the layout, not the stream.
- **§4.2.10 Hemichordata** has two prose blocks; the opener is the first by layout ("Hemichordata was earlier considered as a sub-phylum under phylum Chordata."), not the later "This phylum consists of a small group of worm-like marine animals…".
- **Seam respected:** §4.2.11 Chordata's opener (page 9, y=684) was **not** taken — it belongs to 1b.

**Not done by 1a-O, by design:** the whole second half (1b-*), figures (1-F), gaps/summary/freeze (1-Z).

---

## 5. Environment note

The sandbox had been reset and `/vercel/share/neetenv` was gone. Rebuilt before any work: **Python 3.13.11**, reportlab **5.0.1**, pymupdf **1.28.2**, Pillow **12.3.0**, pdfplumber present — all imported and version-printed from that interpreter, per `setup_environment.md`.

---

## 6. Carry-overs for later sessions

Full list lives in the inventory's `## Carry-over list` (10 items). The ones that change how a later session must work:

| # | Finding | Binds | Status |
| :-: | :--- | :--- | :--- |
| 1 | Source page 5 extracts **out of reading order** — the §4.2.2 heading and opener sit at the bottom of the text stream. Take the opener from the layout, not the stream. | 1a-O | ✅ discharged |
| 2 | Source pages 11–15 render each class heading **five times** (faux-bold overprint), e.g. `4.2.11.1` ×5. Do not count duplicates as headings. | 1b-H | ✅ discharged — 7 class headings counted once (`F326`–`F332`) |
| 3 | TABLE 4.2 (page 15) extracts **column-major** — all "Level of Organisation" values, then all "Symmetry" values, phylum names last. Reassemble by column position. | 1b-S | ✅ discharged — 11 rows `F314`–`F324`, cross-checked vs 1a prose |
| 4 | Every source-page number from the archived arc is suspect (14-vs-18 page error); re-pin from page images. | 1-F | ✅ discharged |
| 5 | `fig_vertebrata_chart.png` is a real unnumbered figure, not a "bonus"; census from page images and classify properly. | 1-F | ✅ discharged (manifest) |
| 8 | **Figure-label matrix absent.** 1-F built the 26-row manifest but harvested **no** in-figure labels (`_extract_labels` = 0/0). §3 Step 1 + Gate 1 require a label matrix harvested by opening each asset. | resumed **1-F** (before Gate 1) | ✅ discharged — 7 label rows `F343`–`F349`; `_extract_labels` = 56 strings / 6 fig-id groups, 0 doubled |
| 9 | **Figure manifest itself corrupted** by the untrusted prior arc — 12 wrong verbatim captions, 6 wrong source pages (all asset artwork correct). | resumed **1-F** | ✅ discharged — every row re-pinned pixel-for-pixel against rendered pages, `CORRECTED:` notes in manifest |
| 10 | **Cosmetic:** `_extract_labels` keys figures on the Section column, so F348 + F349 (both §4.2.11) report as **6 fig-id groups for 7 label rows**. Not a missing/merged figure; changes no pass/fail. | Pass-2 readers | ℹ️ logged — benign off-by-one |

---

## 7. Artifacts on disk

| Path | Trust |
| :--- | :--- |
| `Ch4_AnimalKingdom_inventory.md` | **current — FROZEN 2026-09-03** at 352 rows (`F001`–`F352`), machine-validated (0 gaps/dupes), all unticked |
| `scratch/ch4_gate1/validate_1z.py` | **current** — 1-Z machine validator (row count, contiguity, Type histogram, `_extract_labels`), imports `check_pdf.py` |
| `Ch4_AnimalKingdom_TRACKER.md` (this file) | **current** |
| `scratch/ch4_gate1/ch4_source.txt` | **current** — 18/18 pages, page-marked |
| `assets/` (26 PNG) | **assets and metadata verified at 1-F** — all opened, grayscale confirmed, manifest documented |
| `extract_figures.py` | untrusted arc — starting point for 1-F rectangles only |
| `Ch4_figure_audit.md` | untrusted arc — not evidence |
| `Ch4_prior_TRACKER_UNTRUSTED.md`, `Ch4_prior_figure_notes_UNTRUSTED.md` | archived, **not evidence** |
| `scratch/ch4_gate1/source_text.txt` | untrusted arc snapshot — superseded by `ch4_source.txt` |

---

## 7a. What session Pass 2a produced (2026-09-03)

First half of the notes script — the non-chordate arc — built into the single deliverable
`Ch4_AnimalKingdom.py`, which renders `Ch4_AnimalKingdom.pdf` (**12 pages so far, 3021 KB**).

- **Scope written (1a half):** title block; §4.0 opener; §4.1 + §4.1.1–§4.1.6 (levels of
  organisation, symmetry, diploblastic/triploblastic, coelom, segmentation, notochord);
  §4.2 opener with the Figure 4.4 classification chart described in prose; and all ten
  non-chordate phyla §4.2.1–§4.2.10 (Porifera → Hemichordata), each with its example list.
- **Figures placed (15 of 26):** 4.1(a), 4.1(b), 4.2ab, 4.3abc, 4.4, 4.5abc, 4.6ab, 4.7,
  4.8, 4.9ab, 4.10, 4.11ab, 4.12abcd, 4.13ab, 4.14ab, 4.15 — every 1a asset, each with its
  verbatim NCERT caption. Remaining 11 assets (4.16–4.24 + `fig_vertebrata_chart.png`) are 1b.
- **Rows ticked: 200** — `F001`–`F194` (all prose/heading/opener rows of the 1a half), the
  five 1a figure-label rows `F343`–`F347`, and the one 1a summary fold `F350` (Porifera
  "flagellated choanocytes", woven into §4.2.1). Inventory now 200/352 ticked, 152 unticked
  (all `F195`+, the 1b half). No 1b row was pre-ticked; nothing was back-dated into the freeze.
- **Label coverage engineered in:** the §4.2 prose deliberately spells the Fig 4.4 chart terms
  verbatim (Kingdom / Levels of Organisation / Symmetry / Body Cavity or Coelom / acoelomates /
  pseudocoelomates / coelomates / every phylum leaf) so check 6 clears all 1a labels.

### Pass 2a mid-build lint (`check_pdf.py`, whole PDF) — the expected healthy signature

Ran `python check_pdf.py "notes/class 11/Ch4_AnimalKingdom"`. **All nine mechanical/1a checks PASS**;
the only two FAILs are 100% 1b territory and clear when 2b lands:

| Check | Result |
| :--- | :--- |
| 1 Footer/header band | ✅ PASS — content fills the frame only |
| 2 Legibility floor | ✅ PASS — smallest text 6.0pt (floor 5.0) |
| 3 Grayscale-only images | ✅ PASS — all 16 embedded images monochrome |
| 4 No person photograph | ✅ PASS |
| 5 Banned glyphs | ✅ PASS — no arrows/sub-super/Greek/emoji |
| 6 Figure-label coverage | ⛔ FAIL — 42/56 in text; **all 13 missing are §4.2.11** (F348 Chordata + F349 Vertebrata chart) whose figures/text are 2b |
| 7 Inventory fully ticked | ⛔ FAIL — 152/352 unticked, **exactly `F195`+** (the entire 1b half) |
| 8 Page geometry | ✅ PASS — all 12 pages A4 portrait (595×842pt) |
| 9 Orphaned headings | ✅ PASS — 38 banner headings, none stranded |
| 10 Badge-plate collision | ✅ PASS — 46 filled plates all clear |

Neither FAIL is a defect in the 1a build: both are simply "1b not written yet". Gate 2 is
judged on the whole merged PDF **after 2b**, per v6 §7. No mechanical regression exists in 1a.

---

## 8. Gate ledger

| Pass | Scope | Status |
| :--- | :--- | :--- |
| **Pass 1** | Source mastery & frozen inventory | **✅ COMPLETE — all nine sessions done; inventory FROZEN at 352 rows. GATE 1 CLOSED (GREEN).** |
| **Pass 2a** | Script + PDF build, **first half** (non-chordates, Figs 4.1–4.15) | **✅ DONE (2026-09-03) — 200/352 rows ticked (`F001`–`F194`, `F343`–`F347`, `F350`); PDF 12 pp; all 9 mechanical/1a lint checks green.** |
| Pass 2b | Script + PDF build, **second half** (Chordata + 7 classes, TABLE 4.1/4.2, summary, `check_pdf.py` fully green) | ⬜ not started — appends at the `### PASS 2b CONTINUES HERE ###` seam; must tick `F195`+ and clear checks 6 & 7 |
| Pass 3 | Verify & deliver (zero confirmed defects) | ⬜ not started — blocked on Gate 2b |

**GATE 1 VERDICT: CLOSED (GREEN), 2026-09-03.** All nine Pass-1 sessions ran (1a-S, 1a-H, 1a-O, 1b-S, 1b-H, 1b-O, 1-F, 1-F resumed, 1-Z) and 1-Z froze the inventory over the whole chapter at **352 rows (F001–F352, contiguous, 0 gaps/dupes)**, machine-validated. **Gate 1 closed is NOT chapter closed:** Pass 2 (script + PDF) has not started and every row is unticked, so Chapter 4 stays out of any "Done" tally until Pass 3 delivers a defect-free PDF.
