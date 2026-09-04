# Frozen Inventory — Class 11 Chapter 4: Animal Kingdom
Source: `Chapter/class 11/Chapter 04 - Animal Kingdom.pdf` (18 source pages) | Frozen: **FROZEN 2026-09-03 at 1-Z** (Pass 1 complete — all five session kinds ran: 1-S, 1-H, 1-O, 1-F, 1-Z; ticking begins in Pass 2) | Rows: 352

Tick legend: `x` = written into the script and verified present in the generated PDF. All rows are unticked — Pass 2 has not started.

## Status of this file

This inventory was **started from zero on 2026-09-03**. The previous file at this path was not a Gate 1 inventory at all — it was a figure-extraction write-up with no Facts table, no heading/opener rows, no summary classification and no exercise-gap table. It has been moved to `Ch4_prior_figure_notes_UNTRUSTED.md` and **nothing in it is treated as a finding**. Per operator instruction, only the **extracted figure assets** in `assets/` are trusted; every claim about them (page numbers, label sets, mono/verified status) is re-derived in session 1-F.

Chapter 4 is run as a **big chapter** (§8): Pass 1a inventories the first half, Pass 1b the second half, into this same file. Gate 1 is evaluated over the whole chapter only after 1b.

### Half seam (fixed here so nothing is double-covered or dropped)

| Half | Scope | Source pages |
|---|---|---|
| **1a** | Chapter intro, §4.1 and all of §4.1.1–§4.1.6, §4.2 opener, and §4.2.1–§4.2.10 (Porifera through Hemichordata — the non-chordates), incl. the Figure 4.4 footnote | 1–9 |
| **1b** | §4.2.11 Chordata and all of §4.2.11.1–§4.2.11.7, TABLE 4.1, TABLE 4.2 (**all 11 phylum rows, including the non-chordate rows**), SUMMARY, EXERCISES | 10–18 |

Seam rule: TABLE 4.2 is assigned to **1b by physical location** even though its first ten rows describe 1a phyla. 1a must not pre-empt it.

### Session log (each session states its own machine-derived row count)

| Session | Scope | Status | Rows added |
|---|---|---|---|
| 1a-S | Steps 1–3, prose facts, first half | **DONE** | 154 (F001–F154) |
| 1a-H | Step 4, heading sweep, first half | **DONE** | 21 (F155–F175) |
| 1a-O | Step 5, opener sweep, first half | **DONE** | 19 (F176–F194) |
| 1b-S | Steps 1–3, prose facts, second half | **DONE (2026-09-03)** | 130 (F195–F324) |
| 1b-H | Step 4, heading sweep, second half | **DONE (2026-09-03)** | 10 (F325–F334) |
| 1b-O | Step 5, opener sweep, second half | **DONE (2026-09-03)** | 8 (F335–F342) |
| 1-F | Step 6, figures, whole chapter | **DONE (2026-09-03)** | 26 manifest rows |
| 1-F (resumed) | Step 6 continued — figure-label matrix + manifest caption/page audit | **DONE (2026-09-03)** — discharges carry-over #8; also found and fixed carry-over #9 (12 wrong captions + 6 wrong pages in the manifest itself, all assets confirmed correct) | 7 Facts rows (F343–F349) |
| 1-Z | Steps 7–10, gaps + summary + freeze | **DONE (2026-09-03)** — exercise-gap scan (15 exercises: 13 COVERED, 2 GAP, 0 overlooked), summary two-pass check (34 sentences: 3 SUMMARY-UNIQUE folded, 31 BODY-PRESENT, 0 overlooked), freeze + machine recount | 3 Facts rows (F350–F352, summary folds) |

**Pass 1 is complete — all five session kinds ran.** 1a (154 + 21 + 19 = 194) + 1b (130 + 10 + 8 = 148) = 342 rows; **1-F** added 7 figure-label matrix rows (F343–F349) → 349; **1-Z** folded 3 SUMMARY-UNIQUE facts (F350–F352) → **352 rows total, machine-re-parsed below**. 1-Z also ran the exercise-gap scan (15 exercises: 13 COVERED, 2 GAP, 0 overlooked) and the summary two-pass check (34 sentences: 3 SUMMARY-UNIQUE folded, 31 BODY-PRESENT, 0 overlooked), then froze the file. **Gate 1 is now evaluable over the whole chapter and is GREEN** (see status below); the inventory is **FROZEN** — no further rows are added in Pass 2, only ticks.

> **Gate 1 status: CLOSED (GREEN) 2026-09-03; Pass 2 not started.** All nine Pass-1 sessions ran, each with its own machine-derived row count: 1a-S, 1a-H, 1a-O, 1b-S, 1b-H, 1b-O, 1-F, 1-F (resumed), 1-Z. The inventory is frozen at **352 rows (F001–F352, contiguous, 0 gaps/dupes)**, machine-validated (`scratch/ch4_gate1/validate_1z.py`). **Gate 1 closed is NOT chapter closed** — there is no script, no PDF, and all 352 rows are unticked. Chapter 4 must **not** appear in any "Done" completion tally.

### 1a-S census — re-parsed from the Facts table itself (step 10), never hand-tallied

Re-parsing the finished table with `check_pdf.py`'s own row logic gives **154 Facts rows, IDs `F001`–`F154`, contiguous with no gaps and no duplicates**, all unticked. The total is derivable from this per-section list, which sums to 154:

`4.0`=2, `4.1`=2, `4.1.1`=11, `4.1.2`=4, `4.1.3`=3, `4.1.4`=5, `4.1.5`=2, `4.1.6`=2, `4.2`=3, `4.2.1`=13, `4.2.2`=12, `4.2.3`=9, `4.2.4`=10, `4.2.5`=10, `4.2.6`=12, `4.2.7`=19, `4.2.8`=11, `4.2.9`=12, `4.2.10`=12 — 19 sections, 154 rows.

> **Pass 3(b) amendment (§4.1 verify):** one antecedent row, **F015a** (`4.1.2` — "Animals can be categorised on the basis of their symmetry."), was added during Pass 3(b) as an honest Pass 1 freeze gap (see §4.1 verification log below). It was **not** back-dated into the 1a-S census above; with it, `4.1.2` = 5 and the 1a-S total is **155**. IDs `F016`–`F154` are unchanged (suffix insertion, per the Ch9 F194a/F221a/F225a precedent).

`Type` histogram (machine-grouped, all lowercase, no casing split): feature 86, definition 24, example 17, term 10, number 4, etymology 4, comparison 4, process 3, list 1, exception 1 = 154.

### 1a-H census — re-parsed from the Facts table itself (step 10)

Re-parsing the finished table gives **21 heading rows, IDs `F155`–`F175`, contiguous, all unticked**. The total is derivable from this list: **20 numbered/title headings + the 1 structural sidebar row** —

- Chapter-title tier: `CHAPTER 4`, `ANIMAL KINGDOM` (F155–F156) = 2
- §-title tier (small-caps): `4.1 BASIS OF CLASSIFICATION` (F157), `4.2 CLASSIFICATION OF ANIMALS` (F164) = 2
- Numbered sub-headings: `4.1.1`–`4.1.6` (F158–F163) = 6, and `4.2.1`–`4.2.10` (F165–F174) = 10 → 16
- Structural row: chapter-opening contents sidebar, page 1 (F175) = 1

2 + 2 + 16 + 1 = **21**, matching the machine tally. **No unnumbered sub-headings exist in the 1a half** — every 12.0/13.0 bold line on pages 1–9 is a numbered heading; 10.5 bold runs are inline term emphasis, excluded. `4.2.11 Phylum – Chordata` sits physically on page 9 but belongs to **1b** by the fixed seam and was not taken here.

### 1a-O census — re-parsed from the Facts table itself (step 10)

Re-parsing gives **19 opener rows, IDs `F176`–`F194`, contiguous, all unticked** — exactly one opener for each of the 19 sections in the 1a half. Count derivable from the list: `4.0`(1) + `4.1`(1) + `4.1.1`–`4.1.6`(6) + `4.2`(1) + `4.2.1`–`4.2.10`(10) = 1 + 1 + 6 + 1 + 10 = **19**, matching the machine tally. Openers were read from **layout reading-order** (blocks sorted by y-position), not the raw text stream — see carry-over #5 (discharged). §4.2.11 Chordata's opener (page 9) was not taken; it belongs to 1b.

`check_pdf.py._extract_labels` baseline was **0 label rows, 0 figures, no phantom `Fig #` row** before 1-F. The figure manifest now contains **26 non-doubled caption rows**, including the unnumbered Vertebrata chart; figure rows are documentation only and remain unticked until Pass 2.

### 1b-S census — re-parsed from the Facts table itself (step 10), never hand-tallied

Re-parsing the finished table gives **130 prose-fact rows, IDs `F195`–`F324`, contiguous, all unticked** — source pages 9(§4.2.11 opener)–15 (through TABLE 4.2). The total is derivable from this per-section list, which sums to 130:

`4.2.11`=24 (Chordata prose 12 + TABLE 4.1 title+5 rows = 6 + Vertebrata chart 6), `4.2.11.1`=10, `4.2.11.2`=16, `4.2.11.3`=12, `4.2.11.4`=15, `4.2.11.5`=12, `4.2.11.6`=15, `4.2.11.7`=13, `4.2`=13 (chapter-wide transition 1 + TABLE 4.2 title+11 rows = 12) — 9 section-groups, 130 rows.

`Type` histogram of the 1b-S rows (machine-grouped, all lowercase): feature 96, example 9, comparison 7, definition 6, list 5, number 2, etymology 2, caption 2, exception 1 = 130.

**Seam cross-check (TABLE 4.2 vs 1a prose, per the seam rule):** TABLE 4.2's ten non-chordate rows (F314–F323) were reassembled **column-major** per carry-over #7 and checked against the per-phylum prose already in 1a (F035–F154). All values agree with the prose except where the source table itself is terser than its prose — recorded as source wording, not a defect: Porifera symmetry reads **"Various"** in the table (prose F016/F036 say "mostly asymmetrical"), and Echinodermata symmetry reads **"Radial"** in the table (prose F133 gives the fuller "adult radial / larvae bilateral"). Both are verbatim from TABLE 4.2 and preserved as such. The 11th row (F324, Chordata) is cross-checked against 1b's own Chordata prose (F195–F206).

### 1b-H census — re-parsed from the Facts table itself (step 10)

Re-parsing gives **10 heading rows, IDs `F325`–`F334`, contiguous, all unticked**. The total is derivable from this list: **8 numbered headings + 2 unnumbered structural headings** —

- Numbered: `4.2.11 Phylum – Chordata` (F325), and the seven classes `4.2.11.1`–`4.2.11.7` (F326–F332) = 8.
- Unnumbered structural: `SUMMARY` (F333, source page 16), `EXERCISES` (F334, source page 17) = 2.

8 + 2 = **10**, matching the machine tally. Carry-over #6 (each class heading renders **five times** as a faux-bold overprint on pages 11–15) was respected: every class was counted **once**. The `4.2.11 Phylum – Chordata` heading physically sits on source page 9 but is 1b's by the fixed seam (1a-H deliberately left it) and is taken here.

### 1b-O census — re-parsed from the Facts table itself (step 10)

