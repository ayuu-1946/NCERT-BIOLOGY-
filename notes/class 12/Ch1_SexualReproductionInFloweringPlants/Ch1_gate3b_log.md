# Ch1 (Class 12) — Gate 3(b) content cross-check log

Session: 2026-09-24. Gate 3(a) (visual, every page) was performed by the operator by direct visual inspection of the PDF and is not re-run here.
Method: full read, both directions, sequential section-pairs (no parallel subagents). Source text layer dumped to `scratch/ch1_gate3b/source.txt` (25 source pages) only to make reading possible; **every verdict below is a reading claim, not a grep/score**. Inventory loaded from the FILE `Ch1_SexualReproductionInFloweringPlants_inventory.md`.

## Pre-audit cross-document check (§7 rule 2)
- `CHAPTER_STATUS.md` / `CHAPTER_TRACKER.md`: Gate 1 CLOSED, Gate 2 evidence green, Gate 3 OPEN — agree with each other.
- **Mismatch found (X1):** inventory Gate-1/post-Gate-1 record states the build is **18 A4 pages**; the committed PDF on disk has **16 pages**. Stated-count metadata drift; reconciled at closure (the page count is re-derived from the final rebuild and written into all three documents).

---

## Pair 1 — Unit-6 opener + chapter opener + §1.1 + §1.2
Read source pp. 1–4 (unit opener, Maheshwari page, chapter opener, §1.1, §1.2) against script blocks `# ---- Unit 6 opener ----`, `# ---- 1.1 ... ----`, `# ---- 1.2 ... ----`.

| Section | Status | Covered | Missing | Fabricated | Drifted | Uninventoried |
|---|---|---|---|---|---|---|
| Unit opener | CLEAN | F001–F003 (3/3) | — | — | — | — |
| p2 profile | **ISSUES** | — | profile block | — | — | **U1** Panchanan Maheshwari profile (whole page) |
| 1.1 | **ISSUES** | F004–F011 (8/8); 7/7 Fig 1.1 labels in running text | — | — | — | **U2** "Flowers are objects of aesthetic, ornamental, social, religious and cultural value … symbols for … love, affection, happiness, grief, mourning" |
| 1.2 | CLEAN | F012–F017 (6/6) | — | — | — | — |

**Confirmed defects**
- **D1 (U1, Pass 1 gap + metadata defect).** Source p2 carries a full text biography of Panchanan Maheshwari (1904–1966; Jaipur; D.Sc. Allahabad; inspired by Dr W. Dudgeon; embryological characters in taxonomy; Dept of Botany, Univ. of Delhi as centre for embryology & tissue culture; artificial culture of immature embryos; test-tube fertilisation & intra-ovarian pollination; FRS, INSA; first NCERT Higher-Secondary Biology textbooks 1964). §5 item 3 requires a text-only profile box. Script header item 6 falsely states "the source page 2 plate is a photograph only". No inventory row existed.
- **D2 (U2, Pass 1 gap).** §1.1 factual sentence on the cultural/ornamental value of flowers has no row and is absent from the script.

**False positives (dismissed, keep)**
- FP1 Unit opener s1–2 ("Biology in essence is the story of life … extinction") — unit-level scene-setting framing, no chapter fact; garbage rule (rhetorical scene-setting).
- FP2 §1.1 "List at least five flowers…", "Have you heard of floriculture?" — in-text activity prompts, no fact stated.
- FP3 §1.2 "In the flower the male and female reproductive structures, the androecium and the gynoecium differentiate and develop." — carried by F015→F016/F017 sequence in the 1.2 body+keyterm; restatement.
- FP4 Fig 1.1 walk-through "from outside inwards … protective and attractive whorls" — label ordering gloss, factually correct, no new claim.

---

## Pair 2 — §1.2.1 (Stamen/anther + Structure of microsporangium + Microsporogenesis + Pollen grain)
Read source pp. 5–8 (through "…in crop breeding programmes") against script blocks `# ---- 1.2.1 Stamen … ----`, `# ---- 1.2.1 Structure of microsporangium ----`, `# ---- 1.2.1 Microsporogenesis ----`, `# ---- 1.2.1 Pollen grain ----`. All four sub-headings present in script (H2 + 3×H3).

| Block | Status | Covered | Missing | Fabricated | Drifted | Uninventoried |
|---|---|---|---|---|---|---|
| Stamen (F018–F028) | CLEAN | 11/11; 5/5 Fig 1.2 labels in text; F252 "tetrasporangiate" folded | — | — | — | — |
| Structure of microsporangium (F029–F037) | **ISSUES** | 9/9; 8/8 Fig 1.3 labels | — | — | **DR1** F035 | — |
| Microsporogenesis (F038–F044) | CLEAN | 7/7 | — | — | — | — |
| Pollen grain (F045–F072) | **ISSUES** | 28/28; 5/5 Fig 1.5 labels; Fig 1.4, 1.6 caption-only (correct) | — | — | **DR2** F068 | **U3** exine patterns sentence |

