# Gate 1 for Ch5 — Morphology of Flowering Plants

*An explainer for the change that closed Gate 1 on Class 11, Chapter 5.*

---

## Background

### For a reader new to this repository (skip if you built it)

This repository turns NCERT Biology chapters into replacement study PDFs. The governing idea,
set out in `SUPREME COMMAND PROMPT.md` and extracted into `GATE_1_PASS_1_SOURCE_MASTERY.md`, is
**bounded iteration through gated passes**:

```
Pass 1 → [GATE 1] → Pass 2 → [Gate 2] → Pass 3 → [Gate 3] → deliver
```

Each pass ends at a gate that must be green before the next begins. The unusual part is where
the effort goes. Most document pipelines start writing and fix problems later. This one spends
Pass 1 doing nothing but *reading the source and writing down what is in it* — and it does not
permit a single line of the chapter script to be written until that list is frozen and
machine-validated.

> **The frozen inventory.** A Markdown file, `<Chapter>_inventory.md`, holding one numbered row
> per preservable fact: every definition, number, scientist, binomial, example, process step,
> comparison, exception, table cell, figure caption, and — critically — **every label printed
> inside every figure**. Rows are `F001`, `F002`, … and once frozen, *the rows win*: if a count
> and the rows disagree, you change the count, not the rows.

The inventory is not documentation about the work. It is load-bearing. The repo-level linter
`check_pdf.py` reads it directly:

- **check 6** parses the inventory's figure-label rows and fails the build unless every label
  appears somewhere in the PDF's running text.
- **check 7** fails unless every Facts row is ticked, which is how Pass 2 proves it wrote
  everything down.

So a thin inventory does not produce a loud failure. It produces a *quiet success*: check 6
finds no labels, verifies nothing, and passes. This is the failure mode the whole design is
arranged against.

### The five-session rule

Pass 1 is split across five mandatory sessions, and this is a rule rather than a preference:

| Session | Job |
|---|---|
| `1-S` | Read the source; build the Facts inventory from prose |
| `1-H` | Heading sweep — walk the skeleton, ignore the prose |
| `1-O` | Opener sweep — read the first sentence of each section, ignore the headings |
| `1-F` | Figures — extract, convert to monochrome, verify, harvest in-figure labels |
| `1-Z` | Exercise gaps, summary classification, freeze, machine-derived counts |

The reason `1-F` is isolated is worth stating, because this change turns on it. **Opening every
rendered figure and reading it consumes context.** When context runs short, the label harvest
silently degrades into text extraction — and text extraction of NCERT figures returns almost
nothing, because labels are baked into the artwork as pixels or vector strokes. On Ch12, *all
61 labels across 7 figures were invisible to `get_text()`*. An empty label set passes Gate 1
and check 6 trivially. Hence the doctrine's warning: **a suspiciously label-free figure is a
red flag, not a clean result.**

### Where Ch5 actually stood

`CHAPTER_TRACKER.md` said "⬜ Not done". On disk, it was more interesting than that. Session
`1-F` had already run in some earlier task, and had left behind real work: 17 extracted assets,
a re-pin log, a three-part crop audit recorded as clean, and a reproducible `extract_figures.py`.

But the inventory was **extraction-only**. It had a figure table and production notes, and it
had *none* of the following:

- no Facts table — so nothing for check 7 to tick;
- no heading sweep, no opener sweep;
- no summary classification, no exercise-gap classification;
- and no figure-label matrix in the format `check_pdf.py._extract_labels` parses.

This exact shape had already been hit twice, on Ch12 (Respiration in Plants) and Ch6 (Anatomy of
Flowering Plants). Both times the standing decision was the same: **a substandard inventory is
rebuilt to the §6 standard, not patched.** That is what this change does — plus one thing
nobody expected to be necessary.

---

## Intuition

Two ideas carry this change. The first is mundane and the second is the interesting one.

### Idea 1: derive every count, never state it

The doctrine says a count is never stated in one place, so a count is never *fixed* in one
place. Ch13's tracker header said `9/32` while its own footer said `4/13`. Ch11's inventory
header described a 158-row table that actually held 282 rows, so *every derived count in it was
wrong*.

