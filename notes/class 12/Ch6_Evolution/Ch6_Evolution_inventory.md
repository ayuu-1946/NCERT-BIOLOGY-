# Working Inventory (NOT FROZEN) — Chapter 6: Evolution (Class XII)

**Status: PASS 1 SESSION `1-F` COMPLETE (2026-08-26). Sessions `1-S`, `1-H`, `1-O`, `1-Z`
NOT STARTED. GATE 1 OPEN. No script, no PDF.**

Source PDF: `Chapter/class 12/Chapter 6 - Evolution.pdf` (17 pages, page box 612 x 820.8)

This file currently documents **one** Pass 1 session — `1-F`, the figure session (§4.4 /
§6 Pass 1 step 6). It is deliberately **not** a freeze: there is no Facts table, no
heading census and no opener census yet, so the row IDs in the label matrix below are
`—` and are to be assigned by `1-Z` when it stitches the single contiguous `F###`
sequence. Nothing here may be read as "Gate 1 closed".

Tick legend: `x` = written into the script and verified present in the generated PDF.
**Every row below is deliberately unticked** — no script exists, so a tick would be
premature bookkeeping (the Ch7 lesson: ticks on 1-F rows feed `check_pdf.py` check 7 a
false green towards Gate 2, not Gate 1).

| Row block | Session | Count | IDs |
|---|---|---|---|
| Figure-label matrix (`Type: label`) | `1-F` | 13 | assigned by `1-Z` |
| **Total rows in this file** | | **13** | — |

Machine-derived by this session: **11 numbered NCERT figures → 13 asset files**, all
`mode=L`, **116 quoted in-figure labels across 9 label-bearing assets**.

---

## Session log — Pass 1

| Session | Scope | State | Rows added |
|---|---|---|---|
| **1-S** | Source read + Facts inventory (steps 1, 2, 3) | **not started** | — |
| **1-H** | Structural census (heading sweep, step 4) | **not started** | — |
| **1-O** | Section-opener census (step 5) | **not started** | — |
| **1-F** | Figures: census, rect pinning, extraction, raster audit, label matrix (step 6) | **complete** (2026-08-26) | 13 matrix rows (IDs by `1-Z`) |
| **1-Z** | Exercise-gap scan, summary classification, freeze, count derivation (steps 7-10) | **not started** | — |

Environment: `/vercel/share/neetenv` was **absent** at session start (the expected §0.2
state) and rebuilt before anything was diagnosed — `pymupdf 1.28.2`, `Pillow 12.3.0`,
`numpy 2.5.2` on CPython 3.13.11. Every command in this session ran through
`/vercel/share/neetenv/bin/python`.

---

## Figure manifest

11 numbered figures, 6.1-6.11, on artwork pages **3, 5, 6, 7, 8, 9, 11, 13, 14, 16**.
Figures 6.3 and 6.4 are each printed as two labelled sub-panels and get one asset each
per the skill's split rule, so the chapter ships **13** assets. Every asset is
single-channel greyscale (`PIL` mode `L`), verified mechanically this session.

**Captions are transcribed from rendered caption bands, not from the text layer** — this
chapter's PDF has no text layer at all (see the audit record). The strip render used for
the transcription is `scratch/ch6_doc/captions.png`.

