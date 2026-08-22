# Gate 3b — findings, BOTH directions, all 646 frozen rows

Inventory is FROZEN at `F001..F646`: findings are FLAGGED here and registered in the
inventory's Gate 3b defect register. **No Facts row was added, removed or reworded.**
Where a finding was a genuine fact loss in the *deliverable*, the **script** was fixed
(the freeze binds the inventory, not the PDF) and the fix is named below.

---

# DIRECTION 1 — every inventory row traced to the NCERT SOURCE

Two methods, because the rows are of two kinds.

## D1 part A — the 510 prose/heading/opener/question/table rows (machine + eye)

`scratch/ch5_3b/trace_d1.py` — puts the **source** on one side (Gate 2's tick audit had
our own PDF on *both* sides and structurally could not catch a Pass-1 mis-transcription).

    rows: 646   EXACT 495   MISS 151
    MISS = 136 figure-label (part B, below) + 15 prose rows

All **15** residual MISS rows were eye-read against their cited source page. **All 15 are
extraction artefacts, none is drift:**

| Cause | Rows |
|---|---|
| A figure caption is interleaved into the sentence by the text layer | `F029` `F048` `F219` `F227` `F406` `F467` |
| Superscript flattened (`10-9` in the layer vs `10^-9` written, per check 5) | `F048` `F057` `F251` `F426` |
| Symbol-font glyph transliterated by doctrine (`φx174`→`phi x 174`, `σ/ρ`→`sigma/rho`) | `F016` `F223` |
| Quote/paren/spacing only (`''`→`'`, `polyploidy(a` → `polyploidy (a`) | `F146` `F185` `F199` `F302` |

**Part A verdict: CLEAN.** 495 verbatim + 15 explained = 510/510.

## D1 part B — the 136 figure-label rows (visual, the only possible method)

In-figure labels are **vector artwork**: `page.get_text("words")` returns *zero* words
inside most figure rects, so the only way to check them is to render the source rect and
read it. Every one of the **15 label-bearing figures** was rendered at 300 dpi (+8pt
margin) from the SOURCE pdf and read label-by-label against its rows.

| Figure | rows | verdict |
|---|---|---|
| Fig 5.1 | `F511`-`F516` (6) | CONFIRMED |
| Fig 5.2 | `F517`-`F523` (7) | CONFIRMED — 5′, 3′, hydrogen bonds, A, T, G, C all printed |
| Fig 5.3 | `F524`-`F533` (10) | **DEFECT — D1-1 / D1-2** (6 confirmed, 4 mis-attributed) |
| Fig 5.4a | `F534`-`F537` (4) | CONFIRMED |
| Fig 5.5 | `F538`-`F547` (10) | CONFIRMED (source capitalises "No Radioactive"; immaterial) |
| Fig 5.6 | `F548`-`F553` (6) | CONFIRMED |
| Fig 5.7 | `F554`-`F564` (11) | CONFIRMED — incl. the parenthesised "(Separation of DNA by Centrifugation)" |
| Fig 5.8 | `F565`-`F570` (6) | CONFIRMED |
| Fig 5.9 | `F571`-`F578` (8) | CONFIRMED |
| Fig 5.10 | `F579`-`F590` (12) | CONFIRMED |
| Fig 5.11 | `F591`-`F601` (11) | CONFIRMED |
| Fig 5.12 | `F602`-`F610` (9) | **DEFECT — D1-4** (8 confirmed, 1 phantom) |
| Fig 5.13 | `F611`-`F623` (13) | CONFIRMED |
| Fig 5.14 | `F624`-`F636` (13) | CONFIRMED (source sets "operator region(o)" unspaced; immaterial) |
| Fig 5.16 | `F637`-`F646` (10) | CONFIRMED |

136 rows, **15 figures**, 4 defects (D1-1..D1-4). `5.4b` and `5.15` are genuinely label-free.

### D1-1 — Fig 5.3's rows include four labels belonging to a different plate

Fig 5.3 (p4, DNA double helix) prints exactly **six** labels — Base pairs, Adenine,
Thymine, Guanine, Cytosine, Sugar phosphate backbone = `F524`-`F529`, all CONFIRMED.