The fix is to stop writing counts down. The inventory is emitted by a script that holds the
rows as data:

```python
ROWS = [
    ("5.1", "opener", '"In majority of the dicotyledonous plants..." (qualifier: majority)'),
    ("5.1", "term",   '"It bears lateral roots of several orders..."'),
    # ... 278 more
]
```

IDs become `F001..F280` by construction — contiguous because they are generated, not typed. And
every number in the header is an f-string over a parse of that same list:

```
- Heading rows (`Type: heading`): **30** = 20 numbered + 4 structural + 6 unnumbered
```

Nobody counted to 30. The `30`, the `20`, the `4` and the `6` are all `len()` calls, and a
separate checker asserts the addends sum to the total — because *"a census that asserts a total
separately from its own list will disagree with it."*

### Idea 2: a green audit can be lying to you

Now the substance. Session `1-F` had already run, its audit was green, and its tracker even
said, of Figure 5.2:

> *"Figure 5.2's `Laterals` word is an in-figure label and is intentionally retained."*

Here is what the asset actually contained:

```
   ╭──────────── crop rect x0 = 78 ────────────╮
   │                                          │
 L a│t e r a l s        ⟵ label starts at x = 63.1
   │                                          │
```

The crop began at `x = 78`. The label began at `x = 63.1`. Fourteen and a half points of the
word were outside the rectangle, so the printed asset read **"erals"**.

Why did the audit pass it? Because of how the two text-based checks are built. Consider a toy
page with one label and one crop:

| | check A — *word grazing* | check C — *border-band ink* |
|---|---|---|
| **What it does** | flags a word only *partly* inside the rect | flags dark pixels just outside the rect |
| **What it ignores** | words wholly outside | any pixel a text-layer word explains |

A label sitting *entirely* outside the rect satisfies both. It grazes no boundary, so A is
silent. Every dark pixel it produces is explained by a text-layer word, so C deletes them all.
**Both checks are structurally blind to the one defect that matters most.** Twelve of Ch5's
seventeen crops carried a defect, and the audit was green on every one.

There is no clever fix for this. The only thing that finds it is opening the image and looking —
which is exactly why `§4.4 Step 3` makes the visual pass mandatory, and why `1-F` gets its own
context budget.

### Idea 2b: and the measurement tool was lying too

Having found the clipping, the obvious move is to re-pin the rectangles from the page's own
geometry — take the union of `page.get_drawings()` rects and pad it. For Figure 5.14 that
returns a right edge at `x = 299.9`.

The plate's actual ink ends at `x = 276.9`. The neighbouring prose column begins at `x = 303.1`.

So the "measured" rectangle is 23 points too wide, in a 26-point gap — and a rect padded from it
bleeds body text into the figure. Which is precisely what happened on the first re-pin attempt.

The culprit is NCERT's copyright watermark. That diagonal *"not to be republished"* across every
page is **vector artwork**, and `get_drawings()` has no notion of "belongs to the figure":

```
        ┌─────────────── page 12 ───────────────┐
        │   ╭─── real plate ───╮                │
        │   │  ink → x=276.9   │   prose col →  │
        │   ╰──────────────────╯   x=303.1      │
        │        ╲ n o t   t o   b e ╲          │   ← vector strokes,
        │  drawings union → x=299.9             │     grey ≈ 235
        └───────────────────────────────────────┘
```

The insight that unlocks it: **the watermark is light and the artwork is dark.** The watermark
renders around grey 230–245; figure outlines and label text sit below 215. So don't ask the PDF
what it drew — render it and measure the dark pixels:

```python
bbox = img.point(lambda v: 255 if v < 215 else 0, mode="L").getbbox()
```

That single threshold separates the two, and it is what every rectangle in this change is
ultimately pinned against.

---

## Code

Nothing shared was touched. `check_pdf.py` and `neet_template.py` are frozen repo-level files
and remain byte-identical; the gate check *imports* from `check_pdf.py` rather than modifying or
replicating it.

