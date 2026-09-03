# GATE 1 — Pass 1: Source Mastery & Frozen Inventory

> **Self-contained reference for Pass 1 only.** Derived from `SUPREME COMMAND PROMPT.md` (v6). Read this to plan, execute, and close **Gate 1**. Gate 2 (build+lint) and Gate 3 (verify+deliver) have their own files. Do not delete the original prompt — this is a working extract, the original is the source of truth if the two ever disagree.

---

## 0. Where Gate 1 sits

Normal chapter: `Pass 1 → [GATE 1] → Pass 2 → [Gate 2] → Pass 3 → [Gate 3] → deliver`
Big chapter: `Pass 1a → Pass 1b → [GATE 1] → Pass 2a → Pass 2b → [Gate 2] → Pass 3 → [Gate 3] → deliver`

**Core doctrine — bounded iteration through gated passes.** Effort goes in *before* the script exists: read the source multiple times and freeze an inventory. A pass may **not** start on an ungated predecessor. Iteration is bounded (3 passes normal, 5 big). If Pass 3 later surfaces more than a handful of scattered issues, that is a signal Pass 1 was rushed — you come back and redo the relevant part of Pass 1.

**Gate 1's whole job:** produce a **frozen, machine-validated inventory `.md`** that captures every testable fact, every heading, every section opener, every figure + every in-figure label, the exercise-gap classification, and the summary classification — with every header count derived by machine from the table itself. No line of the chapter script is written until Gate 1 is green.

---

## 1. Every-session preamble (run first, every session — no exceptions)

The sandbox resets between sessions. **The first command of any session is the venv existence check.** A missing interpreter is the single most common *misdiagnosed* failure — a handoff that says "validation failed, suspected script bug" is usually just a gone venv.

```bash
ls /vercel/share/neetenv/bin/python
```

If absent, rebuild (this is the only install form proven to work in this sandbox):

```bash
uv venv /vercel/share/neetenv --python 3.13
uv pip install --python /vercel/share/neetenv/bin/python reportlab pdfplumber pymupdf Pillow
```

Invoke **every** Python command through that interpreter — never bare `python3`:

```bash
/vercel/share/neetenv/bin/python -c "
import sys, reportlab, pdfplumber, pymupdf, PIL
print('interpreter:', sys.version.split()[0], '@', sys.prefix)
print('reportlab:', reportlab.Version); print('pdfplumber: OK')
print('pymupdf:', pymupdf.__version__); print('Pillow:', PIL.__version__)
"
```

Known-good output: reportlab 5.0.1, pymupdf 1.28.2, Pillow 12.3.0 on 3.13. **Do not write around a missing library** — fix the environment. `pip install --break-system-packages` fails (pip is aliased to uv); `pip install --system` *appears* to succeed but installs into a different Python (3.9) than the `python3` on PATH — the two-interpreter trap. A venv sidesteps all of it; print `sys.prefix` to confirm packages land where you'll use them.

When a handoff reports a failed step with a suspected cause, **re-run that step after rebuilding the venv and before accepting the diagnosis.** A wrong hypothesis pointed at a shared repo-level file (`check_pdf.py`, `neet_template.py`) risks "fixing" a frozen file that was never broken.

### File & folder conventions

Deliverables live in a `notes/` tree mirroring the source `Chapter/` tree. Source PDFs are never modified/moved. Two files are repo-level, shared across all chapters: `neet_template.py` and `check_pdf.py`. Per chapter:

```
notes/class 11/Ch14_BreathingAndExchangeOfGases/
  Ch14_BreathingAndExchangeOfGases.pdf            ← the notes PDF (Pass 2)
  Ch14_BreathingAndExchangeOfGases.py             ← the exact generating script (Pass 2)
  Ch14_BreathingAndExchangeOfGases_inventory.md   ← THE GATE 1 DELIVERABLE
  assets/
    fig_14_1.png ...
```

- PDF, script, and inventory share the same base name apart from extension/suffix — `check_pdf.py` auto-discovery relies on this.
- Figure assets: `fig_<chapter>_<number>.png` matching NCERT numbering exactly; multi-part figures get letter suffixes (`fig_14_2a.png`).
- Scratch work may live in a scratch dir, but the inventory must land in the chapter folder.
- Retired: `First Pass/`, `Second Pass/`, `Final Pass/`, `Python Script Latest/`, `Final Result PDF/`. Passes are workflow stages, not folders.

---

## 2. Content Rules — what a fact IS (governs what the inventory must capture)

