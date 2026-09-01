# Chapter 11 — Photosynthesis in Higher Plants — Operator decisions record

Authoritative record of the **operator-directed deviations** for this chapter: the three
figure resizes, the deliberate non-embedding of Figure 11.1, and the deliberate
non-answering of the non-gap exercises.

This file exists because all three are decisions a later auditor would otherwise read as
**defects**: a figure rendered smaller than the column, a manifest figure absent from the
PDF, and exercises with no answer. Each is intentional, each was ordered by the operator,
and none of them is an extraction failure or a coverage miss. `Ch11_...py` comments point
here rather than restating the reasoning at three call sites.

Nothing in this file is reader-facing. Per **Rule 6** none of it appears in the PDF — the
PDF carries notes, not meta-notes about itself.

**Governing spec:** `SUPREME COMMAND PROMPT.md` — §4.4 (figures), Rule 2 (exercise gap),
Rule 6 (no meta notes in the PDF).

---

## §1 Why three figures were resized — the pagination budget

Ordered in the review session after the operator eyeballed the rendered PDF. The
complaint was structural, not aesthetic: **§11.8 (the C4 pathway) was being torn across
three pages by its own figure.**

State before the change:

| Page | Content | Problem |
|---|---|---|
| 11 | Fig 11.8 (Calvin cycle) + stages 1 and 2 | stage **(3) Regeneration** pushed off |
| 12 | §11.8 C4 pathway text, ending at "identify the C4 plants" | text stopped at y=588.8 of a y≈792 frame — **≈203 pt of dead white space** |
| 13 | **Fig 11.9 alone**, plus its label paragraph | a figure occupying a page by itself |
| 14 | rest of §11.8, then §11.9 Photorespiration | C4 content resumed two pages after it started |

The dead space on page 12 was not a spacing bug. `neet_template.figure()` wraps image +
caption in `KeepTogether`, so the Fig 11.9 block is indivisible; at 10.0 cm it measured
≈385 pt (347.9 pt image + 10 pt frame padding + caption + gap) and could not fit in the
203 pt left on page 12. ReportLab therefore did the only thing it could — moved the whole
block to a fresh page — and the 203 pt stayed blank.

**Why shrinking Fig 11.9 alone could not fix it.** Fitting the block into the existing
203 pt tail needs an image height of ≈163 pt, i.e. a render width of **≈4.7 cm** — a
two-cell diagram with 16 in-figure labels reduced to under half width. That fails §4.4
Step 3(c) (legible at print size) and the photocopier rule in §5, so it was rejected.

**The budget that does work.** Shrinking Fig 11.8 pulls text *up* onto page 11, and every
point it frees is a point added to page 12's tail. With `h8`/`h9` the rendered image
heights in points:

```
required:  h9 + ~40 (frame padding + caption + gap)  <=  203 + (346.1 - h8)
therefore: h8 + h9 <= ~509 pt        (it was 346.1 + 347.9 = 694 pt)
```

Chosen point: **h8 = 251, h9 = 257, sum 508 pt** — inside the budget by 1 pt of slack,
which is why both figures had to move and why neither was cut further than needed. This
is the operator's stated fallback ("reduce 11.8 so the regeneration stage fits, then 11.9
fits on the C4 pathway page itself"), reached because the primary option was not
achievable at a legible size.

## §2 Figure size ledger

Referenced from the `# LAYOUT` comments in `Ch11_PhotosynthesisInHigherPlants.py`.

| Fig | `max_width_cm` before → after | Rendered w × h (pt) before → after | Linear scale | Why |
|---|---|---|---|---|
| 11.8 Calvin cycle | 10.5 → **7.6** | 297.6 × 346.1 → 215 × 251 | 0.72 | frees 95 pt so stage (3) Regeneration rejoins its section, and pays for 11.9's move |
| 11.9 Hatch & Slack | 10.0 → **7.4** | 283.5 × 347.9 → 210 × 257 | 0.74 | block now fits the tail of the C4 page instead of taking a page of its own |
| 11.10 Light-intensity graph | 8.0 → **6.2** | 226.8 × 196.0 → 176 × 152 | 0.78 | **size order, not a pagination fix** — see below |

Fig 11.10 was resized on direct instruction, not to solve a break. It is the cheapest
figure in the chapter to shrink: two axis names and the points A–E, versus 16 labels in
11.9. It buys §11.10.1 more text on its opening page.

**What did NOT change.** Only the `max_width_cm` argument at three call sites. No asset was
re-extracted or re-cropped, no crop rectangle moved, no caption was reworded, no inventory
row was altered, and `neet_template.py` was not touched. Every asset is still the same
300 dpi `mode=L` file with the same pixels; `figure()` scales at draw time and its
`min(width_cm * cm, natural_w)` no-upscale cap is unaffected, since all three moves are
downward. Effective print resolution therefore *rose* in all three figures.

## §3 Figure 11.1 — deliberate operator omission, NOT an extraction failure

