# Class 11 Chapter 7 — Pass 2 decisions

Status: Gate 2 closed (strict linter: 0 failures, 0 warnings); Gate 3 pending. This record explains the Pass 2 script and PDF, not a completed visual/content audit.

## Input and scope

- Frozen source of truth for coverage: `Ch7_StructuralOrganisationInAnimals_inventory.md` (F001–F398; 398 rows). Source PDF: `Chapter/class 11/Chapter 07 - Structural Organisation in Animals.pdf` (19 supplied pages; printed pages 100–106 and 111–122).
- Under the approved NEET scope, section 7.3 Earthworm and directly related summary/exercise entries are excluded. Printed pages 107–110 and figures 7.9–7.13 are absent from the supplied edition; no other edition was substituted. The retained sections run intro → 7.1 → 7.2 → 7.4 → 7.5. The pre-filter introduction removals (transition and rhetorical question) and retained human-cell-count fact are recorded in the tracker.
- The source summary calls adipose tissue specialised connective tissue, while the body places it under loose connective tissue. Both descriptions are retained with that attribution in the 7.1.2 block; do not silently harmonise them in a later pass.

## Script structure and editorial choices

- `Ch7_StructuralOrganisationInAnimals.py` imports `neet_template.py`; its `# ---- 7.x ----` comments identify the blocks for later edits. The PDF is generated alongside it as `Ch7_StructuralOrganisationInAnimals.pdf`.
- The 14 SUMMARY-UNIQUE rows F368–F381 are inserted in their inventory-assigned body locations (marked `[FOLD Fxxx]` in the script) and represented in the Quick Recap. The inventory's Summary classification table gives the individual sentence-to-section mappings.
- Comparative statements are arranged as tables (epithelial subtypes, glands, junctions, muscle types); ordered anatomical routes are presented as process flows (including the cockroach alimentary canal and frog digestion). This changes presentation, not the planned fact inventory. An appendix answers only the four GAP exercise subparts: 7(b), 9(e), 10(e), 11(e). These explanations supply terms missing from the retained chapter prose, so do not attribute them to the supplied NCERT body. The remaining 25 subparts are classified COVERED in the inventory; no separate answers are added for them.
- Typhlosole is defined solely to answer the retained 11(e) exercise gap; its appearance does not restore the out-of-syllabus Earthworm section. Protonema is likewise an exercise term, not a new chapter section.
- The 17 retained assets (7.1–7.8, 7.14–7.22) are embedded at their relevant sections using the shared `figure()` helper. **No figure-width override** (`max_width_cm`) was passed at any call site, so no before/after resizing deviation is claimed. Each image has an adjacent NOTE giving its labels as PDF text: 143/143 figure-label strings match the inventory matrix in the linter. A matching text label is not proof that the image itself has been visually checked at final print size; that remains for Pass 3(a).
- The source's quarter-inch fraction is set as ASCII `1/4 inches` to avoid the banned fraction glyph. No script-level style or font constants were introduced.

## Validation boundary

On 2026-09-26, from the repository root, `/vercel/share/neetenv/bin/python check_pdf.py --strict "notes/class 11/Ch7_StructuralOrganisationInAnimals"` reported **PASS (0 fail, 0 warn)** on the 17-page A4 PDF. Checks 1–10 passed: monochrome images 17/17, figure-label text 143/143, ticked rows 398/398, and no orphaned headings. Check 4 is a true negative (no portrait in the manifest). Neither the ticks nor the linter prove semantic completeness, accuracy of exercise answers, diagram readability, or final delivery. Gate 3 requires direct inspection of every rendered page, a full bidirectional source/script read with per-section evidence, a still-green final linter, zero confirmed defects, and rebuild equivalence.

Rebuild and lint:

```bash
/vercel/share/neetenv/bin/python 'notes/class 11/Ch7_StructuralOrganisationInAnimals/Ch7_StructuralOrganisationInAnimals.py'
/vercel/share/neetenv/bin/python check_pdf.py --strict 'notes/class 11/Ch7_StructuralOrganisationInAnimals'
```

If the canonical environment is absent after a sandbox reset, follow §1 of `GATE_2_PASS_2_BUILD_AND_LINT.md` before rebuilding. No Pass 3 verification is recorded in this file.
