# Ch14 Breathing and Exchange of Gases — Tracker

## Pass / gate status

**Pass 1: COMPLETE — GATE 1 CLOSED (2026-08-31).**
- Inventory **FROZEN at 139 rows, `F001`–`F139`, contiguous, 0 gaps, 0 duplicate IDs, 0 ticked** (machine re-parsed from the finished table).
- Blocks: 107 Facts (`1-S`) + 14 heading (`1-H`) + 12 opener (`1-O`) + 0 summary-unique (`1-Z`) + 6 figure-label matrix (`1-F`) = **139**, equal to the highest ID.
- Type census (10 lowercase values, machine-derived, sums to 139): `concept` 47 · `definition` 27 · `number` 18 · `heading` 14 · `opener` 12 · `process` 9 · `figure-label` 6 · `example` 3 · `name` 2 · `list` 1.
- Heading census **10 numbered + 4 unnumbered = 14**; openers **12**.
- Summary classification **18 sentences = 18 BODY-PRESENT + 0 SUMMARY-UNIQUE** — nothing to fold into the body.
- Exercise-gap scan: **14 exercises / 3 genuine gaps** (hypoxia definition, high-altitude respiratory effect, sigmoid-curve reason), each with a planned home noted in the inventory.
- Figure-label matrix machine-checked: `check_pdf.py`'s own `_extract_labels` returns **42 labels across 6 figure rows, no doubling, no phantom `Fig #` row**. (Gate 1 had recorded this as 47 — a hand-tally error in a stated count only, corrected in all four live restatements at Gate 2; no label row or asset changed. See the inventory's Gate 2 record.)

**Pass 2: COMPLETE — GATE 2 CLOSED (2026-08-31).**
- Script `Ch14_BreathingAndExchangeOfGases.py` written linearly from the frozen inventory in Content Order (§5), importing the repo-level `neet_template.py`; no style, geometry, colour or font re-declared. Every block carries its `# ---- N.N ----` marker and inventory row IDs.
- PDF generated: **9 pages, 814 KB** (source is 12 PDF pages / textbook pp. 183–192).
- **`check_pdf.py` exits 0 — VERDICT PASS, 0 fail / 0 warn, green under `--strict`.** All ten checks pass: no footer/header band text · smallest rendered text **6.0pt** · all **6** images monochrome · no person photo · **0** banned Unicode glyphs · figure-label coverage **42/42** (0 partial, 0 missing) · inventory **139/139** Facts rows ticked · **9/9** pages A4 portrait · **53** headings unorphaned · **82** badge plates collision-free.
- Inventory ticking complete: all **145** boxes `[x]` (139 `F001`–`F139` rows + 6 `F133b`–`F133g` figure-label rows), ticked while writing.
- Exercise gaps closed in a **Terms Used in the Exercises** appendix (Ex 9 high altitude, Ex 11 sigmoidal reason, Ex 12 hypoxia, plus the Ex 14 per-hour derivation), all derived strictly from chapter content. The freeze was **not** back-dated; no `a`-suffixed rows were added.
- Only one render/lint cycle was needed for content — the first run's single FAIL was check 7 (rows not yet ticked), the expected bookkeeping step.

**Pass 3: COMPLETE — GATE 3 CLOSED (2026-08-31). CHAPTER DONE.**
- Venv was **absent at session start** (expected §0.2 state); rebuilt to the §0.3 reference versions before any diagnosis.
- **Reproducibility checked first:** committed PDF fingerprinted, regenerated from the script, re-fingerprinted — **9 pages / 23,863 chars / 6 images, identical.**
- **One confirmed defect, D1 (audit-trail):** Gate 2's inherited claim of "0 warn, green under `--strict`" was **false when re-tested** — `--strict` returned WARN/exit 1 because the verdict table pasted into the inventory contains the words *portrait*/*photograph*, which check 4 scans for in any table row. The act of documenting Gate 2 invalidated its own claim. Fixed by rewording two cells (**metadata only — no Facts row, caption or asset touched**); `--strict` now genuinely **exit 0, 0 fail / 0 warn**.
- **`check_pdf.py` was deliberately NOT modified.** The same words appear in 12 other inventories, and in Ch11 (RAMDEO MISRA) and Ch1 (ERNST MAYR) they are **real content rows** where check 4 firing is intended. Editing the shared frozen linter would have blinded every chapter with an actual scientist profile.
- **Pass 3(a): 9/9 pages inspected** at 125 dpi and at 300 dpi 1-bit. No overflow/clipping/orphan; no figure squashed (all 6 drawn aspect ratios match source to 3 dp); font canon holds at **only the four Times base-14 faces**; smallest span **6.0pt**; NOTE vs MEMORY AID still distinguishable at 1-bit.
- **Pass 3(b): full read, both directions, 11 section-pair reading claims** naming source pages against script blocks. All NCERT headings map one-to-one to script blocks; every section's antecedent sentence and every heading-word definition verified. **0 MISSING · 0 FABRICATED · 0 DRIFTED · 0 UNINVENTORIED** — no row added, freeze intact.
- **4 false positives documented** (not discarded): the `pO2`/`pCO2` misread of a page image, the "missing" Fig 14.2(b) that `KeepTogether` moved to p4, the ALFONSO CORTI unit-divider profile (Ch18's, not Ch14's), and NCERT's own `(Figure 14.4)` typo which the notes handle correctly.
- **3 carry-overs** logged (C1 p3 whitespace — do not "fix"; C2 never spell check-4 trigger words in an inventory table row; C3 keep subscripts as tags).

