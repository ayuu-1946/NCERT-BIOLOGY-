# Ch19 - Chemical Coordination and Integration (Class 11)

Build record kept under **SUPREME COMMAND PROMPT.md v6**. Pipeline:
`Pass 1 -> [Gate 1] -> Pass 2 -> [Gate 2] -> Pass 3 -> [Gate 3] -> deliver`.

**Status: Gate 2 CLOSED (green). Pass 3 (dual human verification) not yet started.**

## Files

| File | Role |
|---|---|
| `Ch19_ChemicalCoordinationAndIntegration_inventory.md` | Pass 1 frozen inventory - 218 rows, no row may be added, removed or reworded |
| `extract_figures.py` | Pass 1-F figure extraction (pinned boxes -> monochrome PNG) |
| `assets/` | 7 extracted plates, all single-channel `L` |
| `Ch19_ChemicalCoordinationAndIntegration.py` | Pass 2 script - imports repo-level `neet_template.py`, declares no style |
| `Ch19_ChemicalCoordinationAndIntegration.pdf` | Rendered output, 14 pages A4 portrait |
| `README.md` | This build record |

## Pass 2 - what was written

The script was written **linearly from the frozen inventory in Content Order (SS5)**,
one `# ---- N.N ----` block per NCERT section, importing the frozen style module so
that no colour, font, geometry or flowable style is re-declared locally.

Section blocks, in order: title -> chapter intro/map -> 19.1 -> 19.2 -> 19.2.1
hypothalamus -> 19.2.2 pituitary -> 19.2.3 pineal -> 19.2.4 thyroid -> 19.2.5
parathyroid -> 19.2.6 thymus -> 19.2.7 adrenal -> 19.2.8 pancreas -> 19.2.9 testis
-> 19.2.10 ovary -> 19.3 heart/kidney/GI hormones -> 19.4 mechanism of hormone
action -> Recap (source SUMMARY) -> Appendix (exercise terms + trailing NOTE page).

All 7 plates are placed inside the section that cites them, each followed by a
"Read the plate" NOTE that names its in-figure labels **verbatim** (carry-forward 7).

### Rule 3 - summary-unique facts folded into the body

| Row | Fact stated only in the NCERT summary | Folded into |
|---|---|---|
| F125 | catecholamines drive glycogenolysis / lipolysis / proteolysis | 19.2.7 |
| F179 | progesterone in mammary gland development and lactation | 19.2.10 |
| F191 | the GI hormones regulate secretion of digestive juices | 19.3 |

### The eight Pass-1 carry-forwards, and how each was honoured

1. **Greek glyphs (F142/F143).** check 5 bans Greek from the PDF, so the running
   text spells the islet cells `alpha-cells` / `beta-cells` and a NOTE records that
   the source prints the Greek letters. Ionic charges use `<super>` tags
   (`Ca<super>2+</super>`, `Na<super>+</super>`, `K<super>+</super>`,
   `Ca<super>++</super>`), never Unicode superscripts.
2. **Source-verbatim spellings.** All five printed as the source prints them and
   flagged in place: `sella tursica` (F039), `Exopthalmic goitre` (F087),
   `pupilary dilation` (F121/F125), `glucagons` (F153), and `Diagramatic` in the
   Figure 19.5 captions (F208) - while Figures 19.2/19.3/19.4 keep the source's
   correct `Diagrammatic`.
3. **Page 6 is not italic.** The source italicises nearly all of page 6 by
   typesetting accident; SS19.2.7 is set here as ordinary body text.
4. **The one exercise gap** - Q1(a) `Exocrine gland`, a term the body uses (F139,
   F188) but never defines - is closed in SS19.1, phrased only from the chapter's own
   ductless-vs-duct-bearing contrast and **labelled as an addition** (Rules 2, 5).
5. **Figure 19.5 stays with SS19.4.** Q8 is answered by SS19.4's prose plus F217's
   plate labels, so both panels sit inside SS19.4.
6. **Exercise wording.** The body keeps `atrial wall` and `gastro-intestinal tract`;
   the exercises' shorter `Atrium` / `G-I Tract` are recorded only in the appendix.
7. **Figure-label coverage.** All 7 plates carry their callouts as artwork, so each
   figure is followed by a NOTE naming its labels - matrix rows F212-F218, **38
   label strings**, which is what satisfies check 6 and lets a print reader name the
   parts of a photocopied diagram.
8. **Figure 19.4 is one asset.** Its two panels interleave horizontally, so (a) and
   (b) ship as the single combined plate `fig_19_4.png` and are read in one note.

## Gate 2 - linter result

```
cd /vercel/share/v0-project
python check_pdf.py --strict "notes/class 11/Ch19_ChemicalCoordinationAndIntegration"
```

```
check_pdf.py - Ch19_ChemicalCoordinationAndIntegration.pdf  (14 pages)
inventory: Ch19_ChemicalCoordinationAndIntegration_inventory.md

[PASS]  1. Footer/header band .......... no text in top/bottom margin bands
[PASS]  2. Legibility floor ............ smallest rendered text 6.0pt
[PASS]  3. Grayscale-only images ....... all 7 embedded images monochrome
[PASS]  4. No person photograph ........ no portrait/photo row in the manifest
[PASS]  5. Banned glyphs ............... no Unicode arrows, sub/superscripts, Greek, emoji
[PASS]  6. Figure-label coverage ....... 38/38 labels fully in text; 0 partial; 0 missing
[PASS]  7. Frozen inventory ticked ..... all 218 Facts rows ticked
[PASS]  8. Page geometry ............... all 14 pages A4 portrait (595x842pt)
[PASS]  9. Orphaned headings ........... 57 banner headings all followed by content
[PASS] 10. Badge/heading collision ..... 147 filled plates all clear

VERDICT: PASS   (0 fail, 0 warn)   exit 0
```

`--strict` is green as well, i.e. **zero WARNs** - no warning had to be waived to
advance, which is the ideal condition the prompt asks for at Gate 2.

## Rebuilding

```bash
cd "notes/class 11/Ch19_ChemicalCoordinationAndIntegration"
/vercel/share/neetenv/bin/python Ch19_ChemicalCoordinationAndIntegration.py   # -> PDF
cd /vercel/share/v0-project
/vercel/share/neetenv/bin/python check_pdf.py --strict "notes/class 11/Ch19_ChemicalCoordinationAndIntegration"
```

If `/vercel/share/neetenv/bin/python` is missing, rebuild the venv first (SS0.2) -
never diagnose anything before that check.

## Next: Pass 3

Gate 3 requires **zero confirmed defects plus a bidirectional full read** - source
-> PDF (is every fact there, in the right place, unmangled?) and PDF -> source (is
anything here that the source does not support, or that Rule 5 leaves unlabelled?),
with every rendered page eyeballed for layout. Spot-rendering during Pass 2 covered
only pages 1, 4, 8, 12 and 14; the remaining pages are unread by a human eye and
must not be treated as verified.
