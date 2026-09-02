# Ch12 — Respiration in Plants — Figure Extraction Tracker

| Gate | Status | Evidence |
|---|---|---|
| Source PDF located | Done | `Chapter/class 11/Chapter 12 - Respiration in Plants.pdf` |
| Mandatory 440-dpi/5-point grids | Done | `scratch/ch12_figs/grid_4x/p04.png`, `p05.png`, `p06.png`, `p07.png`, `p08.png`, `p09.png`, `p11.png` |
| Numbered figure inventory | Done | `Ch12_RespirationInPlants_inventory.md`; six numbered figures |
| Reproducible extraction script | Done | `extract_figures.py` |
| Three-part crop audit | Pass | `scratch/ch12_figs/audit_results.txt`; all border bands clean, no remaining grazing, no drawing overflow |
| Individual visual review | Pass | `scratch/ch12_figs/grid_findings.md`; all six PNGs opened individually |
| Monochrome conversion | Pass | All six assets report Pillow mode `L` |
| Documentation | Done | Inventory, tracker, and `Ch12_figure_audit.md` |

## Current deliverables

The chapter contains **6 figure assets** under `assets/`: `fig_12_1.png` through `fig_12_6.png`. Each crop excludes its caption and neighboring prose, uses tight spacing rather than a large white border, and preserves the source’s in-figure labels and arrows.

## Layout revision — SS12.4 page break + Fig 12.2 / Fig 12.3 resize (operator instruction)

| Item | Status | Evidence |
|---|---|---|
| SS12.4 moved wholly to page 5 | Done | Explicit `PageBreak()` before `heading("12.4", ...)`; heading + intro + both process-flow steps verified on one page |
| Fig 12.2 enlarged 8.65 cm to 11.0 cm | Done | Fills the page-4 space vacated by SS12.4; below the 12.68 cm 300-dpi natural width of the PR #192 high-DPI asset, so no upscaling; all of SS12.3 still completes on page 4 (first try at 12.2 cm overflowed SS12.3's last paragraph and was rejected) |
| Fig 12.3 reduced 9.0 cm to 8.2 cm | Done | The SS12.4.2 sentence "...oxygen acts as the final hydrogen acceptor" now completes on the same page as Fig 12.3 (page 6) instead of stranding its last line on page 7 |
| Page count | Unchanged | 10 pages before and after |
| Gate 2 (`check_pdf.py`) | Green | 0 FAIL, 1 WARN — the WARN is check 4's keyword scan matching the word "photosynthesis" in inventory prose; check 3 confirms all 6 embedded images are monochrome figure plates, no person photo embedded |
| Pass 3a visual review | Pass | Pages 4, 5, 6 rendered and individually reviewed after Gate 2 + documentation; full-document page-by-page sweep re-confirmed no regression on the untouched pages |

## Layout revision — SS12.5 page break + Fig 12.4 enlargement (operator instruction)

| Item | Status | Evidence |
|---|---|---|
| SS12.5 moved wholly to page 8 | Done | Explicit `PageBreak()` before `heading("12.5", ...)`. SS12.5 previously stranded its banner + opening paragraph at the foot of page 7 under the Fig 12.4 / 12.5 plate while the assumptions list, NOTE and balance sheet ran over to page 8; the whole block now opens page 8 intact |
| Fig 12.4 enlarged 7.0 cm to 8.4 cm | Done | Spends the ~2.4 cm of page-7 column height vacated by SS12.5. Measured render 8.40 cm wide x 14.12 cm tall (was 11.77 cm tall); inside the 9.75 cm 300-dpi natural width, so the move is downward-only and no upscaling occurs |
| Fig 12.5 left at 7.6 cm request | By design | Its 300-dpi natural width is only **6.67 cm**, so `_panel()`'s no-upscale cap already clamps it there and it renders at 6.67 cm regardless. Any larger request would only push it past 300 dpi without changing the render, so the pair was enlarged on the 12.4 side alone |
| Pair still fits the column | Verified | Row measures ~16.1 cm against the 18 cm `FRAME_WIDTH` |
| Page 7 overflow | None | Last content y=775.9 pt against the 802.2 pt column limit |
| Page 8 absorbs the moved block | Verified | Page 8 last content y=722.6 pt against the 802.2 pt limit; it had 129.5 pt of slack before the move |
| Last 2 pages untouched (operator constraint) | Verified | Pages 9 and 10 rendered at 72 dpi and compared byte-for-byte against the `HEAD` build: **pixel-identical** |
| Page count | Unchanged | 10 pages before and after |
| Gate 2 (`check_pdf.py`) | Green | 0 FAIL, 1 WARN, exit 0. Check 9 (orphaned headings) passes — 43 banners all followed by content on their own page, which is the check that governs this revision. The lone WARN is check 4's keyword scan matching the substring "photo" inside "photosynthesis"/"photophosphorylation" in inventory prose; it was reproduced identically on the pre-change `HEAD` build, so this revision introduced no new findings. Check 3 confirms all 6 embedded images are monochrome figure plates with no person photo embedded |
| Pass 3 visual review | Not entered | Operator specified a hard stop at Gate 2. Pages 7 and 8 were rendered and inspected as part of sizing the change, but the Pass 3 sweep was deliberately not started |

