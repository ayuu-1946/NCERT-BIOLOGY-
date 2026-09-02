# Ch2 Human Reproduction — Figure Extraction Tracker

## Current status

**Previous chapter-specific extraction work:** Deleted as requested.  
**Fresh figure extraction:** Complete for the extraction-only scope.  
**Figure census:** 12 numbered figures represented by 14 assets; Figures 2.1 and 2.3 are split into labeled `(a)` and `(b)` assets.  
**Assets:** 14/14 present, all freshly regenerated from the source PDF and converted to `mode=L`.  
**Visual review:** Fresh 4× grid inspection and final contact-sheet review completed; correction-sensitive assets were individually checked.  
**Full replacement chapter/PDF gate:** In progress.

## Pass 1 / Gate 1 — GREEN (frozen inventory)

Pass 1 ran as five discrete sessions (1-S source read + facts, 1-H heading sweep, 1-O opener sweep, 1-F figure harvest, 1-Z gaps/summary/freeze). The frozen inventory `Ch2_HumanReproduction_inventory.md` is machine-validated:

- **220 rows**, IDs contiguous `F001..F220` — no gaps, no duplicates, no letter-suffixed IDs.
- `Type` column normalized to one vocabulary: 1 title, 8 openers, 10 headings (7 numbered + 3 unnumbered: Menstrual Hygiene, SUMMARY, EXERCISES), 14 captions, 187 content rows.
- **Figure-label matrix validated with `check_pdf.py`'s own `_extract_labels`:** 14 distinct figure rows (2.1a, 2.1b, 2.2, 2.3a, 2.3b, 2.4–2.12), 131 labels, **no doubling, no phantom rows.** Each caption row carries a unique figure number in the Section column so no two figures collapse.
- Every header/census count matches a re-parse of the table; each census total is derivable from the list beside it.
- All 14 figures marked `Mono: yes`, `Verified: yes`.
- 3 SUMMARY-UNIQUE facts folded into body rows F076, F077, F204; 2 exercise gaps (Q20 twins, Q21 litter) have a planned appendix home.

Gate 1 is green; Pass 2 (build the script from the frozen inventory + `check_pdf.py` render→lint loop) may begin.
Validation scripts live in `scratch/ch2_gate1/` (`validate_gate1.py`).

## Pass 2 / Gate 2 — GREEN (check_pdf.py, then HARD STOP)

Pass 2 wrote the replacement chapter script `Ch2_HumanReproduction.py` linearly from the frozen
inventory in Content Order (§5), importing the repo-level frozen `neet_template.py` (§0.6) — no
style, geometry, colour or font re-declared. Every one of the 220 Facts rows was ticked in the
inventory (`x` in the Ticked column) as it was written, and all 14 assets are embedded inline at
their topic via `neet_template.figure()`.

Environment for this session (rebuilt; venv does not survive a session boundary):
- `/vercel/share/neetenv/bin/python` was **absent** at session start and was rebuilt per §0.2
  (`uv venv` + `uv pip install reportlab pdfplumber pymupdf Pillow`). Verified interpreter
  3.13.11 @ `/vercel/share/neetenv`, reportlab 5.0.1, pymupdf 1.28.2, Pillow 12.3.0.

Deliverables produced by Pass 2:
- `Ch2_HumanReproduction.pdf` — 13 pages, A4 portrait, 3.86 MB.
- `Ch2_HumanReproduction.py` — the exact generating script (block-marked `# ---- N.N ----`,
  row IDs traced in comments).
- Inventory `Ch2_HumanReproduction_inventory.md` — all 220 Facts rows ticked.

**Gate 2 result — `check_pdf.py "notes/class 12/Ch2_HumanReproduction"`: VERDICT PASS (0 fail, 0 warn).**
`--strict` also exits 0. All ten checks green:

| # | Check | Result |
|---|-------|--------|
| 1 | Footer/header band | PASS — no text in top/bottom margin bands |
| 2 | Legibility floor | PASS — smallest rendered text 6.0pt (FAIL<5.0, WARN<6.0) |
| 3 | Grayscale-only images | PASS — all 14 embedded images monochrome |
| 4 | No person photograph | PASS — no portrait/photo row in manifest |
| 5 | Banned glyphs | PASS — no Unicode arrows / sub-super / Greek / emoji |
| 6 | Figure-label coverage | PASS — 131/131 labels fully in text; 0 partial; 0 missing |
| 7 | Inventory ticked | PASS — all 220 Facts rows ticked |
| 8 | Page geometry | PASS — all 13 pages A4 portrait (595x842pt) |
| 9 | Orphaned headings | PASS — 48 banner headings, none stranded |
| 10 | Badge/banner collision | PASS — 106 filled plates, no collisions |

**HARD STOP after Gate 2 (as instructed).** Pass 3 (dual verification — full bidirectional read
+ per-page visual render check, ending in Gate 3) has **NOT** been started. The chapter is not yet
delivered; it is parked at a green Gate 2, which is the sanctioned foundation on which Pass 3 may
later begin.

Reproduce Gate 2 from the repo root:
```bash
ls /vercel/share/neetenv/bin/python   # rebuild per §0.2 if absent
/vercel/share/neetenv/bin/python 'notes/class 12/Ch2_HumanReproduction/Ch2_HumanReproduction.py'
/vercel/share/neetenv/bin/python check_pdf.py 'notes/class 12/Ch2_HumanReproduction' --strict
```

## Re-pin and replacement record

The former `notes/class 12/Ch2_HumanReproduction/` directory and related Human Reproduction scratch artifacts were deleted before rebuilding. The source PDF was not modified. Rectangles were then re-established from fresh 4× grid overlays. The new extraction removed caption, prose, and page-number remnants identified during review, retained connected multi-panel figures 2.8 and 2.11 as complete assets, and preserved all documented in-figure labels.

## Deliverables

The chapter folder contains the reproducible extraction script, the frozen inventory with the per-figure label matrix, the detailed audit, and 14 grayscale PNG assets under `assets/`. The raw source census, 4× grid overlays, extraction output, and audit output remain in `scratch/` during this session for re-audit.

## Reproduction commands

From the repository root:

```bash
/vercel/share/neetenv/bin/python 'notes/class 12/Ch2_HumanReproduction/extract_figures.py'
/vercel/share/neetenv/bin/python scratch/audit_human_reproduction_figures.py
```

## References

[1]: `../../../../Chapter/class 12/Chapter 2 - Human Reproduction.pdf` "NCERT Biology, Class 12, Chapter 2: Human Reproduction"
[2]: `../../../../SUPREME COMMAND PROMPT.md` "Repository SUPREME COMMAND prompt"
[3]: `../../../../skills/ncert-figure-extraction/SKILL.md` "ncert-figure-extraction workflow"