These rules define what counts as a preservable fact, so Pass 1 must apply them to build a complete Facts inventory. **Mode: NCERT REPLACEMENT, not high-density transcription.** Prose may be merged/reordered/tabled freely; if source and output were each reduced to a flat list of facts, the two lists must match exactly.

### Rule 1 — Zero information loss
Every one of these, wherever it appears, must appear in the rewrite (and therefore get an inventory row):
- Every definition and named structure/process
- Every number — counts, percentages, dates, ranges, dimensions, durations
- Every named scientist and their credit
- Every taxonomic name and Latin binomial (italics)
- Every example organism/compound/case
- Every step of a process, in original order
- Every comparison or exception ("unlike X, Y…")
- Every table row/column and every figure caption or label
- **Every figure itself** — extracted, monochrome, embedded (§4.4 / session 1-F)
- **Every in-figure label** — each becomes its own figure-label-matrix row and must be found in running text (check 6)
- Every fact inside a "Do You Know?" box, footnote, margin note, or in-text activity/question

Default when unsure: **keep it.** If you can't tell scene-setting from fact, treat it as fact.

### Rule 2 — Close the exercise gap (gap-only; never a full answer key)
1. Scan every exercise question.
2. Check whether main text/summary genuinely explains each term/fact it assumes.
3. Classify every question, reproduce only one class:
   - **COVERED** — rewrite already answers it. Do **not** reproduce the question, do **not** write an answer. The body text *is* the answer.
   - **GAP** — needs something the chapter never states. Reproduce in full, answer it, label as an addition (Rule 5).
4. GAP questions + answers go in the closing appendix **"Terms used in the exercises"** (or inline, cross-referenced). A gap is written once, in one place. Zero gaps → no appendix and no exercise section.

**Inventory obligation:** the Pass 1 inventory carries the *full* classification — every exercise numbered, marked COVERED (naming the answering section) or GAP (naming where the answer lives). This table lives in the inventory `.md`, never the PDF. **State the arithmetic in words:** *"N exercises, G answered by design (GAP), C unanswered by design (COVERED), 0 overlooked."* Worked example: Ch11 — *9 exercises, 4 answered, 5 unanswered by design, 0 overlooked.*

### Rule 3 — What's actually allowed to cut
"Garbage" is exactly three things: a sentence restating an already-given fact; purely rhetorical scene-setting ("Have you ever wondered…"); transitional filler. Nothing else. Merge redundant sentences but preserve every fact. Never cut for feeling "minor."

**Summary section — mandatory two-pass check.** The chapter summary is a *second source document*. For each summary sentence:
1. **Body-present check:** is the fact/number/term explicitly in the body? → BODY-PRESENT, skip it (belongs in the rewritten Quick Recap).
2. **Summary-unique check:** not in the body (even if implied, or shown only in a figure)? → **SUMMARY-UNIQUE**. Must be added to the relevant body section before the Quick Recap. Implied does not count; only explicit statement counts.

Mark each summary sentence BODY-PRESENT or SUMMARY-UNIQUE in the inventory. Every SUMMARY-UNIQUE line becomes a body addition and a mandatory Gate 1 checklist item.

### Rule 4 — Preserve exact terms and qualifier words (marks-critical)
- **Term substitution** is banned: keep "juxtaglomerular apparatus," never "kidney's filtration sensor." Rewrite *around* the term, never the term itself.
- **Qualifier drift** is banned: *usually, generally, mostly, except, only, always, never, may, cannot, unlike, in some, rarely, all, no, majority, many, some, most* change truth value. Preserve the exact NCERT word ("majority" ≠ "most"; "may" ≠ "can"; "all" ≠ "every"). Never smooth a hedge into an absolute or vice versa. (Defect 4, EcoRI "next" vs "second two letters", was this class.)

Capture the exact wording in the Facts row's "Exact original wording" column so Pass 3 can catch drift.

### Rule 5 — No outside content (anti-hallucination)
Every fact traces to *this* chapter's source PDF. No facts from general knowledge or other editions, even if true. Only exception: a clearly-labeled **Memory Aid** box (invented, not examinable). Figures: only source-extracted, monochrome-converted figures; never redraw/substitute from memory; never embed a raw/color extraction. Title motif is the one decorative exception.