## Gate 3(a) — whole-chapter visual render check (2026-09-02)

This is the **Pass 3(a) visual render check only** (SUPREME COMMAND §6 Pass 3(a)). Pass 3(b) — the bidirectional content cross-check against the frozen inventory — was **deliberately not started** this session, so **Gate 3 remains OPEN**. Nothing here closes Gate 3 or moves the Done tally.

**Method.** Every page of the final `Ch12_RespirationInPlants.pdf` (1.0 MB, 10 pp) was rendered twice from the committed PDF via `pymupdf`: a 150-dpi colour pass for direct layout inspection (`scratch/gate3a/color/p01..p10.png`) and a 300-dpi grayscale → 1-bit threshold (cut at 160) pass for print-size legibility and cross-page style consistency (`scratch/gate3a/bw/p01..p10.png`). All 10 pages measured exactly **595×842 pt (A4 portrait)** at render time.

**Per-page layout inspection — 10/10 pages inspected, 0 defects.**

| Page | Elements present | Layout verdict |
|---|---|---|
| 1 | Title H1 (badge 12), H1 banner, NOTE, H2 12.1, table 12.1a (header row) | Clean — no overflow/clip |
| 2 | Table 12.1a continuation (header re-drawn), C₆H₁₂O₆ equation, H3 12.1b, H2 12.2, H3 12.2a, glycolysis flow steps 1–7 | Clean — table splits correctly, flow rule aligned |
| 3 | Glycolysis flow steps 8–10, fate-of-pyruvate table (3-col), Fig 12.1 + caption | Clean — figure correct aspect, caption intact |
| 4 | Fig 12.2 + caption, H2 12.3, H3 12.3a, NOTE, H3 12.3b | Clean — figure correct aspect |
| 5 | H2 12.4, steps 1–2, H3 12.4.1, cyclic TCA flow (steps 1–5), summary equation | Clean — cyclic header + rule intact, superscripts fine |
| 6 | Fig 12.3 + caption, H3 12.4.2, ETS steps 1–6, NADH/FADH₂ ATP table | Clean — figure correct aspect |
| 7 | Oxidative-phosphorylation bullet, H3 12.4.2a, Fig 12.4 (left) + Fig 12.5 (right) two-column plate, both captions | Clean — two-column figure spread balanced, no clip |
| 8 | H2 12.5, NOTE, table 12.5a (3-col), H2 12.6, amphibolic substrate table (3-col), bullets | Clean — no overflow |
| 9 | Fig 12.6 + caption, H2 12.7, RQ formula, RQ table (3-col), NOTE, MEMORY AID, Quick Recap banner | Clean — dashed MEMORY-AID border + star badge intact |
| 10 | Quick Recap bullets (tail) | Clean — ends cleanly, no orphaned heading |

No overflow, no clipping, no table running off the page, no orphaned heading, no process-flow rule misaligned with its badges, and no figure squashed to a wrong aspect ratio were found on any page.

**Cross-page style-consistency matrix (print-DPI B&W pass).** For each element type, one rendered instance was pulled from at least three different points in the chapter and confirmed visually identical — the expected result now that all styles are imported from the frozen repo-level `neet_template.py` (this check confirms the template held rather than hunting hand-typed drift):

