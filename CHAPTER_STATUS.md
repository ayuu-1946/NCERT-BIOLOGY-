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
| 2 | Biological Classification | 11 | ✅ 192 facts frozen · 26/26 labels · 2 summary-unique folded | ✅ WARN (0 fail, **1 benign warn**) · 15 pp · 6 mono imgs | ✅ zero confirmed defects (2 found + fixed) | ✅ pdf · py · inventory · assets | **✅ FULLY COMPLETE — CLOSED** |
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

## Chapter 2 — Biological Classification — ✅ FULLY COMPLETE (CLOSED)

Pass 2 verification completed under the supreme command prompt v6 on 2026-08-19. Pass 3(a) — the visual render check — completed on 2026-08-20. **Pass 3(b) — the full-read content cross-check — completed 2026-08-20, Gate 3 closed the same day.** The sandbox was fresh at the start of the Pass 3(b) session (venv is not persisted by git); `.venv` was rebuilt with `reportlab 5.0.0` / `pymupdf 1.28.2` / `Pillow 12.3.0`. Not a §0 restart — no re-extraction of figures, no re-render of source assets; Gate 2 was re-confirmed green on the existing PDF before Pass 3(b) began.

| Workflow stage | Evidence |
|----------------|----------|
| **Pass 2 / Gate 2** | `check_pdf.py` → **VERDICT WARN, 0 fail / 1 warn, exit 0**. Checks 1, 2, 3, 5, 6, 7, 8 PASS. 15 × A4-portrait pages, **6 monochrome images**, all 192 Facts rows ticked. Gate 2 re-confirmed green on 2026-08-20 before Pass 3 began (smallest text 6.0pt; 26/26 labels in text; all pages A4 portrait). |
| **The 1 warning** | Check 4 photo-keyword heuristic — a **confirmed benign false positive**. It matches “photo” inside textual mentions of photosynthetic biology terms/profile hints (F007, F032, F041, F048, F064, F070, F076, F085); no scientist portrait is embedded. Check 3 independently confirms the 6 embedded images are the required monochrome biology figures. |
| **Pass 3(a) — visual render check** | **PASS — zero layout defects.** All 15 pages rendered with pymupdf at actual size (150 dpi) and at a 1-bit B&W print-safety threshold, each inspected directly. Verified: no overflow/clipping, no orphaned headings, no squashed figures, no table running off the page, process-flow rules aligned with their triangle badges (fungal sexual cycle p8; virus discovery p12), figures boxed with captions, NOTE (solid rule + `!`) vs MEMORY AID (dashed border + star) tell-apart-able in B&W. Cross-page style identity confirmed by comparing H1/H2/H3 banners, tables, boxes and figure boxes from ≥3 points in the chapter — **template held, no drift**. |
| **Badge micro-text reviewed, not a defect** | The `Quick Recap` and `Terms Used in the Exercises` headings feed text labels (`"Recap"`, `"Appendix"`) into the section-number badge. `neet_template._badge_section` grows the plate sideways to fit at a ≥6pt floor (never clips), and the closed, Gate-3-passed Ch1 uses the identical `heading("Recap", …)` / `heading("Appendix", …)` calls. Kept as-is for cross-chapter consistency (check 2 passed at 6.0pt smallest). |
| **Source watermark** | Faint NCERT "not to be republished" watermark is visible on some extracted figures (Fig 2.1, 2.2, 2.4, 2.6). It originates in the source PDF, not the layout. Flagged for optional cleanup during Pass 3(b); not a layout defect. |
| **Genuine layout defects** | **None.** No `# [VERIFICATION FIX]` edit to the `.py` was required by Pass 3(a). |
| **Pass 3(b) — content cross-check** | **Complete.** Fresh `pdfplumber` re-extraction of all 13 source pages, read start-to-finish (not grepped) against all **192 Facts rows** and all **6 figure-label rows**, section pair by section pair. Result after fixes: **192/192 COVERED, 0 MISSING / 0 FABRICATED / 0 DRIFTED**; every scientist, date, taxon name, qualifier and Table 2.1 cell verbatim; 26/26 in-figure labels found in running text at their own topic. Figure-label rows L01-L06, previously unticked, are now ticked in the inventory (Gate 2's check 7 only gates Facts rows, so they had never been machine-gated). |
| **Defect 1 found + fixed (F169, MISSING)** | The 2.6a virus-discovery process flow gave Beijerinck only "called the fluid as *Contagium vivum fluidum*" and had dropped NCERT's "**named the new pathogen 'virus'**" — the naming of the virus itself, a directly examinable fact. Restored verbatim ahead of the fluid name (`# [VERIFICATION FIX]`). |
| **Defect 2 found + fixed (F163, DRIFTED)** | The 2.6 opening had been reflowed to "no mention of some acellular organisms like viruses and viroids, prions and lichens", which reads **lichens as acellular**. NCERT groups them differently: "no mention of **lichens** *and* some acellular organisms like viruses, viroids and prions" — a lichen is a *cellular* alga+fungus association, excluded from the five kingdoms for a different reason. Original grouping restored plus one explicit clarifying clause (`# [VERIFICATION FIX]`). |
| **Re-verification after the fixes** | PDF regenerated; both fixes land on rendered page 12, which was re-rendered and inspected: text correct, process-flow badges 1/2/3 still aligned to their rules, no orphan/overflow introduced, page count unchanged at 15. `check_pdf.py` re-run: still **0 fail / 1 benign warn, exit 0**. Only the fixed block was re-verified — nothing else changed. |
| **Documentary fix** | The script's source-spelling policy header listed 2 normalised source typos; the full read turned up a third — "Multiceullar" in the Table 2.1 body-organisation row for Fungi (normalised to "Multicellular" in the table). Added to the policy header and to the inventory's Source problems, so all three normalisations are recorded rather than silent. |
| **Source watermark — accepted, not a defect** | Faint NCERT "not to be republished" watermark in the source artwork of Fig 2.1, 2.2, 2.4, 2.6. Re-examined during Pass 3(b) as flagged: it carries no meaning and obscures no in-figure label (all 26 read cleanly), so it was left as-is — retouching an original NCERT figure is a larger risk than the watermark. |
| **Deliverables** | `Ch2_BiologicalClassification.pdf` (15 pp) · `.py` · `_inventory.md` (figure-label matrix ticked + section-wise coverage + Gate 3 closure + Coverage note) · `assets/` (6 mono PNGs). |
| **Pass 3 / Gate 3** | **Zero confirmed defects remain AND `check_pdf.py` green.** Gate 3 closed 2026-08-20 — chapter delivered. |

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
