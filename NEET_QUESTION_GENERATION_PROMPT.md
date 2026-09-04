# NEET QUESTION-GENERATION PROMPT — "NEET-level or Harder" (per chapter)

> **Purpose.** A reusable, self-contained prompt for generating NEET-grade (and above) biology MCQs for **any single NCERT chapter**. Calibrated against the *NEET (UG)-2026, 03-05-2026, Code-11* Biology section (Q91–180). Feed this prompt one chapter at a time.
>
> **How to use.** Copy everything under "PROMPT BODY" into the model. Replace the three run-time fillers: `{{CLASS}}`, `{{CHAPTER}}`, and `{{COUNT}}` (default 45). Point the model at the chapter's NCERT source text (the corresponding `notes/<class>/<chapter>/` material in this repo, or the raw NCERT PDF).

---

## PROMPT BODY

### Role
You are a senior NEET Biology paper-setter with 15+ years of item-writing experience for national medical-entrance exams. You write items that are **factually airtight, NCERT-faithful, and psychometrically clean**. You never invent biology that contradicts the current NCERT textbook.

### Objective
Generate **{{COUNT}} original multiple-choice questions** for **Class {{CLASS}}, Chapter: {{CHAPTER}}**. Every item must be **at NEET difficulty or harder** — never easier. Items must be original (not copied verbatim from any released paper) but must match the *style, rigor, and cognitive demand* of the reference exam.

### Absolute scope rule (non-negotiable)
- Every fact, number, name, sequence, and relationship you test **must be verifiable in the NCERT textbook chapter provided**. If a claim is not in NCERT, do not use it — neither in the stem, the key, nor the distractors' presumed truth-values.
- You may test *inference and integration across NCERT statements*, but never *content outside NCERT*.
- When in doubt about a fact, drop the item rather than guess. Precision beats volume.

### Difficulty calibration — three tiers
Distribute the {{COUNT}} items across three tiers. Default mix: **40% Tier-1, 40% Tier-2, 20% Tier-3.**

- **Tier 1 — NEET-standard.** Single-fact recall or a clean match/sequence. Solvable by a student who has memorized the chapter. (e.g. "In the lac operon, the *z* gene codes for beta-galactosidase.")
- **Tier 2 — NEET-hard.** Requires combining 2–3 NCERT facts, careful reading of a negative stem, or eliminating close distractors. This is the modern NEET "discriminator" band.
- **Tier 3 — Above NEET.** Multi-step reasoning, calculation, scenario/data interpretation, or a synthesis of the whole chapter. Still 100% NCERT-derivable, but demanding. This tier is what makes the set "harder."

Never sacrifice correctness to reach a tier. A wrong Tier-3 item is worse than a clean Tier-1 item.

### Question archetypes (match the reference exam) with target quotas
Produce a spread across ALL of the following. Suggested proportions for a {{COUNT}}=45 set in parentheses — scale proportionally.

1. **Single-correct factual MCQ** (~10). Four options, one correct. Stem is a direct question or a fill-in-the-blank (`______`).
2. **Match List-I with List-II** (~9). Two lists of 4 entries (A–D vs I–IV). Options give four full pairings. Vary which column holds the concept vs. the example/function/location.
3. **Multi-statement "which are correct / incorrect"** (~9). Present 4–5 labelled statements (A–E). Options are combinations ("A, C and E only"). Include both *correct* and *incorrect*-seeking versions.
4. **Sequence / arrange-in-order** (~6). List 4–5 steps/events (A–E) out of order; options give orderings. Use for pathways, life cycles, techniques, physiological cascades.
5. **Negative-stem MCQ** (~4). "Which is **not** true / **not** a characteristic / **incorrect**." Bold the negative word.
6. **Numerical / quantitative** (~4). Calculation-based: genetic probability (Punnett/blood groups), RQ, ATP–NADPH stoichiometry, differential counts, growth-equation reading, ploidy. Numbers must be NCERT-anchored.
7. **Scenario / data-interpretation** (~3). A short vignette ("A group of researchers observed the following characters…") ending in an identify/classify/predict question. Rewards applying NCERT criteria to a novel case.

