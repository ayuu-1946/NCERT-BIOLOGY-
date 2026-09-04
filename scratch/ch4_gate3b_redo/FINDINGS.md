# Chapter 4 — Animal Kingdom — Pass 3(b) REDO (content cross-check, both directions)

> Operator instruction (2026-09-04): **redo Pass 3(b) fresh; ignore the prior Pass 3(b) verdict.**
> Documentation is written into this file **incrementally, section by section, as each is completed**,
> so no work is lost if the session is interrupted. On completion the confirmed outcomes are reconciled
> into the inventory `.md`, `Ch4_AnimalKingdom_TRACKER.md`, `CHAPTER_TRACKER.md`, and `CHAPTER_STATUS.md`.

## Why the prior verdict is not trusted (motivating this redo)
- The tracker Gate-ledger row marks Pass 3(b) **DONE** citing evidence in "§7e §4.2→end", but **no §7e exists**
  in `Ch4_AnimalKingdom_TRACKER.md` — the file jumps from §7d (§4.1 only) straight to §8. The only real
  Pass 3(b) evidence on disk covers §4.1 (31 rows). ~90% of the chapter had no reading claim. Per GATE_3 §4
  condition 4 + §7 rule 1, that closure is a claim, not a fact, and is re-verified here from scratch.

## Method (GATE_3 §3 + §7)
- Full start-to-finish read of each source section against the matching script block(s) and inventory rows —
  **no grep, no coverage %, no similarity score** used as clearing evidence.
- Source read from `scratch/ch4_gate1/ch4_source.txt` (PyMuPDF, 18/18 pages, page-marked), cross-checked
  against the rendered PDF where reflow was suspected.
- Script read from `notes/class 11/Ch4_AnimalKingdom/Ch4_AnimalKingdom.py` (`# ---- N ----` block markers).
- Inventory rows read from `Ch4_AnimalKingdom_inventory.md` (FROZEN, F001–F352 + F015a).
- Both directions per row: **Dir 1** inventory→script (MISSING/FABRICATED/DRIFTED); **Dir 2** source→inventory
  (UNINVENTORIED — every source sentence/heading must name a carrying row).

Legend: COVERED / MISSING / FABRICATED / DRIFTED / UNINVENTORIED. A section is CLEAN only if BOTH directions clean.

---

## Group 1 — §4.0 intro + §4.1 + §4.1.1–§4.1.6  (source pp.37–39)

Read source pp.37–39 (`===== PAGE 1/2/3 =====`) against script blocks `# ---- 4.0 ----` … `# ---- 4.1.6 ----`
and inventory rows F001–F031, F015a, F155–F163, F175–F183, F343 (Fig 4.2 labels), F344 (Fig 4.3 labels).

| Section | Source ↔ script | Rows | Dir 1 (inv→script) | Dir 2 (source→inv) |
| :--- | :--- | :--- | :--- | :--- |
| §4.0 intro | p.37 "When you look around…newly described species." ↔ `# ---- 4.0 ----` | F001,F002,F155,F156,F175,F176 | 6/6 COVERED | every sentence has a row ✓ |
| §4.1 opener | p.37 "Inspite of differences…discussed here." ↔ `# ---- 4.1 ----` | F003,F004,F157,F177 | 4/4 COVERED | ✓ |
| §4.1.1 Levels of Organisation | pp.37–38 ↔ `# ---- 4.1.1 ----` | F005–F015,F158,F178 | 13/13 COVERED | ✓ |
| §4.1.2 Symmetry | p.38 ↔ `# ---- 4.1.2 ----` | F015a,F016–F019,F159,F179 | 7/7 COVERED | ✓ (antecedent carried by F015a) |
| §4.1.3 Diplo/Triploblastic | pp.38–39 ↔ `# ---- 4.1.3 ----` | F020–F022,F160,F180,F343 | 6/6 COVERED | ✓ |
| §4.1.4 Coelom | p.39 ↔ `# ---- 4.1.4 ----` | F023–F027,F161,F181,F344 | 8/8 COVERED | ✓ |
| §4.1.5 Segmentation | p.39 ↔ `# ---- 4.1.5 ----` | F028,F029,F162,F182 | 4/4 COVERED | ✓ |
| §4.1.6 Notochord | p.39 ↔ `# ---- 4.1.6 ----` | F030,F031,F163,F183 | 4/4 COVERED | ✓ |