| Fig # | Caption (verbatim) | Asset file | Src page | Mono | Opened |
|---|---|---|---|---|---|
| Figure 6.1 | Diagrammatic representation of Miller's experiment | `assets/fig_6_1.png` | 3 | yes (L) | yes |
| Figure 6.2 | A family tree of dinosaurs and their living modern day counterpart organisms like crocodiles and birds | `assets/fig_6_2.png` | 5 | yes (L) | yes |
| Figure 6.3 (a) | Example of homologous organs in (a) Plants and (b) Animals | `assets/fig_6_3a.png` | 6 | yes (L) | yes |
| Figure 6.3 (b) | Example of homologous organs in (a) Plants and (b) Animals | `assets/fig_6_3b.png` | 6 | yes (L) | yes |
| Figure 6.4 (a) | Figure showing white - winged moth and dark - winged moth (melanised) on a tree trunk (a) In unpolluted area (b) In polluted area | `assets/fig_6_4a.png` | 7 | yes (L) | yes |
| Figure 6.4 (b) | Figure showing white - winged moth and dark - winged moth (melanised) on a tree trunk (a) In unpolluted area (b) In polluted area | `assets/fig_6_4b.png` | 7 | yes (L) | yes |
| Figure 6.5 | Variety of beaks of finches that Darwin found in Galapagos Island | `assets/fig_6_5.png` | 8 | yes (L) | yes |
| Figure 6.6 | Adaptive radiation of marsupials of Australia | `assets/fig_6_6.png` | 8 | yes (L) | yes |
| Figure 6.7 | Picture showing convergent evolution of Australian Marsupials and placental mammals | `assets/fig_6_7.png` | 9 | yes (L) | yes |
| Figure 6.8 | Diagrammatic representation of the operation of natural selection on different traits : (a) Stabilising (b) Directional and (c) Disruptive | `assets/fig_6_8.png` | 11 | yes (L) | yes |
| Figure 6.9 | A sketch of the evolution of plant forms through geological periods | `assets/fig_6_9.png` | 13 | yes (L) | yes |
| Figure 6.10 | Representative evolutionary history of vertebrates through geological periods | `assets/fig_6_10.png` | 14 | yes (L) | yes |
| Figure 6.11 | A comparison of the skulls of adult modern human being, baby chimpanzee and adult chimpanzee. The skull of baby chimpanzee is more like adult human skull than adult chimpanzee skull | `assets/fig_6_11.png` | 16 | yes (L) | yes |

