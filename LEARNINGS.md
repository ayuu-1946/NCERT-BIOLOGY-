# Learnings

Running log of non-obvious findings from building/fixing chapter PDFs. Add new entries at the top of the relevant section. Keep entries short and actionable — link to the exact file/line pattern, not a narrative.

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
