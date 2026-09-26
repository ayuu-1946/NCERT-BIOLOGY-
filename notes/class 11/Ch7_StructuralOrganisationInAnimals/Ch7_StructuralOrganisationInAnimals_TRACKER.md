# Class 11 Chapter 7 — Structural Organisation in Animals Tracker

## Current status — 2026-09-26

**Gate 1 closed; Gate 2 closed for the requested NEET syllabus scope; Gate 3 open.** The Earthworm section (7.3) and directly related summary/exercise material are intentionally excluded under the approved syllabus scope. The Pass 2 script and PDF are present. The strict PDF linter passes with 0 failures and 0 warnings. This is a mechanical Gate 2 result, **not** a Pass 3 content or page-by-page visual verification.

### Syllabus-scoped inventory evidence

- `Ch7_StructuralOrganisationInAnimals_inventory.md` contains **398 rows**, F001–F398, contiguous and duplicate-free: `fact` 322 · `caption` 17 · `heading` 15 · `opener` 13 · `summary-unique` 14 · `figure-labels` 17.
- **53 syllabus-scope summary sentences** are classified: 14 SUMMARY-UNIQUE and 39 BODY-PRESENT. Retained summary wording/order is checked against the source summary.
- **29 syllabus-scope exercise subparts** are classified: 4 GAP and 25 COVERED.
- In the introduction, two transition/rhetorical items were accepted for removal; a general cell-count fact was rejected for removal and retained. The individual decision log follows below.
- Figure extraction was not repeated. The figure manifest lists 17 figures and 143 parsed labels; all 22 existing PNG assets were re-probed as single-channel grayscale.
- `verify_gate1.py` checks row counts, source alignment, retained summary/exercise classifications and figure assets for this syllabus scope.

### User-accepted filtering decisions

Using the pre-filter inventory IDs: **F001 accepted for removal** (chapter-transition sentence); **F006 accepted for removal** (rhetorical question); **F005 rejected for removal and retained** (general human-cell-count statement). IDs in the current inventory were then renumbered contiguously.

### Source edition and figure evidence

The supplied PDF contains printed pages 100–106 and 111–122; pages 107–110 and Figures 7.9–7.13 are absent. The source edition contains section 7.3, but the user confirms Earthworm has been removed from the NEET syllabus, so that material is out of scope for this syllabus-aligned inventory. No facts from another edition were imported. Figure extraction and the existing visual/crop audits were retained unchanged; see `audit_report.txt`, `audit_figures.py`, and `extract_figures.py`.

### Pass 2 build and Gate 2 evidence

- Deliverables: `Ch7_StructuralOrganisationInAnimals.py` and `Ch7_StructuralOrganisationInAnimals.pdf` (17 A4 portrait pages); all 398 Facts rows marked `x` in the frozen inventory. Source is `Chapter/class 11/Chapter 07 - Structural Organisation in Animals.pdf`. The script imports the shared `neet_template.py`; figure assets are in `assets/`.
- Content order: intro, 7.1 (four tissue types), 7.2 (organ systems), 7.4 (cockroach), 7.5 (frog), Quick Recap, then the four GAP exercise subparts in the Terms Used in the Exercises appendix. The 14 SUMMARY-UNIQUE rows F368–F381 have named body fold points in the script. The 17 retained figures are embedded at their topics; their 143 figure-label strings are repeated in adjacent NOTE boxes for text-layer coverage. See `PASS2_DECISIONS.md` for the editorial boundaries and distinctions.
- From the repository root, `/vercel/share/neetenv/bin/python check_pdf.py --strict "notes/class 11/Ch7_StructuralOrganisationInAnimals"` exits 0: **PASS, 0 fail, 0 warn**. Checks 1–10 pass; 17/17 images monochrome, 143/143 label strings matched in extracted text, 398/398 inventory rows ticked, no orphaned heading (69 banners), no badge collisions (129 plates), smallest glyph 6.0 pt. Check 4 passes because there is no portrait/photo row, not because a portrait was manually reviewed.
- This validates the automated print and bookkeeping checks only. It does **not** attest to a human inspection of all 17 rendered pages or a bidirectional source-to-script content read. **Pass 3(a), Pass 3(b), rebuild equivalence, and Gate 3 remain pending.** Do not describe the chapter as delivered or Gate 3 closed until all five Gate 3 conditions in the source prompt have been met.

### Reproduction / validation

Gate 1 was originally checked in a repo-ignored Python 3.11.2 `.venv` when the canonical environment was unavailable. This is historical Gate 1 evidence, not the current runtime. In the Pass 2 session, `/vercel/share/neetenv` was rebuilt with Python 3.13 and the required ReportLab, pdfplumber, PyMuPDF, and Pillow packages. From the repository root:

```bash
/vercel/share/neetenv/bin/python 'notes/class 11/Ch7_StructuralOrganisationInAnimals/Ch7_StructuralOrganisationInAnimals.py'
/vercel/share/neetenv/bin/python check_pdf.py --strict 'notes/class 11/Ch7_StructuralOrganisationInAnimals'
```

For the original Gate 1 checks (the audit depends on its original environment and may need NumPy):

```bash
./.venv/bin/python 'notes/class 11/Ch7_StructuralOrganisationInAnimals/verify_gate1.py'
./.venv/bin/python 'notes/class 11/Ch7_StructuralOrganisationInAnimals/audit_figures.py'
```