**Asset count reconciliation:** 11 numbered NCERT figures, two of which (6.3, 6.4) split
into `(a)`/`(b)` sub-panels → **13** asset files, **13** files on disk, **13** rects in
`extract_figures.py`, **13** rows in the label matrix. There is **no unnumbered bonus
plate** in this chapter (unlike Ch5's central-dogma schematic) — the census below was
taken from the page images, not from caption numbers, precisely to establish that. The
denominator is **13 assets / 11 figure numbers** everywhere it appears.

**Crop convention:** captions are **excluded** from every crop (the Ch5 convention — the
notes restate each caption in running text). Every rect's bottom edge stops short of its
caption band. Sub-panel letters `(a)`/`(b)`/`(c)` *are* inside their crops, because they
are the only thing distinguishing the two moth panels and the three selection panels.

**Figure 6.8 is deliberately ONE asset, not three.** Its (a)/(b)/(c) panels sit inside a
single rounded frame and the grey arrows *between* the panels carry the "one starting
distribution, three outcomes" meaning. Splitting it would satisfy the skill's sub-figure
rule while destroying the figure, so the rule is knowingly not applied here; NCERT also
numbers it as one figure with lettered panels, not as 6.8a/6.8b/6.8c.

### Figure census — pages swept, and everything deliberately excluded

All 17 pages were rendered and read (`scratch/ch6_doc/pages_census.png`). Ink-bearing
non-furniture regions occur on exactly the 10 artwork pages above. Everything else:

| Page | Region | Why excluded |
|---|---|---|
| 1 | Chapter-opener plate: QR code, "CHAPTER 6 / EVOLUTION" title, the §6.1-§6.9 contents list, and a tilted drop-shadowed thumbnail | Page furniture / title block. The thumbnail is a **re-print of fig 6.11's bottom row** (adult-chimpanzee skull + head) at reduced size, verified by rendering it (`scratch/ch6_doc/p1_head.png`); it carries no fact of its own. |
| 2, 4, 10, 12, 15 | prose only | No artwork. |
| 17 | SUMMARY box + EXERCISES | No artwork. |
| every page | dark header band (`EVOLUTION` / `BIOLOGY`), top-corner leaf/branch motif, right-margin decorative band, page-number tab, full-page "(c) NCERT / not to be republished" watermark | Furniture and watermark. These are what checks A'/B' below have to be told to ignore. |

**No scientist portrait exists in this chapter** — there is no Darwin headshot, no
"Do You Know?" portrait, nothing matching §5 item 3. The §4.4 photograph hard-no therefore
has no manifest row here, and `check_pdf.py` check 4 should have no portrait row to flag.
`fig_6_11` contains human/chimpanzee **line-art heads and skulls**, drawn illustrations
rather than photographs of a person, so it is not the banned class. Record this
adjudication now: Pass 2 must not "fix" `fig_6_11` by dropping it.

### Rects, as pinned by session `1-F`

Rects are in PDF points on a **612 x 820.8** page (not the usual 612 x 792 — every `y`
below lives on the taller page). Pinned by hand off a 20 pt coordinate grid
(`scratch/ch6_figs/grid/pNN.png`) and then re-measured against raster ink extents.
`extract_figures.py` carries a comment per rect recording *what* pinned it.

| Asset | Src page | Rect (pt) | Kind |
|---|---|---|---|
| `fig_6_1` | 3 | (226, 102, 519, 359) | scanned line diagram, labels both sides |
| `fig_6_2` | 5 | (89, 110, 540, 515) | full-width scanned plate |
| `fig_6_3a` | 6 | (272, 103, 522, 278) | plate **beside** a prose column |
| `fig_6_3b` | 6 | (272, 288, 535, 566) | plate **beside** a prose column |
| `fig_6_4a` | 7 | (76, 101, 310, 236) | raster photo panel |
| `fig_6_4b` | 7 | (316, 101, 550, 242) | raster photo panel |
| `fig_6_5` | 8 | (100, 101, 502, 188) | wide short strip, 4 beaks |
| `fig_6_6` | 8 | (65, 392, 504, 710) | radial plate |
| `fig_6_7` | 9 | (76, 100, 308, 550) | bordered table, **left** column, prose to its right |
| `fig_6_8` | 11 | (120, 268, 549, 686) | rounded-frame 3-panel figure |
| `fig_6_9` | 13 | (76, 102, 549, 508) | full-width chart |
| `fig_6_10` | 14 | (57, 99, 536, 604) | full-width chart |
| `fig_6_11` | 16 | (136, 102, 435, 516) | 3 x 2 illustration grid |

Figures 6.3(a), 6.3(b) and 6.7 sit **beside a body-text column**, which is the exact
failure mode this skill exists to prevent. Their prose-side edges are clipped against the
column gutter measured from the page raster (there is no text layer to read a boundary
from): p6 prose ends x~260 with the gutter at x=262-278, so both 6.3 rects start at
x=272; p9 prose starts x~320, so 6.7 stops at x=308.

---

## Figure-label matrix

Thirteen rows, one per asset. Rows for the four assets with no descriptive callouts are
worded so they do **not** begin `Figure labels`, because `check_pdf.py`'s
`_extract_labels` falls back to semicolon-splitting an unquoted body — a row reading
"Figure labels: (none)" would manufacture a phantom label no running text could satisfy.
The column header is worded the same way, for the same reason. The parser reads
**column index 3** of every pipe-delimited line, so this table's shape is load-bearing.

**This table must exist in exactly ONE place in this file.** When `1-Z` freezes the
inventory it must *move* these rows into the single `## Facts` table and assign IDs — not
copy them, and not leave a readable duplicate behind. A restated matrix double-counts
every label and turns the separator row into a phantom figure named `Fig #` (the Ch12
defect), producing check-6 FAILs that cannot be fixed by editing prose.

Labels were harvested by **opening each of the 13 rendered assets** in this session,
never by text extraction. This chapter is the strongest possible case for that rule:
`page.get_text("words")` returns **0 words on all 17 pages** and `page.get_drawings()`
returns **0 drawings**, because the source is a 100% scanned raster. A text-extraction
harvest here would have returned an empty label set for all 116 labels and passed every
downstream check vacuously.

| ID | Fig # | Type | Label row wording | Ticked |
|----|-------|------|-------------------|--------|
| — | Fig 6.1 | label | Figure labels: "Electrodes"; "Spark discharge"; "Gases"; "CH4"; "NH3"; "H2O"; "H2"; "To vacuum pump"; "Boiling water"; "Water out"; "Condenser"; "Water in"; "Water droplets"; "Water containing organic compounds"; "Liquid water in trap" | |
| — | Fig 6.2 | label | Figure labels: "Triceratops"; "Tyrannosaurus"; "Pteranodon"; "Crocodilian"; "Archaeopteryx"; "Stegosaurus"; "Brachiosaurus" | |
| — | Fig 6.3 (a) | label | Figure labels: "Thorn"; "Bougainvillea"; "Tendril"; "Cucurbita" | |
| — | Fig 6.3 (b) | label | Figure labels: "Man"; "Cheetah"; "Whale"; "Bat" | |
| — | Fig 6.4 (a) | label | No descriptive callouts — unpolluted-area panel carrying only the "(a)" panel letter; a dark-winged and a white-winged moth on a pale lichen-covered trunk | |
| — | Fig 6.4 (b) | label | No descriptive callouts — polluted-area panel carrying only the "(b)" panel letter; the same two moths on a soot-darkened trunk | |
| — | Fig 6.5 | label | No descriptive callouts — four finch heads distinguished only by the numerals 1, 2, 3, 4 below them | |
| — | Fig 6.6 | label | Figure labels: "Marsupial radiation"; "AUSTRALIA"; "Sugar glider"; "Tasmanian wolf"; "Tiger cat"; "Marsupial mole"; "Banded anteater"; "Koala"; "Marsupial rat"; "Bandicoot"; "Wombat"; "Kangaroo" | |
| — | Fig 6.7 | label | Figure labels: "Placental mammals"; "Australian marsupials"; "Mole"; "Marsupial mole"; "Anteater"; "Numbat (anteater)"; "Mouse"; "Marsupial mouse"; "Lemur"; "Spotted cuscus"; "Flying squirrel"; "Flying phalanger"; "Bobcat"; "Tasmanian tiger cat"; "Wolf"; "Tasmanian wolf" | |
| — | Fig 6.8 | label | Figure labels: "Number of individuals with phenotype"; "Phenotypes favoured by natural selection"; "Medium-sized individuals are favoured"; "Peak gets higher and narrower"; "Peak shifts in one direction"; "Two peaks form" | |
| — | Fig 6.9 | label | Figure labels: "Cenozoic"; "Mesozoic"; "Paleozoic"; "Quaternary"; "Tertiary"; "Cretaceous"; "Jurassic"; "Triassic"; "Permian"; "Carboniferous"; "Devonian"; "Silurian"; "Bryophytes"; "Sphenopsids (horsetails)"; "Ginkgos"; "Gnetales"; "Angiosperms (flowering plants)"; "Monocotyledons"; "Dicotyledons"; "Herbaceous lycopods"; "Ferns"; "Conifers"; "Cycads"; "Arborescent lycopods"; "Seed ferns"; "Progymnosperms"; "Psilophyton"; "Zosterophyllum"; "Rhynia-type plants"; "Tracheophyte ancestors"; "Chlorophyte ancestors" | |
| — | Fig 6.10 | label | Figure labels: "Turtles"; "Lizards"; "Snakes"; "Tuataras"; "Crocodiles"; "Birds"; "Mammals"; "Sauropsids"; "Synapsids"; "Dinosaurs (extinct)"; "Therapsids (extinct)"; "Thecodonts (extinct)"; "Pelycosaurs (extinct)"; "Early reptiles (extinct)"; "Quaternary"; "Tertiary"; "Cretaceous"; "Jurassic"; "Triassic"; "Permian"; "Carboniferous" | |
| — | Fig 6.11 | label | No descriptive callouts — a 3 x 2 grid of unlabelled skull-and-head illustrations, top to bottom: adult modern human being, baby chimpanzee, adult chimpanzee | |

**Parsed label total: 116** = 15 + 7 + 4 + 4 + 12 + 16 + 6 + 31 + 21, across **9**
label-bearing assets. The four `No descriptive callouts` rows contribute 0 and are
invisible to the parser by design. Verify with `_extract_labels` **imported from
`check_pdf.py`**, never a re-implementation.

### Labels deliberately NOT quoted, and the obligations they create

- **The panel letters `(a)`, `(b)`, `(c)`** on figs 6.3, 6.4 and 6.8. Single-character
  tokens; `_coverage_ratio` strips length-1 tokens and would match any stray letter.
  **Obligation:** each caption must name its panels as NCERT does — 6.3 "(a) Plants and
  (b) Animals", 6.4 "(a) In unpolluted area (b) In polluted area", 6.8 "(a) Stabilising
  (b) Directional and (c) Disruptive".
- **Fig 6.5's numerals 1-4.** Bare digits. **Obligation:** the adaptive-radiation passage
  must state that Darwin's finches show *varieties of beaks on the same island*, which is
  what the four heads exist to show; the digits themselves carry no fact.
- **Fig 6.10's time axis (0, 50, 100, 150, 200, 250, 300, 350 million years).** Numerals
  on a scale bar, not callouts. **Obligation, and it is marks-critical:** the running text
  must carry the ages — early reptiles at ~350 mya, the Sauropsid/Synapsid split near
  300 mya, dinosaurs extinct ~65 mya — since dropping the axis loses the only quantitative
  content of the figure.
- **Fig 6.1's four gas formulas are quoted** (`CH4`, `NH3`, `H2O`, `H2`) because Miller's
  input mixture is examinable. **Obligation:** write them with `<sub>` tags, never Unicode
  subscripts (§4.4 / check 5); ReportLab's text layer then extracts them as `CH4`, `NH3`,
  `H2O`, `H2`, which is what check 6 will look for.
- **Colour-carried meaning, fig 6.4.** NCERT distinguishes the two moths *and* the two
  trunks by tone. After `convert("L")` + `autocontrast` the dark-winged and white-winged
  moths remain plainly distinguishable, and panel (b)'s trunk is visibly darker than
  panel (a)'s — checked on the opened assets, so no information is lost. **Obligation:**
  the caption/text still states in words that the melanised moth is inconspicuous on the
  soot-covered trunk and conspicuous on the lichen-covered one.

---

## Extraction gate record — session `1-F`

Run: `/vercel/share/neetenv/bin/python "notes/class 12/Ch6_Evolution/audit_figures.py"`
→ **GATE PASSED: 13 figures, slack in range, all edge ink explained.** (Re-run from disk
this session; the script is committed beside `extract_figures.py`.)

### Why this chapter needs a different gate — the premise, proved not assumed

The audit prints its premise before it prints results:
`PREMISE: total text-layer words=0, total drawings=0`.

The source is a **100% scanned raster** — every one of the 17 pages is a single full-page
image. Two of the skill's three checks are therefore **structurally inert**, not merely
quiet:

| Skill check | On this chapter | Verdict |
|---|---|---|
| **A.** text-layer word grazing | `words_in_rect = 0` for all 13 rects | **vacuous — cannot fail.** Provides zero evidence and must never be cited here |
| **B.** drawings-extent overflow | `no drawings` for all 13 rects | **vacuous** |
| **C.** border-band ink | works, but its word-exclusion clause is inert, so scanned prose and captions fire as edge ink | **usable only with a named-explanation list** |

Replacement gate, both computed from page pixels at 150 dpi (`audit_figures.py`):

- **A' interior ink slack** — distance from each rect edge to the nearest ink inside it.
  Negative slack means ink is flush against the edge (probable clip); large positive slack
  means wasted margin or a mis-pinned edge. Tolerances `SLACK_MIN = -0.5 pt` (one pixel of
  quantisation noise, validated by re-measuring six figures at 150/200/300/400 dpi) and
  `SLACK_MAX = 22.0 pt`.
- **B' edge-band probe** — dark pixels in an 8 pt band just outside each edge. Every hit
  must be named in the script's `EXPLAINED` dict; an unnamed hit **fails** the gate.

**`BAND_TOL` is 12 px, not the skill's 40.** Two real defects in this chapter sat *under*
40 and passed clean before being caught by eye — see the re-pin table. A clipped 8 pt
label is a small ink cluster by construction, so a 40 px floor is blind to exactly the
defect class that survives every other check on a scanned page. The cost is more chatter
from neighbouring prose, which `EXPLAINED` triages by name.

### Gate output, as re-run this session

| Asset | A) words | B) drawings | A') interior slack L/T/R/B (pt) | B') edge-band ink |
|---|---|---|---|---|
| `fig_6_1` | **vacuous** (0) | **vacuous** (0) | 3.0 / 3.6 / 4.4 / 3.3 | B:32px — caption band + prose below |
| `fig_6_2` | **vacuous** (0) | **vacuous** (0) | -0.2 / 9.0 / 5.8 / 2.4 | clean |
| `fig_6_3a` | **vacuous** (0) | **vacuous** (0) | 3.0 / 3.1 / 5.0 / 5.8 | T:20px — leaf/branch furniture |
| `fig_6_3b` | **vacuous** (0) | **vacuous** (0) | 2.1 / 0.0 / 9.4 / 3.9 | T:46px — panel (a) above; B:60px — caption band |
| `fig_6_4a` | **vacuous** (0) | **vacuous** (0) | 2.2 / 3.6 / 0.9 / 0.8 | R:98px — panel (b), separate asset; T:50px — furniture |
| `fig_6_4b` | **vacuous** (0) | **vacuous** (0) | 3.7 / 4.6 / 0.9 / 4.4 | L:671px — panel (a), separate asset; R:1028px — decorative border band from x~551 |
| `fig_6_5` | **vacuous** (0) | **vacuous** (0) | -0.2 / 4.1 / 3.3 / 4.2 | T:39px — furniture |
| `fig_6_6` | **vacuous** (0) | **vacuous** (0) | 4.1 / 5.0 / 3.8 / 1.0 | clean |
| `fig_6_7` | **vacuous** (0) | **vacuous** (0) | 2.2 / 4.2 / 2.7 / 2.3 | T:62px — furniture; B:36px — caption band |
| `fig_6_8` | **vacuous** (0) | **vacuous** (0) | 2.9 / 2.2 / 0.8 / 3.0 | clean |
| `fig_6_9` | **vacuous** (0) | **vacuous** (0) | 2.7 / 4.1 / 2.3 / 4.0 | T:34px — furniture |
| `fig_6_10` | **vacuous** (0) | **vacuous** (0) | 3.5 / 2.8 / 3.2 / 3.5 | T:63px — furniture |
| `fig_6_11` | **vacuous** (0) | **vacuous** (0) | 3.2 / 4.1 / 3.5 / 3.4 | clean |