**Decision:** `assets/fig_11_1.png` (Priestley's experiment, source p. 4) is extracted,
monochrome, verified, listed in the manifest — and **deliberately never embedded in the
PDF**, on the operator's judgement that the plate carries no teaching value for NEET.

**This is the point that needs the loudest documentation**, because §4.4 Step 3 and §5
recognise only two states for a figure — *embedded*, or *failed extraction and therefore
flagged in the PDF under "Figures requiring manual attention"* — and instruct: "never skip
a figure silently." Figure 11.1 is neither. It is a **third state**: extraction succeeded
completely, and the figure is dropped by choice.

Consequences, all deliberate:

- It is **not** flagged in the PDF under "Figures requiring manual attention". That heading
  means *"a diagram you should have is missing, go find it"*. Figure 11.1 is not missing by
  accident and a student is not being deprived of anything, so flagging it would be a false
  alarm — and per Rule 6 the PDF does not explain itself.
- Its asset stays on disk and stays in the manifest. The extraction is good work and is
  reproducible; the omission is a *placement* decision and is reversible by adding one
  `figure("fig_11_1.png", ...)` call.
- Its label row **`F271`** — the four bare panel markers `(a)`, `(b)`, `(c)`, `(d)` — is not
  written into running text *as figure labels*. Bare panel markers carry no fact; there is
  nothing to lose. `check_pdf.py` check 6 still reports **116/116 labels present**.
- **No factual coverage is lost.** Every fact in the Priestley plate survives in prose at
  `F024`–`F029` in §11.2: the bell jar, the candle going out, the mouse suffocating, the
  mint plant, and the "plants restore to the air" hypothesis. This is the test that makes
  the omission safe, and it is the reason the decision is defensible rather than merely
  permitted — §4.4's rule that the text must stand alone even if a figure is illegible is
  satisfied *a fortiori* when the figure is absent.

The general form of this state is written into the spec at §4.4 Step 3 so the next chapter
does not have to re-derive it.

## §4 Exercises — non-gap questions are deliberately unanswered

**Decision:** the appendix answers **only** the 4 exercise-gap items (Ex. 1, 5, 6, 7). The
other 5 of the 9 exercises are **intentionally left unanswered** because their content is
already taught in the chapter body.

This is not a gap in the notes — it is **Rule 2 working as specified**. Rule 2 and §5 item
9 require the "Terms used in the exercises" appendix to contain *only* the GAP questions,
and explicitly forbid "a walk-through of all N exercises". A reader who can answer Ex. 2,
3, 4, 8 or 9 from the body is exactly the outcome the notes are built for; printing an
answer key beside the text that already answers it would duplicate the chapter and bury
the four items that genuinely need help.

The four that are answered, and why each is a real gap (full reasoning in the inventory's
*Exercise-gap terms* table):

| Ex. | The gap — what the body never states outright |
|---|---|
| 1 | that C3 vs C4 **cannot** be told apart externally; the body gives only internal Kranz-anatomy criteria |
| 5 | that chlorophyll *a* is indispensable — the body names *b* as accessory but never says *b* alone cannot run photosynthesis |
| 6 | the pigment **stability ordering** — chlorophyll degrades in darkness faster than carotenoids |
| 7 | why shade leaves are darker green — more chlorophyll per unit area |

Each was re-confirmed against the extracted source in session `1-Z`. So the count is
recorded plainly: **9 exercises, 4 answered by design, 5 unanswered by design, 0 overlooked.**

## §5 Verification of the resize

Rebuilt with `/vercel/share/neetenv/bin/python Ch11_PhotosynthesisInHigherPlants.py`, then
re-measured from the PDF with PyMuPDF (`get_image_info()` for image boxes, `get_text("blocks")`
for text extents) and inspected page by page as rendered images.

| Goal | Result |
|---|---|
| Stage (3) Regeneration on Fig 11.8's page | ✅ page 11 now carries Fig 11.8 + all three stages |
| Fig 11.9 on the C4 pathway page | ✅ page 12, image box y = 500–757, under the C4 text |
| No figure alone on a page | ✅ the figure-only page is gone |
| Content above §11.9 Photorespiration contiguous | ✅ §11.8 runs pages 10→13; the Photorespiration banner is followed by its own content on page 13 |
| Dead white space closed | ✅ page-12 text extent 588.8 → 778 pt; pages 11–15 all end in the 761–796 pt band |
| Figures still legible | ✅ all three opened and read at render size; in-figure labels of 11.9 (the dense one) still resolve |
| Page count | 17 pp, unchanged — the reclaimed space absorbed the reflow rather than adding a page |

`check_pdf.py` after the rebuild: check 6 **116/116 labels**, check 8 **17/17 A4 portrait**,
check 9 **88 banners, 0 orphaned headings**, checks 1/2/3/5 pass.

**Pre-existing linter state, untouched by this change and not introduced by it:** check 7
fails (inventory rows show `[ ]`, so 0/270 ticked — a Pass 2 bookkeeping debt in the
inventory `.md`, not a PDF defect) and check 4 raises its usual benign WARN, which fires on
inventory rows whose own text contains the words *portrait/photo*. Both were failing in
exactly this form before the resize. The chapter's only embedded human-subject content
remains none: the Melvin Calvin profile is text-only from `F004`–`F010`/`F246`.
