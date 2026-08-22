# Chapter Tracker — At a Glance

Chapter name and done / not done only, arranged unit-wise. A chapter counts as **Done** only when Gate 3 is genuinely closed (inventory frozen, `check_pdf.py` green, defects fixed, deliverables in place) per `SUPREME COMMAND PROMPT.md`.

For the evidence behind every Done, see `CHAPTER_STATUS.md`.

**Legend:** ✅ Done · ▶️ In progress · ⬜ Not done

**Progress: 11 / 32 chapters done** — Class 11: 6/19 · Class 12: 5/13

**Current work:** Class 12, Chapter 5 — **Molecular Basis of Inheritance** is **▶️ in progress: PASS 1 COMPLETE, GATE 1 CLOSED, PASS 2 COMPLETE, GATE 2 CLOSED, Pass 3 under way (Gate 3a COMPLETE and its fixes landed; Gate 3b not started).** It runs the **big-chapter 5-pass protocol** (31 source pages): 1a covers the intro + §5.1–§5.5, 1b covers §5.6–§5.10 + Summary + Exercises, with figures as one whole-chapter `1-F` and a single whole-chapter freeze `1-Z`. All Pass 1 sessions delivered **646 frozen Facts rows, `F001..F646`, contiguous, 0 gaps, 0 duplicates, IDs monotonic, every count re-derived by machine re-parse** — including 136 figure-label rows — plus **18/18 verified mono assets** *(corrected this session: this paragraph previously read "17/17", a caption-derived census that omitted the unnumbered p4 central-dogma plate — exactly the §4.4 miscount. The Ch5 table row below always read 18/18; disk and the inventory both hold 18. The rows won, the count changed.)* Summary classification is 33 = 29 BODY-PRESENT + 4 SUMMARY-UNIQUE; the exercise-gap scan is **17 rows / 5 gaps**. `check_pdf.py`'s own `_extract_labels` returns **136 labels / 15 label-bearing figures / no doubling / no phantom `Fig #` row**. **Gate 2 is now CLOSED too:** the script and PDF exist and **all 646/646 rows are ticked**; `check_pdf.py --strict` returns **PASS, 0 fail / 0 warn** — re-derived independently in four separate sessions, so Gate 2 is treated as settled. The PDF is **30 pages** with **17 embedded mono images** (18 assets on disk; `fig_5_15` was removed from the PDF by owner decision and retained on disk). **Gate 2 closed is still not chapter closed** — Gate 3 is **OPEN**, but **Gate 3a's defect list is now fully dispositioned and both of its fixable items are FIXED** (this session). Owner decisions taken and executed: (1) **unnumbered NCERT sub-headings now take a letter suffix** — `heading("5.2", "Transforming Principle")` → **`5.2a`**, `heading("5.2", "Biochemical Characterisation…")` → **`5.2b`**, `heading("Goals", "Goals of HGP")` → **`5.9a`**. This was done **at the call sites only**, so the convention is an **authoring rule and `neet_template.py` was not touched**; `QR`/`EX` stay as intentional non-numeric mnemonic badges. (2) The prior handoff's "**21 literal `•` glyphs bypassing Check 5**" claim was **re-derived and found wrong**: a machine scan found **zero typed U+2022 literals** — all 21 come from ReportLab markup, 9 as proper hanging `<bullet>&bull;</bullet>` and **12 in Quick Recap as inline `&bull;` with no hanging indent**. The real defect was **markup inconsistency, not a banned glyph**, so `check_pdf.py` was correctly left unpatched and the **12 Quick Recap paragraphs were normalized to `<bullet>&bull;</bullet>`** (`Bullet1` already carries `firstLineIndent=-8`, so they now hang like every other bullet). The large `●` on p24 was checked and is **`keyterm()`, a different template component — not an inconsistent bullet**. (3) **Baked-in double borders** on `fig_5_4b`/`5_6`/`5_7`/`5_9` — **ACCEPTED and closed, same disposition as the watermark**: the frame is inside NCERT's own source artwork, and re-cropping 4 assets is real session cost for a cosmetic inherited artifact. **Do not re-raise it.** Post-fix `check_pdf.py --strict` re-run: **PASS, 0 fail / 0 warn**, 30 pages, 646/646 ticked, 136/136 labels, 17 mono images — all unchanged, so the fixes cost no regressions. Pages 6, 24 and 29 were re-rendered and re-inspected to confirm the three badges and all 12 bullets visually. Ch5 is still **not** counted in the Done tally. Next, and the **only** remaining work: **Gate 3b's bidirectional full read of all 646 rows against the NCERT source** — never yet run, and the only thing that can actually close Gate 3. *(Superseded text, kept as history: this paragraph previously read "no script, no PDF, 0/646 rows ticked ... Next: Pass 2a.")*