Every B' hit is one of four things — the neighbouring sub-panel, the caption band the
crop convention excludes, the page-furniture leaf motif, or the decorative right-margin
band — and each is named per side in `audit_figures.py`'s `EXPLAINED` dict. The two
`-0.2 pt` L readings (`fig_6_2`, `fig_6_5`) are pixel quantisation, not clipping: they
oscillate around zero across DPIs instead of staying negative, and both edges are clean
on the opened asset.

### Rects re-pinned during `1-F`, and what caught each one

| Asset | Was | Now | Caught by | Why |
|---|---|---|---|---|
| `fig_6_1` | (214, 103, 531, 499) | (226, 102, 519, 359) | **eye** (contact sheet) | `y1=499` came from a mis-read caption row. The caption band is at y=366-390, not y=502-535, so the crop shipped the caption **plus five lines of body prose** (y404-497). Full-width prose lines look exactly like figure ink to an extent probe, so no numeric check objected. Artwork ink ends y=356.1 ("Liquid water in trap"); `y1=359` splits art from caption. x edges tightened once the prose was gone. |
| `fig_6_2` | y1=545 | y1=515 | A' slack | Plate ink ends y=512.6, then y=513-545 is blank before the caption at y=555 — 33 pt of dead whitespace. |
| `fig_6_3a` | x0=392 | x0=272 | **eye** | The figure spans the full text-block width, not just the right half. `x0=392` sliced the **entire Bougainvillea + Thorn panel** off, leaving only Cucurbita. Column profile shows figure ink from x~280 to x~517; x0=272 clears the prose gutter (x=262-278). |
| `fig_6_3b` | x0=392 | x0=272 | **eye** | Same error: the forelimb row has four ink clusters (Man x280-320, Cheetah x330-360, Whale x390-420, Bat x450-505) and `x0=392` cut Man and Cheetah off entirely. |
| `fig_6_4b` | x1=547, y1=236 | x1=550, y1=242 | x1 by B'; **y1 by eye** | x1=547 clipped the photo (the reported R-band ink was the decorative border band from x~551, not artwork). y1=236 **sliced the "(b)" panel label in half** (label at y=229-238) — only ~9 dark px/row, far under a 40 px band floor, which is why `BAND_TOL` is 12. |
| `fig_6_8` | x0=126 | x0=120 | B' **after** lowering `BAND_TOL` 40 → 12 | The rounded frame's left arc bulges to x=123.0 at mid-height, so x0=126 cut a flat notch out of the figure's own border. At `BAND_TOL=40` the 25 px arc read as "clean". |
| `fig_6_10` | x0=65 | x0=57 | **eye** (contact sheet) | The era label "Carboniferous" outdents to x=59.5, so x0=65 shaved its leading "C" off — the asset read "arboniferous". ~55 dark px at 200 dpi, again under a 40 px floor. Nothing at all left of x=59, so x0=57 is safe. |
| `fig_6_11` | (148, 98, 478, 518) | (136, 102, 435, 516) | L by B', y0 by A', x1 by A' | Old rect clipped the middle skull's occiput (380 px L-band hit). `y0=96` pulled a sliver of the top-right leaf furniture (x=488-496, ink to y=97) into the corner — A' read T slack 0.0; artwork starts y=106, so y0=102 clears it. Excluding that furniture then exposed R+65.5 pt of dead margin: real artwork ends x=431.7, so x1 went 497 → 435. |