`F530` "Central dogma", `F531` "DNA", `F532` "RNA", `F533` "Protein" are **not on Fig 5.3's
artwork at all.** They belong to the **unnumbered central-dogma plate** lower on p4
(shipped as `fig_5_central_dogma.png`). `1-F` had no figure number to file them under and
parked them on the nearest numbered figure. Consequence: the inventory's own "Fig 5.3: 10
labels" is wrong, and the unnumbered plate reads as having zero label rows when it has four.
**Section-attribution defect, not a content loss.** Same root cause as the already-closed
`fig_5_3` caption mislabel — the plate had nowhere to go.

### D1-2 — `F532` "RNA" is a wording drift; the plate prints "mRNA"

The plate prints verbatim: `replication`, `DNA`, `transcription`, `mRNA`, `translation`,
`protein`, `Central dogma`. `F532` says **RNA**; the source says **mRNA**. Real drift and
exam-relevant — that the middle term of the central dogma is specifically mRNA is the
point. (`F533` "Protein" vs printed lowercase `protein`: immaterial.)

### D1-3 — three plate labels have no inventory row anywhere

`replication`, `transcription`, `translation` are printed labels on that plate with **no**
`figure-label` row in `F511`-`F646`. Uninventoried figure content (Direction-2 class).

**Script fix for D1-2 + D1-3:** the central-dogma caption now names all six printed plate
labels, so every printed label is in running text and the middle term reads `mRNA`.

### D1-4 — `F606` "anticodon loop" is a phantom label

