TR = "notes/class 12/Ch2_HumanReproduction/Ch2_TRACKER.md"
t = open(TR).read()

old = """**Full replacement chapter/PDF gate:** Not started; no chapter notes PDF was requested or generated."""

new = """**Full replacement chapter/PDF gate:** In progress.

## Pass 1 / Gate 1 — GREEN (frozen inventory)

Pass 1 ran as five discrete sessions (1-S source read + facts, 1-H heading sweep, 1-O opener sweep, 1-F figure harvest, 1-Z gaps/summary/freeze). The frozen inventory `Ch2_HumanReproduction_inventory.md` is machine-validated:

- **220 rows**, IDs contiguous `F001..F220` — no gaps, no duplicates, no letter-suffixed IDs.
- `Type` column normalized to one vocabulary: 1 title, 8 openers, 10 headings (7 numbered + 3 unnumbered: Menstrual Hygiene, SUMMARY, EXERCISES), 14 captions, 187 content rows.
- **Figure-label matrix validated with `check_pdf.py`'s own `_extract_labels`:** 14 distinct figure rows (2.1a, 2.1b, 2.2, 2.3a, 2.3b, 2.4–2.12), 131 labels, **no doubling, no phantom rows.** Each caption row carries a unique figure number in the Section column so no two figures collapse.
- Every header/census count matches a re-parse of the table; each census total is derivable from the list beside it.
- All 14 figures marked `Mono: yes`, `Verified: yes`.
- 3 SUMMARY-UNIQUE facts folded into body rows F076, F077, F204; 2 exercise gaps (Q20 twins, Q21 litter) have a planned appendix home.

Gate 1 is green; Pass 2 (build the script from the frozen inventory + `check_pdf.py` render→lint loop) may begin.
Validation scripts live in `scratch/ch2_gate1/` (`validate_gate1.py`)."""

assert t.count(old) == 1
t = t.replace(old, new)
open(TR, "w").write(t)
print("tracker updated")