**Group 1 result: CLEAN both directions.** 0 MISSING, 0 FABRICATED, 0 DRIFTED, 0 UNINVENTORIED.
The §4.1.2 antecedent "Animals can be categorised on the basis of their symmetry." is present in the script
(body line 178) AND carries inventory row F015a — confirmed, not a new gap.

Figure-label rows confirmed in running text: Fig 4.2 labels (Ectoderm/Mesoglea/Endoderm/Mesoderm) spelled in
the §4.1.3 caption + bullets; Fig 4.3 labels (Coelom/Pseudocoelom) spelled in §4.1.4. Both figures sit at topic.

**False positives (investigated, dismissed — do not "re-fix"):**
1. §4.1 opener: script inserts "…nature of coelom, **and** patterns of digestive…"; source omits "and". Trivial
   list connective, no meaning change. NOT a defect.
2. §4.1.1: script "division of labour (activities) **occurs**" vs source "**occur**". Subject–verb normalisation.
   NOT a defect.
3. §4.1.1: the four organisation levels rendered as bold lead-in labels (Cellular/Tissue/Organ/Organ system
   level:) rather than the source's inline "…i.e., X level of organisation". Safe compression; each level name
   preserved verbatim; rows F006–F010 fully represented. NOT a defect — compression decision.
4. §4.0: script adds a sentence "This chapter runs in two parts: 4.1 Basis of Classification and 4.2
   Classification of Animals." This carries the page-1 contents sidebar (F175) into running prose. NOT a
   fabrication — it is the sidebar content, inventoried as F175.

_Doc note:_ inventory exercise-gap table lists Q3 (coelom) as answered by "§4.1.5"; coelom is actually §4.1.4
(§4.1.5 is Segmentation). Cosmetic cross-reference slip in the exercise table, not a content defect in the
PDF. Logged for the reconciliation step; no PDF impact.

---

## Group 2 — §4.2 opener + §4.2.1–§4.2.10 (the ten non-chordate phyla)  (source pp.39–45)

Read source pp.39–45 (`===== PAGE 3–9 =====`) against script blocks `# ---- 4.2 ----` … `# ---- 4.2.10 ----`
and inventory rows F032–F154 (prose), F164–F174 (headings), F184–F194 (openers), F345 (Fig 4.4 chart labels),
F346 (Fig 4.10 Male/Female), F347 (Fig 4.15 Proboscis/Collar/Trunk), F350 (Porifera "flagellated" fold).

| Section | Source ↔ script | Rows | Dir 1 | Dir 2 |
| :--- | :--- | :--- | :--- | :--- |
| §4.2 opener + Fig 4.4 | pp.39–40 ↔ `# ---- 4.2 ----` | F032–F034,F164,F184,F345 | 6/6 COVERED | ✓ (footnote F034, "features…described" F033) |
| §4.2.1 Porifera | p.40 ↔ `# ---- 4.2.1 ----` | F035–F047,F165,F185,F350 | 16/16 COVERED | ✓ |
| §4.2.2 Coelenterata | pp.40–41 ↔ `# ---- 4.2.2 ----` | F048–F059,F166,F186 | 14/14 COVERED | ✓ |
| §4.2.3 Ctenophora | p.42 ↔ `# ---- 4.2.3 ----` | F060–F068,F167,F187 | 11/11 COVERED | ✓ |
| §4.2.4 Platyhelminthes | p.42 ↔ `# ---- 4.2.4 ----` | F069–F078,F168,F188 | 12/12 COVERED | ✓ |
| §4.2.5 Aschelminthes | p.43 ↔ `# ---- 4.2.5 ----` | F079–F088,F169,F189,F346 | 13/13 COVERED | ✓ |
| §4.2.6 Annelida | p.43 ↔ `# ---- 4.2.6 ----` | F089–F100,F170,F190 | 14/14 COVERED | ✓ |
| §4.2.7 Arthropoda | p.44 ↔ `# ---- 4.2.7 ----` | F101–F119,F171,F191 | 21/21 COVERED | ✓ |
| §4.2.8 Mollusca | pp.44–45 ↔ `# ---- 4.2.8 ----` | F120–F130,F172,F192 | 13/13 COVERED | ✓ |
| §4.2.9 Echinodermata | p.45 ↔ `# ---- 4.2.9 ----` | F131–F142,F173,F193 | 14/14 COVERED | ✓ |
| §4.2.10 Hemichordata | p.45 ↔ `# ---- 4.2.10 ----` | F143–F154,F174,F194,F347 | 15/15 COVERED | ✓ |

