# NEET QUESTION-GENERATION PROMPT — "Defeat the Aspirant / 360 Mastery Set" (per chapter)

> **Purpose.** A reusable, self-contained prompt for generating **adversarial, multi-concept, cross-chapter** biology MCQs anchored to **one NCERT chapter** but licensed to pull in every linked NCERT idea. The design goal is blunt: **defeat the under-prepared aspirant.** A student who can genuinely solve *every* item this prompt produces, across every chapter, should be able to score **360/360** in NEET Biology. Calibrated against — and deliberately pitched *above* — the *NEET (UG)-2026, 03-05-2026, Code-11* Biology section (Q91-180).
>
> **This prompt is Gate 4 of the workflow in `SUPREME COMMAND PROMPT.md`, not a separate tool.** It inherits that document's doctrine wholesale: bounded passes, hard gates between them, and the founding rule that **a "PASS" verdict is a claim, not a fact** (Supreme, Gate 3(b) rule 1). Everything this prompt asks the model to *state* about its own output is re-derived by machine at `check_qbank.py` and compared against the claim. Where the two disagree, the claim is the defect.
>
> **How to use — do not copy this file by hand.** Run the builder, which enforces the gate precondition, supplies the frozen source text, and stamps the build:
>
> ```bash
> /vercel/share/neetenv/bin/python scripts/build_question_prompt.py --class 11 --chapter Ch4 --count 45
> ```
>
> It writes `scratch/question_prompts/<Chapter>_prompt.md` — this prompt with `11`, `Ch4_AnimalKingdom (Animal Kingdom)`, `45`, `AnimalKingdom@353+BodyFluidsAndCirculation@241,ExcretoryProductsAndTheirElimination@172,PlantKingdom@215`, `BodyFluidsAndCirculation, ExcretoryProductsAndTheirElimination, PlantKingdom` filled in and every usable Facts table appended. Paste that file. Nothing else to attach: the source text arrives with the prompt precisely so the model is never asked to recall NCERT.

---

## Q0. Where this sits, and what it is allowed to run on

### Q0.1 Gate 4 comes after Gate 3, never beside it

A question bank inherits the trustworthiness of the inventory it cites. An un-closed chapter's rows have not survived Pass 3's bidirectional read, so items built on them are *rigorous-looking claims resting on unverified text* — the exact failure the Supreme gates exist to prevent.

- **A chapter's QBank may only be generated once that chapter is `Done` (Gate 3 closed) in `CHAPTER_TRACKER.md`.** The builder reads the tracker and refuses otherwise.
- **A bridge chapter must also be `Done` for a cross-chapter link to be load-bearing.** Bridges that are open, missing from `notes/`, or lacking a Facts table are **withheld from the supplied text** and listed in the prompt as unavailable. A link into a withheld chapter is UNGROUNDED, no matter how well NCERT supports it.
- `--allow-open-gates` drafts from an open chapter for experimentation only. It stamps the prompt `PROVISIONAL` and `check_qbank.py` **FAILs Gate 4 by design** — a provisional bank can be read, but never recorded as closed.

### Q0.2 Interpreter (§0.2 of the Supreme prompt applies unchanged)

Run every command through the venv interpreter — `/vercel/share/neetenv/bin/python` — never bare `python3`. The two-interpreter trap cost four failed attempts in the Ch12 session and it does not care that the current task is questions rather than PDFs. `check_qbank.py` itself is **stdlib-only**, so a red Q-Gate can never be a missing-library artifact; the venv is still the rule so one command form works everywhere.

### Q0.3 Deliverables (extends Supreme §0.5)

Two files per chapter, in the chapter folder beside the PDF, script, inventory and `assets/`:

```
notes/class 11/Ch4_AnimalKingdom/
  Ch4_AnimalKingdom_QBANK.md          <- run header + SECTION A + SECTION B
  Ch4_AnimalKingdom_QBANK_ledger.md   <- machine-derived counts + Gate 4 verdict + human adjudication
```

The ledger is **written by the machine, not by hand**: `check_qbank.py <folder> --emit-ledger` derives every count from the bank itself and records the verdict per check. `CHAPTER_TRACKER.md`'s "Gate 4 — Question Banks" table is updated in the *same* edit that closes the ledger (Supreme, Gate 3(b) rule 8: close the loop atomically).

---

## PROMPT BODY

### Role
You are a **ruthless senior NEET Biology paper-setter and destroyer of ranks** with 15+ years of national item-writing experience. Your items are **factually airtight, NCERT-faithful, and psychometrically clean**, but their explicit purpose is to *separate the student who memorized the book from the student who actually understands it*. You never invent biology that contradicts current NCERT — your cruelty comes from **integration and reasoning depth, never from going out of syllabus**.

### Objective
Generate **45 original multiple-choice questions** anchored to **Class 11, Chapter: Ch4_AnimalKingdom (Animal Kingdom)**. Every item must be **at NEET difficulty or harder — the center of gravity is *harder***. The set must be built so that a student who masters all of it has no exploitable weakness left in this chapter or its connections to the rest of the syllabus. Items are original (never copied verbatim) but exceed the reference exam in cognitive demand.

Build stamp for this run: `AnimalKingdom@353+BodyFluidsAndCirculation@241,ExcretoryProductsAndTheirElimination@172,PlantKingdom@215`. Bridge chapters supplied: `BodyFluidsAndCirculation, ExcretoryProductsAndTheirElimination, PlantKingdom`. Echo the stamp verbatim in your run header — it is how the gate later proves the bank was generated from the source text that is on disk *now* rather than from a stale copy.

### The "360" mandate — what "harder" actually means
Difficulty here does **not** come from obscure trivia. It comes from four legitimate, NCERT-bounded levers. Use them relentlessly:

1. **Multi-concept fusion.** A single item must force the student to hold and combine **2-4 distinct NCERT facts** to reach the answer. No item should be solvable by recalling one sentence. This is machine-enforced: a Tier-2/3 item citing fewer than two frozen fact IDs is a FAIL.
2. **Cross-chapter reasoning.** The chapter is the *anchor*, not a fence. Deliberately link it to the supplied bridge chapters — e.g. Animal Kingdom `<->` Body Fluids/Circulation (heart chambers), `<->` Breathing (respiratory surfaces), `<->` Evolution (phylogeny); Photosynthesis `<->` Respiration (energetics); Genetics `<->` Molecular Basis `<->` Biotechnology. At least the Tier-2 and Tier-3 items should reach beyond the anchor chapter.
3. **Extra reasoning steps.** Chain inferences: "if X is true, then which of Y follows" — require 2-3 logical hops, elimination under a negative stem, or resolving a contradiction between statements.
4. **Discrimination under pressure.** Distractors must be things a 320-scorer would actually pick. The item should punish shallow pattern-matching and reward true conceptual command.

If an item can be answered by a single recalled line, it is **too easy — rewrite or discard it.**

### Absolute scope rule (non-negotiable)
- Every fact, number, name, sequence, and relationship tested **must be verifiable in the SUPPLIED source text below**. Cross-chapter is encouraged; **out-of-NCERT is forbidden** — not in the stem, key, or the presumed truth-value of any distractor.
- You may test *inference, integration, and synthesis across the supplied chapters*, but never *content outside them* (no research trivia, no coaching-only mnemonics presented as fact, no exceptions the book does not state).
- When in doubt about a fact, drop the item rather than guess. A hard item built on a shaky fact is a defect, not a challenge.

### Source-grounding mandate (READ THIS FIRST — highest reliability lever)
- The **SUPPLIED NCERT SOURCE TEXT** section at the end of this prompt is the anchor chapter's frozen inventory plus the Facts tables of every gate-closed bridge chapter. **You may only use facts you can trace to a row in those tables.** Do not rely on your own memory of NCERT — memory is the #1 cause of out-of-syllabus drift and wrong answer keys.
- If a fact you want has **not** been supplied, you have two choices: (a) do not use it, or (b) name it in the run header's `UNGROUNDED:` line and omit the item. Never silently trust recall.
- **Citation is by row ID, not by quotation.** Every item's `Meta:` line lists the exact frozen rows it fuses:
  - anchor-chapter rows are cited bare: `F012`
  - bridge-chapter rows carry their chapter key: `BodyFluidsAndCirculation:F031`
- This is the single most important change from a prose-quote citation: `check_qbank.py` resolves **every ID you write** against the real inventory files. An ID that does not exist is a hard FAIL, so an invented citation cannot pass as a plausible-looking quote. Quoting prose proves nothing a machine can check; citing `F012` proves everything.
- An item whose fused facts cannot all be cited to supplied rows is a **defect — remove it.** Grounding beats cleverness.

### Difficulty calibration — three tiers (reweighted for adversarial intent)
Distribute the 45 items. **Default mix: 20% Tier-1, 45% Tier-2, 35% Tier-3** (the gate allows +/- 10 percentage points per tier and WARNs outside that band). The mass sits in the hard bands on purpose.

- **Tier 1 — NEET-standard floor (20%).** Clean single-concept anchor items. Present only to guarantee full syllabus coverage of core facts a 360 requires — never the bulk of the set. Minimum 1 cited fact ID.
- **Tier 2 — NEET-hard / multi-concept (45%).** Requires fusing 2-3 NCERT facts, a careful negative stem, or eliminating close confusables. Frequently pulls one link from a bridge chapter. This is the modern NEET discriminator band. Minimum 2 cited fact IDs.
- **Tier 3 — Above NEET / integrative destroyer (35%).** Multi-step reasoning, cross-chapter synthesis, calculation, or data/scenario interpretation combining several NCERT ideas. Still 100% NCERT-derivable, but engineered to break students who only memorized. This tier is the point of the set. Minimum 2 cited fact IDs; aim for 3-4.

Never sacrifice correctness to reach a tier. A wrong Tier-3 item is worse than a clean Tier-1 item. **Never inflate a tier tag to hit the mix, either** — the tag is checked against the citation count, so a "Tier 3" resting on one fact fails rather than flatters.

### Question archetypes with target quotas
Produce a spread across ALL of the following. The **tag in square brackets is a controlled vocabulary** — write exactly these eight strings, because the gate groups on them. Suggested proportions for 45=45 in parentheses; scale proportionally. Bias every archetype toward the multi-concept/cross-chapter version wherever the content allows.

| Tag | Archetype | ~45-item quota | Notes |
|---|---|---|---|
| `single` | Single-correct factual/conceptual | 8 | Prefer stems that still require combining two facts over pure recall. |
| `match` | Match List-I with List-II | 8 | Two lists of 4 (A-D vs I-IV), four full-pairing options. Make at least half **cross-chapter**. 5x5 lists raise load. |
| `count` | Multi-statement "how many are correct" | 9 | 4-5 labelled statements (A-E) from *different* sections/chapters. Prefer "how many" over "which combination" — it removes elimination shortcuts. |
| `sequence` | Arrange-in-order | 5 | 4-5 steps out of order (pathways, life cycles, techniques, cascades, hierarchy). |
| `assertion-reason` | Assertion-Reason | 5 | Standard four NCERT-style options. Tests *causation*, not facts. Make A and R come from linked concepts. |
| `negative` | Negative stem | 3 | "Which is **not** true / **incorrect** / **wrongly matched**." **Bold the negative word** — the gate WARNs if it is unbolded. |
| `numerical` | Numerical / quantitative | 4 | Genetic probability, RQ, ATP-NADPH stoichiometry, differential counts, ploidy, growth equations, Hardy-Weinberg. Numbers must be NCERT-anchored. |
| `scenario` | Scenario / data interpretation | 3 | A vignette ending in identify/classify/predict, ideally spanning two chapters. |

If the chapter cannot support an archetype, redistribute the quota to supported ones and **name the substitution in the run header's `Substitutions:` line** — an absent archetype is a WARN, and the header line is what turns it into an accounted-for decision instead of a silent gap.

### Cross-chapter linking — required discipline
- For every Tier-2 and Tier-3 item, identify the **anchor concept (from Ch4_AnimalKingdom (Animal Kingdom))** and the **linked concept(s)** it fuses with. Declare the link in the item tag's `Links:` field *and* cite at least one bridge row ID in `Meta: facts=[...]`.
- **A link is load-bearing only if it cites a fact from the linked chapter.** Declaring `Links: Evolution` while citing no `Evolution:F###` row is a **decorative link and a hard FAIL** — this is the check that makes "at least 50% cross-chapter" a measured property instead of a self-graded one.
- **At least 50% of Tier-2 + Tier-3 items must be genuinely cross-chapter** (gate floor, FAIL below).
- Legitimate links only: the connection must be one NCERT itself supports (shared structure, shared pathway, evolutionary relationship, cause-effect, exception-to-a-rule) **and** appear in the APPENDIX registry for this anchor. Off-registry links FAIL. Do not force artificial links.

### Distractor (wrong-option) construction rules
Distractors are where the defeat happens. For every item:
- All four options must be **grammatically parallel, similar in length, and genuinely tempting** to a well-prepared-but-not-expert student.
- Build distractors from **real NCERT confusables**: the sibling term, the adjacent step, the reciprocal relationship, the commonly-swapped pair (GPP vs NPP, promoter vs terminator, autogamy vs geitonogamy vs xenogamy, Chondrichthyes vs Osteichthyes, incomplete vs codominance).
- Exactly **one** option is defensibly correct. No "two-could-be-right" items. Every distractor must be *defensibly wrong* with a citable reason. **Two options with identical text is a FAIL** (it makes the item multi-correct by construction).
- Kill giveaway cues: don't make the key the longest/most-qualified option, don't echo a stem keyword only in the key, randomize key positions.
- **Key positions are gated:** no option number may hold more than 35% or fewer than 15% of the keys. Balance as you write; do not leave it to the audit.
- For match/sequence/count items, ensure no single trivial elimination reveals the key; each distractor should differ from the key in a way that traps a specific misconception.

### Output format (strict — the gate parses this exactly)
Emit the run header, then two clearly separated sections. No preamble, no commentary.

**SECTION A — QUESTION PAPER (no answers).** Number items continuously from 1. For each:
```
Q<n>. [Tier <1|2|3>] [<archetype tag>] [Anchor: <topic> | Links: <ChapterKey(s) or -->]
<stem>
  (1) <option>
  (2) <option>
  (3) <option>
  (4) <option>
```
For `match` items, render both lists as a two-column table before the options. Use LaTeX in double dollar signs for any equation (e.g. $$dN/dt = rN\left(\frac{K-N}{K}\right)$$).

**SECTION B — ANSWER KEY & EXPLANATIONS.** For each item:
```
Q<n>. Correct: (<x>)
Meta: tier=<1|2|3> | archetype=<tag> | facts=[F012, F045, BodyFluidsAndCirculation:F031] | trap=<sibling-term|adjacent-step|reciprocal|swapped-pair|false-cause|scope-overreach|...>
Reasoning chain: <the 2-4 step path from the cited rows to the answer>
Why others fail: (1) ... (2) ... (3) ... (4) ...
Trap targeted: <the specific misconception this item punishes>
```
The `Meta:` line is the machine-auditable spine of the whole bank — tier, archetype, grounding, cross-chapter status and duplication are all derived from it. An item without a parseable `Meta:` line is treated as ungrounded and FAILs.

### Glyph discipline
Write ASCII: `->` for arrows, `<->` for bidirectional links, spelled-out Greek (`alpha`, `beta`), and plain digits instead of Unicode sub/superscripts. Unicode arrows, Greek letters and sub/superscript characters are banned exactly as they are in `check_pdf.py` check 5, because a bank may later be rendered through the same PDF pipeline.

### Q-Pass 1 — generate, then Q-Pass 2 — attack your own paper (both silent)
Do not emit anything until both passes are done.

**Q-Pass 2 — self-adversarial solve.** After drafting all items, *become a 340-scorer attacking your own paper.* For every item, actively try to break it, and **rewrite or discard** any item that fails ANY of these:
- **One-line-solvable:** answerable by recalling a single sentence (except the deliberate Tier-1 floor). -> make it fuse more, or demote its tier honestly.
- **Ambiguous / multi-correct:** more than one option is defensible, or the "correct" one is arguably wrong. -> fix the options or cut.
- **Ungrounded or decorative link:** the cross-chapter connection cites no bridge row, or the row cited does not actually support the claim. -> replace with a real fused link or drop the cross-chapter claim (and its `Links:` field).
- **Backsolvable trick:** the key is guessable from length, grammar, position, or a stem echo without any biology. -> rewrite options.
Report the counts in the header (`Pass-Q2 fixes: __ rewritten / __ discarded`). If Q-Pass 2 changes the tier or archetype counts, re-balance before output.

### Q-Pass 3 — self-audit, then hand to the machine
Do all of this silently, then emit only the header and the two sections:

1. **Fact check:** re-derive each key from the cited rows; confirm every distractor is genuinely wrong and every fused fact is a real supplied row ID.
2. **Single-answer check:** no item has zero or multiple correct options; no two options share text.
3. **Difficulty check:** the tier mix holds and **no item is solvable by a single recalled line** except the deliberate Tier-1 floor.
4. **Integration check:** >= 50% of Tier-2/Tier-3 items cite a bridge row, and each declared `Links:` chapter has a cited row.
5. **Archetype spread check:** all supported archetype tags appear near quota, spelled from the controlled vocabulary.
6. **Coverage check:** cited anchor rows span the chapter's major sections (>= 80% of Section values in the frozen inventory; a 360 needs total coverage, not a hot topic).
7. **Answer-distribution check:** keys within the 15-35% band per option.
8. **Duplication check:** no two items cite the identical fact-set. Merge or replace near-duplicates.
9. **Header-honesty check:** every number in the run header is one you actually counted from your own items. **This is the one the machine checks hardest** — the gate re-derives all of them and FAILs on any disagreement, so a rounded or remembered figure is worse than useless.

**Then the header is verified, not trusted.** The operator runs:

```bash
/vercel/share/neetenv/bin/python check_qbank.py "notes/class 11/<ChapterDir>" --emit-ledger
```

which runs nine checks (exit 0 clean / 1 FAIL / 2 setup error; `--strict` treats WARN as failure, `--json` for a machine report):

| # | Check | Fails when |
|---|---|---|
| Q1 | Provenance & Gate-4 precondition | anchor not `Done`; bridge not `Done`; off-registry or non-existent chapter cited; stamp missing, PROVISIONAL, or STALE against current inventories |
| Q2 | Structure & item/key correspondence | items not contiguous from 1; header `Items:` disagrees; an item without a key or a key without an item |
| Q3 | Options | not exactly four options `(1)-(4)`; duplicate option text; key outside the emitted options |
| Q4 | Key distribution | derived counts disagree with the header, or any option outside the 15-35% band |
| Q5 | Tier mix | derived mix disagrees with the header (FAIL); outside the +/- 10pp band (WARN) |
| Q6 | Fact grounding | missing `Meta: facts=[...]`; a cited ID absent from the frozen inventory; a Tier-2/3 item citing one fact |
| Q7 | Cross-chapter load-bearing | header cross-count disagrees; a declared `Links:` chapter with no cited row; under the 50% floor |
| Q8 | Duplication & coverage | two items cite the identical fact-set (FAIL); anchor sections touched under 80% (WARN) |
| Q9 | Archetype spread, glyphs, style | unrecognised archetype tag; header archetype counts disagree; banned Unicode glyph; unbolded negative stem (WARN) |

**Gate 4 closes only when all three hold** — mirroring Gate 3's structure, because a green linter and a correct bank are different things:
1. `check_qbank.py` exits 0 against the bank **as saved on disk** — never a verdict carried forward from an earlier draft.
2. A **stated human adjudication** in the ledger: which items were read against which frozen rows, which flags were investigated and dismissed (kept, with reasoning), and every accepted WARN justified. No derived percentage substitutes for this.
3. The ledger and `CHAPTER_TRACKER.md`'s Gate 4 table are updated in the **same edit**.

### Run header to emit first (exact format — the gate parses these lines)
```
QBANK HEADER
Anchor: class 11 / <ChapterDir>
Prompt-build: AnimalKingdom@353+BodyFluidsAndCirculation@241,ExcretoryProductsAndTheirElimination@172,PlantKingdom@215
Items: 45 | Tier mix T1/T2/T3 = __/__/__
Archetypes: single=__ | match=__ | count=__ | sequence=__ | assertion-reason=__ | negative=__ | numerical=__ | scenario=__
Cross-chapter: __/__ | Bridges used: <ChapterKey, ...>
Key distribution: (1)=__ (2)=__ (3)=__ (4)=__
Pass-Q2 fixes: __ rewritten / __ discarded
UNGROUNDED: <facts I could not pin to a supplied row, omitted — or "none">
Substitutions: <archetype redistributions — or "none">
```
`Cross-chapter` is stated as *cross-chapter Tier-2+3 items / total Tier-2+3 items* — not out of `45`, since Tier-1 is not expected to reach beyond the anchor.

