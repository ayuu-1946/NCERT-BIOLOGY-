# Chapter Production Status

Tracking every chapter against the **v6 gated pass workflow** defined in `SUPREME COMMAND PROMPT.md`.

**Pipeline:** `Pass 1 → [Gate 1] → Pass 2 → [Gate 2: check_pdf.py green] → Pass 3 → [Gate 3: zero confirmed defects] → deliver`

**Gate legend**
- **Gate 1** — Frozen, numbered inventory + figure manifest + figure-label matrix complete (Pass 1).
- **Gate 2** — `check_pdf.py` exits 0 (no FAILs); any WARN eyeballed and confirmed benign.
- **Gate 3** — Zero confirmed defects remain AND `check_pdf.py` still green; full chapter folder delivered.

**Deliverables per chapter (§0.5):** `<Chapter>.pdf` · `<Chapter>.py` · `<Chapter>_inventory.md` (with figure-label matrix) · `assets/`. Shared repo-level files: `neet_template.py`, `check_pdf.py`.

**Status legend:** ✅ complete · ⚠️ green but not independently re-verified this cycle · ⬜ not started · ▶️ in progress

---

## Overview table

| # | Chapter | Class | Gate 1 (inventory) | Gate 2 (`check_pdf.py`) | Gate 3 (defects) | Deliverables | Overall |
|---|---------|-------|--------------------|-------------------------|------------------|--------------|---------|
| 1 | The Living World | 11 | ✅ 121 facts frozen · 14/14 labels · 3 summary-unique folded | ✅ WARN (0 fail, **1 benign warn**) · 7 pp · 1 mono img | ✅ zero confirmed defects | ✅ pdf · py · inventory · assets | **✅ FULLY COMPLETE — CLOSED** |
| 2 | Biological Classification | 11 | ✅ 192 facts frozen · 26/26 labels | ✅ WARN (0 fail, **1 benign warn**) · 15 pp · 6 mono imgs | ⏳ Pass 3 pending | ✅ pdf · py · inventory · assets | **🟡 PASS 2 COMPLETE — PASS 3 PENDING** |
| 8 | Cell: The Unit of Life | 11 | ✅ 325 facts frozen · 82/82 labels · 6 summary-unique folded | ✅ WARN (0 fail, **1 benign warn**) · 18 pp · 14 mono imgs | ✅ zero confirmed defects | ✅ pdf · py · inventory · assets | **✅ FULLY COMPLETE — CLOSED** |
| 9 | Biotechnology: Principles and Processes | 12 | ✅ 200 facts frozen · 38/38 labels | ✅ WARN (0 fail, **1 benign warn**) · 13 pp · 7 mono imgs | ✅ zero confirmed defects | ✅ pdf · py · inventory · assets | **✅ FULLY COMPLETE — CLOSED** |
| 10 | Biotechnology and its Applications | 12 | ✅ 147 facts frozen · 10/10 labels · 14 summary rows | ✅ PASS (0 fail, **1 benign warn**) · 8 pp · 3 mono imgs | ✅ zero confirmed defects | ✅ pdf · py · inventory · assets | **✅ FULLY COMPLETE — CLOSED** |

---

## Chapter 1 — The Living World — ✅ FULLY COMPLETE (CLOSED)

Verified closed under the supreme command prompt v6 on 2026-08-19. Resumed mid-workflow after a prior run stopped on credit limit immediately after "Task 0 of 5 complete"; Gate 1 was independently re-verified against current files (not trusted from prior-run prose) before Pass 2 began. Pass 3 (dual verification) run to Gate 3 closure in this cycle.

