# Class 11 Chapter 7 — Pass 2 decisions

Status: the current 16-page Pass 2 PDF builds successfully, but the strict linter is not green: check 6 fails after the earlier requested removal of figure-label transcription boxes, and check 7 flags four rows explicitly approved for removal in the latest prose revision. Gate 3 pending. This record explains the current script and PDF, not a completed visual/content audit.

## Input and scope

- Frozen source of truth for coverage: `Ch7_StructuralOrganisationInAnimals_inventory.md` (F001–F398; 398 rows). Source PDF: `Chapter/class 11/Chapter 07 - Structural Organisation in Animals.pdf` (19 supplied pages; printed pages 100–106 and 111–122).
- Under the approved NEET scope, section 7.3 Earthworm and directly related summary/exercise entries are excluded. Printed pages 107–110 and figures 7.9–7.13 are absent from the supplied edition; no other edition was substituted. The retained sections run intro → 7.1 → 7.2 → 7.4 → 7.5. Earlier pre-filter introduction removals (transition and rhetorical question) and the retained human-cell-count fact are recorded in the tracker.
- The source summary calls adipose tissue specialised connective tissue, while the body places it under loose connective tissue. Both descriptions are retained with that attribution in the 7.1.2 block; do not silently harmonise them in a later pass.

## Script structure and editorial choices

- `Ch7_StructuralOrganisationInAnimals.py` imports `neet_template.py`; its `# ---- 7.x ----` comments identify the blocks for later edits. The PDF is generated alongside it as `Ch7_StructuralOrganisationInAnimals.pdf`.
- The 14 SUMMARY-UNIQUE rows F368–F381 are inserted in their inventory-assigned body locations (marked `[FOLD Fxxx]` in the script) and represented in the Quick Recap. The inventory's Summary classification table gives the individual sentence-to-section mappings.
- Comparative statements are arranged as tables (epithelial subtypes, glands, junctions, muscle types); ordered anatomical routes are presented as process flows (including the cockroach alimentary canal and frog digestion). This changes presentation, not the planned fact inventory. An appendix answers only the four GAP exercise subparts: 7(b), 9(e), 10(e), 11(e). These explanations supply terms missing from the retained chapter prose, so do not attribute them to the supplied NCERT body. The remaining 25 subparts are classified COVERED in the inventory; no separate answers are added for them.
- Typhlosole is defined solely to answer the retained 11(e) exercise gap; its appearance does not restore the out-of-syllabus Earthworm section. Protonema is likewise an exercise term, not a new chapter section.
- The 17 retained assets (7.1–7.8, 7.14–7.22) remain embedded at their relevant sections. By user request, all 17 figure-label transcription NOTE boxes were removed, including the Figure 7.20 box; the original labels remain printed in the figure artwork. Figures 7.16/7.17 and 7.21/7.22 each share a two-column row with their own captions, using direct helper contents because nesting `KeepTogether` inside a table cell yields an infinite row height in ReportLab. The final 15-page PDF's Figure 7.16/7.17 row was inspected at 1.5x render size; full-page Pass 3(a) inspection remains pending.
- The source's quarter-inch fraction is set as ASCII `1/4 inches` to avoid the banned fraction glyph. No script-level style or font constants were introduced.
- For the requested page flow, Figure 7.3 uses a 520-dpi vector crop and 12.5-cm maximum display width, placing the full cell-junction table at the start of the next page. Figures 7.16 and 7.17 now share one horizontal, captioned row at a 6.9-cm maximum width each; both fit on page 9. Both placements were visually checked; other figure sizes are unchanged.

## User-requested prose edits (2026-09-26)

Applied in `Ch7_StructuralOrganisationInAnimals.py` and rebuilt the PDF:

- Removed opener F355 so body text starts with “In unicellular organisms…”.
- Removed F007, the redundant four-basic-tissue-types sentence; the 7.1 opening sentence still states that tissues are broadly classified into four types.
- Removed F083; the blood paragraph now ends with its transport sentence.
- Reframed F111–F112 as: “The complexity in organ and organ systems shows a discernable trend, called the evolutionary trend (details in class XII).”
- Removed F113, the redundant preview of the worked examples; the following NOTE naming Cockroach and Frog remains.
- Removed “(learn more in Chapter 20)” after “Voluntary”.
- Removed “(details in Chapter 21)” from the neuron sentence.
- Reframed F214–F216 as: “Frogs change colour on grasses and dry land to hide from predators (camouflage); this protective coloration is called mimicry.” The following summer/winter shelter sentence remains.
- Kept that following frog sleep bullet together in the layout so its final word is not stranded at the top of the next page.

The inventory preserves the frozen 398-row numbering and leaves F007, F083, F113, and F355 unticked to record the approved omissions; the other 394 rows remain ticked.

## Validation boundary

On 2026-09-26, the latest 16-page PDF was rebuilt using a repo-local Python 3.13 environment (ReportLab 5.0.1, pdfplumber 0.11.10, PyMuPDF 1.28.2, Pillow 12.3.0) after the required shared-template smoke test. Text checks confirmed all eight requested edits. `check_pdf.py --strict` reports **2 fails, 0 warnings**: check 6 finds 117/143 figure-label strings fully in extracted running text, 3 partial, and 23 missing (unchanged from removal of transcription boxes); check 7 finds F007, F083, F113, and F355 intentionally unticked per the latest user-approved removals. The other eight checks pass, including monochrome images 17/17 and A4 geometry. No checker change or exemption has been applied. Gate 3 still requires direct inspection of every rendered page, a full bidirectional source/script read, resolution or explicit acceptance of the gate findings, and rebuild equivalence.

Rebuild and lint from the repository root:

```bash
.venv/bin/python 'notes/class 11/Ch7_StructuralOrganisationInAnimals/Ch7_StructuralOrganisationInAnimals.py'
.venv/bin/python check_pdf.py --strict 'notes/class 11/Ch7_StructuralOrganisationInAnimals'
```

For this revision, the repo-local `.venv` was created with Python 3.13 and the versions listed above, at the user's direction to use the closest local environment rather than `/vercel`. No full Pass 3 verification is recorded in this file.
