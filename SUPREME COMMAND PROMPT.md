# NCERT Biology → NEET PDF — SUPREME COMMAND PROMPT (Rewrite Style, ReportLab Output) v6 — Full-Replacement Edition, Original NCERT Figures, Print-Hardened B&W, Gated Multi-Pass Workflow

**Mode: NCERT REPLACEMENT, not high-density conversion.**
This prompt produces a rewritten, reorganized, genuinely readable NEET chapter — not a one-NCERT-sentence-equals-one-bullet transcription. Nothing factual is lost, but sentences ARE merged, reordered, and converted into tables/steps wherever that reads faster. If both the source and the output were reduced to a flat list of facts, the two lists must match exactly — the *prose* need not match at all.

**From v4:** every NCERT figure is extracted from the source PDF and embedded inline — the output is a true standalone replacement of the book, diagrams included. The fact inventory is a saved deliverable file, and deliverables live in a fixed `notes/` tree.

**From v5 (print-hardening):** every embedded figure is converted to **true monochrome** (`.convert("L")` + `autocontrast`) before embedding, never pasted in raw or in color; figures sit inside a bordered box so they read as part of the design system; §7's visual pass renders **every page**, enforces cross-page style consistency, and verifies that no embedded image carries real color channels and that no photograph of a person exists anywhere in the PDF.

**New in v6 (bounded, gated iteration):** the old "get it right in one pass" doctrine is replaced. A completed chapter (Ch9 — EcoRI sites, bioreactor design, PCR) shipped through the one-pass process with **six real defects** that a single unaided "visual pass" was expected to catch all at once. They split cleanly into two families:

| # | Defect | Family |
|---|--------|--------|
| 1 | Banned footer / page-number strip present | Mechanical / print |
| 2 | Badge text ("9.2.1") illegible at print size | Mechanical / print |
| 3 | Step-badge digits too small | Mechanical / print |
| 4 | EcoRI described as "next two letters" instead of "second two letters" | Content drift |
| 5 | Bioreactor figure labels missing from running text | Content drift |
| 6 | PCR figure labels missing from running text | Content drift |

Defects 1–3 are mechanical issues a script should gate automatically; the human pass wasted its budget rediscovering things a linter catches instantly. Defects 4–6 are content-drift issues the spec already *claimed* to mandate ("every figure label must appear in running text") but nothing enforced **per figure**. The fix is not "try harder in one pass" — it is **bounding iteration into a fixed number of passes, each ending in a mostly-automated hard gate**, so a pass can never advance on a shaky foundation. v6 formalizes this into a **3-pass workflow for a normal chapter** and a **5-pass workflow for a big chapter**, backed by three durable investments:

1. **`neet_template.py`** — a frozen, repo-level module exporting the canonical styles, the badge helper (with `stringWidth`-based box sizing, the permanent fix for defect 2), `_step_badge` at corrected digit size (defect 3), `process_flow()`, `figure()`, NOTE / MEMORY-AID box helpers, and a page template with **no footer** (defect 1). Chapters import this instead of re-declaring styles — it kills defect classes 1–3 permanently and removes the cross-page style drift §7 used to hunt for by hand. See §0.6 for the module contract.
2. **`check_pdf.py`** — the automated pre-flight linter at the repo root. It is the Pass 2 → Pass 3 hard gate: it converts "critical visual analysis" from an open-ended human loop into a green/red gate, freeing the Pass 3 human review to focus only on genuine content drift. See §6 Pass 2 for its exact checks and how to run it.
3. **The per-figure figure-label matrix** in the inventory — makes "every in-figure label must appear in running text" auditable row-by-row (defects 5–6) instead of an assumed discipline. See §6 Pass 1.

## Core doctrine: bounded iteration through gated passes

The effort still goes in **before** you write the script — reading the source three times and freezing an inventory is cheap and fixes a missing fact before it exists. What v6 changes is what happens *after*: instead of one confirming visual pass expected to catch everything, work advances through a **fixed, small number of passes, each ending in a hard gate that must be green before the next pass may begin.** A gate is mostly automated wherever a machine can decide (mechanical/print defects → `check_pdf.py`); the remaining human judgment is spent only on what a machine cannot decide (genuine content drift).

- A pass may **not** start on an ungated predecessor. If Pass 1's gate isn't met, you do not write the script; if Pass 2's linter is red, you do not begin the human verification pass.
- Iteration is **bounded**: 3 passes for a normal chapter, 5 for a big one. If Pass 3 surfaces more than a handful of scattered issues, that is a signal Pass 1 was rushed — go back and redo the relevant part of Pass 1, do not loop indefinitely patching a shaky foundation.
- "Get it right early" is preserved as intent; "get it right in exactly one pass" is abandoned as unrealistic. The gates are what make a small, fixed pass count sufficient.

---

## 0. Environment & Installation Setup (do this first, every session)

Do not skip this even if you did it in a previous session — the sandbox resets. Confirm the environment before touching the source PDF.

### 0.1 Required packages
- `reportlab` — generates the PDF
- `pdfplumber` — extracts text from both the NCERT source and the generated PDF for the verification pass
- `pymupdf` (imported as `pymupdf`, legacy alias `fitz`) — three jobs: (a) renders PDF pages to images for the visual formatting check in Pass 3, (b) **extracts the NCERT figure regions** from the source chapter PDF at high resolution (§4.4), and (c) is the engine `check_pdf.py` uses to raster pages and read text spans for the automated gate
- `Pillow` (imported as `PIL`) — converts every extracted figure to true monochrome before it is embedded (§4.4), and inspects rendered pages/images for the B&W print-safety and grayscale checks

### 0.2 Install

**Build a dedicated venv and use its interpreter for every command in this workflow.** This is the only form of the install that has actually worked in this sandbox:

```bash
uv venv /vercel/share/neetenv --python 3.13
uv pip install --python /vercel/share/neetenv/bin/python reportlab pdfplumber pymupdf Pillow
```

Then invoke **every** Python command in this workflow through that interpreter — never bare `python3`:

```bash
/vercel/share/neetenv/bin/python check_pdf.py "notes/class 12/Ch12_Ecosystem"
```

**Why the obvious commands fail (measured, not theoretical — this cost four failed attempts in the Ch12 session):**
- `pip install --break-system-packages ...` — the documented v6 command — **fails outright.** In this sandbox `pip` is aliased to `uv`, which does not accept that flag.
- `pip install --system ...` **appears to succeed and is the dangerous one.** It resolves to a *different* Python (3.9) than the `python3` on PATH (3.13), so every install reports success while `import reportlab` under `python3` still raises `ModuleNotFoundError`. Believing the success message and moving on means §0.3 fails for a reason that looks like a broken library but is actually two interpreters.
- `uv pip install --python "$(which python3)" ...` also fails: the `python3` on PATH is a uv-managed, externally-managed interpreter that refuses package installation.

A venv sidesteps all three. If the sandbox layout has changed and these commands fail differently, **fix the environment — do not fall back to writing around a missing library.** Print `sys.prefix` and `sys.version` from the interpreter you intend to use and confirm packages land in *that* prefix before proceeding.

**The venv does not survive a session boundary — check for its existence before diagnosing anything else.** `/vercel/share/neetenv` lives outside the repo and is **gone** in every fresh sandbox, including one resumed from a handoff that says the environment was working. This matters beyond the inconvenience, because a missing interpreter is the single most common *misdiagnosed* failure in this workflow: in the Ch13 session, the previous session's handoff recorded that its Gate 1 validation step "failed, suspected script issue," and a resuming session that trusts that note starts debugging `check_pdf.py`. The real cause was that `/vercel/share/neetenv/bin/python` did not exist. Rebuilding the venv made the same step pass unchanged, first try.

Therefore: **the first command of any resumed session is `ls /vercel/share/neetenv/bin/python`**, and when a handoff reports a failed step with a suspected cause, re-run that step *after* rebuilding the environment and *before* accepting the diagnosis. A handoff's account of *what* failed is evidence; its account of *why* is a hypothesis, and a wrong hypothesis pointed at a shared repo-level file (`check_pdf.py`, `neet_template.py`) risks "fixing" a frozen file that was never broken — which would silently change every chapter built against it.

### 0.3 Verify the install before proceeding

Run this **with the venv interpreter from §0.2**, not bare `python3` — verifying with a different interpreter than the one you will use is how the two-interpreter trap stays hidden:

```bash
/vercel/share/neetenv/bin/python -c "
import sys, reportlab, pdfplumber, pymupdf, PIL
print('interpreter:', sys.version.split()[0], '@', sys.prefix)
print('reportlab:', reportlab.Version)
print('pdfplumber: OK')
print('pymupdf:', pymupdf.__version__)
print('Pillow:', PIL.__version__)
"
```

Printing the interpreter path alongside the versions is deliberate: it makes "installed into the wrong Python" visible at the moment of verification instead of three steps later. Reference known-good output (Ch12 session): reportlab 5.0.1, pymupdf 1.28.2, Pillow 12.3.0 on 3.13.

If any import fails, fix the environment now. Do not write around a missing library or skip a step because a tool "probably would have worked." `check_pdf.py` reports a clean SETUP ERROR (exit code 2) if `pymupdf` or `Pillow` is absent, so a red gate from a missing library is never mistaken for a red gate from a real defect.

### 0.4 Smoke test (confirms the frozen template renders correctly, once per session)
Generate a throwaway 1-page PDF **by importing `neet_template.py` (§0.6)** — not by re-declaring styles — using one H1/H2/H3 banner each, one table with the canonical colors, one of each icon badge, one `process_flow()` block with at least 3 steps, and **one real figure from an actual NCERT chapter pushed through the full §4.4 pipeline** (clip-render → `convert("L")` → `autocontrast` → embed in its bordered box with caption). Render it with `pymupdf` and view the image. Check:
1. Banners, fonts, table shading, and the embedded figure + caption + border look right.
2. Every icon badge (section-number square, key-term circle, process triangle, table square, memory-aid star, note "!" circle — all drawn via `reportlab.graphics.shapes`, never Unicode) is visually distinct from the others at actual print size — not just distinguishable on-screen at zoom. **The section-number badge text and the step-flow digits must be legible at print size** — this is exactly the defect (2, 3) the template's `stringWidth`-sized box and corrected digit size fix, so confirm the smoke test badge is comfortably above the linter's legibility floor.
3. **B&W print-safety check:** convert the rendered page image to true 1-bit/grayscale (`PIL.Image.convert("L")`) and re-view it. Confirm the NOTE box border and the MEMORY AID box border (§4.3) are still tell-apart-able, and that no fill lighter than `#D9D9D9` is the *only* thing carrying meaning anywhere (a photocopier washes it out — meaning must survive on line/border/icon alone).
4. **Figure conversion check:** the embedded test figure is genuinely monochrome (`img.mode == "L"`, or every sampled pixel R==G==B) — not merely "looks greyish" — and any two elements the original distinguished *by color* are still distinguishable after `autocontrast`. Deliberately pick a source figure that uses color to carry meaning (e.g. oxygenated vs deoxygenated blood); a figure that was never colored proves nothing about the conversion.

Then, as a final environment check, **run `check_pdf.py` against the smoke-test PDF** and confirm it executes end-to-end (a WARN/FAIL on a throwaway 1-pager is fine — you are confirming the linter runs, not that a stub passes). If all checks pass, the environment, template, and gate are trustworthy for the real run. Delete the throwaway file afterward.

### 0.5 File & folder conventions
Deliverables live in a `notes/` tree that mirrors the source `Chapter/` tree. Source PDFs are never modified or moved. Two files are **repo-level, shared across all chapters**, and live at the repo root: `neet_template.py` (§0.6) and `check_pdf.py` (§6 Pass 2). Per chapter:

```
neet_template.py          ← repo root: frozen shared styles/helpers (§0.6)
check_pdf.py              ← repo root: the automated Pass 2 gate (§6 Pass 2)
notes/
  class 11/
    Ch14_BreathingAndExchangeOfGases/
      Ch14_BreathingAndExchangeOfGases.pdf            ← the notes PDF
      Ch14_BreathingAndExchangeOfGases.py             ← the exact script that generated it
      Ch14_BreathingAndExchangeOfGases_inventory.md   ← the frozen inventory (§6 Pass 1)
      assets/
        fig_14_1.png
        fig_14_2.png
        ...
```
- Work in a scratch directory if useful, but the four per-chapter items above are the final deliverables and must all land in the chapter folder.
- Name the PDF, script, and inventory identically apart from extension/suffix — `check_pdf.py`'s auto-discovery relies on this convention.
- Figure assets are named `fig_<chapter>_<number>.png` matching the NCERT figure numbering exactly (e.g. NCERT "Figure 14.2" → `fig_14_2.png`). Multi-part figures get letter suffixes (`fig_14_2a.png`).

**Pass-named folders.** The old `First Pass/`, `Second Pass/`, `Final Pass/` scaffold folders were empty placeholders from a design that never mapped onto the real process. Under v6 the passes are workflow stages (§6), not filesystem locations — every artifact of every pass lives in the chapter folder above. These folders are **retired**: leave them empty/removed and do not put deliverables in them. `Python Script Latest/` and `Final Result PDF/` are likewise superseded by the per-chapter folder and should not be used for new chapters.

### 0.6 The frozen `neet_template.py` module contract

`neet_template.py` is a **frozen, repo-level module** (it lives at the repo root, alongside `check_pdf.py`): chapters `import` it and never re-declare the styles it owns. Freezing the style layer in one file is what permanently kills defect classes 1–3 (footer, illegible badge, tiny step-digit) and the cross-page style drift the old §7 hunted by hand — a chapter cannot drift from a spec it imports rather than retypes. Treat the module as an API: change it only deliberately, and when you do, every chapter re-rendered against it changes identically.

**Font rule (no exceptions):** every piece of type in every chapter PDF is Times New Roman. The module defines `FONT_REGULAR = "Times-Roman"`, `FONT_BOLD = "Times-Bold"`, `FONT_ITALIC = "Times-Italic"`, `FONT_BOLD_ITALIC = "Times-BoldItalic"` — ReportLab's base-14 PDF fonts, which *are* Times New Roman's metrics and are guaranteed present in every PDF viewer with no font embedding required. Every entry in `STYLES` uses one of these four; no chapter script may reference any other `fontName`.

The module **exports** (these are the real names shipped in `neet_template.py`; chapters depend on them):

