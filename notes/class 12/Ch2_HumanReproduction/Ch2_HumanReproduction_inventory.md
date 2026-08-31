# Ch2 Human Reproduction — Figure Inventory

## Figure extraction status

**Source PDF:** `Chapter/class 12/Chapter 2 - Human Reproduction.pdf`
**Figure census:** 12 numbered source figures, represented by 14 assets because Figures 2.1 and 2.3 each contain two labeled source panels.
**Extraction status:** Complete for the figure-extraction scope. All 14 assets were freshly regenerated after the previous chapter work was deleted, rendered at 300 dpi, converted to true grayscale (`mode=L`) with autocontrast, and visually reviewed using the fresh 4× source grids and final contact sheet.
**Extraction script:** `extract_figures.py`
**Audit record:** `Ch2_figure_audit.md`

The source chapter contains 15 PDF pages. Figure-bearing artwork occurs on PDF pages 2–12. Page 1 contains references to Figure 2.1 but no figure artwork, so it is excluded from the asset census.

## Figure manifest

| Figure | Verbatim source caption | PDF page | Asset | Status |
|---|---|---:|---|---|
| 2.1a | Diagrammatic sectional view of male pelvis showing reproductive system | 2 | `assets/fig_2_1a.png` | Extracted, grayscale, visually verified |
| 2.1b | Diagrammatic view of male reproductive system (part of testis is open to show inner details) | 2 | `assets/fig_2_1b.png` | Extracted, grayscale, visually verified |
| 2.2 | Diagrammatic sectional view of seminiferous tubule | 3 | `assets/fig_2_2.png` | Extracted, grayscale, visually verified |
| 2.3a | Diagrammatic sectional view of female pelvis showing reproductive system | 4 | `assets/fig_2_3a.png` | Extracted, grayscale, visually verified |
| 2.3b | Diagrammatic sectional view of the female reproductive system | 4 | `assets/fig_2_3b.png` | Extracted, grayscale, visually verified |
| 2.4 | A diagrammatic sectional view of Mammary gland | 5 | `assets/fig_2_4.png` | Extracted, grayscale, visually verified |
| 2.5 | Diagrammatic sectional view of a seminiferous tubule (enlarged) | 6 | `assets/fig_2_5.png` | Extracted, grayscale, visually verified |
| 2.6 | Structure of a sperm | 7 | `assets/fig_2_6.png` | Extracted, grayscale, visually verified |
| 2.7 | Diagrammatic Section view of ovary | 8 | `assets/fig_2_7.png` | Extracted, grayscale, visually verified |
| 2.8 | Schematic representation of (a) Spermatogenesis; (b) Oogenesis | 8 | `assets/fig_2_8.png` | Extracted as one complete shared-annotation asset, grayscale, visually verified |
| 2.9 | Diagrammatic presentation of various events during a menstrual cycle | 9 | `assets/fig_2_9.png` | Extracted, grayscale, visually verified |
| 2.10 | Ovum surrounded by few sperms | 10 | `assets/fig_2_10.png` | Extracted, grayscale, visually verified |
| 2.11 | Transport of ovum, fertilisation and passage of growing embryo through fallopian tube | 11 | `assets/fig_2_11.png` | Extracted as one connected multi-stage asset, grayscale, visually verified |
| 2.12 | The human foetus within the uterus | 12 | `assets/fig_2_12.png` | Extracted, grayscale, visually verified |

## Figure-label matrix

The labels below were checked against the rendered figure assets during the fresh visual review. They are the in-figure labels that should be represented in the chapter’s running text or explicitly referenced in its figure discussion.

| Figure | In-figure labels verified in asset |
|---|---|
| 2.1a | Ureter; Seminal vesicle; Urinary bladder; Vas deferens; Prostate; Penis; Urethra; Glans penis; Foreskin; Testis; Scrotum; Ejaculatory duct; Rectum; Anus; Bulbourethral gland |
| 2.1b | Ureter; Vas deferens; Epididymis; Vasa efferentia; Rete testis; Testicular lobules; Glans penis; Foreskin; Urinary bladder; Seminal vesicle; Prostate; Bulbourethral gland; Urethra; Testis |
| 2.2 | Interstitial cells; Spermatogonia; Spermatozoa; Sertoli cells |
| 2.3a | Uterus; Urinary Bladder; Pubic symphysis; Urethra; Clitoris; Labium minora; Labium majora; Vaginal orifice; Cervix; Rectum; Vagina; Anus |
| 2.3b | Uterine fundus; Uterine cavity; Endometrium; Myometrium; Perimetrium; Isthmus; Ampulla; Infundibulum; Fallopian tube; Ovary; Fimbriae; Cervix; Cervical canal; Vagina |
| 2.4 | Mammary lobe; Mammary alveolus; Mammary duct; Ampulla; Lactiferous duct; Nipple; Areola; Fat; Rib; Muscles between ribs; Pectoralis major muscle |
| 2.5 | Spermatozoa; Spermatid; Secondary spermatocyte; Primary spermatocyte; Sertoli cell; Spermatogonium |
| 2.6 | Plasma membrane; Acrosome; Nucleus containing chromosomal material; Head; Neck; Middle piece; Mitochondria (energy source for swimming); Tail |
| 2.7 | Blood vessels; Primary follicle; Tertiary follicle Showing antrum; Graafian follicle; Secondary oocyte; Corpus luteum |
| 2.8 | Spermatogonia; Mitosis differentiation; Primary spermatocytes; 1st meiotic division; Secondary spermatocytes; 2nd meiotic division; Spermatids; Differentiation; Spermatozoa; CHROMOSOME NUMBER PER CELL; 46; 23; Oogonia; Fetal life; Birth; Childhood; Puberty; Adult reproductive life; Primary oocyte; 1st meiotic division (completed prior to ovulation); Secondary oocyte; First polar body; Second polar body; Ovum |
| 2.9 | Pituitary hormone levels; FSH; LH; Ovarian events; Developing follicle; Mature follicle; Developing corpus luteum; Regressing corpus luteum; Ovulation; Ovarian hormone levels; Estrogen; Progesterone; Uterine events; Menses; Days; Menstruation; Follicular phase (Proliferative phase); Luteal phase (Secretory phase); Next cycle begins |
| 2.10 | Sperm; Zona pellucida; Ovum; Cells of the corona radiata; Perivitelline space |
| 2.11 | Morula; Blastocyst; Implantation |
| 2.12 | Placental villi; Umbilical cord with its vessels; Cavity of uterus; Yolk sac; Embryo; Plug of mucus in cervix |

## Crop and audit notes

The rectangles in `extract_figures.py` were freshly checked against the canonical 4× grid overlays in `scratch/ch2_figs/grid_4x/`. Captions and page-number furniture were excluded wherever the source layout allowed. Figures 2.1 and 2.3 were split into their separately labeled `(a)` and `(b)` panels. Figures 2.8 and 2.11 remain complete single assets because their panels or stages share central annotations and connected artwork.

Some source pages place vector labels beside or over the prose columns, so the text-layer check can report zero words or grazing for otherwise correct artwork. The final audit records these source-layout exceptions explicitly; visual review, drawing extent checks, and border-band checks were also completed.

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

## Tight-crop revision

At the user’s request, Figures 2.8, 2.12, 2.1a, 2.3b, 2.3a, 2.11, and 2.1b were tightened to approximately 10 pt padding around meaningful printed ink. Figure 2.8 appeared twice in the request and was processed once. Figure 2.1a received an additional left-edge cleanup to remove adjacent prose while retaining every anatomical label.
