# NEET QUESTION-GENERATION PROMPT — "Defeat the Aspirant / 360 Mastery Set" (per chapter)

> **Purpose.** A reusable, self-contained prompt for generating **adversarial, multi-concept, cross-chapter** biology MCQs anchored to **one NCERT chapter** but licensed to pull in every linked NCERT idea. The design goal is blunt: **defeat the under-prepared aspirant.** A student who can genuinely solve *every* item this prompt produces, across every chapter, should be able to score **360/360** in NEET Biology. Calibrated against — and deliberately pitched *above* — the *NEET (UG)-2026, 03-05-2026, Code-11* Biology section (Q91–180).
>
> **How to use.** Copy everything under "PROMPT BODY" into the model. Replace the fillers: `{{CLASS}}`, `{{CHAPTER}}`, and `{{COUNT}}` (default 45). Point the model at the chapter's NCERT source (`notes/<class>/<chapter>/` material in this repo, or the raw NCERT PDF) **and** make the full NCERT Biology corpus available for the cross-chapter links.

---

## PROMPT BODY

### Role
You are a **ruthless senior NEET Biology paper-setter and destroyer of ranks** with 15+ years of national item-writing experience. Your items are **factually airtight, NCERT-faithful, and psychometrically clean**, but their explicit purpose is to *separate the student who memorized the book from the student who actually understands it*. You never invent biology that contradicts current NCERT — your cruelty comes from **integration and reasoning depth, never from going out of syllabus**.

### Objective
Generate **{{COUNT}} original multiple-choice questions** anchored to **Class {{CLASS}}, Chapter: {{CHAPTER}}**. Every item must be **at NEET difficulty or harder — the center of gravity is *harder***. The set must be built so that a student who masters all of it has no exploitable weakness left in this chapter or its connections to the rest of the syllabus. Items are original (never copied verbatim) but exceed the reference exam in cognitive demand.

### The "360" mandate — what "harder" actually means
Difficulty here does **not** come from obscure trivia. It comes from four legitimate, NCERT-bounded levers. Use them relentlessly:

1. **Multi-concept fusion.** A single item must force the student to hold and combine **2–4 distinct NCERT facts** to reach the answer. No item should be solvable by recalling one sentence.
2. **Cross-chapter reasoning.** The chapter is the *anchor*, not a fence. Deliberately link it to other NCERT chapters — e.g. Animal Kingdom ↔ Body Fluids/Circulation (heart chambers), ↔ Breathing (respiratory surfaces), ↔ Evolution (phylogeny); Photosynthesis ↔ Respiration (energetics) ↔ Plant Physiology; Genetics ↔ Molecular Basis ↔ Biotechnology. At least the Tier-2 and Tier-3 items should reach beyond the anchor chapter.
3. **Extra reasoning steps.** Chain inferences: "if X is true, then which of Y follows" — require 2–3 logical hops, elimination under a negative stem, or resolving a contradiction between statements.
4. **Discrimination under pressure.** Distractors must be things a 320-scorer would actually pick. The item should punish shallow pattern-matching and reward true conceptual command.

If an item can be answered by a single recalled line, it is **too easy — rewrite or discard it.**

### Absolute scope rule (non-negotiable)
- Every fact, number, name, sequence, and relationship tested **must be verifiable somewhere in the NCERT Biology textbooks** (Class 11 + Class 12). Cross-chapter is encouraged; **out-of-NCERT is forbidden** — not in the stem, key, or the presumed truth-value of any distractor.
- You may test *inference, integration, and synthesis across NCERT chapters*, but never *content outside NCERT* (no research trivia, no coaching-only mnemonics presented as fact, no exceptions the book does not state).
- When in doubt about a fact, drop the item rather than guess. A hard item built on a shaky fact is a defect, not a challenge.

### Difficulty calibration — three tiers (reweighted for adversarial intent)
Distribute the {{COUNT}} items. **Default mix: 20% Tier-1, 45% Tier-2, 35% Tier-3.** The mass sits in the hard bands on purpose.

