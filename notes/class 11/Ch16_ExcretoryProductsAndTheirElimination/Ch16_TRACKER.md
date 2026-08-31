# Ch16 — Excretory Products and their Elimination

## Current status

**PASS 2 COMPLETE — GATE 2 GREEN (2026-08-31).** Normal 3-pass protocol, 12 source pages (`Chapter/class 11/Chapter 16 - Excretory Products and their Elimination.pdf`). Pass 1 (all five sessions `1-S/1-H/1-O/1-F/1-Z`) closed Gate 1 with the inventory **FROZEN** — H1 reads `# Frozen Inventory` — at **178 rows, `F001`–`F178`, contiguous, 0 gaps, 0 duplicate IDs**, now **all 172 Facts rows ticked**. The rewritten chapter script and PDF are built and reproducible (18 pages, ~1065 KB).

**Gate 2:** GREEN. `check_pdf.py` exits 0 — **0 fail, 0 warn** across all 10 checks, re-run against the freshly rebuilt PDF this session.

**Gate 3:** OPEN — Pass 3 dual verification in progress. This chapter is **not** countable in any completion tally until Gate 3 closes.

**Pass 2 defect caught this session (documentation-verification of Gate 2):** the committed script embedded only **5 of 6** figures — **Figure 16.4 "Malpighian body (renal corpuscle)"** (`fig_16_4.png`, asset present, `mode=L`) was never `figure()`-appended, so its image was missing from the PDF while its 4 labels still appeared in running text. `check_pdf.py` did **not** catch this — check 6 verifies label *text* coverage, not image *embedding*, so a dropped embed is invisible to the linter. Fixed by appending `figure("fig_16_4.png", ...)` + its verbatim-labels NOTE at its topic (the Malpighian-body keyterm in 16.1b, tagged `# [VERIFICATION FIX]`). Rebuilt PDF now embeds **6/6** images; Gate 2 re-run stays green (0/0).

## Machine-derived metrics (re-parsed from disk this session, not recalled)

- **178 rows** = **172 Facts + 6 figure-label matrix rows** (matrix `F173`–`F178`).
- **Type census (172 Facts, 11 values, all lowercase):** concept 84 · process 20 · number 15 · heading 15 · opener 13 · definition 13 · example 8 · caption 6 · disorder 2 · list 1 · question 1 = 172. Plus 6 `figure-label` = 178.
- **Heading census: 15 = 8 numbered (16.1–16.8) + 4 run-in (PCT / Henle's Loop / DCT / Collecting Duct, all inside 16.3) + 3 unnumbered (title plate · SUMMARY · EXERCISES).** No `16.N.N` sub-numbered heads exist; `Renal calculi:` / `Glomerulonephritis:` are `disorder` rows (`F163`/`F164`), not headings.
- **Openers: 13** = 15 headings − 3 unpaired (title plate, SUMMARY, EXERCISES) + 1 unheaded chapter-intro opener.
- **Captions: 6** (`F165`–`F170`), verbatim; Fig 16.6 "mechanisms" plural confirmed against the PDF.
- **Summary classification: 22 = 18 BODY-PRESENT + 4 SUMMARY-UNIQUE**, all 4 folded into their named sections pre-freeze.
- **Exercise-gap scan: 12 exercises / 4 genuine gaps**, each with a planned Pass 2 home; 17 non-gaps recorded so a later audit does not re-raise them. Exercise 7's source numbering `(a)(b)(c)(d)(d)` is transcribed verbatim.
- **Figures: 6 numbered → 6 assets**, all 300 dpi `mode=L`, each opened individually at full size, three-part crop audit clean. No unnumbered bonus plate (denominator 6); no person photograph anywhere (check 4 has no manifest row — a true negative).
- **Labels: 76 across 6 figures** (12 / 9 / 11 / 4 / 16 / 24). Harvested by opening each rendered asset, **not** the text layer (two-column layout; callouts are vector artwork). `check_pdf._extract_labels`, imported from the repo linter, returns **76 labels / 6 figure rows / no doubling / no phantom `Fig #` row**.
- **13 figure-only labels flagged** and split into 10 parser artefacts (split subscripts `H2O`/`NH3`/`HCO3-`, artwork-only osmolarity scale marks) + 3 genuine Pass 2 obligations (Inferior vena cava, Dorsal aorta, thick-vs-thin ascending-limb segment).

## Verification this session

- `verify_inventory.py` (run with `/vercel/share/neetenv/bin/python`) — **RESULT: PASS, all 39 checks passed.** It re-parses the source PDF and this inventory and exits non-zero on any drift, so a stale inventory can never look green.
- **Verifier bug fixed this session:** check [4] called `.values()` on the return of `check_pdf._extract_labels`, which returns a flat `list[tuple[str, str]]`, not a dict — it raised `AttributeError` after the label-count assertion. Rewritten to `len(parsed)` plus a distinct-figure-count guard. No inventory row, caption, asset, or the shared linter was touched.
- Encoding hygiene: no Unicode sub/superscripts, no U+FFFD (asserted by the verifier).

## Deliverables

| Deliverable | Status |
|---|---|
| `extract_figures.py` | Present; reproducible 300 dpi extraction + grayscale conversion |
| `Ch16_ExcretoryProductsAndTheirElimination_inventory.md` | Present; **FROZEN, 178 rows**, six-row figure manifest + per-figure label matrix |
| `assets/fig_16_1.png` … `assets/fig_16_6.png` | Present; all `mode=L`, individually visually verified |
| `verify_inventory.py` | Present; **39/39 checks PASS** |
| `Ch16_ExcretoryProductsAndTheirElimination.py` | Present; builds reproducibly, imports `neet_template.py`, embeds 6/6 figures |
| `Ch16_ExcretoryProductsAndTheirElimination.pdf` | Present; 18 pages, ~1065 KB, 6 embedded monochrome figures |
| `check_pdf.py` chapter preflight | **PASS — 0 fail, 0 warn** (Gate 2 green) |

## References

- Source PDF: `Chapter/class 11/Chapter 16 - Excretory Products and their Elimination.pdf`
- Assets: `assets/fig_16_1.png` .. `assets/fig_16_6.png`
- Verifier: `verify_inventory.py` (run with `/vercel/share/neetenv/bin/python`)
- Protocol: `SUPREME COMMAND PROMPT.md` §4.4 (figures), §6 (3-pass workflow), Gate 1
- Checker: `check_pdf.py` (check 6 consumes the label matrix)