---

## MAINTAINER NOTES (not part of the prompt to the model)

- **Design intent:** this is the "defeat the aspirant" upgrade of the original NEET set. Difficulty is bought with *integration and reasoning*, never with out-of-syllabus trivia. If output starts leaking non-NCERT content to seem hard, tighten the scope rule — do not relax it.
- **The 360 claim is a coverage + depth contract:** mastering every item across every chapter should leave no exploitable gap. That requires both the Tier-1 floor (total factual coverage) and the Tier-2/3 mass (integration). Do not drop the Tier-1 floor to look harder — full marks needs the easy facts locked too.
- **Why fact IDs replaced source quotes.** The original prompt asked for a `Source lines:` quote per fused fact. It reads convincingly and audits to nothing: a paraphrase cannot be mechanically matched to a row, so a hallucinated fact and a real one look identical on the page. Row IDs are resolvable, which is why Q6 can be a hard gate at all. This mirrors the Supreme prompt's move from "every label must appear in text" to a per-label inventory row that `check_pdf.py` check 6 audits.
- **The registry lives in exactly one place — the APPENDIX table below.** `check_qbank.py:parse_registry()` reads it and `scripts/build_question_prompt.py` imports that parser; neither keeps a hardcoded copy. This is Supreme step-10's rule ("a count is never *fixed* in only one place") applied to the bridge list, and it is why the old `BRIDGE_GROUPS` constant was deleted rather than kept in sync.
- **Reference calibration set:** `user_read_only_context/text_attachments/NEET_2026_May3_Biology_QuestionsOnly-*.pdf` (Q91-180). Generated items should feel *harder* than these, not merely equal.
- **Per-chapter batching:** run once per chapter, over the chapters that are `Done`. `--list-bridges` shows which bridges a given anchor can currently use and why the others are withheld — useful for deciding which chapter to close next in order to unlock a rich bridge set.
- **Recommended default count:** 45/chapter; raise to 60-90 for heavily-weighted chapters (Genetics, Human Physiology, Ecology, Biotechnology, Cell/Biomolecules).
- **Most common failure modes, and what now catches each:** (1) a "hard" item that quietly leaves NCERT -> Q6 unknown-ID FAIL; (2) a plausible distractor that is actually true -> human adjudication only, still the irreducible judgment call; (3) a fake cross-chapter link -> Q7 decorative-link FAIL; (4) drifting the tier mix easy -> Q5 band + Q6 per-tier citation minimum; (5) a run header that flatters the bank -> every derived-vs-claimed comparison.
- **When a bank goes stale.** The stamp fingerprints each supplied inventory's row count. If a chapter's inventory is later corrected (Supreme's Gate 1 rule 5 permits metadata corrections, and Ch4 gained `F015a` at Gate 3(b)), the recomputed stamp differs and Q1 reports STALE. Regenerate the prompt and re-run rather than patching the bank — the bank was grounded in text that no longer exists.

---

## APPENDIX — CROSS-CHAPTER LINK REGISTRY (machine-parsed; single source of truth)

A curated list of **legitimate, high-yield NCERT bridges** so "cross-chapter" stays real and repeatable instead of improvised each run. All bridges are stated or directly implied by NCERT itself.

**This table is parsed, not just read.** `check_qbank.py:parse_registry()` reads each row's *Chapter keys* column and takes only the backticked tokens, so prose in the basis column can never leak a phantom chapter into the registry. Keys are the canonical folder suffixes under `notes/class N/Ch<n>_<Key>` — a key that does not resolve to a real folder is reported as an unavailable bridge, never silently dropped.

To add a bridge: add a row here with its NCERT basis. Nothing else needs editing anywhere.

| Bridge | Class | Chapter keys | NCERT basis for the bridge |
|---|---|---|---|
| B01 | 11 | `AnimalKingdom` + `BodyFluidsAndCirculation` + `BreathingAndExchangeOfGases` + `ExcretoryProductsAndTheirElimination` | Heart-chamber count as a classification character; respiratory surfaces (gills/lungs/skin/trachea); ammonotelic vs ureotelic vs uricotelic against habitat. |
| B02 | 11 | `AnimalKingdom` + `Evolution` | Phylogeny, coelom, symmetry and common ancestry as the basis of the classification hierarchy. |
| B03 | 11 | `StructuralOrganisationInAnimals` + `BreathingAndExchangeOfGases` + `BodyFluidsAndCirculation` | Epithelial and connective tissue types lining the organs those chapters describe. |
| B04 | 11 | `Biomolecules` + `CellTheUnitOfLife` | Macromolecule classes and enzyme cofactors located in the organelles that house them. |
| B05 | 11 | `Biomolecules` + `RespirationInPlants` + `PhotosynthesisInHigherPlants` | Glycolytic substrates and Calvin-cycle substrates as the same biomolecule classes; enzyme classes driving both. |
| B06 | 11 | `RespirationInPlants` + `PhotosynthesisInHigherPlants` | Energetics: ATP/NADPH yield, RQ, and the reciprocal gas exchange of the two pathways. |
| B07 | 11 | `PlantKingdom` + `MorphologyOfFloweringPlants` + `AnatomyOfFloweringPlants` | Life-cycle and ploidy alternation expressed in the organs and tissues of the flowering plant body. |
| B08 | 11 | `PlantKingdom` + `SexualReproductionInFloweringPlants` | Haplontic/diplontic/haplo-diplontic alternation carried into the angiosperm life cycle. |
| B09 | 11 | `CellCycleAndCellDivision` + `SexualReproductionInFloweringPlants` | Where meiosis sits in a life cycle; double-fertilisation ploidy arithmetic. |
| B10 | 11 | `CellCycleAndCellDivision` + `MolecularBasisOfInheritance` | Chromosome behaviour underlying linkage, recombination and DNA replication timing. |
| B11 | 11 | `ChemicalCoordinationAndIntegration` + `NeuralControlAndCoordination` | Neural vs hormonal control of the same effector; hypothalamic-pituitary axis. |
| B12 | 11 | `ChemicalCoordinationAndIntegration` + `ExcretoryProductsAndTheirElimination` + `BodyFluidsAndCirculation` | ADH, aldosterone, ANF: hormonal regulation of urine formation and blood pressure. |
| B13 | 11 | `BreathingAndExchangeOfGases` + `BodyFluidsAndCirculation` | Oxygen and carbon-dioxide transport by blood; the dissociation curve. |
| B14 | 12 | `PrinciplesOfInheritanceAndVariation` + `MolecularBasisOfInheritance` | Gene -> mutation -> phenotype; the molecular identity of a Mendelian factor. |
| B15 | 12 | `PrinciplesOfInheritanceAndVariation` + `Evolution` | Allele frequency, Hardy-Weinberg equilibrium and its disturbing forces. |
| B16 | 12 | `MolecularBasisOfInheritance` + `BiotechnologyPrinciplesAndProcesses` | Restriction sites, vectors, plasmids and PCR as applied nucleic-acid chemistry. |
| B17 | 12 | `MolecularBasisOfInheritance` + `Evolution` | Molecular clock, homologous sequence and common ancestry. |
| B18 | 12 | `HumanReproduction` + `ReproductiveHealth` | Contraceptive mode of action against the reproductive events they interrupt. |
| B19 | 12 | `HumanReproduction` + `ChemicalCoordinationAndIntegration` | Gonadotropins and the hormonal control of gametogenesis and the menstrual cycle. |
| B20 | 12 | `SexualReproductionInFloweringPlants` + `PrinciplesOfInheritanceAndVariation` | Pollination and the test cross as the experimental basis of inheritance. |
| B21 | 12 | `Ecosystem` + `OrganismsAndPopulations` | Energy flow, trophic structure and population growth models. |
| B22 | 12 | `Ecosystem` + `BiodiversityAndConservation` | Productivity and stability against species richness and conservation strategy. |
| B23 | 12 | `OrganismsAndPopulations` + `BiodiversityAndConservation` | Population interactions, adaptation and extinction risk. |
| B24 | 12 | `MicrobesInHumanWelfare` + `BiotechnologyAndItsApplications` | Microbial products, fermentation and engineered organisms. |
| B25 | 12 | `MicrobesInHumanWelfare` + `HumanHealthAndDisease` | Pathogens, antibiotics and immunity. |
| B26 | 12 | `BiotechnologyPrinciplesAndProcesses` + `BiotechnologyAndItsApplications` | Tools and processes against their agricultural and medical applications. |
| B27 | 12 | `BiotechnologyAndItsApplications` + `HumanHealthAndDisease` | Gene therapy, recombinant insulin and molecular diagnostics. |
| B28 | 12 | `Evolution` + `AnimalKingdom` + `PlantKingdom` | Homology, analogy and common ancestry read off the two classification schemes. |

**How to use the registry:** in Q-Pass 1, when building a Tier-2/3 item, pick a bridge whose keys include this anchor chapter; the other key is your `Links:` field, and you must cite at least one `Key:F###` row from it. A bridge not listed here is **not** available — off-registry links FAIL Q1, and a listed bridge whose chapter is not yet `Done` is withheld from the supplied text and listed as unavailable in the prompt the builder produced.


---

## SUPPLIED NCERT SOURCE TEXT (auto-assembled — the ONLY text you may treat as ground truth)

Build stamp: `AnimalKingdom@353+BodyFluidsAndCirculation@241,ExcretoryProductsAndTheirElimination@172,PlantKingdom@215`  ·  Anchor: **Class 11 — Ch4_AnimalKingdom (Animal Kingdom)**  ·  Anchor Gate 3: **DONE**

Bridge chapters supplied (3): BodyFluidsAndCirculation (class 11 Body Fluids And Circulation), ExcretoryProductsAndTheirElimination (class 11 Excretory Products And Their Elimination), PlantKingdom (class 11 Plant Kingdom)

**Citation contract.** Anchor facts are cited bare (`F012`); bridge facts are cited with their chapter key (`BodyFluidsAndCirculation:F031`). `check_qbank.py` resolves every ID you write against these exact tables, so an invented ID is a hard FAIL, not a stylistic slip.

**Bridges deliberately withheld** — do not link to these; NCERT may support the connection, but this repo has not gate-verified the facts, so any such link is UNGROUNDED:
- `BreathingAndExchangeOfGases` — UNAVAILABLE: no Facts table in its inventory
- `Evolution` — UNAVAILABLE: Gate 3 open — facts not gate-verified

### ANCHOR CHAPTER — Class 11, Ch4_AnimalKingdom (Animal Kingdom) — cite these as bare `F###` — 353 supplied source facts (frozen inventory rows)
- **F001** [4.0] (number): "As over a million species of animals have been described till now, the need for classification becomes all the more important."
- **F002** [4.0] (feature): "The classification also helps in assigning a systematic position to newly described species."
- **F003** [4.1] (list): "there are fundamental features common to various individuals in relation to the arrangement of cells, body symmetry, nature of coelom, patterns of digestive, circulatory or reproductive systems"
- **F004** [4.1] (feature): "These features are used as the basis of animal classification and some of them are discussed here."
- **F005** [4.1.1] (feature): "Though all members of Animalia are multicellular, all of them do not exhibit the same pattern of organisation of cells."
- **F006** [4.1.1] (definition): "in sponges, the cells are arranged as loose cell aggregates, i.e., they exhibit cellular level of organisation"
- **F007** [4.1.1] (feature): "Some division of labour (activities) occur among the cells."
- **F008** [4.1.1] (definition): "In coelenterates, the arrangement of cells is more complex. Here the cells performing the same function are arranged into tissues, hence is called tissue level of organisation."
- **F009** [4.1.1] (definition): "A still higher level of organisation, i.e., organ level is exhibited by members of Platyhelminthes and other higher phyla where tissues are grouped together to form organs, each specialised for a particular function."
- **F010** [4.1.1] (definition): "In animals like Annelids, Arthropods, Molluscs, Echinoderms and Chordates, organs have associated to form functional systems, each system concerned with a specific physiological function. This pattern is called organ system level of organisation."
- **F011** [4.1.1] (feature): "Organ systems in different groups of animals exhibit various patterns of complexities."
- **F012** [4.1.1] (definition): "the digestive system in Platyhelminthes has only a single opening to the outside of the body that serves as both mouth and anus, and is hence called incomplete"
- **F013** [4.1.1] (definition): "A complete digestive system has two openings, mouth and anus."
- **F014** [4.1.1] (definition): "(i) open type in which the blood is pumped out of the heart and the cells and tissues are directly bathed in it"
- **F015** [4.1.1] (definition): "(ii) closed type in which the blood is circulated through a series of vessels of varying diameters (arteries, veins and capillaries)"
- **F015a** [4.1.2] (feature): "Animals can be categorised on the basis of their symmetry." *(added in Pass 3(b) — §4.1.2 antecedent sentence; Pass 1 freeze gap, already present in script/PDF)*
- **F016** [4.1.2] (definition): "Sponges are mostly asymmetrical, i.e., any plane that passes through the centre does not divide them into equal halves."
- **F017** [4.1.2] (definition): "When any plane passing through the central axis of the body divides the organism into two identical halves, it is called radial symmetry."
- **F018** [4.1.2] (example): "Coelenterates, ctenophores and echinoderms have this kind of body plan (Figure 4.1a)."
- **F019** [4.1.2] (definition): "Animals like annelids, arthropods, etc., where the body can be divided into identical left and right halves in only one plane, exhibit bilateral symmetry (Figure 4.1b)."
- **F020** [4.1.3] (definition): "Animals in which the cells are arranged in two embryonic layers, an external ectoderm and an internal endoderm, are called diploblastic animals, e.g., coelenterates."
- **F021** [4.1.3] (feature): "An undifferentiated layer, mesoglea, is present in between the ectoderm and the endoderm (Figure 4.2a)."
- **F022** [4.1.3] (definition): "Those animals in which the developing embryo has a third germinal layer, mesoderm, in between the ectoderm and endoderm, are called triploblastic animals (platyhelminthes to chordates, Figure 4.2b)."
- **F023** [4.1.4] (feature): "Presence or absence of a cavity between the body wall and the gut wall is very important in classification."
- **F024** [4.1.4] (definition): "The body cavity, which is lined by mesoderm is called coelom."
- **F025** [4.1.4] (example): "Animals possessing coelom are called coelomates, e.g., annelids, molluscs, arthropods, echinoderms, hemichordates and chordates (Figure 4.3a)."
- **F026** [4.1.4] (definition): "In some animals, the body cavity is not lined by mesoderm, instead, the mesoderm is present as scattered pouches in between the ectoderm and endoderm. Such a body cavity is called pseudocoelom and the animals possessing them are called pseudocoelomates, e.g., aschelminthes (Figure 4.3b)."
- **F027** [4.1.4] (definition): "The animals in which the body cavity is absent are called acoelomates, e.g., platyhelminthes (Figure 4.3c)."
- **F028** [4.1.5] (definition): "In some animals, the body is externally and internally divided into segments with a serial repetition of at least some organs."
- **F029** [4.1.5] (definition): "For example, in earthworm, the body shows this pattern called metameric segmentation and the phenomenon is known as metamerism."
- **F030** [4.1.6] (definition): "Notochord is a mesodermally derived rod-like structure formed on the dorsal side during embryonic development in some animals."
- **F031** [4.1.6] (definition): "Animals with notochord are called chordates and those animals which do not form this structure are called non-chordates, e.g., porifera to echinoderms."
- **F032** [4.2] (feature): "The broad classification of Animalia, based on common fundamental features as mentioned in the preceding sections, is given in Figure 4.4."
- **F033** [4.2] (feature): "The important characteristic features of the different phyla are described."
- **F034** [4.2] (exception): Figure 4.4 footnote: "*Echinodermata exhibits radial or bilateral symmetry depending on the stage."
- **F035** [4.2.1] (term): "Members of this phylum are commonly known as sponges."
- **F036** [4.2.1] (feature): "They are generally marine and mostly asymmetrical animals (Figure 4.5)."
- **F037** [4.2.1] (feature): "These are primitive multicellular animals and have cellular level of organisation."
- **F038** [4.2.1] (feature): "Sponges have a water transport or canal system."
- **F039** [4.2.1] (process): "Water enters through minute pores (ostia) in the body wall into a central cavity, spongocoel, from where it goes out through the osculum."
- **F040** [4.2.1] (feature): "This pathway of water transport is helpful in food gathering, respiratory exchange and removal of waste."
- **F041** [4.2.1] (term): "Choanocytes or collar cells line the spongocoel and the canals."
- **F042** [4.2.1] (feature): "Digestion is intracellular."
- **F043** [4.2.1] (feature): "The body is supported by a skeleton made up of spicules or spongin fibres."
- **F044** [4.2.1] (feature): "Sexes are not separate (hermaphrodite), i.e., eggs and sperms are produced by the same individual."
- **F045** [4.2.1] (process): "Sponges reproduce asexually by fragmentation and sexually by formation of gametes."
- **F046** [4.2.1] (feature): "Fertilisation is internal and development is indirect having a larval stage which is morphologically distinct from the adult."
- **F047** [4.2.1] (example): "Examples: Sycon (Scypha), Spongilla (Fresh water sponge) and Euspongia (Bath sponge)."
- **F048** [4.2.2] (feature): "They are aquatic, mostly marine, sessile or free-swimming, radially symmetrical animals (Figure 4.6)."
- **F049** [4.2.2] (etymology): "The name cnidaria is derived from the cnidoblasts or cnidocytes (which contain the stinging capsules or nematocysts) present on the tentacles and the body."
- **F050** [4.2.2] (feature): "Cnidoblasts are used for anchorage, defense and for the capture of prey (Figure 4.7)."
- **F051** [4.2.2] (feature): "Cnidarians exhibit tissue level of organisation and are diploblastic."
- **F052** [4.2.2] (feature): "They have a central gastro-vascular cavity with a single opening, mouth on hypostome."
- **F053** [4.2.2] (feature): "Digestion is extracellular and intracellular."
- **F054** [4.2.2] (example): "Some of the cnidarians, e.g., corals have a skeleton composed of calcium carbonate."
- **F055** [4.2.2] (feature): "Cnidarians exhibit two basic body forms called polyp and medusa (Figure 4.6)."
- **F056** [4.2.2] (definition): "The former is a sessile and cylindrical form like Hydra, Adamsia, etc."
- **F057** [4.2.2] (definition): "whereas, the latter is umbrella-shaped and free-swimming like Aurelia or jelly fish"
- **F058** [4.2.2] (process): "Those cnidarians which exist in both forms exhibit alternation of generations (Metagenesis), i.e., polyps produce medusae asexually and medusae form the polyps sexually (e.g., Obelia)."
- **F059** [4.2.2] (example): "Examples: Physalia (Portuguese man-of-war), Adamsia (Sea anemone), Pennatula (Sea-pen), Gorgonia (Sea-fan) and Meandrina (Brain coral)."
- **F060** [4.2.3] (term): "Ctenophores, commonly known as sea walnuts or comb jellies"
- **F061** [4.2.3] (feature): "are exclusively marine, radially symmetrical, diploblastic organisms with tissue level of organisation"
- **F062** [4.2.3] (number): "The body bears eight external rows of ciliated comb plates, which help in locomotion (Figure 4.8)."
- **F063** [4.2.3] (feature): "Digestion is both extracellular and intracellular."
- **F064** [4.2.3] (definition): "Bioluminescence (the property of a living organism to emit light) is well-marked in ctenophores."
- **F065** [4.2.3] (feature): "Sexes are not separate."
- **F066** [4.2.3] (feature): "Reproduction takes place only by sexual means."
- **F067** [4.2.3] (feature): "Fertilisation is external with indirect development."
- **F068** [4.2.3] (example): "Examples: Pleurobrachia and Ctenoplana."
- **F069** [4.2.4] (term): "They have dorso-ventrally flattened body, hence are called flatworms (Figure 4.9)."
- **F070** [4.2.4] (feature): "These are mostly endoparasites found in animals including human beings."
- **F071** [4.2.4] (feature): "Flatworms are bilaterally symmetrical, triploblastic and acoelomate animals with organ level of organisation."
- **F072** [4.2.4] (feature): "Hooks and suckers are present in the parasitic forms."
- **F073** [4.2.4] (feature): "Some of them absorb nutrients from the host directly through their body surface."
- **F074** [4.2.4] (term): "Specialised cells called flame cells help in osmoregulation and excretion."
- **F075** [4.2.4] (feature): "Sexes are not separate."
- **F076** [4.2.4] (feature): "Fertilisation is internal and development is through many larval stages."
- **F077** [4.2.4] (example): "Some members like Planaria possess high regeneration capacity."
- **F078** [4.2.4] (example): "Examples: Taenia (Tapeworm), Fasciola (Liver fluke)."
- **F079** [4.2.5] (term): "The body of the aschelminthes is circular in cross-section, hence, the name roundworms (Figure 4.10)."
- **F080** [4.2.5] (feature): "They may be freeliving, aquatic and terrestrial or parasitic in plants and animals."
- **F081** [4.2.5] (feature): "Roundworms have organ-system level of body organisation."
- **F082** [4.2.5] (feature): "They are bilaterally symmetrical, triploblastic and pseudocoelomate animals."
- **F083** [4.2.5] (feature): "Alimentary canal is complete with a well-developed muscular pharynx."
- **F084** [4.2.5] (feature): "An excretory tube removes body wastes from the body cavity through the excretory pore."
- **F085** [4.2.5] (feature): "Sexes are separate (dioecious), i.e., males and females are distinct."
- **F086** [4.2.5] (comparison): "Often females are longer than males."
- **F087** [4.2.5] (feature): "Fertilisation is internal and development may be direct (the young ones resemble the adult) or indirect."
- **F088** [4.2.5] (example): "Examples : Ascaris (Roundworm), Wuchereria (Filaria worm), Ancylostoma (Hookworm)."
- **F089** [4.2.6] (feature): "They may be aquatic (marine and fresh water) or terrestrial; free-living, and sometimes parasitic."
- **F090** [4.2.6] (feature): "They exhibit organ-system level of body organisation and bilateral symmetry."
- **F091** [4.2.6] (feature): "They are triploblastic, metamerically segmented and coelomate animals."
- **F092** [4.2.6] (etymology): "Their body surface is distinctly marked out into segments or metameres and, hence, the phylum name Annelida (Latin, annulus : little ring) (Figure 4.11)."
- **F093** [4.2.6] (feature): "They possess longitudinal and circular muscles which help in locomotion."
- **F094** [4.2.6] (feature): "Aquatic annelids like Nereis possess lateral appendages, parapodia, which help in swimming."
- **F095** [4.2.6] (feature): "A closed circulatory system is present."
- **F096** [4.2.6] (term): "Nephridia (sing. nephridium) help in osmoregulation and excretion."
- **F097** [4.2.6] (feature): "Neural system consists of paired ganglia (sing. ganglion) connected by lateral nerves to a double ventral nerve cord."
- **F098** [4.2.6] (comparison): "Nereis, an aquatic form, is dioecious, but earthworms and leeches are monoecious."
- **F099** [4.2.6] (feature): "Reproduction is sexual."
- **F100** [4.2.6] (example): "Examples : Nereis, Pheretima (Earthworm) and Hirudinaria (Blood sucking leech)."
- **F101** [4.2.7] (feature): "This is the largest phylum of Animalia which includes insects."
- **F102** [4.2.7] (number): "Over two-thirds of all named species on earth are arthropods (Figure 4.12)."
- **F103** [4.2.7] (feature): "They have organ-system level of organisation."
- **F104** [4.2.7] (feature): "They are bilaterally symmetrical, triploblastic, segmented and coelomate animals."
- **F105** [4.2.7] (feature): "The body of arthropods is covered by chitinous exoskeleton."
- **F106** [4.2.7] (feature): "The body consists of head, thorax and abdomen."
- **F107** [4.2.7] (etymology): "They have jointed appendages (arthros-joint, poda-appendages)."
- **F108** [4.2.7] (feature): "Respiratory organs are gills, book gills, book lungs or tracheal system."
- **F109** [4.2.7] (feature): "Circulatory system is of open type."
- **F110** [4.2.7] (feature): "Sensory organs like antennae, eyes (compound and simple), statocysts or balancing organs are present."
- **F111** [4.2.7] (feature): "Excretion takes place through malpighian tubules."
- **F112** [4.2.7] (feature): "They are mostly dioecious."
- **F113** [4.2.7] (feature): "Fertilisation is usually internal."
- **F114** [4.2.7] (feature): "They are mostly oviparous."
- **F115** [4.2.7] (feature): "Development may be direct or indirect."
- **F116** [4.2.7] (example): "Examples: Economically important insects – Apis (Honey bee), Bombyx (Silkworm), Laccifer (Lac insect)"
- **F117** [4.2.7] (example): "Vectors – Anopheles, Culex and Aedes (Mosquitoes)"
- **F118** [4.2.7] (example): "Gregarious pest – Locusta (Locust)"
- **F119** [4.2.7] (example): "Living fossil – Limulus (King crab)."
- **F120** [4.2.8] (number): "This is the second largest animal phylum (Figure 4.13)."
- **F121** [4.2.8] (feature): "Molluscs are terrestrial or aquatic (marine or fresh water) having an organ-system level of organisation."
- **F122** [4.2.8] (feature): "They are bilaterally symmetrical, triploblastic and coelomate animals."
- **F123** [4.2.8] (feature): "Body is covered by a calcareous shell and is unsegmented with a distinct head, muscular foot and visceral hump."
- **F124** [4.2.8] (feature): "A soft and spongy layer of skin forms a mantle over the visceral hump."
- **F125** [4.2.8] (definition): "The space between the hump and the mantle is called the mantle cavity in which feather like gills are present."
- **F126** [4.2.8] (feature): "They have respiratory and excretory functions."
- **F127** [4.2.8] (feature): "The anterior head region has sensory tentacles."
- **F128** [4.2.8] (term): "The mouth contains a file-like rasping organ for feeding, called radula."
- **F129** [4.2.8] (feature): "They are usually dioecious and oviparous with indirect development."
- **F130** [4.2.8] (example): "Examples: Pila (Apple snail), Pinctada (Pearl oyster), Sepia (Cuttlefish), Loligo (Squid), Octopus (Devil fish), Aplysia (Sea-hare), Dentalium (Tusk shell) and Chaetopleura (Chiton)."
- **F131** [4.2.9] (etymology): "These animals have an endoskeleton of calcareous ossicles and, hence, the name Echinodermata (Spiny bodied, Figure 4.14)."
- **F132** [4.2.9] (feature): "All are marine with organ-system level of organisation."
- **F133** [4.2.9] (comparison): "The adult echinoderms are radially symmetrical but larvae are bilaterally symmetrical."
- **F134** [4.2.9] (feature): "They are triploblastic and coelomate animals."
- **F135** [4.2.9] (feature): "Digestive system is complete with mouth on the lower (ventral) side and anus on the upper (dorsal) side."
- **F136** [4.2.9] (feature): "The most distinctive feature of echinoderms is the presence of water vascular system which helps in locomotion, capture and transport of food and respiration."
- **F137** [4.2.9] (feature): "An excretory system is absent."
- **F138** [4.2.9] (feature): "Sexes are separate."
- **F139** [4.2.9] (feature): "Reproduction is sexual."
- **F140** [4.2.9] (feature): "Fertilisation is usually external."
- **F141** [4.2.9] (feature): "Development is indirect with free-swimming larva."
- **F142** [4.2.9] (example): "Examples: Asterias (Star fish), Echinus (Sea urchin), Antedon (Sea lily), Cucumaria (Sea cucumber) and Ophiura (Brittle star)."
- **F143** [4.2.10] (comparison): "Hemichordata was earlier considered as a sub-phylum under phylum Chordata. But now it is placed as a separate phylum under non-chordata."
- **F144** [4.2.10] (term): "Hemichordates have a rudimentary structure in the collar region called stomochord, a structure similar to notochord."
- **F145** [4.2.10] (feature): "This phylum consists of a small group of worm-like marine animals with organ-system level of organisation."
- **F146** [4.2.10] (feature): "They are bilaterally symmetrical, triploblastic and coelomate animals."
- **F147** [4.2.10] (feature): "The body is cylindrical and is composed of an anterior proboscis, a collar and a long trunk (Figure 4.15)."
- **F148** [4.2.10] (feature): "Circulatory system is of open type."
- **F149** [4.2.10] (feature): "Respiration takes place through gills."
- **F150** [4.2.10] (term): "Excretory organ is proboscis gland."
- **F151** [4.2.10] (feature): "Sexes are separate."
- **F152** [4.2.10] (feature): "Fertilisation is external."
- **F153** [4.2.10] (feature): "Development is indirect."
- **F154** [4.2.10] (example): "Examples: Balanoglossus and Saccoglossus."
- **F155** [4.0] (heading): "CHAPTER 4"
- **F156** [4.0] (heading): "ANIMAL KINGDOM"
- **F157** [4.1] (heading): "4.1 BASIS OF CLASSIFICATION"
- **F158** [4.1.1] (heading): "4.1.1 Levels of Organisation"
- **F159** [4.1.2] (heading): "4.1.2 Symmetry"
- **F160** [4.1.3] (heading): "4.1.3 Diploblastic and Triploblastic Organisation"
- **F161** [4.1.4] (heading): "4.1.4 Coelom"
- **F162** [4.1.5] (heading): "4.1.5 Segmentation"
- **F163** [4.1.6] (heading): "4.1.6 Notochord"
- **F164** [4.2] (heading): "4.2 CLASSIFICATION OF ANIMALS"
- **F165** [4.2.1] (heading): "4.2.1 Phylum – Porifera"
- **F166** [4.2.2] (heading): "4.2.2 Phylum – Coelenterata (Cnidaria)"
- **F167** [4.2.3] (heading): "4.2.3 Phylum – Ctenophora"
- **F168** [4.2.4] (heading): "4.2.4 Phylum – Platyhelminthes"
- **F169** [4.2.5] (heading): "4.2.5 Phylum – Aschelminthes"
- **F170** [4.2.6] (heading): "4.2.6 Phylum – Annelida"
- **F171** [4.2.7] (heading): "4.2.7 Phylum – Arthropoda"
- **F172** [4.2.8] (heading): "4.2.8 Phylum – Mollusca"
- **F173** [4.2.9] (heading): "4.2.9 Phylum – Echinodermata"
- **F174** [4.2.10] (heading): "4.2.10 Phylum – Hemichordata"
- **F175** [4.0] (heading): Chapter-opening contents sidebar (source page 1, italic light face, not a body heading tier): "4.1 Basis of Classification"; "4.2 Classification of Animals"
- **F176** [4.0] (opener): "When you look around, you will observe different animals with different structures and forms."
- **F177** [4.1] (opener): "Inspite of differences in structure and form of different animals, there are fundamental features common to various individuals in relation to the arrangement of cells, body symmetry, nature of coelom, patterns of digestive, circulatory or reproductive systems."
- **F178** [4.1.1] (opener): "Though all members of Animalia are multicellular, all of them do not exhibit the same pattern of organisation of cells."
- **F179** [4.1.2] (opener): "Animals can be categorised on the basis of their symmetry."
- **F180** [4.1.3] (opener): "Animals in which the cells are arranged in two embryonic layers, an external ectoderm and an internal endoderm, are called diploblastic animals, e.g., coelenterates."
- **F181** [4.1.4] (opener): "Presence or absence of a cavity between the body wall and the gut wall is very important in classification."
- **F182** [4.1.5] (opener): "In some animals, the body is externally and internally divided into segments with a serial repetition of at least some organs."
- **F183** [4.1.6] (opener): "Notochord is a mesodermally derived rod-like structure formed on the dorsal side during embryonic development in some animals."
- **F184** [4.2] (opener): "The broad classification of Animalia, based on common fundamental features as mentioned in the preceding sections, is given in Figure 4.4."
- **F185** [4.2.1] (opener): "Members of this phylum are commonly known as sponges."
- **F186** [4.2.2] (opener): "They are aquatic, mostly marine, sessile or free-swimming, radially symmetrical animals (Figure 4.6)."
- **F187** [4.2.3] (opener): "Ctenophores, commonly known as sea walnuts or comb jellies are exclusively marine, radially symmetrical, diploblastic organisms with tissue level of organisation."
- **F188** [4.2.4] (opener): "They have dorso-ventrally flattened body, hence are called flatworms (Figure 4.9)."
- **F189** [4.2.5] (opener): "The body of the aschelminthes is circular in cross-section, hence, the name roundworms (Figure 4.10)."
- **F190** [4.2.6] (opener): "They may be aquatic (marine and fresh water) or terrestrial; free-living, and sometimes parasitic."
- **F191** [4.2.7] (opener): "This is the largest phylum of Animalia which includes insects."
- **F192** [4.2.8] (opener): "This is the second largest animal phylum (Figure 4.13)."
- **F193** [4.2.9] (opener): "These animals have an endoskeleton of calcareous ossicles and, hence, the name Echinodermata (Spiny bodied, Figure 4.14)."
- **F194** [4.2.10] (opener): "Hemichordata was earlier considered as a sub-phylum under phylum Chordata."
- **F195** [4.2.11] (definition): "Animals belonging to phylum Chordata are fundamentally characterised by the presence of a notochord, a dorsal hollow nerve cord and paired pharyngeal gill slits (Figure 4.16)."
- **F196** [4.2.11] (feature): "These are bilaterally symmetrical, triploblastic, coelomate with organ-system level of organisation."
- **F197** [4.2.11] (feature): "They possess a post anal tail and a closed circulatory system."
- **F198** [4.2.11] (feature): "Table 4.1 presents a comparison of salient features of chordates and non-chordates."
- **F199** [4.2.11] (feature): "Phylum Chordata is divided into three subphyla: Urochordata or Tunicata, Cephalochordata and Vertebrata."
- **F200** [4.2.11] (definition): "Subphyla Urochordata and Cephalochordata are often referred to as protochordates (Figure 4.17) and are exclusively marine."
- **F201** [4.2.11] (comparison): "In Urochordata, notochord is present only in larval tail, while in Cephalochordata, it extends from head to tail region and is persistent throughout their life."
- **F202** [4.2.11] (example): "Examples: Urochordata – Ascidia, Salpa, Doliolum; Cephalochordata – Branchiostoma (Amphioxus or Lancelet)."
- **F203** [4.2.11] (feature): "The members of subphylum Vertebrata possess notochord during the embryonic period."
- **F204** [4.2.11] (feature): "The notochord is replaced by a cartilaginous or bony vertebral column in the adult."
- **F205** [4.2.11] (comparison): "Thus all vertebrates are chordates but all chordates are not vertebrates."
- **F206** [4.2.11] (feature): "Besides the basic chordate characters, vertebrates have a ventral muscular heart with two, three or four chambers, kidneys for excretion and osmoregulation and paired appendages which may be fins or limbs."
- **F207** [4.2.11] (caption): TABLE 4.1 title: "TABLE 4.1 Comparison of Chordates and Non-chordates"
- **F208** [4.2.11] (comparison): TABLE 4.1 row 1 — Chordates: "Notochord present." / Non-chordates: "Notochord absent."
- **F209** [4.2.11] (comparison): TABLE 4.1 row 2 — Chordates: "Central nervous system is dorsal, hollow and single." / Non-chordates: "Central nervous system is ventral, solid and double."
- **F210** [4.2.11] (comparison): TABLE 4.1 row 3 — Chordates: "Pharynx perforated by gill slits." / Non-chordates: "Gill slits are absent."
- **F211** [4.2.11] (comparison): TABLE 4.1 row 4 — Chordates: "Heart is ventral." / Non-chordates: "Heart is dorsal (if present)."
- **F212** [4.2.11] (comparison): TABLE 4.1 row 5 — Chordates: "A post-anal part (tail) is present." / Non-chordates: "Post-anal tail is absent."
- **F213** [4.2.11] (feature): "The subphylum Vertebrata is further divided as follows:" (lead-in to the Vertebrata classification chart, source page 11)
- **F214** [4.2.11] (list): Vertebrata chart: Vertebrata is split into two divisions — "Agnatha (lacks jaw)" and "Gnathostomata (bears jaw)".
- **F215** [4.2.11] (list): Vertebrata chart: Division "Agnatha (lacks jaw)" contains Class "1. Cyclostomata".
- **F216** [4.2.11] (list): Vertebrata chart: Division "Gnathostomata (bears jaw)" contains two Super Classes — "Pisces (bear fins)" and "Tetrapoda (bear limbs)".
- **F217** [4.2.11] (list): Vertebrata chart: Super Class "Pisces (bear fins)" contains Classes "1. Chondrichthyes" and "2. Osteichthyes".
- **F218** [4.2.11] (list): Vertebrata chart: Super Class "Tetrapoda (bear limbs)" contains Classes "1. Amphibia", "2. Reptilia", "3. Aves" and "4. Mammals".
- **F219** [4.2.11.1] (feature): "All living members of the class Cyclostomata are ectoparasites on some fishes."
- **F220** [4.2.11.1] (number): "They have an elongated body bearing 6-15 pairs of gill slits for respiration."
- **F221** [4.2.11.1] (feature): "Cyclostomes have a sucking and circular mouth without jaws (Fig. 4.18)."
- **F222** [4.2.11.1] (feature): "Their body is devoid of scales and paired fins."
- **F223** [4.2.11.1] (feature): "Cranium and vertebral column are cartilaginous."
- **F224** [4.2.11.1] (feature): "Circulation is of closed type."
- **F225** [4.2.11.1] (feature): "Cyclostomes are marine but migrate for spawning to fresh water."
- **F226** [4.2.11.1] (feature): "After spawning, within a few days, they die."
- **F227** [4.2.11.1] (feature): "Their larvae, after metamorphosis, return to the ocean."
- **F228** [4.2.11.1] (example): "Examples: Petromyzon (Lamprey) and Myxine (Hagfish)."
- **F229** [4.2.11.2] (feature): "They are marine animals with streamlined body and have cartilaginous endoskeleton (Figure 4.19)."
- **F230** [4.2.11.2] (feature): "Mouth is located ventrally."
- **F231** [4.2.11.2] (feature): "Notochord is persistent throughout life."
- **F232** [4.2.11.2] (feature): "Gill slits are separate and without operculum (gill cover)."
- **F233** [4.2.11.2] (feature): "The skin is tough, containing minute placoid scales."
- **F234** [4.2.11.2] (feature): "Teeth are modified placoid scales which are backwardly directed."
- **F235** [4.2.11.2] (feature): "Their jaws are very powerful."
- **F236** [4.2.11.2] (feature): "These animals are predaceous."
- **F237** [4.2.11.2] (feature): "Due to the absence of air bladder, they have to swim constantly to avoid sinking."
- **F238** [4.2.11.2] (feature): "Heart is two-chambered (one auricle and one ventricle)."
- **F239** [4.2.11.2] (example): "Some of them have electric organs (e.g., Torpedo) and some possess poison sting (e.g., Trygon)."
- **F240** [4.2.11.2] (definition): "They are cold-blooded (poikilothermous) animals, i.e., they lack the capacity to regulate their body temperature."
- **F241** [4.2.11.2] (feature): "Sexes are separate."
- **F242** [4.2.11.2] (feature): "In males pelvic fins bear claspers."
- **F243** [4.2.11.2] (feature): "They have internal fertilisation and many of them are viviparous."
- **F244** [4.2.11.2] (example): "Examples: Scoliodon (Dog fish), Pristis (Saw fish), Carcharodon (Great white shark), Trygon (Sting ray)."
- **F245** [4.2.11.3] (feature): "It includes both marine and fresh water fishes with bony endoskeleton."
- **F246** [4.2.11.3] (feature): "Their body is streamlined."
- **F247** [4.2.11.3] (feature): "Mouth is mostly terminal (Figure 4.20)."
- **F248** [4.2.11.3] (number): "They have four pairs of gills which are covered by an operculum on each side."
- **F249** [4.2.11.3] (feature): "Skin is covered with cycloid/ctenoid scales."
- **F250** [4.2.11.3] (feature): "Air bladder is present which regulates buoyancy."
- **F251** [4.2.11.3] (feature): "Heart is two-chambered (one auricle and one ventricle)."
- **F252** [4.2.11.3] (feature): "They are cold-blooded animals."
- **F253** [4.2.11.3] (feature): "Sexes are separate."
- **F254** [4.2.11.3] (feature): "Fertilisation is usually external."
- **F255** [4.2.11.3] (feature): "They are mostly oviparous and development is direct."
- **F256** [4.2.11.3] (example): "Examples: Marine – Exocoetus (Flying fish), Hippocampus (Sea horse); Freshwater – Labeo (Rohu), Catla (Katla), Clarias (Magur); Aquarium – Betta (Fighting fish), Pterophyllum (Angel fish)."
- **F257** [4.2.11.4] (etymology): "As the name indicates (Gr., Amphi : dual, bios, life), amphibians can live in aquatic as well as terrestrial habitats (Figure 4.21)."
- **F258** [4.2.11.4] (feature): "Most of them have two pairs of limbs."
- **F259** [4.2.11.4] (feature): "Body is divisible into head and trunk."
- **F260** [4.2.11.4] (feature): "Tail may be present in some."
- **F261** [4.2.11.4] (feature): "The amphibian skin is moist (without scales)."
- **F262** [4.2.11.4] (feature): "The eyes have eyelids."
- **F263** [4.2.11.4] (feature): "A tympanum represents the ear."
- **F264** [4.2.11.4] (definition): "Alimentary canal, urinary and reproductive tracts open into a common chamber called cloaca which opens to the exterior."
- **F265** [4.2.11.4] (feature): "Respiration is by gills, lungs and through skin."
- **F266** [4.2.11.4] (feature): "The heart is three-chambered (two auricles and one ventricle)."
- **F267** [4.2.11.4] (feature): "These are cold-blooded animals."
- **F268** [4.2.11.4] (feature): "Sexes are separate."
- **F269** [4.2.11.4] (feature): "Fertilisation is external."
- **F270** [4.2.11.4] (feature): "They are oviparous and development is indirect."
- **F271** [4.2.11.4] (example): "Examples: Bufo (Toad), Rana (Frog), Hyla (Tree frog), Salamandra (Salamander), Ichthyophis (Limbless amphibia)."
- **F272** [4.2.11.5] (etymology): "The class name refers to their creeping or crawling mode of locomotion (Latin, repere or reptum, to creep or crawl)."
- **F273** [4.2.11.5] (feature): "They are mostly terrestrial animals and their body is covered by dry and cornified skin, epidermal scales or scutes (Fig. 4.22)."
- **F274** [4.2.11.5] (feature): "They do not have external ear openings."
- **F275** [4.2.11.5] (feature): "Tympanum represents ear."
- **F276** [4.2.11.5] (feature): "Limbs, when present, are two pairs."
- **F277** [4.2.11.5] (exception): "Heart is usually three-chambered, but four-chambered in crocodiles."
- **F278** [4.2.11.5] (feature): "Reptiles are poikilotherms."
- **F279** [4.2.11.5] (feature): "Snakes and lizards shed their scales as skin cast."
- **F280** [4.2.11.5] (feature): "Sexes are separate."
- **F281** [4.2.11.5] (feature): "Fertilisation is internal."
- **F282** [4.2.11.5] (feature): "They are oviparous and development is direct."
- **F283** [4.2.11.5] (example): "Examples: Chelone (Turtle), Testudo (Tortoise), Chameleon (Tree lizard), Calotes (Garden lizard), Crocodilus (Crocodile), Alligator (Alligator). Hemidactylus (Wall lizard), Poisonous snakes – Naja (Cobra), Bangarus (Krait), Vipera (Viper)."
- **F284** [4.2.11.6] (feature): "The characteristic features of Aves (birds) are the presence of feathers and most of them can fly except flightless birds (e.g., Ostrich)."
- **F285** [4.2.11.6] (feature): "They possess beak (Figure 4.23)."
- **F286** [4.2.11.6] (feature): "The forelimbs are modified into wings."
- **F287** [4.2.11.6] (feature): "The hind limbs generally have scales and are modified for walking, swimming or clasping the tree branches."
- **F288** [4.2.11.6] (feature): "Skin is dry without glands except the oil gland at the base of the tail."
- **F289** [4.2.11.6] (feature): "Endoskeleton is fully ossified (bony) and the long bones are hollow with air cavities (pneumatic)."
- **F290** [4.2.11.6] (feature): "The digestive tract of birds has additional chambers, the crop and gizzard."
- **F291** [4.2.11.6] (feature): "Heart is completely four-chambered."
- **F292** [4.2.11.6] (definition): "They are warm-blooded (homoiothermous) animals, i.e., they are able to maintain a constant body temperature."
- **F293** [4.2.11.6] (feature): "Respiration is by lungs."
- **F294** [4.2.11.6] (feature): "Air sacs connected to lungs supplement respiration."
- **F295** [4.2.11.6] (feature): "Sexes are separate."
- **F296** [4.2.11.6] (feature): "Fertilisation is internal."
- **F297** [4.2.11.6] (feature): "They are oviparous and development is direct."
- **F298** [4.2.11.6] (example): "Examples : Corvus (Crow), Columba (Pigeon), Psittacula (Parrot), Struthio (Ostrich), Pavo (Peacock), Aptenodytes (Penguin), Neophron (Vulture)."
- **F299** [4.2.11.7] (feature): "They are found in a variety of habitats – polar ice caps, deserts, mountains, forests, grasslands and dark caves."
- **F300** [4.2.11.7] (feature): "Some of them have adapted to fly or live in water."
- **F301** [4.2.11.7] (definition): "The most unique mammalian characteristic is the presence of milk producing glands (mammary glands) by which the young ones are nourished."
- **F302** [4.2.11.7] (feature): "They have two pairs of limbs, adapted for walking, running, climbing, burrowing, swimming or flying (Figure 4.24)."
- **F303** [4.2.11.7] (feature): "The skin of mammals is unique in possessing hair."
- **F304** [4.2.11.7] (feature): "External ears or pinnae are present."
- **F305** [4.2.11.7] (feature): "Different types of teeth are present in the jaw."
- **F306** [4.2.11.7] (feature): "Heart is four-chambered."
- **F307** [4.2.11.7] (feature): "They are homoiothermous."
- **F308** [4.2.11.7] (feature): "Respiration is by lungs."
- **F309** [4.2.11.7] (feature): "Sexes are separate and fertilisation is internal."
- **F310** [4.2.11.7] (feature): "They are viviparous with few exceptions and development is direct."
- **F311** [4.2.11.7] (example): "Examples: Oviparous-Ornithorhynchus (Platypus); Viviparous - Macropus (Kangaroo), Pteropus (Flying fox), Camelus (Camel), Macaca (Monkey), Rattus (Rat), Canis (Dog), Felis (Cat), Elephas (Elephant), Equus (Horse), Delphinus (Common dolphin), Balaenoptera (Blue whale), Panthera tigris (Tiger), Panthera leo (Lion)."
- **F312** [4.2] (feature): "The salient distinguishing features of all phyla under animal kingdom is comprehensively given in the Table 4.2."
- **F313** [4.2] (caption): TABLE 4.2 title: "TABLE 4.2 Salient Features of Different Phyla in the Animal Kingdom"
- **F314** [4.2] (feature): TABLE 4.2 — Porifera: Level of Organisation "Cellular"; Symmetry "Various"; Coelom "Absent"; Segmentation "Absent"; Digestive System "Absent"; Circulatory System "Absent"; Respiratory System "Absent"; Distinctive Features "Body with pores and canals in walls."
- **F315** [4.2] (feature): TABLE 4.2 — Coelenterata (Cnidaria): Level of Organisation "Tissue"; Symmetry "Radial"; Coelom "Absent"; Segmentation "Absent"; Digestive System "Incomplete"; Circulatory System "Absent"; Respiratory System "Absent"; Distinctive Features "Cnidoblasts present."
- **F316** [4.2] (feature): TABLE 4.2 — Ctenophora: Level of Organisation "Tissue"; Symmetry "Radial"; Coelom "Absent"; Segmentation "Absent"; Digestive System "Incomplete"; Circulatory System "Absent"; Respiratory System "Absent"; Distinctive Features "Comb plates for locomotion."
- **F317** [4.2] (feature): TABLE 4.2 — Platyhelminthes: Level of Organisation "Organ & Organ-system"; Symmetry "Bilateral"; Coelom "Absent"; Segmentation "Absent"; Digestive System "Incomplete"; Circulatory System "Absent"; Respiratory System "Absent"; Distinctive Features "Flat body, suckers."
- **F318** [4.2] (feature): TABLE 4.2 — Aschelminthes: Level of Organisation "Organ-system"; Symmetry "Bilateral"; Coelom "Pseudocoelomate"; Segmentation "Absent"; Digestive System "Complete"; Circulatory System "Absent"; Respiratory System "Absent"; Distinctive Features "Often worm-shaped, elongated."
- **F319** [4.2] (feature): TABLE 4.2 — Annelida: Level of Organisation "Organ-system"; Symmetry "Bilateral"; Coelom "Coelomate"; Segmentation "Present"; Digestive System "Complete"; Circulatory System "Present"; Respiratory System "Absent"; Distinctive Features "Body segmentation like rings."
- **F320** [4.2] (feature): TABLE 4.2 — Arthropoda: Level of Organisation "Organ-system"; Symmetry "Bilateral"; Coelom "Coelomate"; Segmentation "Present"; Digestive System "Complete"; Circulatory System "Present"; Respiratory System "Present"; Distinctive Features "Exoskeleton of cuticle, jointed appendages."
- **F321** [4.2] (feature): TABLE 4.2 — Mollusca: Level of Organisation "Organ-system"; Symmetry "Bilateral"; Coelom "Coelomate"; Segmentation "Absent"; Digestive System "Complete"; Circulatory System "Present"; Respiratory System "Present"; Distinctive Features "External skeleton of shell usually present."
- **F322** [4.2] (feature): TABLE 4.2 — Echinodermata: Level of Organisation "Organ-system"; Symmetry "Radial"; Coelom "Coelomate"; Segmentation "Absent"; Digestive System "Complete"; Circulatory System "Present"; Respiratory System "Present"; Distinctive Features "Water vascular system, radial symmetry."
- **F323** [4.2] (feature): TABLE 4.2 — Hemichordata: Level of Organisation "Organ-system"; Symmetry "Bilateral"; Coelom "Coelomate"; Segmentation "Absent"; Digestive System "Complete"; Circulatory System "Present"; Respiratory System "Present"; Distinctive Features "Worm-like with proboscis, collar and trunk."
- **F324** [4.2] (feature): TABLE 4.2 — Chordata: Level of Organisation "Organ-system"; Symmetry "Bilateral"; Coelom "Coelomate"; Segmentation "Present"; Digestive System "Complete"; Circulatory System "Present"; Respiratory System "Present"; Distinctive Features "Notochord, dorsal hollow nerve cord, gill slits with limbs or fins."
- **F325** [4.2.11] (heading): "4.2.11 Phylum – Chordata"
- **F326** [4.2.11.1] (heading): "4.2.11.1 Class – Cyclostomata"
- **F327** [4.2.11.2] (heading): "4.2.11.2 Class – Chondrichthyes"
- **F328** [4.2.11.3] (heading): "4.2.11.3 Class – Osteichthyes"
- **F329** [4.2.11.4] (heading): "4.2.11.4 Class – Amphibia"
- **F330** [4.2.11.5] (heading): "4.2.11.5 Class – Reptilia"
- **F331** [4.2.11.6] (heading): "4.2.11.6 Class – Aves"
- **F332** [4.2.11.7] (heading): "4.2.11.7 Class – Mammalia"
- **F333** [SUMMARY] (heading): "SUMMARY" (unnumbered structural heading, source page 16)
- **F334** [EXERCISES] (heading): "EXERCISES" (unnumbered structural heading, source page 17)
- **F335** [4.2.11] (opener): "Animals belonging to phylum Chordata are fundamentally characterised by the presence of a notochord, a dorsal hollow nerve cord and paired pharyngeal gill slits (Figure 4.16)."
- **F336** [4.2.11.1] (opener): "All living members of the class Cyclostomata are ectoparasites on some fishes."
- **F337** [4.2.11.2] (opener): "They are marine animals with streamlined body and have cartilaginous endoskeleton (Figure 4.19)."
- **F338** [4.2.11.3] (opener): "It includes both marine and fresh water fishes with bony endoskeleton."
- **F339** [4.2.11.4] (opener): "As the name indicates (Gr., Amphi : dual, bios, life), amphibians can live in aquatic as well as terrestrial habitats (Figure 4.21)."
- **F340** [4.2.11.5] (opener): "The class name refers to their creeping or crawling mode of locomotion (Latin, repere or reptum, to creep or crawl)."
- **F341** [4.2.11.6] (opener): "The characteristic features of Aves (birds) are the presence of feathers and most of them can fly except flightless birds (e.g., Ostrich)."
- **F342** [4.2.11.7] (opener): "They are found in a variety of habitats – polar ice caps, deserts, mountains, forests, grasslands and dark caves."
- **F343** [4.1.3] (caption): Figure labels: "Ectoderm"; "Mesoglea"; "Endoderm"; "Mesoderm" (Figure 4.2ab, harvested from the rendered asset)
- **F344** [4.1.4] (caption): Figure labels: "Coelom"; "Pseudocoelom" (Figure 4.3abc, harvested from the rendered asset; panel (c) is unlabeled in the source)
- **F345** [4.2] (caption): Figure labels: "Kingdom"; "Levels of Organisation"; "Symmetry"; "Body Cavity or Coelom"; "Phylum"; "Animalia (multicellular)"; "Cellular level"; "mostly asymmetrical"; "acoelomata"; "Porifera"; "Tissue/Organ/Organ system"; "Radial"; "Coelenterata (Cnidaria)"; "Ctenophora"; "Without body cavity (acoelomates)"; "Platyhelminthes"; "Bilateral"; "With false coelom (pseudocoelomates)"; "Aschelminthes"; "With true coelom (coelomates)"; "Annelida"; "Arthropoda"; "Mollusca"; "Echinodermata"; "Hemichordata"; "Chordata" (Figure 4.4, harvested from the rendered asset)
- **F346** [4.2.5] (caption): Figure labels: "Male"; "Female" (Figure 4.10, harvested from the rendered asset)
- **F347** [4.2.10] (caption): Figure labels: "Proboscis"; "Collar"; "Trunk" (Figure 4.15, harvested from the rendered asset)
- **F348** [4.2.11] (caption): Figure labels: "Nerve cord"; "Notochord"; "Post-anal part"; "Gill slits" (Figure 4.16, harvested from the rendered asset)
- **F349** [4.2.11] (caption): Figure labels: "Vertebrata"; "Division"; "Agnatha (lacks jaw)"; "Gnathostomata (bears jaw)"; "Super Class"; "Pisces (bear fins)"; "Tetrapoda (bear limbs)"; "Class"; "Cyclostomata"; "Chondrichthyes"; "Osteichthyes"; "Amphibia"; "Reptilia"; "Aves"; "Mammals" (Vertebrata chart, harvested from the rendered asset)
- **F350** [4.2.1] (feature): "Porifera … have characteristic flagellated choanocytes." (folded from SUMMARY at 1-Z — body F041 names "Choanocytes or collar cells" but never states they are flagellated; only the "flagellated" qualifier is SUMMARY-UNIQUE)
- **F351** [4.2.11.1] (feature): "They are the most primitive chordates …" (folded from SUMMARY at 1-Z — body F219/F336 state cyclostomes are ectoparasites on fishes but never that they are the most primitive chordates; the ectoparasite half is BODY-PRESENT, only "most primitive chordates" is SUMMARY-UNIQUE)
- **F352** [4.2.11.5] (feature): "Limbs are absent in snakes." (folded from SUMMARY at 1-Z — body F273/F279 describe reptile dry/cornified skin and scale-shedding by snakes and lizards but never state that limbs are absent in snakes)

### BRIDGE CHAPTER — Class 11, Ch15_BodyFluidsAndCirculation (Body Fluids And Circulation) — cite these as `BodyFluidsAndCirculation:F###` — 241 supplied source facts (frozen inventory rows)
- **F001** [title] (heading): Chapter title plate: 'BODY FLUIDS AND CIRCULATION' with 'CHAPTER 15' (no opening sentence of its own)
- **F002** [intro] (opener): "You have learnt that all living cells have to be provided with nutrients, O2 and other essential substances."
- **F003** [intro] (concept): "Also, the waste or harmful substances produced, have to be removed continuously for healthy functioning of tissues."
- **F004** [intro] (concept): "It is therefore, essential to have efficient mechanisms for the movement of these substances to the cells and from the cells."
- **F005** [intro] (concept): "Different groups of animals have evolved different methods for this transport."
- **F006** [intro] (example): "Simple organisms like sponges and coelenterates circulate water from their surroundings through their body cavities to facilitate the cells to exchange these substances."
- **F007** [intro] (concept): "More complex organisms use special fluids within their bodies to transport such materials."
- **F008** [intro] (concept): "Blood is the most commonly used body fluid by most of the higher organisms, including humans, for this purpose."
- **F009** [intro] (concept): "Another body fluid, lymph, also helps in the transport of certain substances."
- **F010** [intro] (concept): "In this chapter, you will learn about the composition and properties of blood and lymph (tissue fluid) and the mechanism of circulation of blood is also explained herein."
- **F011** [intro] (list): Chapter contents panel (p. 193 margin): "15.1 Blood"; "15.2 Lymph (Tissue Fluid)"; "15.3 Circulatory Pathways"; "15.4 Double Circulation"; "15.5 Regulation of Cardiac Activity"; "15.6 Disorders of Circulatory System"
- **F012** [15.1] (heading): "15.1 BLOOD"
- **F013** [15.1] (opener): "Blood is a special connective tissue consisting of a fluid matrix, plasma, and formed elements."
- **F014** [15.1.1] (heading): "15.1.1 Plasma"
- **F015** [15.1.1] (opener): "Plasma is a straw coloured, viscous fluid constituting nearly 55 per cent of the blood."
- **F016** [15.1.1] (number): "90-92 per cent of plasma is water and proteins contribute 6-8 per cent of it."
- **F017** [15.1.1] (list): "Fibrinogen, globulins and albumins are the major proteins."
- **F018** [15.1.1] (concept): "Fibrinogens are needed for clotting or coagulation of blood."
- **F019** [15.1.1] (concept): "Globulins primarly are involved in defense mechanisms of the body"
- **F020** [15.1.1] (concept): "the albumins help in osmotic balance"
- **F021** [15.1.1] (list): "Plasma also contains small amounts of minerals like Na+, Ca++, Mg++, HCO3–, Cl–, etc."
- **F022** [15.1.1] (concept): "Glucose, amino acids, lipids, etc., are also present in the plasma as they are always in transit in the body."
- **F023** [15.1.1] (concept): "Factors for coagulation or clotting of blood are also present in the plasma in an inactive form."
- **F024** [15.1.1] (definition): "Plasma without the clotting factors is called serum."
- **F025** [15.1.2] (heading): "15.1.2 Formed Elements"
- **F026** [15.1.2] (opener): "Erythrocytes, leucocytes and platelets are collectively called formed elements (Figure 15.1) and they constitute nearly 45 per cent of the blood."
- **F027** [15.1.2] (definition): "Erythrocytes or red blood cells (RBC) are the most abundant of all the cells in blood."
- **F028** [15.1.2] (number): "A healthy adult man has, on an average, 5 millions to 5.5 millions of RBCs mm–3 of blood."
- **F029** [15.1.2] (concept): "RBCs are formed in the red bone marrow in the adults."
- **F030** [15.1.2] (concept): "RBCs are devoid of nucleus in most of the mammals and are biconcave in shape."
- **F031** [15.1.2] (concept): "They have a red coloured, iron containing complex protein called haemoglobin, hence the colour and name of these cells."
- **F032** [15.1.2] (number): "A healthy individual has 12-16 gms of haemoglobin in every 100 ml of blood."
- **F033** [15.1.2] (concept): "These molecules play a significant role in transport of respiratory gases."
- **F034** [15.1.2] (number): "RBCs have an average life span of 120 days after which they are destroyed in the spleen (graveyard of RBCs)."
- **F035** [15.1.2] (definition): "Leucocytes are also known as white blood cells (WBC) as they are colourless due to the lack of haemoglobin."
- **F036** [15.1.2] (number): "They are nucleated and are relatively lesser in number which averages 6000-8000 mm–3 of blood."
- **F037** [15.1.2] (concept): "Leucocytes are generally short lived."
- **F038** [15.1.2] (list): "We have two main categories of WBCs – granulocytes and agranulocytes."
- **F039** [15.1.2] (list): "Neutrophils, eosinophils and basophils are different types of granulocytes, while lymphocytes and monocytes are the agranulocytes."
- **F040** [15.1.2] (number): "Neutrophils are the most abundant cells (60-65 per cent) of the total WBCs and basophils are the least (0.5-1 per cent) among them."
- **F041** [15.1.2] (number): "Neutrophils and monocytes (6-8 per cent) are phagocytic cells which destroy foreign organisms entering the body."
- **F042** [15.1.2] (concept): "Basophils secrete histamine, serotonin, heparin, etc., and are involved in inflammatory reactions."
- **F043** [15.1.2] (number): "Eosinophils (2-3 per cent) resist infections and are also associated with allergic reactions."
- **F044** [15.1.2] (number): "Lymphocytes (20-25 per cent) are of two major types – 'B' and 'T' forms."
- **F045** [15.1.2] (concept): "Both B and T lymphocytes are responsible for immune responses of the body."
- **F046** [15.1.2] (definition): "Platelets also called thrombocytes, are cell fragments produced from megakaryocytes (special cells in the bone marrow)."
- **F047** [15.1.2] (number): "Blood normally contains 1,500,00-3,500,00 platelets mm–3."
- **F048** [15.1.2] (concept): "Platelets can release a variety of substances most of which are involved in the coagulation or clotting of blood."
- **F049** [15.1.2] (concept): "A reduction in their number can lead to clotting disorders which will lead to excessive loss of blood from the body."
- **F050** [15.1.2] (caption): "Figure 15.1 Diagrammatic representation of formed elements in blood"
- **F051** [15.1.3] (heading): "15.1.3 Blood Groups"
- **F052** [15.1.3] (opener): "As you know, blood of human beings differ in certain aspects though it appears to be similar."
- **F053** [15.1.3] (concept): "Various types of grouping of blood has been done."
- **F054** [15.1.3] (concept): "Two such groupings – the ABO and Rh – are widely used all over the world."
- **F055** [15.1.3.1] (heading): "15.1.3.1 ABO grouping"
- **F056** [15.1.3.1] (opener): "ABO grouping is based on the presence or absence of two surface antigens (chemicals that can induce immune response) on the RBCs namely A and B."
- **F057** [15.1.3.1] (definition): "Similarly, the plasma of different individuals contain two natural antibodies (proteins produced in response to antigens)."
- **F058** [15.1.3.1] (concept): "The distribution of antigens and antibodies in the four groups of blood, A, B, AB and O are given in Table 15.1."
- **F059** [15.1.3.1] (concept): "during blood transfusion, any blood cannot be used; the blood of a donor has to be carefully matched with the blood of a recipient before any blood transfusion to avoid severe problems of clumping (destruction of RBC)."
- **F060** [15.1.3.1] (concept): "The donor's compatibility is also shown in the Table 15.1."
- **F061** [15.1.3.1] (table): Table title and column heads: "TABLE 15.1 Blood Groups and Donor Compatibility" / "Blood Group" / "Antigens on RBCs" / "Antibodies in Plasma" / "Donor's Group"
- **F062** [15.1.3.1] (table): Table 15.1 row: blood group A - antigens on RBCs A - antibodies in plasma anti-B - donor's group A, O
- **F063** [15.1.3.1] (table): Table 15.1 row: blood group B - antigens on RBCs B - antibodies in plasma anti-A - donor's group B, O
- **F064** [15.1.3.1] (table): Table 15.1 row: blood group AB - antigens on RBCs A, B - antibodies in plasma nil - donor's group AB, A, B, O
- **F065** [15.1.3.1] (table): Table 15.1 row: blood group O - antigens on RBCs nil - antibodies in plasma anti-A, B - donor's group O
- **F066** [15.1.3.1] (concept): "group 'O' blood can be donated to persons with any other blood group and hence 'O' group individuals are called 'universal donors'."
- **F067** [15.1.3.1] (concept): "Persons with 'AB' group can accept blood from persons with AB as well as the other groups of blood. Therefore, such persons are called 'universal recipients'."
- **F068** [15.1.3.2] (heading): "15.1.3.2 Rh grouping"
- **F069** [15.1.3.2] (opener): "Another antigen, the Rh antigen similar to one present in Rhesus monkeys (hence Rh), is also observed on the surface of RBCs of majority (nearly 80 per cent) of humans."
- **F070** [15.1.3.2] (definition): "Such individuals are called Rh positive (Rh+ve) and those in whom this antigen is absent are called Rh negative (Rh-ve)."
- **F071** [15.1.3.2] (concept): FOLDED SUMMARY-UNIQUE (summary sentence S6): "Another blood grouping is also done based on the presence or absence of another antigen called Rhesus factor (Rh) on the surface of RBCs." - the term 'Rhesus factor' appears only in the summary; the body says only 'Rh antigen ... Rhesus monkeys'.
- **F072** [15.1.3.2] (concept): "An Rh-ve person, if exposed to Rh+ve blood, will form specific antibodies against the Rh antigens."
- **F073** [15.1.3.2] (concept): "Therefore, Rh group should also be matched before transfusions."
- **F074** [15.1.3.2] (concept): "A special case of Rh incompatibility (mismatching) has been observed between the Rh-ve blood of a pregnant mother with Rh+ve blood of the foetus."
- **F075** [15.1.3.2] (concept): "Rh antigens of the foetus do not get exposed to the Rh-ve blood of the mother in the first pregnancy as the two bloods are well separated by the placenta."
- **F076** [15.1.3.2] (concept): "However, during the delivery of the first child, there is a possibility of exposure of the maternal blood to small amounts of the Rh+ve blood from the foetus."
- **F077** [15.1.3.2] (concept): "In such cases, the mother starts preparing antibodies against Rh antigen in her blood."
- **F078** [15.1.3.2] (concept): "In case of her subsequent pregnancies, the Rh antibodies from the mother (Rh-ve) can leak into the blood of the foetus (Rh+ve) and destroy the foetal RBCs."
- **F079** [15.1.3.2] (concept): "This could be fatal to the foetus or could cause severe anaemia and jaundice to the baby."
- **F080** [15.1.3.2] (definition): "This condition is called erythroblastosis foetalis."
- **F081** [15.1.3.2] (concept): "This can be avoided by administering anti-Rh antibodies to the mother immediately after the delivery of the first child."
- **F082** [15.1.4] (heading): "15.1.4 Coagulation of Blood"
- **F083** [15.1.4] (opener): "You know that when you cut your finger or hurt yourself, your wound does not continue to bleed for a long time; usually the blood stops flowing after sometime. Do you know why?" (the trailing rhetorical hook was folded into this opener at Gate 3(b) — see the Gate 3(b) record)
- **F084** [15.1.4] (concept): "Blood exhibits coagulation or clotting in response to an injury or trauma."
- **F085** [15.1.4] (concept): "This is a mechanism to prevent excessive loss of blood from the body."
- **F086** [15.1.4] (concept): "You would have observed a dark reddish brown scum formed at the site of a cut or an injury over a period of time."
- **F087** [15.1.4] (definition): "It is a clot or coagulam formed mainly of a network of threads called fibrins in which dead and damaged formed elements of blood are trapped."
- **F088** [15.1.4] (process): "Fibrins are formed by the conversion of inactive fibrinogens in the plasma by the enzyme thrombin."
- **F089** [15.1.4] (process): "Thrombins, in turn are formed from another inactive substance present in the plasma called prothrombin."
- **F090** [15.1.4] (process): "An enzyme complex, thrombokinase, is required for the above reaction."
- **F091** [15.1.4] (process): "This complex is formed by a series of linked enzymic reactions (cascade process) involving a number of factors present in the plasma in an inactive state."
- **F092** [15.1.4] (process): "An injury or a trauma stimulates the platelets in the blood to release certain factors which activate the mechanism of coagulation."
- **F093** [15.1.4] (process): "Certain factors released by the tissues at the site of injury also can initiate coagulation."
- **F094** [15.1.4] (concept): "Calcium ions play a very important role in clotting."
- **F095** [15.2] (heading): "15.2 LYMPH (TISSUE FLUID)"
- **F096** [15.2] (opener): "As the blood passes through the capillaries in tissues, some water along with many small water soluble substances move out into the spaces between the cells of tissues leaving the larger proteins and most of the formed elements in the blood vessels."
- **F097** [15.2] (definition): "This fluid released out is called the interstitial fluid or tissue fluid."
- **F098** [15.2] (concept): "It has the same mineral distribution as that in plasma."
- **F099** [15.2] (concept): "Exchange of nutrients, gases, etc., between the blood and the cells always occur through this fluid."
- **F100** [15.2] (concept): "An elaborate network of vessels called the lymphatic system collects this fluid and drains it back to the major veins."
- **F101** [15.2] (definition): "The fluid present in the lymphatic system is called the lymph."
- **F102** [15.2] (definition): "Lymph is a colourless fluid containing specialised lymphocytes which are responsible for the immune responses of the body."
- **F103** [15.2] (concept): "Lymph is also an important carrier for nutrients, hormones, etc."
- **F104** [15.2] (concept): "Fats are absorbed through lymph in the lacteals present in the intestinal villi."
- **F105** [15.2] (concept): FOLDED SUMMARY-UNIQUE (summary sentence S8): "This fluid called lymph is almost similar to blood except for the protein content and the formed elements." - the explicit lymph-versus-blood contrast is stated only in the summary.
- **F106** [15.3] (heading): "15.3 CIRCULATORY PATHWAYS"
- **F107** [15.3] (opener): "The circulatory patterns are of two types – open or closed."
- **F108** [15.3] (concept): "Open circulatory system is present in arthropods and molluscs in which blood pumped by the heart passes through large vessels into open spaces or body cavities called sinuses."
- **F109** [15.3] (concept): "Annelids and chordates have a closed circulatory system in which the blood pumped by the heart is always circulated through a closed network of blood vessels."
- **F110** [15.3] (concept): "This pattern is considered to be more advantageous as the flow of fluid can be more precisely regulated."
- **F111** [15.3] (concept): FOLDED SUMMARY-UNIQUE (summary sentence S9): "All vertebrates and a few invertebrates have a closed circulatory system." - the body names only annelids and chordates; this vertebrate/invertebrate framing is summary-only.
- **F112** [15.3] (concept): "All vertebrates possess a muscular chambered heart."
- **F113** [15.3] (number): "Fishes have a 2-chambered heart with an atrium and a ventricle."
- **F114** [15.3] (number): "Amphibians and the reptiles (except crocodiles) have a 3-chambered heart with two atria and a single ventricle"
- **F115** [15.3] (number): "whereas crocodiles, birds and mammals possess a 4-chambered heart with two atria and two ventricles."
- **F116** [15.3] (process): "In fishes the heart pumps out deoxygenated blood which is oxygenated by the gills and supplied to the body parts from where deoxygenated blood is returned to the heart (single circulation)."
- **F117** [15.3] (concept): "In amphibians and reptiles, the left atrium receives oxygenated blood from the gills/lungs/skin and the right atrium gets the deoxygenated blood from other body parts."
- **F118** [15.3] (concept): "However, they get mixed up in the single ventricle which pumps out mixed blood (incomplete double circulation)."
- **F119** [15.3] (concept): "In birds and mammals, oxygenated and deoxygenated blood received by the left and right atria respectively passes on to the ventricles of the same sides."
- **F120** [15.3] (concept): "The ventricles pump it out without any mixing up, i.e., two separate circulatory pathways are present in these organisms, hence, these animals have double circulation."
- **F121** [15.3.1] (heading): "15.3.1 Human Circulatory System"
- **F122** [15.3.1] (opener): "Human circulatory system, also called the blood vascular system consists of a muscular chambered heart, a network of closed branching blood vessels and blood, the fluid which is circulated."
- **F123** [15.3.1] (concept): "Heart, the mesodermally derived organ, is situated in the thoracic cavity, in between the two lungs, slightly tilted to the left."
- **F124** [15.3.1] (concept): "It has the size of a clenched fist."
- **F125** [15.3.1] (concept): "It is protected by a double walled membranous bag, pericardium, enclosing the pericardial fluid."
- **F126** [15.3.1] (number): "Our heart has four chambers, two relatively small upper chambers called atria and two larger lower chambers called ventricles."
- **F127** [15.3.1] (concept): "A thin, muscular wall called the inter-atrial septum separates the right and the left atria, whereas a thick-walled, the inter-ventricular septum, separates the left and the right ventricles (Figure 15.2)."
- **F128** [15.3.1] (concept): "The atrium and the ventricle of the same side are also separated by a thick fibrous tissue called the atrio-ventricular septum."
- **F129** [15.3.1] (concept): "However, each of these septa are provided with an opening through which the two chambers of the same side are connected."
- **F130** [15.3.1] (concept): "The opening between the right atrium and the right ventricle is guarded by a valve formed of three muscular flaps or cusps, the tricuspid valve, whereas a bicuspid or mitral valve guards the opening between the left atrium and the left ventricle."
- **F131** [15.3.1] (concept): "The openings of the right and the left ventricles into the pulmonary artery and the aorta respectively are provided with the semilunar valves."
- **F132** [15.3.1] (concept): "The valves in the heart allows the flow of blood only in one direction, i.e., from the atria to the ventricles and from the ventricles to the pulmonary artery or aorta. These valves prevent any backward flow."
- **F133** [15.3.1] (concept): "The entire heart is made of cardiac muscles."
- **F134** [15.3.1] (concept): "The walls of ventricles are much thicker than that of the atria."
- **F135** [15.3.1] (concept): "A specialised cardiac musculature called the nodal tissue is also distributed in the heart (Figure 15.2)."
- **F136** [15.3.1] (concept): "A patch of this tissue is present in the right upper corner of the right atrium called the sino-atrial node (SAN)."
- **F137** [15.3.1] (concept): "Another mass of this tissue is seen in the lower left corner of the right atrium close to the atrio-ventricular septum called the atrio-ventricular node (AVN)."
- **F138** [15.3.1] (concept): "A bundle of nodal fibres, atrio-ventricular bundle (AV bundle) continues from the AVN which passes through the atrio-ventricular septa to emerge on the top of the inter-ventricular septum and immediately divides into a right and left bundle."
- **F139** [15.3.1] (concept): "These branches give rise to minute fibres throughout the ventricular musculature of the respective sides and are called purkinje fibres."
- **F140** [15.3.1] (concept): "The nodal musculature has the ability to generate action potentials without any external stimuli, i.e., it is autoexcitable."
- **F141** [15.3.1] (concept): "However, the number of action potentials that could be generated in a minute vary at different parts of the nodal system."
- **F142** [15.3.1] (number): "The SAN can generate the maximum number of action potentials, i.e., 70-75 min–1, and is responsible for initiating and maintaining the rhythmic contractile activity of the heart. Therefore, it is called the pacemaker."
- **F143** [15.3.1] (number): "Our heart normally beats 70-75 times in a minute (average 72 beats min–1)."
- **F144** [15.3.1] (caption): "Figure 15.2 Section of a human heart"
- **F145** [15.3.2] (heading): "15.3.2 Cardiac Cycle"
- **F146** [15.3.2] (opener): "How does the heart function? Let us take a look."
- **F147** [15.3.2] (process): "To begin with, all the four chambers of heart are in a relaxed state, i.e., they are in joint diastole."
- **F148** [15.3.2] (process): "As the tricuspid and bicuspid valves are open, blood from the pulmonary veins and vena cava flows into the left and the right ventricle respectively through the left and right atria."
- **F149** [15.3.2] (process): "The semilunar valves are closed at this stage."
- **F150** [15.3.2] (process): "The SAN now generates an action potential which stimulates both the atria to undergo a simultaneous contraction – the atrial systole."
- **F151** [15.3.2] (number): "This increases the flow of blood into the ventricles by about 30 per cent."
- **F152** [15.3.2] (process): "The action potential is conducted to the ventricular side by the AVN and AV bundle from where the bundle of His transmits it through the entire ventricular musculature."
- **F153** [15.3.2] (process): "This causes the ventricular muscles to contract, (ventricular systole), the atria undergoes relaxation (diastole), coinciding with the ventricular systole."
- **F154** [15.3.2] (process): "Ventricular systole increases the ventricular pressure causing the closure of tricuspid and bicuspid valves due to attempted backflow of blood into the atria."
- **F155** [15.3.2] (process): "As the ventricular pressure increases further, the semilunar valves guarding the pulmonary artery (right side) and the aorta (left side) are forced open, allowing the blood in the ventricles to flow through these vessels into the circulatory pathways."
- **F156** [15.3.2] (process): "The ventricles now relax (ventricular diastole) and the ventricular pressure falls causing the closure of semilunar valves which prevents the backflow of blood into the ventricles."
- **F157** [15.3.2] (process): "As the ventricular pressure declines further, the tricuspid and bicuspid valves are pushed open by the pressure in the atria exerted by the blood which was being emptied into them by the veins."
- **F158** [15.3.2] (process): "The blood now once again moves freely to the ventricles. The ventricles and atria are now again in a relaxed (joint diastole) state, as earlier."
- **F159** [15.3.2] (process): "Soon the SAN generates a new action potential and the events described above are repeated in that sequence and the process continues."
- **F160** [15.3.2] (definition): "This sequential event in the heart which is cyclically repeated is called the cardiac cycle and it consists of systole and diastole of both the atria and ventricles."
- **F161** [15.3.2] (number): "As mentioned earlier, the heart beats 72 times per minute, i.e., that many cardiac cycles are performed per minute."
- **F162** [15.3.2] (number): "From this it could be deduced that the duration of a cardiac cycle is 0.8 seconds."
- **F163** [15.3.2] (number): "During a cardiac cycle, each ventricle pumps out approximately 70 mL of blood which is called the stroke volume."
- **F164** [15.3.2] (definition): "The stroke volume multiplied by the heart rate (no. of beats per min.) gives the cardiac output."
- **F165** [15.3.2] (definition): "the cardiac output can be defined as the volume of blood pumped out by each ventricle per minute and averages 5000 mL or 5 litres in a healthy individual."
- **F166** [15.3.2] (concept): FOLDED SUMMARY-UNIQUE (summary sentence S18): "About 70 mL of blood is pumped out by each ventricle during a cardiac cycle and it is called the stroke or beat volume." - the synonym 'beat volume' occurs only in the summary.
- **F167** [15.3.2] (concept): "The body has the ability to alter the stroke volume as well as the heart rate and thereby the cardiac output."
- **F168** [15.3.2] (example): "For example, the cardiac output of an athlete will be much higher than that of an ordinary man."
- **F169** [15.3.2] (concept): "During each cardiac cycle two prominent sounds are produced which can be easily heard through a stethoscope."
- **F170** [15.3.2] (concept): "The first heart sound (lub) is associated with the closure of the tricuspid and bicuspid valves whereas the second heart sound (dub) is associated with the closure of the semilunar valves."
- **F171** [15.3.2] (concept): "These sounds are of clinical diagnostic significance."
- **F172** [15.3.3] (heading): "15.3.3 Electrocardiogram (ECG)"
- **F173** [15.3.3] (opener): "You are probably familiar with this scene from a typical hospital television show: A patient is hooked up to a monitoring machine that shows voltage traces on a screen and makes the sound '... pip... pip... pip..... peeeeeeeeeeeeeeeeeeeeee' as the patient goes into cardiac arrest."
- **F174** [15.3.3] (concept): "This type of machine (electro-cardiograph) is used to obtain an electrocardiogram (ECG)."
- **F175** [15.3.3] (definition): "ECG is a graphical representation of the electrical activity of the heart during a cardiac cycle."
- **F176** [15.3.3] (number): "To obtain a standard ECG (as shown in the Figure 15.3), a patient is connected to the machine with three electrical leads (one to each wrist and to the left ankle) that continuously monitor the heart activity."
- **F177** [15.3.3] (concept): "For a detailed evaluation of the heart's function, multiple leads are attached to the chest region."
- **F178** [15.3.3] (concept): "Here, we will talk only about a standard ECG."
- **F179** [15.3.3] (concept): "Each peak in the ECG is identified with a letter from P to T that corresponds to a specific electrical activity of the heart."
- **F180** [15.3.3] (concept): "The P-wave represents the electrical excitation (or depolarisation) of the atria, which leads to the contraction of both the atria."
- **F181** [15.3.3] (concept): "The QRS complex represents the depolarisation of the ventricles, which initiates the ventricular contraction."
- **F182** [15.3.3] (concept): "The contraction starts shortly after Q and marks the beginning of the systole."
- **F183** [15.3.3] (concept): "The T-wave represents the return of the ventricles from excited to normal state (repolarisation)."
- **F184** [15.3.3] (concept): "The end of the T-wave marks the end of systole."
- **F185** [15.3.3] (concept): "Obviously, by counting the number of QRS complexes that occur in a given time period, one can determine the heart beat rate of an individual."
- **F186** [15.3.3] (concept): "Since the ECGs obtained from different individuals have roughly the same shape for a given lead configuration, any deviation from this shape indicates a possible abnormality or disease. Hence, it is of a great clinical significance."
- **F187** [15.3.3] (caption): "Figure 15.3 Diagrammatic presentation of a standard ECG"
- **F188** [15.4] (heading): "15.4 DOUBLE CIRCULATION"
- **F189** [15.4] (opener): "The blood flows strictly by a fixed route through Blood Vessels—the arteries and veins."
- **F190** [15.4] (concept): "Basically, each artery and vein consists of three layers: an inner lining of squamous endothelium, the tunica intima, a middle layer of smooth muscle and elastic fibres, the tunica media, and an external layer of fibrous connective tissue with collagen fibres, the tunica externa."
- **F191** [15.4] (concept): "The tunica media is comparatively thin in the veins (Figure 15.4)."
- **F192** [15.4] (concept): "As mentioned earlier, the blood pumped by the right ventricle enters the pulmonary artery, whereas the left ventricle pumps blood into the aorta."
- **F193** [15.4] (process): "The deoxygenated blood pumped into the pulmonary artery is passed on to the lungs from where the oxygenated blood is carried by the pulmonary veins into the left atrium. This pathway constitutes the pulmonary circulation."
- **F194** [15.4] (process): "The oxygenated blood entering the aorta is carried by a network of arteries, arterioles and capillaries to the tissues from where the deoxygenated blood is collected by a system of venules, veins and vena cava and emptied into the right atrium. This is the systemic circulation (Figure 15.4)."
- **F195** [15.4] (concept): "The systemic circulation provides nutrients, O2 and other essential substances to the tissues and takes CO2 and other harmful substances away for elimination."
- **F196** [15.4] (concept): "A unique vascular connection exists between the digestive tract and liver called hepatic portal system."
- **F197** [15.4] (concept): "The hepatic portal vein carries blood from intestine to the liver before it is delivered to the systemic circulation."
- **F198** [15.4] (concept): "A special coronary system of blood vessels is present in our body exclusively for the circulation of blood to and from the cardiac musculature."
- **F199** [15.4] (concept): FOLDED SUMMARY-UNIQUE (summary sentence S21): "We have a complete double circulation, i.e., two circulatory pathways, namely, pulmonary and systemic are present." - the qualifier 'complete' for the human pattern is stated only in the summary.
- **F200** [15.4] (caption): "Figure 15.4 Schematic plan of blood circulation in human"
- **F201** [15.5] (heading): "15.5 REGULATION OF CARDIAC ACTIVITY"
- **F202** [15.5] (opener): "Normal activities of the heart are regulated intrinsically, i.e., auto regulated by specialised muscles (nodal tissue), hence the heart is called myogenic."
- **F203** [15.5] (concept): "A special neural centre in the medulla oblangata can moderate the cardiac function through autonomic nervous system (ANS)."
- **F204** [15.5] (concept): "Neural signals through the sympathetic nerves (part of ANS) can increase the rate of heart beat, the strength of ventricular contraction and thereby the cardiac output."
- **F205** [15.5] (concept): "On the other hand, parasympathetic neural signals (another component of ANS) decrease the rate of heart beat, speed of conduction of action potential and thereby the cardiac output."
- **F206** [15.5] (concept): "Adrenal medullary hormones can also increase the cardiac output."
- **F207** [15.6] (heading): "15.6 DISORDERS OF CIRCULATORY SYSTEM"
- **F208** [15.6] (heading): Unnumbered run-in heading: "High Blood Pressure (Hypertension):"
- **F209** [15.6] (opener): "Hypertension is the term for blood pressure that is higher than normal (120/80)."
- **F210** [15.6] (number): "In this measurement 120 mm Hg (millimetres of mercury pressure) is the systolic, or pumping, pressure and 80 mm Hg is the diastolic, or resting, pressure."
- **F211** [15.6] (number): "If repeated checks of blood pressure of an individual is 140/90 (140 over 90) or higher, it shows hypertension."
- **F212** [15.6] (concept): "High blood pressure leads to heart diseases and also affects vital organs like brain and kidney."
- **F213** [15.6] (heading): Unnumbered run-in heading: "Coronary Artery Disease (CAD):"
- **F214** [15.6] (opener): "Coronary Artery Disease, often referred to as atherosclerosis, affects the vessels that supply blood to the heart muscle."
- **F215** [15.6] (concept): "It is caused by deposits of calcium, fat, cholesterol and fibrous tissues, which makes the lumen of arteries narrower."
- **F216** [15.6] (heading): Unnumbered run-in heading: "Angina:"
- **F217** [15.6] (opener): "It is also called 'angina pectoris'."
- **F218** [15.6] (concept): "A symptom of acute chest pain appears when no enough oxygen is reaching the heart muscle."
- **F219** [15.6] (concept): "Angina can occur in men and women of any age but it is more common among the middle-aged and elderly."
- **F220** [15.6] (concept): "It occurs due to conditions that affect the blood flow."
- **F221** [15.6] (heading): Unnumbered run-in heading: "Heart Failure:"
- **F222** [15.6] (opener): "Heart failure means the state of heart when it is not pumping blood effectively enough to meet the needs of the body."
- **F223** [15.6] (concept): "It is sometimes called congestive heart failure because congestion of the lungs is one of the main symptoms of this disease."
- **F224** [15.6] (concept): "Heart failure is not the same as cardiac arrest (when the heart stops beating) or a heart attack (when the heart muscle is suddenly damaged by an inadequate blood supply)."
- **F225** [summary] (heading): Unnumbered heading: "SUMMARY"
- **F226** [summary] (opener): "Vertebrates circulate blood, a fluid connective tissue, in their body, to transport essential substances to the cells and to carry waste substances from there."
- **F227** [exercises] (heading): Unnumbered heading: "EXERCISES" (no opening sentence of its own)
- **F228** [exercises] (question): Exercise 1: "Name the components of the formed elements in the blood and mention one major function of each of them."
- **F229** [exercises] (question): Exercise 2: "What is the importance of plasma proteins?"
- **F230** [exercises] (question): Exercise 3: "Match Column I with Column II" - Column I (a) Eosinophils (b) RBC (c) AB Group (d) Platelets (e) Systole; Column II (i) Coagulation (ii) Universal Recipient (iii) Resist Infections (iv) Contraction of Heart (v) Gas transport
- **F231** [exercises] (question): Exercise 4: "Why do we consider blood as a connective tissue?"
- **F232** [exercises] (question): Exercise 5: "What is the difference between lymph and blood?"
- **F233** [exercises] (question): Exercise 6: "What is meant by double circulation? What is its significance?"
- **F234** [exercises] (question): Exercise 7: "Write the differences between :" (a) Blood and Lymph (b) Open and Closed system of circulation (c) Systole and Diastole (d) P-wave and T-wave
- **F235** [exercises] (question): Exercise 8: "Describe the evolutionary change in the pattern of heart among the vertebrates."
- **F236** [exercises] (question): Exercise 9: "Why do we call our heart myogenic?"
- **F237** [exercises] (question): Exercise 10: "Sino-atrial node is called the pacemaker of our heart. Why?"
- **F238** [exercises] (question): Exercise 11: "What is the significance of atrio-ventricular node and atrio-ventricular bundle in the functioning of heart?"
- **F239** [exercises] (question): Exercise 12: "Define a cardiac cycle and the cardiac output."
- **F240** [exercises] (question): Exercise 13: "Explain heart sounds."
- **F241** [exercises] (question): Exercise 14: "Draw a standard ECG and explain the different segments in it."

### BRIDGE CHAPTER — Class 11, Ch16_ExcretoryProductsAndTheirElimination (Excretory Products And Their Elimination) — cite these as `ExcretoryProductsAndTheirElimination:F###` — 172 supplied source facts (frozen inventory rows)
- **F001** [title] (heading): Chapter title plate: 'EXCRETORY PRODUCTS AND THEIR ELIMINATION' with 'CHAPTER 16' (no opening sentence of its own)
- **F002** [intro] (opener): "Animals accumulate ammonia, urea, uric acid, carbon dioxide, water and ions like Na+, K+, Cl-, phosphate, sulphate, etc., either by metabolic activities or by other means like excess ingestion."
- **F003** [intro] (concept): "These substances have to be removed totally or partially."
- **F004** [intro] (concept): "In this chapter, you will learn the mechanisms of elimination of these substances with special emphasis on common nitrogenous wastes."
- **F005** [intro] (concept): "Ammonia, urea and uric acid are the major forms of nitrogenous wastes excreted by the animals."
- **F006** [intro] (concept): "Ammonia is the most toxic form and requires large amount of water for its elimination, whereas uric acid, being the least toxic, can be removed with a minimum loss of water."
- **F007** [intro] (definition): "The process of excreting ammonia is Ammonotelism."
- **F008** [intro] (example): "Many bony fishes, aquatic amphibians and aquatic insects are ammonotelic in nature." (source sets "ammonotelic" five times over-struck as a bold artefact)
- **F009** [intro] (concept): "Ammonia, as it is readily soluble, is generally excreted by diffusion across body surfaces or through gill surfaces (in fish) as ammonium ions."
- **F010** [intro] (concept): "Kidneys do not play any significant role in its removal."
- **F011** [intro] (concept): "Terrestrial adaptation necessitated the production of lesser toxic nitrogenous wastes like urea and uric acid for conservation of water."
- **F012** [intro] (example): "Mammals, many terrestrial amphibians and marine fishes mainly excrete urea and are called ureotelic animals." (source sets "ureotelic" five times over-struck)
- **F013** [intro] (process): "Ammonia produced by metabolism is converted into urea in the liver of these animals and released into the blood which is filtered and excreted out by the kidneys."
- **F014** [intro] (concept): "Some amount of urea may be retained in the kidney matrix of some of these animals to maintain a desired osmolarity."
- **F015** [intro] (example): "Reptiles, birds, land snails and insects excrete nitrogenous wastes as uric acid in the form of pellet or paste with a minimum loss of water and are called uricotelic animals." (source sets "uricotelic" five times over-struck)
- **F016** [intro] (list): Chapter contents panel (p. 205 margin), title-case in the source: "16.1 Human Excretory System"; "16.2 Urine Formation"; "16.3 Function of the Tubules"; "16.4 Mechanism of Concentration of the Filtrate"; "16.5 Regulation of Kidney Function"; "16.6 Micturition"; "16.7 Role of other Organs in Excretion"; "16.8 Disorders of the Excretory System"
- **F017** [intro] (concept): "A survey of animal kingdom presents a variety of excretory structures."
- **F018** [intro] (concept): "In most of the invertebrates, these structures are simple tubular forms whereas vertebrates have complex tubular organs called kidneys."
- **F019** [intro] (concept): "Some of these structures are mentioned here."
- **F020** [intro] (example): "Protonephridia or flame cells are the excretory structures in Platyhelminthes (Flatworms, e.g., Planaria), rotifers, some annelids and the cephalochordate - Amphioxus."
- **F021** [intro] (concept): "Protonephridia are primarily concerned with ionic and fluid volume regulation, i.e., osmoregulation."
- **F022** [intro] (example): "Nephridia are the tubular excretory structures of earthworms and other annelids."
- **F023** [intro] (concept): "Nephridia help to remove nitrogenous wastes and maintain a fluid and ionic balance."
- **F024** [intro] (example): "Malpighian tubules are the excretory structures of most of the insects including cockroaches."
- **F025** [intro] (concept): "Malpighian tubules help in the removal of nitrogenous wastes and osmoregulation."
- **F026** [intro] (example): "Antennal glands or green glands perform the excretory function in crustaceans like prawns."
- **F027** [16.1] (heading): "16.1 HUMAN EXCRETORY SYSTEM"
- **F028** [16.1] (opener): "In humans, the excretory system consists of a pair of kidneys, one pair of ureters, a urinary bladder and a urethra (Figure 16.1)."
- **F029** [16.1] (concept): "Kidneys are reddish brown, bean shaped structures situated between the levels of last thoracic and third lumbar vertebra close to the dorsal inner wall of the abdominal cavity."
- **F030** [16.1] (number): "Each kidney of an adult human measures 10-12 cm in length, 5-7 cm in width, 2-3 cm in thickness with an average weight of 120-170 g."
- **F031** [16.1] (concept): "Towards the centre of the inner concave surface of the kidney is a notch called hilum through which ureter, blood vessels and nerves enter."
- **F032** [16.1] (concept): "Inner to the hilum is a broad funnel shaped space called the renal pelvis with projections called calyces."
- **F033** [16.1] (concept): "The outer layer of kidney is a tough capsule."
- **F034** [16.1] (concept): "Inside the kidney, there are two zones, an outer cortex and an inner medulla."
- **F035** [16.1] (concept): "The medulla is divided into a few conical masses (medullary pyramids) projecting into the calyces (sing.: calyx)."
- **F036** [16.1] (concept): "The cortex extends in between the medullary pyramids as renal columns called Columns of Bertini."
- **F037** [16.1] (number): "Each kidney has nearly one million complex tubular structures called nephrons (Figure 16.3), which are the functional units."
- **F038** [16.1] (concept): "Each nephron has two parts - the glomerulus and the renal tubule."
- **F039** [16.1] (definition): "Glomerulus is a tuft of capillaries formed by the afferent arteriole - a fine branch of renal artery."
- **F040** [16.1] (concept): "Blood from the glomerulus is carried away by an efferent arteriole."
- **F041** [16.1] (concept): "The renal tubule begins with a double walled cup-like structure called Bowman's capsule, which encloses the glomerulus."
- **F042** [16.1] (definition): "Glomerulus along with Bowman's capsule, is called the malpighian body or renal corpuscle (Figure 16.4)."
- **F043** [16.1] (concept): "The tubule continues further to form a highly coiled network - proximal convoluted tubule (PCT)."
- **F044** [16.1] (concept): "A hairpin shaped Henle's loop is the next part of the tubule which has a descending and an ascending limb."
- **F045** [16.1] (concept): "The ascending limb continues as another highly coiled tubular region called distal convoluted tubule (DCT)."
- **F046** [16.1] (concept): "The DCTs of many nephrons open into a straight tube called collecting duct, many of which converge and open into the renal pelvis through medullary pyramids in the calyces."
- **F047** [16.1] (concept): "The Malpighian corpuscle, PCT and DCT of the nephron are situated in the cortical region of the kidney whereas the loop of Henle dips into the medulla."
- **F048** [16.1] (definition): "In majority of nephrons, the loop of Henle is too short and extends only very little into the medulla. Such nephrons are called cortical nephrons."
- **F049** [16.1] (definition): "In some of the nephrons, the loop of Henle is very long and runs deep into the medulla. These nephrons are called juxta medullary nephrons."
- **F050** [16.1] (concept): "The efferent arteriole emerging from the glomerulus forms a fine capillary network around the renal tubule called the peritubular capillaries."
- **F051** [16.1] (concept): "A minute vessel of this network runs parallel to the Henle's loop forming a 'U' shaped vasa recta."
- **F052** [16.1] (concept): "Vasa recta is absent or highly reduced in cortical nephrons."
- **F053** [16.2] (heading): "16.2 URINE FORMATION"
- **F054** [16.2] (opener): "Urine formation involves three main processes namely, glomerular filtration, reabsorption and secretion, that takes place in different parts of the nephron."
- **F055** [16.2] (process): "The first step in urine formation is the filtration of blood, which is carried out by the glomerulus and is called glomerular filtration."
- **F056** [16.2] (number): "On an average, 1100-1200 ml of blood is filtered by the kidneys per minute which constitute roughly 1/5th of the blood pumped out by each ventricle of the heart in a minute."
- **F057** [16.2] (number): "The glomerular capillary blood pressure causes filtration of blood through 3 layers, i.e., the endothelium of glomerular blood vessels, the epithelium of Bowman's capsule and a basement membrane between these two layers."
- **F058** [16.2] (concept): "The epithelial cells of Bowman's capsule called podocytes are arranged in an intricate manner so as to leave some minute spaces called filtration slits or slit pores."
- **F059** [16.2] (concept): "Blood is filtered so finely through these membranes, that almost all the constituents of the plasma except the proteins pass onto the lumen of the Bowman's capsule."
- **F060** [16.2] (definition): "Therefore, it is considered as a process of ultra filtration."
- **F061** [16.2] (definition): "The amount of the filtrate formed by the kidneys per minute is called glomerular filtration rate (GFR)."
- **F062** [16.2] (number): "GFR in a healthy individual is approximately 125 ml/minute, i.e., 180 litres per day !"
- **F063** [16.2] (concept): "The kidneys have built-in mechanisms for the regulation of glomerular filtration rate."
- **F064** [16.2] (concept): "One such efficient mechanism is carried out by juxta glomerular apparatus (JGA)."
- **F065** [16.2] (definition): "JGA is a special sensitive region formed by cellular modifications in the distal convoluted tubule and the afferent arteriole at the location of their contact."
- **F066** [16.2] (process): "A fall in GFR can activate the JG cells to release renin which can stimulate the glomerular blood flow and thereby the GFR back to normal."
- **F067** [16.2] (number): "A comparison of the volume of the filtrate formed per day (180 litres per day) with that of the urine released (1.5 litres), suggest that nearly 99 per cent of the filtrate has to be reabsorbed by the renal tubules."
- **F068** [16.2] (definition): "This process is called reabsorption."
- **F069** [16.2] (concept): "The tubular epithelial cells in different segments of nephron perform this either by active or passive mechanisms."
- **F070** [16.2] (example): "For example, substances like glucose, amino acids, Na+, etc., in the filtrate are reabsorbed actively whereas the nitrogenous wastes are absorbed by passive transport."
- **F071** [16.2] (concept): "Reabsorption of water also occurs passively in the initial segments of the nephron (Figure 16.5)."
- **F072** [16.2] (process): "During urine formation, the tubular cells secrete substances like H+, K+ and ammonia into the filtrate."
- **F073** [16.2] (concept): "Tubular secretion is also an important step in urine formation as it helps in the maintenance of ionic and acid base balance of body fluids."
- **F074** [16.3] (heading): "16.3 FUNCTION OF THE TUBULES"
- **F075** [16.3] (heading): Run-in head, bold, colon-terminated: "Proximal Convoluted Tubule (PCT):"
- **F076** [16.3] (opener): "PCT is lined by simple cuboidal brush border epithelium which increases the surface area for reabsorption."
- **F077** [16.3] (number): "Nearly all of the essential nutrients, and 70-80 per cent of electrolytes and water are reabsorbed by this segment."
- **F078** [16.3] (concept): "PCT also helps to maintain the pH and ionic balance of the body fluids by selective secretion of hydrogen ions and ammonia into the filtrate and by absorption of HCO3- from it."
- **F079** [16.3] (heading): Run-in head, bold, colon-terminated: "Henle's Loop:"
- **F080** [16.3] (opener): "Reabsorption is minimum in its ascending limb."
- **F081** [16.3] (concept): "However, this region plays a significant role in the maintenance of high osmolarity of medullary interstitial fluid."
- **F082** [16.3] (concept): "The descending limb of loop of Henle is permeable to water but almost impermeable to electrolytes."
- **F083** [16.3] (concept): "This concentrates the filtrate as it moves down."
- **F084** [16.3] (concept): "The ascending limb is impermeable to water but allows transport of electrolytes actively or passively."
- **F085** [16.3] (concept): "Therefore, as the concentrated filtrate pass upward, it gets diluted due to the passage of electrolytes to the medullary fluid."
- **F086** [16.3] (heading): Run-in head, bold, colon-terminated: "Distal Convoluted Tubule (DCT):"
- **F087** [16.3] (opener): "Conditional reabsorption of Na+ and water takes place in this segment."
- **F088** [16.3] (concept): "DCT is also capable of reabsorption of HCO3- and selective secretion of hydrogen and potassium ions and NH3 to maintain the pH and sodium-potassium balance in blood."
- **F089** [16.3] (heading): Run-in head, bold, colon-terminated: "Collecting Duct:"
- **F090** [16.3] (opener): "This long duct extends from the cortex of the kidney to the inner parts of the medulla."
- **F091** [16.3] (concept): "Large amounts of water could be reabsorbed from this region to produce a concentrated urine."
- **F092** [16.3] (concept): "This segment allows passage of small amounts of urea into the medullary interstitium to keep up the osmolarity."
- **F093** [16.3] (concept): "It also plays a role in the maintenance of pH and ionic balance of blood by the selective secretion of H+ and K+ ions (Figure 16.5)."
- **F094** [16.4] (heading): "16.4 MECHANISM OF CONCENTRATION OF THE FILTRATE" (the p. 209 running head sets this as "ofthe Filtrate", a source typo)
- **F095** [16.4] (opener): "Mammals have the ability to produce a concentrated urine."
- **F096** [16.4] (concept): "The Henle's loop and vasa recta play a significant role in this."
- **F097** [16.4] (concept): "The flow of filtrate in the two limbs of Henle's loop is in opposite directions and thus forms a counter current."
- **F098** [16.4] (concept): "The flow of blood through the two limbs of vasa recta is also in a counter current pattern."
- **F099** [16.4] (number): "The proximity between the Henle's loop and vasa recta, as well as the counter current in them help in maintaining an increasing osmolarity towards the inner medullary interstitium, i.e., from 300 mOsmolL-1 in the cortex to about 1200 mOsmolL-1 in the inner medulla."
- **F100** [16.4] (concept): "This gradient is mainly caused by NaCl and urea."
- **F101** [16.4] (process): "NaCl is transported by the ascending limb of Henle's loop which is exchanged with the descending limb of vasa recta."
- **F102** [16.4] (process): "NaCl is returned to the interstitium by the ascending portion of vasa recta."
- **F103** [16.4] (process): "Similarly, small amounts of urea enter the thin segment of the ascending limb of Henle's loop which is transported back to the interstitium by the collecting tubule."
- **F104** [16.4] (definition): "The above described transport of substances facilitated by the special arrangement of Henle's loop and vasa recta is called the counter current mechanism (Figure. 16.6)." (source prints a stray period after "Figure")
- **F105** [16.4] (concept): "This mechanism helps to maintain a concentration gradient in the medullary interstitium."
- **F106** [16.4] (concept): "Presence of such interstitial gradient helps in an easy passage of water from the collecting tubule thereby concentrating the filtrate (urine)."
- **F107** [16.4] (number): "Human kidneys can produce urine nearly four times concentrated than the initial filtrate formed."
- **F108** [16.5] (heading): "16.5 REGULATION OF KIDNEY FUNCTION"
- **F109** [16.5] (opener): "The functioning of the kidneys is efficiently monitored and regulated by hormonal feedback mechanisms involving the hypothalamus, JGA and to a certain extent, the heart."
- **F110** [16.5] (concept): "Osmoreceptors in the body are activated by changes in blood volume, body fluid volume and ionic concentration."
- **F111** [16.5] (process): "An excessive loss of fluid from the body can activate these receptors which stimulate the hypothalamus to release antidiuretic hormone (ADH) or vasopressin from the neurohypophysis."
- **F112** [16.5] (concept): "ADH facilitates water reabsorption from latter parts of the tubule, thereby preventing diuresis."
- **F113** [16.5] (process): "An increase in body fluid volume can switch off the osmoreceptors and suppress the ADH release to complete the feedback."
- **F114** [16.5] (concept): "ADH can also affect the kidney function by its constrictory effects on blood vessels."
- **F115** [16.5] (concept): "This causes an increase in blood pressure."
- **F116** [16.5] (concept): "An increase in blood pressure can increase the glomerular blood flow and thereby the GFR."
- **F117** [16.5] (concept): "The JGA plays a complex regulatory role."
- **F118** [16.5] (process): "A fall in glomerular blood flow/glomerular blood pressure/GFR can activate the JG cells to release renin which converts angiotensinogen in blood to angiotensin I and further to angiotensin II."
- **F119** [16.5] (concept): "Angiotensin II, being a powerful vasoconstrictor, increases the glomerular blood pressure and thereby GFR."
- **F120** [16.5] (process): "Angiotensin II also activates the adrenal cortex to release Aldosterone."
- **F121** [16.5] (concept): "Aldosterone causes reabsorption of Na+ and water from the distal parts of the tubule."
- **F122** [16.5] (concept): "This also leads to an increase in blood pressure and GFR."
- **F123** [16.5] (definition): "This complex mechanism is generally known as the Renin-Angiotensin mechanism."
- **F124** [16.5] (process): "An increase in blood flow to the atria of the heart can cause the release of Atrial Natriuretic Factor (ANF)."
- **F125** [16.5] (concept): "ANF can cause vasodilation (dilation of blood vessels) and thereby decrease the blood pressure."
- **F126** [16.5] (concept): "ANF mechanism, therefore, acts as a check on the renin-angiotensin mechanism."
- **F127** [16.6] (heading): "16.6 MICTURITION"
- **F128** [16.6] (opener): "Urine formed by the nephrons is ultimately carried to the urinary bladder where it is stored till a voluntary signal is given by the central nervous system (CNS)."
- **F129** [16.6] (process): "This signal is initiated by the stretching of the urinary bladder as it gets filled with urine."
- **F130** [16.6] (process): "In response, the stretch receptors on the walls of the bladder send signals to the CNS."
- **F131** [16.6] (process): "The CNS passes on motor messages to initiate the contraction of smooth muscles of the bladder and simultaneous relaxation of the urethral sphincter causing the release of urine."
- **F132** [16.6] (definition): "The process of release of urine is called micturition and the neural mechanisms causing it is called the micturition reflex."
- **F133** [16.6] (number): "An adult human excretes, on an average, 1 to 1.5 litres of urine per day."
- **F134** [16.6] (number): "The urine formed is a light yellow coloured watery fluid which is slightly acidic (pH-6.0) and has a characterestic odour." (source spells "characterestic")
- **F135** [16.6] (number): "On an average, 25-30 gm of urea is excreted out per day."
- **F136** [16.6] (concept): "Various conditions can affect the characteristics of urine."
- **F137** [16.6] (concept): "Analysis of urine helps in clinical diagnosis of many metabolic discorders as well as malfunctioning of the kidney." (source spells "discorders")
- **F138** [16.6] (example): "For example, presence of glucose (Glycosuria) and ketone bodies (Ketonuria) in urine are indicative of diabetes mellitus."
- **F139** [16.7] (heading): "16.7 ROLE OF OTHER ORGANS IN EXCRETION"
- **F140** [16.7] (opener): "Other than the kidneys, lungs, liver and skin also help in the elimination of excretory wastes."
- **F141** [16.7] (number): "Our lungs remove large amounts of CO2 (approximately 200mL/minute) and also significant quantities of water every day."
- **F142** [16.7] (concept): "Liver, the largest gland in our body, secretes bile-containing substances like bilirubin, biliverdin, cholesterol, degraded steroid hormones, vitamins and drugs."
- **F143** [16.7] (concept): "Most of these substances ultimately pass out along with digestive wastes."
- **F144** [16.7] (concept): "The sweat and sebaceous glands in the skin can eliminate certain substances through their secretions."
- **F145** [16.7] (concept): "Sweat produced by the sweat glands is a watery fluid containing NaCl, small amounts of urea, lactic acid, etc."
- **F146** [16.7] (concept): "Though the primary function of sweat is to facilitate a cooling effect on the body surface, it also helps in the removal of some of the wastes mentioned above."
- **F147** [16.7] (concept): "Sebaceous glands eliminate certain substances like sterols, hydrocarbons and waxes through sebum."
- **F148** [16.7] (concept): "This secretion provides a protective oily covering for the skin."
- **F149** [16.7] (question): "Do you know that small amounts of nitrogenous wastes could be eliminated through saliva too?"
- **F150** [16.8] (heading): "16.8 DISORDERS OF THE EXCRETORY SYSTEM"
- **F151** [16.8] (opener): "Malfunctioning of kidneys can lead to accumulation of urea in blood, a condition called uremia, which is highly harmful and may lead to kidney failure."
- **F152** [16.8] (concept): "In such patients, urea can be removed by a process called hemodialysis."
- **F153** [16.8] (process): "During the process of haemodialysis, the blood drained from a convenient artery is pumped into a dialysing unit called artificial kidney."
- **F154** [16.8] (process): "Blood drained from a convenient artery is pumped into a dialysing unit after adding an anticoagulant like heparin."
- **F155** [16.8] (concept): "The unit contains a coiled cellophane tube surrounded by a fluid (dialysing fluid) having the same composition as that of plasma except the nitrogenous wastes."
- **F156** [16.8] (concept): "The porous cellophane membrance of the tube allows the passage of molecules based on concentration gradient." (source spells "membrance")
- **F157** [16.8] (process): "As nitrogenous wastes are absent in the dialysing fluid, these substances freely move out, thereby clearing the blood."
- **F158** [16.8] (process): "The cleared blood is pumped back to the body through a vein after adding anti-heparin to it."
- **F159** [16.8] (concept): "This method is a boon for thousands of uremic patients all over the world."
- **F160** [16.8] (concept): "Kidney transplantation is the ultimate method in the correction of acute renal failures (kidney failure)."
- **F161** [16.8] (concept): "A functioning kidney is used in transplantation from a donor, preferably a close relative, to minimise its chances of rejection by the immune system of the host."
- **F162** [16.8] (concept): "Modern clinical procedures have increased the success rate of such a complicated technique."
- **F163** [16.8] (disorder): "Renal calculi: Stone or insoluble mass of crystallised salts (oxalates, etc.) formed within the kidney."
- **F164** [16.8] (disorder): "Glomerulonephritis: Inflammation of glomeruli of kidney."
- **F165** [figures] (caption): "Figure 16.1 Human Urinary system"
- **F166** [figures] (caption): "Figure 16.2 Longitudinal section (Diagrammatic) of Kidney"
- **F167** [figures] (caption): "Figure 16.3 A diagrammatic representation of a nephron showing blood vessels, duct and tubules"
- **F168** [figures] (caption): "Figure 16.4 Malpighian body (renal corpuscle)"
- **F169** [figures] (caption): "Figure 16.5 Reabsorption and secretion of major substances at different parts of the nephron (Arrows indicate direction of movement of materials.)"
- **F170** [figures] (caption): "Figure 16.6 Diagrammatic representation of a nephron and vasa recta showing counter current mechanisms" (caption sets "mechanisms" plural)
- **F171** [summary] (heading): "SUMMARY"
- **F172** [exercises] (heading): "EXERCISES"

### BRIDGE CHAPTER — Class 11, Ch3_PlantKingdom (Plant Kingdom) — cite these as `PlantKingdom:F###` — 215 supplied source facts (frozen inventory rows)
- **F001** [3.0] (fact): "In the previous chapter, we looked at the broad classification of living organisms under the system proposed by Whittaker (1969) wherein he suggested the Five Kingdom classification viz. Monera, Protista, Fungi, Animalia and Plantae."
- **F002** [3.0] (scientist/date): Whittaker (1969) — the Five Kingdom classification is credited to him with this date.
- **F003** [3.0] (fact): "In this chapter, we will deal in detail with further classification within Kingdom Plantae popularly known as the 'plant kingdom'."
- **F004** [3.0] (fact): "We must stress here that our understanding of the plant kingdom has changed over time."
- **F005** [3.0] (exception): "Fungi, and members of the Monera and Protista having cell walls have now been excluded from Plantae though earlier classifications placed them in the same kingdom."
- **F006** [3.0] (exception): "So, the cyanobacteria that are also referred to as blue green algae are not 'algae' any more."
- **F007** [3.0] (fact): "In this chapter, we will describe Algae, Bryophytes, Pteridophytes, Gymnosperms and Angiosperms under Plantae."
- **F008** [3.0] (fact): "Let us also look at classification within angiosperms to understand some of the concerns that influenced the classification systems."
- **F009** [3.0] (fact): "The earliest systems of classification used only gross superficial morphological characters such as habit, colour, number and shape of leaves, etc."
- **F010** [3.0] (fact): Earliest systems "were based mainly on vegetative characters or on the androecium structure (system given by Linnaeus)."
- **F011** [3.0] (scientist): Linnaeus — credited with the classification system based on androecium structure.
- **F012** [3.0] (fact): "Such systems were artificial; they separated the closely related species since they were based on a few characteristics."
- **F013** [3.0] (fact): "Also, the artificial systems gave equal weightage to vegetative and sexual characteristics; this is not acceptable since we know that often the vegetative characters are more easily affected by environment."
- **F014** [3.0] (fact): "As against this, natural classification systems developed, which were based on natural affinities among the organisms and consider, not only the external features, but also internal features, like ultra-structure, anatomy, embryology and phytochemistry."
- **F015** [3.0] (scientist): "Such a classification for flowering plants was given by George Bentham and Joseph Dalton Hooker."
- **F016** [3.0] (fact): "At present phylogenetic classification systems based on evolutionary relationships between the various organisms are acceptable."
- **F017** [3.0] (fact): Phylogenetic classification "assumes that organisms belonging to the same taxa have a common ancestor."
- **F018** [3.0] (fact): "We now use information from many other sources too to help resolve difficulties in classification. These become more important when there is no supporting fossil evidence."
- **F019** [3.0] (definition): "Numerical Taxonomy which is now easily carried out using computers is based on all observable characteristics."
- **F020** [3.0] (process): In Numerical Taxonomy "Number and codes are assigned to all the characters and the data are then processed."
- **F021** [3.0] (fact): "In this way each character is given equal importance and at the same time hundreds of characters can be considered."
- **F022** [3.0] (definition): "Cytotaxonomy, that is based on cytological information like chromosome number, structure, behaviour"
- **F023** [3.0] (definition): "chemotaxonomy, that uses the chemical constituents of the plant to resolve confusions, are also used by taxonomists these days."
- **F024** [3.1] (definition): "Algae are chlorophyll-bearing, simple, thalloid, autotrophic and largely aquatic (both fresh water and marine) organisms."
- **F025** [3.1] (fact): Algae "occur in a variety of other habitats: moist stones, soils and wood."
- **F026** [3.1] (example): "Some of them also occur in association with fungi (lichen) and animals (e.g., on sloth bear)."
- **F027** [3.1] (fact): "The form and size of algae is highly variable, ranging from colonial forms like Volvox and the filamentous forms like Ulothrix and Spirogyra (Figure 3.1)."
- **F028** [3.1] (example): "A few of the marine forms such as kelps, form massive plant bodies."
- **F029** [3.1] (fact): "The algae reproduce by vegetative, asexual and sexual methods."
- **F030** [3.1] (process): "Vegetative reproduction is by fragmentation. Each fragment develops into a thallus."
- **F031** [3.1] (process): "Asexual reproduction is by the production of different types of spores, the most common being the zoospores."
- **F032** [3.1] (fact): Zoospores "are flagellated (motile) and on germination gives rise to new plants."
- **F033** [3.1] (process): "Sexual reproduction takes place through fusion of two gametes."
- **F034** [3.1] (definition): Gametes "can be flagellated and similar in size (as in Ulothrix) or non-flagellated (non-motile) but similar in size (as in Spirogyra). Such reproduction is called isogamous."
- **F035** [3.1] (definition): "Fusion of two gametes dissimilar in size, as in species of Eudorina is termed as anisogamous."
- **F036** [3.1] (definition): "Fusion between one large, non-motile (static) female gamete and a smaller, motile male gamete is termed oogamous, e.g., Volvox, Fucus."
- **F037** [3.1] (fact): "Algae are useful to man in a variety of ways."
- **F038** [3.1] (number): "At least a half of the total carbon dioxide fixation on earth is carried out by algae through photosynthesis."
- **F039** [3.1] (fact): "Being photosynthetic, they increase the level of dissolved oxygen in their immediate environment."
- **F040** [3.1] (fact): Algae "are of paramount importance as primary producers of energy-rich compounds which form the basis of the food cycles of all aquatic animals."
- **F041** [3.1] (number/example): "Many species of Porphyra, Laminaria and Sargassum are among the 70 species of marine algae used as food."
- **F042** [3.1] (example): "Certain marine brown and red algae produce large amounts of hydrocolloids (water holding substances), e.g., algin (brown algae) and carrageen (red algae) which are used commercially."
- **F043** [3.1] (example): "Agar, one of the commercial products obtained from Gelidium and Gracilaria are used to grow microbes and in preparations of ice-creams and jellies."
- **F044** [3.1] (example): "Chlorella, a unicellular alga rich in proteins, is used as food supplement even by space travellers."
- **F045** [3.1] (fact): "The algae are divided into three main classes: Chlorophyceae, Phaeophyceae and Rhodophyceae."
- **F046** [3.1.1] (fact): "The members of chlorophyceae are commonly called green algae."
- **F047** [3.1.1] (fact): Green algae: "The plant body may be unicellular, colonial or filamentous."
- **F048** [3.1.1] (fact): "They are usually grass green due to the dominance of pigments chlorophyll a and b."
- **F049** [3.1.1] (fact): "The pigments are localised in definite chloroplasts."
- **F050** [3.1.1] (fact): "The chloroplasts may be discoid, plate-like, reticulate, cup-shaped, spiral or ribbon-shaped in different species."
- **F051** [3.1.1] (definition): "Most of the members have one or more storage bodies called pyrenoids located in the chloroplasts."
- **F052** [3.1.1] (fact): "Pyrenoids contain protein besides starch."
- **F053** [3.1.1] (fact): "Some algae may store food in the form of oil droplets."
- **F054** [3.1.1] (fact): "Green algae usually have a rigid cell wall made of an inner layer of cellulose and an outer layer of pectose."
- **F055** [3.1.1] (process): Chlorophyceae: "Vegetative reproduction usually takes place by fragmentation."
- **F056** [3.1.1] (process): Chlorophyceae: "Asexual reproduction is by flagellated zoospores produced in zoosporangia."
- **F057** [3.1.1] (process): Chlorophyceae: "The sexual reproduction shows considerable variation in the type and formation of sex cells and it may be isogamous, anisogamous or oogamous."
- **F058** [3.1.1] (example): "Some commonly found green algae are: Chlamydomonas, Volvox, Ulothrix, Spirogyra and Chara (Figure 3.1a)."
- **F059** [3.1.2] (fact): "The members of phaeophyceae or brown algae are found primarily in marine habitats."
- **F060** [3.1.2] (fact): Brown algae "show great variation in size and form."
- **F061** [3.1.2] (number/example): "They range from simple branched, filamentous forms (Ectocarpus) to profusely branched forms as represented by kelps, which may reach a height of 100 metres."
- **F062** [3.1.2] (fact): Phaeophyceae "possess chlorophyll a, c, carotenoids and xanthophylls."
- **F063** [3.1.2] (fact): "They vary in colour from olive green to various shades of brown depending upon the amount of the xanthophyll pigment, fucoxanthin present in them."
- **F064** [3.1.2] (fact): Phaeophyceae: "Food is stored as complex carbohydrates, which may be in the form of laminarin or mannitol."
- **F065** [3.1.2] (fact): "The vegetative cells have a cellulosic wall usually covered on the outside by a gelatinous coating of algin."
- **F066** [3.1.2] (fact): "The protoplast contains, in addition to plastids, a centrally located vacuole and nucleus."
- **F067** [3.1.2] (definition): "The plant body is usually attached to the substratum by a holdfast, and has a stalk, the stipe and leaf like photosynthetic organ - the frond."
- **F068** [3.1.2] (process): Phaeophyceae: "Vegetative reproduction takes place by fragmentation."
- **F069** [3.1.2] (process): "Asexual reproduction in most brown algae is by biflagellate zoospores that are pear-shaped and have two unequal laterally attached flagella."
- **F070** [3.1.2] (process): Phaeophyceae: "Sexual reproduction may be isogamous, anisogamous or oogamous."
- **F071** [3.1.2] (fact): "Union of gametes may take place in water or within the oogonium (oogamous species)."
- **F072** [3.1.2] (fact): "The gametes are pyriform (pear-shaped) and bear two laterally attached flagella."
- **F073** [3.1.2] (example): "The common forms are Ectocarpus, Dictyota, Laminaria, Sargassum and Fucus (Figure 3.1b)."
- **F074** [3.1.3] (fact): "The members of rhodophyceae are commonly called red algae because of the predominance of the red pigment, r-phycoerythrin in their body."
- **F075** [3.1.3] (fact): "Majority of the red algae are marine with greater concentrations found in the warmer areas."
- **F076** [3.1.3] (fact): Red algae "occur in both well-lighted regions close to the surface of water and also at great depths in oceans where relatively little light penetrates."
- **F077** [3.1.3] (fact): "The red thalli of most of the red algae are multicellular. Some of them have complex body organisation."
- **F078** [3.1.3] (fact): "The food is stored as floridean starch which is very similar to amylopectin and glycogen in structure."
- **F079** [3.1.3] (process): "The red algae usually reproduce vegetatively by fragmentation."
- **F080** [3.1.3] (process): "They reproduce asexually by non-motile spores and sexually by non-motile gametes."
- **F081** [3.1.3] (process): Rhodophyceae: "Sexual reproduction is oogamous and accompanied by complex post fertilisation developments."
- **F082** [3.1.3] (example): "The common members are: Polysiphonia, Porphyra (Figure 3.1c), Gracilaria and Gelidium."
- **F083** [Table 3.1] (table): Table title, verbatim: "TABLE 3.1 Divisions of Algae and their Main Characteristics"
- **F084** [Table 3.1] (table): Table 3.1 column headers, in printed left-to-right order: "Classes"; "Common Name"; "Major Pigments"; "Stored Food"; "Cell Wall"; "Flagellar Number and Position of Insertions"; "Habitat"
- **F085** [Table 3.1] (table): Chlorophyceae row: Common Name "Green algae"; Major Pigments "Chlorophyll a, b"; Stored Food "Starch"; Cell Wall "Cellulose"; Flagellar "2-8, equal, apical"; Habitat "Fresh water, brackish water, salt water"
- **F086** [Table 3.1] (table): Phaeophyceae row: Common Name "Brown algae"; Major Pigments "Chlorophyll a, c, fucoxanthin"; Stored Food "Mannitol, laminarin"; Cell Wall "Cellulose and algin"; Flagellar "2, unequal, lateral"; Habitat "Fresh water (rare), brackish water, salt water"
- **F087** [Table 3.1] (table): Rhodophyceae row: Common Name "Red algae"; Major Pigments "Chlorophyll a, d, phycoerythrin"; Stored Food "Floridean starch"; Cell Wall "Cellulose, pectin and poly sulphate esters"; Flagellar "Absent"; Habitat "Fresh water (some), brackish water, salt water (most)"
- **F088** [3.2] (definition): "Bryophytes include the various mosses and liverworts that are found commonly growing in moist shaded areas in the hills (Figure 3.2)."
- **F089** [3.2] (fact): "Bryophytes are also called amphibians of the plant kingdom because these plants can live in soil but are dependent on water for sexual reproduction."
- **F090** [3.2] (fact): Bryophytes "usually occur in damp, humid and shaded localities."
- **F091** [3.2] (fact): "They play an important role in plant succession on bare rocks/soil."
- **F092** [3.2] (comparison): "The plant body of bryophytes is more differentiated than that of algae."
- **F093** [3.2] (fact): Bryophyte plant body "is thallus-like and prostrate or erect, and attached to the substratum by unicellular or multicellular rhizoids."
- **F094** [3.2] (exception): "They lack true roots, stem or leaves. They may possess root-like, leaf-like or stem-like structures."
- **F095** [3.2] (fact): "The main plant body of the bryophyte is haploid. It produces gametes, hence is called a gametophyte."
- **F096** [3.2] (fact): "The sex organs in bryophytes are multicellular."
- **F097** [3.2] (definition): "The male sex organ is called antheridium. They produce biflagellate antherozoids."
- **F098** [3.2] (definition): "The female sex organ called archegonium is flask-shaped and produces a single egg."
- **F099** [3.2] (process): "The antherozoids are released into water where they come in contact with archegonium."
- **F100** [3.2] (process): "An antherozoid fuses with the egg to produce the zygote."
- **F101** [3.2] (process): "Zygotes do not undergo reduction division immediately. They produce a multicellular body called a sporophyte."
- **F102** [3.2] (fact): "The sporophyte is not free-living but attached to the photosynthetic gametophyte and derives nourishment from it."
- **F103** [3.2] (process): "Some cells of the sporophyte undergo reduction division (meiosis) to produce haploid spores. These spores germinate to produce gametophyte."
- **F104** [3.2] (fact): "Bryophytes in general are of little economic importance but some mosses provide food for herbaceous mammals, birds and other animals."
- **F105** [3.2] (example): "Species of Sphagnum, a moss, provide peat that have long been used as fuel, and as packing material for trans-shipment of living material because of their capacity to hold water."
- **F106** [3.2] (fact): "Mosses along with lichens are the first organisms to colonise rocks and hence, are of great ecological importance."
- **F107** [3.2] (fact): "They decompose rocks making the substrate suitable for the growth of higher plants."
- **F108** [3.2] (fact): "Since mosses form dense mats on the soil, they reduce the impact of falling rain and prevent soil erosion."
- **F109** [3.2] (fact): "The bryophytes are divided into liverworts and mosses."
- **F110** [3.2.1] (fact): "The liverworts grow usually in moist, shady habitats such as banks of streams, marshy ground, damp soil, bark of trees and deep in the woods."
- **F111** [3.2.1] (example): "The plant body of a liverwort is thalloid, e.g., Marchantia."
- **F112** [3.2.1] (fact): "The thallus is dorsiventral and closely appressed to the substrate."
- **F113** [3.2.1] (fact): "The leafy members have tiny leaf-like appendages in two rows on the stem-like structures."
- **F114** [3.2.1] (process): "Asexual reproduction in liverworts takes place by fragmentation of thalli, or by the formation of specialised structures called gemmae (sing. gemma)."
- **F115** [3.2.1] (definition): "Gemmae are green, multicellular, asexual buds, which develop in small receptacles called gemma cups located on the thalli."
- **F116** [3.2.1] (process): "The gemmae become detached from the parent body and germinate to form new individuals."
- **F117** [3.2.1] (fact): "During sexual reproduction, male and female sex organs are produced either on the same or on different thalli."
- **F118** [3.2.1] (fact): Liverworts: "The sporophyte is differentiated into a foot, seta and capsule."
- **F119** [3.2.1] (process): "After meiosis, spores are produced within the capsule. These spores germinate to form free-living gametophytes."
- **F120** [3.2.2] (fact): "The predominant stage of the life cycle of a moss is the gametophyte which consists of two stages."
- **F121** [3.2.2] (definition): "The first stage is the protonema stage, which develops directly from a spore."
- **F122** [3.2.2] (fact): The protonema "is a creeping, green, branched and frequently filamentous stage."
- **F123** [3.2.2] (definition): "The second stage is the leafy stage, which develops from the secondary protonema as a lateral bud."
- **F124** [3.2.2] (fact): Leafy stage: "They consist of upright, slender axes bearing spirally arranged leaves."
- **F125** [3.2.2] (fact): "They are attached to the soil through multicellular and branched rhizoids."
- **F126** [3.2.2] (fact): "This stage bears the sex organs."
- **F127** [3.2.2] (process): "Vegetative reproduction in mosses is by fragmentation and budding in the secondary protonema."
- **F128** [3.2.2] (process): "In sexual reproduction, the sex organs antheridia and archegonia are produced at the apex of the leafy shoots."
- **F129** [3.2.2] (process): "After fertilisation, the zygote develops into a sporophyte, consisting of a foot, seta and capsule."
- **F130** [3.2.2] (comparison): "The sporophyte in mosses is more elaborate than that in liverworts."
- **F131** [3.2.2] (fact): "The capsule contains spores. Spores are formed after meiosis."
- **F132** [3.2.2] (fact): "The mosses have an elaborate mechanism of spore dispersal."
- **F133** [3.2.2] (example): "Common examples of mosses are Funaria, Polytrichum and Sphagnum (Figure 3.2)."
- **F134** [3.3] (fact): "The Pteridophytes include horsetails and ferns."
- **F135** [3.3] (fact): "Pteridophytes are used for medicinal purposes and as soil-binders. They are also frequently grown as ornamentals."
- **F136** [3.3] (fact): "Evolutionarily, they are the first terrestrial plants to possess vascular tissues - xylem and phloem."
- **F137** [3.3] (cross-ref): "You shall study more about these tissues in Chapter 6."
- **F138** [3.3] (fact): "The pteridophytes are found in cool, damp, shady places though some may flourish well in sandy-soil conditions."
- **F139** [3.3] (comparison): "You may recall that in bryophytes the dominant phase in the life cycle is the gametophytic plant body."
- **F140** [3.3] (fact): "However, in pteridophytes, the main plant body is a sporophyte which is differentiated into true root, stem and leaves (Figure 3.3)."
- **F141** [3.3] (fact): "These organs possess well-differentiated vascular tissues."
- **F142** [3.3] (definition/example): "The leaves in pteridophyta are small (microphylls) as in Selaginella or large (macrophylls) as in ferns."
- **F143** [3.3] (definition): "The sporophytes bear sporangia that are subtended by leaf-like appendages called sporophylls."
- **F144** [3.3] (definition/example): "In some cases sporophylls may form distinct compact structures called strobili or cones (Selaginella, Equisetum)."
- **F145** [3.3] (process): "The sporangia produce spores by meiosis in spore mother cells."
- **F146** [3.3] (definition): "The spores germinate to give rise to inconspicuous, small but multicellular, free-living, mostly photosynthetic thalloid gametophytes called prothallus."
- **F147** [3.3] (fact): "These gametophytes require cool, damp, shady places to grow."
- **F148** [3.3] (fact): "Because of this specific restricted requirement and the need for water for fertilisation, the spread of living pteridophytes is limited and restricted to narrow geographical regions."
- **F149** [3.3] (fact): "The gametophytes bear male and female sex organs called antheridia and archegonia, respectively."
- **F150** [3.3] (process): "Water is required for transfer of antherozoids - the male gametes released from the antheridia, to the mouth of archegonium."
- **F151** [3.3] (process): "Fusion of male gamete with the egg present in the archegonium result in the formation of zygote."
- **F152** [3.3] (process): "Zygote thereafter produces a multicellular well-differentiated sporophyte which is the dominant phase of the pteridophytes."
- **F153** [3.3] (definition): "In majority of the pteridophytes all the spores are of similar kinds; such plants are called homosporous."
- **F154** [3.3] (definition/example): "Genera like Selaginella and Salvinia which produce two kinds of spores, macro (large) and micro (small) spores, are known as heterosporous."
- **F155** [3.3] (fact): "The megaspores and microspores germinate and give rise to female and male gametophytes, respectively."
- **F156** [3.3] (fact): "The female gametophytes in these plants are retained on the parent sporophytes for variable periods."
- **F157** [3.3] (fact): "The development of the zygotes into young embryos take place within the female gametophytes."
- **F158** [3.3] (fact): "This event is a precursor to the seed habit considered an important step in evolution."
- **F159** [3.3] (fact/example): "The pteridophytes are further classified into four classes: Psilopsida (Psilotum); Lycopsida (Selaginella, Lycopodium), Sphenopsida (Equisetum) and Pteropsida (Dryopteris, Pteris, Adiantum)."
- **F160** [3.4] (definition): "The gymnosperms (gymnos : naked, sperma : seeds) are plants in which the ovules are not enclosed by any ovary wall and remain exposed, both before and after fertilisation."
- **F161** [3.4] (fact): "The seeds that develop post-fertilisation, are not covered, i.e., are naked."
- **F162** [3.4] (fact): "Gymnosperms include medium-sized trees or tall trees and shrubs (Figure 3.4)."
- **F163** [3.4] (example): "One of the gymnosperms, the giant redwood tree Sequoia is one of the tallest tree species."
- **F164** [3.4] (fact): Gymnosperms: "The roots are generally tap roots."
- **F165** [3.4] (example): "Roots in some genera have fungal association in the form of mycorrhiza (Pinus)"
- **F166** [3.4] (example): "while in some others (Cycas) small specialised roots called coralloid roots are associated with N<sub>2</sub>-fixing cyanobacteria."
- **F167** [3.4] (example): "The stems are unbranched (Cycas) or branched (Pinus, Cedrus)."
- **F168** [3.4] (fact): Gymnosperms: "The leaves may be simple or compound."
- **F169** [3.4] (example): "In Cycas the pinnate leaves persist for a few years."
- **F170** [3.4] (fact): "The leaves in gymnosperms are well-adapted to withstand extremes of temperature, humidity and wind."
- **F171** [3.4] (fact): "In conifers, the needle-like leaves reduce the surface area."
- **F172** [3.4] (fact): "Their thick cuticle and sunken stomata also help to reduce water loss."
- **F173** [3.4] (fact): "The gymnosperms are heterosporous; they produce haploid microspores and megaspores."
- **F174** [3.4] (fact): "The two kinds of spores are produced within sporangia that are borne on sporophylls which are arranged spirally along an axis to form lax or compact strobili or cones."
- **F175** [3.4] (definition): "The strobili bearing microsporophylls and microsporangia are called microsporangiate or male strobili."
- **F176** [3.4] (fact): "The microspores develop into a male gametophytic generation which is highly reduced and is confined to only a limited number of cells."
- **F177** [3.4] (definition): "This reduced gametophyte is called a pollen grain."
- **F178** [3.4] (fact): "The development of pollen grains take place within the microsporangia."
- **F179** [3.4] (definition): "The cones bearing megasporophylls with ovules or megasporangia are called macrosporangiate or female strobili."
- **F180** [3.4] (example): "The male or female cones or strobili may be borne on the same tree (Pinus)."
- **F181** [3.4] (exception/example): "However, in cycas male cones and megasporophylls are borne on different trees."
- **F182** [3.4] (fact): "The megaspore mother cell is differentiated from one of the cells of the nucellus."
- **F183** [3.4] (definition): "The nucellus is protected by envelopes and the composite structure is called an ovule."
- **F184** [3.4] (fact): "The ovules are borne on megasporophylls which may be clustered to form the female cones."
- **F185** [3.4] (number/process): "The megaspore mother cell divides meiotically to form four megaspores."
- **F186** [3.4] (number/process): "One of the megaspores enclosed within the megasporangium develops into a multicellular female gametophyte that bears two or more archegonia or female sex organs."
- **F187** [3.4] (fact): "The multicellular female gametophyte is also retained within megasporangium."
- **F188** [3.4] (comparison): "Unlike bryophytes and pteridophytes, in gymnosperms, the male and the female gametophytes do not have an independent free-living existence."
- **F189** [3.4] (fact): Gymnosperm gametophytes "remain within the sporangia retained on the sporophytes."
- **F190** [3.4] (process): "The pollen grain is released from the microsporangium."
- **F191** [3.4] (process): "They are carried in air currents and come in contact with the opening of the ovules borne on megasporophylls."
- **F192** [3.4] (process): "The pollen tube carrying the male gametes grows towards archegonia in the ovules and discharge their contents near the mouth of the archegonia."
- **F193** [3.4] (process): "Following fertilisation, zygote develops into an embryo and the ovules into seeds. These seeds are not covered."
- **F194** [3.5] (comparison): "Unlike the gymnosperms where the ovules are naked, in the angiosperms or flowering plants, the pollen grains and ovules are developed in specialised structures called flowers."
- **F195** [3.5] (fact): "In angiosperms, the seeds are enclosed in fruits."
- **F196** [3.5] (fact): "The angiosperms are an exceptionally large group of plants occurring in wide range of habitats."
- **F197** [3.5] (number/example): "They range in size from the smallest Wolffia to tall trees of Eucalyptus (over 100 metres)."
- **F198** [3.5] (fact): Angiosperms "provide us with food, fodder, fuel, medicines and several other commercially important products."
- **F199** [3.5] (fact): "They are divided into two classes : the dicotyledons and the monocotyledons (Figure 3.5)."
- **F200** [Fig 3.1] (caption): "Figure 3.1 Algae : (a) Green algae (i) Volvox (ii) Ulothrix (b) Brown algae (i) Laminaria (ii) Fucus (iii) Dictyota (c) Red algae (i) Porphyra (ii) Polysiphonia"
- **F201** [Fig 3.2] (caption): "Figure 3.2 Bryophytes: A liverwort - Marchantia (a) Female thallus (b) Male thallus Mosses - (c) Funaria, gametophyte and sporophyte (d) Sphagnum gametophyte"
- **F202** [Fig 3.3] (caption): "Figure 3.3 Pteridophytes : (a) Selaginella (b) Equisetum (c) Fern (d) Salvinia"
- **F203** [Fig 3.4] (caption): "Figure 3.4 Gymnosperms: (a) Cycas (b) Pinus (c) Ginkgo"
- **F204** [Fig 3.5] (caption): "Figure 3.5 Angiosperms : (a) A dicotyledon (b) A monocotyledon"
- **F205** [3.1] (summary-fold): "Depending on the type of pigment possesed and the type of stored food, algae are classfied into three classes, namely Chlorophyceae, Phaeophyceae and Rhodophyceae." — the SUMMARY-UNIQUE *criterion* for algal classification (pigment + stored food); the body states only the three-class division (F045) and never names the basis. Folded into 3.1 as the classification-basis statement. Source spellings "possesed"/"classfied" are NCERT typos (see Source problems).
- **F206** [3.2] (summary-fold): "They possess root-like, leaf-like and stem-like structures." — the summary asserts bryophytes *do* possess all three; the body (F094) says "They **may** possess root-like, leaf-like or stem-like structures" after "They lack true roots, stem or leaves". Body qualifier "may"/"or" is authoritative; the summary's flat assertion is recorded here and folded into 3.2 without dropping the body hedge.
- **F207** [3.2.1/3.2.2] (summary-fold): "The plant body of liverworts is thalloid and dorsiventral whereas mosses have upright, slender axes bearing spirally arranged leaves." — the summary states the liverwort-vs-moss contrast as one explicit comparison; the body gives the two halves separately (F112, F124) and never juxtaposes them. Folded into a 3.2.1/3.2.2 comparison.
- **F208** [3.4] (summary-fold): "After fertilisation the seeds remain exposed and therefore these plants are called naked-seeded plants." — the term "naked-seeded plants" appears ONLY in the summary; the body says the seeds "are not covered, i.e., are naked" (F161) but never coins this name. Folded into 3.4.
- **F209** [3.4] (summary-fold): "The sporophylls - microsporophylls and megasporophylls - are arranged spirally on axis to form male and female cones, respectively." — the summary pairs each sporophyll type to its cone sex explicitly; the body (F174, F175, F179) gives the spiral arrangement and the two cone names but never states the one-to-one pairing in a single sentence. Folded into 3.4.
- **F210** [3.4] (summary-fold): "The pollen grain germinates and pollen tube releases the male gamete into the ovule, where it fuses with the egg cell in archegonia." — the summary says the pollen grain **germinates** and names the **egg cell**; the body (F192) has the pollen tube growing and discharging "their contents near the mouth of the archegonia" without the word "germinates" and without naming the egg cell. Folded into 3.4.
- **F211** [Exercises] (exercise): Q10 match-the-columns pairs, verbatim: "(a) Chlamydomonas (i) Moss"; "(b) Cycas (ii) Pteridophyte"; "(c) Selaginella (iii) Algae"; "(d) Sphagnum (iv) Gymnosperm" — the printed Column I / Column II order is deliberately scrambled; the intended matches are Chlamydomonas-Algae, Cycas-Gymnosperm, Selaginella-Pteridophyte, Sphagnum-Moss.
- **F212** [Exercises] (exercise): Q8 term list requiring explanation with suitable examples: "(i) protonema (ii) antheridium (iii) archegonium (iv) diplontic (v) sporophyll (vi) isogamy"
- **F213** [Exercises] (exercise): Q9 differentiation pairs: "(i) red algae and brown algae (ii) liverworts and moss (iii) homosporous and heterosporous pteridophyte"
- **F214** [Exercises] (exercise): Q4 ploidy list, verbatim: "protonemal cell of a moss; primary endosperm nucleus in dicot, leaf cell of a moss; prothallus cell of a ferm; gemma cell in Marchantia; meristem cell of monocot, ovum of a liverwort, and zygote of a fern." ("ferm" is an NCERT typo for "fern".)
- **F215** [3.0] (structure): Chapter-opening sidebar contents list printed in the left margin of page 1, verbatim in printed order: "3.1 Algae"; "3.2 Bryophytes"; "3.3 Pteridophytes"; "3.4 Gymnosperms"; "3.5 Angiosperms". Confirmed by page-1 geometry (all five entries at x0=60/79.9, y=372.8-456.8, left of the 130 pt body margin) — printed page furniture, not body prose. Matches the precedent set by the closed Chapter 1 inventory, which records its printed contents list as a `Structure` row (F011).