**Group 2 result: CLEAN both directions.** 0 MISSING, 0 FABRICATED, 0 DRIFTED, 0 UNINVENTORIED.
- F350 fold confirmed: script §4.2.1 reads "Choanocytes or collar cells, **which are flagellated**, line the
  spongocoel…" — the SUMMARY-UNIQUE "flagellated" qualifier is present and woven in at topic.
- Figure-label rows confirmed in running text and placed at topic: Fig 4.4 chart terms (Kingdom / Levels of
  Organisation / Symmetry / Body Cavity or Coelom / Phylum / acoelomates / pseudocoelomates / coelomates / all
  11 phylum leaves) spelled verbatim in the two §4.2 bullets; Fig 4.10 Male/Female and Fig 4.15
  Proboscis/Collar/Trunk spelled in their captions. All non-chordate figures 4.5–4.15 sit at their topic.

**Compression/reorder decisions (safe, dismissed):**
- §4.2.1: the sentence "This pathway of water transport is helpful in food gathering, respiratory exchange and
  removal of waste." (F040) is placed **before** the ostia→spongocoel→osculum `process_flow` rather than after,
  as in the source. No fact added/removed; the water-path facts (F039) render as a 3-step process flow. Safe
  reorder, not drift.
- §4.2.1: the four canal-system verbs and the choanocyte/digestion/skeleton facts (F041–F043) are merged into
  one bullet. All wording preserved; NOT a defect.
- Trivial normalisations (not defects): source "freeliving" → script "free-living" (§4.2.5); source "feather
  like" → "feather-like" (§4.2.8). No meaning change.

---

## Group 3 — §4.2.11 Chordata + Vertebrata chart + the 7 classes  (source pp.45–51)

Read source pp.45–51 (`===== PAGE 9–15 =====`) against script blocks `# ---- 4.2.11 ----` …
`# ---- 4.2.11.7 ----` (incl. the Vertebrata chart block) and inventory rows F195–F206 (Chordata prose),
F213–F218 (chart), F219–F311 (7 classes), F325–F332 (headings), F335–F342 (openers), F348 (Fig 4.16 labels),
F349 (chart labels), F351 (Cyclostomata "most primitive" fold), F352 (Reptilia "limbs absent in snakes" fold).

| Section | Source ↔ script | Rows | Dir 1 | Dir 2 |
| :--- | :--- | :--- | :--- | :--- |
| §4.2.11 Chordata + Fig 4.16 + Fig 4.17 | pp.45–46 ↔ `# ---- 4.2.11 ----` | F195–F206,F325,F335,F348 | 15/15 COVERED | ✓ |
| Vertebrata chart | p.47 ↔ chart block | F213–F218,F349 | 6/6 COVERED | ✓ |
| §4.2.11.1 Cyclostomata | p.47 ↔ `# ---- 4.2.11.1 ----` | F219–F228,F326,F336,F351 | 13/13 COVERED | ✓ |
| §4.2.11.2 Chondrichthyes | pp.47–48 ↔ `# ---- 4.2.11.2 ----` | F229–F244,F327,F337 | 18/18 COVERED | ✓ |
| §4.2.11.3 Osteichthyes | p.48 ↔ `# ---- 4.2.11.3 ----` | F245–F256,F328,F338 | 14/14 COVERED | ✓ |
| §4.2.11.4 Amphibia | pp.48–49 ↔ `# ---- 4.2.11.4 ----` | F257–F271,F329,F339 | 17/17 COVERED | ✓ |
| §4.2.11.5 Reptilia | p.49 ↔ `# ---- 4.2.11.5 ----` | F272–F283,F330,F340,F352 | 15/15 COVERED | ✓ |
| §4.2.11.6 Aves | pp.49–50 ↔ `# ---- 4.2.11.6 ----` | F284–F298,F331,F341 | 17/17 COVERED | ✓ |
| §4.2.11.7 Mammalia | pp.50–51 ↔ `# ---- 4.2.11.7 ----` | F299–F311,F332,F342 | 15/15 COVERED | ✓ |

