# Ch13 Plant Growth and Development — Gate 3, Pass 3(b) Content Cross-Check

**Method:** One complete full read (not a keyword search) of the NCERT source and the matching script blocks, in **both directions**, against the frozen inventory (`Ch13_PlantGrowthAndDevelopment_inventory.md`, loaded from file). Source text re-extracted this session with pdfplumber to `/tmp/ch13_pass3/source_text.txt` (15 pages). Parallel subagents unavailable, so the section-pair cross-check was done sequentially by hand per §6 Pass 3.

- **Direction 1 (inventory → script):** for each of F001–F084, O01–O16, H01–H20, E01–E10, is it in the script and correct? → catches MISSING / DRIFTED / FABRICATED.
- **Direction 2 (source → inventory):** walk each NCERT section sentence-by-sentence and heading-by-heading; name the row carrying each; anything with no row = UNINVENTORIED. Special attention to first/antecedent sentences, H3 sub-headings, and heading-defining sentences (the Ch9 failure class).

No coverage percentage or grep result is used to clear any row; every verdict below rests on a stated reading claim.

## Per-section reading claims (both directions)

| Script block | Source read | Rows | Dir-1 | Dir-2 (UNINVENTORIED) | Verdict |
|---|---|---|---|---|---|
| Introduction | src p1 (§intro) | O01, F001–F006 | all COVERED | none material (see FP-1) | CLEAN |
| `13.1 Growth` | src p2 §13.1 | O02, F007–F009 | all COVERED | none material (see FP-2) | CLEAN |
| `13.1.1` | src p2–3 | O03, F010–F014 | all COVERED | none material (see FP-3) | CLEAN |
| `13.1.2` | src p3–4 | O04, F015–F018 | all COVERED | none (maize=cell-number / watermelon=cell-size carried by wording, FP-4) | CLEAN |
| `13.1.3` | src p3–4 | O05, F019–F022 | all COVERED | none (pedagogical tail only) | CLEAN |
| `13.1.4` | src p4–6 | O06, F023–F032 | all COVERED | none | CLEAN |
| `13.1.5` | src p6 | O07, F033–F037 | all COVERED | none material (see FP-5) | CLEAN |
| `13.2` | src p7 | O08, F038–F043 | all COVERED | none | CLEAN |
| `13.3` | src p7–9 | O09, F044–F049 | all COVERED | none | CLEAN |
| `13.4 / 13.4.1` | src p9 | H10, O10, F050–F054 | all COVERED | none (kinetin IUPAC name compressed, see CD-1) | CLEAN |
| `13.4.2` | src p9–10 | O11, F055–F061 | all COVERED | none | CLEAN |
| `13.4.3 / 13.4.3.1` | src p10–11 | O12, F062–F066 | all COVERED | none (apical-dominance preamble, see FP-6) | CLEAN |
| `13.4.3.2` | src p11 | O13, F067–F070 | all COVERED | none | CLEAN |
| `13.4.3.3` | src p11–12 | O14, F071–F073 | all COVERED | none material (see FP-7) | CLEAN |
| `13.4.3.4` | src p12 | O15, F074–F079 | all COVERED | none | CLEAN |
| `13.4.3.5` | src p12–13 | O16, F080–F084 | all COVERED | none | CLEAN |
| `Quick Recap` | src p13–14 Summary | H19, recaps F008/F016/F011/F013/F024/F027/F028/F038/F040/F041/F048/F046/F049/F051/F083 | all COVERED | **intercalary meristem** surfaced here (see NOTE-1) | CLEAN |
| (exercises, not a block) | src p14–15 Exercises | E01–E10 | all supported | E07, E09 = source gap (see SRC-1) | CLEAN w/ noted source gap |

**Both sub-headings/H3s present:** 13.4.3.1–13.4.3.5 all rendered as their own H3 banners (verified in Pass 3a p7–p9). Every section's first/opener sentence (O01–O16) is present. No heading-defining antecedent sentence is dropped (the Ch9 D9 class): §13.2's opener defining *differentiation* is present (F038, script keyterm line 266); §13.3's opener defining *development* is present (F044, script line 295).

