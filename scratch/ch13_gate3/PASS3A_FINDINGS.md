# Ch13 Plant Growth and Development — Gate 3, Pass 3(a) Visual Render Check

**Session:** Gate 3 for Ch13 (Pass 1 + Pass 2 inherited complete; Gate 2 re-confirmed green this session).
**Method:** `pymupdf` rendered every page of the *final rebuilt* PDF at 150 dpi (colour) and again at a 1-bit B&W threshold. Each page inspected directly.

## Environment re-established first (§0.2 discipline)
- `/vercel/share/neetenv/bin/python` was **absent** at session start (expected — venv does not survive a session boundary). Rebuilt with `uv venv ... --python 3.13` + `uv pip install reportlab pdfplumber pymupdf Pillow`.
- Verified interpreter: Python 3.13.11 @ `/vercel/share/neetenv`; reportlab 5.0.1, pymupdf 1.28.2, Pillow 12.3.0 — matches the known-good Ch12 baseline.
- Rebuilt the PDF from the committed script, then re-ran `check_pdf.py`: **VERDICT WARN (0 fail, 1 warn)** = green gate. The single WARN is check 4's known portrait-heuristic false positive: the substring "photo" inside the text rows F056 (Darwin/phototropism), E07 and E09 (photoperiod). No person photograph is embedded — check 3 confirms all 11 embedded images are monochrome, and these are text rows, not images. Accepted, matching the Ch12/tracker baseline.

## Page-by-page render inspection — 10/10 pages

| Page | Contents | Layout | Verdict |
|---|---|---|---|
| 1 | DNA-motif title block + "Plant Growth and Development"; intro prose; Fig 13.1 (bordered, captioned); H1 `13.1 Growth`; H2 `13.1.1` | Title rule clean; figure inside border box; badges legible | CLEAN |
| 2 | Fig 13.2, Fig 13.3 (both bordered/captioned); H2 `13.1.2`, `13.1.3`; three-bullet phase list | Figures correct aspect; captions intact | CLEAN |
| 3 | H2 `13.1.4 Growth Rates`; arithmetic eqn L_t=L_0+rt; Fig 13.5; geometric eqn W_1=W_0 e^{rt} | Sub/superscripts render (reportlab markup, not Unicode); trailing whitespace = KeepTogether pushed Fig 13.6 to p4/p5 — normal | CLEAN |
| 4 | Fig 13.4 (a/b/c multi-part, legend intact); absolute/relative text; Fig 13.7 (leaf areas, superscript cm²) | Both large figures bordered, not squashed | CLEAN |
| 5 | Fig 13.6 (sigmoid, all phase labels); H2 `13.1.5`; H1 `13.2`; H1 `13.3`; process-flow steps 1–2 | Triangle step-badges digits legible; H1 banners identical | CLEAN |
| 6 | Process-flow steps 3–4; Fig 13.8; heterophylly text; Fig 13.9; H1 `13.4`; H2 `13.4.1`; GA₃/C₂H₄ subscripts | Process flow rule aligned with badges across page break (steps 1–2 on p5, 3–4 on p6) | CLEAN |
| 7 | Two-bullet promoter/inhibitor list; data_table (PGR group/Chemical nature/Example); H2 `13.4.2`; discovery bullets; Fig 13.10; H2 `13.4.3`, H3 `13.4.3.1` | Table dark header + alternating rows + gridlines correct; subscripts in cells | CLEAN |
| 8 | Auxin bullets; Fig 13.11 (apical dominance a/b); H3 `13.4.3.2 Gibberellins`; GA₁/GA₂/GA₃; H3 `13.4.3.3 Cytokinins` | Figure bordered; bullets clean | CLEAN |
| 9 | H3 `13.4.3.4 Ethylene`; H3 `13.4.3.5 Abscisic acid`; closing PGR paragraph; NOTE box | NOTE box solid double-rule + `!` icon + `[NOTE]` label render | CLEAN |
| 10 | "Quick Recap" H1 banner; 6 summary bullets with inline L_t/W_1 eqns | End-of-chapter whitespace normal | CLEAN |

## Cross-page style consistency (template held)
Pulled each element type from ≥3 points and confirmed visual identity:
- **H1 banner** (dark band + white bold + number plate): 13.1 (p1), 13.2/13.3 (p5), 13.4 (p6), "Quick Recap" (p10) — identical band height, plate style, font.
- **H2/H3 banner** (medium-grey band): 13.1.1 (p1), 13.1.4 (p3), 13.4.1 (p6), 13.4.3.1 (p7), 13.4.3.5 (p9) — identical.
- **Section-number badge**: legible at print size on every banner (smallest rendered text 6.0 pt per linter — above the 5.0 pt FAIL floor and at the 6.0 pt review band).
- **Figure box**: thin border + italic caption identical on all 11 figures (p1–p8).
- **Process-flow triangle badge**: steps 1–4 (p5–p6) identical digit size, vertical rule aligned.
- **Data table**: single instance (p7) — dark header, white bold, ROW_ALT alternation, gridlines all correct.
- **NOTE box**: single instance (p9) — correct. No MEMORY AID box exists in this chapter (true negative, not a suppressed finding).

## B&W 1-bit print-safety
1-bit threshold render of p9 confirms banners, badges, NOTE border, and the `!` icon all survive; no meaning carried by fill alone. Figure pages remain readable in 1-bit. No fill lighter than #D9D9D9 is the sole carrier of meaning anywhere.

## Pass 3(a) verdict
**10/10 pages inspected. Zero layout, style-drift, or print-safety defects.** No orphaned headings, no overflow, no clipped/squashed figures, no colour channels. Proceed to Pass 3(b) content cross-check.