| Workflow stage | Evidence |
|----------------|----------|
| **Environment resume** | Sandbox was fresh (venv not persisted by git); rebuilt `.venv` with `reportlab 5.0.0` / `pymupdf 1.28.2` / `Pillow 12.3.0`. Not a §0 restart — no re-extraction, no re-render of source, no Fig 1.1 re-extraction; all reused as-is. |
| **Gate 1 (independently confirmed)** | 121 Facts rows (F001-F121) contiguous, all ticked, header `Rows: 121` matches; all 6 required inventory sections present; figure-label matrix present and parses to 7/7 real labels incl. exact phrase "Phylum or Division"; summary classification (10 rows, 3 SUMMARY-UNIQUE); exercise-gap terms (10 rows, Q1-Q10); figure manifest (1 row, `Mono: yes`, `Verified: yes`); `assets/fig_1_1.png` on disk, `mode=L`, 0 colored px; `git status`/`git diff HEAD` clean on the Ch1 folder — no corruption since prior run. |
| **Pass 2 / Gate 2** | `check_pdf.py` → **VERDICT WARN, 0 fail / 1 warn, exit 0**. Checks 1,2,3,5,6,7,8 PASS. 7 × A4-portrait pages, **1 monochrome image** (Fig 1.1), all 121 rows ticked, 14/14 figure labels covered in running text. |
| **The 1 warning** | Check 4 photo-keyword heuristic — a **confirmed benign false positive**. Fires on the 10 Ernst Mayr biography rows (F013-F022) because their inventory `Type` column is literally "Profile", and `"profile"` is one of the checker's `PORTRAIT_HINTS` substrings. Independently confirmed only 1 image is embedded in the whole PDF (Fig 1.1, colorspace=1/gray) — the Mayr content is a text-only block, no photograph. |
| **Fixes applied** | (1) Removed an invented figure-caption sentence ("Reading the arrows upward…") not present in NCERT; restored exact frozen F108 wording. (2) Replaced a `process_flow` misuse for the taxonomic hierarchy (falsely implying species→kingdom is a sequential procedure) with a rank `data_table`, ascending order matching Fig 1.1, no new facts introduced. (3) Dropped the decorative `has_table=True` flag on two headings — the frozen template renders its table-icon cell outside the banner fill, leaving a stray glyph; omitted at chapter level rather than patching the frozen module. (4) Wrapped Table 1.1's intro line + 4 rows + reading NOTE in `KeepTogether` to fix an orphan-row page split. |
| **False positives correctly rejected** | Check 6's apparent "2 missing labels" traced to `_extract_labels` mis-parsing the Figure-label matrix's own markdown header row as data; fixed by rewording only the column caption (no fact/label/tick touched). The "two implicit questions" `process_flow` at 1.1 was left as-is — the source itself says "the first… the second", so numbering is source-grounded. |
| **Colour-dependent figures** | Fig 1.1 is a monochrome hierarchy diagram with no colour-encoded meaning; verified legible at 1-bit B&W threshold render. |
| **Deliverables** | `Ch1_TheLivingWorld.pdf` · `.py` · `_inventory.md` (with figure-label matrix) · `assets/fig_1_1.png`. |
| **Pass 3 / Gate 3** | **Zero confirmed defects.** Pass 3(a): all 7 pages rendered + inspected; cross-page style identity confirmed (template held). **One layout defect found and fixed** — the `Table 1.1` banner was orphaned at the bottom of page 5, split from its table; fixed by folding `heading("Table 1.1", …)` into the table's `KeepTogether` (`# [VERIFICATION FIX]`). Pass 3(b): full-read cross-check of all 121 rows against source → **121/121 COVERED, 0 MISSING / 0 FABRICATED / 0 DRIFTED**; every number/date verbatim; Fig 1.1's 7 labels all in text. `check_pdf.py` re-run after the fix: still **0 fail / 1 benign warn, exit 0**, 7 pp. |

---

## Chapter 2 — Biological Classification — 🟡 PASS 2 COMPLETE (PASS 3 PENDING)

Pass 2 verification completed under the supreme command prompt v6 on 2026-08-19. Pass 2 resumed from the existing successful build; Gate 1, source extraction, figure regeneration, and Pass 2 script generation were not repeated. Chapter 2 is not closed until Pass 3 / Gate 3 is completed.

