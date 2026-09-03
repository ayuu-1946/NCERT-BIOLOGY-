# GATE 2 — Pass 2: Build on the Hardened Template + Auto-Lint

> **Self-contained reference for Pass 2 only.** Derived from `SUPREME COMMAND PROMPT.md` (v6). Read this to write the chapter script against the frozen inventory and drive `check_pdf.py` green. Gate 1 (inventory) and Gate 3 (verify+deliver) have their own files. The original prompt is the source of truth if the two disagree.

---

## 0. Where Gate 2 sits

Normal: `Pass 1 → [Gate 1] → Pass 2 → [GATE 2: check_pdf.py green] → Pass 3 → [Gate 3] → deliver`
Big: `… → [Gate 1] → Pass 2a → Pass 2b → [GATE 2] → Pass 3 → …`

**Precondition:** Gate 1 is green — a frozen, machine-validated inventory exists. **A pass may not start on an ungated predecessor:** do not write the script if Gate 1 isn't met. **Gate 2's whole job:** write the script *linearly from the frozen inventory*, importing the frozen `neet_template.py`, ticking rows as you go, and loop `render → lint` until `check_pdf.py` exits 0. Gate 2 gates the mechanical/print defect classes so Pass 3's human budget isn't wasted rediscovering them.

---

## 1. Every-session preamble (run first, every session)

Sandbox resets between sessions. **First command of any session:**

```bash
ls /vercel/share/neetenv/bin/python
```

If absent, rebuild + verify (only proven install form in this sandbox):

```bash
uv venv /vercel/share/neetenv --python 3.13
uv pip install --python /vercel/share/neetenv/bin/python reportlab pdfplumber pymupdf Pillow
/vercel/share/neetenv/bin/python -c "import sys,reportlab,pdfplumber,pymupdf,PIL;print(sys.version,sys.prefix,reportlab.Version,pymupdf.__version__,PIL.__version__)"
```

Invoke every Python command through `/vercel/share/neetenv/bin/python`, never bare `python3`. Known-good: reportlab 5.0.1, pymupdf 1.28.2, Pillow 12.3.0 on 3.13. Never write around a missing library. Never "fix" a shared repo-level file (`check_pdf.py`, `neet_template.py`) on an inherited hypothesis — re-run the step after rebuilding the venv first.

### File conventions (auto-discovery depends on these)
```
neet_template.py   ← repo root: frozen shared styles/helpers
check_pdf.py       ← repo root: the automated gate
notes/class 11/Ch14_.../
  Ch14_....pdf      Ch14_....py      Ch14_..._inventory.md      assets/fig_14_1.png ...
```
PDF, script, inventory share one base name apart from extension/suffix. Assets: `fig_<ch>_<n>.png`, multi-part `fig_14_2a.png`.

