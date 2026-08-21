# Chapter Tracker — At a Glance

Chapter name and done / not done only, arranged unit-wise. A chapter counts as **Done** only when Gate 3 is genuinely closed (inventory frozen, `check_pdf.py` green, defects fixed, deliverables in place) per `SUPREME COMMAND PROMPT.md`.

For the evidence behind every Done, see `CHAPTER_STATUS.md`.

**Legend:** ✅ Done · ▶️ In progress · ⬜ Not done

**Progress: 11 / 32 chapters done** — Class 11: 6/19 · Class 12: 5/13

**Current work:** Class 12, Chapter 5 — **Molecular Basis of Inheritance** is **▶️ in progress: Pass 1a session `1a-S` complete, Gate 1 OPEN, Pass 2 not started.** It runs the **big-chapter 5-pass protocol** (31 source pages): 1a covers the intro + §5.1–§5.5, 1b covers §5.6–§5.10 + Summary + Exercises, with figures as one whole-chapter `1-F` and a single whole-chapter freeze `1-Z`. Session `1a-S` delivered the first-half prose inventory — **231 Facts rows, `F001..F231`, 0 gaps, 0 duplicates, every count re-derived by machine re-parse**, `Type` values normalized, and **0 heading / 0 opener rows by design** because those are the sole deliverables of `1a-H` and `1a-O`. `check_pdf.py`'s own `_extract_labels` returns 0 labels / 0 figures / **no phantom `Fig #` row** against the file. **Gate 1 closed is not chapter closed, and Gate 1 is not even closed here** — no script, no PDF, 0/231 rows ticked, so Ch5 is **not** counted in any Done tally below. Next session: `1a-H` — first-half headings only, target scoped from source at **17 heading lines on pp. 1–17** (16 in-body + chapter title).

**Ch5 detail layer:** `notes/class 12/Ch5_MolecularBasisOfInheritance/Ch5_TRACKER.md` — a per-chapter tracker holding the **9-session Pass-1 ledger** (1 done, 8 outstanding), the verified source map with the mid-page-17 seam, the copy-paste re-derivation commands behind every count here, per-session acceptance criteria, the `1-F` figure census (**16 figure numbers / 17 assets**, because `Figure 5.4` splits into `5.4a`/`5.4b`), and a corrections log. Where this roll-up and that tracker disagree about Ch5, the tracker is re-derived from disk and wins — and the correction must be written into both in the same session.

**Previously:** Class 12, Chapter 13 — Biodiversity and Conservation (the last chapter of the Ecology unit) is now **✅ Done — Gate 3 CLOSED**, which also **completes the entire Class 12 Ecology unit** (chapters 11, 12, 13). Pass 3(b) was run as a bidirectional full read: 13/13 source pages read start to finish against the named `# ---- 13.n ----` blocks, per-section reading claim recorded, and **no grep, coverage percentage or similarity score used to clear any row**. Direction 2 found **7 UNINVENTORIED defects — all one family**, NCERT's rhetorical questions and framing/opening sentences (the insect-diversification question; the two "inventory of our biological wealth" questions; the tropics framing sentence; "What exactly is stability…?"; "no direct answers to such naive questions"; the Evil Quartet's opening sentence; the ex-situ "beyond enclosures" sentence). All 7 were fixed and 7 rows added — `F035a`, `F048a`, `F065a`, `F085a`, `F092a`, `F112a`, `F171a` — logged loudly as a **real Pass 1 gap and never back-dated into the freeze**, taking the inventory from 189 to **196 rows**. 0 MISSING · 0 FABRICATED · 0 DRIFTED. The final artefact is an **11-page PDF (35,632 chars, 2 mono images)** with **196/196 rows ticked**, `check_pdf.py` exit 0 (0 fail, 1 inspected benign warn on "photo**synthesis**" in F143), **11/11 pages re-inspected after the reflow**, and a reproducible rebuild (two builds identical, same text SHA-256).

**Closure note — what the last session left open.** The 3(b) audit session ended before it could update the two tracker documents, so the inventory said "Gate 3 CLOSED" while both trackers still said "3(b) not started". Under Gate 3(b) rule 2 that disagreement **is itself the defect**, so the closure session re-derived every claim from the artefacts (fix presence and verbatim wording against the source, the `VERIFICATION FIX` audit trail, a machine re-parse giving 196/196 ticked, a fresh linter run, a byte-comparable rebuild, and an 11/11 visual re-inspection) **before** touching any status file, then reconciled all three in one operation per rule 8.

**Count-derivation note (Ch5 `1a-S` session):** the roll-up was **re-derived by counting the ✅ rows, not incremented** — `awk` over the unit tables returns 11 Done (Class 11: 6, Class 12: 5), matching both section footers, and Ch5's new **▶️** row is deliberately excluded because Gate 1 is still open there.

**Count-correction note (closure session):** the roll-up was **re-derived by counting the ✅ rows, not by incrementing** — `grep -c` returns 11 Done overall, Class 11 6/19 and Class 12 5/13, matching the section footers. The earlier note below records the same lesson from the previous drift.

**Count-correction note (2026-08-22):** this header previously read "9 / 32 · Class 12: 3/13" while the Class 12 section footer read "4 / 13". The footer was correct — Class 12 has four closed chapters (9, 10, 11, 12) — so Ch12's closure had been recorded in its own unit table and section total but never propagated to this header. Corrected at the time to 10 / 32, and now to **11 / 32** with Ch13 genuinely closed.

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
| 5. Molecular Basis of Inheritance | ▶️ In progress — Pass 1a session `1a-S` done; **Gate 1 OPEN**, Pass 2 not started |
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
| 13. Biodiversity and Conservation | ✅ Done |

**Class 12 total: 5 / 13 done** — Units IX and X are both complete