**Ch5 detail layer:** `notes/class 12/Ch5_MolecularBasisOfInheritance/Ch5_TRACKER.md` — a per-chapter tracker holding the **9-session Pass-1 ledger** (**all 9 entries complete; Gate 1 closed**), the verified source map with the mid-page-17 seam, the copy-paste re-derivation commands behind every count here, per-session acceptance criteria, the `1-F` figure census (**16 figure numbers / 17 numbered asset files** — because `Figure 5.4` splits into `5.4a`/`5.4b` — **plus the unnumbered p4 central-dogma plate = 18 assets total**), and a corrections log. *(Corrected this session: this read "16 figure numbers / 17 assets", which stated the numbered-file count as though it were the total and so dropped the unnumbered plate.)* Where this roll-up and that tracker disagree about Ch5, the tracker is re-derived from disk and wins — and the correction must be written into both in the same session.

**Ch5 stale-instruction audit (historical prior session — superseded by the Gate 1 closure above).** The venv was **absent again** at session start (the expected §0.2 state) and was rebuilt to identical versions before anything was diagnosed. Every current-state fact was then **re-derived by machine, not recalled, and all matched**: **510 rows `F001..F510`**, 0 gaps, 0 dups, monotonic, **0 ticked**; census sums to **510**; **30 heading / 27 opener / 0 figure-label** rows; the real `_extract_labels` imported from `check_pdf.py` returns **0 labels / 0 figures / no phantom `Fig #` row**; the exercise-gap table measures **17 data rows / 5 GAP rows** (the earlier 16→17 correction **confirmed, not reverted**); H1 still `# Working Inventory (NOT FROZEN)`; no `.py`, no `.pdf`, no `assets/`; Done tally re-counted at **11 ✅ rows**. **The defect fixed this session was stale *instructions*, not stale numbers** — the more dangerous kind, because numbers get re-derived while instructions get obeyed. `Ch5_TRACKER.md` **§4 was still headed "NEXT SESSION — `1a-H`"** and directed the next agent to append heading rows continuing from **`F231`**, an ID occupied since `1a-S` closed; following it would have collided with 279 existing rows and duplicated a completed sweep. §4 now carries the real **`1-F`** brief (17 assets / 16 figure numbers, labels from `F511`, acceptance criteria, and an explicit "Gate 1 stays OPEN when `1-F` closes"), while the whole `1a-H` scoping record — target table, four traps, criteria — is preserved **verbatim** in a new **§4a marked HISTORICAL / do not action**. Three adjacent stale claims were reconciled in the same pass: §5 still listed the completed `1a-O` as a forward note and described `1-Z` as wholly pending; §5's **"Gate 1 is judged only after `1b`"** implied the gate should now be closed; and the inventory's Facts-table scope note still read *"after session 1a-S: prose facts of the first half only"*, which would have licensed a future agent to believe heading and opener rows were still missing. All corrected, with the superseded text quoted rather than deleted. **No Facts row was touched, no history rewritten, no freeze run. Gate 1 OPEN · Pass 2 not started · Done tally unchanged at 11/32 · next session `1-F`.**

**Ch5 documentation-consistency note (prior session — no sweep run, no state advanced, Gate 1 still OPEN).** Every Ch5 claim in this roll-up, in `CHAPTER_STATUS.md` and in `Ch5_TRACKER.md` was re-derived from disk under the rebuilt `/vercel/share/neetenv`: **510 rows `F001..F510`**, contiguous, 0 gaps, 0 dups, IDs monotonic, **0 ticked**; `Type` census sums to **510**; **30 heading / 27 opener / 0 figure-label rows**; the **real** `_extract_labels`, imported from `check_pdf.py` rather than replicated, returns **0 labels / 0 figures / no phantom `Fig #` row**; inventory H1 still `# Working Inventory (NOT FROZEN)`; the chapter folder holds only the inventory and the tracker — no `.py`, no `.pdf`, no `assets/`; Done tally re-counted at **11 ✅ rows**. **One substantive inconsistency found and fixed, in five places** — the exercise-gap count read **"16 scanned items"** in the inventory (Gate 1 table, gap-section prose, session log) and the tracker (ledger row, machine-metrics row), but a machine parse of the table's own length returns **17 rows**: the old number was a hand-tally of *questions* reported as if it were *rows* (the 14 questions occupy 16 rows because `Q3`+`Q4` share one and `Q8`/`Q14` each split, and the in-body `F288`/`F289` pair is the 17th). All five now read **17 rows / 5 gaps** and state their basis. **`CHAPTER_STATUS.md` was the worst-drifted document** — both its overview row and its Ch5 section still described the `1a-S`-only state (231 rows, "0 heading / 0 opener by design", "next session `1a-H`") after six sweeps and three freeze steps had landed; both were rewritten. The previous session's two carry-overs are now closed: `_extract_labels` has been re-run under a real venv, and the session-count basis is stated in both trackers.

