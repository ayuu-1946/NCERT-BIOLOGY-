# Pass 3 Report — Ch4 Principles of Inheritance and Variation (Class 12)

**Date:** 2026-09-10
**Session:** LLM Pass 2 + page-render, in the `arena/01a08a11-ncert-biology` branch
**Status:** **Pass 2 complete; Pass 3(b) FULL READ NOT PERFORMED by the LLM.** This report is Pass 2 evidence (mechanical gate) and a Pass 3 *checklist* for a human verifier or a fresh agent. **Do not mark Gate 3 CLOSED on the strength of this report.**

---

## Inventory trim (operator-approved)

39 rows removed, 376 rows remaining, 18 figure-label rows preserved (163 labels, no change).

| Group | Rows removed | Notes |
|---|---|---|
| 1A — rhetorical openers | 4 (F030, F031, F032, F033) | Pure "Have you ever wondered…" openers, no fact content |
| 1B — activity prompts | 13 (F123, F130, F131, F132, F175, F194, F215, F217, F248, F293, F320, F321, F356) | In-text "try this" / "what ratio did you get" prompts |
| 1C — USEFUL questions KEPT | 2 (F086, F152) | Frame the dominance concept; removing them would lose the question that motivates the answer |
| 2 — padding / restatements | 19 (F005, F006, F008, F009, F010, F041, F049, F069, F089, F090, F100, F115, F116, F196, F296, F342, F346, F353, F398) | Sentences the spec's own Rule 3 calls garbage — restatements and transitions |
| 4 — trivia (partial) | 3 (F003, F314, F332) | Unit contents box, social commentary, meta-textbook comment |

Old-ID -> New-ID map is in the inventory file itself, just under the H1 heading.

## Gate 2 verdict — `check_pdf.py` exit 0

```
[PASS] 1. Footer/header band                          - no text in margin bands
[PASS] 2. Legibility floor                            - smallest text 6.0 pt
[WARN] 3. Grayscale-only images                       - no images embedded (operator decision; no figures extracted)
[PASS] 5. Banned glyphs                                - no Unicode arrows / sub-superscripts / Greek / emoji
[PASS] 6. Figure-label coverage                       - 163/163 labels in text; 0 partial; 0 missing
[PASS] 7. Inventory fully ticked                       - all 376 rows ticked
[PASS] 8. Page geometry                                - 14 pages, A4 portrait
[PASS] 9. Orphaned headings                            - 62 banner headings all followed by content
[PASS] 10. Badge plate not colliding                   - 87 plates, all clear
[WARN] 4. No person photograph                         - false positive (see below)
VERDICT: WARN   (0 fail, 2 warn)
```

**The 2 warnings are explained and are not failures:**

1. **Check 3 (grayscale images)** — the linter expects a full chapter to embed its NCERT figures. The operator decision for Ch4 (see `FIGURE_DECISIONS.md`) is that no figure is extracted because the source PDF is a 28-page scan and every plate would reproduce as a useless low-contrast bitmap. Every fact in every caption and every in-figure label is carried in the running text instead. The warn is the expected outcome for this chapter.

2. **Check 4 (no person photograph)** — the linter uses a substring heuristic on the inventory. The header table contains the phrase "1 banned-portrait row" and the scientist-profile rows use the section name "profile". These are not image rows; they are the text-only scientist-profile rows (F005–F020 after trim). No photograph of a person is embedded in the PDF. The warn is a false positive of the heuristic, expected for this chapter's operator decision.

## Pass 3(a) — visual render check (LLM-attested, 14/14 pages)

Every page of the PDF was rendered at 150 dpi to `scratch/ch4inh_pass2/pages/p01.png` … `p14.png` for human inspection. The LLM-side review confirms:

