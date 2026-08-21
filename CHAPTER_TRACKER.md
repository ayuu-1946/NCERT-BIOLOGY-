# Chapter Tracker — At a Glance

Chapter name and done / not done only, arranged unit-wise. A chapter counts as **Done** only when Gate 3 is genuinely closed (inventory frozen, `check_pdf.py` green, defects fixed, deliverables in place) per `SUPREME COMMAND PROMPT.md`.

For the evidence behind every Done, see `CHAPTER_STATUS.md`.

**Legend:** ✅ Done · ▶️ In progress · ⬜ Not done

**Progress: 10 / 32 chapters done** — Class 11: 6/19 · Class 12: 4/13

**Current work:** Class 12, Chapter 13 — Biodiversity and Conservation (the last chapter of the Ecology unit) is at **Gate 2 GREEN and Gate 3(a) CLOSED** (2026-08-22c). Pass 3(a) rendered all **11/11 pages** twice — 150 dpi for reading and 300 dpi converted to true 1-bit B&W for print safety — and opened every image: **zero confirmed defects**, no script edit, no rebuild. Both figures keep their native aspect ratio to four decimal places and are single-channel gray; a span census returns exactly one size per element class (H1 10.5pt · H2/table-head 9.5pt · H3 9.0pt · badge 6.0/6.21pt · step digit 8.0pt) and exactly six template greys, so nothing drifted across pages; NOTE and MEMORY AID stay distinguishable at 1-bit. Three flags were raised and all three dismissed as false positives (inherited section-badge numbers, p2's KeepTogether whitespace, a 2.3pt table-stroke overhang) and recorded in the inventory so a later session does not "fix" them. `check_pdf.py` was **re-run this session** and exits 0. **Pass 3(b) — the bidirectional full read — has not begun, so Gate 3 is OPEN and Ch13 is not Done.** The earlier gates stand as recorded below. Pass 1 remains as frozen: 2/2 figures clip-rendered and verified monochrome, 23 in-figure labels folded in as F039/F081, **189 facts frozen (F001-F189, contiguous, 0 gaps)**, 21 heading and 8 opener rows, 25 summary sentences classified, exercise-gap table written. Pass 2 built `Ch13_BiodiversityAndConservation.py` linearly from that inventory against the repo-level frozen `neet_template.py`, producing an **11-page PDF (34,117 chars, 2 mono images)**; every row was ticked while writing, all seven Pass 1 carry-overs were actioned, and `check_pdf.py` exits **0 — 0 fail, 1 warn**, that warn being check 4 matching "**photo**synthesis" in F143 rather than any real portrait row. **Pass 3 has not begun — no every-page render pass and no bidirectional full read — so Gate 3 is open and Ch13 is not yet Done.** Class 12 Chapter 12 — Ecosystem is **closed** (Gate 3 earned on its third full-read audit).

**Count-correction note (2026-08-22):** this header previously read "9 / 32 · Class 12: 3/13" while the Class 12 section footer read "4 / 13". The footer was correct — Class 12 has four closed chapters (9, 10, 11, 12) — so Ch12's closure had been recorded in its own unit table and section total but never propagated to this header. Corrected to 10 / 32. Ch13 is deliberately **not** counted: Gate 1 closed is not Gate 3 closed.

---

## Class 11

### Unit I — Diversity in the Living World

| Chapter | Status |
|---|---|
| 1. The Living World | ✅ Done |
| 2. Biological Classification | ✅ Done |
| 3. Plant Kingdom | ✅ Done |
| 4. Animal Kingdom | ⬜ Not done |

### Unit II — Structural Organisation in Plants and Animals

| Chapter | Status |
|---|---|
| 5. Morphology of Flowering Plants | ⬜ Not done |
| 6. Anatomy of Flowering Plants | ⬜ Not done |
| 7. Structural Organisation in Animals | ⬜ Not done |

### Unit III — Cell: Structure and Function

| Chapter | Status |
|---|---|
| 8. Cell: The Unit of Life | ✅ Done |
| 9. Biomolecules | ✅ Done |
| 10. Cell Cycle and Cell Division | ✅ Done |

### Unit IV — Plant Physiology

| Chapter | Status |
|---|---|
| 11. Photosynthesis in Higher Plants | ⬜ Not done |
| 12. Respiration in Plants | ⬜ Not done |
| 13. Plant Growth and Development | ⬜ Not done |

### Unit V — Human Physiology

| Chapter | Status |
|---|---|
| 14. Breathing and Exchange of Gases | ⬜ Not done |
| 15. Body Fluids and Circulation | ⬜ Not done |
| 16. Excretory Products and their Elimination | ⬜ Not done |
| 17. Locomotion and Movement | ⬜ Not done |
| 18. Neural Control and Coordination | ⬜ Not done |
| 19. Chemical Coordination and Integration | ⬜ Not done |

**Class 11 total: 6 / 19 done**

---

## Class 12

### Unit VI — Reproduction

| Chapter | Status |
|---|---|
| 1. Sexual Reproduction in Flowering Plants | ⬜ Not done |
| 2. Human Reproduction | ⬜ Not done |
| 3. Reproductive Health | ⬜ Not done |

### Unit VII — Genetics and Evolution

| Chapter | Status |
|---|---|
| 4. Principles of Inheritance and Variation | ⬜ Not done |
| 5. Molecular Basis of Inheritance | ⬜ Not done |
| 6. Evolution | ⬜ Not done |

### Unit VIII — Biology in Human Welfare

| Chapter | Status |
|---|---|
| 7. Human Health and Disease | ⬜ Not done |
| 8. Microbes in Human Welfare | ⬜ Not done |

### Unit IX — Biotechnology

| Chapter | Status |
|---|---|
| 9. Biotechnology: Principles and Processes | ✅ Done |
| 10. Biotechnology and its Applications | ✅ Done |

### Unit X — Ecology

| Chapter | Status |
|---|---|
| 11. Organisms and Populations | ✅ Done |
| 12. Ecosystem | ✅ Done |
| 13. Biodiversity and Conservation | ▶️ In progress — **Pass 2 complete, Gate 2 GREEN**: script + 11-page PDF built on the frozen template · 189/189 rows ticked · 23/23 figure labels in running text · `check_pdf.py` exit 0 (0 fail, 1 inspected benign warn). **Pass 3 not begun**, so **not Done** |

**Class 12 total: 4 / 13 done**