### Rule 6 — No process/meta commentary in the PDF (affects where Pass 1 records things)
The PDF must read as if it had always been the book. Banned from the PDF: coverage/completeness notes, pipeline vocabulary (pass/gate/linter/verified/extracted/asset counts), editorial self-description. **Every such fact's home is the inventory `.md`** (and `CHAPTER_TRACKER.md`). The one reader-facing exception: a figure that *failed extraction* is flagged in the PDF under **"Figures requiring manual attention"**. Test: is the box's subject *biology* or *this document*? If the document, it belongs in the inventory, not the PDF.

---

## 3. §4.4 Figure obligations (drive session 1-F)

§4.4 states the **obligations**; the skill `skills/ncert-figure-extraction/SKILL.md` (a.k.a. `in-repo-ncert-figure-extraction`) states the **method** and wins on any concrete command/threshold. §4.4 wins on any *requirement* conflict. **Read the skill in full before extracting a single figure.**

**Mandatory grid standard:** before pinning/revising any figure rectangle, render every artwork page at **440 dpi** with gridlines every **5 PDF points** and coordinate labels every 20 points. Save under `scratch/ch<N>_figs/grid_4x/`, inspect, and record any repinning in the inventory/audit notes.

**Step 1 — Locate & extract (session 1-F, before the script exists):**
1. Follow the skill. In outline: open source PDF with `pymupdf`, render a high-res clip of each figure's hand-pinned box — `page.get_pixmap(clip=rect, dpi=300)`. Every rect must clear the skill's three-part crop audit (text-layer grazing, drawings-extent overflow, border-band ink).
2. Save to `assets/fig_<ch>_<n>.png`.
3. Build the **figure manifest** and **figure-label matrix** as inventory sections.
4. **Census from the page images, not caption numbers alone.** Unnumbered plates are real figures and are extracted like any other (Ch5's central-dogma plate had no number; caption-census said 17, real count 18). A caption count is a lower bound — reconcile against what is visibly on the pages.

**Harvest in-figure labels by OPENING each rendered asset and reading it — never by text extraction.** Labels are frequently baked into artwork as pixels/vector strokes, absent from the PDF text layer entirely (Ch12: all 61 labels across 7 figures were invisible to `get_text()`). Text extraction fails *silently* — it returns an empty label set that passes Gate 1 and check 6 trivially, verifying nothing. **A suspiciously label-free figure is a red flag, not a clean result.**

**Step 2 — Convert to true monochrome (mandatory, every figure):**
```python
from PIL import Image, ImageOps
img = Image.open(figure_path).convert("L")   # true greyscale, one channel
img = ImageOps.autocontrast(img, cutoff=1)   # recover contrast lost when hue disappears
img.save(output_path)
```
`autocontrast` is not optional — a figure using hue to separate elements can collapse to identical greys under flat `convert("L")`. Only the converted file is ever embedded.

**Step 3 — Verify (mandatory, every figure, not a spot-check):** open every converted image and confirm (a) correct figure for its caption, (b) no cropped labels/leader lines, (c) legible at print size, (d) not an accidental grab of a neighbor, (e) genuinely monochrome, (f) any color-carried distinction still visible. Mark `Mono: yes`/`Verified: yes` only after this.
- Indistinguishable-after-conversion = real information loss: state the distinction in caption + text/table, record in Coverage.
- Un-extractable/un-convertible figure → Coverage "Figures requiring manual attention" + flagged in PDF where it would appear. Never embed a bad crop silently.
- **Operator-omitted figure (the third state):** extraction succeeded, asset good, operator judges the plate not worth printing. NOT flagged under "manual attention". Stays in the manifest annotated **"extracted, deliberately NOT embedded"**, asset stays on disk. Permissible only once **every fact in its caption + labels is carried in prose** (name the row IDs). Record in Coverage + a decisions file + the script docstring. (Worked example: Ch11 Fig 11.1 Priestley — see its `figure_layout_decisions.md` §3.)

**Hard no:** a scientist profile photograph is never embedded, greyscaled or not. `check_pdf.py` check 4 flags any manifest portrait row for human confirmation it was kept text-only.

(Embedding itself — Step 4 — happens in Pass 2; see the Gate 2 file. Pass 1 only needs assets verified + labels harvested.)

---

## 4. Pass 1 is split across FIVE mandatory sessions (a rule, not a preference)

**A pass is not a session.** Passes are units of *work* ending in gates; sessions are units of *context* ending in handoffs. Pass 1 runs as five sessions, in order, each beginning with the venv check and ending in a handoff:

| Session | Steps | Ends when |
|---|---|---|
| **1-S — Source read & inventory** | 1, 2, 3 | Facts inventory drafted from prose |
| **1-H — Heading sweep** | 4 | Every heading has a `Type: heading` row |
| **1-O — Opener sweep** | 5 | Every section opener has a `Type: opener` row |
| **1-F — Figures** | 6 (§4.4) | Manifest complete, `Mono`+`Verified` all yes, label matrix entered |
| **1-Z — Gaps, summary & freeze** | 7, 8, 9, 10 | Inventory frozen, counts machine-derived → **Gate 1** |

**Why the split is a rule — three independent failure mechanisms:**
1. **Figure work is context-destroying (1-F).** Opening every rendered asset fills context; when it runs short the harvest silently degrades to text extraction → thin/empty labels → green gate that verified nothing. Isolating figures means the budget is spent looking at figures, and a degraded harvest shows up as an unfinished session, not a green gate.
2. **Heading and opener sweeps are different cognitive modes (1-H, 1-O).** 1-H walks the *skeleton* (headings only, prose ignored). 1-O reads the *first sentence of each section* (prose only, headings ignored). Shared, one becomes a by-product of the other — a prose sweep wearing two hats, exactly what step 3 already does. (Ch9 lost §9.8.4's "Temperature and pH" heading (D4) and §9.8.2's "conversion" definition (D9) this way despite step 3 "covering" both.)
3. **A shared session produces untrustworthy counts.** (Ch13 claimed 22 heading / 9 opener rows against a real 21 / 8.) When each sweep owns a session, its count is that session's single deliverable, derived by machine before handoff.

**Session-boundary discipline (every Pass 1 session):**
- Start with the venv check; rebuild if absent. Never diagnose before this.
- End by writing the row count this session added, **derived by machine**, into the inventory and the handoff. A session that cannot state its own count did not finish.
- The inventory file is the only state that crosses a boundary. Anything living only in reasoning is lost — write it to the file or the carry-over list.
- 1-H, 1-O, 1-F are independent of each other; if one must be redone, redo that session alone, not all of Pass 1.

---

## 5. Pass 1 steps 1–10 (detailed)

1. **First read:** read the entire chapter incl. exercises, start to finish, without building the checklist. Get the chapter's shape in your head.
2. **Independent inventory pass:** re-read section by section, build the Facts inventory — one row per fact `[ID][Section][Type][Exact wording]`. Cover Rule 1's full list.
3. **Second, independent hunting pass:** re-read hunting what pass 2 missed — buried qualifiers, footnotes, caption details, parenthetical numbers. Treat pass 2's inventory as provisional. **Does NOT cover headings or openers** — those belong to 1-H/1-O. *(Ends 1-S.)*
4. **Structural heading sweep — OWN SESSION (1-H). Every heading gets a row, `Type: heading`.** Walk headings alone, ignoring prose: numbered sections *and* unnumbered sub-headings inside them. Sub-headings are the easiest thing to lose (prose beneath reads fine). Deliverable: heading row set + machine-derived count written as "N numbered + the M unnumbered IDs below" so the total is derivable from the list. *(Ends 1-H.)*
5. **Section-opener sweep — OWN SESSION (1-O). First sentence of every section, `Type: opener`.** Read openers only, ignoring headings. Openers define terms the section leans on and are the single most-dropped item. Watch for an opener defining a word in its own section's heading (Ch9 D9). Deliverable: opener row set + machine-derived count. An observation *about* openers is not an opener row. *(Ends 1-O.)*
6. **Figure extraction/conversion/verification/label-matrix — OWN SESSION (1-F), per §4.4 (§3 above):** clip-extract at 300 dpi, convert to mono, verify by opening each asset, complete the manifest with `Mono`/`Verified`, enter every in-figure label as its own matrix row. Carry no other step in. If figures end incomplete, resume 1-F rather than proceeding. *(Ends 1-F.)*
7. **Exercise-gap scan (Rule 2):** note every term/fact an exercise assumes but the body never explains, and where the explanation will go.
8. **Summary scan (Rule 3):** classify every summary sentence BODY-PRESENT / SUMMARY-UNIQUE; fold every SUMMARY-UNIQUE fact into the correct body-section entry now.
9. **Freeze the inventory and save the file.** Number every row; ticking happens in Pass 2.
10. **Derive every header count by re-parsing the finished table — never by hand tally.** Row totals, ID ranges, heading/opener/figure-label/summary counts are all machine-countable; count them with a machine and assert ID contiguity (`F001..FNNN`, no gaps/dupes) at the same time.
    - **A count is never stated in one place, so a count is never *fixed* in one place.** The same number recurs in ~4 places (header table, Gate 1 checklist, prose census listing IDs, any status doc). When a count changes, grep the whole file for the old value and fix every live restatement in one edit, then re-parse.
    - **A census that asserts a total separately from its own list will disagree with it.** Write the census so the count is derivable from the list — "9 numbered + the 12 unnumbered IDs below" — then verify the addition equals the header. If a census number has no adjacent list supporting it, the number is the suspect.
    - **A structural finding is not a row.** A written-up observation about two adjacent Facts rows is not itself an opener/heading row. If a census total exceeds the row count by exactly one, look for a prose observation that got tallied.
    - **Controlled-vocabulary columns must be case-normalized before the freeze.** `Type` is machine-grouped — `caption` and `Caption` are two types to every parser. Normalize `Type` to one fixed spelling/casing (`heading`, `opener`, `caption`, `number`, `term`, …) and assert the table uses no others.

---

## 6. Inventory file format (the Gate 1 deliverable)

Written to `<ChapterName>_inventory.md` in the chapter folder. It is a saved file, not working notes — it is what makes the coverage claim auditable and what `check_pdf.py` reads for checks 6 and 7.

```markdown
# Frozen Inventory — <Chapter Name>
Source: <path to source PDF> | Frozen: <date> | Rows: <n>

Tick legend: `x` = written into the script and verified present in the generated PDF.

## Facts
| ID | Section | Type | Exact original wording | Ticked |
|----|---------|------|------------------------|--------|
| F001 | 14.1 | Number | "...about 79% nitrogen..." | x |

## Figure-label matrix
| ID | Fig # | Type | Figure labels (one row per figure; every in-figure label listed) | Ticked |
|----|-------|------|------------------------------------------------------------------|--------|
| F189 | Fig 9.1 | Caption | Figure labels: "Action of Restriction enzyme"; "EcoRI cuts...GAATTC..."; "Sticky end"; "Recombinant DNA" | x |

## Summary classification
| Summary sentence | Classification | Folded into |
|---|---|---|

## Exercise-gap terms
| Term/fact assumed by exercises | Explained where |
|---|---|

## Figure manifest
| Fig # | Caption (verbatim) | Asset file | Source page | Mono | Verified |
|---|---|---|---|---|---|
```

### The figure-label matrix — v6-mandatory artifact, exactly ONE place
- Rows are **Facts-table rows** whose wording begins `Figure labels:` (one row per figure, or per figure-part for multi-part figures like `Fig 9.7 (a)`/`(b)`), each in-figure label a quoted string. This is exactly the format `check_pdf.py`'s `_extract_labels` parses; check 6 fails the build unless every label appears in running text.
- **The matrix must exist in exactly ONE place — the Facts table. Never restate it as a second table for readability.** `_extract_labels` scans *every* pipe-delimited line in the file, so a duplicate table corrupts the parse two ways (both hit in Ch12):
  1. **Every label counts twice** (a restated 61-label matrix parsed as 136 strings).
  2. **The restated table's own separator (`|----|----|`) parses as a phantom figure named `Fig #`** carrying junk "labels" from the dashes.
  Both produce check-6 FAILs **impossible to fix by editing prose** — a clean chapter reported broken, pointing at content instead of the inventory. If you want it readable elsewhere, describe it in prose or list the row IDs — never repeat pipe-delimited rows.

---

## 7. GATE 1 — must be green before Pass 2 begins

- [ ] Every fact has a Facts row **and** every in-figure label has a figure-label-matrix row, with labels **harvested by opening each rendered asset** (§3 Step 1). An empty/thin label set means the harvest method was wrong, not that the figures are unlabelled.
- [ ] **The inventory has been validated by running `check_pdf.py`'s own `_extract_labels` against it** — Gate 1 is a *machine-checked* gate, not merely a written artifact. Confirm it parses the expected figure count, the expected label count with **no doubling**, and **no phantom figure rows** (e.g. a `Fig #` row from a markdown separator). Fix format problems here, while the script does not yet exist — not at Gate 2 where they present as content problems.
- [ ] **Every header count matches a re-parse of the table** (step 10), incl. contiguous `F001..FNNN` (no gaps/dupes). This means *every restatement* of every count (header, this checklist, prose census), and every census total equals the length of its adjacent list. `Type` uses one normalized spelling/casing per value.
- [ ] **Every heading has a row (`Type: heading`), incl. unnumbered sub-headings** (step 4 / 1-H), and **every section's opening sentence has a row** (step 5 / 1-O). Confirm by walking headings and openers as their own list — not by assuming the prose sweep caught them.
- [ ] **Pass 1's five sessions each actually ran and each reported its own machine-derived row count** (1-S, 1-H, 1-O, 1-F, 1-Z). A Pass 1 that reached this gate in fewer sessions has **not** met it.
- [ ] Every figure in the manifest is marked `Mono: yes` and `Verified: yes`.
- [ ] Every exercise-gap term has a planned home; every SUMMARY-UNIQUE fact has been folded into a body row.
- [ ] The inventory file is saved to the chapter folder.

**Gate 1 closed is NOT chapter closed.** State the gate explicitly: *"Gate 1 closed; Pass 2 not started."* A chapter with green Gate 1 has no script, no PDF, all rows unticked — it must never appear in a "Done" tally.

---

## 8. Big-chapter note (Pass 1 half only)

If the chapter genuinely cannot be inventoried at full quality in one Pass-1 arc, split the *source*: **Pass 1a** inventories the first half, **Pass 1b** the second half, into the **SAME** inventory file. Gate 1 is evaluated over the whole chapter only after 1b, so nothing at the seam is double-covered or dropped.
- The five-session split still applies and is orthogonal: 1a/1b halve the *source*; 1-S/1-H/1-O/1-F/1-Z separate the *kinds of work*. In practice: run the prose sweeps per half (1a-S, 1a-H, 1a-O, then 1b-S, 1b-H, 1b-O).
- **Figures run as a single whole-chapter 1-F session** and the freeze as a single 1-Z — a half-chapter figure manifest can't be checked for duplicate/missing `Fig #` numbering across the seam.
- Deliverable is still one merged inventory (and later one PDF, one script). Completeness beats brevity — never cut content to fit one session.

---

## 9. Gate 1 closure & handoff rules (learned from Ch13 Biodiversity — inherited-state failure modes)

1. **A handoff's findings are claims to re-derive, not results to apply.** Re-derive every number with the machine before acting. (Ch13's handoff was right the header was wrong (21/8 not 22/9) but wrong about *why* its validation failed — gone venv, not a script bug — and had missed a third defect, the `Type`-casing split.) **A documented trap is not a fired trap:** run the real check to see if the risk materialized here; never carry a warning forward as a finding.
2. **Closing a gate is a documentation-consistency operation, not just a content fix.** Corrected numbers get restated in ~4 inventory places + status docs; every stale copy is a live defect. Rewrite the "what blocks this gate" section (don't leave an obsolete blocker instructing the next session to re-fix a closed defect). Sweep for stale claims by string *after* editing. **Distinguish a live claim from quoted history** — a properly-recorded correction ("header previously read 22/9") makes the old number appear in a grep; check the surrounding line and frame corrections as history.
3. **Roll-up counters drift silently and must be derived, never incremented.** Derive roll-ups by counting rows (`grep -c` the done marker), re-derive on every closure even when the current chapter doesn't change the total. (Ch13's tracker header said 9/32 while its own footer said 4/13 — an incremented counter that was never propagated.)
4. **Name which gate closed, and count only what that gate earns.** Write the gate number every time: *"Gate 1 closed; Pass 2 not started."* Never fold a Gate-1 chapter into a completion count — that is the false-closure failure that let Ch9 ship defective twice.
5. **A frozen inventory may be corrected in its metadata, never in its rows.**
   - **Allowed:** correcting a count, header field, or census total (metadata *about* the rows).
   - **Not allowed:** adding/removing/reclassifying/rewording a Facts row to make a count come out. If a count and the rows disagree, **the rows win and the count changes.** (One exception: Pass 3 direction 2 may add a genuinely UNINVENTORIED row — logged loudly as a Pass 1 gap, never back-dated.)
   - **Cosmetic defects found after the freeze go to the carry-over list, not into the rows.** (Ch13's `Type`-casing split broke no Gate 1 criterion → logged as a Pass 2 carry-over.)
6. **Carry-overs are the handoff's real payload.** A resumed session's most valuable inheritance is the numbered carry-over list — things found while looking at something else that the current gate has no authority over (a cosmetic finding, a trap that did not fire, a rule about what must *not* be "fixed" later). Keep them in the inventory and add freely; each is a defect that won't have to be rediscovered.