Fig 5.12 prints **Anticodon** (`F605`), never "anticodon loop". Machine-confirmed rather
than eyeballed: the fig 5.12 rect contains **zero** text-layer words, the only `anticodon`
word on p20 sits **outside** the rect at (436,299), and the exact string "anticodon loop"
occurs once chapter-wide — in **body prose** on p20 ("tRNA has an anticodon loop that has
bases complementary to the code"). So the fact is real and correctly in the PDF; it is
**typed as a figure-label row when it is a prose fact.** No content loss.

### Observations, deliberately NOT raised as defects

- Fig 5.7's `15N/14N` tube-band annotations, Fig 5.11's `m7G` cap chemistry, Fig 5.14's
  operon letter boxes (`p i p o z y a`), Fig 5.16's gel lane letters (`C A B`) and its
  0-12 repeat scale are printed but carry no label row. Each is either chemical shorthand
  or a symbol whose meaning is already carried by a prose row. Recording them as label
  rows would inflate the matrix without adding a fact.
- `F223` writes `sigma`/`rho` where the source prints `σ`/`ρ`. Required by check 5 (banned
  Unicode Greek), so it is correct authoring, not drift.

---

# DIRECTION 2 — every source sentence checked for UNINVENTORIED facts

Direction 1 can be 100% green while a whole source paragraph is missing, because nothing
in it ever looks at a sentence no row cites. Three **structurally independent** sweeps were
run so that one sweep's blind spot is another's target; then the survivors were eye-read.

## Sweep 1 — sentence coverage (`scratch/ch5_3b_d2/trace_d2.py`)

    sentences scored: 962   covered 941   suspect 21

Two signals per sentence (best difflib ratio against any candidate row **and** content-token
coverage against the whole inventory), suspect only if **both** fail — one signal alone
yields a list too long to actually eye-read, which is how this step gets skipped.

All 21 suspects eye-read. **19 are SUMMARY (p29-30) rephrasings** of body facts already
inventoried — expected, and consistent with `1-Z`'s classification of the Summary as
29 BODY-PRESENT + 4 SUMMARY-UNIQUE (`F507`-`F510`). **1 is a caption-splice artefact** on p5
("both the amino acid residues carry positive charges" + the Fig 5.4b caption spliced
mid-sentence; the fact itself is inventoried). **1 is a real gap — D2-1.**

## Sweep 2 — atom sweep (`scratch/ch5_3b_d2/trace_d2b.py`)

Sweep 1's structural blind spot: a sentence whose whole fact was dropped but whose
*vocabulary* repeats elsewhere scores high on token coverage and never surfaces. So this
sweep ignores sentences and checks the two atom classes heaviest in NEET marking and least
likely to be coincidentally present.

    distinct numbers in source: 93    absent from inventory: 7
    distinct proper nouns in source: 159   absent from inventory: 0

All **7** absent numbers were located in context and are **NCERT folio page numbers**
(83, 88, 89, 98, 101, 102, and `110033` = folio 103 with each digit doubled by the
two-column overlay) spliced mid-sentence by the extractor. **Zero content numbers and zero
proper nouns are missing.**

## Sweep 3 — per-page density + eye read of the thinnest pages

D1 EXACT hits per source page flagged four thin pages: p4 (5), p29 (1), p30 (5), p16 (6).
p29/p30 are the Summary and Fig 5.16's caption; p4 is almost entirely artwork. **p16 was
eye-read in full against the inventory** — all nine of its sentences trace to
`F220`-`F226`/`F231`, so its low count is a **hit-attribution artefact** (a sentence
straddling a page break is credited to the earlier page), not a gap.

### D2-1 — Fig 5.16's caption prose is uninventoried, and its conclusion was missing from the PDF

NCERT's Fig 5.16 caption (p29) is four substantive sentences, and **no `F###` row covers
any of them** — captions live in the figure manifest, which records only the short title.
Checked against the built PDF one statement at a time:

| Caption statement | in built PDF? |
|---|---|
| few representative chromosomes shown with different VNTR copy number | yes |
| different colour schemes used to trace each band's origin | n/a — a print-artifact note, void in a mono replacement |
| **the two alleles (paternal and maternal) of a chromosome also contain different copy numbers of VNTR** | yes, as "Repeats on the Paternal chromosome and the Maternal chromosome ... differ in the Number of short tandem repeats" |
| **the banding pattern of crime-scene DNA matches individual B, and not A** | **NO — absent entirely.** The PDF said only "can be compared band for band" |

The last row is a **genuine fact loss** and the highest-severity finding of Gate 3b: it is
the conclusion the whole figure exists to deliver, and exactly the figure-interpretation
NEET asks. **Script fixed** — the Fig 5.16 caption now carries both statements verbatim in
substance; page 28 re-rendered at 130 dpi and re-read, caption still fits its page.

## Direction 2 verdict

962 sentences, 93 numbers, 159 proper nouns and 31 source pages swept three ways:
**one** uninventoried fact with exam weight (D2-1), now in the deliverable. No dropped
paragraph, no missing number, no missing name.

---

# Post-fix verification

    /vercel/share/neetenv/bin/python check_pdf.py "notes/class 12/Ch5_MolecularBasisOfInheritance" --strict
    VERDICT: PASS  (0 fail, 0 warn)   exit 0
    30 pages · 646/646 ticked · 136/136 labels · 17 mono images · smallest text 6.0pt

Identical on every metric to the pre-fix Gate 3a run, so the two caption edits regressed
nothing.

# Open for OWNER DECISION (frozen inventory — cannot be fixed here)

| id | what | severity | proposed |
|---|---|---|---|
| D1-1 | `F530`-`F533` filed under Fig 5.3; belong to the unnumbered central-dogma plate | low (attribution) | re-section to `Fig 5.central_dogma` at the next unfreeze |
| D1-2 | `F532` says "RNA"; plate prints "mRNA" | **medium (wording drift)** | reword to `mRNA`; PDF already says mRNA |
| D1-3 | plate labels `replication`/`transcription`/`translation` have no row | low | add 3 label rows at the next unfreeze; PDF already names them |
| D1-4 | `F606` "anticodon loop" typed `figure-label`; it is p20 body prose | low (type) | retype to `concept`, keep the fact |
| D2-1 | Fig 5.16 caption prose has no row (fact now in PDF) | medium | add caption-prose rows at the next unfreeze |

None blocks Gate 3: every one is either an inventory-bookkeeping defect with the fact
correctly in the deliverable, or (D2-1) a fact loss that has been fixed in the deliverable.