### 1. The measurement primitive — `scratch/ch5morph_gate1/ink_bbox.py`

The whole re-pin rests on this. Render a band of the page, threshold, take the bounding box, and
convert back to PDF points:

```python
def ink_bbox(page_no, band, threshold=215):
    """Bbox of pixels darker than `threshold` inside `band`, in PDF points."""
    pix = page.get_pixmap(clip=pymupdf.Rect(*band), dpi=DPI, alpha=False)
    img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples).convert("L")
    mask = img.point(lambda v: 255 if v < threshold else 0, mode="L")
    box = mask.getbbox()
    ...
```

One correction was needed after first use. A **photograph's** ink bbox under-reports its edge,
because the background is light — Fig 5.6's Guava photo has ink to `x=501.7` but its image
extends to `x=512.0`. So for photographic plates the ink bbox is unioned with the raster
`get_image_info()` bbox.

### 2. The re-pin — `extract_figures.py`

All 17 rectangles were replaced, and the docstring now records the standard rather than leaving
it implicit:

```python
# Each rect = the plate's measured content extent, padded by ~8 pt and then clamped
# by the nearest neighbour (printed caption, adjacent prose column, page header).
FIGS = [
    ("5_1",  4, (88,  98, 325, 404)),
    ("5_2",  4, (55, 445, 543, 663)),   # x0 78 → 55 restores `Laterals`
    ...
]
```

One standing decision changed here: **assets are now artwork-only, with the printed caption
excluded.** Captions are typeset by the Pass-2 script from the inventory's `caption` rows, so a
caption baked into the plate would print twice. This matches Ch6, and it fixes the four half-cut
caption rows by construction.

### 3. The audit gains an authoritative check — `audit_figures.py`

Check B (drawings-extent overflow) is kept, because deleting it would hide the disagreement, but
it is now explicitly subordinate to a new check **B2** that measures ink instead of drawings:

```
--- B) drawings-extent overflow (watermark-polluted; adjudicated by B2) ---
fig_5_3:  OVERFLOW L0.0 T5.8 R0.0 B0.0
fig_5_8:  OVERFLOW L1.7 T6.7 R0.0 B12.9
fig_5_14: OVERFLOW L0.4 T0.0 R19.1 B0.0
fig_5_15: OVERFLOW L10.3 T3.1 R0.0 B6.8

--- B2) ink-extent overflow (authoritative) ---
fig_5_3 … fig_5_17: clean          ← all 17
```

B2 being clean is what *proves* B's four reports are watermark rather than clipping. Check A also
now excludes **rotated** text spans, because page 11 carries a rotated, non-rendering duplicate
`(a)` from the watermark layer that otherwise reports as a grazing word against Fig 5.12.

### 4. The inventory is generated — `scratch/ch5morph_gate1/build_inventory.py`

280 rows as data, and the whole document emitted from them. The crop rects are *not* restated
here; they are imported from the extraction script that actually produced the assets:

```python
def crop_rects():
    """Crop rects, imported from the extraction script rather than restated."""
    ...
    assert {f for f, _, _, _ in MANIFEST} == set(rects)
```

That assertion exists because the first draft *did* duplicate them, and Fig 5.1's copy went
stale within one re-pin. A rect written in two places is a count written in two places.

### 5. The gate is earned by machine — `scratch/ch5morph_gate1/gate1_close.py`

37 assertions, importing the real parser rather than imitating it:

```python
spec = importlib.util.spec_from_file_location("check_pdf", CHECK_PDF)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
labels = mod._extract_labels(text)          # the function check 6 will actually use
```

It asserts the label parse (11 figures / 56 labels, **no doubling, no phantom `Fig #` row**), ID
contiguity, header agreement against a re-parse, census totals against their own adjacent lists,
that all 20 numbered source headings appear *in source order*, that manifest rects equal the
extraction script's, and that all 17 assets on disk are single-channel `mode=L`.

