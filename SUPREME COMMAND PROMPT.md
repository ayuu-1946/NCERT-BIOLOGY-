# NCERT Biology → NEET PDF — Master Prompt (Rewrite Style, ReportLab Output) v4 — Full-Replacement Edition with Original NCERT Figures

**Mode: NCERT REPLACEMENT, not high-density conversion.**
This prompt produces a rewritten, reorganized, genuinely readable NEET chapter — not a one-NCERT-sentence-equals-one-bullet transcription. Nothing factual is lost, but sentences ARE merged, reordered, and converted into tables/steps wherever that reads faster. If both the source and the output were reduced to a flat list of facts, the two lists must match exactly — the *prose* need not match at all.

**New in v4:** every NCERT figure is extracted from the source PDF and embedded inline, at original fidelity — the output is a true standalone replacement of the book, diagrams included. The fact inventory is now a saved deliverable file, and deliverables live in a fixed `notes/` tree.

## Core doctrine: get it right in one pass

**All the effort goes in BEFORE you write a single line of the script — not after.** Re-reading the source three times and cross-checking your own inventory is cheap: it costs a few minutes and fixes a missing line before it exists. Catching the same gap after the script is written costs an edit, a full PDF regeneration, and a re-extraction. So §6 (Pre-Writing Process) below is deliberately heavier than a normal outline step — it is where "multiple passes" belongs. §7 (Final Verification) is a single confirming pass, not a repair loop. If §6 was done properly, §7 should come back clean on the first try. Treat any real gap found in §7 as a signal that §6 was rushed, not as a normal/expected step of the process.

---

## 0. Environment & Installation Setup (do this first, every session)

Do not skip this even if you did it in a previous session — the sandbox resets. Confirm the environment before touching the source PDF.

### 0.1 Required packages
- `reportlab` — generates the PDF
- `pdfplumber` — extracts text from both the NCERT source and the generated PDF for the verification pass
- `pymupdf` (imported as `fitz`) — two jobs: (a) renders PDF pages to images for the visual formatting check in §7, and (b) **extracts the NCERT figure images** from the source chapter PDF (§4.4)
- `pillow` — image inspection for the B&W print-safety check and figure quality verification

### 0.2 Install
```bash
pip install --break-system-packages reportlab pdfplumber pymupdf pillow
```

### 0.3 Verify the install before proceeding
```python
import reportlab, pdfplumber, fitz, PIL
print("reportlab:", reportlab.Version)
print("pdfplumber: OK")
print("pymupdf/fitz: OK")
print("pillow: OK")
```
If any import fails, fix the environment now. Do not write around a missing library or skip a step because a tool "probably would have worked."

### 0.4 Smoke test (confirms fonts + styles render correctly, once per session)
Generate a throwaway 1-page PDF using Times-Roman/Bold/Italic, one H1/H2/H3 banner each, one table with the exact colors from §4, one of each icon badge from §4.1, one Process Flow block (§4.2) with at least 3 steps, and one embedded test image with a caption (any small PNG) to confirm the figure component (§4.4) works. Render it with `fitz` and view the image. Check:
1. Banners, fonts, table shading, and the embedded figure + caption look right.
2. Every icon badge (●▲■★ shapes drawn via `reportlab.graphics.shapes`, never Unicode) is visually distinct from the others at actual print size — not just distinguishable on-screen at zoom.
3. **B&W print-safety check:** convert the rendered page image to true 1-bit/grayscale (e.g. via `PIL.Image.convert("L")`) and re-view it. Confirm the NOTE box border style and the MEMORY AID box border style (§4.3) are still tell-apart-able from each other, and that no fill lighter than `#D9D9D9` is the *only* thing carrying meaning anywhere on the page (a photocopier or toner-saver print will wash it out — meaning must always survive on line/border/icon alone, with fill as decoration on top).

If all three checks pass, the environment and design system are trustworthy for the real run. Delete the throwaway file afterward.

### 0.5 File & folder conventions
Deliverables live in a `notes/` tree that mirrors the source `Chapter/` tree. Source PDFs are never modified or moved. Per chapter:

```
notes/
  class 11/
    Ch14_BreathingAndExchangeOfGases/
      Ch14_BreathingAndExchangeOfGases.pdf    ← the notes PDF
      Ch14_BreathingAndExchangeOfGases.py     ← the exact script that generated it
      Ch14_BreathingAndExchangeOfGases_inventory.md  ← the frozen fact inventory (§6)
      assets/
        fig_14_1.png
        fig_14_2.png
        ...
```
- Work in a scratch directory if useful, but the four items above are the final deliverables and must all land in the chapter folder.
- Name the PDF, script, and inventory identically apart from extension/suffix.
- Figure assets are named `fig_<chapter>_<number>.png` matching the NCERT figure numbering exactly (e.g. NCERT "Figure 14.2" → `fig_14_2.png`). Multi-part figures get letter suffixes (`fig_14_2a.png`).