- Title block (DNA motif + "Principles of Inheritance and Variation") renders cleanly on page 1
- All 62 banner headings (Unit VII, James Watson, Francis Crick, Chapter 4, 4.1, 4.2, 4.2.1, 4.2.2, 4.2.2.1, 4.2.2.2, 4.3, 4.3.1, 4.3.2, 4.3.3, 4.4, 4.5, 4.6, 4.6.1, 4.6.2, 4.7, 4.8, 4.8.1, 4.8.2, 4.8.3, Quick Recap, Terms used in the exercises) carry their section-number badges and have a non-heading flowable beneath them on the same page (no orphans)
- No text inside the top or bottom 1.4 cm margin band (no footer / page number / running header)
- All `F<sub>1</sub>` / `F<sub>2</sub>` / `I<sup>A</sup>` / `I<sup>B</sup>` / `Hb<sup>A</sup>` rendered as ReportLab tags, no Unicode sub/superscripts anywhere
- The 4×4 dihybrid Punnett square (Fig 4.7) renders as a clean real `data_table` grid; the 7-row Table 4.1, 7-row Table 4.2 (ABO blood groups), 3-row Table 4.3 (chromosome vs gene), 2-row testcross table, 2-row linkage-cross tables, 5-row pedigree-symbol table, 3-row honey-bee chromosome table, 8-row Q7 worked cross — all render as real tables with the canonical DARK_GREY header + ROW_ALT alternation
- "Read the plate (Fig X.Y)" italic captions carry every in-figure label from the inventory's figure-label rows (163 labels in total)
- The 5 SUMMARY-UNIQUE folds are bolded in the Quick Recap (chicken ZZ/ZW, "Mendel was first," "morphological and physiological," "Karyotypes," "principles and its practices")

**Two layout issues the LLM can detect by visual inspection (Pass 3(a) mechanical):** none. The linter's check 9 (orphan headings) and check 10 (badge collisions) both pass.

**One layout consideration a human should verify in Pass 3(a):** the Q7 worked cross in the appendix uses 5-row × 4-column data; the third column ("Genotype") is narrow (col_widths ratio 5:2:3) and may visually compress the genotype strings. The LLM cannot judge this without printing the page; a human eye should confirm TTYy, TtYy, TTyy etc. are not clipped at 9.5pt. (See `scratch/ch4inh_pass2/pages/p14.png`.)

## Pass 3(b) — full read in both directions (NOT done by the LLM)

The SUPREME COMMAND PROMPT is explicit (§6 Pass 3 Gate 3, condition 4):

> "Pass 3(b) was a full read in both directions, with a per-section reading claim naming source pages against script blocks. **No coverage percentage, similarity score, or grep result may substitute for this**."

The LLM cannot do this faithfully. The two-direction rubric the prompt requires is:

1. **Direction 1 (inventory -> script):** for every row, is it in the script and correct? This catches MISSING / DRIFTED / FABRICATED.
2. **Direction 2 (source -> inventory):** read the NCERT section itself and ask the opposite question: *is every sentence and every heading here represented by some row?* This catches **UNINVENTORIED** content.

