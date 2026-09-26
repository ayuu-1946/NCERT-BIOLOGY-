# Class 11 Chapter 7 — Structural Organisation in Animals Tracker

## Current status — 2026-09-26

**Gate 1 closed; revised Gate 2 is NOT closed; Gate 3 open.** The Earthworm section (7.3) and directly related summary/exercise material remain excluded under the approved syllabus scope. After the user-requested removal of all figure-label NOTE boxes, the rebuilt 16-page PDF fails the strict linter's running-text label coverage check (check 6); the earlier 17-page version passed. The diagrams still carry their printed labels, and Figures 7.21 and 7.22 now sit side by side. No Pass 3 content or page-by-page visual verification has been performed.

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

- Deliverables: `Ch7_StructuralOrganisationInAnimals.py` and `Ch7_StructuralOrganisationInAnimals.pdf` (currently 16 A4 portrait pages); all 398 Facts rows marked `x` in the frozen inventory. Source is `Chapter/class 11/Chapter 07 - Structural Organisation in Animals.pdf`. The script imports the shared `neet_template.py`; figure assets are in `assets/`.
- Content order: intro, 7.1 (four tissue types), 7.2 (organ systems), 7.4 (cockroach), 7.5 (frog), Quick Recap, then the four GAP exercise subparts in the Terms Used in the Exercises appendix. The 14 SUMMARY-UNIQUE rows F368–F381 have named body fold points. All 17 figures remain embedded, but their separate label-transcription NOTE boxes were removed by user request. Figures 7.21 and 7.22 share one two-column row. See `PASS2_DECISIONS.md` for editorial boundaries.
- Historical baseline (before this revision): the 17-page PDF passed the strict linter with 0 failures/warnings and 143/143 labels matched in extracted text. **Current result:** the rebuilt 16-page PDF has **1 failure (check 6), 0 warnings**: 117/143 figure labels fully matched in running text, 3 partial and 23 missing. The other nine checks pass, including 17/17 monochrome embedded images, 398/398 inventory rows ticked, A4 portrait geometry and no orphaned headings. The strict linter exits 1. This follows directly from removing the transcription boxes; the image artwork retains the labels, but the checker cannot extract text from raster artwork.
- This records automated print/bookkeeping results only. Page 15 (the new side-by-side layout) was visually inspected; **all-page Pass 3(a), bidirectional Pass 3(b), a green final linter, rebuild equivalence, and Gate 3 remain pending.** Do not describe the revised chapter as Gate 2 closed or delivered.

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