One subtlety it protects. Six of Ch5's plates are genuinely label-free, and the tempting thing
is to give them a row saying so. That would be a bug: `_extract_labels` matches any row
beginning "Figure labels" and, finding no quoted strings, **splits the remainder on `;`** — so
`Figure labels: none` parses as a phantom label. Their emptiness is recorded in the manifest
prose instead, and each was confirmed by opening the asset.

### 6. The adjudicator — `scratch/ch5morph_gate1/adjudicate_inherited.py`

This one exists because the first draft of the re-pin log was *wrong*. It claimed "15 defects"
while listing 16 IDs, and it recorded a Fig 5.14 clip inferred from the very drawings union the
change had just rejected — Fig 5.14's inherited rect was clean.

So the defect count stopped being asserted and started being measured. Every inherited rectangle
is tested against its plate's ink-and-image extent:

```
inherited rects that CLIPPED artwork/labels: 8 of 17  -> 5.1, 5.2, 5.4, 5.5, 5.6, 5.9, 5.10, 5.16
inherited rects that cut the caption:        4 of 17  -> 5.3, 5.8, 5.12, 5.17
TOTAL with at least one defect:             12 of 17
TOTAL fully clean:                           5 of 17  -> 5.7, 5.11, 5.13, 5.14, 5.15

--- same test applied to the CURRENT rects ---
current rects that clip content: 0  (none)
```

A detail worth keeping: the adjudicator deliberately does **not** union text-layer word bboxes
into the content extent. Text renders as ink, so the ink bbox already covers every label; adding
words only drags in the neighbouring prose column (it put Fig 5.1's extent at `x=330.0`, the
left edge of page 4's right-hand column) and the rotated watermark `(a)`.

### 7. Reconciling parallel figure work that landed on `main` mid-session

While this was in progress, two commits reached `main` adding *derived* figure layers — and
both were built from the pre-re-pin assets, so both had inherited the defects.

**`assets/caption_free/`** was 17 copies produced by a `remove_captions.py` that pixel-crops
the caption band off an already-extracted PNG. Its own record listed 10 of 17 figures as
"unchanged", which is exactly what you would expect: those were the plates whose crop excluded
the caption already. So `caption_free/fig_5_2.png` still read **"erals"**, and
`caption_free/fig_5_4.png` still had no `(b)`/`(c)` markers. Cropping a caption off a defective
plate leaves a defective plate.

It was removed, for three reasons that compound:

1. it carried the defects;
2. its crop boxes were hardcoded pixels measured against the old dimensions — `fig_5_12.png`
   went from 684x2180 to 430x2230, so a box of `(0, 0, 592, 2240)` now *pads with black*
   instead of trimming;
3. it is subsumed. Excluding the caption in the PDF rect is one reproducible step instead of
   two, and it is what surfaced the 12 defective rectangles in the first place.

**The two horizontal composites were kept**, because they solve a real problem rather than a
duplicated one. Fig 5.12 is 430x2230 natively — about 1:5.2 — and §4.4 forbids squashing a
plate to fit, so re-flowing its five panels into a strip is the correct remedy, not a
cosmetic one.

But they needed regenerating, and doing so exposed a defect that would have failed Gate 2:

```python
canvas = Image.new("RGB", (...), "white")     # ← both committed composites were 3-channel
```

`check_pdf.py` check 3 fails any build that embeds a non-greyscale image, so neither composite
could have been used as it stood. They are now `mode="L"`.

Their panel coordinates were also hardcoded pixels, and several already reached past the image
bounds *before* the re-pin — the script cropped `fig_5_12.png` to `y=2240` when that asset was
2180 px tall. So the constants were replaced with row projection, and two details were needed
to make it work:

- **"Blank" has to mean "holds no pixel darker than 215", not "is white."** Same watermark
  problem in a new place: at a pure-white threshold every watermarked row counts as content and
  the whole of Fig 5.12 segments as one band.
- **Short bands attach to a neighbouring panel, keyed on height, not on gap.** A gap rule
  cannot separate the two cases in Fig 5.12 — panel (a) sits **1 px** above panel (b) and must
  stay separate, while each panel sits ~27 px above its own marker and must merge with it.
  Heights are unambiguous: markers 33–37 px, panels 373–413 px.

The payoff is visible: the regenerated `fig_5_4_horizontal.png` **contains the `(b)` and `(c)`
markers its predecessor could not**, because its source plate now has them.

The reasoning is recorded in `HORIZONTAL_FIGURES.md`, which §4.4 sanctions as a *decisions
file* — the same role Ch11's `figure_layout_decisions.md` plays.

### 7. What the reading found

Beyond the figures, the source read produced four findings about the **source**, not the
inventory. The sharpest is `SRC-1`: §5.5.1.4 names **six** placentation types —

> *"The placentation are of different types namely, marginal, axile, parietal, basal, **central**
> and **free central**"*

— then defines and figures only five. "Central placentation" is named and never explained, which
makes exercise Q7 ("Describe the various types of placentations") impossible to answer
exhaustively from the chapter.

The tempting move is to call Q7 a Rule 2 **GAP** and answer it. That would violate Rule 5: every
fact must trace to *this* chapter's PDF, and the missing definition is not in it. So Q7 is
classified COVERED for the five described types and the shortfall is logged as a source
inconsistency, with an instruction that Pass 2 **reproduce the six-name list verbatim and not
silently "correct" it to five.**

The other three: §5.9 carries two different titles; the source prints "bicarpellary
**obligately** placed" where the standard term is *obliquely* (preserved exactly — Rule 4 bans
term drift); and the floral-formula glyphs are **invisible to `get_text()`**, so the symbol key
was read off the page images. The printed distinction — **G̲ = superior ovary, Ḡ = inferior
ovary** — exists nowhere in the text layer.

