# GATE 3 — Pass 3: Dual Verification & Deliver

> **Self-contained reference for Pass 3 only.** Derived from `SUPREME COMMAND PROMPT.md` (v6). Read this to run the visual + content verification and close **Gate 3** / deliver. Gate 1 (inventory) and Gate 2 (build+lint) have their own files. The original prompt is the source of truth if the two disagree.

---

## 0. Where Gate 3 sits

Normal: `Pass 1 → [Gate 1] → Pass 2 → [Gate 2] → Pass 3 → [GATE 3: zero confirmed defects + bidirectional full read] → deliver`
Big: `… → [Gate 2] → Pass 3 → [GATE 3] → deliver` (Pass 3 is a single whole-chapter pass either way)

**Precondition:** Gate 2 is green — `check_pdf.py` exits 0 on the current PDF. **Do not begin Pass 3 while the linter is red.** With mechanical/print defects gated out by Pass 2, Pass 3 is the two focused checks a machine cannot make: **cross-page visual consistency** and **genuine content drift** against the frozen inventory. **Gate 2 and Gate 3 test different things** — a fully-green `--strict` linter does not mean the content is correct (Ch9 was green under `--strict` with all three of its confirmed content defects still present).

---

## 1. Every-session preamble (run first, every session)

Sandbox resets between sessions. **First command of any session:**
```bash
ls /vercel/share/neetenv/bin/python
```
If absent, rebuild + verify:
```bash
uv venv /vercel/share/neetenv --python 3.13
uv pip install --python /vercel/share/neetenv/bin/python reportlab pdfplumber pymupdf Pillow
/vercel/share/neetenv/bin/python -c "import sys,reportlab,pdfplumber,pymupdf,PIL;print(sys.version,sys.prefix,reportlab.Version,pymupdf.__version__,PIL.__version__)"
```
Invoke every Python command through `/vercel/share/neetenv/bin/python`. Known-good: reportlab 5.0.1, pymupdf 1.28.2, Pillow 12.3.0 on 3.13. Never write around a missing library; never "fix" a shared repo-level file on an inherited hypothesis without re-running after a venv rebuild first.

**Load the inventory from the saved FILE, not from memory.** Every row checked in Pass 3 is read out of `<ChapterName>_inventory.md`.

---

## 2. Pass 3(a) — Visual render check (every page)

Render **every page** with `pymupdf` and look at each directly. Layout bugs — overflow, clipping, a table running off the page, an orphaned heading, a process-flow rule misaligned with its badges, a figure squashed to the wrong aspect ratio — show up only in the rendered page, not in extracted text.

Additionally render each page at **true print DPI + a B&W 1-bit threshold** and confirm cross-page **style consistency:** pull one rendered instance of each element type (H1, H2, H3, table, NOTE, MEMORY AID, process flow, figure box) from **at least three different points** in the chapter and confirm they are visually *identical*. (Styles are imported from `neet_template.py`, so drift should be rare — this confirms the template held rather than hunting hand-typed drift.)

Pass 3(a) must **cover every page**, later stated as a count ("15/15 pages inspected"), never "spot-checked".

---

## 3. Pass 3(b) — Content cross-check, BOTH directions (mandatory)

Do **one complete, full read** — not a keyword search — of the source sections and the matching script blocks, checking every inventory row (loaded from the FILE). Classify each item:
- **COVERED** — present and accurate in the script
- **MISSING** — in the inventory/NCERT but absent from the script
- **FABRICATED** — in the script but not in NCERT or the inventory
- **DRIFTED** — present but value/qualifier/direction/term is wrong (defect 4 was this class)
- **UNINVENTORIED** — in NCERT but has **no inventory row at all**

### Both directions are mandatory. Direction 2 is the one that has actually failed.
1. **Inventory → script.** For every row, is it in the script and correct? Catches MISSING / DRIFTED / FABRICATED.
2. **Source → inventory.** Read the NCERT section itself: *is every sentence and every heading here represented by some row?* Catches **UNINVENTORIED** — a Pass 1 gap, not a Pass 2 gap.

Direction 1 alone is **structurally incapable** of finding a Pass 1 omission: if the freeze never created a row, there is nothing to classify, and the section reports CLEAN while genuinely incomplete. **Ch9 proved this twice** — Gate 3 closed with direction 1 clean while the chapter was missing an NCERT sentence (D9 — the §9.8.2 antecedent defining the word in its own section's heading) and two NCERT sub-headings (D4 — §9.8.4's "Temperature and pH" and "Concentration of Substrate"). All were invisible to direction 1 and required adding new rows (F194a, F221a, F225a) during Pass 3. When direction 2 forces a new row, **say so plainly and log it as a real Pass 1 gap — never back-date it into the freeze** to make Pass 1 look clean.