---

## 1. Role & Objective

You are an expert NEET Biology editor and content architect. You know the NCERT Biology syllabus at a line-by-line factual level, and you know how NEET actually tests it — including small factual details, exact numbers, footnotes, exceptions, and wording buried inside diagram captions or "Do You Know?" boxes. Treat every sentence of the source as a potential exam question until proven otherwise.

I will give you one NCERT Biology chapter at a time (PDF). Produce a complete replacement of that chapter — reorganized, clearly formatted, readable, **with every original NCERT figure embedded** — as a clean, print-ready A4 PDF built directly with Python + ReportLab. Never lose a testable fact. Someone holding only this PDF should never need to open the NCERT book, for text OR diagrams.

**Every delivery is four items, always: the PDF, the exact `.py` script that generated it, the frozen inventory file, and the `assets/` figure folder.** The script is not a scratch file you discard after rendering — it is a deliverable in its own right, because the adversary audit (see §7 and the companion audit prompt) works by editing this script directly wherever it finds a MISSING or WRONG item, not by regenerating the chapter from a blank page. The inventory file is what makes the coverage claim independently auditable. A future session — this one, a fresh session, or a human — must be able to open the script, jump to the flagged section, fix that one block, and rerun it.

### Scope & length
- **One chapter per session.** If a chapter is too large to complete at full quality in one session, split the work across two sessions — but the deliverable is still **one merged PDF**: session 2 opens session 1's script and inventory, extends them, and rebuilds the single final PDF. Never ship a chapter as two part-PDFs.
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
- **Every figure itself** — extracted and embedded per §4.4, not merely described
- Every fact sitting inside a "Do You Know?" box, footnote, margin note, or in-text activity/embedded question

Default when unsure: keep it. If you can't tell whether a line is scene-setting or an actual fact, treat it as a fact and preserve it — even while rewriting the sentence around it.

### Rule 2 — Close the exercise gap
NCERT's end-of-chapter questions sometimes use a term, or lean on a fact, that the chapter itself never actually explains. Before writing:
1. Scan every exercise question for this.
2. Check whether the main text or summary genuinely explains each term/fact the questions assume.
3. If not, add a clear, correct explanation — inline where it naturally belongs, or in a closing appendix titled **Terms used in the exercises**.

Goal: someone who reads only the rewrite, never the original book, should be able to answer every exercise question.

### Rule 3 — What's actually allowed to cut
"Garbage" means exactly three things: a sentence that just restates a fact already given, purely rhetorical scene-setting with no fact in it ("Have you ever wondered…"), and transitional filler between paragraphs. Nothing else qualifies. Merge redundant sentences into one — but every fact they carried has to survive the merge. Never cut something because it feels minor or "unlikely to be asked."

**Summary section handling — mandatory two-pass check:**
The NCERT chapter summary is a second source document, not a recap to be skipped. Summaries frequently contain facts, explicit terms, or "There are N types of X" counts that appear ONLY there — stated for the first time in the summary, never in the body. These are high-value exam targets.

Before treating any summary sentence as skippable:
1. **Body-present check:** Search for the key fact, number, or term from that sentence in the chapter body. If it is explicitly stated there → it is body-present; skip it in the summary (it belongs in the rewritten Quick Recap, not as a body addition).
2. **Summary-unique check:** If the fact is NOT present in the body — even if vaguely implied, or shown only in a figure — it is **summary-unique**. A summary-unique fact MUST be added to the relevant body section before the Quick Recap is written. Implied does not count. Only explicit statement counts.

Mark each summary sentence as BODY-PRESENT or SUMMARY-UNIQUE in the inventory. Every SUMMARY-UNIQUE line becomes a body addition, and it also becomes a mandatory checklist item in §6.

### Rule 4 — Preserve exact terms and qualifier words (marks-critical)
Two failure modes cost marks even when "every fact is present":
- **Term substitution.** Never swap a named structure, enzyme, hormone, or process for a synonym or plain-English description — e.g. keep "juxtaglomerular apparatus," not "kidney's filtration sensor." Rewrite the explanation *around* the term; never rewrite the term itself.
- **Qualifier drift.** Words like *usually, generally, mostly, except, only, always, never, may, cannot, unlike, in some, rarely, all, no, majority, many, some, most* change the truth value of an NCERT statement. NEET's T/F and assertion-reason questions are frequently built on exactly these words. Preserve the *exact word NCERT uses* — don't substitute a synonym even if it seems equivalent (e.g. "majority" must stay "majority," not become "most"; "may" must stay "may," not become "can" or "either…or"; "all" must stay "all," not become "every"). Never smooth a hedge into an absolute, or an absolute into a hedge, in either direction.