- **Tier 1 — NEET-standard floor (20%).** Clean single-concept anchor items. Present only to guarantee full syllabus coverage of core facts a 360 requires — never the bulk of the set.
- **Tier 2 — NEET-hard / multi-concept (45%).** Requires fusing 2–3 NCERT facts, a careful negative stem, or eliminating close confusables. Frequently pulls one link from an adjacent chapter. This is the modern NEET discriminator band.
- **Tier 3 — Above NEET / integrative destroyer (35%).** Multi-step reasoning, cross-chapter synthesis, calculation, or data/scenario interpretation combining several NCERT ideas. Still 100% NCERT-derivable, but engineered to break students who only memorized. This tier is the point of the set.

Never sacrifice correctness to reach a tier. A wrong Tier-3 item is worse than a clean Tier-1 item.

### Question archetypes with target quotas
Produce a spread across ALL of the following. Suggested proportions for {{COUNT}}=45 in parentheses — scale proportionally. Bias every archetype toward the multi-concept/cross-chapter version wherever the content allows.

1. **Single-correct factual/conceptual MCQ** (~8). Four options, one correct. Prefer stems that still require combining two facts over pure recall.
2. **Match List-I with List-II** (~8). Two lists of 4 (A–D vs I–IV), four full-pairing options. Make at least half of these **cross-chapter** (e.g. organism ↔ feature from a different chapter). Consider 5×5 lists to raise load.
3. **Multi-statement "how many are correct / incorrect"** (~9). Present 4–5 labelled statements (A–E), ideally drawn from *different* sections/chapters. Prefer the "**how many** are correct" counting format over "which combination" — it removes elimination shortcuts and is harder.
4. **Sequence / arrange-in-order** (~5). 4–5 steps/events out of order (pathways, life cycles, techniques, cascades, taxonomic hierarchy). Use cross-process sequences where valid.
5. **Assertion–Reason** (~5). Standard A/R with the four NCERT-style options (both true + R explains A / both true + R doesn't explain / A true R false / A false R true). Excellent for testing whether a student understands *causation*, not just facts. Make A and R come from linked concepts.
6. **Negative-stem MCQ** (~3). "Which is **not** true / **incorrect** / **wrongly matched**." Bold the negative word.
7. **Numerical / quantitative** (~4). Genetic probability (Punnett/blood groups/pedigree), RQ, ATP–NADPH stoichiometry, differential counts, ploidy across a life cycle, growth-equation reading, Hardy–Weinberg. Numbers must be NCERT-anchored; combine two quantitative facts where possible.
8. **Scenario / data-interpretation** (~3). A vignette (organism characters, a graph/table in words, an experimental observation) ending in identify/classify/predict — rewarding application of NCERT criteria to a novel case, ideally spanning two chapters.

If the chapter cannot support an archetype, redistribute the quota to supported ones and note the substitution in the run header.

### Cross-chapter linking — required discipline
- For every Tier-2 and Tier-3 item, identify the **anchor concept (from {{CHAPTER}})** and the **linked concept(s)** it fuses with. Record the linked chapter in the answer key's "NCERT anchor" line.
- Aim for **at least 50% of Tier-2 and Tier-3 items to be genuinely cross-chapter** (the link is load-bearing, not decorative).
- Legitimate links only: the connection must be one NCERT itself supports (shared structure, shared pathway, evolutionary relationship, cause–effect, exception-to-a-rule). Do not force artificial links.

### Distractor (wrong-option) construction rules
Distractors are where the defeat happens. For every item:
- All four options must be **grammatically parallel, similar in length, and genuinely tempting** to a well-prepared-but-not-expert student.
- Build distractors from **real NCERT confusables**: the sibling term, the adjacent step, the reciprocal relationship, the commonly-swapped pair (GPP vs NPP, promoter vs terminator, autogamy vs geitonogamy vs xenogamy, Chondrichthyes vs Osteichthyes, incomplete vs codominance).
- Exactly **one** option is defensibly correct. No "two-could-be-right" items. Every distractor must be *defensibly wrong* with a citable reason.
- Kill giveaway cues: don't make the key the longest/most-qualified option, don't echo a stem keyword only in the key, randomize key positions (don't cluster on one number).
- For match/sequence/multi-statement/count items, ensure no single trivial elimination reveals the key; each distractor should differ from the key in a way that traps a specific misconception.

### Output format (strict)
Produce two clearly separated sections.

**SECTION A — QUESTION PAPER (no answers).** Number items continuously from 1. For each:
```
Q<n>. [Tier <1|2|3>] [<archetype>] [Anchor: <topic> | Links: <chapter(s) or "—">]
<stem>
  (1) <option>
  (2) <option>
  (3) <option>
  (4) <option>
```
For Match items, render both lists as a two-column table before the options. Use LaTeX in double dollar signs for any equation/formula (e.g. $$dN/dt = rN\left(\frac{K-N}{K}\right)$$).

**SECTION B — ANSWER KEY & EXPLANATIONS.** For each item:
```
Q<n>. Correct: (<x>)
Reasoning chain: <the 2–4 step path from NCERT facts to the answer>
NCERT anchor: <anchor chapter/section> ; Links: <other chapter/section(s) used>
Why others fail: (a) … (b) … (c) …
Trap targeted: <the specific misconception this item punishes>
```
Every explanation must cite the specific NCERT basis for *each* fact fused. If any fused fact cannot be cited, the item is invalid — remove it.

### Self-audit before you output (do all silently, then emit only the two sections)
1. **Fact check:** re-derive each key from NCERT; confirm every distractor is genuinely wrong and every fused fact is citable.
2. **Single-answer check:** confirm no item has zero or multiple correct options.
3. **Difficulty check:** confirm the reweighted tier mix and that **no item is solvable by a single recalled line** except the deliberate Tier-1 floor.
4. **Integration check:** confirm ≥50% of Tier-2/Tier-3 items are genuinely multi-concept, and the cross-chapter links are load-bearing.
5. **Archetype spread check:** confirm all supported archetypes appear near quota, including Assertion–Reason and "how many" counting items.
6. **Coverage check:** confirm items span the chapter's major sections (a 360 needs total coverage, not a hot topic).
7. **Style check:** negative words bolded; options parallel; key positions randomized; no external content.

Output only the run header (below) followed by SECTION A and SECTION B. No preamble, no commentary.

### Run header to emit first
```
CHAPTER: Class {{CLASS}} — {{CHAPTER}}
ITEMS: {{COUNT}} | Tier mix: T1/T2/T3 = __/__/__
Archetype counts: single __ | match __ | multi/count __ | sequence __ | assertion-reason __ | negative __ | numerical __ | scenario __
Cross-chapter items: __/{{COUNT}} | Linked chapters used: ...
Substitutions (if any): ...
```

---

## MAINTAINER NOTES (not part of the prompt to the model)

- **Design intent:** this is the "defeat the aspirant" upgrade of the original NEET set. Difficulty is bought with *integration and reasoning*, never with out-of-syllabus trivia. If output starts leaking non-NCERT content to seem hard, tighten the scope rule — do not relax it.
- **The 360 claim is a coverage + depth contract:** mastering every item across every chapter should leave no exploitable gap. That requires both the Tier-1 floor (total factual coverage) and the Tier-2/3 mass (integration). Do not drop the Tier-1 floor to look harder — full marks needs the easy facts locked too.
- **Cross-chapter needs the whole corpus:** give the model both the anchor chapter and access to the full NCERT Biology text, or the links will be hallucinated. The "Links" field in the key is the audit hook — spot-check it.
- **Reference calibration set:** `user_read_only_context/text_attachments/NEET_2026_May3_Biology_QuestionsOnly-*.pdf` (Q91–180). Generated items should feel *harder* than these, not merely equal.
- **Per-chapter batching:** run once per chapter. For a full-syllabus bank, loop over every chapter in `CHAPTER_TRACKER.md`, storing output as `notes/<class>/<chapter>/<chapter>_QBANK.md`.
- **Recommended default count:** 45/chapter; raise to 60–90 for heavily-weighted chapters (Genetics, Human Physiology, Ecology, Biotechnology, Cell/Biomolecules).
- **Answer-key discipline mirrors this repo's Gate ethos:** an item with an uncitable fused fact is a *defect*, not a stylistic choice — cut it. Treat "NCERT anchor / Links" as mandatory evidence, exactly like Fact-ledger citations elsewhere in this project.
- **Most common failure modes to police:** (1) a "hard" item that quietly leaves NCERT; (2) a plausible distractor that is actually true; (3) a fake cross-chapter link that isn't load-bearing; (4) drifting the tier mix easy to make single-answer bookkeeping simpler. The scope rule and self-audit exist to kill all four.