Divide the chapter's sections into adjacent pairs and run one subagent per pair in parallel (`config: { $kind: "explore" }`) with the rubric below; **if parallel subagents are unavailable, do the identical section-pair cross-check yourself, sequentially** — the rigor is in the rubric and the full-read discipline, not the parallelism. Figure-label-matrix rows are cross-checked here too (correct asset, caption number/text correct, placed at the right topic), as a human backstop to check 6.

### Subagent / per-pair rubric
```
For each of your 2 assigned sections:
1. Read the full source text for these sections, start to finish — not a term search.
2. Read the full corresponding script block(s), start to finish.
3. DIRECTION 1 (inventory -> script): classify each inventory row
   COVERED / MISSING / FABRICATED / DRIFTED.
4. DIRECTION 2 (source -> inventory), MANDATORY: walk the NCERT section
   sentence by sentence and heading by heading. For each one, name the row
   that carries it. Anything with no row is UNINVENTORIED - report it.
   Check explicitly, because these are the ones that slip:
     - every sub-heading, including H3s under a numbered section
     - the FIRST sentence of each section (antecedent/defining sentences
       are the most commonly dropped item of all - this was Ch9 D9)
     - sentences that define a term used in the section's own heading
5. For each figure-label row: confirm the label appears in the running text
   and the figure sits at its topic.
6. Return: SECTION | STATUS (CLEAN | ISSUES FOUND) | COVERED count |
   MISSING list | FABRICATED list | DRIFTED (NCERT says X, script says Y) |
   UNINVENTORIED list
   A section is CLEAN only if BOTH directions are clean. Do not report CLEAN
   on the strength of direction 1 alone.
```

### Evidence discipline
- **Confirm every flag by full read, never by grep.** A grep miss doesn't mean a fact is missing (it may be paraphrased/reflowed by `pdfplumber`); a grep hit doesn't mean it's correct. Open the source paragraph and the script block and read both before deciding CONFIRMED vs FALSE POSITIVE.
- **No statistical text match may close Gate 3 — hard bar, not preference.** Token-coverage scores, similarity %, fuzzy matching, "N/N rows at ≥X% coverage" tables, any automated inventory-vs-extracted-text comparison are **Pass 2 evidence only.** They may *locate* suspicious rows; they may **never** *clear* them. They fail silently in exactly the cases that matter: drop an antecedent sentence and remaining tokens still overlap (score stays high); omit a sub-heading and there's no row to score (nothing registers). Ch9's "276/276 rows at ≥78% coverage, 260 at 100%" passed a chapter missing one sentence and two sub-headings. **A high score is evidence only that the text you wrote resembles the text you wrote down.**
- **Gate 3 evidence must be a stated, human-legible reading claim**, per section, in both directions — e.g. *"read source §9.8.4 pp. 114–115 against script block `# ---- 9.8.4 ----`; both sub-headings present; 12 rows COVERED; 0 UNINVENTORIED."* If the record cannot state *what was read against what*, Gate 3 is not satisfied, regardless of linter/coverage output.
- **Record false positives separately from confirmed defects, and keep both.** A flag investigated and correctly dismissed is real audit work — keep it with its reasoning, distinct from the confirmed-defect list, so a later session doesn't re-litigate or "fix" a deliberate rejection. Likewise note where a `check_pdf.py` check legitimately does not fire (e.g. check 4 on a chapter with no scientist profile) so a true negative isn't later mistaken for a suppressed finding.

### Fixing confirmed items
Open the `.py`, locate the block via its `# ---- N.N ----` comment, **edit only that block** (tag `# [VERIFICATION FIX]`), regenerate the PDF, **re-run `check_pdf.py` (it must stay green)**, and re-verify only the fixed block. The rest was already verified and nothing else changed.

If Pass 3 surfaces more than a handful of small scattered issues, treat that as a signal **Pass 1 was incomplete** — redo the relevant part of Pass 1 rather than patching piecemeal against a shaky checklist.

---

## 4. GATE 3 (deliver) — all five conditions, no exceptions

1. **Zero confirmed defects remain.**
2. **`check_pdf.py` is still green**, re-run against the *final rebuilt* PDF — never a verdict carried forward from an earlier run or session.
3. **Pass 3(a) covered every page**, stated as a count (e.g. "15/15 pages inspected"), not "spot-checked".
4. **Pass 3(b) was a full read in both directions**, with a per-section reading claim naming source pages against script blocks. **No coverage percentage, similarity score, or grep result may substitute for this.**
5. **The rebuild is reproducible** — regenerate from the final script and confirm the PDF matches the committed one (same page count, same extracted character count, same image count; an embedded timestamp is the only acceptable byte difference).

**Say "PASS" only when all five hold.** If Pass 3(b) was in fact a token screen, the honest verdict is *Gate 3 not yet satisfied* — say that instead. A chapter wrongly marked closed is worse than one openly marked incomplete, because it will never be looked at again: **Ch9 was marked CLOSED twice while still defective.** Never let a green linter stand in for the content read.

---

## 5. Deliver