### Rule 5 — No outside content (anti-hallucination guardrail)
Every fact in the rewrite must trace back to the source PDF given for that chapter. Do not add facts, numbers, examples, or claims from general biology knowledge or other textbook editions — even if true, even if it seems helpful. The chapter PDF is the only source of truth. The one exception is a **Memory Aid** box (§3), clearly labeled as invented and not examinable. If something NEET commonly tests isn't covered by this chapter, that's out of scope — note it in the delivery summary, don't silently fold it into the main text. This rule matters for single-pass success specifically: an invented "helpful" detail is a fabrication the verification pass must catch and remove, which is wasted work in both directions.

This rule extends to figures: only figures extracted from the source PDF may appear. Never generate, redraw, or substitute a diagram from memory or another edition.

### Worked example
**NCERT-style original:**
"You might have noticed that when a seed germinates, the radicle comes out first, followed by the emergence of the plumule. Germination in dicots can be epigeal, where the cotyledons come above the soil, as in bean, or hypogeal, where the cotyledons remain below the soil, as in gram and pea."

**Rewrite:** Germination bullet ("radicle emerges first, then the plumule") + a 3-column table (Type / Cotyledons / Example: Epigeal–Rise above soil–Bean; Hypogeal–Stay below soil–Gram, pea).

Cut: the "you might have noticed" framing. Kept: emergence order, both germination types, both example plants — reformatted as a table for faster review.

---

## 3. Structure, Formatting & Style Rules

- Clear headers/subheaders. Reorder or regroup content from the original — e.g. pulling a comparison scattered across two paragraphs into one place — as long as nothing is lost.
- **Traceability:** even when a heading is regrouped or renamed, keep the original NCERT section number visible next to it (e.g. "14.1.2"). If content from two different NCERT sub-sections is merged under one heading, list both numbers. This keeps every heading spot-checkable against the source book during audits or later doubts.
- **Bold** key terms on first use.
- Convert anything comparative or enumerable into a table.
- Write processes/pathways using the **Process Flow** component (§4.2) — a connected sequence of numbered badges, not a plain numbered list and not prose paragraphs. Use it for every multi-step process, pathway, or cycle in the chapter — with the fallback rule in §4.2 if it misbehaves.
- Every heading gets a small **section-number badge** (§4.1) instead of a bare number typed inline — same traceability, more visual structure.
- **Figures appear inline, at the exact point in the rewrite where their topic is covered** — never grouped at the end. Each carries its NCERT figure number and rewritten-but-factually-exact caption (§4.4).
- Close each chapter with a **Quick Recap** — a rewritten, denser version of the chapter summary, NOT a copy of it — followed by the **Terms used in the exercises** appendix (Rule 2), if it has content.
- **Design for the photocopier, not the screen.** These notes exist to be printed and re-photocopied in black and white — often several generations deep, on a cheap office/college printer. Every visual distinction (NOTE vs MEMORY AID, H1 vs H2 vs H3, "this row matters" vs "this row doesn't") must be carried by shape, border style, or icon first, with grey fill as a bonus, never the only signal. If you'd have to ask "is that light grey or white?" on a bad photocopy, redesign it.
- Write like a sharp, direct tutor, not a textbook. Short, information-dense sentences, active voice, no motivational asides, no invented anecdotes, no padding.
- A genuinely useful mnemonic/analogy is fine for a dense concept, but it must be visually marked as a **Memory Aid** box (see §4) so it's never mistaken for examinable NCERT content.

### Special content handling
- **Figures/diagrams**: the figure image itself is embedded per §4.4. IN ADDITION, pull every fact out of its caption and labels into the running text — the text must stand alone even if a print of the figure is illegible. If a figure fails extraction or verification (§4.4), flag it in the Coverage note under the fixed heading **"Figures requiring manual attention"** — never silently omit it.
- **Scientific names**: correct italics, correct binomial format.
- **Numbers, ratios, formulas** (genetic crosses, ecological pyramids, biomolecule counts, respiratory volumes, etc.): reproduce exactly — never round or approximate.
- **Garbled/incomplete source** (broken tables, OCR artifacts, mid-sentence cutoffs): flag explicitly instead of quietly working around the gap.

---

## 4. PDF Design Specifications

**Page:** A4, margins 1.5 cm all sides, topMargin/bottomMargin 1.4 cm

**Font:** Times-Roman family throughout (Times-Roman, Times-Bold, Times-Italic)

**No header, no footer, no page numbers.** Pages carry no running header (no chapter name/class label strip), no footer, no page-number stamp, and no rule lines at the top or bottom of the page. Content simply fills the full margin area on every page.

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

