# Gate 3 Findings — Ch4 Principles of Inheritance and Variation (Class 12)

**Date:** 2026-09-12  
**Branch:** `arena/01a0939f-ncert-biology`  
**Environment:** `/tmp/neetenv` (sandbox had no `/vercel/share/neetenv`; CPython 3.11.2 · reportlab 5.0.1 · pymupdf 1.28.2 · Pillow 12.3.0)  
**Precondition:** Gate 2 green re-confirmed on the committed PDF before Pass 3 began (`check_pdf.py` exit 0, 0 fail / 2 inspected-benign warn).  
**Status:** **Gate 3 CLOSED under STRICT re-audit** (operator order “Go more strict standards” after the first CLOSED). First CLOSED (SHA `7a06e53d59916a5b`) is superseded; final rebuild is SHA `403fdc209f066f4e`.

---

## Gate 3(a) — visual render check

**20/20 pages** rendered at 150 dpi (`scratch/ch4inh_gate3/pages/p01.png` … `p20.png`) and inspected individually. Sample pages also rendered at 200 dpi → 1-bit B&W (`bw01`, `bw06`, `bw11`, `bw16`, `bw20`).

| Check | Result |
|---|---|
| Overflow / clipping / table run-off | **0** |
| Orphaned headings (linter check 9) | **0** — 96 banners all followed by content |
| Badge/banner collision (linter check 10) | **0** |
| Footer/header band | **0** — y-range on every page stays inside ~45–795 pt (A4 bands end/start at ~39.7 / 802.3) |
| Figure aspect squash | **n/a** — operator decision: 0 figures embedded |
| Cross-page style | **held** — only Times-Bold/Roman/Italic/BoldItalic; body 10.8 pt, banners 10.5, tables/captions 9.5, NOTE/MEMORY 10.2, badges 6.0–6.2 (above 5.0 FAIL floor) |
| NOTE vs MEMORY AID at 1-bit | distinguishable (solid rule + `!` vs dashed + star) |

**Accepted layout observations (not defects):**
- p11 and p17 end short because the next large `KeepTogether` (table / process block) refuses to split — same class accepted on Ch16.
- p20 (appendix tail after the Q7 fix) ends with white space; last page by design.
- No figure boxes exist (operator omission); "Read the plate" NOTE boxes carry the 163 labels instead.

**Pass 3(a) verdict: CLEAN — 20/20 pages inspected, 0 confirmed layout defects.**

---

## Gate 3(b) — bidirectional full read

### Method
- Source: OCR-derived `scratch/ch4inh_gate1/source_text_v1.txt` (28 pages; the chapter PDF is a pure scan with empty text layer — same source Pass 1 used).
- Inventory: frozen 376-row file loaded from disk (post Pass-2 operator trim of 39 rows from the 415 freeze).
- Script: every `# ---- N.N ----` block in `Ch4_PrinciplesOfInheritanceAndVariation.py`, read start to finish.
- **No coverage % / similarity score / grep used to clear any row.** Token screens were used only to *locate* candidates; every flag was opened and read.
- SUMMARY-UNIQUE folds (F372–F376) checked in both body homes and Quick Recap.

### Per-section reading claims