Deliver the full chapter folder: the PDF, the `.py` script (saved as a file, never only pasted in chat), the inventory with **every row ticked**, and `assets/` with every verified monochrome figure. (Plus the repo-level `neet_template.py` and `check_pdf.py`, which the chapter depends on but does not duplicate.)

Along with the files include:
- A **section-wise coverage confirmation** — e.g. *"14.1 — 12/12 body facts, 2/2 summary-unique, 3/3 figures embedded + verified mono, all figure labels in text."*
- A short **Coverage note**, written into the chapter's **inventory `.md`** and **never into the PDF** (Rule 6), with these **fixed headings** so an audit prompt can consume it mechanically:
  - **Compression decisions** — what was merged/reformatted and why it's safe
  - **Exercise classification** — every exercise numbered, marked COVERED (naming the answering section) or GAP (naming where its added answer lives), per Rule 2
  - **Drift caught and fixed** — anything Pass 3 found
  - **Figures requiring manual attention** — figures that failed extraction/conversion/verification (write "None" if empty)
  - **Color-dependent figures** — figures whose meaning relied on color, and where that distinction is now stated in words (write "None" if empty)
  - **Source problems** — any part of the source flagged garbled/unrecoverable (write "None" if empty)
  - **Linter verdict** — the final `check_pdf.py` summary (fail/warn counts), with any accepted WARN justified

If an adversary-audit error list comes back later, the expected fix is: open that same `.py`, edit the flagged block (found via `# ---- N.N ----`), rerun it, re-run `check_pdf.py` to confirm the gate is still green, and hand back the regenerated PDF + updated script — not a rewrite from scratch.

---

## 6. Big-chapter note

Pass 3 for a big chapter is **a single whole-chapter verification**, exactly as the normal Pass 3, over the merged PDF. The deliverable is still one merged PDF, one script, one inventory — never two part-PDFs. The frozen whole-chapter inventory is the seam-guard.

---

## 7. Gate 3(b) verification rules (learned from the Ch12 Ecosystem audit — apply to every Gate 3(b))

1. **A "clean"/"PASS" verdict is a claim, not a fact.** Re-verify every previously-clean block with the same rigor as unread blocks; scrutinize hardest any block where a defect was previously found.
2. **Cross-document disagreement IS the finding.** Before auditing content, compare every status-bearing document — inventory, `CHAPTER_STATUS.md`, `CHAPTER_TRACKER.md` must agree. Any mismatch is itself a defect and leaves the chapter unresolved.
3. **Match the verification method to the defect class:**
   - Leaked text, clipping, layout bugs → direct inspection of rendered pages.
   - Phrasing drift, silent compression → full side-by-side reading, never skimming/summarizing.
   - Internal contradictions using legitimate vocabulary → side-by-side reading of both instances; grep/keyword cannot establish correctness.
   - Mislabeled IDs, wrong audit-trail comments → check script bookkeeping against the defect register.
   Choose the method for the defect being hunted, not the fastest method.
4. **Fail loud, not silently-plausible.** When a silent-failure mode is found, add a guard/assertion/hard check that rejects the entire class (e.g. out-of-bounds crops must error, not be silently clamped) — don't only patch the one bad instance.
5. **Metadata correctness matters as much as content correctness.** Audit trails, block markers, verification comments, defect-register IDs are deliverables — verify them against the register with the same care as reader-facing text.
6. **When a shortcut keeps getting taken, ban it.** grep may locate candidates but may **not** serve as evidence for a Gate 3(b) content verdict.
7. **Size is not a proxy for difficulty.** Set scrutiny by dependency density and cross-references, not page count. Exercise answers, appendix rows, figure labels, and summary facts can make a short chapter harder than a long one.
8. **Close the loop atomically.** When a defect is fixed, update every document that claims its status in the same session. Content fix + `CHAPTER_STATUS.md` + `CHAPTER_TRACKER.md` are one operation; until all agree, the gate stays open.

### Gate 3(b) pre-closure checklist
Before writing "Gate 3: CLOSED" anywhere, confirm:
- [ ] Every previously "clean" block was re-read this session.
- [ ] Inventory, `CHAPTER_STATUS.md`, and `CHAPTER_TRACKER.md` agree explicitly.
- [ ] Layout, drift, contradiction, and metadata defects were checked with their matching methods.
- [ ] Every discovered silent-failure mode was fixed at the guard level.
- [ ] Script comments and defect IDs match the inventory's defect register.
- [ ] `CHAPTER_STATUS.md` and `CHAPTER_TRACKER.md` were edited in this same session before closure.

### Roll-up counters (shared with Gate 1 closure discipline)
Derive roll-ups by counting rows (`grep -c` the done marker), **never by incrementing** — re-derive on every closure even when the current chapter doesn't change the total. **Name which gate closed:** "Gate 3 closed / chapter delivered" is different from "Gate 1 closed; Pass 2 not started." Only a chapter that passed all five Gate-3 conditions counts as Done.