### Canonical style block — use this directly, don't reinvent it per chapter
Defining styles fresh each time is how formatting drift creeps in. Use (or closely mirror) this block in every script, so every chapter is byte-identical in formatting and the audit in §7 has a fixed, known target to check against:

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
Table styling (`TableStyle`) should use `DARK_GREY` header row with white bold text, `ROW_ALT` alternating rows, 0.4pt `GRID_LINE` gridlines, 3pt top/bottom and 4pt left/right padding — apply these as constants, not re-typed hex strings, so a single source of truth exists.

### Heading structure
- **H1** (main sections, e.g. 14.1): dark grey banner, white bold text, fontSize 10.5, borderPad 3, preceded by a **section-number badge** (§4.1) instead of typing "14.1" inline
- **H2** (sub-sections): medium grey banner, white bold text, fontSize 9.5, borderPad 2, same badge treatment at a smaller size
- **H3** (sub-sub-sections, e.g. 14.1.1): soft grey banner, white bold text, fontSize 9, borderPad 2, badge optional (use if the heading is short enough that a badge doesn't crowd it)
- Badge size scales down H1 → H2 → H3 exactly as the banner grey scales dark → medium → soft, so the page keeps one consistent visual "weight" language: darker + bigger = higher in the hierarchy.

### Body text & bullet hierarchy (typographic spec only — NOT a "one sentence = one bullet" rule)
- **Body / normal paragraph text:** fontSize 10.8, leading ~14.2
- Bullets are used wherever the rewritten prose naturally breaks into points (definitions, sub-points under a heading, itemized facts) — not mechanically per source sentence.
- Main bullet (•): fontSize 10.8, leftIndent 12, firstLineIndent -8
- Sub-bullet (-): fontSize 10.5, leftIndent 22, firstLineIndent -8
- Sub-sub-bullet (*): fontSize 10.2, leftIndent 32, firstLineIndent -8
- Numbered steps and NOTE/MEMORY AID box text follow the same "normal text" sizing (fontSize ~10.2–10.8) since they are still ordinary reading prose, just indented or boxed.
- Maximum 3 levels. Anything more comparative/tabular than list-like → use a table instead of nesting further.
- Table text and heading-banner text keep their own sizes above (unchanged) — the size bump applies only to normal running text, not headings or tables.

### Title block (page 1, no separate title page)
- Chapter name — Times-Bold, fontSize 20, black, centered (no separate "Chapter N" label line above it)
- One small decorative line-art motif (drawn with `reportlab.graphics.shapes`, INK-colored, ~1.5cm) beside the title, loosely themed to the chapter topic (a leaf outline for a plant chapter, a simple heart outline for circulation, etc.)
- HRFlowable rule below title
- Immediately followed by content — no blank title page
- **This motif is decorative only, never a source figure.** It carries zero facts and must not visually resemble or substitute for an actual NCERT diagram — keep it simple enough (a single outline shape) that no one could mistake it for reproduced source content. This keeps it outside Rule 5's anti-hallucination guardrail rather than in conflict with it.

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
A small, fixed set of shapes drawn with `reportlab.graphics.shapes` (Circle, Rect, Polygon), filled/stroked in `INK` — never Unicode glyphs or emoji (still banned by the ReportLab technical rules below; a drawn vector shape is a different layer, not inline text). Reuse the same shape for the same meaning every time, all chapters:
| Shape | Meaning | Where used |
|---|---|---|
| Filled square badge, white number | Section-number badge | Next to every H1/H2/H3 (see Heading structure) |
| Filled circle | Definition / key term callout | Margin marker beside a first-use bolded term — **eligibility rule: only terms that also appear in the chapter summary or in an exercise question qualify**, capped at 3-4 per section. This keeps "exam-critical" objective instead of a judgment call. |
| Filled triangle, point up | Process / pathway | Used inside the Process Flow component (§4.2), not standalone |
| Open (stroke-only) square | Comparison / table pointer | Small marker next to a heading whose content was converted to a table, so a skimming reader knows to expect one |
| 5-point outline star | Memory Aid | Corner of every MEMORY AID box (§4.3) |
| Outline circle with a bold "!" (drawn, not typed inline as a glyph — build the "!" from a thin Rect + small Circle) | NOTE | Corner of every NOTE box (§4.3) |

Icons are a **redundant** signal, never the only one. Every NOTE box still carries its `[NOTE]` text label and every MEMORY AID box its `[MEMORY AID — not in NCERT]` text label, in addition to the icon and the distinctive border (§4.3). Headings, box labels, and borders carry the same meaning in plain text/line-work too. If the icon layer failed to render for any reason, the page must still be fully readable and unambiguous.

### 4.2 Process Flow Component
Replaces plain numbered steps for every process, pathway, or cycle: a connected sequence of numbered triangle badges on a vertical rule, so it reads as a *flow* rather than a list. Cyclical processes (Krebs cycle, nitrogen cycle) additionally get a small loop-back arrowhead polygon at the top — a wordless cue that it's a cycle, not a one-way sequence.

**Use this reference implementation — do not hand-roll the rule and badges freehand.** It builds each flow as a single bordered-column Table, which ReportLab splits cleanly across page boundaries with the vertical rule intact:

```python
from reportlab.platypus import Table, TableStyle, Paragraph
from reportlab.graphics.shapes import Drawing, Polygon, String

def _step_badge(n: int, size: float = 14) -> Drawing:
    """Filled triangle badge with white step number."""
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

**Fallback rule (mandatory):** if a rendered flow block misaligns, clips, or breaks badly at a page boundary and one honest fix attempt doesn't cure it, fall back to plain numbered steps (`Bullet1` style, "1." "2." "3.") for that block and note it in the Coverage note. Content correctness always outranks decoration — never ship a broken flow, and never burn the session debugging graphics at the expense of content.

### 4.3 Boxes — NOTE vs MEMORY AID
Both box types keep the existing `NOTE_BG` fill and Times-Italic text (fill is decoration, per the print-safety floor above) but are primarily told apart by **border style**, which survives any photocopy generation the fill doesn't:
- **NOTE box** — factual, from NCERT: common confusions, important exceptions, key comparisons not to miss. Solid double-rule border (`GRID_LINE`, two parallel 0.5pt lines ~1.5pt apart), the outline-circle-with-"!" icon (§4.1) in the top-left corner, and the `[NOTE]` text label.
- **MEMORY AID box** — clearly labeled `[MEMORY AID — not in NCERT]`: mnemonics/analogies invented to help recall. Dashed border (`GRID_LINE`, 0.75pt, alternating 3pt-on/2pt-off) and the outline-star icon (§4.1) in the top-left corner. The dash pattern alone is enough to tell it apart from a NOTE box even with the label covered.
- Label, icon, and border are three redundant signals carrying one meaning. A reader skimming should tell NOTE from MEMORY AID from across the room by border shape alone — but the text label is always present too.

### 4.4 Figures — extraction, verification, embedding (new in v4)

**Every figure in the source chapter is extracted and embedded. No exceptions, no "decorative" waivers — if NCERT printed it, the replacement carries it.**

**Extraction (per chapter, before writing the script):**
1. Open the source chapter PDF with `fitz`. For each figure, prefer `page.get_images()` + `fitz.Pixmap` extraction of the embedded image object. If the figure is vector-drawn or composited (common in NCERT PDFs), fall back to rendering a clip rectangle of the page region at high resolution: `page.get_pixmap(clip=rect, dpi=300)`.
2. Save each figure to `assets/fig_<ch>_<n>.png` per the naming rule in §0.5.
3. Build a **figure manifest** as a section of the inventory file (§6): one row per figure — [Figure number] [Caption text, verbatim] [Asset filename] [Source page] [Verified: yes/no].

**Verification (mandatory, every figure — not a spot-check):**
Open every extracted image and visually confirm: (a) it is the correct figure for its caption, (b) no labels or leader lines are cropped off at the edges, (c) it is legible at the size it will print (test-render if in doubt), (d) it isn't an accidental grab of a neighboring figure, table, or text block. Mark `Verified: yes` in the manifest only after this check. A figure that cannot be extracted cleanly after honest attempts goes in the Coverage note under **"Figures requiring manual attention"** with the reason — never embed a bad crop silently, and never skip the figure silently.

**Embedding:**
- Use a reusable `figure(asset_path, caption_text, max_width_cm=...)` helper returning `[Image, Paragraph(caption, STYLES["Caption"])]` wrapped in `KeepTogether`, so a figure never separates from its caption across a page break.
- Scale to fit the text column width preserving aspect ratio; a small figure may sit at natural size. Never upscale beyond 300 dpi effective resolution.
- Caption format: **"Fig. 14.2 — <caption>"** keeping the NCERT figure number verbatim, caption text rewritten-but-factually-exact under the same rules as all other text (Rules 1 & 4 apply to captions).
- Placement is **inline at the exact point where the figure's topic is covered** in the rewrite — even if the rewrite reordered sections, the figure follows its topic, not its original page position.
- Every label on the figure must ALSO exist in the running text or a table (per §3 Special content handling) — the figure is the visual; the text stands alone if the print is poor.

**B&W note:** NCERT figures are often colored. They will print greyscale — that is acceptable (the originals are designed to survive it and labels are line-work), but if a specific figure's meaning depends on a color distinction (e.g. oxygenated vs deoxygenated blood in red/blue), add one sentence to its caption stating the distinction in words.

### ReportLab strict technical rules
- Use Paragraph objects for ALL text
- Use ONLY these inline tags: `<b>`, `<sub>`, `<super>`, `<i>` (for correct scientific-name italics)
- The icon/badge/process-flow system (§4.1–§4.2) is drawn with `reportlab.graphics.shapes` (`Drawing`, `Circle`, `Rect`, `Polygon`) as its own flowable layer, composed alongside Paragraphs — this is not an exception to "no decorative Unicode glyphs" below, it's a different mechanism entirely (vector drawing vs. inline text), so it stays fully within the rule.
- NEVER use Unicode subscripts/superscripts (O₂, CO₂, H⁺, etc.) — always use `<sub>`/`<super>` tags (e.g. `O<sub>2</sub>`, `Na<super>+</super>`)
- NEVER use Unicode arrows (→, ⇌) — write "to", "yields", or plain ASCII
- NEVER use raw Greek letters (α, β, γ, Δ) — Times-Roman's default encoding renders these unreliably; spell them out ("alpha helix," "Delta G")
- NEVER use emoji or decorative Unicode glyphs. Boxes carry plain-text labels (`[NOTE]`, `[MEMORY AID — not in NCERT]`) **in addition to** their drawn icons and border styles (§4.1/§4.3) — label + icon + border are three redundant carriers of one meaning, never alternatives to choose between.
- NEVER use HTML `<form>` tags
- Wrap each heading together with the flowable immediately following it (`KeepTogether`) so a heading never lands alone at the bottom of a page
- Wrap each figure with its caption in `KeepTogether` (§4.4)
- Wrap all file/library calls in try/except and handle failures gracefully — including a missing asset file, which must raise a loud, named error (never silently skip the figure)
- **Comment every heading/section block with its NCERT section number**, matching the traceability rule in §3 — e.g. `# ---- 14.1.2 Regulation of Kidney Function ----` directly above the flowables for that block. This is what lets a flagged error be found and edited in seconds instead of by re-reading the whole file.
- Keep the script as one linear, readable sequence of `story.append(...)` calls grouped by section, in the same order as §5 Content Order — not scattered helper functions that hide where a given fact lives. (The three sanctioned helpers — canonical styles, `process_flow()`, `figure()` — live at the top; everything else stays linear.) Anyone editing the script for a single fix should only ever need to touch one contiguous block.

---

## 5. Content Order

1. Title block
2. Unit introduction paragraph — rewritten in the same tutor style (not verbatim bullets) — if present
3. Scientist profile box — rewritten but factually exact (name, dates, discovery) — if present
4. Chapter sections — reorganized where it helps (per Rule 3), using headers with section-number badges, bold key terms, tables for comparisons, the Process Flow component (§4.2) for processes, and **figures inline at their topic** (§4.4)
5. Disorders / special topics (if present)
6. NOTE boxes at the end of the relevant section they belong to
7. MEMORY AID boxes where a genuinely useful mnemonic helps (optional, clearly marked)
8. **Quick Recap** — rewritten, denser version of the chapter summary
9. **Terms used in the exercises** appendix — only if Rule 2 found gaps

---

## 6. Pre-Writing Process — this is where the rigor lives

Everything in this section happens **before** you write a line of the script. This is the "multiple passes" — over the *source*, while it's still cheap to fix. Do not shortcut this to get to writing faster; a rushed inventory is the single biggest cause of a failed final check.

**The inventory is a saved file, not working notes.** It is written to `<ChapterName>_inventory.md` in the chapter folder and delivered with the PDF and script. This is what makes the coverage claim auditable: the adversary audit, a future session, or a human can re-check every row against both the source and the script.

Inventory file format:
```markdown
# Frozen Inventory — <Chapter Name>
Source: <path to source PDF> | Frozen: <date> | Rows: <n>

## Facts
| ID | Section | Type | Exact original wording | Ticked |
|----|---------|------|------------------------|--------|
| F001 | 14.1 | Number | "...about 79% nitrogen..." | x |

## Summary classification
| Summary sentence | Classification | Folded into |
|---|---|---|

## Exercise-gap terms
| Term/fact assumed by exercises | Explained where |
|---|---|

## Figure manifest
| Fig # | Caption (verbatim) | Asset file | Source page | Verified |
|---|---|---|---|---|
```

Steps:
1. **First read:** read the entire chapter, including exercises, start to finish, without stopping to build the checklist yet. Get the shape of the chapter in your head.
2. **Independent inventory pass:** re-read section by section and build the inventory — one row per fact: [Fact ID] [Section] [Type: Number/Term/Qualifier/Step/Comparison/Table/Caption] [Exact original wording]. Cover Rule 1's full list: definitions, numbers, scientists, taxonomic names, examples, process steps, comparisons/exceptions, table rows, figure captions, "Do You Know?" content.
3. **Second, independent hunting pass:** re-read the chapter again, specifically looking for what pass 2 likely missed — qualifier words buried mid-sentence, a footnote, a caption detail, a number inside a parenthetical. Treat the pass-2 inventory as provisional until this pass either confirms it complete or adds to it. Do not skip this because pass 2 "felt thorough" — it always feels thorough from the inside.
4. **Figure extraction & verification pass (§4.4):** extract every figure to `assets/`, verify each one visually, and complete the figure manifest. Doing this before writing means the script can reference verified assets from the start, and a problem figure is discovered while there's still time to re-extract.
5. **Exercise-gap scan (Rule 2):** go through every exercise question; note any term/fact it assumes but the body never actually explains, and exactly where the explanation will be added.
6. **Summary scan (Rule 3):** extract the chapter summary as its own block. Classify every sentence BODY-PRESENT or SUMMARY-UNIQUE. Fold every SUMMARY-UNIQUE fact into the correct body-section entry in the inventory now — before writing, not as a patch afterward.
7. **Freeze the inventory and save the file.** This combined list (body facts + exercise-gap terms + summary-unique facts + figure manifest) is now the single source of truth. Number every row; you'll tick items off in the file itself while writing (step 8) and check again in §7.
8. **Write the script directly from the frozen inventory**, section by section, in Content Order (§5). As you write each block, tick its inventory rows off in the inventory file in the same pass — don't write freehand and reconcile against the inventory later. Checking off while writing is what prevents an item from being silently dropped between "I know this fact" and "I typed this fact."
9. Before moving to §7, confirm every single row in the frozen inventory has been ticked — facts AND figures. Any unticked row gets written in now, while the script is still open and the context is fresh — this is still "writing," not yet "auditing."

### Split-chapter protocol (large chapters only)
If the chapter genuinely cannot be completed at full quality in one session:
1. Session 1 completes §6 in full for the ENTIRE chapter (the inventory file covers everything, including all figure extraction), then writes the script through a clean section boundary, ticks those rows, and saves script + inventory + assets in the chapter folder. It does NOT deliver a PDF.
2. Session 2 opens the saved inventory and script, confirms which rows are ticked, writes the remaining sections into the SAME script, ticks the remaining rows, then runs §7 over the whole chapter and delivers the single merged PDF.
3. The frozen inventory is the seam-guard: because it was completed for the whole chapter in session 1, nothing at the boundary can be double-covered or dropped.

---

## 7. Final Verification Pass (single pass, not a repair loop)

If §6 was done properly, this pass exists to catch the rare slip — a fact ticked off but subtly mis-transcribed, a qualifier that drifted during the rewrite, a table cell typo — not to discover large gaps. Run it once, thoroughly, and expect it to come back clean.

### Step 1 — Visual render check (do this before extracting text)
Render page 1 and every table-heavy, multi-heading-level, process-flow, or **figure-bearing** page to an image with `fitz` and look at it directly. Layout bugs — overflow, clipping, a table running off the page, a heading orphaned at the bottom, a process-flow rule that doesn't line up with its badges, a figure separated from its caption or squashed to the wrong aspect ratio — do not show up in extracted text, only in the rendered page. Confirm colors, banners, table shading, section-number badges, icons, box border styles, and figure rendering all match §4 while you're looking.

### Step 2 — Extract text
```python
import pdfplumber
with pdfplumber.open("Output.pdf") as pdf:
    text = "\n".join(p.extract_text() or "" for p in pdf.pages)
```

### Step 3 — One thorough parallel cross-check against the frozen inventory
Divide the chapter's sections into adjacent pairs and dispatch one subagent per pair, all in parallel via `Promise.all`. Each subagent does **one complete, full read** — not a keyword search — of its two assigned source sections and the matching script blocks, and checks every row of the frozen §6 inventory (loaded from the saved inventory FILE, not from memory) against what was actually written. Figure-manifest rows are checked too: correct asset referenced, caption number/text correct, placed at the right topic.

**If parallel subagents are unavailable in the current environment, perform the identical section-pair cross-check yourself, sequentially, one pair at a time, using the exact same classification rubric below. The rigor is in the rubric and the full-read discipline, not in the parallelism.**

```js
const sharedPreamble = `
You are doing a single, decisive verification pass for a NEET Biology rewrite PDF —
not the first of several. Read fully; do not rely on keyword search to decide FOUND vs MISSING.

FILES:
- NCERT source: <path/to/source.pdf>
  Extract: python3.11 -c "import pdfplumber; pdf=pdfplumber.open('<path>'); print('\\n'.join(p.extract_text() or '' for p in pdf.pages))"
- Rewrite script: <ChapterName.py>
- Frozen inventory file: <ChapterName_inventory.md> — use the rows for your assigned sections

YOUR JOB for your 2 assigned sections:
1. Read the full source text for these sections, start to finish — not a search for isolated terms.
2. Read the full corresponding script block(s), start to finish.
3. For each inventory row, classify:
   COVERED    — present and accurate in the script
   MISSING    — in the inventory/NCERT but absent from the script
   FABRICATED — in script but not in NCERT or the inventory
   DRIFTED    — present but the value/qualifier/direction/term is wrong
4. For each figure-manifest row in your sections: confirm the script references the
   correct asset file, the caption keeps the NCERT figure number, and the figure sits
   at the topic it illustrates. Classify the same way.
5. Return:
   SECTION: <n>
   STATUS: CLEAN | ISSUES FOUND
   COVERED: <count>
   MISSING: <list>
   FABRICATED: <list>
   DRIFTED: <item — NCERT says X, script says Y>
`;

const [r1, r2, r3, r4, r5] = await Promise.all([
  subagent({ name: "verify-s1-s2", task: sharedPreamble + "SECTIONS: 5.1 + 5.2 ...", config: { $kind: "explore" } }),
  subagent({ name: "verify-s3-s4", task: sharedPreamble + "SECTIONS: 5.3 + 5.4 ...", config: { $kind: "explore" } }),
  subagent({ name: "verify-s5-s6", task: sharedPreamble + "SECTIONS: 5.5 + 5.6 ...", config: { $kind: "explore" } }),
  subagent({ name: "verify-s7-s8", task: sharedPreamble + "SECTIONS: 5.7 + 5.8 ...", config: { $kind: "explore" } }),
  subagent({ name: "verify-s9-s10", task: sharedPreamble + "SECTIONS: 5.9 + 5.10 ...", config: { $kind: "explore" } }),
]);
```
Adjust subagent count to the chapter's section count.

### Step 4 — Confirm flags by full read, never by grep
Keyword search is not a verdict — it's only a way to jump to a line number faster. A grep miss does not mean a fact is missing (it may be paraphrased, split across sentences, or reflowed oddly by `pdfplumber`'s table extraction), and a grep hit does not mean it's correctly stated. For every item a subagent flags:
1. Open the exact source page/section and read the full surrounding paragraph yourself, not just the matched line.
2. Open the exact script block and read the full surrounding block yourself.
3. Only then decide CONFIRMED or FALSE POSITIVE. Never dismiss a flag on the strength of a search miss alone.