---

## Verification

### What was run

| Check | Result |
|---|---|
| `gate1_close.py` | **VERDICT GREEN — 37 pass / 0 fail** |
| `adjudicate_inherited.py` | 12 of 17 inherited crops defective; **current crops clip nothing** |
| `audit_figures.py` A / B2 / C / D | **0 grazing · B2 clean 17/17 · C clean 17/17 · D 17/17 `mode=L` @ 300 dpi** |
| Visual verification | **all 17 assets opened and read** — twice for Figs 5.5 and 5.17, after their corrections |
| `check_pdf.py` | correctly reports `SETUP ERROR: no .pdf found` — Gate 2's deliverable does not exist yet |
| Derived composites | regenerated from the corrected assets, both **`mode=L`** (were RGB), both opened and read |

The gate check was re-run **after** the documentation was written, because the Ch19 lesson is
that documentation can degrade a gate it only describes — Ch11's inventory once produced a
phantom figure and two doubled labels purely because a *column header* began "Figure labels".

### How to reproduce it

The sandbox resets between sessions, so the first command is always the venv check. A missing
interpreter is the most commonly *misdiagnosed* failure in this repo.

```bash
ls /vercel/share/neetenv/bin/python || {
  uv venv /vercel/share/neetenv --python 3.13
  uv pip install --python /vercel/share/neetenv/bin/python reportlab pdfplumber pymupdf Pillow numpy
}
```

Then, from the repository root:

```bash
# 1. regenerate all 17 assets from the source PDF
/vercel/share/neetenv/bin/python 'notes/class 11/Ch5_MorphologyOfFloweringPlants/extract_figures.py'

# 2. three-part crop audit + print-asset check
/vercel/share/neetenv/bin/python 'notes/class 11/Ch5_MorphologyOfFloweringPlants/audit_figures.py'

# 3. re-emit the inventory from its row data
/vercel/share/neetenv/bin/python scratch/ch5morph_gate1/build_inventory.py

# 4. THE GATE — must print "VERDICT: GREEN  (37 pass / 0 fail)"
/vercel/share/neetenv/bin/python scratch/ch5morph_gate1/gate1_close.py

# 5. re-derive the inherited-defect count rather than trusting the log
/vercel/share/neetenv/bin/python scratch/ch5morph_gate1/adjudicate_inherited.py
```