**Previously:** Class 12, Chapter 13 — Biodiversity and Conservation (the last chapter of the Ecology unit) is now **✅ Done — Gate 3 CLOSED**, which also **completes the entire Class 12 Ecology unit** (chapters 11, 12, 13). Pass 3(b) was run as a bidirectional full read: 13/13 source pages read start to finish against the named `# ---- 13.n ----` blocks, per-section reading claim recorded, and **no grep, coverage percentage or similarity score used to clear any row**. Direction 2 found **7 UNINVENTORIED defects — all one family**, NCERT's rhetorical questions and framing/opening sentences (the insect-diversification question; the two "inventory of our biological wealth" questions; the tropics framing sentence; "What exactly is stability…?"; "no direct answers to such naive questions"; the Evil Quartet's opening sentence; the ex-situ "beyond enclosures" sentence). All 7 were fixed and 7 rows added — `F035a`, `F048a`, `F065a`, `F085a`, `F092a`, `F112a`, `F171a` — logged loudly as a **real Pass 1 gap and never back-dated into the freeze**, taking the inventory from 189 to **196 rows**. 0 MISSING · 0 FABRICATED · 0 DRIFTED. The final artefact is an **11-page PDF (35,632 chars, 2 mono images)** with **196/196 rows ticked**, `check_pdf.py` exit 0 (0 fail, 1 inspected benign warn on "photo**synthesis**" in F143), **11/11 pages re-inspected after the reflow**, and a reproducible rebuild (two builds identical, same text SHA-256).

**Closure note — what the last session left open.** The 3(b) audit session ended before it could update the two tracker documents, so the inventory said "Gate 3 CLOSED" while both trackers still said "3(b) not started". Under Gate 3(b) rule 2 that disagreement **is itself the defect**, so the closure session re-derived every claim from the artefacts (fix presence and verbatim wording against the source, the `VERIFICATION FIX` audit trail, a machine re-parse giving 196/196 ticked, a fresh linter run, a byte-comparable rebuild, and an 11/11 visual re-inspection) **before** touching any status file, then reconciled all three in one operation per rule 8.

**Count-derivation note (re-confirmed at the latest Ch5 session):** the roll-up is **re-derived by counting the ✅ rows, never incremented** — `awk` over the unit tables returns 11 Done (Class 11: 6, Class 12: 5), matching both section footers, and Ch5's **▶️** row is deliberately excluded because Gate 1 closure is not chapter completion. Its 646 frozen inventory rows do **not** move this tally.

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
| 5. Molecular Basis of Inheritance | ▶️ **Gates 1 + 2 CLOSED, Gate 3 OPEN** — 646 frozen rows (`F001..F646`), **646/646 ticked**, 136 figure-label rows, **18/18 verified mono assets** (16 figure numbers; `5.4` splits a/b, plus the unnumbered p4 central-dogma plate); `check_pdf.py --strict` **PASS 0/0**; PDF 30 pp / 17 embedded images; **Gate 3a COMPLETE** — 30/30 pages + 18/18 assets inspected, defect list fully dispositioned: **badges FIXED** (`5.2a`/`5.2b`/`5.9a`, call sites only), **Quick Recap bullets FIXED** (12 inline `&bull;` normalized to hanging `<bullet>`; the "21 literal glyphs" claim was re-derived as false — 0 typed U+2022), watermark + baked-in double borders (`5.4b`/`5.6`/`5.7`/`5.9`) **ACCEPTED, do not re-raise**; strict re-run after fixes still **PASS 0/0**. **Gate 3b (bidirectional full read of 646 rows) NOT STARTED — the only work left** |
| 6. Evolution | ⬜ Not done |

### Unit VIII — Biology in Human Welfare

| Chapter | Status |
|---|---|
| 7. Human Health and Disease | ⬜ Not done |
| 8. Microbes in Human Welfare | ▶️ **`1-F` figure sweep COMPLETE — GATE 1 OPEN** — **9/9 verified mono assets** (`mode=L`, 300 dpi) covering **8 numbered figures**, 8.2 split into `8_2a` (panels a+b) + `8_2c`; no unnumbered plates, so the denominator is 9 · rects hand-pinned in `extract_figures.py`, each with a comment recording what pinned it · four-part crop gate passed (**A word-grazing · B drawings-extent · B2 raster-extent · C border ink**) — **B2 was added this chapter** because check B reports `no drawings` for the four photographic plates 8.4–8.7 and would have left them mechanically unchecked · check A is **vacuous for 5 of 9 assets** (0 words in rect; every callout is artwork, not text) · **2 rects re-pinned after the gate caught real clipping**: `fig_8_1` (`82,78,…`→`56,76,…`, flagellum sliced off panel c) and `fig_8_3` (`148,…`→`93,…`, petri dish a clipped) · 4 gate hits explained and accepted in writing (page-header motif, neighbouring 8.2c leader artwork, caption tint panels) · all 9 PNGs eyeballed on a fresh contact sheet · figure manifest + caption-verbatim check + figure-label matrix written. **NO Facts table, no `F###` row, no script, no PDF — `1-S`/`1-H`/`1-O`/`1-Z` all outstanding** |

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
