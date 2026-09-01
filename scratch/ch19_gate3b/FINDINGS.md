# Ch19 Gate 3(b) — running findings log

Every entry is a *finding*, not yet a fix. Disposition is decided after the
bidirectional read, so that a defect and its cause are never confused.

## Re-derivation of the handoff (Gate 1 Closure rule 1)

All re-derived from disk this session under a freshly rebuilt `/vercel/share/neetenv`
(absent at session start — the expected §0.2 state): CPython 3.13.11, reportlab 5.0.1,
pymupdf 1.28.2, pdfplumber, Pillow 12.3.0.

| Claim carried in | Claim | Re-derived | Verdict |
|---|---|---|---|
| tracker / inventory | 218 rows `F001`–`F218`, contiguous, monotonic, 0 dupes | same | confirmed |
| tracker / inventory | 218/218 ticked | 218/218 | confirmed |
| inventory | type census sums to 218, all-lowercase values | 9 values, sums to 218 | confirmed |
| tracker | 7 label-bearing figures / 38 labels / no doubling / no phantom row | 7 / 38 / none / none | confirmed |
| tracker | 14 A4-upright pages, 7 mono images | 14 / all (595,842) / 7 | confirmed |
| inventory Gate 2 | rebuild content-identical to committed PDF | **YES** — 14 pp / 31,149 chars / 7 img / SHA `f4850a48c881f3b3` on both | confirmed |
| inventory Gate 2 | "31,137 chars, text SHA `08d68d03f8d3c05f`" | **31,149 / `f4850a48c881f3b3`** | **STALE — D1** |

Two of my own four initial "mismatches" were **measurement defects, not repo defects**,
and are recorded because the next agent will hit them too:

1. `check_pdf.py::_extract_labels(inv_text)` takes the inventory **text**. Passing
   the **path** returns `[]` silently — a green-looking empty result that would have
   let me "confirm" 0 labels. Asserted in the harness now.
2. A matrix-row sweep keyed on `startswith("Figure labels:")` finds only 3 of the 7
   rows, because four rows read `Figure (a) labels:` / `Figure (b) labels:`. The
   linter's own regex allows the `(x)` infix; a hand-rolled prefix test does not.
   Same family as the Ch19 Gate 1 finding that a name-based heading sweep silently
   dropped real headings.

## D1 — inventory Gate 2 record carries a fingerprint that no longer reproduces

**Status: confirmed documentation defect (metadata only, no content loss).**

The `## Gate 2 record` states the PDF is *"31,137 extracted characters, text SHA-256
(first 16) `08d68d03f8d3c05f`"*, and its reproducibility paragraph repeats both.
Neither pymupdf (31,149 / `f4850a48c881f3b3`) nor pdfplumber (31,422 /
`4297a27a6e8b6a98`) reproduces them, so this is not the Ch16-style
"different extractor, same bytes" case — the bytes really did change.

Cause, established from git rather than guessed: commit `957c1dd` ("update modDate
and filter length…") applied the two **Pass 3(a) D1** string fixes to the script and
rebuilt the PDF — `"SS19.2"` → `"Section 19.2"` and `"SS19.2.5"` → `"Section 19.2.5"`,
+6 characters each. 31,137 + 12 = **31,149**, exactly the count now on disk. The
delta is fully accounted for by the two documented fixes; nothing else moved.

So the Gate 2 record was true when written and was **not updated by the session that
changed the artefact it describes** — the same half-finished-handoff shape the tracker
records for Ch8/Ch13/Ch14/Ch18. Under Gate 3(b) rule 2 the disagreement *is* the defect.

Confirmed alongside: the leaked token is genuinely gone from delivered text
(`"SS19."` not present; `"Section 19.2 uses them"` present), so the Pass 3(a) fix
is real and verified in the PDF, not just in the script.

**Fix:** restate the fingerprint as **14 pp / 31,149 chars / 7 images / pymupdf text
SHA `f4850a48c881f3b3`**, *naming the extractor* (a char count without its extractor
is what made Ch16 ambiguous), and note the +12 provenance so the old number is
explained rather than silently overwritten.

## D2 — `CHAPTER_STATUS.md` still says Pass 3(a) has never run

**Status: confirmed documentation defect.** To be re-read and quoted exactly before fixing.

The Ch19 detailed section states Gate 3 is open with *"Pass 3(a) has seen only 5 of 14
pages and Pass 3(b) has never run"*, while the inventory carries a full `## Gate 3(a)
record` and the tracker's current-session note describes all 14 pages rendered and
inspected with three benign findings. Inventory + tracker agree with each other and
with disk; `CHAPTER_STATUS.md` is the stale one.

## Content findings (bidirectional read)

To be filled by the section-by-section read — direction 1 (inventory → script) and
direction 2 (source → inventory) — below.