### Manual QA — how to see the defects for yourself

The point of this change is visual, so the check should be too.

1. **See the original defect.** Restore one inherited crop and compare:
   ```bash
   git show HEAD:"notes/class 11/Ch5_MorphologyOfFloweringPlants/assets/fig_5_2.png" > /tmp/fig_5_2_before.png
   ```
   Open `/tmp/fig_5_2_before.png` and the current `assets/fig_5_2.png` side by side. In the
   *before*, the left-hand label reads **"erals"**. In the *after* it reads **"Laterals"**.

2. **Fig 5.4 is the starkest.** Do the same for `fig_5_4.png`. The before has panels (a), (b),
   (c) but **no `(b)` or `(c)` markers at all** — the caption maps them, so a reader cannot tell
   which leaf is reticulate and which is parallel. The after has both.

3. **Check a caption cut.** `fig_5_17.png` before shows a sliced row of type along the bottom
   edge; after, the caption is gone entirely (typeset by the script in Pass 2 instead).

4. **Confirm the watermark claim yourself:**
   ```bash
   /vercel/share/neetenv/bin/python scratch/ch5morph_gate1/probe_geometry.py 12 470 620
   /vercel/share/neetenv/bin/python scratch/ch5morph_gate1/ink_bbox.py 12 40 470 302 616
   ```
   The drawings union reports Fig 5.14's right edge at `299.9`; the ink bbox reports `276.9`.
   The prose column starts at `303.1`.

5. **Prove the gate is not self-certifying.** Break the inventory and watch it fail — for
   example, duplicate one figure-label row, or change a header count by hand, then re-run
   `gate1_close.py`. It should go RED with a specific message. Then `build_inventory.py`
   regenerates the file and it goes GREEN again.

### What was deliberately *not* done

Gate 1 does not earn "Done", and this chapter has **no script, no PDF, and all 280 rows
unticked**. The repo tally was **re-derived, not incremented** — parsing the ✅ rows in
`CHAPTER_TRACKER.md` returns **24 / 32 (Class 11 17/19, Class 12 7/13)**, unchanged by this
session and in agreement with that file's header.

Two pre-existing roll-up issues surfaced while deriving that number. One was fixed because it
defeats machine counting: the **Ch17 row carried a stray leading space**, excluding it from any
`^\|\s*\d+\.` parse — which is why a strict count returned 23/31 against a correct header of
24/32. No status was changed. The other was **flagged and deliberately not adjudicated**, since
it does not concern Ch5: an "Also in progress" narrative still describes Ch12 as having Gate 3
open, while its own unit row and `CHAPTER_STATUS.md` both record all gates closed.

---

## Alternatives

### Alternative A — patch the existing inventory instead of rebuilding it

Add the missing Facts/heading/opener/summary/exercise sections to the file already on disk, and
reformat its figure table into the matrix format the linter parses.

| Pros | Cons |
|---|---|
| Much smaller diff; the file's history stays continuous | The figure table's label lists were *summaries* ("Flower, fruit, stem, leaf, node…"), not a verified harvest — reformatting them would launder unverified data into the gate |
| Preserves the earlier author's prose and production notes | Would have preserved the 12 crop defects, because nothing in a reformat requires opening an asset |
| No asset churn — 17 PNGs stay byte-identical | Leaves counts hand-written, which is the failure mode Ch11 and Ch13 both hit |

**Rejected** because the repo already decided this question twice, on Ch12 and Ch6: a
substandard inventory is quashed rather than patched. The deciding detail is that the inherited
label lists were comma-joined prose summaries. Nothing about turning them into quoted strings
would have revealed that `Laterals` was not actually in the asset.

### Alternative B — hand-write the inventory Markdown directly

Skip `build_inventory.py`; write the 280 rows and the header counts straight into the `.md`, as
most closed chapters in this repo were done.

| Pros | Cons |
|---|---|
| One artifact, no generator to keep in sync | Every count becomes hand-typed — the exact defect that made Ch11's header describe a 158-row table holding 282 rows |
| Matches how the other chapters were produced | ID contiguity becomes a manual invariant across 280 rows |
| Nothing extra in `scratch/` | Correcting one row means re-typing up to four restatements of every affected count |

