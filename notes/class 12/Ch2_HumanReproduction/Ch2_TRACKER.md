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

## Pass 3 / Gate 3(a) — GREEN (per-page visual render inspection)

Gate 3 was started after the Gate-2 hard stop. Environment was rebuilt again this session
(venv absent at start; `uv venv` + `uv pip install reportlab pdfplumber pymupdf Pillow numpy`,
interpreter 3.13.11 @ `/vercel/share/neetenv`, reportlab 5.0.1, pymupdf 1.28.2, Pillow 12.3.0).
The PDF was rebuilt from the script and **Gate 2 re-run green against the freshly rebuilt PDF
(0 fail, 0 warn, `--strict` exit 0)** before any 3(a) work — the linter is never carried forward.

All 13 pages rendered at 150 dpi (correction-sensitive regions re-cropped at 300 dpi) and
inspected one by one. Banners, step/number badges, the NOTE box (`!` icon), tables, figures
and captions are structurally consistent on every page. Two flagged artifacts were run to ground:

1. **Page 1 — stray open-square at the right of the "2.1" banner.** *Not* a watermark. It was
   the `_icon_table()` design-system badge emitted by `heading(..., has_table=True)`, which was
   mis-attached to §2.1 — a section that contains **no** `data_table`. The two sections that do
   carry tables (§2.2 mammary-gland structure, §2.6 foetal-growth timeline) were missing the
   badge. **Fix (script):** removed `has_table=True` from the §2.1 heading and added it to the
   §2.2 and §2.6 headings. The badge now marks exactly the table-bearing sections; the page-1
   banner is clean. Verified by re-render.

2. **Page 12 — fig 2.12.** Genuine NCERT source-scan artifacts baked into `assets/fig_2_12.png`:
   the diagonal "…not to be republished" cursive watermark (top/left, over white) and a grey
   vertical bar + dash in the far-right white margin (x≈1198–1232, y≈610–771). **Fix (asset):**
   white-washed in place — the isolated right-margin bar/dash box was set to white (verified to
   contain **zero** dark artwork pixels first), and the watermark strokes were removed by raising
   near-white pixels (tone ≥224) to white only within the top/left white zones, leaving all
   artwork lines, labels and tissue shading (median tone ~166) untouched. Original backed up to
   `scratch/` before editing. Verified by re-render: watermark and bar gone, diagram intact.

**Scope decision (user-confirmed):** the same faint "…not to be republished" scan watermark is
baked into most other figure PNGs (2.1, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, and prominently 2.11).
Per user instruction, **only the two flagged artifacts were remediated**; all other figure
watermarks are left intact as faithful to the NCERT source.

After both fixes the PDF was rebuilt and **Gate 2 re-run green again (0 fail, 0 warn)**, so the
lint state matches the final rebuilt PDF. Gate 3(a) is green. Gate 3(b) (bidirectional content
cross-check) follows.

## Pass 3 / Gate 3(b) — GREEN (bidirectional content cross-check), then HARD STOP

Gate 3(b) was started after the Gate 3(a) green. Environment was rebuilt for this session (venv
does not survive a session boundary): `uv venv` + `uv pip install reportlab pdfplumber pymupdf
Pillow`, interpreter 3.13.11 @ `/vercel/share/neetenv`, reportlab 5.0.1, pymupdf 1.28.2,
Pillow 12.3.0. The PDF was rebuilt from the script and **Gate 2 re-run green against the freshly
rebuilt PDF (0 fail, 0 warn, `--strict` exit 0)** before any 3(b) work — the linter is never
carried forward. pdfplumber hung on this source PDF, so the source text was re-extracted with
pymupdf to `scratch/ch2_gate3b/source_text.txt` (13 pages, ~28.2k chars, 14 images).

**Method — a true bidirectional read across three artifacts:**
- **Direction 1 (source → chapter):** every NCERT source paragraph, caption, hormone pathway,
  numeric fact and figure label was traced forward into the frozen inventory row and then into the
  `Ch2_HumanReproduction.py` block that renders it. Confirmed nothing in the source is silently
  dropped from the chapter.
- **Direction 2 (chapter → source):** every rendered claim in the script was traced back to a
  source sentence. Confirmed the chapter invents nothing and adds no fact absent from NCERT.

**High-risk facts reconciled verbatim (source line → script block), all faithful:**
- Spermatogenesis chain: primary spermatocyte → first meiotic (reduction) division → two haploid
  **secondary spermatocytes with only 23 chromosomes** → second meiotic division → four haploid
  **spermatids** → **spermiogenesis** → spermatozoa → **spermiation** (heads embedded in Sertoli
  cells). Source L197–216 ↔ script L302–312.
- **Sertoli cells provide nutrition** to germ cells; **Leydig (interstitial) cells synthesise and
  secrete testicular androgens**. Source L68–77 ↔ script L120–126.
- Sperm structure — head/neck/**middle piece** (mitochondria, energy)/tail, acrosome cap with
  enzymes. Source L236–242 ↔ script L337–348.
- Hormonal control: **GnRH** (hypothalamic) → anterior pituitary → LH/FSH; LH → Leydig,
  FSH → Sertoli; mid-cycle **LH surge → ovulation**. Source L218–224, L344 ↔ script L323–325,
  L421/L436.
- Ovarian/menstrual: tertiary → **Graafian follicle**, **zona pellucida**, ~**28/29-day** cycle,
  ruptured follicle → **corpus luteum → progesterone**. Source L292–353, L312 ↔ script L383–436.
- Post-fertilisation: morula → **blastocyst** → **trophoblast** + **inner cell mass** →
  implantation → **chorionic villi** ↔ maternal blood; **pregnancy lasts 9 months**; first
  lactation secretion is antibody-rich **colostrum**. Source L440–528 ↔ script L514–650.

**Findings:** **no content defects, no fabrications, no omissions.** The two artifacts fixed in
Gate 3(a) (misattached table badge on §2.1; baked scan artifacts on `fig_2_12.png`) were the only
defects in the chapter, and both remain resolved. No script or asset changes were required in
Gate 3(b); therefore the green Gate 2 above already matches the final delivered PDF.

**Gate 3(b) result: GREEN.** Pass 3 (Gate 3a visual + Gate 3b bidirectional) is complete and the
chapter is faithful to NCERT source, machine-clean, and reproducible.

**HARD STOP after Gate 3(b) (as instructed).** No further passes were started.

Reproduce Gate 3(b) source extraction and the closing Gate 2 from the repo root:
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