Re-parsing gives **8 opener rows, IDs `F335`–`F342`, contiguous, all unticked** — exactly one opener for each of the 8 content sections in the 1b half (`4.2.11` and `4.2.11.1`–`4.2.11.7`). Count derivable from that list: 1 + 7 = **8**, matching the machine tally. `SUMMARY` and `EXERCISES` are not content sections and take **no** opener row; their content is processed at 1-Z. The §4.2.11 Chordata opener (F335, source page 9, "Animals belonging to phylum Chordata are fundamentally characterised…") is the genuine first sentence of the section in the source.

### Whole-chapter census after Pass 1b — re-parsed from the Facts table (step 10)

Re-parsing immediately after Pass 1b (before the resumed 1-F session) gave **342 rows, IDs `F001`–`F342`, contiguous, 0 gaps, 0 duplicate IDs, all unticked** (Pass 2 has not started). Derivable as 1a (194) + 1b (148) = 342. `Type` histogram at that point (machine-grouped, all lowercase, **no casing split**): feature 182, heading 31, opener 27, definition 30, example 26, comparison 11, term 10, number 6, etymology 6, list 6, process 3, caption 2, exception 2 = **342**. `check_pdf.py._extract_labels` returned **0 labels / 0 figures / no phantom `Fig #` row** at that point — expected, because the figure-**label matrix** had not yet been written (carry-over #8, then OPEN).

### Whole-chapter census after resumed 1-F — re-parsed from the Facts table (step 10)

Re-parsing after the resumed 1-F session (carry-over #8 discharge) gives **349 rows, IDs `F001`–`F349`, contiguous, 0 gaps, 0 duplicate IDs, all unticked**. Derivable as 342 (post-1b) + 7 (F343–F349, the figure-label matrix) = 349. `Type` histogram now: feature 182, heading 31, opener 27, definition 30, example 26, comparison 11, term 10, number 6, etymology 6, list 6, process 3, **caption 9** (2 original + 7 new label rows), exception 2 = **349**. `check_pdf.py._extract_labels` now returns **6 fig-id groups / 56 individual label strings** across the **7 label-bearing Facts rows** F343–F349 (4+2+26+2+3+4+15 = 56; the parser keys figures on the Section column, so F348 and F349 — both Section 4.2.11 — collapse into one group, giving 6 groups for 7 rows), **0 doubled, no phantom `Fig #` row** — carry-over #8 is discharged. The figure manifest's own caption/page defects (carry-over #9, found while harvesting the labels) are corrected directly in the "Figure manifest" table above; they do not add or remove Facts rows.

### Whole-chapter census after 1-Z (FROZEN) — re-parsed from the Facts table (step 10)

Re-parsing the **frozen** table with the machine (`scratch/ch4_gate1/validate_1z.py`, importing `check_pdf._extract_labels` verbatim) gives **352 rows, IDs `F001`–`F352`, contiguous, 0 gaps, 0 duplicate IDs, all unticked** (Pass 2 has not started). Derivable as 349 (post-1-F) + 3 (F350–F352, the SUMMARY-UNIQUE folds) = 352. `Type` histogram now: feature **185**, heading 31, definition 30, opener 27, example 26, comparison 11, term 10, **caption 9**, number 6, list 6, etymology 6, process 3, exception 2 = **352**. All three folds are `Type: feature`, so feature rose 182 → 185; every other value is unchanged from the post-1-F census. `Type` uses one normalised lowercase spelling per value (machine-asserted, no casing split). `check_pdf.py._extract_labels` returns **6 fig-id groups / 56 label strings** across the 7 label-bearing rows (F343–F349), **0 doubled, no phantom `Fig #` row** — unchanged by the folds, since F350–F352 carry no `Figure labels:` wording.

**Step-10 reconciliation — every live restatement now agrees.** Header (352, FROZEN), the session-log 1-Z row (DONE), the Pass-1-complete summary line, this census, and carry-over #8 all state the same machine-derived numbers. Two stale/imprecise claims were corrected at 1-Z: (a) carry-over #8's stale **"47" label strings → 56**; (b) the imprecise **"7 labelled figures" → 6 fig-id groups for 7 label rows** (post-1-F census and carry-over #8), because `_extract_labels` groups on the Section column and F348 + F349 share §4.2.11. The 6-vs-7 difference is a parser-grouping artifact, **not** a missing or duplicated figure — logged as cosmetic carry-over #10; it changes no pass/fail outcome.

### `Type` controlled vocabulary (normalised lowercase, asserted at 1-Z)

`definition`, `feature`, `number`, `example`, `process`, `comparison`, `exception`, `etymology`, `list`, `term`, `heading`, `opener`, `caption`

## Facts
| ID | Section | Type | Exact original wording | Ticked |
|----|---------|------|------------------------|--------|
| F001 | 4.0 | number | "As over a million species of animals have been described till now, the need for classification becomes all the more important." | x |
| F002 | 4.0 | feature | "The classification also helps in assigning a systematic position to newly described species." | x |
| F003 | 4.1 | list | "there are fundamental features common to various individuals in relation to the arrangement of cells, body symmetry, nature of coelom, patterns of digestive, circulatory or reproductive systems" | x |
| F004 | 4.1 | feature | "These features are used as the basis of animal classification and some of them are discussed here." | x |
| F005 | 4.1.1 | feature | "Though all members of Animalia are multicellular, all of them do not exhibit the same pattern of organisation of cells." | x |
| F006 | 4.1.1 | definition | "in sponges, the cells are arranged as loose cell aggregates, i.e., they exhibit cellular level of organisation" | x |
| F007 | 4.1.1 | feature | "Some division of labour (activities) occur among the cells." | x |
| F008 | 4.1.1 | definition | "In coelenterates, the arrangement of cells is more complex. Here the cells performing the same function are arranged into tissues, hence is called tissue level of organisation." | x |
| F009 | 4.1.1 | definition | "A still higher level of organisation, i.e., organ level is exhibited by members of Platyhelminthes and other higher phyla where tissues are grouped together to form organs, each specialised for a particular function." | x |
| F010 | 4.1.1 | definition | "In animals like Annelids, Arthropods, Molluscs, Echinoderms and Chordates, organs have associated to form functional systems, each system concerned with a specific physiological function. This pattern is called organ system level of organisation." | x |
| F011 | 4.1.1 | feature | "Organ systems in different groups of animals exhibit various patterns of complexities." | x |
| F012 | 4.1.1 | definition | "the digestive system in Platyhelminthes has only a single opening to the outside of the body that serves as both mouth and anus, and is hence called incomplete" | x |
| F013 | 4.1.1 | definition | "A complete digestive system has two openings, mouth and anus." | x |
| F014 | 4.1.1 | definition | "(i) open type in which the blood is pumped out of the heart and the cells and tissues are directly bathed in it" | x |
| F015 | 4.1.1 | definition | "(ii) closed type in which the blood is circulated through a series of vessels of varying diameters (arteries, veins and capillaries)" | x |
| F015a | 4.1.2 | feature | "Animals can be categorised on the basis of their symmetry." *(added in Pass 3(b) — §4.1.2 antecedent sentence; Pass 1 freeze gap, already present in script/PDF)* | x |
| F016 | 4.1.2 | definition | "Sponges are mostly asymmetrical, i.e., any plane that passes through the centre does not divide them into equal halves." | x |
| F017 | 4.1.2 | definition | "When any plane passing through the central axis of the body divides the organism into two identical halves, it is called radial symmetry." | x |
| F018 | 4.1.2 | example | "Coelenterates, ctenophores and echinoderms have this kind of body plan (Figure 4.1a)." | x |
| F019 | 4.1.2 | definition | "Animals like annelids, arthropods, etc., where the body can be divided into identical left and right halves in only one plane, exhibit bilateral symmetry (Figure 4.1b)." | x |
| F020 | 4.1.3 | definition | "Animals in which the cells are arranged in two embryonic layers, an external ectoderm and an internal endoderm, are called diploblastic animals, e.g., coelenterates." | x |
| F021 | 4.1.3 | feature | "An undifferentiated layer, mesoglea, is present in between the ectoderm and the endoderm (Figure 4.2a)." | x |
| F022 | 4.1.3 | definition | "Those animals in which the developing embryo has a third germinal layer, mesoderm, in between the ectoderm and endoderm, are called triploblastic animals (platyhelminthes to chordates, Figure 4.2b)." | x |
| F023 | 4.1.4 | feature | "Presence or absence of a cavity between the body wall and the gut wall is very important in classification." | x |
| F024 | 4.1.4 | definition | "The body cavity, which is lined by mesoderm is called coelom." | x |
| F025 | 4.1.4 | example | "Animals possessing coelom are called coelomates, e.g., annelids, molluscs, arthropods, echinoderms, hemichordates and chordates (Figure 4.3a)." | x |
| F026 | 4.1.4 | definition | "In some animals, the body cavity is not lined by mesoderm, instead, the mesoderm is present as scattered pouches in between the ectoderm and endoderm. Such a body cavity is called pseudocoelom and the animals possessing them are called pseudocoelomates, e.g., aschelminthes (Figure 4.3b)." | x |
| F027 | 4.1.4 | definition | "The animals in which the body cavity is absent are called acoelomates, e.g., platyhelminthes (Figure 4.3c)." | x |
| F028 | 4.1.5 | definition | "In some animals, the body is externally and internally divided into segments with a serial repetition of at least some organs." | x |
| F029 | 4.1.5 | definition | "For example, in earthworm, the body shows this pattern called metameric segmentation and the phenomenon is known as metamerism." | x |
| F030 | 4.1.6 | definition | "Notochord is a mesodermally derived rod-like structure formed on the dorsal side during embryonic development in some animals." | x |
| F031 | 4.1.6 | definition | "Animals with notochord are called chordates and those animals which do not form this structure are called non-chordates, e.g., porifera to echinoderms." | x |
| F032 | 4.2 | feature | "The broad classification of Animalia, based on common fundamental features as mentioned in the preceding sections, is given in Figure 4.4." | x |
| F033 | 4.2 | feature | "The important characteristic features of the different phyla are described." | x |
| F034 | 4.2 | exception | Figure 4.4 footnote: "*Echinodermata exhibits radial or bilateral symmetry depending on the stage." | x |
| F035 | 4.2.1 | term | "Members of this phylum are commonly known as sponges." | x |
| F036 | 4.2.1 | feature | "They are generally marine and mostly asymmetrical animals (Figure 4.5)." | x |
| F037 | 4.2.1 | feature | "These are primitive multicellular animals and have cellular level of organisation." | x |
| F038 | 4.2.1 | feature | "Sponges have a water transport or canal system." | x |
| F039 | 4.2.1 | process | "Water enters through minute pores (ostia) in the body wall into a central cavity, spongocoel, from where it goes out through the osculum." | x |
| F040 | 4.2.1 | feature | "This pathway of water transport is helpful in food gathering, respiratory exchange and removal of waste." | x |
| F041 | 4.2.1 | term | "Choanocytes or collar cells line the spongocoel and the canals." | x |
| F042 | 4.2.1 | feature | "Digestion is intracellular." | x |
| F043 | 4.2.1 | feature | "The body is supported by a skeleton made up of spicules or spongin fibres." | x |
| F044 | 4.2.1 | feature | "Sexes are not separate (hermaphrodite), i.e., eggs and sperms are produced by the same individual." | x |
| F045 | 4.2.1 | process | "Sponges reproduce asexually by fragmentation and sexually by formation of gametes." | x |
| F046 | 4.2.1 | feature | "Fertilisation is internal and development is indirect having a larval stage which is morphologically distinct from the adult." | x |
| F047 | 4.2.1 | example | "Examples: Sycon (Scypha), Spongilla (Fresh water sponge) and Euspongia (Bath sponge)." | x |
| F048 | 4.2.2 | feature | "They are aquatic, mostly marine, sessile or free-swimming, radially symmetrical animals (Figure 4.6)." | x |
| F049 | 4.2.2 | etymology | "The name cnidaria is derived from the cnidoblasts or cnidocytes (which contain the stinging capsules or nematocysts) present on the tentacles and the body." | x |
| F050 | 4.2.2 | feature | "Cnidoblasts are used for anchorage, defense and for the capture of prey (Figure 4.7)." | x |
| F051 | 4.2.2 | feature | "Cnidarians exhibit tissue level of organisation and are diploblastic." | x |
| F052 | 4.2.2 | feature | "They have a central gastro-vascular cavity with a single opening, mouth on hypostome." | x |
| F053 | 4.2.2 | feature | "Digestion is extracellular and intracellular." | x |
| F054 | 4.2.2 | example | "Some of the cnidarians, e.g., corals have a skeleton composed of calcium carbonate." | x |
| F055 | 4.2.2 | feature | "Cnidarians exhibit two basic body forms called polyp and medusa (Figure 4.6)." | x |
| F056 | 4.2.2 | definition | "The former is a sessile and cylindrical form like Hydra, Adamsia, etc." | x |
| F057 | 4.2.2 | definition | "whereas, the latter is umbrella-shaped and free-swimming like Aurelia or jelly fish" | x |
| F058 | 4.2.2 | process | "Those cnidarians which exist in both forms exhibit alternation of generations (Metagenesis), i.e., polyps produce medusae asexually and medusae form the polyps sexually (e.g., Obelia)." | x |
| F059 | 4.2.2 | example | "Examples: Physalia (Portuguese man-of-war), Adamsia (Sea anemone), Pennatula (Sea-pen), Gorgonia (Sea-fan) and Meandrina (Brain coral)." | x |
| F060 | 4.2.3 | term | "Ctenophores, commonly known as sea walnuts or comb jellies" | x |
| F061 | 4.2.3 | feature | "are exclusively marine, radially symmetrical, diploblastic organisms with tissue level of organisation" | x |
| F062 | 4.2.3 | number | "The body bears eight external rows of ciliated comb plates, which help in locomotion (Figure 4.8)." | x |
| F063 | 4.2.3 | feature | "Digestion is both extracellular and intracellular." | x |
| F064 | 4.2.3 | definition | "Bioluminescence (the property of a living organism to emit light) is well-marked in ctenophores." | x |
| F065 | 4.2.3 | feature | "Sexes are not separate." | x |
| F066 | 4.2.3 | feature | "Reproduction takes place only by sexual means." | x |
| F067 | 4.2.3 | feature | "Fertilisation is external with indirect development." | x |
| F068 | 4.2.3 | example | "Examples: Pleurobrachia and Ctenoplana." | x |
| F069 | 4.2.4 | term | "They have dorso-ventrally flattened body, hence are called flatworms (Figure 4.9)." | x |
| F070 | 4.2.4 | feature | "These are mostly endoparasites found in animals including human beings." | x |
| F071 | 4.2.4 | feature | "Flatworms are bilaterally symmetrical, triploblastic and acoelomate animals with organ level of organisation." | x |
| F072 | 4.2.4 | feature | "Hooks and suckers are present in the parasitic forms." | x |
| F073 | 4.2.4 | feature | "Some of them absorb nutrients from the host directly through their body surface." | x |
| F074 | 4.2.4 | term | "Specialised cells called flame cells help in osmoregulation and excretion." | x |
| F075 | 4.2.4 | feature | "Sexes are not separate." | x |
| F076 | 4.2.4 | feature | "Fertilisation is internal and development is through many larval stages." | x |
| F077 | 4.2.4 | example | "Some members like Planaria possess high regeneration capacity." | x |
| F078 | 4.2.4 | example | "Examples: Taenia (Tapeworm), Fasciola (Liver fluke)." | x |
| F079 | 4.2.5 | term | "The body of the aschelminthes is circular in cross-section, hence, the name roundworms (Figure 4.10)." | x |
| F080 | 4.2.5 | feature | "They may be freeliving, aquatic and terrestrial or parasitic in plants and animals." | x |
| F081 | 4.2.5 | feature | "Roundworms have organ-system level of body organisation." | x |
| F082 | 4.2.5 | feature | "They are bilaterally symmetrical, triploblastic and pseudocoelomate animals." | x |
| F083 | 4.2.5 | feature | "Alimentary canal is complete with a well-developed muscular pharynx." | x |
| F084 | 4.2.5 | feature | "An excretory tube removes body wastes from the body cavity through the excretory pore." | x |
| F085 | 4.2.5 | feature | "Sexes are separate (dioecious), i.e., males and females are distinct." | x |
| F086 | 4.2.5 | comparison | "Often females are longer than males." | x |
| F087 | 4.2.5 | feature | "Fertilisation is internal and development may be direct (the young ones resemble the adult) or indirect." | x |
| F088 | 4.2.5 | example | "Examples : Ascaris (Roundworm), Wuchereria (Filaria worm), Ancylostoma (Hookworm)." | x |
| F089 | 4.2.6 | feature | "They may be aquatic (marine and fresh water) or terrestrial; free-living, and sometimes parasitic." | x |
| F090 | 4.2.6 | feature | "They exhibit organ-system level of body organisation and bilateral symmetry." | x |
| F091 | 4.2.6 | feature | "They are triploblastic, metamerically segmented and coelomate animals." | x |
| F092 | 4.2.6 | etymology | "Their body surface is distinctly marked out into segments or metameres and, hence, the phylum name Annelida (Latin, annulus : little ring) (Figure 4.11)." | x |
| F093 | 4.2.6 | feature | "They possess longitudinal and circular muscles which help in locomotion." | x |
| F094 | 4.2.6 | feature | "Aquatic annelids like Nereis possess lateral appendages, parapodia, which help in swimming." | x |
| F095 | 4.2.6 | feature | "A closed circulatory system is present." | x |
| F096 | 4.2.6 | term | "Nephridia (sing. nephridium) help in osmoregulation and excretion." | x |
| F097 | 4.2.6 | feature | "Neural system consists of paired ganglia (sing. ganglion) connected by lateral nerves to a double ventral nerve cord." | x |
| F098 | 4.2.6 | comparison | "Nereis, an aquatic form, is dioecious, but earthworms and leeches are monoecious." | x |
| F099 | 4.2.6 | feature | "Reproduction is sexual." | x |
| F100 | 4.2.6 | example | "Examples : Nereis, Pheretima (Earthworm) and Hirudinaria (Blood sucking leech)." | x |
| F101 | 4.2.7 | feature | "This is the largest phylum of Animalia which includes insects." | x |
| F102 | 4.2.7 | number | "Over two-thirds of all named species on earth are arthropods (Figure 4.12)." | x |
| F103 | 4.2.7 | feature | "They have organ-system level of organisation." | x |
| F104 | 4.2.7 | feature | "They are bilaterally symmetrical, triploblastic, segmented and coelomate animals." | x |
| F105 | 4.2.7 | feature | "The body of arthropods is covered by chitinous exoskeleton." | x |
| F106 | 4.2.7 | feature | "The body consists of head, thorax and abdomen." | x |
| F107 | 4.2.7 | etymology | "They have jointed appendages (arthros-joint, poda-appendages)." | x |
| F108 | 4.2.7 | feature | "Respiratory organs are gills, book gills, book lungs or tracheal system." | x |
| F109 | 4.2.7 | feature | "Circulatory system is of open type." | x |
| F110 | 4.2.7 | feature | "Sensory organs like antennae, eyes (compound and simple), statocysts or balancing organs are present." | x |
| F111 | 4.2.7 | feature | "Excretion takes place through malpighian tubules." | x |
| F112 | 4.2.7 | feature | "They are mostly dioecious." | x |
| F113 | 4.2.7 | feature | "Fertilisation is usually internal." | x |
| F114 | 4.2.7 | feature | "They are mostly oviparous." | x |
| F115 | 4.2.7 | feature | "Development may be direct or indirect." | x |
| F116 | 4.2.7 | example | "Examples: Economically important insects – Apis (Honey bee), Bombyx (Silkworm), Laccifer (Lac insect)" | x |
| F117 | 4.2.7 | example | "Vectors – Anopheles, Culex and Aedes (Mosquitoes)" | x |
| F118 | 4.2.7 | example | "Gregarious pest – Locusta (Locust)" | x |
| F119 | 4.2.7 | example | "Living fossil – Limulus (King crab)." | x |
| F120 | 4.2.8 | number | "This is the second largest animal phylum (Figure 4.13)." | x |
| F121 | 4.2.8 | feature | "Molluscs are terrestrial or aquatic (marine or fresh water) having an organ-system level of organisation." | x |
| F122 | 4.2.8 | feature | "They are bilaterally symmetrical, triploblastic and coelomate animals." | x |
| F123 | 4.2.8 | feature | "Body is covered by a calcareous shell and is unsegmented with a distinct head, muscular foot and visceral hump." | x |
| F124 | 4.2.8 | feature | "A soft and spongy layer of skin forms a mantle over the visceral hump." | x |
| F125 | 4.2.8 | definition | "The space between the hump and the mantle is called the mantle cavity in which feather like gills are present." | x |
| F126 | 4.2.8 | feature | "They have respiratory and excretory functions." | x |
| F127 | 4.2.8 | feature | "The anterior head region has sensory tentacles." | x |
| F128 | 4.2.8 | term | "The mouth contains a file-like rasping organ for feeding, called radula." | x |
| F129 | 4.2.8 | feature | "They are usually dioecious and oviparous with indirect development." | x |
| F130 | 4.2.8 | example | "Examples: Pila (Apple snail), Pinctada (Pearl oyster), Sepia (Cuttlefish), Loligo (Squid), Octopus (Devil fish), Aplysia (Sea-hare), Dentalium (Tusk shell) and Chaetopleura (Chiton)." | x |
| F131 | 4.2.9 | etymology | "These animals have an endoskeleton of calcareous ossicles and, hence, the name Echinodermata (Spiny bodied, Figure 4.14)." | x |
| F132 | 4.2.9 | feature | "All are marine with organ-system level of organisation." | x |
| F133 | 4.2.9 | comparison | "The adult echinoderms are radially symmetrical but larvae are bilaterally symmetrical." | x |
| F134 | 4.2.9 | feature | "They are triploblastic and coelomate animals." | x |
| F135 | 4.2.9 | feature | "Digestive system is complete with mouth on the lower (ventral) side and anus on the upper (dorsal) side." | x |
| F136 | 4.2.9 | feature | "The most distinctive feature of echinoderms is the presence of water vascular system which helps in locomotion, capture and transport of food and respiration." | x |
| F137 | 4.2.9 | feature | "An excretory system is absent." | x |
| F138 | 4.2.9 | feature | "Sexes are separate." | x |
| F139 | 4.2.9 | feature | "Reproduction is sexual." | x |
| F140 | 4.2.9 | feature | "Fertilisation is usually external." | x |
| F141 | 4.2.9 | feature | "Development is indirect with free-swimming larva." | x |
| F142 | 4.2.9 | example | "Examples: Asterias (Star fish), Echinus (Sea urchin), Antedon (Sea lily), Cucumaria (Sea cucumber) and Ophiura (Brittle star)." | x |
| F143 | 4.2.10 | comparison | "Hemichordata was earlier considered as a sub-phylum under phylum Chordata. But now it is placed as a separate phylum under non-chordata." | x |
| F144 | 4.2.10 | term | "Hemichordates have a rudimentary structure in the collar region called stomochord, a structure similar to notochord." | x |
| F145 | 4.2.10 | feature | "This phylum consists of a small group of worm-like marine animals with organ-system level of organisation." | x |
| F146 | 4.2.10 | feature | "They are bilaterally symmetrical, triploblastic and coelomate animals." | x |
| F147 | 4.2.10 | feature | "The body is cylindrical and is composed of an anterior proboscis, a collar and a long trunk (Figure 4.15)." | x |
| F148 | 4.2.10 | feature | "Circulatory system is of open type." | x |
| F149 | 4.2.10 | feature | "Respiration takes place through gills." | x |
| F150 | 4.2.10 | term | "Excretory organ is proboscis gland." | x |
| F151 | 4.2.10 | feature | "Sexes are separate." | x |
| F152 | 4.2.10 | feature | "Fertilisation is external." | x |
| F153 | 4.2.10 | feature | "Development is indirect." | x |
| F154 | 4.2.10 | example | "Examples: Balanoglossus and Saccoglossus." | x |
| F155 | 4.0 | heading | "CHAPTER 4" | x |
| F156 | 4.0 | heading | "ANIMAL KINGDOM" | x |
| F157 | 4.1 | heading | "4.1 BASIS OF CLASSIFICATION" | x |
| F158 | 4.1.1 | heading | "4.1.1 Levels of Organisation" | x |
| F159 | 4.1.2 | heading | "4.1.2 Symmetry" | x |
| F160 | 4.1.3 | heading | "4.1.3 Diploblastic and Triploblastic Organisation" | x |
| F161 | 4.1.4 | heading | "4.1.4 Coelom" | x |
| F162 | 4.1.5 | heading | "4.1.5 Segmentation" | x |
| F163 | 4.1.6 | heading | "4.1.6 Notochord" | x |
| F164 | 4.2 | heading | "4.2 CLASSIFICATION OF ANIMALS" | x |
| F165 | 4.2.1 | heading | "4.2.1 Phylum – Porifera" | x |
| F166 | 4.2.2 | heading | "4.2.2 Phylum – Coelenterata (Cnidaria)" | x |
| F167 | 4.2.3 | heading | "4.2.3 Phylum – Ctenophora" | x |
| F168 | 4.2.4 | heading | "4.2.4 Phylum – Platyhelminthes" | x |
| F169 | 4.2.5 | heading | "4.2.5 Phylum – Aschelminthes" | x |
| F170 | 4.2.6 | heading | "4.2.6 Phylum – Annelida" | x |
| F171 | 4.2.7 | heading | "4.2.7 Phylum – Arthropoda" | x |
| F172 | 4.2.8 | heading | "4.2.8 Phylum – Mollusca" | x |
| F173 | 4.2.9 | heading | "4.2.9 Phylum – Echinodermata" | x |
| F174 | 4.2.10 | heading | "4.2.10 Phylum – Hemichordata" | x |
| F175 | 4.0 | heading | Chapter-opening contents sidebar (source page 1, italic light face, not a body heading tier): "4.1 Basis of Classification"; "4.2 Classification of Animals" | x |
| F176 | 4.0 | opener | "When you look around, you will observe different animals with different structures and forms." | x |
| F177 | 4.1 | opener | "Inspite of differences in structure and form of different animals, there are fundamental features common to various individuals in relation to the arrangement of cells, body symmetry, nature of coelom, patterns of digestive, circulatory or reproductive systems." | x |
| F178 | 4.1.1 | opener | "Though all members of Animalia are multicellular, all of them do not exhibit the same pattern of organisation of cells." | x |
| F179 | 4.1.2 | opener | "Animals can be categorised on the basis of their symmetry." | x |
| F180 | 4.1.3 | opener | "Animals in which the cells are arranged in two embryonic layers, an external ectoderm and an internal endoderm, are called diploblastic animals, e.g., coelenterates." | x |
| F181 | 4.1.4 | opener | "Presence or absence of a cavity between the body wall and the gut wall is very important in classification." | x |
| F182 | 4.1.5 | opener | "In some animals, the body is externally and internally divided into segments with a serial repetition of at least some organs." | x |
| F183 | 4.1.6 | opener | "Notochord is a mesodermally derived rod-like structure formed on the dorsal side during embryonic development in some animals." | x |
| F184 | 4.2 | opener | "The broad classification of Animalia, based on common fundamental features as mentioned in the preceding sections, is given in Figure 4.4." | x |
| F185 | 4.2.1 | opener | "Members of this phylum are commonly known as sponges." | x |
| F186 | 4.2.2 | opener | "They are aquatic, mostly marine, sessile or free-swimming, radially symmetrical animals (Figure 4.6)." | x |
| F187 | 4.2.3 | opener | "Ctenophores, commonly known as sea walnuts or comb jellies are exclusively marine, radially symmetrical, diploblastic organisms with tissue level of organisation." | x |
| F188 | 4.2.4 | opener | "They have dorso-ventrally flattened body, hence are called flatworms (Figure 4.9)." | x |
| F189 | 4.2.5 | opener | "The body of the aschelminthes is circular in cross-section, hence, the name roundworms (Figure 4.10)." | x |
| F190 | 4.2.6 | opener | "They may be aquatic (marine and fresh water) or terrestrial; free-living, and sometimes parasitic." | x |
| F191 | 4.2.7 | opener | "This is the largest phylum of Animalia which includes insects." | x |
| F192 | 4.2.8 | opener | "This is the second largest animal phylum (Figure 4.13)." | x |
| F193 | 4.2.9 | opener | "These animals have an endoskeleton of calcareous ossicles and, hence, the name Echinodermata (Spiny bodied, Figure 4.14)." | x |
| F194 | 4.2.10 | opener | "Hemichordata was earlier considered as a sub-phylum under phylum Chordata." | x |
| F195 | 4.2.11 | definition | "Animals belonging to phylum Chordata are fundamentally characterised by the presence of a notochord, a dorsal hollow nerve cord and paired pharyngeal gill slits (Figure 4.16)." | x |
| F196 | 4.2.11 | feature | "These are bilaterally symmetrical, triploblastic, coelomate with organ-system level of organisation." | x |
| F197 | 4.2.11 | feature | "They possess a post anal tail and a closed circulatory system." | x |
| F198 | 4.2.11 | feature | "Table 4.1 presents a comparison of salient features of chordates and non-chordates." | x |
| F199 | 4.2.11 | feature | "Phylum Chordata is divided into three subphyla: Urochordata or Tunicata, Cephalochordata and Vertebrata." | x |
| F200 | 4.2.11 | definition | "Subphyla Urochordata and Cephalochordata are often referred to as protochordates (Figure 4.17) and are exclusively marine." | x |
| F201 | 4.2.11 | comparison | "In Urochordata, notochord is present only in larval tail, while in Cephalochordata, it extends from head to tail region and is persistent throughout their life." | x |
| F202 | 4.2.11 | example | "Examples: Urochordata – Ascidia, Salpa, Doliolum; Cephalochordata – Branchiostoma (Amphioxus or Lancelet)." | x |
| F203 | 4.2.11 | feature | "The members of subphylum Vertebrata possess notochord during the embryonic period." | x |
| F204 | 4.2.11 | feature | "The notochord is replaced by a cartilaginous or bony vertebral column in the adult." | x |
| F205 | 4.2.11 | comparison | "Thus all vertebrates are chordates but all chordates are not vertebrates." | x |
| F206 | 4.2.11 | feature | "Besides the basic chordate characters, vertebrates have a ventral muscular heart with two, three or four chambers, kidneys for excretion and osmoregulation and paired appendages which may be fins or limbs." | x |
| F207 | 4.2.11 | caption | TABLE 4.1 title: "TABLE 4.1 Comparison of Chordates and Non-chordates" | x |
| F208 | 4.2.11 | comparison | TABLE 4.1 row 1 — Chordates: "Notochord present." / Non-chordates: "Notochord absent." | x |
| F209 | 4.2.11 | comparison | TABLE 4.1 row 2 — Chordates: "Central nervous system is dorsal, hollow and single." / Non-chordates: "Central nervous system is ventral, solid and double." | x |
| F210 | 4.2.11 | comparison | TABLE 4.1 row 3 — Chordates: "Pharynx perforated by gill slits." / Non-chordates: "Gill slits are absent." | x |
| F211 | 4.2.11 | comparison | TABLE 4.1 row 4 — Chordates: "Heart is ventral." / Non-chordates: "Heart is dorsal (if present)." | x |
| F212 | 4.2.11 | comparison | TABLE 4.1 row 5 — Chordates: "A post-anal part (tail) is present." / Non-chordates: "Post-anal tail is absent." | x |
| F213 | 4.2.11 | feature | "The subphylum Vertebrata is further divided as follows:" (lead-in to the Vertebrata classification chart, source page 11) | x |
| F214 | 4.2.11 | list | Vertebrata chart: Vertebrata is split into two divisions — "Agnatha (lacks jaw)" and "Gnathostomata (bears jaw)". | x |
| F215 | 4.2.11 | list | Vertebrata chart: Division "Agnatha (lacks jaw)" contains Class "1. Cyclostomata". | x |
| F216 | 4.2.11 | list | Vertebrata chart: Division "Gnathostomata (bears jaw)" contains two Super Classes — "Pisces (bear fins)" and "Tetrapoda (bear limbs)". | x |
| F217 | 4.2.11 | list | Vertebrata chart: Super Class "Pisces (bear fins)" contains Classes "1. Chondrichthyes" and "2. Osteichthyes". | x |
| F218 | 4.2.11 | list | Vertebrata chart: Super Class "Tetrapoda (bear limbs)" contains Classes "1. Amphibia", "2. Reptilia", "3. Aves" and "4. Mammals". | x |
| F219 | 4.2.11.1 | feature | "All living members of the class Cyclostomata are ectoparasites on some fishes." | x |
| F220 | 4.2.11.1 | number | "They have an elongated body bearing 6-15 pairs of gill slits for respiration." | x |
| F221 | 4.2.11.1 | feature | "Cyclostomes have a sucking and circular mouth without jaws (Fig. 4.18)." | x |
| F222 | 4.2.11.1 | feature | "Their body is devoid of scales and paired fins." | x |
| F223 | 4.2.11.1 | feature | "Cranium and vertebral column are cartilaginous." | x |
| F224 | 4.2.11.1 | feature | "Circulation is of closed type." | x |
| F225 | 4.2.11.1 | feature | "Cyclostomes are marine but migrate for spawning to fresh water." | x |
| F226 | 4.2.11.1 | feature | "After spawning, within a few days, they die." | x |
| F227 | 4.2.11.1 | feature | "Their larvae, after metamorphosis, return to the ocean." | x |
| F228 | 4.2.11.1 | example | "Examples: Petromyzon (Lamprey) and Myxine (Hagfish)." | x |
| F229 | 4.2.11.2 | feature | "They are marine animals with streamlined body and have cartilaginous endoskeleton (Figure 4.19)." | x |
| F230 | 4.2.11.2 | feature | "Mouth is located ventrally." | x |
| F231 | 4.2.11.2 | feature | "Notochord is persistent throughout life." | x |
| F232 | 4.2.11.2 | feature | "Gill slits are separate and without operculum (gill cover)." | x |
| F233 | 4.2.11.2 | feature | "The skin is tough, containing minute placoid scales." | x |
| F234 | 4.2.11.2 | feature | "Teeth are modified placoid scales which are backwardly directed." | x |
| F235 | 4.2.11.2 | feature | "Their jaws are very powerful." | x |
| F236 | 4.2.11.2 | feature | "These animals are predaceous." | x |
| F237 | 4.2.11.2 | feature | "Due to the absence of air bladder, they have to swim constantly to avoid sinking." | x |
| F238 | 4.2.11.2 | feature | "Heart is two-chambered (one auricle and one ventricle)." | x |
| F239 | 4.2.11.2 | example | "Some of them have electric organs (e.g., Torpedo) and some possess poison sting (e.g., Trygon)." | x |
| F240 | 4.2.11.2 | definition | "They are cold-blooded (poikilothermous) animals, i.e., they lack the capacity to regulate their body temperature." | x |
| F241 | 4.2.11.2 | feature | "Sexes are separate." | x |
| F242 | 4.2.11.2 | feature | "In males pelvic fins bear claspers." | x |
| F243 | 4.2.11.2 | feature | "They have internal fertilisation and many of them are viviparous." | x |
| F244 | 4.2.11.2 | example | "Examples: Scoliodon (Dog fish), Pristis (Saw fish), Carcharodon (Great white shark), Trygon (Sting ray)." | x |
| F245 | 4.2.11.3 | feature | "It includes both marine and fresh water fishes with bony endoskeleton." | x |
| F246 | 4.2.11.3 | feature | "Their body is streamlined." | x |
| F247 | 4.2.11.3 | feature | "Mouth is mostly terminal (Figure 4.20)." | x |
| F248 | 4.2.11.3 | number | "They have four pairs of gills which are covered by an operculum on each side." | x |
| F249 | 4.2.11.3 | feature | "Skin is covered with cycloid/ctenoid scales." | x |
| F250 | 4.2.11.3 | feature | "Air bladder is present which regulates buoyancy." | x |
| F251 | 4.2.11.3 | feature | "Heart is two-chambered (one auricle and one ventricle)." | x |
| F252 | 4.2.11.3 | feature | "They are cold-blooded animals." | x |
| F253 | 4.2.11.3 | feature | "Sexes are separate." | x |
| F254 | 4.2.11.3 | feature | "Fertilisation is usually external." | x |
| F255 | 4.2.11.3 | feature | "They are mostly oviparous and development is direct." | x |
| F256 | 4.2.11.3 | example | "Examples: Marine – Exocoetus (Flying fish), Hippocampus (Sea horse); Freshwater – Labeo (Rohu), Catla (Katla), Clarias (Magur); Aquarium – Betta (Fighting fish), Pterophyllum (Angel fish)." | x |
| F257 | 4.2.11.4 | etymology | "As the name indicates (Gr., Amphi : dual, bios, life), amphibians can live in aquatic as well as terrestrial habitats (Figure 4.21)." | x |
| F258 | 4.2.11.4 | feature | "Most of them have two pairs of limbs." | x |
| F259 | 4.2.11.4 | feature | "Body is divisible into head and trunk." | x |
| F260 | 4.2.11.4 | feature | "Tail may be present in some." | x |
| F261 | 4.2.11.4 | feature | "The amphibian skin is moist (without scales)." | x |
| F262 | 4.2.11.4 | feature | "The eyes have eyelids." | x |
| F263 | 4.2.11.4 | feature | "A tympanum represents the ear." | x |
| F264 | 4.2.11.4 | definition | "Alimentary canal, urinary and reproductive tracts open into a common chamber called cloaca which opens to the exterior." | x |
| F265 | 4.2.11.4 | feature | "Respiration is by gills, lungs and through skin." | x |
| F266 | 4.2.11.4 | feature | "The heart is three-chambered (two auricles and one ventricle)." | x |
| F267 | 4.2.11.4 | feature | "These are cold-blooded animals." | x |
| F268 | 4.2.11.4 | feature | "Sexes are separate." | x |
| F269 | 4.2.11.4 | feature | "Fertilisation is external." | x |
| F270 | 4.2.11.4 | feature | "They are oviparous and development is indirect." | x |
| F271 | 4.2.11.4 | example | "Examples: Bufo (Toad), Rana (Frog), Hyla (Tree frog), Salamandra (Salamander), Ichthyophis (Limbless amphibia)." | x |
| F272 | 4.2.11.5 | etymology | "The class name refers to their creeping or crawling mode of locomotion (Latin, repere or reptum, to creep or crawl)." | x |
| F273 | 4.2.11.5 | feature | "They are mostly terrestrial animals and their body is covered by dry and cornified skin, epidermal scales or scutes (Fig. 4.22)." | x |
| F274 | 4.2.11.5 | feature | "They do not have external ear openings." | x |
| F275 | 4.2.11.5 | feature | "Tympanum represents ear." | x |
| F276 | 4.2.11.5 | feature | "Limbs, when present, are two pairs." | x |
| F277 | 4.2.11.5 | exception | "Heart is usually three-chambered, but four-chambered in crocodiles." | x |
| F278 | 4.2.11.5 | feature | "Reptiles are poikilotherms." | x |
| F279 | 4.2.11.5 | feature | "Snakes and lizards shed their scales as skin cast." | x |
| F280 | 4.2.11.5 | feature | "Sexes are separate." | x |
| F281 | 4.2.11.5 | feature | "Fertilisation is internal." | x |
| F282 | 4.2.11.5 | feature | "They are oviparous and development is direct." | x |
| F283 | 4.2.11.5 | example | "Examples: Chelone (Turtle), Testudo (Tortoise), Chameleon (Tree lizard), Calotes (Garden lizard), Crocodilus (Crocodile), Alligator (Alligator). Hemidactylus (Wall lizard), Poisonous snakes – Naja (Cobra), Bangarus (Krait), Vipera (Viper)." | x |
| F284 | 4.2.11.6 | feature | "The characteristic features of Aves (birds) are the presence of feathers and most of them can fly except flightless birds (e.g., Ostrich)." | x |
| F285 | 4.2.11.6 | feature | "They possess beak (Figure 4.23)." | x |
| F286 | 4.2.11.6 | feature | "The forelimbs are modified into wings." | x |
| F287 | 4.2.11.6 | feature | "The hind limbs generally have scales and are modified for walking, swimming or clasping the tree branches." | x |
| F288 | 4.2.11.6 | feature | "Skin is dry without glands except the oil gland at the base of the tail." | x |
| F289 | 4.2.11.6 | feature | "Endoskeleton is fully ossified (bony) and the long bones are hollow with air cavities (pneumatic)." | x |
| F290 | 4.2.11.6 | feature | "The digestive tract of birds has additional chambers, the crop and gizzard." | x |
| F291 | 4.2.11.6 | feature | "Heart is completely four-chambered." | x |
| F292 | 4.2.11.6 | definition | "They are warm-blooded (homoiothermous) animals, i.e., they are able to maintain a constant body temperature." | x |
| F293 | 4.2.11.6 | feature | "Respiration is by lungs." | x |
| F294 | 4.2.11.6 | feature | "Air sacs connected to lungs supplement respiration." | x |
| F295 | 4.2.11.6 | feature | "Sexes are separate." | x |
| F296 | 4.2.11.6 | feature | "Fertilisation is internal." | x |
| F297 | 4.2.11.6 | feature | "They are oviparous and development is direct." | x |
| F298 | 4.2.11.6 | example | "Examples : Corvus (Crow), Columba (Pigeon), Psittacula (Parrot), Struthio (Ostrich), Pavo (Peacock), Aptenodytes (Penguin), Neophron (Vulture)." | x |
| F299 | 4.2.11.7 | feature | "They are found in a variety of habitats – polar ice caps, deserts, mountains, forests, grasslands and dark caves." | x |
| F300 | 4.2.11.7 | feature | "Some of them have adapted to fly or live in water." | x |
| F301 | 4.2.11.7 | definition | "The most unique mammalian characteristic is the presence of milk producing glands (mammary glands) by which the young ones are nourished." | x |
| F302 | 4.2.11.7 | feature | "They have two pairs of limbs, adapted for walking, running, climbing, burrowing, swimming or flying (Figure 4.24)." | x |
| F303 | 4.2.11.7 | feature | "The skin of mammals is unique in possessing hair." | x |
| F304 | 4.2.11.7 | feature | "External ears or pinnae are present." | x |
| F305 | 4.2.11.7 | feature | "Different types of teeth are present in the jaw." | x |
| F306 | 4.2.11.7 | feature | "Heart is four-chambered." | x |
| F307 | 4.2.11.7 | feature | "They are homoiothermous." | x |
| F308 | 4.2.11.7 | feature | "Respiration is by lungs." | x |
| F309 | 4.2.11.7 | feature | "Sexes are separate and fertilisation is internal." | x |
| F310 | 4.2.11.7 | feature | "They are viviparous with few exceptions and development is direct." | x |
| F311 | 4.2.11.7 | example | "Examples: Oviparous-Ornithorhynchus (Platypus); Viviparous - Macropus (Kangaroo), Pteropus (Flying fox), Camelus (Camel), Macaca (Monkey), Rattus (Rat), Canis (Dog), Felis (Cat), Elephas (Elephant), Equus (Horse), Delphinus (Common dolphin), Balaenoptera (Blue whale), Panthera tigris (Tiger), Panthera leo (Lion)." | x |
| F312 | 4.2 | feature | "The salient distinguishing features of all phyla under animal kingdom is comprehensively given in the Table 4.2." | x |
| F313 | 4.2 | caption | TABLE 4.2 title: "TABLE 4.2 Salient Features of Different Phyla in the Animal Kingdom" | x |
| F314 | 4.2 | feature | TABLE 4.2 — Porifera: Level of Organisation "Cellular"; Symmetry "Various"; Coelom "Absent"; Segmentation "Absent"; Digestive System "Absent"; Circulatory System "Absent"; Respiratory System "Absent"; Distinctive Features "Body with pores and canals in walls." | x |
| F315 | 4.2 | feature | TABLE 4.2 — Coelenterata (Cnidaria): Level of Organisation "Tissue"; Symmetry "Radial"; Coelom "Absent"; Segmentation "Absent"; Digestive System "Incomplete"; Circulatory System "Absent"; Respiratory System "Absent"; Distinctive Features "Cnidoblasts present." | x |
| F316 | 4.2 | feature | TABLE 4.2 — Ctenophora: Level of Organisation "Tissue"; Symmetry "Radial"; Coelom "Absent"; Segmentation "Absent"; Digestive System "Incomplete"; Circulatory System "Absent"; Respiratory System "Absent"; Distinctive Features "Comb plates for locomotion." | x |
| F317 | 4.2 | feature | TABLE 4.2 — Platyhelminthes: Level of Organisation "Organ & Organ-system"; Symmetry "Bilateral"; Coelom "Absent"; Segmentation "Absent"; Digestive System "Incomplete"; Circulatory System "Absent"; Respiratory System "Absent"; Distinctive Features "Flat body, suckers." | x |
| F318 | 4.2 | feature | TABLE 4.2 — Aschelminthes: Level of Organisation "Organ-system"; Symmetry "Bilateral"; Coelom "Pseudocoelomate"; Segmentation "Absent"; Digestive System "Complete"; Circulatory System "Absent"; Respiratory System "Absent"; Distinctive Features "Often worm-shaped, elongated." | x |
| F319 | 4.2 | feature | TABLE 4.2 — Annelida: Level of Organisation "Organ-system"; Symmetry "Bilateral"; Coelom "Coelomate"; Segmentation "Present"; Digestive System "Complete"; Circulatory System "Present"; Respiratory System "Absent"; Distinctive Features "Body segmentation like rings." | x |
| F320 | 4.2 | feature | TABLE 4.2 — Arthropoda: Level of Organisation "Organ-system"; Symmetry "Bilateral"; Coelom "Coelomate"; Segmentation "Present"; Digestive System "Complete"; Circulatory System "Present"; Respiratory System "Present"; Distinctive Features "Exoskeleton of cuticle, jointed appendages." | x |
| F321 | 4.2 | feature | TABLE 4.2 — Mollusca: Level of Organisation "Organ-system"; Symmetry "Bilateral"; Coelom "Coelomate"; Segmentation "Absent"; Digestive System "Complete"; Circulatory System "Present"; Respiratory System "Present"; Distinctive Features "External skeleton of shell usually present." | x |
| F322 | 4.2 | feature | TABLE 4.2 — Echinodermata: Level of Organisation "Organ-system"; Symmetry "Radial"; Coelom "Coelomate"; Segmentation "Absent"; Digestive System "Complete"; Circulatory System "Present"; Respiratory System "Present"; Distinctive Features "Water vascular system, radial symmetry." | x |
| F323 | 4.2 | feature | TABLE 4.2 — Hemichordata: Level of Organisation "Organ-system"; Symmetry "Bilateral"; Coelom "Coelomate"; Segmentation "Absent"; Digestive System "Complete"; Circulatory System "Present"; Respiratory System "Present"; Distinctive Features "Worm-like with proboscis, collar and trunk." | x |
| F324 | 4.2 | feature | TABLE 4.2 — Chordata: Level of Organisation "Organ-system"; Symmetry "Bilateral"; Coelom "Coelomate"; Segmentation "Present"; Digestive System "Complete"; Circulatory System "Present"; Respiratory System "Present"; Distinctive Features "Notochord, dorsal hollow nerve cord, gill slits with limbs or fins." | x |
| F325 | 4.2.11 | heading | "4.2.11 Phylum – Chordata" | x |
| F326 | 4.2.11.1 | heading | "4.2.11.1 Class – Cyclostomata" | x |
| F327 | 4.2.11.2 | heading | "4.2.11.2 Class – Chondrichthyes" | x |
| F328 | 4.2.11.3 | heading | "4.2.11.3 Class – Osteichthyes" | x |
| F329 | 4.2.11.4 | heading | "4.2.11.4 Class – Amphibia" | x |
| F330 | 4.2.11.5 | heading | "4.2.11.5 Class – Reptilia" | x |
| F331 | 4.2.11.6 | heading | "4.2.11.6 Class – Aves" | x |
| F332 | 4.2.11.7 | heading | "4.2.11.7 Class – Mammalia" | x |
| F333 | SUMMARY | heading | "SUMMARY" (unnumbered structural heading, source page 16) | x |
| F334 | EXERCISES | heading | "EXERCISES" (unnumbered structural heading, source page 17) | x |
| F335 | 4.2.11 | opener | "Animals belonging to phylum Chordata are fundamentally characterised by the presence of a notochord, a dorsal hollow nerve cord and paired pharyngeal gill slits (Figure 4.16)." | x |
| F336 | 4.2.11.1 | opener | "All living members of the class Cyclostomata are ectoparasites on some fishes." | x |
| F337 | 4.2.11.2 | opener | "They are marine animals with streamlined body and have cartilaginous endoskeleton (Figure 4.19)." | x |
| F338 | 4.2.11.3 | opener | "It includes both marine and fresh water fishes with bony endoskeleton." | x |
| F339 | 4.2.11.4 | opener | "As the name indicates (Gr., Amphi : dual, bios, life), amphibians can live in aquatic as well as terrestrial habitats (Figure 4.21)." | x |
| F340 | 4.2.11.5 | opener | "The class name refers to their creeping or crawling mode of locomotion (Latin, repere or reptum, to creep or crawl)." | x |
| F341 | 4.2.11.6 | opener | "The characteristic features of Aves (birds) are the presence of feathers and most of them can fly except flightless birds (e.g., Ostrich)." | x |
| F342 | 4.2.11.7 | opener | "They are found in a variety of habitats – polar ice caps, deserts, mountains, forests, grasslands and dark caves." | x |
| F343 | 4.1.3 | caption | Figure labels: "Ectoderm"; "Mesoglea"; "Endoderm"; "Mesoderm" (Figure 4.2ab, harvested from the rendered asset) | x |
| F344 | 4.1.4 | caption | Figure labels: "Coelom"; "Pseudocoelom" (Figure 4.3abc, harvested from the rendered asset; panel (c) is unlabeled in the source) | x |
| F345 | 4.2 | caption | Figure labels: "Kingdom"; "Levels of Organisation"; "Symmetry"; "Body Cavity or Coelom"; "Phylum"; "Animalia (multicellular)"; "Cellular level"; "mostly asymmetrical"; "acoelomata"; "Porifera"; "Tissue/Organ/Organ system"; "Radial"; "Coelenterata (Cnidaria)"; "Ctenophora"; "Without body cavity (acoelomates)"; "Platyhelminthes"; "Bilateral"; "With false coelom (pseudocoelomates)"; "Aschelminthes"; "With true coelom (coelomates)"; "Annelida"; "Arthropoda"; "Mollusca"; "Echinodermata"; "Hemichordata"; "Chordata" (Figure 4.4, harvested from the rendered asset) | x |
| F346 | 4.2.5 | caption | Figure labels: "Male"; "Female" (Figure 4.10, harvested from the rendered asset) | x |
| F347 | 4.2.10 | caption | Figure labels: "Proboscis"; "Collar"; "Trunk" (Figure 4.15, harvested from the rendered asset) | x |
| F348 | 4.2.11 | caption | Figure labels: "Nerve cord"; "Notochord"; "Post-anal part"; "Gill slits" (Figure 4.16, harvested from the rendered asset) | x |
| F349 | 4.2.11 | caption | Figure labels: "Vertebrata"; "Division"; "Agnatha (lacks jaw)"; "Gnathostomata (bears jaw)"; "Super Class"; "Pisces (bear fins)"; "Tetrapoda (bear limbs)"; "Class"; "Cyclostomata"; "Chondrichthyes"; "Osteichthyes"; "Amphibia"; "Reptilia"; "Aves"; "Mammals" (Vertebrata chart, harvested from the rendered asset) | x |
| F350 | 4.2.1 | feature | "Porifera … have characteristic flagellated choanocytes." (folded from SUMMARY at 1-Z — body F041 names "Choanocytes or collar cells" but never states they are flagellated; only the "flagellated" qualifier is SUMMARY-UNIQUE) | x |
| F351 | 4.2.11.1 | feature | "They are the most primitive chordates …" (folded from SUMMARY at 1-Z — body F219/F336 state cyclostomes are ectoparasites on fishes but never that they are the most primitive chordates; the ectoparasite half is BODY-PRESENT, only "most primitive chordates" is SUMMARY-UNIQUE) | x |
| F352 | 4.2.11.5 | feature | "Limbs are absent in snakes." (folded from SUMMARY at 1-Z — body F273/F279 describe reptile dry/cornified skin and scale-shedding by snakes and lizards but never state that limbs are absent in snakes) | x |

## Summary classification

**Rule 3 two-pass check applied to every summary sentence (source pages 16–17).** 34 summary sentences; **3 carry a SUMMARY-UNIQUE fact** now folded into the body (F350–F352), the remaining fully **BODY-PRESENT**, **0 overlooked**. Every SUMMARY-UNIQUE line is a mandatory Gate 1 checklist item and a Pass-2 body addition.

| # | Summary sentence (verbatim) | Classification | Folded into |
|---|---|---|---|
| 1 | "The basic fundamental features such as level of organisation, symmetry, cell organisation, coelom, segmentation, notochord, etc., have enabled us to broadly classify the animal kingdom." | BODY-PRESENT | — (§4.1, F001-area) |
| 2 | "Besides the fundamental features, there are many other distinctive characters which are specific for each phyla or class." | BODY-PRESENT (transitional restatement) | — |
| 3 | "Porifera includes multicellular animals which exhibit cellular level of organisation and have characteristic flagellated choanocytes." | SPLIT — multicellular/cellular level BODY-PRESENT (F037); **"flagellated" choanocytes SUMMARY-UNIQUE** (F041 omits it) | **F350 (§4.2.1)** |
| 4 | "The coelenterates have tentacles and bear cnidoblasts." | BODY-PRESENT (§4.2.2) | — |
| 5 | "They are mostly aquatic, sessile or free-floating." | BODY-PRESENT (§4.2.2) | — |
| 6 | "The ctenophores are marine animals with comb plates." | BODY-PRESENT (§4.2.3) | — |
| 7 | "The platyhelminths have flat body and exhibit bilateral symmetry." | BODY-PRESENT (§4.2.4) | — |
| 8 | "The parasitic forms show distinct suckers and hooks." | BODY-PRESENT (§4.2.4) | — |
| 9 | "Aschelminthes are pseudocoelomates and include parasitic as well as non-parasitic roundworms." | BODY-PRESENT (§4.2.5) | — |
| 10 | "Annelids are metamerically segmented animals with a true coelom." | BODY-PRESENT (§4.2.6, F091) | — |
| 11 | "The arthropods are the most abundant group of animals characterised by the presence of jointed appendages." | BODY-PRESENT (§4.2.7) | — |
| 12 | "The molluscs have a soft body surrounded by an external calcareous shell." | BODY-PRESENT (§4.2.8, F123) | — |
| 13 | "The body is covered with external skeleton made of chitin." | BODY-PRESENT (§4.2.7 chitinous exoskeleton, F105) | — |
| 14 | "The echinoderms possess a spiny skin." | BODY-PRESENT (§4.2.9, F131 "Spiny bodied") | — |
| 15 | "Their most distinctive feature is the presence of water vascular system." | BODY-PRESENT (§4.2.9) | — |
| 16 | "The hemichordates are a small group of worm-like marine animals." | BODY-PRESENT (§4.2.10) | — |
| 17 | "They have a cylindrical body with proboscis, collar and trunk." | BODY-PRESENT (§4.2.10, F347 labels) | — |
| 18 | "Phylum Chordata includes animals which possess a notochord either throughout or during early embryonic life." | BODY-PRESENT (§4.2.11, F335) | — |
| 19 | "Other common features observed in the chordates are the dorsal, hollow nerve cord and paired pharyngeal gill slits." | BODY-PRESENT (§4.2.11, F335) | — |
| 20 | "Some of the vertebrates do not possess jaws (Agnatha) whereas most of them possess jaws (Gnathostomata)." | BODY-PRESENT (§4.2.11 Vertebrata chart, F349) | — |
| 21 | "Agnatha is represented by the class, Cyclostomata." | BODY-PRESENT (§4.2.11.1) | — |
| 22 | "They are the most primitive chordates and are ectoparasites on fishes." | SPLIT — ectoparasites BODY-PRESENT (F219/F336); **"most primitive chordates" SUMMARY-UNIQUE** | **F351 (§4.2.11.1)** |
| 23 | "Gnathostomata has two super classes, Pisces and Tetrapoda." | BODY-PRESENT (§4.2.11 chart, F349) | — |
| 24 | "Classes Chondrichthyes and Osteichthyes bear fins for locomotion and are grouped under Pisces." | BODY-PRESENT (§4.2.11 chart / §4.2.11.2–3) | — |
| 25 | "The Chondrichthyes are fishes with cartilaginous endoskeleton and are marine." | BODY-PRESENT (§4.2.11.2, F337) | — |
| 26 | "Classes, Amphibia, Reptilia, Aves and Mammalia have two pairs of limbs and are thus grouped under Tetrapoda." | BODY-PRESENT (§4.2.11 chart, F349) | — |
| 27 | "The amphibians have adapted to live both on land and water." | BODY-PRESENT (§4.2.11.4, F339) | — |
| 28 | "Reptiles are characterised by the presence of dry and cornified skin." | BODY-PRESENT (§4.2.11.5, F273) | — |
| 29 | "Limbs are absent in snakes." | **SUMMARY-UNIQUE** | **F352 (§4.2.11.5)** |
| 30 | "Fishes, amphibians and reptiles are poikilothermous (cold-blooded)." | BODY-PRESENT (F240 cartilaginous fishes, F252 bony fishes, F267 amphibians, F278 reptiles — all stated cold-blooded/poikilothermous) | — |
| 31 | "Aves are warm-blooded animals with feathers on their bodies and forelimbs modified into wings for flying." | BODY-PRESENT (§4.2.11.6, F292) | — |
| 32 | "Hind limbs are adapted for walking, swimming, perching or clasping." | BODY-PRESENT (§4.2.11.6) | — |
| 33 | "The unique features of mammals are the presence of mammary glands and hairs on the skin." | BODY-PRESENT (§4.2.11.7, F301/F303) | — |
| 34 | "They commonly exhibit viviparity." | BODY-PRESENT (§4.2.11.7, F310) | — |

## Exercise-gap terms

**Rule 2 classification applied to every exercise (source pages 17–18).** Arithmetic in words: **15 exercises, 13 COVERED (the body already answers), 2 GAP (a term the exercise assumes but the body never explains), 0 overlooked.** Each GAP names where the explanation must be added in Pass 2.

| Exercise | Classification | Answered by / GAP home |
|---|---|---|
| Q1 — difficulties in classification if common fundamental features are ignored | COVERED | §4.1 (classification rests on common fundamental features; Fig 4.4 caption) |
| Q2 — steps to classify a given specimen | COVERED | §4.1 + §4.1.1–4.1.6 (organisation, symmetry, coelom, segmentation, notochord criteria) |
| Q3 — usefulness of body cavity and coelom in classification | COVERED | §4.1.5 (coelom/pseudocoelom/acoelom) |
| Q4 — distinguish intracellular vs extracellular digestion | **GAP** | body uses both terms (F042 Porifera "intracellular"; F053 Coelenterata, F063 Ctenophora "extracellular and intracellular") but never **defines** the distinction — add a definition at §4.2.1/§4.2.2 or the Quick Recap |
| Q5 — difference between direct and indirect development | COVERED | body states indirect development (F270 Amphibia, F129 Mollusca) and direct development (F255 Osteichthyes, F282 Reptilia, F297 Aves, F310 Mammalia) |
| Q6 — peculiar features of parasitic platyhelminthes | COVERED | §4.2.4 (suckers, hooks, absorption of digested food) |
| Q7 — reasons arthropods are the largest group | COVERED | §4.2.7 (largest phylum; jointed appendages, wide adaptation) |
| Q8 — MCQ: water vascular system → (c) Echinodermata | COVERED | §4.2.9 (water vascular system) |
| Q9 — "all vertebrates are chordates but all chordates are not vertebrates" | COVERED | §4.2.11 (notochord/nerve cord/gill slits in all chordates; vertebral column defines Vertebrata) |
| Q10 — importance of air bladder in Pisces | COVERED | §4.2.11.3 (F250 air bladder regulates buoyancy) vs §4.2.11.2 (F237 its absence forces constant swimming) |
| Q11 — modifications in birds that help them fly | COVERED | §4.2.11.6 (feathers, forelimbs modified into wings, hollow/pneumatic bones) |
| Q12 — could eggs/young of an oviparous vs viviparous mother be equal? Why | **GAP** | body uses oviparous/viviparous throughout (F114, F129, F243, F255, F270, F282, F297, F310, F311) but never **defines** them — add definitions at §4.2 or the Quick Recap |
| Q13 — MCQ: segmentation first observed in → (c) Annelida | COVERED | §4.2.6 (F091 metameric segmentation; cf. F029 metamerism) |
| Q14 — match: operculum/parapodia/scales/comb plates/radula/hairs/choanocytes/gill slits | COVERED | operculum → §4.2.11.3 (F248); parapodia → §4.2.6 (F094); comb plates → §4.2.3; radula → §4.2.8 (F128); hairs → §4.2.11.7 (F303); choanocytes → §4.2.1 (F041); gill slits → §4.2.11 (F335/F348); scales → §4.2.11.2–5 |
| Q15 — list animals parasitic on human beings | COVERED | examples in body: Aschelminthes §4.2.5 (Ascaris, Wuchereria, Ancylostoma); Platyhelminthes §4.2.4 (tapeworm, liver fluke); Annelida §4.2.6 (Hirudinaria, leech) |

## Figure manifest

**Re-derived from scratch (2026-09-03, resumed 1-F)** by rendering every source page to an image and reading each caption verbatim from the source text layer, then comparing that ground truth against the actual pixels of every asset in `assets/`. Every caption below is the exact NCERT wording (letter-for-letter, including which species goes with which sub-letter) and every source page is the page the figure and its caption physically sit on — **not** copied from the previous (corrupted) version of this table. See carry-over #8's discharge note for what was wrong and how each row was checked against the rendered asset, not just the text.

| Fig # | Caption (verbatim) | Asset file | Source page | Mono | Verified |
|---|---|---|---|---|---|
| 4.1a | Radial symmetry | `fig_4_1a.png` | 2 | yes | yes — visually verified; complete radial-symmetry organism, no baked-in text labels |
| 4.1b | Bilateral symmetry | `fig_4_1b.png` | 2 | yes | yes — visually verified; complete crab, no baked-in text labels |
| 4.2ab | Showing germinal layers : (a) Diploblastic (b) Triploblastic | `fig_4_2ab.png` | 2 | yes | yes — CORRECTED: page was wrongly given as 3 (verbatim caption and its artwork sit on page 2, immediately after the Fig 4.1 pair); caption was a paraphrase ("Diploblastic and triploblastic organisation"), now verbatim. Artwork and in-figure labels Ectoderm/Mesoglea/Endoderm/Mesoderm complete |
| 4.3abc | Diagrammatic sectional view of : (a) Coelomate (b) Pseudocoelomate (c) Acoelomate | `fig_4_3abc.png` | 3 | yes | yes — CORRECTED: caption was a paraphrase ("Coelom, pseudocoelom and acoelom"), now verbatim; page (3) was already correct. In-figure labels "Coelom" (a) and "Pseudocoelom" (b) complete; (c) is unlabeled in the source |
| 4.4 | Broad classification of Kingdom Animalia based on common fundamental features | `fig_4_4.png` | 4 | yes | yes — CORRECTED: trailing "based on common fundamental features" was dropped from the caption, now restored verbatim. Full classification chart (Kingdom / Levels of Organisation / Symmetry / Body Cavity or Coelom / Phylum columns, all 11 phylum leaves) and text labels complete |
| 4.5abc | Examples of Porifera : (a) Sycon (b) Euspongia (c) Spongilla | `fig_4_5abc.png` | 4 | yes | yes — visually verified; plain rect `(60,426,290,681)`, all three panels complete, prose/caption excluded |
| 4.6ab | Examples of Coelenterata indicating outline of their body form : (a) Aurelia (Medusa) (b) Adamsia (Polyp) | `fig_4_6ab.png` | 5 | yes | yes — CORRECTED: prior caption "(a) Polyp and (b) medusa" both dropped the genus names and reversed the (a)/(b) order against the source (source is (a) Aurelia=Medusa, (b) Adamsia=Polyp); asset artwork itself was already correct, only the caption text was wrong |
| 4.7 | Diagrammatic view of Cnidoblast | `fig_4_7.png` | 5 | yes | yes — CORRECTED: caption was truncated to just "Cnidoblast"; artwork complete, no baked-in text labels |
| 4.8 | Example of Ctenophora (Pleurobrachia) | `fig_4_8.png` | 6 | yes | yes — CORRECTED: caption was truncated to just "Pleurobrachia"; upper tip retained, no baked-in text labels |
| 4.9ab | Examples of Platyhelminthes : (a) Tape worm (b) Liver fluke | `fig_4_9ab.png` | 6 | yes | yes — CORRECTED: caption gave the genus names "(a) Taenia and (b) Fasciola" instead of the verbatim common names; species themselves (and the artwork) were already right |
| 4.10 | Example of Aschelminthes : Roundworm | `fig_4_10.png` | 7 | yes | yes — CORRECTED: caption was a paraphrase ("Male and female Ascaris") naming a genus not in the verbatim source caption; artwork's own baked-in "Male"/"Female" in-figure labels are correct and retained |
| 4.11ab | Examples of Annelida : (a) Nereis (b) Hirudinaria | `fig_4_11ab.png` | 7 | yes | yes — already correct; visually verified, rect `(310,356,512,687)` with foreign "Roundworm" caption masked; artwork complete |
| 4.12abcd | Examples of Arthropoda : (a) Locust (b) Butterfly (c) Scorpion (d) Prawn | `fig_4_12abcd.png` | 8 | yes | yes — CORRECTED: prior caption "Different classes of Arthropoda" was not the verbatim source wording and omitted all four species; asset artwork (locust/butterfly/scorpion/prawn) was already correct |
| 4.13ab | Examples of Mollusca : (a) Pila (b) Octopus | `fig_4_13ab.png` | 8 | yes | yes — CORRECTED: prior caption listed the wrong species "(a) Unio and (b) Sepia"; asset artwork (apple snail / octopus) was already correct, only the caption text was wrong |
| 4.14ab | Examples of Echinodermata : (a) Asterias (b) Ophiura | `fig_4_14ab.png` | 9 | yes | yes — already correct; visually verified, both echinoderm specimens complete |
| 4.15 | Balanoglossus | `fig_4_15.png` | 9 | yes | yes — CORRECTED: source page is 9, not 10 (it sits directly under the Fig 4.14 pair, before the page break into §4.2.11); caption was a paraphrase of the in-figure labels ("Proboscis, collar and trunk of Balanoglossus") rather than the verbatim caption, which is just "Balanoglossus". In-figure labels Proboscis/Collar/Trunk complete |
| 4.16 | Chordata characteristics | `fig_4_16.png` | 10 | yes | yes — CORRECTED: prior caption "External features of a urochordate" was entirely wrong (this figure illustrates general Chordata features — nerve cord, notochord, post-anal part, gill slits — not a urochordate); page (10) was already correct. In-figure labels Nerve cord/Notochord/Post-anal part/Gill slits complete |
| 4.17 | Ascidia | `fig_4_17.png` | 10 | yes | yes — CORRECTED: source page is 10, not 11 (it sits on the same page as Fig 4.16, both above TABLE 4.1); caption itself was already correct. Artwork complete, asterisk retained |
| Vertebrata chart | The subphylum Vertebrata is further divided as follows: | `fig_vertebrata_chart.png` | 11 | yes | yes — real unnumbered figure; page (11) already correct; full chart and labels complete |
| 4.18 | A jawless vertebrate - Petromyzon | `fig_4_18.png` | 11 | yes | yes — CORRECTED: prior caption "Amphioxus" was the wrong species entirely — Amphioxus is the Cephalochordata example from running text (F209‑area), not this figure, which is the Cyclostomata example, Petromyzon. Source page is 11, not 12. Asset artwork was already correct |
| 4.19ab | Example of Cartilaginous fishes : (a) Scoliodon (b) Pristis | `fig_4_19ab.png` | 11 | yes | yes — CORRECTED: prior caption "(a) Petromyzon and (b) Myxine" belonged to Fig 4.18's class (Cyclostomata), not this figure (Chondrichthyes). Source page is 11, not 12. Asset artwork (dogfish/saw fish) was already correct |
| 4.20ab | Examples of Bony fishes : (a) Hippocampus (b) Catla | `fig_4_20ab.png` | 12 | yes | yes — CORRECTED: prior caption "(a) Scoliodon and (b) Pristis" belonged to Fig 4.19 (Chondrichthyes); page (12) was already correct. Asset artwork (sea horse/Catla) was already correct, rect `(54,96,255,336)`, prose excluded |
| 4.21ab | Examples of Amphibia : (a) Salamandra (b) Rana | `fig_4_21ab.png` | 12 | yes | yes — CORRECTED: prior caption "(a) Rohu and (b) Catla" belonged to Fig 4.20 (bony fishes); source page is 12, not 13. Asset artwork (salamander/frog) was already correct |
| 4.22abcd | Reptiles : (a) Chameleon (b) Crocodilus (c) Chelone (d) Naja | `fig_4_22abcd.png` | 13 | yes | yes — CORRECTED: prior caption "(a) Salamandra, (b) Rana, (c) Testudo and (d) Chameleon" mixed amphibian species (Salamandra, Rana from Fig 4.21) into the reptile figure and gave the wrong turtle genus; page (13) was already correct. Asset artwork (chameleon/crocodile/turtle/cobra) was already correct |
| 4.23abcd | Some birds : (a) Neophron (b) Struthio (c) Psittacula (d) Pavo | `fig_4_23abcd.png` | 14 | yes | yes — CORRECTED: prior caption "(a) Psittacula, (b) Pavo, (c) Columba and (d) Corvus" had the wrong species and wrong (a)–(d) order; page (14) was already correct. Asset artwork (vulture/ostrich/parrot/peacock) was already correct |
| 4.24abcd | Some mammals : (a) Ornithorhynchus (b) Macropus (c) Pteropus (d) Balaenoptera | `fig_4_24abcd.png` | 14 | yes | yes — CORRECTED: prior caption "(a) Oryctolagus, (b) Macaca, (c) Canis and (d) Panthera" listed the wrong species entirely (those are rabbit/monkey/dog/tiger — not in this figure); page (14) was already correct. Asset artwork (platypus/kangaroo/bat/whale) was already correct |

## Carry-over list

1. **The prior `Ch4_AnimalKingdom_inventory.md` is untrusted and archived** as `Ch4_prior_figure_notes_UNTRUSTED.md`. It contains no Facts/heading/opener/summary/exercise rows. Do not mine it for findings; re-derive at 1-F.
2. **The archived file claims the source PDF has "14 pages"; the machine says 18** (`doc.page_count == 18`, text extracted to `scratch/ch4_gate1/ch4_source.txt`). Every source-page number in that file is therefore suspect and must be re-pinned in 1-F.
3. `Ch4_figure_audit.md` and `extract_figures.py` in this folder are from the same untrusted arc, as was the old tracker — now archived as `Ch4_prior_TRACKER_UNTRUSTED.md` and replaced by a rewritten `Ch4_AnimalKingdom_TRACKER.md` that records Gate 1 as OPEN. `extract_figures.py` may be reused as a *starting point* for 1-F rectangles only after the 440 dpi / 5 pt gridline standard (§3) is applied and each rectangle re-inspected.
4. The archived file records one asset `fig_vertebrata_chart.png` as a "bonus un-numbered" chart. §3 step 1 item 4 says **unnumbered plates are real figures**, not bonuses — 1-F must census from page images and decide its status properly (it is the "The subphylum Vertebrata is further divided as follows:" chart on source page 11, i.e. 1b territory).
5. **[DISCHARGED by 1a-O]** Source page 5 extracts out of reading order: the §4.2.2 heading and its opening sentence sit at the *bottom* of the text stream while the continuation prose sits at the top. 1a-O took the §4.2.2 opener (F186, "They are aquatic, mostly marine, sessile or free-swimming, radially symmetrical animals…") from the layout, not the raw text order, so the correct opening sentence was captured.
6. **[DISCHARGED by 1b-H]** Source pages 11–15 render each class heading **five times** in the text layer (e.g. `4.2.11.1` × 5) — a faux-bold overprint, not five headings. 1b-H counted each of the seven class headings exactly once (F326–F332); no duplicate was taken.
7. **[DISCHARGED by 1b-S]** TABLE 4.2 (source page 15) extracts **column-major**: all "Level of Organisation" values, then all "Symmetry" values, etc., with the phylum names last. 1b-S reassembled it by column position into 11 per-phylum rows (F314–F324) and cross-checked every value against 1a's per-phylum prose (F035–F154); see the 1b-S census "Seam cross-check" note for the two places the source table is verbatim terser than its prose (Porifera "Various", Echinodermata "Radial") — preserved as source wording, not defects.
8. **[DISCHARGED by resumed 1-F, 2026-09-03]** The figure-label matrix did not exist in this inventory. Resumed 1-F harvested every genuinely labeled asset **by opening the rendered PNG**, not by text extraction, and added 7 `Type: caption` Facts rows beginning `Figure labels:` (F343–F349): Figure 4.2ab (Ectoderm/Mesoglea/Endoderm/Mesoderm), Figure 4.3abc (Coelom/Pseudocoelom), Figure 4.4 (the 26-term classification chart), Figure 4.10 (Male/Female), Figure 4.15 (Proboscis/Collar/Trunk), Figure 4.16 (Nerve cord/Notochord/Post-anal part/Gill slits), and the Vertebrata chart (Division/Agnatha/Gnathostomata/Super Class/Pisces/Tetrapoda/Class + the 7 class names). Every other asset (4.1a, 4.1b, 4.5abc, 4.6ab, 4.7, 4.8, 4.9ab, 4.11ab, 4.12abcd, 4.13ab, 4.14ab, 4.17, 4.18, 4.19ab, 4.20ab, 4.21ab, 4.22abcd, 4.23abcd, 4.24abcd) was opened and confirmed to carry **no** baked-in named label — only the bare `(a)`/`(b)`/`(c)`/`(d)` sub-panel letters, which are not label text — so no matrix row was taken for them; this is a finding, not an omission. `check_pdf.py._extract_labels` returns **6 fig-id groups / 56 individual label strings** across the 7 label-bearing rows F343–F349 (the parser keys on the Section column, so F348 + F349, both §4.2.11, collapse into one group — 6 groups for 7 rows; see carry-over #10), 0 doubled, no phantom `Fig #` row. *(Corrected at 1-Z: an earlier draft of this note stated "47 label strings / 7 labelled figures"; the machine-verified truth is 56 strings across 6 fig-id groups / 7 rows.)* Rows F001–F342 are unaffected; at the resumed-1-F point total Facts rows were 349 (F001–F349); the whole-chapter total after 1-Z's summary folds is 352 (F001–F352), all unticked (Pass 2 has not started).

9. **[DISCHARGED by resumed 1-F, 2026-09-03 — found while re-deriving carry-over #8]** Opening every rendered asset (per §3 Step 1) to build the label matrix surfaced that the **figure manifest itself, not just the label matrix, was corrupted** by the same untrusted prior process named in carry-over #1: **12 of the 26 rows had a wrong verbatim caption, and 6 of the 26 rows had a wrong source page**, even though **every asset's actual artwork was already correct**. Confirmed by rendering source pages 2, 3, 4, 9, 10, 11, 12 to images and comparing them pixel-for-pixel against the corresponding asset PNGs (not just re-reading the text layer):
   - **Species/wording swapped or invented** (caption text wrong, artwork correct): 4.6ab (was "(a) Polyp and (b) medusa", reversed and un-named — verbatim is "(a) Aurelia (Medusa) (b) Adamsia (Polyp)"), 4.7 and 4.8 (both truncated to a bare genus name instead of the verbatim "Diagrammatic view of Cnidoblast" / "Example of Ctenophora (Pleurobrachia)"), 4.9ab (genus names substituted for the verbatim common names), 4.10 (paraphrased instead of the verbatim "Roundworm"), 4.12abcd ("Different classes of Arthropoda" — not verbatim, species omitted), 4.13ab (wrong species: Unio/Sepia instead of Pila/Octopus), 4.15 (paraphrased from its own in-figure labels instead of the verbatim "Balanoglossus"), 4.16 ("External features of a urochordate" — completely wrong; it is "Chordata characteristics"), 4.18 ("Amphioxus" — wrong phylum-class entirely; verbatim is "A jawless vertebrate - Petromyzon"), 4.19ab (had 4.18's cyclostome species instead of its own cartilaginous-fish species), 4.20ab (had 4.19's cartilaginous-fish species instead of its own bony-fish species), 4.21ab (had 4.20's bony-fish species instead of its own amphibian species), 4.22abcd (had 4.21's amphibian species mixed in instead of its own reptile species), 4.23abcd and 4.24abcd (right topic, wrong species and/or wrong (a)–(d) order). The pattern reads as each figure's caption having been guessed/misremembered from the general topic rather than read off the source page — see carry-over #1's characterisation of the whole prior file as untrusted.
   - **Source page wrong** (caption fine or also wrong, but the page number did not match where the figure physically sits): 4.2ab (was 3, is 2), 4.15 (was 10, is 9), 4.17 (was 11, is 10), 4.18 (was 12, is 11), 4.19ab (was 12, is 11), 4.21ab (was 13, is 12).
   - Every correction above is entered directly in the "Figure manifest" table with a `CORRECTED:` note explaining what was wrong; nothing was silently changed. No asset file needed re-cropping — this was purely a captioning/paging defect in the documentation, not a defect in the extracted images.

10. **[COSMETIC — logged at 1-Z, does not block Gate 1]** `check_pdf.py._extract_labels` groups label rows by their **Section column** (`cells[1]`), not by figure number. F348 (Fig 4.16 "Chordata characteristics") and F349 (Vertebrata chart) both sit in **§4.2.11**, so the parser reports **6 fig-id groups for the 7 label-bearing rows** F343–F349. This is a reporting artifact of how the check keys figures — it is **not** a missing figure, a merged figure, or a dropped label (all 56 label strings are present and attributed to the correct row; 0 doubled, no phantom `Fig #` row). Any Pass-2 reader comparing "7 label rows" against the check's "6 figures" should expect this off-by-one and treat it as benign. If a future check revision keys on figure number instead of Section, the count becomes 7 with no change to the underlying rows.