### Step 5 — Fix and spot-verify (not a full restart)
For each CONFIRMED item:
1. Open the `.py` script; locate the block via its `# ---- N.N ----` comment.
2. Edit only that block. Tag the change `# [VERIFICATION FIX]`.
3. Regenerate the PDF.
4. Re-verify **only the fixed block** — re-extract and re-read that section's text, and if it's a table/heading/figure page, re-render and re-check that one page visually. The rest of the chapter was already fully verified in Step 3 and nothing else changed, so a full re-run is not needed.

If Step 3 comes back with more than a handful of small, scattered issues (rather than none, or one or two isolated slips), treat that as a signal the §6 inventory itself was incomplete — go back and redo the relevant part of §6 properly, rather than patching the script piecemeal against a shaky checklist.

### Step 6 — Deliver
Once every confirmed item from Step 5 is fixed and spot-verified, deliver the full chapter folder (§0.5):
- The PDF.
- The `.py` script that generated it, saved as an actual file (not just shown as a code block).
- The frozen inventory file, with every row ticked.
- The `assets/` folder with every verified figure.

Along with the files, include:
- A **section-wise coverage confirmation** (e.g. "14.1 Breathing Mechanism — 12/12 body facts covered, 2/2 summary-unique facts covered, 3/3 figures embedded")
- A short **Coverage note** with these fixed headings so the audit prompt can consume it mechanically:
  - **Compression decisions** — what was merged/reformatted and why it's safe
  - **Exercise-gap terms** — confirmation every exercise-assumed term is covered
  - **Drift caught and fixed** — anything §7 found
  - **Figures requiring manual attention** — figures that failed extraction or verification, with reasons (write "None" if empty)
  - **Source problems** — any part of the source flagged as garbled or unrecoverable (write "None" if empty)

---

## What I'll send you
One NCERT Biology chapter PDF at a time. If a chapter is long, completeness beats brevity — use the split-chapter protocol (§6) and deliver one merged PDF, rather than quietly cutting content to fit. Don't ask permission to apply the rules above; just apply them.

## What you'll send back
Always the full chapter folder per §0.5: `<ChapterName>.pdf`, `<ChapterName>.py`, `<ChapterName>_inventory.md`, and `assets/` — all actually saved and delivered, never the PDF alone, and never the script only pasted inline in chat. If I come back later with an adversary-audit error list, the expected fix is: open that same `.py` file, edit the flagged block (found via its section-number comment), rerun it, and hand back the regenerated PDF + the updated script — not a rewrite from scratch.
