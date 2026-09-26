# Class 11 Chapter 7 — Pass 2 decisions

Status: the prior Pass 2 PDF passed Gate 2; the user-requested revision does not pass the strict linter (check 6 fails). Gate 3 pending. This record explains the current script and PDF, not a completed visual/content audit.

## Input and scope

- Frozen source of truth for coverage: `Ch7_StructuralOrganisationInAnimals_inventory.md` (F001–F398; 398 rows). Source PDF: `Chapter/class 11/Chapter 07 - Structural Organisation in Animals.pdf` (19 supplied pages; printed pages 100–106 and 111–122).
- Under the approved NEET scope, section 7.3 Earthworm and directly related summary/exercise entries are excluded. Printed pages 107–110 and figures 7.9–7.13 are absent from the supplied edition; no other edition was substituted. The retained sections run intro → 7.1 → 7.2 → 7.4 → 7.5. The pre-filter introduction removals (transition and rhetorical question) and retained human-cell-count fact are recorded in the tracker.
- The source summary calls adipose tissue specialised connective tissue, while the body places it under loose connective tissue. Both descriptions are retained with that attribution in the 7.1.2 block; do not silently harmonise them in a later pass.

## Script structure and editorial choices

- `Ch7_StructuralOrganisationInAnimals.py` imports `neet_template.py`; its `# ---- 7.x ----` comments identify the blocks for later edits. The PDF is generated alongside it as `Ch7_StructuralOrganisationInAnimals.pdf`.
- The 14 SUMMARY-UNIQUE rows F368–F381 are inserted in their inventory-assigned body locations (marked `[FOLD Fxxx]` in the script) and represented in the Quick Recap. The inventory's Summary classification table gives the individual sentence-to-section mappings.
- Comparative statements are arranged as tables (epithelial subtypes, glands, junctions, muscle types); ordered anatomical routes are presented as process flows (including the cockroach alimentary canal and frog digestion). This changes presentation, not the planned fact inventory. An appendix answers only the four GAP exercise subparts: 7(b), 9(e), 10(e), 11(e). These explanations supply terms missing from the retained chapter prose, so do not attribute them to the supplied NCERT body. The remaining 25 subparts are classified COVERED in the inventory; no separate answers are added for them.
- Typhlosole is defined solely to answer the retained 11(e) exercise gap; its appearance does not restore the out-of-syllabus Earthworm section. Protonema is likewise an exercise term, not a new chapter section.
- The 17 retained assets (7.1–7.8, 7.14–7.22) remain embedded at their relevant sections. By user request, all 17 figure-label transcription NOTE boxes were removed, including the Figure 7.20 box; the original labels remain printed in the figure artwork. This deliberately breaks text-extraction-based figure-label check 6. Figures 7.21 (male) and 7.22 (female) now share a two-column row with their own captions; each calls the shared `figure()` helper with `max_width_cm=6.9` to fit a half-column. The helper's framed image and caption are placed directly in table cells because nesting its `KeepTogether` wrapper yields an infinite row height in ReportLab. The new side-by-side PDF page was inspected at 1.5x render size; full-page Pass 3(a) inspection remains pending.
- The source's quarter-inch fraction is set as ASCII `1/4 inches` to avoid the banned fraction glyph. No script-level style or font constants were introduced.

## Validation boundary

On 2026-09-26, the **earlier 17-page version** passed all checks (0 fail, 0 warn; 143/143 figure labels in running text). Following the requested label-box removal and two-column arrangement, the **current 16-page PDF** fails `check_pdf.py --strict` with **1 fail (check 6), 0 warn**: 117/143 figure-label strings fully matched in running text, 3 partial and 23 missing. The other nine checks pass, including monochrome images 17/17 and ticked rows 398/398. This is an intentional presentation change but a real unresolved failure against the existing Gate 2 contract; no exemption or checker modification has been applied. The label words remain visible in the raster figures. Gate 3 still requires direct inspection of every rendered page, a full bidirectional source/script read, a green final linter, zero confirmed defects, and rebuild equivalence.

Rebuild and lint:

```bash
/vercel/share/neetenv/bin/python 'notes/class 11/Ch7_StructuralOrganisationInAnimals/Ch7_StructuralOrganisationInAnimals.py'
/vercel/share/neetenv/bin/python check_pdf.py --strict 'notes/class 11/Ch7_StructuralOrganisationInAnimals'
```

If the canonical environment is absent after a sandbox reset, follow §1 of `GATE_2_PASS_2_BUILD_AND_LINT.md` before rebuilding. No Pass 3 verification is recorded in this file.