Four of the eight re-pins were found **by eye, not by the numeric gate** — and two of
those (`fig_6_4b`, `fig_6_10`) were clipped labels small enough to pass any cluster
threshold at 40 px. That is the reason step 5 is not optional and the reason this
chapter's threshold is 12.

**Monochrome pipeline defect fixed during `1-F`:** the first version of
`extract_figures.py` autocontrasted the RGB pixmap directly, so all 13 assets shipped
`mode=RGB`. §4.4 and §0.4 require true single-channel monochrome, and autocontrast on RGB
stretches each channel independently (shifting hue rather than maximising ink contrast).
The pipeline is now clip-render → `.convert("L")` → `autocontrast(cutoff=1)`, and all 13
files re-verified `mode=L` this session.

### Visual verification

All **13/13** assets were opened and read at full size in this session — individually,
not merely as a contact sheet — and each is complete, correctly regioned and legible:
6.1 shows all 15 callouts including "Liquid water in trap" with no prose; 6.3a shows both
Bougainvillea/Thorn and Cucurbita/Tendril; 6.3b shows all four animals above all four
forelimbs; 6.4b shows its "(b)" label intact; 6.8 shows the full rounded frame, the
y-axis title and all three panels with their arrows; 6.10 shows "Carboniferous" whole and
the full 0-350 axis; 6.11 shows all six illustration cells. No crop clips artwork and
none admits body text.