**Confirmed defects**
- **D3 (DR1).** NCERT: "*When the anther is young*, a group of compactly arranged homogenous cells called the sporogenous tissue occupies the centre…". Script drops the temporal qualifier (it is what makes the Fig 1.3 young-vs-dehisced contrast true).
- **D4 (DR2).** NCERT: viability "is highly variable and *to some extent* depends on the prevailing temperature and humidity". Script: "depends on…" — qualifier dropped (overstates dependence).
- **D5 (U3, Pass 1 gap, minor).** "The exine exhibits a fascinating array of patterns and designs." (+ variety of architecture — sizes, shapes, colours, designs — Fig 1.4) has no row. Script already carries the idea in the Fig 1.4 caption ("sculptured exine of pollen of different species"); row added for bookkeeping, body sentence made explicit.

**False positives (dismissed, keep)**
- FP5 "Can you think of how tapetal cells could become bi-nucleate?", "What would be the ploidy of the cells of the tetrad?", "Why do you think the exine should be hard? What is the function of germ pore?", "How long do you think…" — embedded questions with no stated fact.
- FP6 Collect-ten-stamens / dissecting-microscope activity; Hibiscus-pollen-on-fingers activity; semen/sperm storage analogy — activities/analogy, no examinable fact beyond F071–F072.
- FP7 Fig 1.3 walk-through "sterile tissue joining the two lobes is the connective" — gloss on a figure label; factually correct, not a contradiction of any row.

---

## Pair 3 — §1.2.2 (Pistil + Megasporangium (Ovule) + Megasporogenesis + Female gametophyte)
Read source pp. 8–11 (from "1.2.2 The Pistil…" to "…though 8-nucleate is 7-celled") plus the p8 Fig 1.6 margin text, against script blocks `# ---- 1.2.2 The Pistil … ----`, `# ---- 1.2.2 The Megasporangium (Ovule) ----`, `# ---- 1.2.2 Megasporogenesis ----`, `# ---- 1.2.2 Female gametophyte ----`. H2 + 3×H3 all present.

| Block | Status | Covered | Missing | Fabricated | Drifted | Uninventoried |
|---|---|---|---|---|---|---|
| Pistil (F073–F085) | CLEAN | 13/13; 15/15 Fig 1.7 labels in text; placentation recall NOTE present (planned exercise-gap home) | — | — | — | — |
| Ovule (F086–F095) | CLEAN | 10/10; F253 "archesporium" folded (matches summary wording) | — | — | — | — |
| Megasporogenesis (F096–F102) | CLEAN | 7/7; 13/13 Fig 1.8 labels | — | — | — | — |
| Female gametophyte (F103–F115) | CLEAN | 13/13; memory aid 2+1+3+1 = 7 cells / 8 nuclei checked arithmetically | — | — | — | — |

Back-check of F065 (Fig 1.6 margin text, p8): "It has become a fashion…pollen tablets as food supplements…tablets and syrups…athletes and race horses" — COVERED (body + Fig 1.6 caption).

**False positives (dismissed, keep)**
- FP8 "Recall the definition and types of placentation that you studied in Class XI" — handled by the planned recall NOTE; the types listed there are Class XI facts supplied for the exercise gap, not fabrication.
- FP9 "What is the importance of the MMC undergoing meiosis?", "What will be the ploidy…?", "Observe the distribution of cells…", "There is a characteristic distribution of the cells", "It is of interest to note" — embedded questions / transitional filler.

---

## Pair 4 — §1.2.3 (Pollination + Kinds + Autogamy/Geitonogamy/Xenogamy + Agents + Outbreeding Devices + Pollen-pistil Interaction)
Read source pp. 11–17 (from "1.2.3 Pollination" to "…and the flower rebagged") against script blocks `# ---- 1.2.3 Pollination ----`, `# ---- 1.2.3 Kinds of Pollination ----`, `# ---- 1.2.3 Agents of Pollination ----`, `# ---- 1.2.3 Outbreeding Devices ----`, `# ---- 1.2.3 Pollen-pistil Interaction ----`. All 8 sub-headings (H2 + 7×H3) present.

| Block | Status | Covered | Missing | Fabricated | Drifted | Uninventoried |
|---|---|---|---|---|---|---|
| Pollination (F116–F119) | CLEAN | 4/4 | — | — | — | — |
| Kinds (F120–F137) | **ISSUES** | 18/18; 2/2 Fig 1.9 labels | cleistogamy mechanism | — | **DR3** F126 examples; **DR4** "figure below" | **U4** |
| Agents (F138–F165) | **ISSUES** | 28/28; 3/3 Fig 1.11 labels | see U5–U8 | — | **DR5** F156 "in some species" dropped | **U5–U8** |
| Outbreeding (F166–F173) | **ISSUES** | 8/8 | "Both these devices prevent autogamy" | — | — | **U9** |
| Pollen-pistil (F174–F191) | **ISSUES** | 18/18; 11/11 Fig 1.12 labels | antecedent of "This dialogue" | — | **DR6** emasculation condition | **U10–U12** |

