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
> It writes `scratch/question_prompts/<Chapter>_prompt.md` — this prompt with `{{CLASS}}`, `{{CHAPTER}}`, `{{COUNT}}`, `{{STAMP}}`, `{{BRIDGES}}` filled in and every usable Facts table appended. Paste that file. Nothing else to attach: the source text arrives with the prompt precisely so the model is never asked to recall NCERT.

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
Generate **{{COUNT}} original multiple-choice questions** anchored to **Class {{CLASS}}, Chapter: {{CHAPTER}}**. Every item must be **at NEET difficulty or harder — the center of gravity is *harder***. The set must be built so that a student who masters all of it has no exploitable weakness left in this chapter or its connections to the rest of the syllabus. Items are original (never copied verbatim) but exceed the reference exam in cognitive demand.

Build stamp for this run: `{{STAMP}}`. Bridge chapters supplied: `{{BRIDGES}}`. Echo the stamp verbatim in your run header — it is how the gate later proves the bank was generated from the source text that is on disk *now* rather than from a stale copy.

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
Distribute the {{COUNT}} items. **Default mix: 20% Tier-1, 45% Tier-2, 35% Tier-3** (the gate allows +/- 10 percentage points per tier and WARNs outside that band). The mass sits in the hard bands on purpose.

- **Tier 1 — NEET-standard floor (20%).** Clean single-concept anchor items. Present only to guarantee full syllabus coverage of core facts a 360 requires — never the bulk of the set. Minimum 1 cited fact ID.
- **Tier 2 — NEET-hard / multi-concept (45%).** Requires fusing 2-3 NCERT facts, a careful negative stem, or eliminating close confusables. Frequently pulls one link from a bridge chapter. This is the modern NEET discriminator band. Minimum 2 cited fact IDs.
- **Tier 3 — Above NEET / integrative destroyer (35%).** Multi-step reasoning, cross-chapter synthesis, calculation, or data/scenario interpretation combining several NCERT ideas. Still 100% NCERT-derivable, but engineered to break students who only memorized. This tier is the point of the set. Minimum 2 cited fact IDs; aim for 3-4.

Never sacrifice correctness to reach a tier. A wrong Tier-3 item is worse than a clean Tier-1 item. **Never inflate a tier tag to hit the mix, either** — the tag is checked against the citation count, so a "Tier 3" resting on one fact fails rather than flatters.

### Question archetypes with target quotas
Produce a spread across ALL of the following. The **tag in square brackets is a controlled vocabulary** — write exactly these eight strings, because the gate groups on them. Suggested proportions for {{COUNT}}=45 in parentheses; scale proportionally. Bias every archetype toward the multi-concept/cross-chapter version wherever the content allows.

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
- For every Tier-2 and Tier-3 item, identify the **anchor concept (from {{CHAPTER}})** and the **linked concept(s)** it fuses with. Declare the link in the item tag's `Links:` field *and* cite at least one bridge row ID in `Meta: facts=[...]`.
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
/vercel/share/neetenv/bin/python check_qbank.py "notes/class {{CLASS}}/<ChapterDir>" --emit-ledger
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
Anchor: class {{CLASS}} / <ChapterDir>
Prompt-build: {{STAMP}}
Items: {{COUNT}} | Tier mix T1/T2/T3 = __/__/__
Archetypes: single=__ | match=__ | count=__ | sequence=__ | assertion-reason=__ | negative=__ | numerical=__ | scenario=__
Cross-chapter: __/__ | Bridges used: <ChapterKey, ...>
Key distribution: (1)=__ (2)=__ (3)=__ (4)=__
Pass-Q2 fixes: __ rewritten / __ discarded
UNGROUNDED: <facts I could not pin to a supplied row, omitted — or "none">
Substitutions: <archetype redistributions — or "none">
```
`Cross-chapter` is stated as *cross-chapter Tier-2+3 items / total Tier-2+3 items* — not out of `{{COUNT}}`, since Tier-1 is not expected to reach beyond the anchor.

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