Contact sheets and per-page overlays from the pinning work are in `scratch/ch6_figs/` and
`scratch/ch6_verify/`; this session's caption strips and page census are in
`scratch/ch6_doc/`. Note that `view` caches by path — every artefact above is written to
a unique filename for that reason.

---

## Carry-over to later Pass 1 sessions

1. **`1-Z` must move the 13 matrix rows into the `## Facts` table** and assign contiguous
   `F###` IDs. Move, never copy; leaving a readable duplicate breaks check 6 (Ch12).
2. **Ticks stay empty** until Pass 2 writes the script.
3. **The five obligations** listed under "Labels deliberately NOT quoted" are Pass 2
   content requirements, not figure work. The fig 6.10 time-axis one is marks-critical.
4. **`1-S` must inventory the facts the figures depend on** — Miller's apparatus and its
   gas mixture (fig 6.1), the industrial-melanism observation (fig 6.4), Darwin's finch
   beaks (fig 6.5), marsupial adaptive radiation and convergence with placentals
   (figs 6.6, 6.7), the three modes of selection (fig 6.8), and the geological-period
   tables (figs 6.9, 6.10). The figures carry no prose of their own for these.
5. **Do not "restore" audit checks A and B** in `audit_figures.py`. They cannot work on a
   scanned PDF; both scripts carry a header saying so.
6. **Gate 1 stays OPEN** when `1-F` closes. Four of the five Pass 1 sessions have not run.