## Direction-1 results
- **84/84 Facts COVERED** by full read. 0 MISSING, 0 FABRICATED, 0 material DRIFT.
- Numbers/qualifiers spot-verified verbatim: "17,500 new cells per hour", "3,50,000 times", "more than 100 gibberellins", "20 tonnes per acre", "mid-1960s", "E. Kurosawa (1926)", "Miller et al. (1955)", "H. H. Cousins (1910)". Qualifier "usually" (decapitation) preserved; "in most situations ABA acts as an antagonist" preserved. NCERT's own spelling "respiratory climactic" retained (not silently "corrected" to climacteric).
- **FABRICATED sweep (script → NCERT):** the PGR data-table (Auxins/Indole/IAA; Gibberellins/Terpenes/GA₃; Cytokinins/Adenine derivatives/Kinetin,zeatin; ABA/Carotenoid derivatives/ABA; Ethylene/Gaseous/C₂H₄) is a faithful reformat of F051 — nothing invented. Process-flow steps trace to Fig 13.8. Quick Recap traces to the Summary. No fabrication.

## Figure-label matrix (human backstop to check 6)
All 11 figures sit at their correct topic (confirmed in Pass 3a): 13.1→intro, 13.2→13.1.1, 13.3→13.1.3, 13.4/13.5/13.6/13.7→13.1.4, 13.8→13.3, 13.9→13.3, 13.10→13.4.2, 13.11→13.4.3.1. Captions match NCERT wording. `check_pdf.py` check 6 = 49/49 labels in running text; spot-confirmed by eye (e.g. "phototropism", "tip of the coleoptile", "apical dominance", "Heterophylly", "sigmoid").

## False positives — investigated and dismissed (kept per §Pass 3 record rule)
- **FP-1 (intro):** source "Once favourable conditions return, the seeds resume metabolic activities and growth takes place" — trivial converse of F005 (germination on favourable conditions); no independent NEET-testable fact. Dismissed.
- **FP-2 (§13.1):** "expansion of a leaf is growth" is an illustrative example; its content (leaf-area increase = growth) is carried by F018. The "swelling of wood in water" line is an unanswered rhetorical question, not a fact. Dismissed.
- **FP-3 (§13.1.1):** "the product soon loses the capacity to divide and such cells make up the plant body" — the maturation-of-derivatives concept is carried by F038 (meristem-derived cells differentiate/mature) and F012 (new cells added to the body). Dismissed.
- **FP-4 (§13.1.2):** "former = increase in cell number; latter = increase in cell size" — carried implicitly by the script's own wording ("17,500 **new cells** per hour" vs watermelon cells "**increase in size**"). Dismissed.
- **FP-5 (§13.1.5):** "any deviation from this range could be detrimental to its survival" — subsumed by F037's "optimum temperature range best suited for its growth". Dismissed.
- **FP-6 (§13.4.3.1):** source preamble "In most higher plants, the growing apical bud inhibits…" — the "in most higher plants" preamble is compressed in **both** the frozen inventory (F065) and the script, so direction 1 is clean; the testable content (apical dominance, decapitation, tea/hedge application) is intact and accurate. Low-severity Pass-1 wording choice, not a Pass-2 drift. Dismissed.
- **FP-7 (§13.4.3.3):** "since the discovery of zeatin, several naturally occurring cytokinins and some synthetic compounds have been identified" — recap-of-existence sentence; F071/F072 carry the substantive cytokinin facts. Dismissed.

## Compression decisions (transparent)
- **CD-1:** kinetin's chemical name "N⁶-furfurylaminopurine" (source §13.4.1) is compressed to "adenine derivatives (kinetin)" in both inventory F051 and the script; kinetin's nature as "a modified form of adenine" is still stated in §13.4.3.3 (F071). NEET-relevant identity preserved; only the full IUPAC-style name omitted.

## NOTE / source observations
- **NOTE-1:** "intercalary meristem" appears only in the NCERT Summary (not the body). It has no dedicated Fact row but is catalogued in inventory section D ("Root/shoot apical + intercalary meristems → elongation") and is **surfaced in the rendered PDF** ("(and intercalary meristems)" in Quick Recap, script line 554). Coverage intact; no defect.
- **SRC-1 (source problem):** Exercises 7 and 9 ask about short-day/long-day plants and photoperiodic response — content that the rationalised NCERT edition removed from the chapter body (photoperiodism/vernalisation sections are gone) while retaining the exercises. The inventory handles this honestly by mapping E07/E09 to F084 (the surviving pointer that light/temperature control flowering, vernalisation, dormancy via PGRs). This is an inherent source inconsistency, not a chapter defect; recorded as a source problem.

## Pass 3(b) verdict
**Both directions CLEAN. 0 confirmed content defects.** All direction-2 candidates were investigated by full read and dismissed with reasoning (FP-1…FP-7), or are transparent compression (CD-1) / a source-level gap (SRC-1). No `.py` edit is required; the frozen inventory and the rendered PDF agree with the source.