| Element | Instances sampled (≥3 points) | Consistent? |
|---|---|---|
| H1 banner + section badge | p1 (only H1 in chapter) | Yes (single instance) |
| H2 banner (dark bar, white numbered square badge) | p1 (12.1), p5 (12.4), p9 (12.7) | Yes — identical bar tone, badge, white bold serif |
| H3 banner (softer grey, smaller badge) | p2 (12.2a), p6 (12.4.2), p7 (12.4.2a) | Yes — identical |
| Table (solid header row + white text, thin body borders) | p1 (12.1a), p6 (ATP table), p9 (RQ table) | Yes — identical header treatment and gridlines |
| NOTE box (light fill, circled "!" badge, italic) | p1, p4, p9 | Yes — identical |
| MEMORY AID (dashed border, star badge, italic) | p9 (only instance in chapter) | Yes (single instance) |
| Process-flow (numbered triangle badges + vertical rule) | p2 (glycolysis), p5 (TCA cyclic), p6 (ETS) | Yes — identical triangle badge + rule |
| Figure box (bordered, grayscale plate, italic caption) | p3 (12.1), p7 (12.4/12.5), p9 (12.6) | Yes — identical border + caption style |

Under the 1-bit threshold the grey figure fills drop out cleanly to crisp line-art, all banner bars stay solid, and every step-badge digit and section-badge digit remains legible at print size — consistent with the Gate 2 check-2 result (smallest glyph 6.0 pt).

**Pass 3(a) verdict: PASS — 10/10 pages inspected, zero layout or style-consistency defects.** Renders saved under `scratch/gate3a/`. **Gate 3 is NOT closed**: Pass 3(b) (bidirectional full read, both directions, per-section reading claims) has not been run, and Gate 3's five closure conditions therefore do not yet hold.

## Repin history

Figure 12.1 was repinned once after the first mechanical audit detected neighboring prose grazing the right edge. Its right boundary changed from `x1=299` to `x1=296`; the corrected asset passed the text-layer gate and was visually confirmed complete. No other rectangle required correction.

## Environment record

The record below is refreshed per session, because `/vercel/share/neetenv` lives outside the repo and **does not survive a session boundary** — see SUPREME COMMAND §0.2. Treat any earlier interpreter path in this file as historical, not as evidence the environment is present.

- **Original extraction session:** `/usr/bin/python3` (Python 3.12.3) with `/home/ubuntu/NCERT-BIOLOGY-` writable; PyMuPDF 1.28.2, Pillow 12.3.0, NumPy 2.5.1, pdfplumber 0.11.10, ReportLab 5.0.0.
- **SS12.5 page-break / Fig 12.4 enlargement session:** the venv was absent at session start and was rebuilt per §0.2 with `uv venv /vercel/share/neetenv --python 3.13`. Active interpreter `/vercel/share/neetenv/bin/python` (Python 3.13.11, `sys.prefix=/vercel/share/neetenv`); reportlab 5.0.1, pymupdf 1.28.2, Pillow 12.3.0, pdfplumber present. Verified against the §0.3 known-good reference before any build or gate was run.
- **Gate 2 re-verification / documentation session (2026-09-02):** the venv was again absent at session start (expected §0.2 state) and rebuilt with `uv venv /vercel/share/neetenv --python 3.13`. Active interpreter `/vercel/share/neetenv/bin/python` (Python 3.13.11, `sys.prefix=/vercel/share/neetenv`); reportlab 5.0.1, pymupdf 1.28.2, Pillow 12.3.0, pdfplumber OK — matches the §0.3 reference. `check_pdf.py` re-run against the delivered PDF returned **exit 0, VERDICT WARN (0 fail, 1 inspected-benign warn)**; the check-4 WARN was re-confirmed a true-negative and Gate 2 remains **CLOSED**. Repo-level `CHAPTER_STATUS.md` and `CHAPTER_TRACKER.md` were updated to record the closure.

- **Gate 3(a) render-check session (2026-09-02):** the venv was again absent at session start (expected §0.2 state) and rebuilt with `uv venv /vercel/share/neetenv --python 3.13`. Active interpreter `/vercel/share/neetenv/bin/python` (Python 3.13.11, `sys.prefix=/vercel/share/neetenv`); pymupdf 1.28.2, Pillow 12.3.0 — matches the §0.3 reference. Used only to render every page of the committed PDF for the Pass 3(a) visual check documented above; no script or PDF was modified, so Gate 2 needs no re-run this session.

The reusable setup note is `setup_environment.md` at the repository root.

## References

[1]: `../../../../SUPREME COMMAND PROMPT.md` "Repository SUPREME COMMAND prompt"
[2]: `../../../../skills/ncert-figure-extraction/SKILL.md` "ncert-figure-extraction workflow"