### 0.4 Smoke test (once per session, before the real build)
Generate a throwaway 1-page PDF **by importing `neet_template.py`** (not re-declaring styles): one H1/H2/H3 banner, one table with canonical colors, one of each icon badge, one `process_flow()` with ≥3 steps, and **one real NCERT figure pushed through the full §4.4 pipeline** (clip-render → `convert("L")` → `autocontrast` → embed in bordered box + caption). Render with `pymupdf` and view. Check:
1. Banners, fonts, table shading, embedded figure + caption + border look right.
2. Every icon badge (section-number square, key-term circle, process triangle, table square, memory-aid star, note "!" circle — all `reportlab.graphics.shapes`, never Unicode) is visually distinct at **print size**; badge text and step digits legible at print size (the defect 2/3 floor).
3. **B&W print-safety:** convert the page image to grayscale and re-view; NOTE-box and MEMORY-AID borders still tell-apart-able; no fill lighter than `#D9D9D9` is the *only* thing carrying meaning.
4. **Figure conversion:** the embedded figure is genuinely monochrome (`img.mode=="L"` or sampled pixels R==G==B); pick a source figure that used color to carry meaning to prove `autocontrast` preserved the distinction.
Then **run `check_pdf.py` against the smoke PDF** and confirm it executes end-to-end (a WARN/FAIL on a 1-pager is fine — you're confirming the linter runs). Delete the throwaway afterward.

---

## 2. The frozen `neet_template.py` contract (§0.6) — import, never re-declare

`neet_template.py` is frozen and repo-level: chapters `import` it and never re-declare the styles it owns. Freezing the style layer permanently kills defect classes 1–3 (footer, illegible badge, tiny step-digit) and cross-page style drift. Treat it as an API — change it only deliberately; when you do, every chapter re-rendered against it changes identically.

**Font rule (no exceptions):** every piece of type is Times New Roman via ReportLab base-14: `FONT_REGULAR="Times-Roman"`, `FONT_BOLD="Times-Bold"`, `FONT_ITALIC="Times-Italic"`, `FONT_BOLD_ITALIC="Times-BoldItalic"`. No chapter script may reference any other `fontName`.

**Exports the chapter depends on:**
- **Geometry & color constants:** `PAGE_SIZE` (A4), `MARGIN` (1.5 cm), `TOP_MARGIN`/`BOTTOM_MARGIN` (1.4 cm), `FRAME_WIDTH`, and the 7 canonical colors `DARK_GREY, MED_GREY, SOFT_GREY, ROW_ALT, NOTE_BG, GRID_LINE, INK`.
- **`STYLES`** — the canonical `ParagraphStyle` dict (Title, H1, H2, H3, Body, Bullet1–3, NoteBox, Caption, TableCell, TableHead), all on the Times canon. Body running text is fontSize 10.8; nothing below the legibility floor.
- **`heading(number, text, level, has_table=False)`** — banner heading with section-number badge, sized internally by `pdfmetrics.stringWidth` so the box always encloses its text (permanent fix for defect 2; stays above `TINY_FAIL_PT` 5.0pt and at/above `TINY_WARN_PT` 6.0pt).
- **`process_flow(steps, cyclic=False)`** — the Process Flow component: bordered-column Table with numbered triangle step-badges at the corrected digit size (defect 3 fix) + vertical rule; splits cleanly across pages.
- **`keyterm(text)`** — bullet with the filled-circle definition icon.
- **`note(text)`** and **`memory_aid(text)`** — the NOTE and MEMORY AID box helpers.
- **`data_table(rows, col_widths=None, font_size=9.5)`** — DARK_GREY header (white bold), ROW_ALT alternating rows, 0.4pt GRID_LINE gridlines with a 0.25pt rule under *every* row, `repeatRows=1`.
- **`figure(asset_name, caption_text, assets_dir, max_width_cm=15.9)`** — monochrome image + `Caption` wrapped in `KeepTogether` inside a 0.5pt GRID_LINE border box. Takes `assets_dir` explicitly.
- **`title_block(title_text, motif_size=42)`** — page-1 DNA-motif + Times-Bold title row + rule; no separate title page.
- **`build_pdf(OUT_PDF, story, title=...)`** — page template with **no footer** (defect 1 fix).

**Chapter script top (sys.path bootstrap walks up to the dir containing `neet_template.py`):**
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
Followed by a linear `story.append(...)` sequence and a `main()` calling `build_pdf(OUT_PDF, story, title=...)`. Nothing style-level, geometry-level, or font-level is redefined per chapter.

---

## 3. §4 PDF Design Specifications (the contract the template implements)

**Page:** A4, margins 1.5 cm all sides, top/bottom margin 1.4 cm.
**Font:** Times-Roman family throughout.
**No header, no footer, no page numbers, no top/bottom rule lines.** Content fills the full margin area on every page. `check_pdf.py` check 1 gates it (no text span inside the top/bottom 1.4 cm band).

**Colors:**
| Name | Hex | Used for |
|---|---|---|
| DARK_GREY | #2C2C2C | H1 banner background |
| MED_GREY | #4A4A4A | H2 banner background |
| SOFT_GREY | #6B6B6B | H3 banner background |
| ROW_ALT | #F0F0F0 | alternate table rows |
| NOTE_BG | #E8E8E8 | note / memory-aid boxes |
| GRID_LINE | #AAAAAA | table gridlines |
| INK | #1A1A1A | icon fill/stroke, badge fill |

**Print-safety floor:** all pure greyscale (R=G=B). A fill lighter than `#D9D9D9` disappears after 2–3 photocopy generations. `ROW_ALT`/`NOTE_BG` are decoration only — every place they're used must also carry a border/rule/icon making the same distinction without the fill.

**Canonical style block (lives in `neet_template.py`; the spec the module must satisfy):**
```python
PAGE_SIZE=A4; MARGIN=1.5*cm; TOP_MARGIN=1.4*cm; BOTTOM_MARGIN=1.4*cm
DARK_GREY=#2C2C2C  MED_GREY=#4A4A4A  SOFT_GREY=#6B6B6B
ROW_ALT=#F0F0F0    NOTE_BG=#E8E8E8   GRID_LINE=#AAAAAA  INK=#1A1A1A

STYLES:
 Title    Times-Bold 20  center
 H1       Times-Bold 10.5 white on DARK_GREY, borderPadding 3, spaceAfter 6
 H2       Times-Bold 9.5  white on MED_GREY,  borderPadding 2, spaceAfter 5
 H3       Times-Bold 9    white on SOFT_GREY, borderPadding 2, spaceAfter 4
 Body     Times-Roman 10.8 leading 14.2
 Bullet1  Times-Roman 10.8 leftIndent 12 firstLineIndent -8 leading 14.2
 Bullet2  Times-Roman 10.5 leftIndent 22 firstLineIndent -8 leading 13.8
 Bullet3  Times-Roman 10.2 leftIndent 32 firstLineIndent -8 leading 13.5
 NoteBox  Times-Italic 10.2 backColor NOTE_BG borderPadding 6 leading 13.5
 Caption  Times-Italic 9.5  center leading 12.5 spaceBefore 3 spaceAfter 8
```
Table styling: DARK_GREY header + white bold text, ROW_ALT alternating rows, 0.4pt GRID_LINE gridlines, 3pt top/bottom + 4pt left/right padding — via `data_table()`, never re-typed hex.

**Heading structure:** H1 dark banner (10.5, badge), H2 medium banner (9.5, smaller badge), H3 soft banner (9, badge optional if short). Badge scales down H1→H2→H3 as grey scales dark→medium→soft (darker+bigger = higher). Badge box sized to text via `stringWidth` — never a fixed box (defect 2 fix; gated by check 2).

**Body & bullets (typographic spec, NOT "one sentence = one bullet"):** Body 10.8/leading 14.2; bullets where prose naturally breaks into points, max 3 levels; more comparative/tabular → use a table. Numbered steps and NOTE/MEMORY-AID text keep normal prose sizing (~10.2–10.8). No style produces text below check_pdf.py's 5.0pt FAIL floor; the 6.0pt WARN band is reserved for legitimate subscripts, not badge/step digits.

**Title block (page 1, no separate title page):** chapter name Times-Bold 20 black centered (no "Chapter N" label line); one small line-art motif (`reportlab.graphics.shapes`, INK, ~1.5cm) loosely themed to topic; HRFlowable rule below; content immediately follows. **Motif is decorative only** — a single outline shape, never resembling/substituting a source figure (keeps it outside Rule 5).

**Table rules:** tables when NCERT compares/classifies or when rewrite converts enumerable/comparative prose; dark header + white bold; alternate shading; 0.4pt #AAAAAA gridlines; 3pt/4pt padding; **no empty cells** (write "N/A" or "—"); `repeatRows=1` across pages; a **0.25pt GRID_LINE rule under every row** (photocopy-survival); full-data tables include every parameter/formula/value (never drop a row to save space).

### §4.1 Icon / Badge System
Fixed shapes drawn with `reportlab.graphics.shapes` (Circle/Rect/Polygon), INK-filled — never Unicode/emoji. All in `neet_template.py`; same shape = same meaning, all chapters:
| Shape | Meaning | Where |
|---|---|---|
| Filled square, white number (`stringWidth`-sized) | Section-number badge | next to every H1/H2/H3 |
| Filled circle | Definition / key term | first-use bolded term — **only** terms also in the summary or an exercise question qualify, capped 3–4/section |
| Filled triangle (point up) | Process / pathway | inside Process Flow only |
| Open (stroke-only) square | Comparison / table pointer | next to a heading whose content became a table |
| 5-point outline star | Memory Aid | corner of every MEMORY AID box |
| Outline circle + bold "!" (drawn from Rect+Circle, not typed) | NOTE | corner of every NOTE box |

Icons are **redundant**, never the only signal: every NOTE keeps its `[NOTE]` label, every MEMORY AID its `[MEMORY AID — not in NCERT]` label, plus the distinctive border. If icons fail to render, the page must still be fully readable.

### §4.2 Process Flow Component
Replaces plain numbered steps for every process/pathway/cycle: numbered triangle badges on a vertical rule. Cyclic processes get a small loop-back arrowhead. Exported as `process_flow()` — do not hand-roll. Reference implementation:
```python
def _step_badge(n, size=14):
    d = Drawing(size, size)
    d.add(Polygon(points=[0,0,size,0,size/2,size], fillColor=INK, strokeColor=INK, strokeWidth=0))
    d.add(String(size/2, size*0.22, str(n), fontName="Times-Bold", fontSize=size*0.5, fillColor=white, textAnchor="middle"))
    return d

def process_flow(steps, cyclic=False):
    rows = []
    if cyclic:
        loop = Drawing(14,10); loop.add(Polygon(points=[2,0,12,0,7,9], fillColor=INK, strokeColor=INK, strokeWidth=0))
        rows.append([loop, Paragraph("<i>(cycle — last step feeds back to step 1)</i>", STYLES["Caption"])])
    for i,s in enumerate(steps,1):
        rows.append([_step_badge(i), Paragraph(s, STYLES["Bullet1"])])
    t = Table(rows, colWidths=[0.7*cm, None])
    t.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),("LINEAFTER",(0,0),(0,-1),0.75,GRID_LINE),
        ("LEFTPADDING",(0,0),(0,-1),0),("RIGHTPADDING",(0,0),(0,-1),4),
        ("TOPPADDING",(0,0),(-1,-1),3),("BOTTOMPADDING",(0,0),(-1,-1),3)]))
    return t
```
**Fallback rule (mandatory):** if a rendered flow misaligns/clips/breaks badly at a page boundary and one honest fix attempt doesn't cure it, fall back to plain numbered steps (`Bullet1`, "1." "2." "3.") for that block and record it in the inventory Coverage (never the PDF). Content correctness outranks decoration — never ship a broken flow, never burn the session debugging graphics.

### §4.3 Boxes — NOTE vs MEMORY AID
Both keep `NOTE_BG` fill + Times-Italic (fill is decoration), told apart primarily by **border**:
- **NOTE** (factual, from NCERT): solid double-rule border (GRID_LINE, two ~1.5pt-apart 0.5pt lines), outline-circle-"!" icon top-left, `[NOTE]` label.
- **MEMORY AID** (labeled `[MEMORY AID — not in NCERT]`, invented mnemonics): dashed border (GRID_LINE, 0.75pt, 3pt-on/2pt-off), outline-star icon top-left. The dash pattern alone tells it apart even with the label covered.
Label, icon, border = three redundant signals for one meaning.

### §4.4 Figures — Step 4 Embed (extraction/verify happened in Pass 1 / Gate 1)
- Use `neet_template.figure(asset_path, caption_text, max_width_cm=...)` — returns image + caption `Paragraph` in `KeepTogether` inside a 0.5pt GRID_LINE border box.
- Scale to text-column width preserving aspect ratio; **never upscale beyond 300 dpi effective**.
- **`max_width_cm` is the pagination lever and acts on neighbours.** A `figure()` block is indivisible (`KeepTogether`): too tall for the remaining space → the whole block moves to the next page, leaving a blank tail. A figure stranded alone, or a section torn across three pages, is almost always this — fix the render width, not a `Spacer`.
  - Budget in points against the measured free tail; the block costs **image height + ~10pt frame padding + caption height + gap**.
  - Shrinking an *earlier* figure pulls text up and adds points to a *later* page's tail — a stubborn break is often cheaper to fix one figure upstream (Ch11 p12: solved by trimming 11.8 and 11.9 together, not 11.9 alone).
  - Downward resizes are safe against the no-upscale cap and raise dpi, but bounded by Step-3(c) legibility and the photocopier rule. Cut the cheap (few-label) figure first.
  - Record every width deviation in the decisions file with before/after numbers + reason, and comment the call site.
- Caption format: **"Fig. 14.2 — <caption>"** keeping the NCERT number verbatim, text rewritten-but-factually-exact (captions keep their own inventory rows). If meaning depended on color, add one caption sentence stating the distinction in words.
- Placement **inline at the exact point where the figure's topic is covered** — never grouped at the end.
- **Every in-figure label must ALSO exist in running text or a table.** Each is a figure-label-matrix row; check 6 fails the build if any label isn't found in the extracted text (permanent fix for defects 5–6).
- **Hard no:** a scientist profile photograph is never embedded, greyscaled or not. Check 4 flags any manifest portrait row.

### ReportLab strict technical rules
- Paragraph objects for ALL text.
- Only these inline tags: `<b>`, `<sub>`, `<super>`, `<i>`.
- Icon/badge/flow system is drawn `reportlab.graphics.shapes` (a vector layer, not inline text) — not an exception to "no decorative Unicode."
- `Image()` only for figures through the full §4.4 pipeline. Never a raw/color/screenshot extraction. Never a photograph of a person.
- **NEVER Unicode sub/superscripts** (O₂, CO₂, H⁺) — use `<sub>`/`<super>`. Check 5 fails on stray codepoints.
- **NEVER Unicode arrows** (→, ⇌) — write "to"/"yields"/plain ASCII. Check 5.
- **NEVER raw Greek** (α, β, γ, Δ) — spell out ("alpha helix", "Delta G"). Check 5.
- **NEVER emoji/decorative Unicode.** Boxes carry plain-text labels in addition to icons/borders.
- **NEVER HTML `<form>`.**
- `KeepTogether` each heading with the flowable after it (no orphaned heading); each figure with its caption.
- Wrap file/library calls in try/except; a missing asset must raise a **loud, named error** — never silently skip a figure.
- **Comment every block with its NCERT section number:** `# ---- 14.1.2 Regulation of Kidney Function ----` directly above its flowables. This is what lets a Pass 3 flag be found and fixed in seconds.
- Keep the script one linear `story.append(...)` sequence grouped by section, in §5 Content Order — the only helpers are those imported from `neet_template.py`. A single fix should touch one contiguous block.

---

## 4. §5 Content Order (the linear script sequence)

1. Title block
2. Unit introduction paragraph (rewritten, tutor style) — if present
3. Scientist profile box (rewritten, factually exact: name, dates, discovery) — if present. **Text only, no photograph.**
4. Chapter sections — reorganized where it helps; headers with section-number badges, bold key terms, tables for comparisons, Process Flow for processes, **figures inline at their topic**
5. Disorders / special topics (if present)
6. NOTE boxes at the end of the section they belong to
7. MEMORY AID boxes where a genuinely useful mnemonic helps (optional, clearly marked)
8. **Quick Recap** — rewritten, denser version of the chapter summary (NOT a copy)
9. **Terms used in the exercises** appendix — only if Rule 2 found gaps, containing **only** GAP questions + answers. Never a walk-through of all N exercises, never a meta note. No gaps → chapter ends at the Quick Recap.

**Traceability:** even when a heading is regrouped/renamed, keep the original NCERT section number visible (e.g. "14.1.2"). Merged sub-sections list both numbers.

---

## 5. Pass 2 workflow — build linearly, then loop render→lint

Write the script **linearly from the frozen inventory**, in Content Order, importing `neet_template.py` so no style is re-declared. **As you write each block, tick its inventory rows off in the inventory file in the same pass** — do not write freehand and reconcile later. Ticking while writing is what stops an item being silently dropped between "I know this fact" and "I typed this fact." Comment every block with its `# ---- N.N ----` marker.

Then loop `render → lint` until green:
```bash
/vercel/share/neetenv/bin/python check_pdf.py "notes/class 12/Ch9_BiotechnologyPrinciplesAndProcesses"
# or explicitly:
/vercel/share/neetenv/bin/python check_pdf.py --pdf <ChapterName>.pdf --inventory <ChapterName>_inventory.md --script <ChapterName>.py
```
`check_pdf.py` auto-discovers sibling PDF/inventory/script by the naming convention. Exit codes: **0 = clean, 1 = ≥1 FAIL, 2 = setup error.** `--strict` treats WARN as failure; `--json` emits a machine-readable report. (Exit 2 for a missing `pymupdf`/`Pillow` means a red gate from a missing library is never mistaken for a real defect.)

### The eight checks
1. **Footer/header band** — no text span inside the top/bottom 1.4 cm margin band. *[defect 1]*
2. **Legibility floor** — no rendered glyph below 5.0pt (FAIL); 5.0–6.0pt is WARN (legitimate subscripts). Badge/step digits are real text spans, so a badge collapsed to ~3.4pt is caught here. *[defects 2, 3]*
3. **Grayscale-only images** — every embedded image is single-channel GRAY or sampled pixels all R==G==B; any real color fails. *[§4.4]*
4. **No person photograph** — a manifest row that looks like a portrait/photo must not be embedded (WARN + human confirmation). *[§5 item 3]*
5. **Banned glyphs** — no Unicode arrows, sub/superscripts, Greek letters, or emoji in the text stream. *[§4 technical rules]*
6. **Figure-label coverage** — every figure-label-matrix row is found in the PDF's extracted running text. *[defects 5, 6]*
7. **Inventory ticked** — every Facts row is ticked. *[Pass 1 completion]*
8. **Page geometry** — every page is A4 portrait.

---

## 6. GATE 2 — must be green before Pass 3 begins

**`check_pdf.py` exits 0 — no FAILs.** A WARN (e.g. check 4's portrait row, or a subscript in the 5–6pt band) may advance **only** after you have eyeballed it and confirmed it is legitimate; treat `--strict` green as the ideal. **Do not begin the human verification pass while the linter is red** — the whole point of v6 is that Pass 3's budget is not spent rediscovering mechanical defects a script already gates.

---

## 7. Big-chapter note (Pass 2 half only)

**Pass 2a** builds the first half into the script, **Pass 2b** the second half into the **SAME** script, ticking rows as you go. A mid-build `check_pdf.py` after 2a is useful, but **Gate 2 is judged on the whole PDF after 2b**. The deliverable is one merged PDF, one script, one inventory — never two part-PDFs.

---

## 8. Reminders that shape a clean Pass 2

- The script is a **deliverable**, not a scratch file — Pass 3 and any later audit edit it via `# ---- N.N ----` markers, never regenerate from scratch. A future session must be able to open the script, jump to a flagged block, fix it, and rerun.
- **Length target ≈ source page count.** No compression pressure — prioritize readability, generous tables, full process flows, and all figures. Completeness and clarity both beat brevity.
- **Rule 6 in force:** no coverage notes, pipeline vocabulary, or editorial self-description in the PDF. Those facts live in the inventory `.md`. The one PDF exception is a *failed-extraction* figure flagged under "Figures requiring manual attention" (an operator-omitted figure is NOT flagged there).
- **Rule 4 in force:** never swap a named term for a synonym; never let a qualifier drift. Type the exact NCERT word.