| Workflow stage | Evidence |
|----------------|----------|
| **Pass 2 / Gate 2** | `check_pdf.py` → **VERDICT WARN, 0 fail / 1 warn, exit 0**. Checks 1, 2, 3, 5, 6, 7, 8 PASS. 15 × A4-portrait pages, **6 monochrome images**, all 192 Facts rows ticked. |
| **The 1 warning** | Check 4 photo-keyword heuristic — a **confirmed benign false positive**. It matches “photo” inside textual mentions of photosynthetic biology terms/profile hints; no scientist portrait is embedded. Check 3 independently confirms the 6 embedded images are the required monochrome biology figures. |
| **Pass 2 visual QA** | **PASS.** All 15 pages rendered and inspected: figures, tables, captions, page breaks, typography, clipping/overflow, collisions, blank pages, banned glyphs, and monochrome print safety were checked. No genuine visual defects found. |
| **Genuine defects** | **None.** The initial Gate 2 check-7 failure was bookkeeping only: all 192 facts were present in the PDF but the inventory tick column was not updated. After verifying coverage, all 192 rows were ticked and the linter re-run successfully. |
| **Deliverables** | `Ch2_BiologicalClassification.pdf` · `.py` · `_inventory.md` (with figure-label matrix) · `assets/` (6 mono PNGs). |
| **Next required step** | Pass 3 — Gate 3 dual verification: cross-page visual style consistency and full-read content cross-check against the frozen inventory. |

---

## Chapter 8 — Cell: The Unit of Life — ✅ FULLY COMPLETE (CLOSED)

Big-chapter 5-pass protocol (`1a → 1b → [Gate 1] → 2a → 2b → [Gate 2] → 3 → [Gate 3]`). Verified closed under the supreme command prompt on 2026-08-19.

| Workflow stage | Evidence |
|----------------|----------|
| **Pass 1 / Gate 1** | Frozen inventory of **325 Facts rows** (F001-F325) inventoried in two halves into one file; figure manifest + figure-label matrix (**82/82** in-figure labels present in running text); **6 summary-unique** facts folded into their named body sections (F308, F310, F312, F314, F317, F319); 2 exercise gaps closed from chapter facts (Q9 division of labour, Q13 centrosome). |
| **Pass 2 / Gate 2** | `check_pdf.py` → **VERDICT WARN, 0 fail / 1 warn, exit 0**. Checks 1,2,3,5,6,7,8 PASS. 18 × A4-portrait pages, **14 monochrome images** (13 figures, Fig 8.3 split a/b), all 325 rows ticked. |
| **The 1 warning** | Check 4 photo-keyword heuristic — a **confirmed benign false positive**. Fires only on the `phot`+`o` substring inside **photosynthetic** (F112) and **photosynthesis** (F213); both are running-text biology rows, neither a figure-manifest row nor a person image. No person photograph embedded; the G.N. Ramachandran biography is a text-only `[NOTE]` box. |
| **Pass 3 / Gate 3** | **Zero confirmed defects.** Pass 3(a): all 18 pages rendered actual-size + print-DPI B&W 1-bit, zero layout defects, cross-page style identity confirmed (template held). Pass 3(b): fresh source re-extraction full-read against all 325 rows → **325/325 COVERED, 0 MISSING / 0 FABRICATED / 0 DRIFTED**; every qualifier, number and µm value preserved verbatim. Historical page-16 Fig 8.13 "overlap" re-confirmed as a false positive on the fresh render. No `# [VERIFICATION FIX]` edit needed. |
| **Colour-dependent figures** | Fig 8.4 (fluid mosaic) and Fig 8.10(b) (cilia/flagella): each caption restates every part by position/shape/geometry so the distinction survives monochrome. |
| **Source problems** | Micron glyph rendered `mm` by pdfplumber (re-read from render as µm); "endoplasmic reticulun" typo; body-vs-summary plastid-location contradiction (body kept, flagged); "Central microtuble" label typo (preserved verbatim). All handled, none unrecoverable. |
| **Deliverables** | `Ch8_CellTheUnitOfLife.pdf` �� `.py` · `_inventory.md` (with figure-label matrix + Gate 3 closure + Coverage note) · `assets/` (14 mono PNGs). |

---

## Chapter 10 — Biotechnology and its Applications — ✅ FULLY COMPLETE (CLOSED)

Verified closed under the supreme command prompt.