## Current status (figure extraction — completed in a prior task)

**Figure extraction stage:** Complete.  
**Figure census:** 5 numbered figures → 6 assets, with Figure 14.2 split into `(a)` and `(b)`.  
**Assets:** 6/6 present, all `mode=L`, all individually visually reviewed.  
**Three-part crop audit:** Complete. Checks A and C are clean for all assets; check B is clean for five assets. Figure 14.4 retains one explained 8.7-point source-PDF vector-tail warning below the meaningful visible artwork; no label or diagram edge is clipped and the caption is excluded.  
**Full chapter replacement/PDF gate:** Not started by that figure-extraction task; the notes PDF was generated later, in Pass 2 (Gate 2 closed — see above).

## Re-pin log

| Asset | Change | Reason |
|---|---|---|
| `fig_14_2b.png` | Final top boundary set to `y0=330` | Earlier visual preview included the neighboring upper-panel `(a)` marker; the final crop begins below it while retaining the “Air expelled from lungs” label. |
| `fig_14_5.png` | Left boundary set to `x0=292` | The first crop grazed the graph’s left tick labels; the boundary was expanded to include all tick labels and then passed the text-layer check. |
| `fig_14_4.png` | Bottom boundary tightened to `y1=660` | Earlier crop included caption text. The final asset excludes the caption and retains all meaningful diagram content; the residual vector tail is documented in `Ch14_figure_audit.md`. |

## Reproduction commands

From the repository root:

```bash
# Environment first — the venv does NOT survive a session boundary (§0.2)
ls /vercel/share/neetenv/bin/python || { uv venv /vercel/share/neetenv --python 3.13; \
  uv pip install --python /vercel/share/neetenv/bin/python reportlab pdfplumber pymupdf Pillow; }

# Figures (already complete; re-run only if re-extracting)
/vercel/share/neetenv/bin/python 'notes/class 11/Ch14_BreathingAndExchangeOfGases/extract_figures.py'
/vercel/share/neetenv/bin/python scratch/audit_ch14_figures.py

# Pass 2: render the notes PDF, then run the Gate 2 linter
/vercel/share/neetenv/bin/python 'notes/class 11/Ch14_BreathingAndExchangeOfGases/Ch14_BreathingAndExchangeOfGases.py'
/vercel/share/neetenv/bin/python check_pdf.py "notes/class 11/Ch14_BreathingAndExchangeOfGases" --strict
```

## Deliverables

All four per-chapter deliverables are now present in the chapter folder: the **notes PDF** (`Ch14_BreathingAndExchangeOfGases.pdf`, 9 pages), the **exact script that generated it** (`Ch14_BreathingAndExchangeOfGases.py`), the **frozen inventory** with the per-figure label matrix (now fully ticked), and the **`assets/` folder** with six grayscale PNGs. The reproducible extraction script and the detailed crop audit sit alongside them. The raw grid overlays, extraction log, audit output, geometry probes, and visual-review notes remain in `scratch/ch14_figs/` and `scratch/ch14_visual_findings.md` for re-audit.

## References

[1]: `../../../../SUPREME COMMAND PROMPT.md` "Repository SUPREME COMMAND prompt"
[2]: `../../../../skills/ncert-figure-extraction/SKILL.md` "ncert-figure-extraction workflow"
