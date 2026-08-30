# Ch2 Human Reproduction — Figure Extraction Audit

## Scope and method

This audit covers the 14 PNG assets extracted from the 12 numbered figures in the current Class 12 NCERT source PDF. Figures 2.1 and 2.3 are represented by separate `(a)` and `(b)` assets. Figures 2.8 and 2.11 remain complete single assets because their panels or stages share central annotations and connected artwork.

Every asset was freshly regenerated after the previous Human Reproduction work was deleted. Each crop was rendered at 300 dpi and converted to true grayscale with Pillow `convert('L')` followed by autocontrast. The mandatory audit checked text-layer grazing, vector-drawing overflow, and unexplained dark ink in the six-point border band. The raw final output is retained at `scratch/ch2_figs/audit_results.txt`.

## Mechanical audit summary

| Area | Result |
|---|---|
| Assets regenerated | 14/14 |
| Text-layer audit | Clean for prose/caption exclusion; vector-label figures may report zero words; Figure 2.8’s `(a)` and `(b)` markers are intentional in-figure labels |
| Drawing-extent audit | Clean or explicitly explained for source-PDF vector tails and shared artwork boundaries; no visually meaningful label or panel was clipped |
| Border-band ink audit | Clean or attributable to source page furniture/watermark adjacent to the intended crop |
| Monochrome check | 14/14 assets report `mode=L` |
| Visual review | Complete contact-sheet review plus individual checks of correction-sensitive assets |
| Source modification | None; the source PDF remains in place and unchanged |

The source PDF contains faint publisher watermark/page-furniture vectors. These can appear in mechanical border-band or drawing-extent checks even when they are outside the meaningful figure artwork. Such cases are retained as documented source-layout exceptions rather than hidden by raising thresholds.

## Final visual-review findings

The final contact sheet shows complete, correctly oriented assets for the male and female reproductive systems, seminiferous tubules, mammary gland, sperm, ovary, gametogenesis, menstrual cycle, fertilisation, embryo transport, and foetal development. The correction-sensitive assets were individually opened from fresh copies: Figure 2.7 has all ovary structures and labels with the caption removed; Figure 2.12 retains the umbilical-cord label and uterine diagram while removing the prose and page-number block; Figure 2.10 retains the sperm/ovum labels and excludes the caption; and Figure 2.11 preserves the connected multi-stage sequence.

## Re-pin history

| Asset | Final adjustment | Reason |
|---|---|---|
| `fig_2_1a.png` | Left edge tightened after visual and text-layer review | Removed the neighboring prose column while retaining the male-pelvis labels. |
| `fig_2_7.png` | Top and bottom tightened | Removed page-furniture and caption remnants. |
| `fig_2_10.png` | Top/right boundaries tightened | Removed prose and page-number furniture while retaining the complete ovum/sperm diagram. |
| `fig_2_11.png` | Left/top/bottom boundaries tightened | Removed page furniture while preserving all connected stages and implantation artwork. |
| `fig_2_12.png` | Top/right boundaries tightened | Removed prose and page-number furniture while retaining the umbilical-cord leader label and uterus diagram. |

## Reproducibility

Run from the repository root:

```bash
/vercel/share/neetenv/bin/python 'notes/class 12/Ch2_HumanReproduction/extract_figures.py'
/vercel/share/neetenv/bin/python scratch/audit_human_reproduction_figures.py
```

## References

[1]: `../../../../Chapter/class 12/Chapter 2 - Human Reproduction.pdf` "NCERT Biology, Class 12, Chapter 2: Human Reproduction"
[2]: `../../../../SUPREME COMMAND PROMPT.md` "Repository SUPREME COMMAND prompt"
[3]: `../../../../skills/ncert-figure-extraction/SKILL.md` "ncert-figure-extraction workflow"