| Source read | Script block | Dir 1 (inv→script) | Dir 2 (source→inv) |
|---|---|---|---|
| p1 Unit VII opener | `# ---- Unit VII opener ----` | F001–F004 COVERED (F003 unit-contents + F005/F006/F008/F009/F010 unit padding removed by operator trim Group 2/4 — deliberate) | clean on remaining sentences |
| p2 Watson / Crick profiles | `# ---- Scientist profiles ----` | F005–F020 COVERED (dates 6 Apr 1928, 1947, 1950, Mar 1953, 8 Jun 1916, 1937, 1954, 23/1953, F.R.S. 1959, prizes 1959/1960/1962/Nobel 1962) | clean; portraits text-only by §4.4 |
| p3–4 Ch opener + Sahiwal | `# ---- Chapter 4 opener ----` | F021–F030 + F372/F373/F374 COVERED | F041 ("ancestors… little idea…") **operator-trimmed** (Group 2, old F041) — deliberate, not a Pass 3 defect |
| p4 §4.1 + Fig 4.1 / Table 4.1 | `# ---- 4.1 ----` | F031–F051 + Fig/Table rows COVERED; `Flouwer colour` kept | F049 ("basic framework… later scientists") **operator-trimmed** (Group 2, old F049) — deliberate |
| p5–9 §4.2 monohybrid → testcross | `# ---- 4.2 ----` (+ 4.2a/b/c/d) | F052–F113 COVERED; Punnett tables, binomial process_flow, testcross table, Fig 4.2–4.5 labels (**D2** role-binding on Fig 4.5 NOTE fixed under strict re-audit) | activity prompts F123/F130/F131/F132 trimmed (Group 1B) — deliberate; rest clean || p9 §4.2.1 / 4.2.2 | `# ---- 4.2.1 ----`, `# ---- 4.2.2 ----` | F114–F122 COVERED (3 numbered dominance statements; segregation) | clean |
| p10–11 §4.2.2.1 Incomplete Dominance | `# ---- 4.2.2.1 ----` | F123–F142 COVERED; snapdragon RR/Rr/rr 1:2:1; enzyme cases (i)(ii)(iii) | clean |
| p11–12 §4.2.2.2 Co-dominance | `# ---- 4.2.2.2 ----` | F143–F167 COVERED; Table 4.2 seven genotype rows; starch-grain Bb incomplete-dominance angle | F175 "How many phenotypes?" trimmed (1B) — deliberate |
| p12–14 §4.3 + 4.3.1 dihybrid | `# ---- 4.3 ----`, `# ---- 4.3.1 ----` | F168–F190 COVERED; 9:3:3:1 derivation process_flow; RY/Ry/rY/ry at 25% | F194/F196/F215/F217 trimmed — deliberate |
| p14–17 §4.3.2 Chromosomal theory | `# ---- 4.3.2 ----` | F191–F226 COVERED; 1865/1900; de Vries, Correns, von Tschermak; Sutton & Boveri; Table 4.3; Fig 4.8/4.9/4.10 labels; Fig 4.9 colour names in words | F248 table activity trimmed — deliberate |
| p17–18 §4.3.3 Linkage | `# ---- 4.3.3 ----` | F227–F238 COVERED; 1.3% / 37.2% / 98.7% / 62.8%; Sturtevant; Fig 4.11 Cross A/B labels | clean |
| p19 §4.4 Polygenic | `# ---- 4.4 ----` | F239–F249 COVERED; AABBCC/aabbcc skin-colour additive model | clean |
| p19 §4.5 Pleiotropy | `# ---- 4.5 ----` | F250–F254 COVERED; phenylalanine hydroxylase → mental retardation + hair/skin pigmentation | clean |
| p19–21 §4.6 Sex determination | `# ---- 4.6 ----` + F375 | F255–F274 + F375 COVERED; Henking 1891 / x body; XO grasshopper; XY man/Drosophila; ZW birds; **chicken ZZ/ZW** summary-unique folded | F293/F296 trimmed — deliberate |
| p21 §4.6.1 Humans | `# ---- 4.6.1 ----` | F275–F283 COVERED; 22 autosome pairs; 50% X/Y sperm; genetic makeup of sperm determines sex | F314 social-commentary trimmed (Group 4) — deliberate |
| p21 §4.6.2 Honey bee | `# ---- 4.6.2 ----` | F284–F290 COVERED; 32/16; haplodiploid; mitosis sperms; Fig 4.13a honey-bee plate distinguished from pedigree plate | F320/F321 bird-compare questions trimmed (1B) |
| p22 §4.7 Mutation | `# ---- 4.7 ----` | F291–F299 COVERED; point mutation / frame-shift / mutagens / UV | F332 "beyond the scope" trimmed (Group 4) |
| p22–23 §4.8 / 4.8.1 Pedigree | `# ---- 4.8 ----` (4.8.1) | F300–F312 COVERED; Fig 4.13b pedigree-symbol plate labels | F342/F346 trimmed (Group 2) |
| p23–25 §4.8.2 Mendelian disorders | same block 4.8.2 | F313–F352 COVERED; colour blindness 8%/0.4%; haemophilia + Queen Victoria; sickle-cell HbA/HbS, Glu→Val pos 6, GAG→GUG; PKU; thalassemia HBA1/HBA2 chr16, HBB chr11; quantitative vs qualitative | F353/F356 trimmed — deliberate |
| p25–26 §4.8.3 Chromosomal + F376 | `# ---- 4.8.3 ----` | F353–F376 COVERED; aneuploidy/polyploidy; Down's trisomy 21 + Langdon Down 1866 + Fig 4.16 six callouts; Klinefelter 47,XXY + Gynaecomastia; Turner 45 with X0; **Karyotypes** summary-unique folded | F398 trimmed (Group 2) |
| p27–28 SUMMARY | `# ---- Quick Recap ----` | all 5 SUMMARY-UNIQUE bolded in recap AND present in body homes; 27 BODY-PRESENT restated | clean |
| p28 EXERCISES | `# ---- Terms used in the exercises ----` | Q1/Q3/Q6/Q7 GAP answers present; 12 COVERED not reproduced | **D1 FOUND in Q7** (see below) |

