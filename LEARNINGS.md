# Learnings

Running log of non-obvious findings from building/fixing chapter PDFs. Add new entries at the top of the relevant section. Keep entries short and actionable — link to the exact file/line pattern, not a narrative.

## Figure extraction / crop auditing

### The three-part crop audit is structurally blind to a label that was cropped away entirely
Found on Ch5 Morphology, where the inherited audit was green and the inherited tracker
recorded Fig 5.2's `Laterals` label as "intentionally retained" — the asset in fact rendered
it as "erals".

Both text-based checks discount text-layer words:
- **check A (word grazing)** only reports a word it can see is *partly* inside the rect;
- **check C (border-band ink)** deletes any dark pixel that a text-layer word explains.

A label that falls *outside* the rect therefore grazes no boundary and leaves no unexplained
ink. Both checks pass, and the label is simply gone. On Ch5, **12 of 17 inherited crops carried
a defect** — 8 clipping artwork or a label, 4 cutting the caption mid-glyph — and the audit was
green on all of them.

**There is no mechanical substitute — open every rendered asset and read it.** This is why
§4.4 Step 3 makes the visual pass mandatory rather than a spot-check, and why session `1-F`
gets its own context budget: when context runs short the harvest silently degrades to text
extraction, which returns an empty label set that passes Gate 1 and check 6 trivially.

A cheap catch for the *specific* case of a clipped label: compare the text-layer bbox of every
word the caption/label set expects against the rect, rather than only the words already inside
it.

### NCERT's page watermark is vector artwork, so `get_drawings()` mis-measures every figure
The diagonal "not to be republished" and © marks are drawn as vector strokes spanning the
whole page. `page.get_drawings()` therefore attributes them to whichever plate happens to sit
behind them, and a union of drawing rects reports a figure far wider than it is.

On Ch5 this put Fig 5.14's right edge at `x=299.9` when its real ink ends at `x=276.9` — and
the neighbouring prose column starts at `x=303.1`, so the phantom 23 pt left no room for a
margin and the "corrected" crop bled prose. Fig 5.12's union was 40 pt too wide the same way.

**Measure dark ink instead.** The watermark renders around grey 230–245; figure outlines and
label text sit below 215, so a threshold separates them cleanly:

```python
pix = page.get_pixmap(clip=band, dpi=200, alpha=False)
img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples).convert("L")
bbox = img.point(lambda v: 255 if v < 215 else 0, mode="L").getbbox()
```

See `scratch/ch5morph_gate1/ink_bbox.py`, and check **B2** in
`notes/class 11/Ch5_MorphologyOfFloweringPlants/audit_figures.py`, which supersedes the
drawings-based check B. Keep both so the disagreement stays visible.

Two corollaries:
- **A photograph's ink bbox under-reports its edge** (light background). Union the ink bbox
  with the raster `get_image_info()` bbox for photographic plates.
- **Rotated text spans belong to the watermark layer and do not render in place.** Exclude
  them from check A, or page 11's rotated duplicate `(a)` reports as a grazing word against
  Fig 5.12.

### A heading sweep keyed on styling can silently drop a whole heading level
On Ch5, 26 of 30 headings are cyan (`colour int 44783`), but `5.5.1.1 Calyx` through
`5.5.1.4 Gynoecium` are 10.5 pt `Bookman-LightItalic` in `colour int 7171953`, **each drawn
five times** to fake a bold weight. A sweep keyed on the heading colour returns 26 and looks
plausible — while having dropped the entire fourth level of the flower section.

Ch19 hit the same class via inconsistent heading *font names*. **Do not derive the heading set
from styling alone**; walk the headings as their own list (session `1-H`) and reconcile against
the chapter's contents box.

## ReportLab / `neet_template.py` pagination

### Nesting `KeepTogether` around `heading()` breaks pagination
`heading()` in `neet_template.py` already returns `KeepTogether([CondPageBreak(...), banner])`.
If you wrap that return value inside **another** `KeepTogether(...)` (e.g. to bind a whole
section — heading + bullets + figure — onto one page), the nested `CondPageBreak` reports a
huge sentinel height back to the outer `KeepTogether`'s `wrap()` call. ReportLab then believes
the whole block can never fit on the current page and pushes it to the next page, even when
there is plenty of free space (this produced a half-empty page in Ch4_AnimalKingdom).

**Fix:** don't nest `KeepTogether` around a `heading()` call. Append `heading(...)` and the
following bullets/paragraphs directly to `story` (unwrapped). Only wrap the *tail* of a section
(e.g. the last paragraph + the figure that must not orphan) in its own flat `KeepTogether`.

### `figure()` already returns `KeepTogether` — don't nest it either
`figure()` returns `KeepTogether([framed_image_table, caption_paragraph])`. Wrapping that
return value inside a second `KeepTogether` (e.g. `KeepTogether([last_bullet, figure(...)])`)
has the same mis-measurement problem — the figure gets orphaned to the next page instead of
staying with the preceding bullet.

**Fix:** splice the figure's *inner* flowables into one flat `KeepTogether` instead of nesting
the whole `figure()` result:
```python
_fig = figure("fig_x.png", "<b>Fig. x</b> - caption", max_width_cm=10.5)
story.append(KeepTogether([
    b1("<b>Examples:</b> ..."),
    *_fig._content,   # splice, don't nest
]))
```

### General rule
Never put a `KeepTogether` result inside another `KeepTogether`. Always flatten to a single
list of plain flowables (`Paragraph`, `Table`, `Image`, etc.) before wrapping once.

### Diagnosing a pagination gap
When a block unexpectedly jumps to the next page and leaves free space behind:
1. Render both pages with `pymupdf` to `/tmp/agent-browser/*.png` and inspect visually.
2. Use `pdfplumber` to get `pg.extract_words()` and find the max `bottom` y-value of content
   on the page with the gap — compare against the frame's usable height to confirm there was
   room.
3. Independently measure the "stuck" block's height with a standalone `wrap(FRAME_WIDTH, 10000)`
   call on its flowables (see scratch measurement pattern used in Ch4 session) to prove it
   should fit — this isolates whether the issue is real overflow vs. a `KeepTogether` nesting
   bug.

## Figure sizing (Ch4_AnimalKingdom)

- Fig 4.16: reduced from `max_width_cm=11.30` → `8.60` to fit alongside Table 4.1 on one page.
- Fig 4.17: reduced from `max_width_cm=4.37` → `3.50`.
- Fig 4.18: reduced from `max_width_cm=14.59` → `10.50` to fit the whole Cyclostomata section
  (heading + 5 bullets + figure) on a single page.
- Docx-derived figure sizes are a starting point, not gospel — when a section must be kept
  together on one page, shrink the figure rather than relying only on `PageBreak`/`KeepTogether`
  placement.

## Workflow

- Build venv lives at `/vercel/share/neetenv` (Python 3.13) with `reportlab`, `pdfplumber`,
  `pymupdf`, `Pillow` installed. Reuse it — don't reinstall per session.
- Verification loop for a chapter script change:
  1. Rebuild: `python "notes/class 11/Ch<N>_<Name>/Ch<N>_<Name>.py"`
  2. Map section → page with `pdfplumber` text search (`find(needle)` helper pattern).
  3. Render suspect pages with `pymupdf` at ~110 dpi to `/tmp/agent-browser/*.png` and view them.
  4. Run `python check_pdf.py "notes/class 11/Ch<N>_<Name>"` and confirm 0 fail / 0 warn before
     committing.