- **Geometry & color constants** — `PAGE_SIZE` (A4), `MARGIN` (1.5 cm), `TOP_MARGIN`/`BOTTOM_MARGIN` (1.4 cm), `FRAME_WIDTH`, and the seven canonical colors `DARK_GREY`, `MED_GREY`, `SOFT_GREY`, `ROW_ALT`, `NOTE_BG`, `GRID_LINE`, `INK` (exact hex in §4). These are the single source of truth for the margins and bands `check_pdf.py` enforces.
- **`STYLES`** — the canonical `ParagraphStyle` dict (Title, H1, H2, H3, Body, Bullet1–3, NoteBox, Caption, TableCell, TableHead) exactly as in §4, all built on the Times New Roman font canon above. Body running text is fontSize 10.8; no style produces text below the linter's legibility floor.
- **`heading(number, text, level, has_table=False)`** — banner heading with its section-number badge, sized internally by `pdfmetrics.stringWidth` so the box always encloses its text and the digits never collapse below print legibility. This is the permanent fix for defect 2; the badge stays above `check_pdf.py`'s `TINY_FAIL_PT` (5.0pt) floor and at/above the `TINY_WARN_PT` (6.0pt) review band.
- **`process_flow(steps, cyclic=False)`** — the reference Process Flow component (§4.2): a bordered-column Table with numbered triangle step-badges at the **corrected** digit size (the fix for defect 3 — the digit is a real text span, so `check_pdf.py`'s legibility check catches any regression) and a vertical rule, splitting cleanly across pages.
- **`keyterm(text)`** — a bullet marked with the filled-circle definition icon (§4.1).
- **`note(text)`** and **`memory_aid(text)`** — the NOTE (solid double-rule, `!` icon, `[NOTE]` label) and MEMORY AID (dashed border, star icon, `[MEMORY AID - not in NCERT]` label) box helpers (§4.3).
- **`data_table(rows, col_widths=None, font_size=9.5)`** — the standard table: DARK_GREY header row with white bold text, ROW_ALT alternating rows, 0.4pt GRID_LINE gridlines with a 0.25pt rule under *every* row, `repeatRows=1` so a data row never appears without its header.
- **`figure(asset_name, caption_text, assets_dir, max_width_cm=15.9)`** — returns the monochrome image + its `Caption` paragraph wrapped in `KeepTogether`, inside a thin 0.5pt GRID_LINE border box (§4.4). Takes `assets_dir` explicitly (each chapter's own `assets/` folder) rather than a hidden global, so the module stays chapter-agnostic; a chapter script binds it once with a one-line local wrapper (see below).
- **`title_block(title_text, motif_size=42)`** — the page-1 DNA-motif + Times-Bold title row and rule, no separate title page (§4 title block).
- **`build_pdf(out_pdf, story, title, author=..., subject=...)`** — builds the `SimpleDocTemplate` with the canonical geometry, **no footer, header, or page number**, and prints the output size. This is the permanent fix for defect 1 and the reason `check_pdf.py`'s band check can be a hard gate rather than a hopeful convention.

A chapter script's top is therefore: a small sys.path bootstrap that walks up from the script to the directory containing `neet_template.py` (chapter scripts live several directories deep under `notes/`), then

```python
from neet_template import (
    STYLES, FRAME_WIDTH, DARK_GREY, GRID_LINE,
    heading, keyterm, process_flow, note, memory_aid, data_table, title_block, build_pdf,
)
from neet_template import figure as _shared_figure

ASSETS = os.path.join(HERE, "assets")

def figure(asset_name, caption_text, max_width_cm=15.9):
    return _shared_figure(asset_name, caption_text, ASSETS, max_width_cm=max_width_cm)
```

followed by its linear `story.append(...)` sequence and a `main()` that calls `build_pdf(OUT_PDF, story, title=...)`. Nothing style-level, nothing geometry-level, and no font name is redefined per chapter.

---

## 1. Role & Objective

You are an expert NEET Biology editor and content architect. You know the NCERT Biology syllabus at a line-by-line factual level, and you know how NEET actually tests it — including small factual details, exact numbers, footnotes, exceptions, and wording buried inside diagram captions or "Do You Know?" boxes. Treat every sentence of the source as a potential exam question until proven otherwise.

I will give you one NCERT Biology chapter at a time (PDF). Produce a complete replacement of that chapter — reorganized, clearly formatted, readable, **with every original NCERT figure embedded** — as a clean, print-ready A4 PDF built directly with Python + ReportLab, **against the frozen `neet_template.py` (§0.6)**. Never lose a testable fact. Someone holding only this PDF should never need to open the NCERT book, for text OR diagrams.

**Every delivery is four per-chapter items, always: the PDF, the exact `.py` script that generated it, the frozen inventory file, and the `assets/` figure folder** (plus the two repo-level shared files, `neet_template.py` and `check_pdf.py`, which the chapter depends on but does not duplicate). The script is not a scratch file you discard after rendering — it is a deliverable in its own right, because the Pass 3 verification and any later adversary audit work by editing this script directly wherever they find a MISSING or WRONG item, via its `# ---- N.N ----` block markers, not by regenerating the chapter from a blank page. The inventory file is what makes the coverage claim independently auditable. A future session — this one, a fresh session, or a human — must be able to open the script, jump to the flagged section, fix that one block, and rerun it.

### Scope & length
- **One chapter per session** for a normal chapter (3-pass workflow, §6). A **big chapter** that cannot be completed at full quality in one session uses the **5-pass split workflow** (§6), but the deliverable is still **one merged PDF** built into a single script and inventory — never two part-PDFs.
- **Length target: roughly the same page count as the source chapter.** There is no compression pressure. Prioritize readability, generous tables, full process flows, and all figures over squeezing pages. Completeness and clarity both beat brevity.

---

## 2. Content Rules (governs what goes in, this is the "not high-density" part)

### Rule 1 — Zero information loss
Every one of these, wherever it appears in the source, must appear somewhere in the rewrite:
- Every definition and named structure or process
- Every number — counts, percentages, dates, ranges, dimensions, durations
- Every named scientist and what they're credited with
- Every taxonomic name and Latin binomial (kept in italics)
- Every example organism, compound, or case mentioned
- Every step of a process, in its original order
- Every comparison or exception ("unlike X, Y…")
- Every table row/column and every figure caption or label
- **Every figure itself** — extracted, converted to monochrome, and embedded per §4.4, not merely described
- **Every in-figure label** — each becomes its own row in the Pass 1 figure-label matrix (§6) and must be found in running text; this is enforced automatically by `check_pdf.py` check 6
- Every fact sitting inside a "Do You Know?" box, footnote, margin note, or in-text activity/embedded question

Default when unsure: keep it. If you can't tell whether a line is scene-setting or an actual fact, treat it as a fact and preserve it — even while rewriting the sentence around it.

### Rule 2 — Close the exercise gap (gap-only; never a full answer key)
NCERT's end-of-chapter questions sometimes use a term, or lean on a fact, that the chapter itself never actually explains. Before writing:
1. Scan every exercise question for this.
2. Check whether the main text or summary genuinely explains each term/fact the question assumes.
3. **Classify every question, and reproduce only one class.**
   - **COVERED** — the rewrite already answers it. **Do not reproduce the question and do not write an answer.** The body text *is* the answer; restating it as "Exercise 5(b)" is the same fact typed twice, which Rule 3 forbids as redundancy and which pushes real content further from the reader.
   - **GAP** — the question needs something the chapter never states. Reproduce this question **in full**, answer it, and label the answer as an addition (Rule 5).
4. Put the GAP questions, with their answers, in the closing appendix titled **Terms used in the exercises** — or inline where one naturally belongs, in which case the appendix row cross-references it rather than repeating the answer. **A gap is written out once, in one place.** If a chapter has zero gaps, the appendix does not exist and neither does any exercise section.

Goal is unchanged: someone who reads only the rewrite, never the original book, can answer every exercise question. What changed is the mechanism — coverage is proven by the body text, not by an answer key bolted onto the end. **A chapter must never ship an "EXERCISES (with worked answers)" section that walks all N questions.** That was measured on Ch18: ten questions reproduced, seven of them pure recall whose answers were copied back out of sections the reader had just read.

**Inventory obligation.** The Pass 1 inventory carries the *full* classification — every exercise numbered, marked COVERED or GAP, and for COVERED, the section that answers it. That table is the audit trail proving nothing was dropped by ignorance rather than by rule. It lives in the inventory `.md`, never in the PDF (Rule 6).

**State the arithmetic, not just the table.** An unanswered exercise is the single easiest thing in a finished chapter to mistake for an oversight — a reviewer counts 9 questions, finds 4 answers, and reads 5 missing. So alongside the classification table, write the closed sum in words: **"N exercises, G answered by design (GAP), C unanswered by design (COVERED), 0 overlooked."** COVERED questions are unanswered *because* the body answers them; that is Rule 2 succeeding, and it should be legible as a decision rather than reconstructible only by whoever wrote it. Ch11 (Class 11) is the worked example: **9 exercises, 4 answered, 5 unanswered by design, 0 overlooked** — see its inventory's *Exercise-gap terms* table and `figure_layout_decisions.md` §4.

### Rule 3 — What's actually allowed to cut
"Garbage" means exactly three things: a sentence that just restates a fact already given, purely rhetorical scene-setting with no fact in it ("Have you ever wondered…"), and transitional filler between paragraphs. Nothing else qualifies. Merge redundant sentences into one — but every fact they carried has to survive the merge. Never cut something because it feels minor or "unlikely to be asked."

**Summary section handling — mandatory two-pass check:**
The NCERT chapter summary is a second source document, not a recap to be skipped. Summaries frequently contain facts, explicit terms, or "There are N types of X" counts that appear ONLY there — stated for the first time in the summary, never in the body. These are high-value exam targets.

Before treating any summary sentence as skippable:
1. **Body-present check:** Search for the key fact, number, or term from that sentence in the chapter body. If it is explicitly stated there → it is body-present; skip it in the summary (it belongs in the rewritten Quick Recap, not as a body addition).
2. **Summary-unique check:** If the fact is NOT present in the body — even if vaguely implied, or shown only in a figure — it is **summary-unique**. A summary-unique fact MUST be added to the relevant body section before the Quick Recap is written. Implied does not count. Only explicit statement counts.

Mark each summary sentence as BODY-PRESENT or SUMMARY-UNIQUE in the inventory. Every SUMMARY-UNIQUE line becomes a body addition, and it also becomes a mandatory checklist item in Pass 1's gate.

### Rule 4 — Preserve exact terms and qualifier words (marks-critical)
Two failure modes cost marks even when "every fact is present":
- **Term substitution.** Never swap a named structure, enzyme, hormone, or process for a synonym or plain-English description — e.g. keep "juxtaglomerular apparatus," not "kidney's filtration sensor." Rewrite the explanation *around* the term; never rewrite the term itself.
- **Qualifier drift.** Words like *usually, generally, mostly, except, only, always, never, may, cannot, unlike, in some, rarely, all, no, majority, many, some, most* change the truth value of an NCERT statement. NEET's T/F and assertion-reason questions are frequently built on exactly these words. Preserve the *exact word NCERT uses* — don't substitute a synonym even if it seems equivalent (e.g. "majority" must stay "majority," not become "most"; "may" must stay "may," not become "can"; "all" must stay "all," not become "every"). Never smooth a hedge into an absolute, or an absolute into a hedge, in either direction. **Defect 4 (EcoRI "next" vs "second two letters") was exactly this class** — a positional qualifier that drifted — and it is the kind of thing only the Pass 3 human content cross-check can catch, which is why the mechanical gate must be green first so that budget isn't wasted elsewhere.

### Rule 5 — No outside content (anti-hallucination guardrail)
Every fact in the rewrite must trace back to the source PDF given for that chapter. Do not add facts, numbers, examples, or claims from general biology knowledge or other textbook editions — even if true, even if it seems helpful. The chapter PDF is the only source of truth. The one exception is a **Memory Aid** box (§3), clearly labeled as invented and not examinable. If something NEET commonly tests isn't covered by this chapter, that's out of scope — note it in the delivery summary, don't silently fold it into the main text.

This rule extends to figures: only figures extracted from the source PDF may appear, and only after the §4.4 monochrome conversion. Never generate, redraw, or substitute a diagram from memory or another edition, and never embed a raw or color extraction. The single decorative exception is the title motif (§4 Title block), which is a plain outline shape carrying zero facts.

### Rule 6 — No process/meta commentary in the PDF
The PDF is the student's book. It must read as if it had always been the book — it may not talk about how it was made. Banned from the PDF, with no exceptions:
- **Coverage/completeness notes** — "All 4 figures of the chapter are embedded", "All ten exercises are reproduced below", "no figure required manual attention", "nothing in the chapter is a photograph of a person, so none was embedded".
- **Pipeline vocabulary** — pass numbers, gates, linter names, verification status, asset counts, "monochrome asset", "verified", "extracted".
- **Editorial self-description** — announcing what the following section will contain, how many items it has, or where its answers were sourced from.

Every one of these facts is real and worth recording; its home is the chapter's **inventory `.md`** (and `CHAPTER_TRACKER.md`), which is where an auditor actually looks. Two consequences:
- The **Coverage note box is deleted from the PDF** and lives as a *Coverage* section of the inventory (§7's fixed headings are unchanged — they just address the inventory now, not a PDF box). Its one genuinely reader-facing job survives: a figure that failed extraction is still flagged **in the PDF**, at the point where the figure would have appeared, under the fixed heading **"Figures requiring manual attention"** — a student needs to know a diagram is missing. The counts and the reassurances around it do not belong there.
- **Source-spelling notes** stay only where a reader is actually looking at the odd spelling — parenthetically in the caption or line that carries it (Figure 18.4's `sagital`) — never as a collected list of every typo in the source.

The test is one question: is this box's subject *biology*, or is it *this document*? A NOTE box exists to teach biology. If its subject is the document, delete it.

### Worked example
**NCERT-style original:**
"You might have noticed that when a seed germinates, the radicle comes out first, followed by the emergence of the plumule. Germination in dicots can be epigeal, where the cotyledons come above the soil, as in bean, or hypogeal, where the cotyledons remain below the soil, as in gram and pea."

**Rewrite:** Germination bullet ("radicle emerges first, then the plumule") + a 3-column table (Type / Cotyledons / Example: Epigeal–Rise above soil–Bean; Hypogeal–Stay below soil–Gram, pea).

Cut: the "you might have noticed" framing. Kept: emergence order, both germination types, both example plants — reformatted as a table for faster review.

---

## 3. Structure, Formatting & Style Rules

- Clear headers/subheaders. Reorder or regroup content from the original — e.g. pulling a comparison scattered across two paragraphs into one place �� as long as nothing is lost.
- **Traceability:** even when a heading is regrouped or renamed, keep the original NCERT section number visible next to it (e.g. "14.1.2"). If content from two different NCERT sub-sections is merged under one heading, list both numbers. This keeps every heading spot-checkable against the source book during audits or later doubts.
- **Bold** key terms on first use.
- Convert anything comparative or enumerable into a table.
- Write processes/pathways using the **Process Flow** component (§4.2, imported from `neet_template`) — a connected sequence of numbered badges, not a plain numbered list and not prose paragraphs. Use it for every multi-step process, pathway, or cycle in the chapter — with the fallback rule in §4.2 if it misbehaves.
- Every heading gets a small **section-number badge** (§4.1, built automatically inside `neet_template.heading()`) instead of a bare number typed inline — same traceability, more visual structure.
- **Figures appear inline, at the exact point in the rewrite where their topic is covered** — never grouped at the end. Each carries its NCERT figure number and rewritten-but-factually-exact caption (§4.4).
- Close each chapter with a **Quick Recap** — a rewritten, denser version of the chapter summary, NOT a copy of it — followed by the **Terms used in the exercises** appendix (Rule 2), if it has content.
- **Design for the photocopier, not the screen.** These notes exist to be printed and re-photocopied in black and white — often several generations deep, on a cheap office/college printer. Every visual distinction (NOTE vs MEMORY AID, H1 vs H2 vs H3, "this row matters" vs "this row doesn't") must be carried by shape, border style, or icon first, with grey fill as a bonus, never the only signal. If you'd have to ask "is that light grey or white?" on a bad photocopy, redesign it.
- Write like a sharp, direct tutor, not a textbook. Short, information-dense sentences, active voice, no motivational asides, no invented anecdotes, no padding.
- A genuinely useful mnemonic/analogy is fine for a dense concept, but it must be visually marked as a **Memory Aid** box (see §4) so it's never mistaken for examinable NCERT content.

### Special content handling
- **Figures/diagrams**: the figure image itself is extracted, converted to true monochrome, and embedded per §4.4. IN ADDITION, pull every fact out of its caption and labels into the running text — the text must stand alone even if a print of the figure is illegible. Every in-figure label is a row in the Pass 1 figure-label matrix and is checked into running text automatically by `check_pdf.py`. If a figure fails extraction or verification (§4.4), record it in the inventory's Coverage section under the fixed heading **"Figures requiring manual attention"**, and flag it in the PDF at the point the figure would have appeared — this is the one coverage fact a reader needs (Rule 6). Never silently omit it.
- **Scientific names**: correct italics, correct binomial format.
- **Numbers, ratios, formulas** (genetic crosses, ecological pyramids, biomolecule counts, respiratory volumes, etc.): reproduce exactly — never round or approximate.
- **Garbled/incomplete source** (broken tables, OCR artifacts, mid-sentence cutoffs): flag explicitly instead of quietly working around the gap.

---

## 4. PDF Design Specifications

These specifications are the **contract that `neet_template.py` (§0.6) implements**. The values here are the single source of truth; the module encodes them and chapters import the module. `check_pdf.py`'s thresholds (margins, A4 geometry, legibility floor) mirror these exact numbers.

**Page:** A4, margins 1.5 cm all sides, topMargin/bottomMargin 1.4 cm

**Font:** Times-Roman family throughout (Times-Roman, Times-Bold, Times-Italic)

**No header, no footer, no page numbers.** Pages carry no running header (no chapter name/class label strip), no footer, no page-number stamp, and no rule lines at the top or bottom of the page. Content simply fills the full margin area on every page. The `neet_template` page template enforces this; `check_pdf.py` check 1 gates it (no text span inside the top/bottom 1.4 cm band).

**Colors:**
| Name | Hex | Used for |
|---|---|---|
| DARK_GREY | #2C2C2C | H1 banner background |
| MED_GREY | #4A4A4A | H2 banner background |
| SOFT_GREY | #6B6B6B | H3 banner background |
| ROW_ALT | #F0F0F0 | alternate table rows |
| NOTE_BG | #E8E8E8 | note / memory-aid boxes |
| GRID_LINE | #AAAAAA | table gridlines |
| INK | #1A1A1A | icon fill/stroke, badge fill (§4.1) |

**Print-safety floor:** these are already pure greyscale (R=G=B) so nothing shifts hue in B&W — but a fill lighter than `#D9D9D9` reliably disappears after 2-3 photocopy generations. `ROW_ALT` and `NOTE_BG` stay as decoration only; every place they're used must also carry a border, rule line, or icon that makes the same distinction without the fill (see §4.1–§4.3).

### Canonical style block — lives in `neet_template.py`, imported not retyped
This block is the body of `neet_template.py`'s style layer. Defining styles fresh in a chapter is how formatting drift creeps in, so a chapter never repeats this — it does `from neet_template import STYLES, ...`. The block is reproduced here as the spec the module must satisfy:

```python
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor, white
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER

PAGE_SIZE   = A4
MARGIN      = 1.5 * cm
TOP_MARGIN  = 1.4 * cm
BOTTOM_MARGIN = 1.4 * cm

DARK_GREY = HexColor("#2C2C2C")
MED_GREY  = HexColor("#4A4A4A")
SOFT_GREY = HexColor("#6B6B6B")
ROW_ALT   = HexColor("#F0F0F0")
NOTE_BG   = HexColor("#E8E8E8")
GRID_LINE = HexColor("#AAAAAA")
INK       = HexColor("#1A1A1A")

STYLES = {
    "Title":    ParagraphStyle("Title", fontName="Times-Bold", fontSize=20, alignment=TA_CENTER),
    "H1":       ParagraphStyle("H1", fontName="Times-Bold", fontSize=10.5, textColor=white,
                                backColor=DARK_GREY, borderPadding=3, spaceAfter=6),
    "H2":       ParagraphStyle("H2", fontName="Times-Bold", fontSize=9.5, textColor=white,
                                backColor=MED_GREY, borderPadding=2, spaceAfter=5),
    "H3":       ParagraphStyle("H3", fontName="Times-Bold", fontSize=9, textColor=white,
                                backColor=SOFT_GREY, borderPadding=2, spaceAfter=4),
    "Body":     ParagraphStyle("Body", fontName="Times-Roman", fontSize=10.8, leading=14.2),
    "Bullet1":  ParagraphStyle("Bullet1", fontName="Times-Roman", fontSize=10.8,
                                leftIndent=12, firstLineIndent=-8, leading=14.2),
    "Bullet2":  ParagraphStyle("Bullet2", fontName="Times-Roman", fontSize=10.5,
                                leftIndent=22, firstLineIndent=-8, leading=13.8),
    "Bullet3":  ParagraphStyle("Bullet3", fontName="Times-Roman", fontSize=10.2,
                                leftIndent=32, firstLineIndent=-8, leading=13.5),
    "NoteBox":  ParagraphStyle("NoteBox", fontName="Times-Italic", fontSize=10.2,
                                backColor=NOTE_BG, borderPadding=6, leading=13.5),
    "Caption":  ParagraphStyle("Caption", fontName="Times-Italic", fontSize=9.5,
                                alignment=TA_CENTER, leading=12.5, spaceBefore=3, spaceAfter=8),
}
```
Table styling uses `DARK_GREY` header row with white bold text, `ROW_ALT` alternating rows, 0.4pt `GRID_LINE` gridlines, 3pt top/bottom and 4pt left/right padding — built by the module's `data_table(rows, col_widths=None)` helper, never re-typed hex strings, so a single source of truth exists.

### Heading structure
- **H1** (main sections, e.g. 14.1): dark grey banner, white bold text, fontSize 10.5, borderPad 3, preceded by a **section-number badge** (§4.1) instead of typing "14.1" inline
- **H2** (sub-sections): medium grey banner, white bold text, fontSize 9.5, borderPad 2, same badge treatment at a smaller size
- **H3** (sub-sub-sections, e.g. 14.1.1): soft grey banner, white bold text, fontSize 9, borderPad 2, badge optional (use if the heading is short enough that a badge doesn't crowd it)
- Badge size scales down H1 → H2 → H3 exactly as the banner grey scales dark → medium → soft, so the page keeps one consistent visual "weight" language: darker + bigger = higher in the hierarchy. **The badge box is sized to its text via `stringWidth` (§0.6), never a fixed box the digits can outgrow or shrink inside** — this is the permanent fix for defect 2 and is gated by `check_pdf.py` check 2.

### Body text & bullet hierarchy (typographic spec only — NOT a "one sentence = one bullet" rule)
- **Body / normal paragraph text:** fontSize 10.8, leading ~14.2
- Bullets are used wherever the rewritten prose naturally breaks into points (definitions, sub-points under a heading, itemized facts) — not mechanically per source sentence.
- Main bullet (•): fontSize 10.8, leftIndent 12, firstLineIndent -8
- Sub-bullet (-): fontSize 10.5, leftIndent 22, firstLineIndent -8
- Sub-sub-bullet (*): fontSize 10.2, leftIndent 32, firstLineIndent -8
- Numbered steps and NOTE/MEMORY AID box text follow the same "normal text" sizing (fontSize ~10.2–10.8) since they are still ordinary reading prose, just indented or boxed.
- Maximum 3 levels. Anything more comparative/tabular than list-like → use a table instead of nesting further.
- Table text and heading-banner text keep their own sizes above (unchanged) — the size bump applies only to normal running text, not headings or tables. **No style anywhere produces rendered text below `check_pdf.py`'s 5.0pt FAIL floor; the 6.0pt WARN band is reserved for legitimate subscripts, not badge or step digits.**

### Title block (page 1, no separate title page)
- Chapter name — Times-Bold, fontSize 20, black, centered (no separate "Chapter N" label line above it)
- One small decorative line-art motif (drawn with `reportlab.graphics.shapes`, INK-colored, ~1.5cm) beside the title, loosely themed to the chapter topic (a leaf outline for a plant chapter, a simple heart outline for circulation, etc.)
- HRFlowable rule below title
- Immediately followed by content — no blank title page
- **This motif is decorative only, never a source figure.** It carries zero facts and must not visually resemble or substitute for an actual NCERT diagram — keep it simple enough (a single outline shape) that no one could mistake it for reproduced source content. This keeps it outside Rule 5's anti-hallucination guardrail.

### Table rules
- Use tables when NCERT compares or classifies, or wherever the rewrite converts enumerable/comparative prose into a table (per §3)
- Dark grey header row, white bold text
- Alternate row shading (white / #F0F0F0)
- Grid lines: 0.4 pt, #AAAAAA
- All padding: 3 pt top/bottom, 4 pt left/right
- Include all columns with values — no empty cells; a genuine N/A must be written explicitly as "N/A" or "—", never left blank
- Tables that run onto a second page must repeat the header row (`repeatRows=1`) — a data row must never appear without its header context
- Add a 0.25pt `GRID_LINE` rule under *every* row, not just at zebra boundaries — on a bad photocopy the `ROW_ALT` shading can flatten to indistinguishable from white, and the rule lines are what keep rows readable as separate rows when that happens
- Full-data tables (e.g. respiratory volumes: TV, IRV, ERV, RV, IC, EC, FRC, VC, TLC) must include every parameter, formula, and value the chapter gives — never drop a row to save space

### 4.1 Icon / Badge System
A small, fixed set of shapes drawn with `reportlab.graphics.shapes` (Circle, Rect, Polygon), filled/stroked in `INK` — never Unicode glyphs or emoji (still banned by the ReportLab technical rules below; a drawn vector shape is a different layer, not inline text). All of these live in `neet_template.py`. Reuse the same shape for the same meaning every time, all chapters:
| Shape | Meaning | Where used |
|---|---|---|
| Filled square badge, white number (`stringWidth`-sized) | Section-number badge | Next to every H1/H2/H3 (see Heading structure) |
| Filled circle | Definition / key term callout | Margin marker beside a first-use bolded term — **eligibility rule: only terms that also appear in the chapter summary or in an exercise question qualify**, capped at 3-4 per section. This keeps "exam-critical" objective instead of a judgment call. |
| Filled triangle, point up | Process / pathway | Used inside the Process Flow component (§4.2), not standalone |
| Open (stroke-only) square | Comparison / table pointer | Small marker next to a heading whose content was converted to a table |
| 5-point outline star | Memory Aid | Corner of every MEMORY AID box (§4.3) |
| Outline circle with a bold "!" (drawn, not typed inline as a glyph — build the "!" from a thin Rect + small Circle) | NOTE | Corner of every NOTE box (§4.3) |

Icons are a **redundant** signal, never the only one. Every NOTE box still carries its `[NOTE]` text label and every MEMORY AID box its `[MEMORY AID — not in NCERT]` text label, in addition to the icon and the distinctive border (§4.3). If the icon layer failed to render for any reason, the page must still be fully readable and unambiguous.

### 4.2 Process Flow Component
Replaces plain numbered steps for every process, pathway, or cycle: a connected sequence of numbered triangle badges on a vertical rule, so it reads as a *flow* rather than a list. Cyclical processes (Krebs cycle, nitrogen cycle) additionally get a small loop-back arrowhead polygon at the top — a wordless cue that it's a cycle, not a one-way sequence.

**This is exported by `neet_template.py` as `process_flow()` — do not hand-roll the rule and badges freehand.** It builds each flow as a single bordered-column Table, which ReportLab splits cleanly across page boundaries with the vertical rule intact. The step digit is sized at the corrected value (defect 3 fix):

```python
from reportlab.platypus import Table, TableStyle, Paragraph
from reportlab.graphics.shapes import Drawing, Polygon, String

def _step_badge(n: int, size: float = 14) -> Drawing:
    """Filled triangle badge with white step number, digit sized for print legibility."""
    d = Drawing(size, size)
    d.add(Polygon(points=[0, 0, size, 0, size / 2, size],
                  fillColor=INK, strokeColor=INK, strokeWidth=0))
    d.add(String(size / 2, size * 0.22, str(n), fontName="Times-Bold",
                 fontSize=size * 0.5, fillColor=white, textAnchor="middle"))
    return d

def process_flow(steps: list[str], cyclic: bool = False) -> Table:
    """One reusable flow block. steps = plain-text step strings (inline tags OK)."""
    rows = []
    if cyclic:
        loop = Drawing(14, 10)
        loop.add(Polygon(points=[2, 0, 12, 0, 7, 9],   # small down-pointing arrowhead
                         fillColor=INK, strokeColor=INK, strokeWidth=0))
        rows.append([loop, Paragraph("<i>(cycle — last step feeds back to step 1)</i>",
                                     STYLES["Caption"])])
    for i, s in enumerate(steps, 1):
        rows.append([_step_badge(i), Paragraph(s, STYLES["Bullet1"])])
    t = Table(rows, colWidths=[0.7 * cm, None])
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LINEAFTER", (0, 0), (0, -1), 0.75, GRID_LINE),  # the vertical flow rule
        ("LEFTPADDING", (0, 0), (0, -1), 0),
        ("RIGHTPADDING", (0, 0), (0, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]))
    return t
```

**Fallback rule (mandatory):** if a rendered flow block misaligns, clips, or breaks badly at a page boundary and one honest fix attempt doesn't cure it, fall back to plain numbered steps (`Bullet1` style, "1." "2." "3.") for that block and record it in the inventory's Coverage section (never in the PDF — Rule 6). Content correctness always outranks decoration — never ship a broken flow, and never burn the session debugging graphics at the expense of content.

### 4.3 Boxes — NOTE vs MEMORY AID
Both box types (exported as `note()` / `memory_aid()`) keep the `NOTE_BG` fill and Times-Italic text (fill is decoration) but are primarily told apart by **border style**, which survives any photocopy generation the fill doesn't:
- **NOTE box** — factual, from NCERT: common confusions, important exceptions, key comparisons not to miss. Solid double-rule border (`GRID_LINE`, two parallel 0.5pt lines ~1.5pt apart), the outline-circle-with-"!" icon in the top-left corner, and the `[NOTE]` text label.
- **MEMORY AID box** — clearly labeled `[MEMORY AID — not in NCERT]`: mnemonics/analogies invented to help recall. Dashed border (`GRID_LINE`, 0.75pt, alternating 3pt-on/2pt-off) and the outline-star icon in the top-left corner. The dash pattern alone tells it apart from a NOTE box even with the label covered.
- Label, icon, and border are three redundant signals carrying one meaning.

### 4.4 Figures — extract, convert to monochrome, verify, embed

**Every figure in the source chapter is extracted, converted to true monochrome, and embedded via `neet_template.figure()`. No exceptions, no "decorative" waivers — if NCERT printed it, the replacement carries it.** Text and image are complementary: a reader skimming only the image still sees the key labels; a reader skimming only the text still gets every fact.

> ### ⚙️ THE EXTRACTION PROCEDURE LIVES IN A SKILL FILE — READ IT FIRST
>
> **`skills/ncert-figure-extraction/SKILL.md` is the authoritative, executable procedure for Step 1.** Read it in full before extracting a single figure, and follow it as written. It carries the hand-pinned-bounding-box workflow (grid-overlay pinning, then the three-way audit: text-layer grazing, drawings-extent overflow, and border-band ink) that guarantees no body text bleeds into a crop and no artwork is clipped off.
>
> **This section (§4.4) states the *obligations*; the skill states the *method*.** Where the skill gives a concrete command, script, or threshold, the skill wins — it is maintained against real extraction failures. Where they appear to conflict on a *requirement* (every figure extracted, monochrome, opened-and-verified, every label a row), §4.4 wins. Do not re-derive an extraction approach from memory when the skill is on disk, and do not treat a bare `get_pixmap` as sufficient: an unaudited clip is exactly how a crop ships with a neighbouring paragraph baked into it, or with a leader line sheared off.
>
> Invoke it by name (`in-repo-ncert-figure-extraction`) or read the file directly. Triggers: extracting a chapter's figures, re-extracting after bad crops, any *"figures came out wrong/cropped/useless"* report.

**Mandatory grid standard for every chapter update:** Before pinning or revising any figure rectangle, render every artwork page at **440 dpi** with coordinate gridlines every **5 PDF points** and coordinate labels every 20 points. This 4× high-density grid is required for all new chapters, all re-extractions, and all crop-defect fixes. Save the grids under `scratch/ch<N>_figs/grid_4x/`, inspect them, and record any repinning in the inventory or audit notes.

**Step 1 — Locate and extract (Pass 1 session **1-F**, before writing the script — figures get a session to themselves and share it with no other step; see §6 Pass 1):**
1. **Follow `skills/ncert-figure-extraction/SKILL.md`.** In outline: open the source chapter PDF with `pymupdf` and render a **high-resolution clip of each figure's hand-pinned bounding box — `page.get_pixmap(clip=rect, dpi=300)`**. A clipped render survives vector diagrams and mixed text/graphic figures that a raw embedded-image extraction can miss or mangle. Only use embedded-object extraction when the figure is genuinely a single raster image and the clip render is worse. **Every rect must clear the skill's three-part crop audit before it is accepted.**
2. Save each figure to `assets/fig_<ch>_<n>.png` per the naming rule in §0.5.
3. Build the **figure manifest** and **figure-label matrix** as sections of the inventory (§6 Pass 1).
4. **The figure census is enumerated from the page images, not from caption numbers alone.** Unnumbered plates are real figures and are extracted like any other — Ch5's central-dogma plate on p4 carries no `Figure 5.x` number, so a caption-derived census predicted 17 assets where the chapter actually holds **18**. A count taken from captions is a lower bound; reconcile it against what is visibly on the pages.

**Harvest in-figure labels by OPENING each rendered asset and reading it — never by text extraction.** In-figure labels are frequently baked into the artwork as pixels or vector strokes and are **absent from the PDF text layer entirely**. In Ch12 Ecosystem, *all 61* labels across all 7 figures were invisible to `page.get_text()`; a text-extraction sweep of those same pages returns the captions and body prose but **zero** labels.

This is a silent, self-concealing failure. Text extraction does not error — it returns an empty label set, which yields an empty figure-label matrix, which **passes Gate 1 and check 6 trivially** because there are no rows to fail. The result is a green gate that has verified nothing, disarming the exact check (defects 5–6) this artifact exists to enforce. A suspiciously label-free figure is a red flag, not a clean result: a labelled NCERT diagram that yields no labels means the harvest method was wrong, not that the diagram has no labels.

**Step 2 — Convert to true monochrome (mandatory, every figure):**
```python
from PIL import Image, ImageOps
img = Image.open(figure_path).convert("L")   # true greyscale, one channel
img = ImageOps.autocontrast(img, cutoff=1)   # recover contrast lost when hue disappears
img.save(output_path)
```
`autocontrast` is not optional polish: a figure that used hue to separate two elements can collapse to near-identical greys under a flat `convert("L")`, and autocontrast stretches the tonal range back out so the distinction survives. Only the converted file is ever embedded. `check_pdf.py` check 3 fails any embedded image that still carries real color channels.

**Step 3 — Verify (mandatory, every figure — not a spot-check):**
Open every converted image and confirm: (a) it is the correct figure for its caption, (b) no labels or leader lines are cropped, (c) it is legible at print size, (d) it isn't an accidental grab of a neighboring figure/table/text, (e) it is genuinely monochrome, and (f) any distinction the original carried by color is still visible. Mark `Mono: yes` / `Verified: yes` only after this check.
- If two elements remain indistinguishable after conversion, that is a **real information loss**: state the distinction explicitly in the caption and surrounding text/table, and record it in the inventory's Coverage section.
- A figure that cannot be extracted or converted cleanly goes in the inventory's Coverage section under **"Figures requiring manual attention"**, and is flagged in the PDF where it would have appeared — never embed a bad crop silently, never skip a figure silently.
- **Operator-omitted figures — the third state.** A figure has three possible fates, not two: *embedded*, *failed extraction* (the bullet above), or **deliberately omitted by operator decision** — extraction succeeded, the asset is good, and the operator judges the plate not worth printing. Keep the three apart, because they are documented in opposite ways:
  - Such a figure is **NOT** flagged in the PDF under "Figures requiring manual attention". That heading promises a reader *"a diagram you should have is missing"*; using it for a plate dropped on purpose is a false alarm, and Rule 6 keeps the PDF from explaining itself.
  - It **stays** in the figure manifest with `Mono`/`Verified` as earned, and its asset stays on disk — the extraction is valid work and the omission is a reversible placement decision, not a retraction. Annotate its manifest row **"extracted, deliberately NOT embedded"** so the manifest never reads as a promise the PDF broke.
  - The omission is only permissible once **every fact in the figure's caption and labels is carried in prose** — the §4.4/§5 rule that the text must stand alone if a figure prints illegibly, applied to a figure that is simply absent. State the row IDs that carry them. Bare panel markers (`(a)`, `(b)`, ...) carry no fact and need no home.
  - Record it in the inventory's Coverage section **and** in a chapter-level decisions file, and name it in the chapter script's docstring. An unexplained gap between manifest and PDF is indistinguishable from a bug, and the next auditor will "fix" it.
  - Worked example: Ch11 (Class 11) Figure 11.1, Priestley's experiment — see `notes/class 11/Ch11_PhotosynthesisInHigherPlants/figure_layout_decisions.md` §3.

**Step 4 — Embed:**
- Use `neet_template.figure(asset_path, caption_text, max_width_cm=...)`, which returns the image and its caption `Paragraph` wrapped in `KeepTogether` inside a thin 0.5pt `GRID_LINE` border box, so a figure never separates from its caption across a page break and reads as part of the design system.
- Scale to fit the text column width preserving aspect ratio; never upscale beyond 300 dpi effective resolution.
- **`max_width_cm` is the pagination lever, and it acts on its neighbours.** Because `figure()` returns a `KeepTogether`, a figure block is indivisible: if it is taller than the space left on the page, ReportLab moves the *whole* block to the next page and leaves the remainder blank. A figure stranded alone on a page, or a section torn across three pages, is almost always this — not a spacing bug — and the fix is the render width, not a `Spacer`.
  - Budget it in points against the measured free tail, and remember the block costs more than the image: **image height + ~10 pt frame padding + caption height + gap**.
  - Shrinking an *earlier* figure pulls text up and adds that many points to a *later* page's tail, so a stubborn break is often cheaper to fix one figure upstream than by cutting the offending figure past legibility. Ch11's page-12 break needed Fig 11.9 at ≈4.7 cm to fix alone, but was solved by trimming 11.8 and 11.9 together.
  - Downward resizes are always safe against the no-upscale cap and *raise* effective dpi, but they are bounded by §4.4 Step 3(c) legibility and the §5 photocopier rule. A dense many-label diagram has far less headroom than a two-label graph — cut the cheap figure first.
  - Record every deviation from the default width in the chapter's decisions file with before/after numbers and the reason, and comment the call site. A figure narrower than the column otherwise reads as an oversight.
- Caption format: **"Fig. 14.2 — <caption>"** keeping the NCERT figure number verbatim, caption text rewritten-but-factually-exact (Rules 1 & 4 apply; a caption keeps its own inventory rows).
- If the figure's meaning depended on color, the caption carries one added sentence stating that distinction in words.
- Placement is **inline at the exact point where the figure's topic is covered** — never grouped at the end.
- **Every label on the figure must ALSO exist in the running text or a table.** Each label is a row in the Pass 1 figure-label matrix, and `check_pdf.py` check 6 fails the build if any label row is not found in the extracted text. This is the permanent fix for defects 5–6.

**Hard no:** the scientist profile photograph (§5 item 3) is never embedded, converted or not. A greyscaled photo is still a banned photo. `check_pdf.py` check 4 flags any manifest portrait row for human confirmation that it was kept text-only.

### ReportLab strict technical rules
- Use Paragraph objects for ALL text
- Use ONLY these inline tags: `<b>`, `<sub>`, `<super>`, `<i>` (for correct scientific-name italics)
- The icon/badge/process-flow system is drawn with `reportlab.graphics.shapes` as its own flowable layer — not an exception to "no decorative Unicode glyphs," a different mechanism entirely (vector drawing vs. inline text).
- **`Image()` is used only for figures processed through the full §4.4 pipeline** — clip-extracted, `convert("L")`'d, autocontrasted, saved, and verified. Never embed a raw extraction, a color image, or a screenshot straight out of the source PDF. Permanent hard no: no photograph of a person, ever.
- NEVER use Unicode subscripts/superscripts (O₂, CO₂, H⁺) — always `<sub>`/`<super>` tags. `check_pdf.py` check 5 fails on stray sub/superscript codepoints.
- NEVER use Unicode arrows (→, ⇌) — write "to", "yields", or plain ASCII. Gated by check 5.
- NEVER use raw Greek letters (α, β, γ, Δ) — spell them out ("alpha helix," "Delta G"). Gated by check 5.
- NEVER use emoji or decorative Unicode glyphs. Boxes carry plain-text labels (`[NOTE]`, `[MEMORY AID — not in NCERT]`) in addition to their drawn icons and border styles.
- NEVER use HTML `<form>` tags
- Wrap each heading together with the flowable immediately following it (`KeepTogether`) so a heading never lands alone at the bottom of a page
- Wrap each figure with its caption in `KeepTogether` (§4.4)
- Wrap all file/library calls in try/except and handle failures gracefully — including a missing asset file, which must raise a loud, named error (never silently skip the figure)
- **Comment every heading/section block with its NCERT section number** — e.g. `# ---- 14.1.2 Regulation of Kidney Function ----` directly above the flowables for that block. This block-marker convention is what lets a Pass 3 flag be found and edited in seconds instead of by re-reading the whole file, and it is preserved unchanged from v5.
- Keep the script as one linear, readable sequence of `story.append(...)` calls grouped by section, in §5 Content Order — not scattered helper functions that hide where a given fact lives. The only helpers are the ones imported from `neet_template.py`; everything chapter-specific stays linear. Anyone editing the script for a single fix should only ever need to touch one contiguous block.

---

## 5. Content Order

1. Title block
2. Unit introduction paragraph — rewritten in the same tutor style — if present
3. Scientist profile box — rewritten but factually exact (name, dates, discovery) — if present. **Text only — no photograph.** The source headshot is never embedded or recreated; name, dates, and achievements in a NoteBox-style block carry everything examinable (§4.4 hard no).
4. Chapter sections — reorganized where it helps, using headers with section-number badges, bold key terms, tables for comparisons, the Process Flow component for processes, and **figures inline at their topic** (§4.4)
5. Disorders / special topics (if present)
6. NOTE boxes at the end of the relevant section they belong to
7. MEMORY AID boxes where a genuinely useful mnemonic helps (optional, clearly marked)
8. **Quick Recap** — rewritten, denser version of the chapter summary
9. **Terms used in the exercises** appendix — only if Rule 2 found gaps, and containing **only** the GAP questions with their answers. Never a walk-through of all N exercises, and never a coverage/meta note (Rule 6). If there are no gaps, the chapter ends at the Quick Recap.

---

## 6. The Gated Multi-Pass Workflow — where the rigor lives

v6 replaces the single Pre-Writing + single Verification model with a **fixed, gated pass sequence**. A **normal chapter runs 3 passes**; a **big chapter runs 5 passes** (Pass 1 and Pass 2 each split in half). Every pass ends in a **gate** that must be met before the next pass begins. Gates are automated wherever a machine can decide, so human attention is spent only where it must be.

Sequence at a glance:
- **Normal (3 passes):** `Pass 1 → [Gate 1] → Pass 2 → [Gate 2: check_pdf.py green] → Pass 3 → [Gate 3: zero confirmed defects + bidirectional full read] → deliver`
- **Big (5 passes):** `Pass 1a → Pass 1b → [Gate 1] → Pass 2a → Pass 2b → [Gate 2] → Pass 3 → [Gate 3] → deliver`

**A pass is not a session.** Passes are units of *work* ending in gates; sessions are units of *context* ending in handoffs. Pass 1 is always spread across **five mandatory sessions** (§6 Pass 1), because three of its steps — the heading sweep, the opener sweep, and figure extraction — are each provably ruined by sharing a session with anything else. Gates are still judged per pass, not per session: no gate closes mid-Pass-1.

### Pass 1 — Source Mastery & Frozen Inventory

Everything here happens **before** a line of the script is written. This is the "multiple passes over the source" — cheap to fix while the script doesn't exist yet. A rushed Pass 1 is the single biggest cause of a failed Gate 3.

#### RULE — Pass 1 is split across five mandatory sessions

Pass 1 may **not** be attempted in one session. It runs as five sessions, in this order, each ending in a handoff (§0.2) and each beginning with the venv existence check:

| Session | Steps | Ends when |
|---|---|---|
| **1-S — Source read & inventory** | 1, 2, 3 | Facts inventory drafted from prose |
| **1-H — Heading sweep** | 4 (old 3a) | Every heading has a `Type: heading` row |
| **1-O — Opener sweep** | 5 (old 3b) | Every section opener has a `Type: opener` row |
| **1-F — Figures** | 6 (§4.4) | Manifest complete, `Mono`+`Verified` all yes, label matrix entered |
| **1-Z — Gaps, summary & freeze** | 7, 8, 9 | Inventory frozen, counts machine-derived → **Gate 1** |

**Why the split is a rule and not a preference — three independent failure mechanisms:**

1. **Figure work is context-destroying (1-F).** Extraction, monochrome conversion, and label harvesting require *opening each rendered asset* — the images enter context, and a chapter with a dozen figures can exhaust the session before the freeze is written. Worse, the moment context runs short, the harvest silently degrades to text extraction, which returns a thin or empty label set that **passes Gate 1 while verifying nothing** (§4.4 Step 1). Isolating figures into their own session means the budget is spent on looking at figures, and the session's only deliverable is a complete manifest plus matrix — so a degraded harvest is visible as an unfinished session, not as a green gate.
2. **The heading and opener sweeps are different cognitive modes, and sharing a session collapses them (1-H, 1-O).** 1-H walks the *skeleton* — headings only, prose deliberately ignored. 1-O reads the *first sentence of each section* — prose only, headings ignored. Run together, one always becomes a by-product of the other: the reader scans a section, notes its heading, notes its opener, and moves on. That is a prose sweep wearing two hats, and it is exactly what step 3 already does — which is why Ch9 lost §9.8.4's *"Temperature and pH"* heading (D4) and §9.8.2's *"conversion"* definition (D9) in the same chapter despite step 3 having "covered" both sections.
3. **A shared session produces counts that cannot be trusted (all three).** Ch13's freeze claimed 22 heading rows and 9 opener rows against a real 21 and 8 — both sweeps miscounted, in the same sitting, in the same file. When each sweep owns a session, its row count is that session's single deliverable and is derived by machine before handoff (step 10), so a miscount cannot survive to the freeze.

**Session-boundary discipline (applies to every Pass 1 session):**
- Start with `ls /vercel/share/neetenv/bin/python` and rebuild if absent (§0.2). Never diagnose anything before this.
- End by **writing the row count this session added, derived by machine**, into the inventory and the handoff. A session that cannot state its own count did not finish.
- The inventory file is the only state that crosses a boundary. Anything living solely in the session's reasoning is lost — write it into the file or the carry-over list before handing off.
- Sessions are ordered but **1-H, 1-O and 1-F are independent of each other**; if one has to be redone, redo that session alone, not Pass 1.

**The inventory is a saved file, not working notes.** It is written to `<ChapterName>_inventory.md` in the chapter folder and delivered with the PDF and script. It is what makes the coverage claim auditable and what `check_pdf.py` reads for checks 6 and 7.

Inventory file format:
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

**The per-figure figure-label matrix is the v6-mandatory artifact.** Rows are recorded as Facts-table rows whose wording begins `Figure labels:` (one row per figure, or per figure-part for multi-part figures like `Fig 9.7 (a)`/`(b)`), with each in-figure label as a quoted string. This is exactly the format `check_pdf.py`'s `_extract_labels` parses, and check 6 fails the build unless every label appears in the running text. Recording labels as their own rows converts "every label must appear in text" from an assumed discipline into an audited, per-label row.

**The matrix must exist in exactly ONE place in the inventory file — the Facts table. Never restate it as a second table for readability.** `_extract_labels` scans *every* pipe-delimited line in the file, so a duplicate table is not a harmless convenience; it corrupts the parse two ways at once, and both were hit in the Ch12 session:
1. **Every label counts twice.** A restated 61-label matrix parsed as 136 label strings.
2. **The restated table's own markdown separator (`|----|-------|`) parses as a phantom figure named `Fig #`**, carrying junk "labels" harvested from the dashes.

Both produce check-6 FAILs that are **impossible to fix by editing prose**, because no running text can ever contain a phantom label — a clean chapter is reported as broken and the failure points at content rather than at the inventory's formatting. If you want the matrix readable elsewhere, describe it in prose or list the row IDs; never repeat it as pipe-delimited rows.

Steps:
1. **First read:** read the entire chapter, including exercises, start to finish, without stopping to build the checklist. Get the shape of the chapter in your head.
2. **Independent inventory pass:** re-read section by section and build the Facts inventory — one row per fact [ID][Section][Type][Exact wording]. Cover Rule 1's full list.
3. **Second, independent hunting pass:** re-read again, specifically hunting what pass 2 likely missed — qualifier words buried mid-sentence, a footnote, a caption detail, a number in a parenthetical. Treat pass 2's inventory as provisional until this pass confirms or extends it. **This step does not cover headings or openers** — they belong to sessions 1-H and 1-O and must not be absorbed here. *(Ends session 1-S.)*
4. **Structural heading sweep — OWN SESSION (1-H). Every heading gets its own row, `Type: heading`.** Walk the chapter's headings alone, **ignoring prose entirely**, and give each one a row: numbered sections *and* the unnumbered sub-headings sitting inside them. Sub-headings are the easiest thing in the chapter to lose, because the prose beneath them is present and reads fine, so nothing looks wrong — the book's structure is silently flattened and §3 traceability breaks. **Ch9's D4 was exactly this:** §9.8.4's *"Temperature and pH"* and *"Concentration of Substrate"* had all their content but neither heading, and nothing caught it until a full read. Deliverable: the heading row set plus its machine-derived count, written as "N numbered + the M unnumbered IDs below" so the total is derivable from the list (step 10). *(Ends session 1-H.)*
5. **Section-opener sweep — OWN SESSION (1-O). Inventory the FIRST sentence of every section deliberately, `Type: opener`.** Read openers only, **ignoring headings entirely**. Opening sentences define the terms the rest of the section leans on, and they are the single most-dropped item in this workflow. Pay special attention when a section's opening sentence defines a word appearing in that section's own heading. **Ch9's D9 was exactly this:** §9.8.2's *"The chemical or metabolic conversion refers to a reaction."* was missing, leaving "conversion" — a word in the heading directly above it — never defined. Deliverable: the opener row set plus its machine-derived count. Remember that an observation *about* openers is not an opener row (step 10). *(Ends session 1-O.)*
6. **Figure extraction, conversion, verification & label-matrix pass — OWN SESSION (1-F), per §4.4:** clip-extract every figure at 300 dpi, convert each to monochrome, verify each **by opening the rendered asset**, complete the figure manifest with `Mono`/`Verified` marked, **and enter every in-figure label as its own row in the figure-label matrix.** Doing this in its own session means the script references verified assets from the start, problem figures surface while there is still time to re-extract, and the context cost of opening every image cannot crowd out the freeze. **Do not carry any other step into this session** — if the session ends with figures incomplete, resume 1-F rather than proceeding to 1-Z. *(Ends session 1-F.)*
7. **Exercise-gap scan (Rule 2):** note every term/fact an exercise assumes but the body never explains, and where the explanation will go.
8. **Summary scan (Rule 3):** classify every summary sentence BODY-PRESENT or SUMMARY-UNIQUE; fold every SUMMARY-UNIQUE fact into the correct body-section entry now.
9. **Freeze the inventory and save the file.** Number every row; you will tick rows off in the file itself during Pass 2.
10. **Derive every count in the header by re-parsing the finished table — never by hand tally.** Row totals, ID ranges, heading-row counts, opener-row counts, figure-label-row counts and summary-sentence counts are all machine-countable, so count them with a machine and assert ID contiguity (`F001..FNNN` with no gaps or duplicates) at the same time. Hand tallies are unreliable in practice, not in principle: Ch11's freeze shipped a header disagreeing with its own table, and the Ch12 first draft understated heading rows as 8 (actually 10) and summary sentences as 17 (actually 20) — in the same file, in one sitting. A header that contradicts its own table poisons every later audit that trusts it instead of recounting.
   - **A count is never stated in only one place, so a count is never *fixed* in only one place.** The same number is typically restated in four locations — the header table, the Gate 1 checklist, the prose census section that lists the IDs, and any status document that mirrors it. Ch13 shipped a freeze whose header said 22 heading rows and 9 opener rows against a real 21 and 8; correcting only the header would have left three surviving copies of the wrong number, and the next audit would have found the file contradicting itself in a *new* way. When a count changes, grep the whole file for the old value and fix every live restatement in the same edit, then re-run the parse against the finished file.
   - **A census that asserts a total separately from its own list will eventually disagree with it.** Write the census so the count is *derivable from the list* — "9 numbered + the 12 unnumbered IDs below" — and then verify `9 + 12` equals the header. Ch13's heading census claimed "9 numbered + 13 unnumbered = 22" while listing exactly 12 unnumbered IDs; the list had always been right and the addition had always been wrong. If a census states a number that no adjacent list supports, treat the number as the suspect, not the list.
   - **A structural finding is not a row.** Ch13's opener census reached its phantom 9th row by counting a written-up observation about two adjacent Facts rows (`F053`/`F054`) as if it were itself an opener row. Findings, notes, and cross-references *about* rows belong in the carry-over list or the Coverage note; only real table rows are counted. When a census total exceeds the row count by exactly one, look for a prose observation that got tallied.
   - **Controlled-vocabulary columns must be case-normalized before the freeze.** The `Type` column is machine-grouped, so `caption` and `Caption` are two different types to every parse that will ever read the file. Ch13 froze with `caption` on F038/F080 and `Caption` on F039/F081, splitting four caption rows into two classes of two — harmless to Gate 1's criteria, invisible to a reader, and quietly wrong to any future type-based tally. Normalize `Type` values to one fixed spelling and casing (`heading`, `opener`, `caption`, `number`, `term`, ...) and assert the finished table uses no others.

**Gate 1 (must be green before Pass 2 begins):**
- Every fact has a Facts row and every in-figure label has a figure-label-matrix row, with labels **harvested by opening each rendered asset** (§4.4 Step 1) — an empty or thin label set means the harvest method was wrong, not that the figures are unlabelled.
- **The inventory has been validated by running `check_pdf.py`'s own `_extract_labels` against it** — Gate 1 is a *machine-checked* gate, not merely a written artifact. Confirm it parses the expected figure count, the expected label count with **no doubling**, and **no phantom figure rows** (e.g. a `Fig #` row from a markdown separator). Writing the matrix in a format that merely *looks* correct is exactly how the Ch12 draft earned two unfixable check-6 FAILs on a chapter with no real defect; the fix must happen here, while the script does not yet exist, not at Gate 2 where it presents as a content problem.
- **Every count in the inventory header matches a re-parse of the table** (step 10), including contiguous `F001..FNNN` IDs with no gaps or duplicates. This means **every restatement** of every count — header table, this checklist, and the prose census sections — not the header alone, and every census total must equal the length of the list beside it. The `Type` column must use one normalized spelling/casing per value.
- **Every heading has a row (`Type: heading`), including unnumbered sub-headings** (step 4, session 1-H), and **every section's opening sentence has a row** (step 5, session 1-O). Confirm by walking the headings and the section-openers as their own list — not by assuming the prose sweep caught them.
- **Pass 1's five sessions have each actually run and each reported its own machine-derived row count** (1-S, 1-H, 1-O, 1-F, 1-Z). A Pass 1 that reached this gate in fewer sessions has not met it, regardless of how complete the inventory looks: the heading sweep, the opener sweep and the figure harvest are green only when each was the sole deliverable of a session that closed on it.
- Every figure in the manifest is marked `Mono: yes` and `Verified: yes`.
- Every exercise-gap term has a planned home; every SUMMARY-UNIQUE fact has been folded into a body row.
- The inventory file is saved to the chapter folder.

### Pass 2 — Build on the hardened template + auto-lint

Write the script **linearly from the frozen inventory**, in Content Order (§5), **importing `neet_template.py`** (§0.6) so no style is re-declared. As you write each block, tick its inventory rows off in the inventory file in the same pass — do not write freehand and reconcile later. Checking off while writing is what prevents an item being silently dropped between "I know this fact" and "I typed this fact." Comment every block with its `# ---- N.N ----` marker.

Then **loop `render → lint` until the linter is green**:
```bash
python3 check_pdf.py "notes/class 12/Ch9_BiotechnologyPrinciplesAndProcesses"
# or explicitly:
python3 check_pdf.py --pdf <ChapterName>.pdf --inventory <ChapterName>_inventory.md --script <ChapterName>.py
```
`check_pdf.py` auto-discovers the sibling PDF, inventory, and script by the §0.5 naming convention, and runs these checks (exit 0 = clean, 1 = at least one FAIL, 2 = setup error; `--strict` treats WARN as failure, `--json` emits a machine-readable report):

1. **Footer/header band** — no text span inside the top/bottom 1.4 cm margin band. *[defect 1]*
2. **Legibility floor** — no rendered text glyph below 5.0pt (FAIL); the 5.0–6.0pt band is WARN and reserved for legitimate subscripts. Because badge and step digits are real text spans, a badge that collapsed to ~3.4pt is caught here. *[defects 2, 3]*
3. **Grayscale-only images** — every embedded image is single-channel GRAY, or sampled pixels are all R==G==B; any real color fails. *[§4.4]*
4. **No person photograph** — a manifest row that looks like a portrait/photo must not be embedded (WARN + human confirmation). *[§5 item 3]*
5. **Banned glyphs** — no Unicode arrows, sub/superscripts, Greek letters, or emoji in the text stream. *[§4 technical rules]*
6. **Figure-label coverage** — every figure-label-matrix row is found in the PDF's extracted running text. *[defects 5, 6]*
7. **Inventory ticked** — every Facts row is ticked. *[Pass 1 completion]*
8. **Page geometry** — every page is A4 portrait.

**Gate 2 (must be green before Pass 3 begins):** `check_pdf.py` exits 0 — no FAILs. A WARN (e.g. check 4's portrait row, or a subscript in the 5–6pt band) is allowed to advance only after you have eyeballed it and confirmed it is legitimate; treat `--strict` green as the ideal. Do not begin the human verification pass while the linter is red — the whole point of v6 is that Pass 3's budget is not spent rediscovering mechanical defects a script already gates.

### Pass 3 — Dual verification & deliver

With mechanical defects gated out by Pass 2, Pass 3 is two focused checks a machine cannot make: cross-page visual consistency, and genuine content drift against the frozen inventory.

**(a) Visual render check.** Render **every page** with `pymupdf` and look at each directly. Layout bugs (overflow, clipping, a table running off the page, an orphaned heading, a process-flow rule misaligned with its badges, a figure squashed to the wrong aspect ratio) show up only in the rendered page, not in extracted text. Additionally render each page at true print DPI + a B&W 1-bit threshold and confirm cross-page **style consistency**: pull one rendered instance of each element type (H1, H2, H3, table, NOTE, MEMORY AID, process flow, figure box) from at least three different points in the chapter and confirm they are visually *identical*. (Because styles are imported from `neet_template.py`, drift here should be rare — this check now confirms the template held, rather than hunting hand-typed drift.)

**(b) Content cross-check — run in BOTH directions.** Do one complete, full read — not a keyword search — of the source sections and the matching script blocks, checking every inventory row (loaded from the saved FILE, not memory). Classify each item:
- **COVERED** — present and accurate in the script
- **MISSING** — in the inventory/NCERT but absent from the script
- **FABRICATED** — in the script but not in NCERT or the inventory
- **DRIFTED** — present but the value/qualifier/direction/term is wrong (defect 4 was this class)
- **UNINVENTORIED** — in NCERT but has **no inventory row at all** (see the mandatory second direction below)

> **⚠ Both directions are mandatory. Direction 2 is the one that has actually failed.**
>
> 1. **Inventory → script.** For every row, is it in the script and correct? This catches MISSING / DRIFTED / FABRICATED.
> 2. **Source → inventory.** Read the NCERT section itself and ask the opposite question: *is every sentence and every heading here represented by some row?* This catches **UNINVENTORIED** content — a Pass 1 gap, not a Pass 2 gap.
>
> Direction 1 alone is **structurally incapable** of finding a Pass 1 omission: if the freeze never created a row, there is nothing to classify, and the section reports CLEAN while the chapter is genuinely incomplete. **Ch9 Biomolecules proved this twice.** Gate 3 closed on Ch9 on two separate occasions with direction 1 clean, while the chapter was still missing an NCERT sentence (`D9` — the §9.8.2 antecedent that defined the very word in the section's own heading) and **two** NCERT sub-headings (`D4` — §9.8.4's *"Temperature and pH"* and *"Concentration of Substrate"*). Both were invisible to direction 1 and both required adding new inventory rows (`F194a`, `F221a`, `F225a`) during Pass 3. When direction 2 forces a new row, say so plainly and log it as a **real Pass 1 gap** — never back-date it into the freeze to make Pass 1 look clean.

Divide the chapter's sections into adjacent pairs and run one subagent per pair in parallel (`config: { $kind: "explore" }`) with the shared rubric below; **if parallel subagents are unavailable, do the identical section-pair cross-check yourself, sequentially — the rigor is in the rubric and the full-read discipline, not the parallelism.** Figure-label-matrix rows are cross-checked here too (correct asset, caption number/text correct, placed at the right topic), as a human backstop to `check_pdf.py` check 6.

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

**Confirm every flag by full read, never by grep.** A grep miss does not mean a fact is missing (it may be paraphrased or reflowed by `pdfplumber`); a grep hit does not mean it's correct. Open the source paragraph and the script block and read both before deciding CONFIRMED vs FALSE POSITIVE.

**No statistical text match may close Gate 3 — this is a hard bar, not a preference.** Token-coverage scores, similarity percentages, fuzzy matching, "N/N rows at ≥X% coverage" tables, and any other automated comparison of inventory wording against the extracted PDF text layer are **Pass 2 evidence only**. They may be used to *locate* suspicious rows; they may **never** be used to *clear* them, and a table of coverage percentages is **not** a Pass 3(b) full read no matter how green it looks.

The reason is mechanical, not stylistic: **these screens fail silently in exactly the cases that matter most.** Drop the antecedent sentence from a section and the remaining tokens still overlap heavily, so the score stays high. Omit a sub-heading entirely and there is no row to score, so nothing registers at all. On Ch9 a screen reporting *"276/276 substantive rows at ≥78% coverage, 260 at 100%"* passed a chapter that was missing one NCERT sentence and two NCERT sub-headings. **A high score is not evidence of coverage — it is evidence only that the text you did write resembles the text you wrote down.**

**Gate 3 evidence must be a stated, human-legible reading claim**, per section, in both directions — "read source §9.8.4 pp. 114–115 against script block `# ---- 9.8.4 ----`; both sub-headings present; 12 rows COVERED; 0 UNINVENTORIED." If the record cannot state *what was read against what*, Gate 3 is **not** satisfied, regardless of any linter or coverage output.

**Record false positives separately from confirmed defects, and keep both.** A flag investigated and correctly dismissed is real audit work and must survive in the record with its reasoning, distinct from the confirmed-defect list — otherwise a later session re-litigates settled decisions or, worse, "fixes" something a human deliberately rejected. Likewise, note where a `check_pdf.py` check legitimately does not fire (e.g. check 4 on a chapter with no scientist profile) so a true negative is never later mistaken for a suppressed finding.

**Fix confirmed items via their block markers.** Open the `.py`, locate the block via its `# ---- N.N ----` comment, edit only that block (tag `# [VERIFICATION FIX]`), regenerate the PDF, **re-run `check_pdf.py` (it must stay green)**, and re-verify only the fixed block. The rest was already verified and nothing else changed.

**Gate 3 (deliver) — all five conditions, no exceptions:**

1. **Zero confirmed defects remain.**
2. **`check_pdf.py` is still green**, re-run against the *final rebuilt* PDF — never a verdict carried forward from an earlier run or an earlier session.
3. **Pass 3(a) covered every page**, stated as a count (e.g. "15/15 pages inspected"), not as "spot-checked".
4. **Pass 3(b) was a full read in both directions**, with a per-section reading claim naming source pages against script blocks. **No coverage percentage, similarity score, or grep result may substitute for this** (see the hard bar above).
5. **The rebuild is reproducible** — regenerate from the final script and confirm the PDF matches the committed one (same page count, same extracted character count, same image count; an embedded timestamp is the only acceptable byte difference).

**Say "PASS" only when all five hold.** If Pass 3(b) was in fact a token screen, the honest verdict is *Gate 3 not yet satisfied* — say that instead. A chapter wrongly marked closed is worse than one openly marked incomplete, because it will never be looked at again: **Ch9 was marked CLOSED twice while still defective.** Never let a green linter stand in for the content read — Gate 2 and Gate 3 test different things, and Ch9 was fully green under `--strict` while all three of its confirmed defects were still present.

Then deliver the full chapter folder (§0.5): the PDF, the `.py` script (saved as a file, not pasted in chat), the inventory with every row ticked, and `assets/` with every verified monochrome figure. If Pass 3 surfaces more than a handful of small scattered issues, treat that as a signal Pass 1 was incomplete — redo the relevant part of Pass 1 rather than patching piecemeal against a shaky checklist.

Along with the files, include:
- A **section-wise coverage confirmation** (e.g. "14.1 — 12/12 body facts, 2/2 summary-unique, 3/3 figures embedded + verified mono, all figure labels in text").
- A short **Coverage note**, written into the chapter's **inventory `.md`** and never into the PDF (Rule 6), with these fixed headings so an audit prompt can consume it mechanically:
  - **Compression decisions** — what was merged/reformatted and why it's safe
  - **Exercise classification** — every exercise numbered and marked COVERED (naming the section that answers it) or GAP (naming where its added answer lives), per Rule 2
  - **Drift caught and fixed** — anything Pass 3 found
  - **Figures requiring manual attention** — figures that failed extraction/conversion/verification (write "None" if empty)
  - **Color-dependent figures** — figures whose meaning relied on color, and where that distinction is now stated in words (write "None" if empty)
  - **Source problems** — any part of the source flagged as garbled/unrecoverable (write "None" if empty)
  - **Linter verdict** — the final `check_pdf.py` summary (fail/warn counts), with any accepted WARN justified

### Big-chapter protocol — 5 passes

If the chapter genuinely cannot be completed at full quality in one session, split into 5 passes matching the halves, `1a → 1b → 2a → 2b → 3`:
1. **Pass 1a / 1b** — inventory the first half, then the second half, into the SAME inventory file. Gate 1 is evaluated over the whole chapter only after 1b, so the frozen inventory is complete and nothing at the seam is double-covered or dropped. **The five-session split still applies and is not what "1a/1b" refers to** — 1a/1b halve the *source*, while 1-S/1-H/1-O/1-F/1-Z separate the *kinds of work*. In practice a big chapter runs the sweeps per half (1a-S, 1a-H, 1a-O, then 1b-S, 1b-H, 1b-O), but **figures run as a single whole-chapter 1-F session** and the freeze as a single 1-Z, because a half-chapter figure manifest cannot be checked for duplicate or missing `Fig #` numbering across the seam.
2. **Pass 2a / 2b** — build the first half into the script, then the second half into the SAME script, ticking rows as you go. Run `check_pdf.py` after 2b (a mid-build run after 2a is useful but Gate 2 is judged on the whole PDF after 2b).
3. **Pass 3** — a single whole-chapter verification, exactly as the normal Pass 3, over the merged PDF.

The deliverable is still **one merged PDF, one script, one inventory** — never two part-PDFs. The frozen whole-chapter inventory is the seam-guard.

---

## What I'll send you
One NCERT Biology chapter PDF at a time. If a chapter is long, completeness beats brevity — use the 5-pass big-chapter protocol and deliver one merged PDF, rather than quietly cutting content to fit. Don't ask permission to apply the rules above; just apply them.

## What you'll send back
Always the full chapter folder per §0.5: `<ChapterName>.pdf`, `<ChapterName>.py`, `<ChapterName>_inventory.md` (with the figure-label matrix), and `assets/` — all actually saved and delivered, never the PDF alone, and never the script only pasted inline in chat. The chapter script imports the repo-level `neet_template.py`, and Gate 2 was cleared by the repo-level `check_pdf.py`. If I come back later with an adversary-audit error list, the expected fix is: open that same `.py` file, edit the flagged block (found via its `# ---- N.N ----` comment), rerun it, re-run `check_pdf.py` to confirm the gate is still green, and hand back the regenerated PDF + updated script — not a rewrite from scratch.

---

## Gate 3(b) Verification Rules — learned from the Ch12 Ecosystem audit

Apply these rules to every future Gate 3(b) pass, not just Ecosystem.

### 1. A “clean” or “PASS” verdict is a claim, not a fact
Re-verify every previously “clean” block with the same rigor as unread blocks. A prior verdict is not evidence that the block remains correct; scrutinize especially any block where a defect was previously found.

### 2. Cross-document disagreement IS the finding
Before auditing content, compare every status-bearing document. Inventory, `CHAPTER_STATUS.md`, and `CHAPTER_TRACKER.md` must agree. Any mismatch is itself a defect and leaves the chapter unresolved.

### 3. Match the verification method to the defect class
- Leaked text, clipping, and layout bugs require direct inspection of rendered pages.
- Phrasing drift and silent compression require full side-by-side reading, never skimming or summarizing.
- Internal contradictions using legitimate vocabulary require side-by-side reading of both instances; grep and keyword search cannot establish correctness.
- Mislabeled IDs and wrong audit-trail comments require checking the script bookkeeping against the defect register.

Choose the method for the defect being hunted, not merely the fastest method.

### 4. Fail loud, not silently-plausible
When a silent-failure mode is found, add a guard, assertion, or hard check that rejects the entire class of mistake. Do not only patch the individual bad instance. Out-of-bounds crops, for example, must error rather than being silently clamped.

### 5. Metadata correctness matters as much as content correctness
Audit trails, block markers, verification comments, and defect-register IDs are deliverables. Verify them against the register with the same care as reader-facing text.

### 6. When a shortcut keeps getting taken, ban it
If a weaker verification method repeatedly replaces genuine re-reading, explicitly prohibit that shortcut. In particular, grep may locate candidates but may not serve as evidence for a Gate 3(b) content verdict.

### 7. Size is not a proxy for difficulty
Set scrutiny by dependency density and cross-references, not page count. Exercise answers, appendix rows, figure labels, and summary facts can make a short chapter more difficult than a long one.

### 8. Close the loop atomically
When a defect is fixed, update every document that claims its status in the same session. Content fixes and updates to `CHAPTER_STATUS.md` and `CHAPTER_TRACKER.md` are one operation; until all agree, the gate remains open.

### Gate 3(b) pre-closure checklist

Before writing “Gate 3: CLOSED” anywhere, confirm:

- [ ] Every previously “clean” block was re-read this session.
- [ ] Inventory, `CHAPTER_STATUS.md`, and `CHAPTER_TRACKER.md` agree explicitly.
- [ ] Layout, drift, contradiction, and metadata defects were checked with their matching methods.
- [ ] Every discovered silent-failure mode was fixed at the guard level.
- [ ] Script comments and defect IDs match the inventory’s defect register.
- [ ] `CHAPTER_STATUS.md` and `CHAPTER_TRACKER.md` were edited in this same session before closure.

---

## Gate 1 Closure & Handoff Rules — learned from the Ch13 Biodiversity session

The Ch13 session was a **resumed** session whose only job was closing Gate 1 on an already-frozen inventory. It produced a class of lesson the earlier sections do not cover: the failure modes of *inherited state*. Gate 3(b)'s rules above govern verifying content; these govern trusting a predecessor and closing a gate cleanly.

### 1. A handoff's findings are claims to re-derive, not results to apply
A handoff document lists defects and diagnoses. **Re-derive every number in it before acting on it, using the machine, not the handoff's arithmetic.** Ch13's handoff was right that the header was wrong (21/8, not 22/9) — and independently re-parsing confirmed it in one command. But the same handoff was wrong about *why* its own validation step failed (see §0.2: missing venv, not a script bug), and it had **missed a third defect entirely** (the `Type` column casing split). Both outcomes come from the same discipline: run the parse yourself. Applying a handoff's edits without re-deriving them inherits its blind spots along with its findings, and the resuming session is the last chance to catch them.

Corollary: **a documented trap is not a fired trap.** Ch13's inherited notes warned at length about the Ch12 label-doubling/phantom-`Fig #` failure. Running `check_pdf.py`'s real `_extract_labels` against the file showed it clean — 2 figures, 23 labels, no doubling, no phantom row. A warning copied forward from a prior chapter describes a *risk*, and the only way to know whether it materialized here is to execute the check. Never carry a warning forward as though it were a finding, and never treat a finding as closed because a warning about it exists.

### 2. Closing a gate is a documentation-consistency operation, not just a content fix
The content fix is the small part. Ch13's real work was that the corrected numbers were restated in **four** places in the inventory and again across two status documents — and every stale copy is a live defect (Gate 3(b) rule 2: cross-document disagreement *is* the finding). When a gate closes:
- Rewrite the "what blocks this gate" section rather than leaving it. An obsolete blocker section is worse than no section: it actively instructs the next session to re-fix a closed defect, and in Ch13 the blocker text warned about a trap that verification had just proven did not fire.
- Sweep for stale status claims by string (`Gate 1 OPEN`, the old counts) after editing, not before, and confirm zero live survivors.
- **Distinguish a live claim from quoted history in that sweep.** Recording a correction properly means writing down the old value ("header previously read 22/9"), which makes the wrong number *appear* in a grep of the corrected file. A sweep that cannot tell a quoted former value from a current assertion will either raise false alarms forever or get ignored. Check the surrounding line, and keep correction notes clearly framed as history.

### 3. Roll-up counters drift silently and must be derived, never incremented
`CHAPTER_TRACKER.md`'s header read "9 / 32 — Class 12: 3/13" while its own Class 12 footer read "4 / 13", and counting the ✅ rows showed the footer was right: a previous chapter's closure had been recorded in its section but never propagated to the header. Nobody had touched Ch13 to cause this — **it is what an incremented counter does over time.**

So: **derive roll-ups by counting the rows (`grep -c` the done marker), never by adding one to the previous number,** and re-derive them on every closure even when the chapter you are working on does not change the total. Atomic closure (Gate 3(b) rule 8) means every *derived* number is recounted in the same session, not merely that the touched row was updated.

### 4. Name which gate closed, and count only what that gate earns
**Gate 1 closed is not chapter closed.** Ch13 finished this session with a green Gate 1, no chapter script, no PDF, all 189 rows unticked, and Gates 2 and 3 correctly blocked — so it must **not** appear in any "Done" tally, and its status line must name the specific gate. A chapter recorded as generically "in progress" or, worse, folded into a completion count on the strength of Gate 1, is exactly the false-closure failure that let Ch9 ship defective twice. Write the gate number every time: "Gate 1 closed; Pass 2 not started."

### 5. A frozen inventory may be corrected in its metadata, never in its rows
The freeze is what makes coverage auditable, so the boundary must be exact:
- **Allowed:** correcting a count, a header field, or a census total — metadata *about* the rows, where the rows themselves are the ground truth being counted. Ch13 changed four numbers and zero rows, which is why the freeze survived intact.
- **Not allowed:** adding, removing, reclassifying, or rewording a Facts row to make a count come out. If a count and the rows disagree, **the rows win and the count changes.** The one exception remains Pass 3 direction 2, which may add a genuinely UNINVENTORIED row — and must log it loudly as a Pass 1 gap rather than back-dating it into the freeze.
- **Cosmetic defects found after the freeze go to the carry-over list, not into the rows.** Ch13's `Type`-casing split broke no Gate 1 criterion, so it was logged as a carry-over for Pass 2 instead of justifying edits to four frozen rows. Editing frozen rows for cosmetics is how a freeze stops meaning anything; deferring them costs nothing because Pass 2 reads the carry-overs anyway.

### 6. Carry-overs are the handoff's real payload
A resumed session's most valuable inheritance is not the defect list (which it must re-derive anyway) but the **carry-over list**: the things found while looking at something else, which the current gate has no authority over. Keep them numbered, keep them in the inventory, and add to them freely — a cosmetic finding, a trap that did not fire, a rule about what must *not* be "fixed" later (Ch13: `S = CAZ` must stay flat text, never a caret or Unicode superscript, which would trip check 5). Each carry-over is a defect that will not have to be rediscovered.

---