**Rejected**, but it is a genuinely reasonable position — the doctrine's own remedy is "derive
every header count by re-parsing the finished table", which a hand-written file plus
`gate1_close.py` also satisfies. The generator goes further: it makes the counts *unable* to
drift rather than merely checked for drift, and it made the Fig 5.1 rect duplication surface as
an assertion failure instead of a stale number. The cost is a second artifact, mitigated by the
fact that `gate1_close.py` validates the `.md` on disk and never consults the generator.

---

## Suggested people to talk to

Being direct about this: **the repository has no second human to route you to.** `git log`
returns exactly two identities — `ayuu-1946` (you, the owner, 51 commits) and `v0`
(an agent, 73 commits) — and the Ch5 figure files, `check_pdf.py` and `neet_template.py` all
arrive in a single squashed merge, so per-file authorship carries no signal.

That matters more than usual here, because it means **the surrounding code is
largely AI-authored and has no human reviewer with independent context.** Two things are worth
your own eyes rather than a colleague's:

- **`check_pdf.py`'s `_extract_labels`, and checks A and C of the crop audit.** This change
  found that A and C are structurally blind to a fully-cropped label, and that a label row
  reading "none" would parse as a phantom label. Both are shared-infrastructure behaviours that
  every chapter depends on. You are the only person positioned to decide whether they should be
  hardened repo-wide or left documented.
- **The §5.9 heading judgement.** The source styles the 11 field labels (`Stem:`, `Calyx:`, …)
  *identically* to the three real sub-headings — all 10.5 pt `Bookman-Demi` — so typography
  cannot separate them and I applied an editorial rule instead. That rule moves the heading
  census, and it is a call about your book rather than about the code.

If you want a second reader, the highest-leverage thing to hand them is not this diff but
`GATE_1_PASS_1_SOURCE_MASTERY.md` §7 plus the `gate1_close.py` output — the gate is small enough
to audit end to end in one sitting.

---

## Quiz

Five questions. They are meant to be answerable only if you actually read the change.

<details>
<summary><b>1.</b> The inherited three-part crop audit reported clean, yet 12 of 17 crops carried a defect. Why did checks A and C both miss <code>Laterals</code>?</summary>

- **(a)** The audit was run before the assets were generated, so it measured stale rectangles.
- **(b)** Both checks discount text-layer words: A only flags a word *partly* inside the rect, and C deletes any dark pixel a word explains — so a label wholly outside the rect is invisible to both. ✅
- **(c)** `Laterals` is vector artwork with no text-layer entry, so neither check could see it.
- **(d)** The threshold was set too high, so the label's grey fell below the detection floor.

**(b) is correct.** The two checks are complementary for *partial* clipping and jointly blind to
*total* clipping. `Laterals` began at `x=63.1` and the crop at `x=78`, so nothing grazed the
boundary and every pixel it produced was explained by a text-layer word.

**(c) is wrong and worth pausing on** — it is true of Fig 5.10's `Gynoecium`, which *is* baked
into raster artwork, but `Laterals` is in the text layer at a known bbox. That is what makes it
the sharper example: the audit had the coordinates and still could not use them.

**(a)** is wrong; the audit ran against the committed rects. **(d)** confuses this with check C's
`DARK=110` threshold, which is not what failed.
</details>

<details>
<summary><b>2.</b> A union of <code>page.get_drawings()</code> rects put Fig 5.14's right edge at <code>x=299.9</code>. What is actually there, and why does 23 pt of error matter so much?</summary>

- **(a)** A clipping path around the plate; the error is harmless because the crop is padded anyway.
- **(b)** NCERT's watermark, drawn as vector strokes across the page; it matters because the neighbouring prose column starts at `x=303.1`, so a padded rect bleeds body text. ✅
- **(c)** The figure's leader lines, which extend beyond the visible artwork.
- **(d)** An off-page raster placement returned by `get_image_info()`.