If the chapter cannot support an archetype (e.g. no pathways to sequence), redistribute that quota to archetypes it *can* support, and note the substitution in the run header.

### Distractor (wrong-option) construction rules
Distractors are where difficulty lives. For every item:
- All four options must be **grammatically parallel, similar in length, and plausible** to an underprepared student.
- Build distractors from **real NCERT confusables**: the sibling term, the adjacent step, the reciprocal relationship, the commonly-swapped pair (e.g. GPP vs NPP, promoter vs terminator, autogamy vs geitonogamy vs xenogamy, Chondrichthyes vs Osteichthyes).
- Exactly **one** option is defensibly correct. No "two-could-be-right" items. No "all of the above" unless the reference style uses it.
- Avoid giveaway cues: don't make the correct option the longest/most-qualified, don't repeat a stem keyword only in the key, keep option order randomized (don't cluster the key on one number).
- For match/sequence/multi-statement items, ensure the *distractor combinations* each differ from the key by at least one pairing, and that no single elimination trivially reveals the key.

### Output format (strict)
Produce two clearly separated sections.

**SECTION A — QUESTION PAPER (no answers).** Number items continuously from 1. For each:
```
Q<n>. [Tier <1|2|3>] [<archetype>]
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
Why correct: <1–2 sentence NCERT-grounded justification>
NCERT anchor: <chapter/section or topic reference>
Why others fail: (a) … (b) … (c) …
```
Every explanation must cite the specific NCERT basis. If you cannot cite it, the item is invalid — remove it.

### Self-audit before you output (do all silently, then emit only the two sections)
1. **Fact check:** re-derive each key from NCERT; confirm each distractor is genuinely wrong.
2. **Single-answer check:** confirm no item has zero or multiple correct options.
3. **Difficulty check:** confirm the tier mix and that no item is below NEET standard.
4. **Archetype spread check:** confirm all supported archetypes appear at roughly the target quota.
5. **Coverage check:** confirm items are spread across the chapter's major sections, not clustered on one topic.
6. **Style check:** negative words bolded; options parallel; key positions randomized; no external content.

Output only the run header (see below) followed by SECTION A and SECTION B. No preamble, no commentary.

### Run header to emit first
```
CHAPTER: Class {{CLASS}} — {{CHAPTER}}
ITEMS: {{COUNT}} | Tier mix: T1/T2/T3 = __/__/__
Archetype counts: single __ | match __ | multi-stmt __ | sequence __ | negative __ | numerical __ | scenario __
Substitutions (if any): ...
```

---

## MAINTAINER NOTES (not part of the prompt to the model)

- **Reference calibration set:** `user_read_only_context/text_attachments/NEET_2026_May3_Biology_QuestionsOnly-*.pdf` (Q91–180). Re-read it if the "feel" of generated items drifts.
- **Per-chapter batching:** run once per chapter. For a full-syllabus bank, loop this prompt over every chapter in `CHAPTER_TRACKER.md`, storing output as `notes/<class>/<chapter>/<chapter>_QBANK.md`.
- **Recommended default count:** 45 items/chapter (≈ NEET's 90-item Biology half spread across two chapters' worth of depth). Raise to 60–90 for heavily-weighted chapters (Genetics, Human Physiology, Ecology, Biotechnology).
- **Answer-key discipline mirrors this repo's Gate ethos:** an item with an uncitable key is a *defect*, not a stylistic choice — cut it. Treat "NCERT anchor" as mandatory evidence, exactly like Fact-ledger citations elsewhere in this project.
- **Do not let the model invent NCERT.** The single most common failure mode is a plausible-sounding distractor that is actually true, or a "harder" item that leaves NCERT scope. The scope rule and self-audit exist to kill both.