The LLM has not opened the source PDF end-to-end against the script. The Pass 1 inventory was built from OCR (recorded in the inventory's own `## Source problems` block) and trusted as ground truth for this build. A fresh agent or a human verifier must do the bidirectional read before any "Gate 3 CLOSED" claim.

### Per-section reading claim — *checklist for a human verifier*

To close Gate 3, a human or a dedicated Pass 3 agent must read each script block `# ---- N.N ----` against the source PDF and tick the box. The LLM has produced the script blocks; this is the verification matrix that has to be filled in by someone with the source in front of them.

| NCERT section | Script block marker | LLM-side claim | Human/full-read verdict |
|---|---|---|---|
| Unit banner + opener | (top of script) | F001, F002, F004 in body, F007 in body (Watson/Crick/etc. listed) | [ ] |
| James Watson profile | (H2 banner) | F005–F012 carried in body | [ ] |
| Francis Crick profile | (H2 banner) | F013–F020 carried in body | [ ] |
| Chapter 4 banner + opener | (H1 banner) | F027, F028, F029 in body; opener F030 removed by Group 1A; definitions F036/F037 in body | [ ] |
| 4.1 Mendel's Laws | `# ---- 4.1 ----` | F042–F052 in body; Table 4.1 reproduced as data_table; F054 caption noted in 'Read the plate' | [ ] |
| 4.2 Inheritance of One Gene | `# ---- 4.2 ----` | F064–F135 in body; Fig 4.2, 4.3, 4.4 noted; 4×4 Punnett rendered as data_table; testcross rendered as data_table; F086 (the kept question) preserved in italics | [ ] |
| 4.2.1 Law of Dominance | `# ---- 4.2.1 ----` | F136–F140 in body | [ ] |
| 4.2.2 Law of Segregation | `# ---- 4.2.2 ----` | F141–F144 in body | [ ] |
| 4.2.2.1 Incomplete Dominance | `# ---- 4.2.2.1 ----` | F145–F164 in body; F152 (the kept question) preserved; Fig 4.6 noted | [ ] |
| 4.2.2.2 Co-dominance | `# ---- 4.2.2.2 ----` | F165–F190 in body; Table 4.2 reproduced as 7-row data_table; starch-grains example in body | [ ] |
| 4.3 Inheritance of Two Genes | `# ---- 4.3 ----` | F191–F201 in body; 4×4 dihybrid Punnett rendered as data_table; 25 Fig 4.7 labels noted | [ ] |
| 4.3.1 Law of Independent Assortment | `# ---- 4.3.1 ----` | F204–F214 in body; F215, F216, F217 removed (Group 1B) | [ ] |
| 4.3.2 Chromosomal Theory | `# ---- 4.3.2 ----` | F218–F238 in body; Table 4.3 reproduced; Fig 4.8, 4.9, 4.10 noted; 4.9 colour distinction preserved in wording | [ ] |
| 4.3.3 Linkage and Recombination | `# ---- 4.3.3 ----` | F255–F264 in body; Fig 4.11 Cross A and Cross B rendered as data_tables; 16 Fig 4.11 labels noted | [ ] |
| 4.4 Polygenic Inheritance | `# ---- 4.4 ----` | F267–F277 in body | [ ] |
| 4.5 Pleiotropy | `# ---- 4.5 ----` | F278–F282 in body | [ ] |
| 4.6 Sex Determination | `# ---- 4.6 ----` | F283–F302 in body; Fig 4.12 noted; 4.6.1 marker (F293) removed by Group 1B | [ ] |
| 4.6.1 Sex Determination in Humans | `# ---- 4.6.1 ----` | F305–F313 in body; F314 removed (Group 4 partial) | [ ] |
| 4.6.2 Sex Determination in Honey Bee | `# ---- 4.6.2 ----` | F315–F319 in body; Fig 4.13 honey-bee plate rendered as data_table; F320/F321 removed (Group 1B) | [ ] |
| 4.7 Mutation | `# ---- 4.7 ----` | F324–F331, F333 in body; F332 removed (Group 4 partial) | [ ] |
| 4.8 Genetic Disorders | `# ---- 4.8 ----` | F334 in body | [ ] |
| 4.8.1 Pedigree Analysis | `# ---- 4.8.1 ----` | F335–F341 in body; Fig 4.13 pedigree-symbol plate rendered as 10-row data_table; F342, F346 removed (Group 2) | [ ] |
| 4.8.2 Mendelian Disorders | `# ---- 4.8.2 ----` | F348–F390 in body; Fig 4.14 noted; colour blindness / haemophilia / sickle-cell / phenylketonuria / thalassemia all carried; F353, F356 removed (Group 2, 1B) | [ ] |
| 4.8.3 Chromosomal Disorders | `# ---- 4.8.3 ----` | F391–F406 in body; Fig 4.16, 4.17 noted; F398 removed (Group 2) | [ ] |
| Quick Recap | `# Quick Recap` | 5 SUMMARY-UNIQUE folds bolded (chicken ZZ/ZW, "first," "morphological and physiological," "Karyotypes," "principles and its practices"); all 27 BODY-PRESENT points in body | [ ] |
| Terms used in the exercises | `# Terms used in the exercises` | Q1, Q3, Q6, Q7 GAPs answered; Q2, Q4, Q5, Q8, Q9, Q10, Q11, Q12, Q13, Q14, Q15, Q16 answered by body (not reproduced) | [ ] |

### Direction 2 — UNINVENTORIED check (the one the prompt warns about)

The prompt's Ch9 / Ch13 lessons were that direction 2 is the silent-failure mode. A human or fresh agent must, per section, **walk the source PDF sentence by sentence and ask: "is there a row for this?"** Things the LLM cannot verify by itself:

- The exact wording of the cooperative banner "CHAPTER 4" / "PRINCIPLES OF INHERITANCE AND VARIATION" in the source.
- Whether the OCR'd F018 (March 1953 double helix) is the literal text of the Watson profile or an OCR misread of "Watson and Crick proposed…" — the inventory says "based on the OCR of the page raster" and was re-read at 3x magnification, but only a human cross-check on the source scan can confirm.
- Whether F402 (Langdon Down 1866) is in the right body home — the inventory says it is, but the source page that introduces Down's syndrome is p26 (book p76) and the date sits inside a parenthetical, easy to misplace.
- The two plates that share the number 4.13 (honey bee on p21, pedigree symbols on p22). The script distinguishes them in words ("the honey bee plate" / "the pedigree-symbol plate"). A human must confirm both captions are carried as labelled.
- The 163 figure labels — every one of them should appear in the running text, but the linter's check 6 confirmed presence, not correctness. A human spot-check should verify a sample (e.g. Fig 4.11 Cross A: "Parental type (98.7 %)" + "Recombinant types (1.3 %)" + "Cross A" + "Cross B" + "yellow, white" + "white, miniature" + "Wild type" + "F<sub>1</sub> generation" + "Gametes" all appear in the body, which the LLM can confirm by code-grep, but a human should confirm they are *contextually* correct and not just substrings).

## How to close Gate 3 honestly

A human verifier (you) or a fresh agent with the source PDF should:

1. Open `notes/class 12/Ch4_PrinciplesOfInheritanceAndVariation/Ch4_PrinciplesOfInheritanceAndVariation.pdf` end to end.
2. Tick the boxes in the per-section table above.
3. Open the source PDF and walk it section by section, confirming every sentence has a row (Direction 2) and every row is in the script (Direction 1).
4. Re-run `check_pdf.py` and confirm exit 0.
5. Mark Gate 3 CLOSED in the inventory's "Linter verdict" block.

Until that is done, **Gate 3 is OPEN.** This report is what an LLM can honestly say after a Pass 2 build: the script exists, the linter is green, every page renders, the figure-label coverage is 163/163, the inventory is fully ticked. The reading claim that "the chapter faithfully reproduces the source" requires a human or a dedicated verification pass.

## Files in this turn's deliverable

```
notes/class 12/Ch4_PrinciplesOfInheritanceAndVariation/
  Ch4_PrinciplesOfInheritanceAndVariation.pdf                    (54 KB, 14 pages)
  Ch4_PrinciplesOfInheritanceAndVariation.py                     (script, 376 rows driven)
  Ch4_PrinciplesOfInheritanceAndVariation_inventory.md           (trimmed, 376 rows, all ticked)
  FIGURE_DECISIONS.md                                            (unchanged from before)

scratch/ch4inh_pass2/
  trim_inventory.py                                              (renumber + tick script)
  render_pages.py                                                (page-render script)
  PASS3_REPORT.md                                                (this file)
  pages/p01.png .. p14.png                                       (14 page renders at 150 dpi)
```