**Group 3 result: CLEAN both directions.** 0 MISSING, 0 FABRICATED, 0 DRIFTED, 0 UNINVENTORIED.
- F351 fold confirmed: script §4.2.11.1 reads "…are ectoparasites on some fishes. They are the **most primitive
  chordates**." — SUMMARY-UNIQUE claim present, at topic.
- F352 fold confirmed: script §4.2.11.5 reads "Limbs, when present, are two pairs; **limbs are absent in
  snakes**." — SUMMARY-UNIQUE claim present, at topic.
- Fig 4.16 labels (Nerve cord/Notochord/Post-anal part/Gill slits) and the full Vertebrata-chart label set
  (Agnatha/Gnathostomata/Pisces/Tetrapoda + all 7 class names) are spelled verbatim in the surrounding bullets
  and captions. Figs 4.16–4.24 all sit at their class topic.

**Benign caption editorialisations (accurate, dismissed — not source-content defects):**
- Fig 4.17 caption rendered "Ascidia (a urochordate protochordate)" vs source bare "Ascidia" — the gloss is
  true and drawn from the adjacent F200/F202 text; it adds no un-sourced fact.
- Figs 4.19/4.20/4.22 captions trim the source lead-in ("Example(s) of" / drop "Examples of"), keeping the
  corrected species + panel letters from the frozen manifest. Cosmetic; species mapping intact.

---

## Group 4 — TABLE 4.1 and TABLE 4.2  (source pp.46 and 51)

Read source p.46 TABLE 4.1 and p.51 TABLE 4.2 (column-major extraction, reassembled by column position) against
the script `KeepTogether([...TABLE 4.1...])` block (lines 516–527) and the `data_table([...TABLE 4.2...])` block
(lines 717–742), and inventory rows F207–F212 (Table 4.1) and F312–F324 (Table 4.2).

**TABLE 4.1 — Comparison of Chordates and Non-chordates (F207–F212): CLEAN both directions.**
| Row | Chordates | Non-chordates | Verdict |
| :--- | :--- | :--- | :--- |
| title | "Comparison of Chordates and Non-chordates" | — | COVERED |
| 1 | Notochord present. | Notochord absent. | COVERED |
| 2 | CNS is dorsal, hollow and single. | CNS is ventral, solid and double. | COVERED |
| 3 | Pharynx perforated by gill slits. | Gill slits are absent. | COVERED |
| 4 | Heart is ventral. | Heart is dorsal (if present). | COVERED |
| 5 | A post-anal part (tail) is present. | Post-anal tail is absent. | COVERED |
- Script omits only the source's cosmetic "S.No." index column (1–5). No fact lost. NOT a defect.