### Direction 1 summary
- **376/376 inventory rows COVERED** in the script (token screen 0 low-hit; high-risk numbers/dates/qualifiers re-read in the PDF text layer).
- **0 MISSING** body facts relative to the frozen 376-row inventory.
- **0 FABRICATED** NCERT-ascribed facts (worked-out GAP answers and MEMORY AID boxes are labelled as non-NCERT).

### Direction 2 summary
- Every retained source sentence maps to a frozen row or to an **operator-approved trim** (39 rows, Groups 1A/1B/2/partial-4 — see `scratch/ch4inh_pass2/PASS3_REPORT.md` and the inventory Old-ID map).
- **0 new UNINVENTORIED rows required** this session. Trimmed sentences (ancestors qualifier, "basic framework", rhetorical openers, activity prompts, social commentary, "beyond the scope") were already inventoried at Pass 1 and deliberately dropped at Pass 2 by operator decision — they are **not** silent Pass 1 gaps of the Ch9/Ch13 class.
- First sentences / sub-headings of every numbered section (4.1–4.8.3) present (Ch9 D4/D9 class checked explicitly).
- Both plates printed as Figure 4.13 distinguished in words (honey bee p21 / pedigree symbols p22).

### SUMMARY-UNIQUE folds (Rule 3) — all five confirmed

| ID | Home | Body | Quick Recap |
|---|---|---|---|
| F372 | ch4 opener | NoteBox "principles of inheritance and its practices" | bold recap bullet |
| F373 | ch4 opener | NoteBox "morphological and physiological" | bold recap bullet |
| F374 | ch4 opener | NoteBox "Mendel was the first… systematically" | bold recap bullet |
| F375 | 4.6 | NoteBox "In chicken… ZZ… ZW" | bold recap bullet |
| F376 | 4.8.3 | NoteBox "analysis of Karyotypes" | bold recap bullet |

---

## Confirmed defects

