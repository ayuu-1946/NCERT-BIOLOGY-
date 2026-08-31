# Animal Kingdom — Figure Extraction Audit

## Method

The source PDF was inspected with 110 dpi coordinate grids and the figure rectangles were hand-pinned in PDF points. Crops were rendered at 300 dpi, converted with `Image.convert("L")`, and passed through `ImageOps.autocontrast(cutoff=1)`. This guarantees that emitted PNGs have one grayscale channel and avoids color-dependent print failures.

## Mechanical checks

The audit script `scratch/audit_ch4_figures.py` runs three complementary checks for every asset: (A) text-layer word grazing, (B) drawings-extent overflow, and (C) dark ink in a six-point border band. It also records emitted image mode and pixel dimensions. Some text-layer hits are intentional source labels or captions that overlap the crop boundary; they are not accepted blindly and must be checked against the asset contact sheet. Any remaining source watermark is a page artifact, not body-text bleed.

| Check | Requirement | Status |
|---|---|---|
| A | No accidental neighboring prose cut by a crop edge | Reviewed against source grids and flagged-asset contact sheet |
| B | No figure artwork clipped at crop edges | Reviewed; rectangles retain specimen/artwork extents |
| C | No unexplained dark edge ink | Reviewed; hits are either intentional artwork/labels or source-page artifacts |
| D | Every emitted PNG is true grayscale (`mode == L`) | Passed for all 26 assets |
| E | Labels and part markers remain visible | Visually reviewed using source grids and regenerated contact sheets |
| F | Excess whitespace controlled | Rectangles use compact approximately 10 pt clearance where layout permits |

## Visual review record

The full contact sheet is `scratch/ch4_assets_contact_final.png`; the focused review sheet is `scratch/ch4_flagged_contact_final.png`. The final asset set contains all numbered figure plates from 4.1 through 4.24, with multi-part plates preserved as grouped assets where that improves label visibility, plus the explicitly marked unnumbered Vertebrata chart. Captions are documented in the inventory rather than needlessly repeated inside the image assets.

## Reproducibility

Run from the repository root with `/vercel/share/neetenv/bin/python`:

```bash
/vercel/share/neetenv/bin/python 'notes/class 11/Ch4_AnimalKingdom/extract_figures.py'
/vercel/share/neetenv/bin/python scratch/audit_ch4_figures.py
```
