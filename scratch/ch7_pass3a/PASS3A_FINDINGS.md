# Ch7 Human Health and Disease — Pass 3(a) Visual Inspection

Build inspected: `notes/class 12/Ch7_HumanHealthAndDisease/Ch7_HumanHealthAndDisease.pdf`
20 pages, 595.3 x 841.9 pt (A4). Every page rendered at 150 dpi and 300 dpi and
inspected directly (40 renders). No page skipped, no page judged from text alone.

Environment rebuilt this session (venv was absent): reportlab 5.0.1, pymupdf 1.28.2,
Pillow 12.3.0 — matches the known-good set recorded in the tracker.

## Gate 2 re-verification (Gate 3 precondition)

Fresh `verify_notes.py` run: **0 FAIL, 1 WARN** — matches the recorded Gate 2 state.

The single WARN is the portrait-keyword check firing on the figure manifest.
Adjudicated as a false positive, on evidence rather than on the previous record's word:
- The chapter embeds exactly 11 images = the 11 numbered figures. There is no 12th image,
  so the M.S. Swaminathan mention is text-only, as the WARN itself asks to confirm.
- `fig_7_3` is a clinical photograph of a ringworm lesion on the chin/jaw — a body-part
  plate, not a person's portrait. Legitimate NCERT figure content.

## Findings

Two candidate defects were found, characterised, root-caused, and then calibrated
against the closed chapters. **Both are pre-existing template-wide behaviour, not Ch7
regressions.** Neither is grounds to hold Gate 3.

### Finding 1 — Stray open square at the right end of `has_table=True` heading banners

Observed on pages 6 (7.1i, 7.2.1), 8 (7.2.3), 9 (7.2.7a), 13 (7.4a) — an unfilled
square outline straddling the dark banner's right edge, reading as a stray empty
checkbox hanging off the banner.

Root cause, traced to the shared template:
- `heading(..., has_table=True)` builds a 3-column table whose 3rd column (0.55cm)
  holds `_icon_table()`, a 9pt open square.
- The banner's dark background is painted by the `H2`/`H3` **ParagraphStyle**
  `backColor`, which only covers the paragraph's own column — never columns 2-3.
- So the icon is always drawn on unpainted white, outside the dark plate.

Scope: `has_table=True` is used by **6 already-closed chapters** (Ch9 Biomolecules
alone uses it 13 times). Rendering the Ch9 instances (p1 y=698.7, p2 y=114.7) produces
a **pixel-identical** notch (`fill='None'`, width 8.0, x0=543.7). This is inherited
house behaviour, present in shipped chapters, not something Ch7 introduced.

### Finding 2 — Two under-filled pages (p3 at 49%, p11 at 44%)

Page 3 ends at 49.4% height and page 11 at 43.7%; the rest of each page is blank.

Root cause: `figure()` keeps image+caption together across page breaks (by design).
The next plate could not fit in the remaining column space, so the whole flowable
moved to the following page:
- p3 → p4: `fig_7_1.png` renders **491.7pt** tall (58% of page height)
- p11 → p12: `fig_7_6.png` renders **451.2pt** tall (54% of page height)

`figure()` scales to the text column and caps width at 300 dpi effective resolution,
but applies **no height cap** — a tall portrait plate can therefore consume over half
the page and strand the preceding page.

Scope, measured across all 14 closed-chapter PDFs (non-last pages below 75% fill):
- Ch5 Molecular Basis of Inheritance: page 7 at **45%** (tallest plate 421.2pt)
- Ch2 Biological Classification: page 6 at **51%** (tallest plate 485.0pt)
- Ch8 Cell The Unit of Life: 4 such pages; Ch3 Plant Kingdom: 3; plus Ch9, Ch10,
  Ch11, Ch12, Ch13 — **10 of 14 closed chapters** show the same pattern.

Ch7's two pages sit inside that established envelope (Ch5 is lower at 45%), and Ch7's
tallest plate (491.7pt) is only marginally above Ch2's shipped 485.0pt. This is the
accepted cost of the keep-together rule, not a Ch7 defect.

## Also noted, not defects

- p2: the malaria life-cycle process flow opens with a "(cycle...)" caption row above
  its numbered steps. Verified as authored content in the chapter script, correctly
  rendered — not a layout break.
- p20 ends at 58% — final page of the chapter, expected.
- Figures 7.1-7.11 all present, framed, monochrome, each with its caption attached;
  the "Reading Figure" prose blocks correctly precede/accompany their plates.

## Verdict

**Pass 3(a) finds no Ch7-specific visual defect.** Both candidate findings reproduce in
already-closed chapters from shared `neet_template.py` code, so fixing them here would
be a template-wide change affecting 10+ shipped chapters — outside the remit of this
chapter's Gate 3 and not a condition of it.

Recommended: log both as known template-level observations for a future deliberate
template pass (a height cap in `figure()`; painting the banner via table BACKGROUND
across all 3 columns instead of ParagraphStyle backColor), and proceed to Gate 3(b).

## Blocker found for Gate 3(b) — cross-document disagreement

`CHAPTER_STATUS.md` line 29 records Ch7 as "PASS 1 COMPLETE — GATE 1 CLOSED", while
`CHAPTER_TRACKER.md` records "PASS 2 COMPLETE — GATE 2 CLOSED". The tracker matches the
verified reality (Gate 2 green). `CHAPTER_STATUS.md` is stale and must be reconciled
atomically as part of the Gate 3 closure write-up, not left for later.
