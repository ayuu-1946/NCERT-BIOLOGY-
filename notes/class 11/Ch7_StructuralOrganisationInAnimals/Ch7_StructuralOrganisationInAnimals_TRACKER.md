# Class 11 Chapter 7 — Structural Organisation in Animals Tracker

## Current status — 2026-09-26

**Gate 1 closed for the requested NEET syllabus scope; Pass 2 not started.** The Earthworm section has been removed from the NEET syllabus, so section 7.3 and directly related summary/exercise material are intentionally excluded from these artifacts. The resulting inventory is complete for the requested syllabus scope; this is a deliberate syllabus exclusion, not an accidental omission. No chapter notes script/PDF exists; all inventory rows are unticked.

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

### Reproduction / validation

The canonical `/vercel/share/neetenv` was missing, `uv` was unavailable, and `/vercel` was permission-denied. At the user's direction, tools ran in the ignored repo-local `.venv` (Python 3.11.2). From repository root:

```bash
./.venv/bin/python 'notes/class 11/Ch7_StructuralOrganisationInAnimals/verify_gate1.py'
./.venv/bin/python 'notes/class 11/Ch7_StructuralOrganisationInAnimals/audit_figures.py'
```