| Workflow stage | Evidence |
|----------------|----------|
| **Pass 1 / Gate 1** | Frozen inventory of **147 Facts rows** + **14 summary rows**; figure manifest + figure-label matrix (**10/10** labels present in running text). |
| **Pass 2 / Gate 2** | `check_pdf.py` → **VERDICT WARN, 0 fail / 1 warn, exit 0**. Checks 1,2,3,5,6,7,8 PASS. 8 × A4-portrait pages, 3 monochrome images, all 147 rows ticked. |
| **The 1 warning** | Check 4 photo-keyword heuristic — a **confirmed benign false positive**. Fires on three *textual* mentions only (F103 "photographic film"; Fig 10.1 caption colour description; Fig 10.1 hand-in-source note). No person photograph is embedded (Check 3 confirms all 3 images monochrome). |
| **Pass 3 / Gate 3** | **Zero confirmed defects.** Cross-page visual render inspected; content cross-checked against frozen inventory. |
| **Grounding** | 147/147 rows ≥ 80% grounded against fresh source. **F129** (10.4 biopiracy "vigilance" qualifier) — full-read confirmed genuinely MISSING, restored verbatim-in-fact, now grounds **97.1%** (was 62%). |
| **Fixes preserved** | Fig 10.1 watermark removal · split-table `KeepTogether` · Fig 10.1/10.2/10.3 caption corrections · Fig 10.3 A/B chain clarification · appendix Q6 row · colour-dependent-figure corrections · GMO banner icon-table placement · F129 restoration. |
| **Deliverables** | `Ch10_BiotechnologyAndItsApplications.pdf` · `.py` · `_inventory.md` · `assets/`. |

---

## Chapter 9 — Biotechnology: Principles and Processes — ✅ FULLY COMPLETE (CLOSED)

Verified closed under the supreme command prompt on 2026-08-19.

| Workflow stage | Evidence |
|----------------|----------|
| **Pass 1 / Gate 1** | Frozen inventory of **200 Facts rows**; figure manifest + figure-label matrix (**38/38** labels present in running text). |
| **Pass 2 / Gate 2** | `check_pdf.py` → **VERDICT WARN, 0 fail / 1 warn, exit 0**. Checks 1,2,3,5,6,7,8 PASS. 13 × A4-portrait pages, **7 monochrome images** (the 7 numbered figures Fig 9.1–9.7), all 200 rows ticked. |
| **The 1 warning** | Check 4 photo-keyword heuristic — a **confirmed benign false positive**. Fires on the Section-wise coverage row `Boyer profile … text-only by design (no person photo)`; the heuristic matches the word "photo" inside the phrase *"no person photo"* — a sentence **denying** a photo. No Boyer portrait is embedded (Check 3 confirms all 7 images monochrome and are the numbered figures); the Herbert Boyer profile is text-only by design. **Accepted, not suppressed** — the "no person photo" phrasing is deliberately not reworded to silence the linter, exactly as Ch8's `photosynthetic` WARN was handled. |
| **Pass 3 / Gate 3** | **Zero confirmed defects.** Pass 3(a): all 13 pages inspected, zero layout defects, cross-page style identity confirmed (template held). Pass 3(b): fresh source re-extraction full-read against all 200 rows → **200/200 COVERED, 0 MISSING / 0 FABRICATED / 0 DRIFTED**; historical defects 4/5/6 re-tested at their exact original sites and re-confirmed correct against source. No `# [VERIFICATION FIX]` edit to the `.py` needed (the one documentary fix was the inventory header row-count line). |
| **Colour-dependent figures** | Fig 9.1 (vector vs foreign DNA), Fig 9.4 (pBR322 `ampR`/`tetR`/`ori`/`rop` arcs) and Fig 9.6 (PCR amplified region): each caption restates the distinction by outline/solid/label/boundary so meaning survives monochrome. |
| **Source problems** | Page-number digits bleeding into text (`168 15-100`, `117722`); unit-opening page interleaving intro with the chapter-list sidebar; degree glyph lost as `420C`; `β` lost from beta-galactosidase; "two sets of primers" split across a page break. All recovered by reading the rendered source page; none unrecoverable. The Herbert Boyer photograph is a deliberate exclusion, not a problem. |
| **Deliverables** | `Ch9_BiotechnologyPrinciplesAndProcesses.pdf` · `.py` (+ `convert_figures_mono.py` helper) · `_inventory.md` (with figure-label matrix + Gate 3 closure + Coverage note) · `assets/` (7 mono PNGs). |
