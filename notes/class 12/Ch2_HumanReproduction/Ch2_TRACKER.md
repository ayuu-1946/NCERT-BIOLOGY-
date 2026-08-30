# Ch2 Human Reproduction — Figure Extraction Tracker

## Current status

**Previous chapter-specific extraction work:** Deleted as requested.  
**Fresh figure extraction:** Complete for the extraction-only scope.  
**Figure census:** 12 numbered figures represented by 14 assets; Figures 2.1 and 2.3 are split into labeled `(a)` and `(b)` assets.  
**Assets:** 14/14 present, all freshly regenerated from the source PDF and converted to `mode=L`.  
**Visual review:** Fresh 4× grid inspection and final contact-sheet review completed; correction-sensitive assets were individually checked.  
**Full replacement chapter/PDF gate:** Not started; no chapter notes PDF was requested or generated.

## Re-pin and replacement record

The former `notes/class 12/Ch2_HumanReproduction/` directory and related Human Reproduction scratch artifacts were deleted before rebuilding. The source PDF was not modified. Rectangles were then re-established from fresh 4× grid overlays. The new extraction removed caption, prose, and page-number remnants identified during review, retained connected multi-panel figures 2.8 and 2.11 as complete assets, and preserved all documented in-figure labels.

## Deliverables

The chapter folder contains the reproducible extraction script, the frozen inventory with the per-figure label matrix, the detailed audit, and 14 grayscale PNG assets under `assets/`. The raw source census, 4× grid overlays, extraction output, and audit output remain in `scratch/` during this session for re-audit.

## Reproduction commands

From the repository root:

```bash
/vercel/share/neetenv/bin/python 'notes/class 12/Ch2_HumanReproduction/extract_figures.py'
/vercel/share/neetenv/bin/python scratch/audit_human_reproduction_figures.py
```

## References

[1]: `../../../../Chapter/class 12/Chapter 2 - Human Reproduction.pdf` "NCERT Biology, Class 12, Chapter 2: Human Reproduction"
[2]: `../../../../SUPREME COMMAND PROMPT.md` "Repository SUPREME COMMAND prompt"
[3]: `../../../../skills/ncert-figure-extraction/SKILL.md` "ncert-figure-extraction workflow"