**TABLE 4.2 — Salient Features of Different Phyla (F312–F324): CLEAN both directions.**
All 11 phylum rows checked cell-by-cell across the 8 attribute columns (Level of Organisation, Symmetry,
Coelom, Segmentation, Digestive, Circulatory, Respiratory, Distinctive Features) against F314–F324; **11/11 rows
match verbatim**, including:
- Porifera Symmetry "Various" and Echinodermata Symmetry "Radial" — the two cells where the source table is
  terser than its prose (per inventory carry-over #7). Preserved as source wording, not "corrected." ✓
- Platyhelminthes "Organ & Organ-system" (rendered via `&amp;`), Aschelminthes "Pseudo-coelomate". ✓
- Lead-in F312 ("The salient distinguishing features … given in Table 4.2") present at line 714; title F313
  present at line 716.
- Column-header hyphenation ("Segmen-tation", "Circula-tory", "Respira-tory") and "Pseudo-coelomate" are
  line-wrap cosmetics only — no value changed.

**Group 4 result: CLEAN both directions.** 0 MISSING, 0 FABRICATED, 0 DRIFTED, 0 UNINVENTORIED.

---

## Group 5 — SUMMARY + EXERCISES + figure-label matrix  (source pp.52–54)

Read source pp.52–53 SUMMARY and pp.53–54 EXERCISES against script `# ---- SUMMARY ----` (lines 745–783) and
`# ---- EXERCISES ----` (lines 786–802), plus a final sweep of figure-label rows F343–F349 against the captions.

**SUMMARY (34 sentences, inventory summary-classification table rows 1–34): CLEAN.**
- Rendered as five full prose paragraphs reproducing all 34 summary sentences (comma/semicolon joins only).
- The 3 SUMMARY-UNIQUE facts are additionally folded into the body at topic and confirmed in Groups 2–3:
  F350 "flagellated" choanocytes (§4.2.1), F351 "most primitive chordates" (§4.2.11.1), F352 "limbs absent in
  snakes" (§4.2.11.5). Nothing SUMMARY-UNIQUE is body-orphaned.
- Summary sentence 13 ("The body is covered with external skeleton made of chitin.") is attached to the
  **arthropods** clause (semicolon) rather than left dangling after the molluscs sentence as in the source.
  This matches the inventory classification (BODY-PRESENT → §4.2.7 chitinous exoskeleton, F105) and the biology
  (molluscs = calcareous shell, arthropods = chitin). Defensible re-attachment of an ambiguous source
  adjacency; no fact added or lost. NOT a defect.

**EXERCISES (15 exercises; Rule-2 gap analysis): CLEAN.**
- The two GAP items are resolved as key-term definitions so the exercise set is self-contained:
  - Q4 — intracellular vs extracellular digestion: defined at line 789–793. ✓
  - Q12 — oviparous vs viviparous: defined at line 794–798. ✓
- The remaining 13 exercises are COVERED by existing body content (per inventory exercise-gap table); the notes
  intentionally do not reproduce the 15 NCERT question stems verbatim (NEET-replacement-notes design).
- A `memory_aid` (Vertebrata ladder + heart-chamber progression 2→3→(3/4)→4→4) is derived entirely from
  body-present facts (F214–F218 chart; F238/F251/F266/F277/F291/F306 heart chambers). No un-sourced fact. ✓

**Figure-label matrix (F343–F349): CLEAN.** Every label-bearing figure spells its labels verbatim at topic:
F343 Fig 4.2 (Ectoderm/Mesoglea/Endoderm/Mesoderm), F344 Fig 4.3 (Coelom/Pseudocoelom), F345 Fig 4.4 (26-term
chart, in the two §4.2 bullets), F346 Fig 4.10 (Male/Female), F347 Fig 4.15 (Proboscis/Collar/Trunk), F348
Fig 4.16 (Nerve cord/Notochord/Post-anal part/Gill slits), F349 Vertebrata chart (all division/super-class/
class terms).

**Group 5 result: CLEAN both directions.** 0 MISSING, 0 FABRICATED, 0 DRIFTED, 0 UNINVENTORIED.

---

# PASS 3(b) REDO — FINAL VERDICT

**Whole chapter re-read start-to-finish, both directions, all 353 inventory rows (F001–F352 + F015a):
CLEAN. 0 MISSING, 0 FABRICATED, 0 DRIFTED, 0 UNINVENTORIED.**

- Every one of the 3 folded SUMMARY-UNIQUE facts (F350/F351/F352) is present in the body at topic.
- Both exercise GAP items (Q4, Q12) are resolved in the Exercises section.
- All 7 figure-label rows and both tables verified cell-by-cell.
- No script change is required by Pass 3(b); the PDF content faithfully represents the frozen inventory.
- All divergences from source found during the read were investigated and are benign (list connectives,
  subject–verb agreement, safe reorders/merges, cosmetic caption trims, line-wrap hyphenation, defensible
  summary re-attribution). None alter a fact. None are "re-fixable" without introducing error.

Remaining delivery steps (todo 7): rebuild the PDF to confirm it compiles, re-run `check_pdf.py` to confirm the
mechanical gate is still green, then reconcile the tracker ledgers — **replacing the prior unsupported "§7e"
Pass 3(b) DONE row with this evidence-backed redo**.