| ID | Class | Where | What | Fix |
|---|---|---|---|---|
| **D1** | **DRIFTED** (wrong worked answer) | `# ---- Terms used in the exercises ----` Q7 | Appendix claimed TtYy × Ttyy → tall-green **1/2**, dwarf-green **0**, "no dwarf". Correct 4×2 Punnett from the chapter's own 4.3.1 gamete frequencies: **(a) tall green = 3/8**, **(b) dwarf green = 1/8**. The prior table dropped every t-bearing gamete from Parent 1. | Full 8-cell table + corrected ratios. Tagged `# [VERIFICATION FIX] D1`. PDF rebuilt; answer verified in text layer and on rendered p20. |
| **D2** | **DRIFTED** (label–role binding) | `# ---- 4.2c Testcross ----` Fig 4.5 NOTE | NOTE said both top panels were "Homozygous recessive parents" labelled **WW** / **Ww**. Source plate (book p59 / OCR p09): top role is **Homozygous recessive** tester; **WW** and **Ww** label the unknown dominant-phenotype parents (hom vs het). Body V/v line and outcomes table already had correct roles (`WW × ww`, `Ww × ww`); only the NOTE parent-role sentence was wrong. Inventory F112 listed labels without roles, so the invented binding slipped the first CLOSED. | NOTE rewritten: recessive tester = **ww**; unknown left = **WW** (hom dom); unknown right = **Ww** (het); outcomes unchanged. Tagged `# [VERIFICATION FIX] D2 (strict Gate 3)`. Verified on PDF p6 text layer + render `scratch/ch4inh_gate3/strict/verify_fig45_p06.png`. |

**0 remaining confirmed defects after D1 + D2.**

---

## Strict re-audit (operator: "Go more strict standards")

First CLOSED (SHA `7a06e53d59916a5b`) was treated as **insufficient**. Re-audit method beyond inventory-tick theatre:

1. **Re-read "clean" blocks for qualifier / label-role drift** — allele systems (V/v, WW/Ww/ww, HbA/HbS, GAG→GUG, ZZ/ZW, 45,X0, trisomy 21, XXY), linkage numbers (1.3% / 37.2%), Nobel 1962, "mainly determined", "only expressed in homozygous", "never blend" / "none were dwarf". Automated phrase windows alone are **not** clearance (line-break FPs: `1.3 per\ncent`, `45 with\nX0`).
2. **Sentence-level source gaps** — side-by-side OCR p09 vs script Fig 4.5 NOTE produced **D2** (only new confirmed defect).
3. **Heavy Pass-2 trim re-adjudication** — candidates (F069/F089/F100/F115/F116/F196/F353/F398-class wordings: "F1 always resembled…", "additional copy… may be included", "lack one of any…", "though rarely", social-blame line, "beyond the scope", etc.) remain **ABSENT by design**; surviving paraphrases still carry the examinable substance. No restore.
4. **SUMMARY-UNIQUE F372–F376** — reconfirmed in body homes + Quick Recap after rebuild.
5. **D1 regression** — Q7 still 3/8 + 1/8; bad "dwarf-green 0" absent.

### False positives / deliberate non-rows (kept so they are not re-litigated)

| ID | Item | Why dismissed |
|---|---|---|
| FP-1 | Unit VII sentences on phenotype-factors / molecular genetics / evolution mechanism | Operator-trimmed Group 2 (old F005/F006/F008/F009/F010); unit framing, not chapter examinable core |
| FP-2 | "Have you ever wondered…" / mango / sibling openers | Operator-trimmed Group 1A (old F030–F033); pure rhetoric |
| FP-3 | Ancestors "little idea about the scientific basis" | Operator-trimmed Group 2 (old F041) |
| FP-4 | "basic framework… expanded on by later scientists" | Operator-trimmed Group 2 (old F049) |
| FP-5 | In-text activity prompts ("try to find out the nature…", "what ratio…") | Operator-trimmed Group 1B |
| FP-6 | "It is unfortunate that in our society women are blamed…" | Operator-trimmed Group 4 (old F314); social commentary |
| FP-7 | "mechanism of mutation is beyond the scope…" | Operator-trimmed Group 4 (old F332) |
| FP-8 | Memory-aid / chapter-map tutor voice | Explicitly labelled non-NCERT organisational aid |
| FP-9 | Automated inventory phrase-screen "misses" on F045–F051, F080, F093, etc. | Table/figure-label line-break false splits; content present when window re-read in PDF text layer |
| FP-10 | Heavy Pass-2 substance paraphrases still "missing" exact frozen wording | Deliberate operator trim; re-adjudicated under strict pass — no substance gap vs surviving body |