**Confirmed defects**
- **D6 (U4 + missing).** Cleistogamy mechanism absent: "In such flowers, the anthers and stigma lie close to each other. When anthers dehisce in the flower buds, pollen grains come in contact with the stigma to effect pollination."
- **D7 (DR3).** NCERT: "Some plants such as *Viola* (common pansy), *Oxalis*, and *Commelina* produce two types of flowers". Script (and inventory F126) attach the three genera to the *chasmogamous* bullet only — wrong attribution (they are the standard cleistogamy examples). "common pansy" also dropped.
- **D8 (DR4, layout-text drift).** Chasmogamous bullet says "labelled in the figure below" but the Fig 1.9 row is placed *above* that sentence.
- **D9 (U5).** Corn cob: "the ears you see are nothing but the stigma and style which wave in the wind to trap pollen grains" — missing (F144 truncated at "corn cob").
- **D10 (U6).** Water: "It is believed, particularly for some bryophytes and pteridophytes, that their distribution is limited because of the need for water…"; "Not all aquatic plants use water for pollination. In a majority of aquatic plants such as water hyacinth and water lily, the flowers emerge above the level of water and are pollinated by insects or wind…"; "*Vallisneria* and *Hydrilla* which grow in fresh water"; Vallisneria pollen "carried passively by water currents; some of them eventually reach the female flowers" — all missing.
- **D11 (U7 + DR5).** Biotic: "Often flowers of animal-pollinated plants are specifically adapted for a particular species of animal."; "Animals are attracted to flowers by colour and/or fragrance."; "To sustain animal visits, the flowers have to provide rewards"; F156 qualifier "in some species" dropped.
- **D12 (U8).** Yucca mechanism: "The moth deposits its eggs in the locule of the ovary and the flower, in turn, gets pollinated by the moth. The larvae of the moth come out of the eggs as the seeds start developing." — missing.
- **D13 (U9).** "Both these devices [non-synchrony, different positions] prevent autogamy." — missing from the device table.
- **D14 (U10, antecedent — Ch9-D9 class).** Script says "This <b>dialogue</b> is mediated…" with no antecedent. NCERT: "Often, pollen of the wrong type, either from other species or from the same plant (if it is self-incompatible), also land on the stigma." and "The ability of the pistil to recognise the pollen followed by its acceptance or rejection is the result of a continuous dialogue between pollen grain and the pistil." Also "only in recent years … botanists have been able to identify some of the pollen and pistil components".
- **D15 (U11).** "The contents of the pollen grain move into the pollen tube."; "pollen-pistil interaction is a dynamic process involving pollen recognition followed by promotion or inhibition of the pollen. The knowledge … would help the plant breeder in manipulating pollen-pistil interaction, even in incompatible pollinations, to get desired hybrids."; in-text activity facts: pollen of pea, chickpea, *Crotalaria*, balsam, *Vinca* germinated in ~10 per cent sugar solution, tubes seen after 15–30 min — missing.
- **D16 (U12 + DR6).** Artificial hybridisation: breeder crosses "different species and often genera to combine desirable characters to produce commercially 'superior' varieties" (missing); emasculation is necessary "*If the female parent bears bisexual flowers*" (condition dropped); post-bagging steps (dust mature pollen when stigma receptive, rebag, fruits allowed to develop; unisexual: bag buds, pollinate when receptive, rebag) missing.

**Pass 1 signal (stated plainly).** 11 confirmed items in one section is more than a handful: §1.2.3 was under-inventoried in Pass 1 (rows truncated with "…" dropped whole sentences). Per §3 "Fixing confirmed items", §1.2.3 was re-read sentence-by-sentence as a Pass 1 redo and the missing sentences are logged as **new rows with suffix IDs** (not back-dated into the freeze).

**False positives (dismissed, keep)**
- FP10 "Can you list the possible external agents?", "Do you think that cleistogamy is advantageous…?", "What would be the reason for this?" — embedded questions.
- FP11 Script NOTE "Colour and nectar are advertisements aimed at animals…" — an answer to the NCERT in-text question, consistent with F152; not a contradiction.
- FP12 Script "Because pollen transfer by abiotic agents is not directed towards the target…" vs NCERT "chance factor … to compensate for this uncertainties and associated loss" — faithful paraphrase of the same causal claim.
- FP13 Observe-flowers-of-Cucumber/Mango/… activity — observation exercise; its only fact (visitors must contact anthers and stigma) is carried by F163's robber definition.
