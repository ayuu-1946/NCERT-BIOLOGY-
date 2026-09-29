---
name: ncert-layout-match
description: Fix layout and pagination of an existing NCERT/NEET chapter notes script (ReportLab, neet_template.py) so its PDF matches a user-supplied reference PDF page by page, without touching the script's template or styling. Use when the user gives a reference PDF (often exported from an edited DOCX) plus replacement figures and says to match layout, pagination, figure sizes or captions, remove/adjust text, or "fix the script, don't rewrite it".
---

# NCERT layout match

The chapter script and `neet_template.py` are the gold standard for STYLE. The reference PDF is the authority for LAYOUT and PAGINATION only. Fix the flaw (spacing, page boundaries, figure size, captions); never replace the styled element. Do not swap `keyterm` for plain bullets, add labels the template lacks (e.g. a "CHAPTER 17" line from the docx), change banners, DNA-motif title, NOTE / MEMORY AID boxes or tables.

## Workflow

1. Clone the repo; find `notes/class N/ChXX_*/ChXX_*.py`. Read the script fully. Never rewrite it wholesale; patch it.
2. Diff reference vs current: `scripts/compare.py <ref.pdf> <cur.pdf>` prints page count, per-page start text match, sentence-level text diffs, and reference image widths (cm).
3. Look at both as contact sheets before editing (render at ~60 dpi). Note where the reference breaks pages.
4. Figures: user zips replace `assets/`. Convert each to mode `L` (`ImageOps.autocontrast`, 300 dpi) because the template raises on non-mono images. Composite PNGs (two figures in one) get a new asset name (e.g. `fig_17_7_8.png`).
5. Patch, in this order:
   - Text edits the reference implies (removed exercises/sub-parts, etc.). Delete whole blocks; keep neighbouring gaps.
   - Figure `max_width_cm` = reference image width from step 2.
   - `PageBreak()` at each reference page start (comment `# ref pN`).
   - Composite figures: one framed image, each caption directly under its own half (`figure_pair`: split x = widest blank gutter in the 25-75% band of the image). No caption detached from its artwork.
   - If a page overflows by a line or two, shrink `gap()` on that page only (e.g. `gap(2)`), never the template.
6. Rebuild. Verify: page count equals reference; every page's first ~22 chars match; view changed pages.
7. Run `python3 check_pdf.py "<chapter folder>"`. Compare against the committed HEAD result; report pre-existing failures as pre-existing (e.g. check 6 figure-label coverage) instead of forcing text into the PDF.
8. Update the chapter README page/image counts if stale. Do NOT commit or push unless asked; deliver the PDF, script, and changed assets.

## Rules learned

- User wording like "don't add X label" can conflict with the reference; if the reference has it but the script's template does not, follow the template and say so.
- Keep the user's terse tone: report what changed, what was kept, what still fails. No long explanations.
- Fix in place: "infection in the finger: medicate, don't amputate."