---

## Gate 3 five conditions

| # | Condition | State |
|---|---|---|
| 1 | Zero confirmed defects remain | ✅ D1 + **D2** fixed; 0 remain |
| 2 | `check_pdf.py` green on **final** rebuild | ✅ exit 0, VERDICT WARN (0 fail / 2 inspected-benign warn) |
| 3 | Pass 3(a) every page | ✅ **20/20** pages inspected |
| 4 | Pass 3(b) full read both directions, per-section claims | ✅ table above + **strict re-audit** (label-role, qualifiers, heavy-trim re-adjudication); no coverage % substitute |
| 5 | Rebuild reproducible | ✅ two builds identical after D2: **20 pp / 70,823 chars / 0 imgs / text SHA `403fdc209f066f4e`** (supersedes `7a06e53d59916a5b`) |

### Accepted WARNs (not failures)
1. **Check 3** — no images embedded (operator decision 2026-09-10; see `FIGURE_DECISIONS.md`).
2. **Check 4** — "profile"/"portrait" substring true-negative on text-only scientist rows; no person photograph embedded.

---

## Section-wise coverage confirmation

| Section | Body facts | Summary-unique | Figures | Labels in text |
|---|---|---|---|---|
| Unit VII + profiles | 20/20 kept rows | — | portraits text-only | n/a |
| Ch4 opener | 10/10 + 3 SU folds | F372–F374 | — | — |
| 4.1 | 11/11 + Table 4.1 (8) + Fig 4.1 (2) | — | plate→text | labels in NOTE |
| 4.2 | 54/54 kept + Figs 4.2–4.5 | — | plates→text/tables | labels in NOTE + Punnett tables |
| 4.2.1 / 4.2.2 | 5+4 | — | — | — |
| 4.2.2.1 | 18/18 + Fig 4.6 | — | plate→text | labels in NOTE |
| 4.2.2.2 | 17/17 + Table 4.2 (8) | — | — | — |
| 4.3 / 4.3.1 | 9+12 + Fig 4.7 | — | plate→text | labels in NOTE |
| 4.3.2 | 23/23 + Table 4.3 + Figs 4.8–4.10 | — | plates→text | labels in NOTE; Fig 4.9 colours in words |
| 4.3.3 | 10/10 + Fig 4.11 | — | plate→text | 1.3%/37.2% + Cross A/B labels |
| 4.4 | 11/11 | — | — | — |
| 4.5 | 5/5 | — | — | — |
| 4.6 | 19/19 + Fig 4.12 + F375 | F375 | plate→text | XX/XY/ZW/ZZ |
| 4.6.1 | 9/9 | — | — | — |
| 4.6.2 | 5/5 + Fig 4.13a | — | plate→table/NOTE | 32/16, Meiosis/Mitosis |
| 4.7 | 9/9 | — | — | — |
| 4.8 / 4.8.1 | 1+9 + Fig 4.13b | — | plate→NOTE | pedigree symbols |
| 4.8.2 | 37/37 + Figs 4.14–4.15 | — | plates→NOTE | HbA/HbS, GAG/GUG, Myo tonic, Micro graph |
| 4.8.3 | 16/16 + Figs 4.16–4.17 + F376 | F376 | plates→NOTE | Down's six callouts; Klinefelter/Turner |
| Quick Recap | 32 summary sentences | 5/5 bolded | — | — |
| Exercises appendix | 4 GAP answers (Q1,Q3,Q6,Q7 corrected) | — | — | — |

**Total: 376/376 ticked · 163/163 labels in running text · 5/5 SUMMARY-UNIQUE folded · 4/4 exercise GAPs answered (Q7 corrected at Gate 3 · Fig 4.5 NOTE role-binding corrected as D2 under strict re-audit).**