**(b) is correct.** The plate's real ink ends at `x=276.9`, so the phantom 23 pt consumed the
entire 26-point gap to the prose column — and the first re-pin, which trusted it, produced an
asset with fragments of §5.7.1's prose down the right-hand side.

**(a)** is the seductive wrong answer: padding is exactly what converts a small measurement error
into a bleed. **(c)** is wrong — leader lines are inside the ink bbox. **(d)** describes a
different real hazard on page 11, but not this one.
</details>

<details>
<summary><b>3.</b> Six of Ch5's plates carry no in-figure labels. Why do they get <em>no</em> <code>figure-labels</code> row rather than a row recording that fact?</summary>

- **(a)** Because check 6 requires at least one label per figure, so an empty row fails the build.
- **(b)** Because `_extract_labels` matches any row beginning "Figure labels" and, finding no quoted strings, splits the remainder on `;` — so "Figure labels: none" parses as a phantom label. ✅
- **(c)** Because label-free figures are not real figures and are excluded from the manifest.
- **(d)** Because the row would be counted twice, once by check 6 and once by check 7.

**(b) is correct**, and the fallback branch is the whole point — it exists to accept
unquoted, semicolon-separated labels, which makes it hostile to explanatory prose in the same
cell. Their emptiness is recorded in the manifest prose instead, with each confirmed by opening
the asset.

**(c)** is wrong: all 17 are in the manifest with `Mono: yes`/`Verified: yes`. **(a)** inverts
the real behaviour — check 6 *warns* when it finds no label rows at all. **(d)** describes the
Ch12 doubling defect, which came from restating the matrix as a second table.
</details>

<details>
<summary><b>4.</b> §5.5.1.4 names six placentation types but explains five, so exercise Q7 cannot be answered exhaustively from the chapter. Why is Q7 classified COVERED rather than GAP?</summary>

- **(a)** Because five of six types are described, which clears the coverage threshold.
- **(b)** Because Figure 5.12 supplies the sixth type visually, so the fact is present.
- **(c)** Because answering it would require defining "central placentation" from outside this chapter, which Rule 5 forbids — so the shortfall is logged as a source inconsistency instead. ✅
- **(d)** Because Rule 2 only applies to terms the exercises introduce, not ones the body introduces.

**(c) is correct.** The two rules pull against each other here: Rule 2 wants the gap closed,
Rule 5 forbids importing the fact needed to close it. Rule 5 wins, and the finding is recorded
as `SRC-1` with an instruction that Pass 2 reproduce the six-name list verbatim and *not*
"correct" it to five.

**(b)** is factually wrong — Fig 5.12 figures exactly the five described types. **(a)** invents a
threshold; Rule 2 is binary. **(d)** is wrong: Q7 assumes "the various types", and the body's own
list is what makes the answer incomplete.
</details>

<details>
<summary><b>5.</b> Gate 1 closed green. Why did the repository's "Done" tally stay at 24 / 32?</summary>

- **(a)** Because Gate 1 closure is provisional until Gate 2 confirms the label parse.
- **(b)** Because the tally counts only chapters with Gate 3 closed, and Ch5 has no script, no PDF and 280 unticked rows — and the total was re-derived by parsing the ✅ rows rather than incremented. ✅
- **(c)** Because the Ch17 leading-space fix removed a chapter from the count, offsetting Ch5.
- **(d)** Because Ch5 was already counted when session `1-F` ran in the earlier task.

**(b) is correct**, and both halves matter. "Done" requires Gate 3 — this is the false-closure
failure that let Ch9 ship defective twice — and roll-ups must be *derived* rather than
incremented, which is how Ch13 ended up with a header saying `9/32` above a footer saying `4/13`.

**(c)** is a trap: the leading-space fix changed no status. It made a *strict machine parse*
return 24/32 instead of 23/31, bringing the parse into agreement with an already-correct header.
**(a)** is wrong — the label parse is validated *at* Gate 1, by importing `_extract_labels`
directly. **(d)** is wrong; `1-F` produced no gate closure.
</details>
