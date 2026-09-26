# Class 11 Chapter 7 — Structural Organisation in Animals Tracker

## Current status — 2026-09-26

**Gate 1 closed; revised Gate 2 is NOT closed; Gate 3 open.** The Earthworm section (7.3) and directly related summary/exercise material remain excluded under the approved syllabus scope. After the figure-label NOTE boxes were removed at the user's request and the latest prose edits were applied, the rebuilt 16-page PDF has two strict-linter failures: figure-label running-text coverage (check 6) and four intentionally unticked, user-approved removals (check 7). No Pass 3 full-document verification has been performed.

### Syllabus-scoped inventory evidence

- `Ch7_StructuralOrganisationInAnimals_inventory.md` contains **398 rows**, F001–F398, contiguous and duplicate-free: `fact` 322 · `caption` 17 · `heading` 15 · `opener` 13 · `summary-unique` 14 · `figure-labels` 17.
- **53 syllabus-scope summary sentences** are classified: 14 SUMMARY-UNIQUE and 39 BODY-PRESENT. Retained summary wording/order is checked against the source summary.
- **29 syllabus-scope exercise subparts** are classified: 4 GAP and 25 COVERED.
- The current prose revision has four accepted omissions: F007, F083, F113, and opener F355. These remain in the frozen inventory but are intentionally unticked; **394/398 rows are ticked**. Earlier intro removals and the rejected broad cell-count removal are also recorded below.
- Crop rectangles and figure census are unchanged; Figure 7.3 was rerendered at 520 dpi from its vector source for larger placement, and the full three-part crop audit was rerun. The manifest lists 17 figures and 143 parsed labels; all 22 PNG assets remain single-channel grayscale.
- `verify_gate1.py` checks row counts, source alignment, retained summary/exercise classifications and figure assets for this syllabus scope. Since it is a pre-Pass-2 validator, its “0 rows ticked before Pass 2” assertion now reports one expected failure after the 394 retained rows were ticked and four approved omissions left unticked.

### User-accepted filtering decisions

Using the current inventory IDs, the new approved omissions are **F007** (redundant four-tissue-types sentence), **F083** (blood cross-reference), **F113** (redundant preview of the worked examples), and **F355** (chapter-transition opener). From the earlier pass, the chapter-transition/rhetorical intro items were accepted for removal and the broad human-cell-count fact was rejected for removal and retained.

### Source edition and figure evidence

The supplied PDF contains printed pages 100–106 and 111–122; pages 107–110 and Figures 7.9–7.13 are absent. The source edition contains section 7.3, but the user confirms Earthworm has been removed from the NEET syllabus, so that material is out of scope for this syllabus-aligned inventory. No facts from another edition were imported. Figure extraction and the existing visual/crop audits were retained unchanged; see `audit_report.txt`, `audit_figures.py`, and `extract_figures.py`.

### Pass 2 build and Gate 2 evidence

- Deliverables: `Ch7_StructuralOrganisationInAnimals.py` and `Ch7_StructuralOrganisationInAnimals.pdf` (currently 16 A4 portrait pages); source is `Chapter/class 11/Chapter 07 - Structural Organisation in Animals.pdf`. The script imports the shared `neet_template.py`; figure assets are in `assets/`.
- Content order: intro, 7.1 (four tissue types), 7.2 (organ systems), 7.4 (cockroach), 7.5 (frog), Quick Recap, then the four GAP exercise subparts in the Terms Used in the Exercises appendix. The 14 SUMMARY-UNIQUE rows F368–F381 have named body fold points.
- The eight latest requested edits are implemented in the generator: the body opens directly with unicellular organisms; redundant F007 and F113 are removed; the blood paragraph ends after the transport sentence; the evolutionary-trend sentence is reframed; the skeletal-muscle entry says only “Voluntary”; the Chapter 21 aside is removed; and the frog-colour sentence is reframed while retaining the following hibernation statement. The worked-example NOTE remains.
- All 17 figures remain embedded, but their separate label-transcription NOTE boxes were removed by earlier user request. Figures 7.21 and 7.22 share one two-column row. In this layout pass, Figure 7.3 is set to a 12.5-cm maximum width; the complete cell-junction table starts on page 3. Figure 7.17 is set to 7.5 cm and its image/caption now fit on page 9. See `PASS2_DECISIONS.md` for editorial boundaries and exact requested wording.
- **Current result:** `.venv/bin/python check_pdf.py --strict 'notes/class 11/Ch7_StructuralOrganisationInAnimals'` reports **2 failures, 0 warnings**. Check 6: 117/143 figure-label strings fully matched in running text, 3 partial and 23 missing; the printed labels remain in the raster artwork. Check 7: the four approved omissions F007, F083, F113 and F355 remain unticked. The other eight checks pass, including 17/17 monochrome embedded images, A4 portrait geometry, and no orphaned headings. The strict linter exits 1; neither failure was masked or patched in the checker.
- This records automated print/bookkeeping results only. **All-page Pass 3(a), bidirectional Pass 3(b), a green final linter, rebuild equivalence, and Gate 3 remain pending.** Do not describe the revised chapter as Gate 2 closed or fully verified.

### Reproduction / validation

For this revision, the user requested using the closest local environment rather than `/vercel`. A repo-local `.venv` was created with Python 3.13.14, ReportLab 5.0.1, pdfplumber 0.11.10, PyMuPDF 1.28.2, and Pillow 12.3.0. The shared-template smoke test passed before the chapter build.

```bash
.venv/bin/python 'notes/class 11/Ch7_StructuralOrganisationInAnimals/Ch7_StructuralOrganisationInAnimals.py'
.venv/bin/python check_pdf.py --strict 'notes/class 11/Ch7_StructuralOrganisationInAnimals'
./.venv/bin/python 'notes/class 11/Ch7_StructuralOrganisationInAnimals/verify_gate1.py'
./.venv/bin/python 'notes/class 11/Ch7_StructuralOrganisationInAnimals/audit_figures.py'
```
