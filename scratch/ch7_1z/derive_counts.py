"""Session 1-Z — Gate 1 count derivation and label-parse validation for Ch7.

Every number in the inventory header is produced here by re-parsing the finished
file (SUPREME COMMAND §6 step 10: "derive every count by re-parsing the finished
table -- never by hand tally"). The label check imports check_pdf.py's OWN
_extract_labels so Gate 1 is validated by the same parser Gate 2 will use, which
is the point of the "machine-checked gate" requirement.

Run:
  /vercel/share/neetenv/bin/python scratch/ch7_1z/derive_counts.py
"""

import importlib.util
import re
import sys
from collections import Counter
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
INV = REPO / "notes/class 12/Ch7_HumanHealthAndDisease/Ch7_HumanHealthAndDisease_inventory.md"


def load_check_pdf():
    """Import the repo-root linter as a module so we use its real parser."""
    spec = importlib.util.spec_from_file_location("check_pdf", REPO / "check_pdf.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def parse_rows(text):
    """Every F### row in the file, as (id, section, type, wording, ticked)."""
    rows = []
    for line in text.splitlines():
        s = line.strip()
        if not s.startswith("|"):
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if len(cells) < 4:
            continue
        if not re.fullmatch(r"F\d{3}", cells[0]):
            continue
        ticked = cells[4] if len(cells) > 4 else ""
        rows.append((cells[0], cells[1], cells[2], cells[3], ticked))
    return rows


def main():
    text = INV.read_text(encoding="utf-8")
    rows = parse_rows(text)
    ids = [r[0] for r in rows]
    nums = [int(i[1:]) for i in ids]

    print("=" * 66)
    print("GATE 1 DERIVATION - Ch7 Human Health and Disease")
    print("=" * 66)

    # --- contiguity ---
    dupes = [i for i, n in Counter(ids).items() if n > 1]
    lo, hi = min(nums), max(nums)
    missing = sorted(set(range(lo, hi + 1)) - set(nums))
    print(f"\n[rows]        total={len(rows)}  range=F{lo:03d}..F{hi:03d}")
    print(f"[contiguity]  duplicates={dupes or 'none'}  gaps={missing or 'none'}")
    contiguous = not dupes and not missing and len(rows) == hi - lo + 1
    print(f"[contiguity]  {'OK - contiguous, no gaps, no duplicates' if contiguous else 'FAIL'}")

    # --- type distribution, and casing normalisation ---
    types = Counter(r[2] for r in rows)
    print(f"\n[types]       {len(types)} distinct values")
    for t, n in sorted(types.items(), key=lambda kv: (-kv[1], kv[0])):
        print(f"              {n:>4}  {t}")
    bad_case = [t for t in types if t != t.lower()]
    print(f"[type-case]   {'OK - all lowercase' if not bad_case else 'FAIL mixed case: ' + str(bad_case)}")

    # --- per-session blocks ---
    def block(lo_, hi_):
        return [r for r in rows if lo_ <= int(r[0][1:]) <= hi_]

    facts = block(1, 276)
    heads = [r for r in rows if r[2] == "heading"]
    opens = [r for r in rows if r[2] == "opener"]
    labels_rows = [r for r in rows if r[2] == "label"]
    summary_unique = [r for r in rows if "SUMMARY-UNIQUE" in r[3]]

    print(f"\n[1-S facts]   F001..F276  -> {len(facts)} rows")
    print(f"[1-H heading] {len(heads)} rows  {heads[0][0]}..{heads[-1][0]}")
    numbered = [r for r in heads if re.match(r'^"7\.\d', r[3])]
    print(f"              numbered={len(numbered)}  unnumbered={len(heads) - len(numbered)}"
          f"  ({len(numbered)} + {len(heads) - len(numbered)} = {len(heads)})")
    print(f"[1-O opener]  {len(opens)} rows  {opens[0][0]}..{opens[-1][0]}")
    print(f"[1-Z folded]  {len(summary_unique)} SUMMARY-UNIQUE rows: "
          f"{', '.join(r[0] for r in summary_unique)}")
    print(f"[1-F labels]  {len(labels_rows)} label rows  "
          f"{labels_rows[0][0]}..{labels_rows[-1][0]}")

    # --- ticks: Gate 1 requires NONE ticked (ticking is Pass 2) ---
    ticked = [r[0] for r in rows if r[4].strip()]
    print(f"\n[ticks]       {len(ticked)} rows ticked "
          f"({'OK - none, as required before Pass 2' if not ticked else 'UNEXPECTED: ' + str(ticked[:8])})")

    # --- THE machine-checked Gate 1 requirement: real _extract_labels ---
    cp = load_check_pdf()
    parsed = cp._extract_labels(text)
    figs = sorted({f for f, _ in parsed})
    print(f"\n[_extract_labels] parsed {len(parsed)} label strings across {len(figs)} figures")
    print(f"              figures: {', '.join(figs)}")
    per = Counter(f for f, _ in parsed)
    for f in figs:
        print(f"              {per[f]:>3}  {f}")

    phantom = [f for f in figs if not re.match(r"^Fig 7\.\d+$", f)]
    print(f"[phantoms]    {'OK - none' if not phantom else 'FAIL: ' + str(phantom)}")
    dupe_labels = [f"{f}/{l}" for (f, l), n in Counter(parsed).items() if n > 1]
    print(f"[doubling]    {'OK - no label parsed twice' if not dupe_labels else 'FAIL: ' + str(dupe_labels)}")

    EXPECT_LABELS, EXPECT_FIGS = 21, 4
    ok_labels = len(parsed) == EXPECT_LABELS and len(figs) == EXPECT_FIGS
    print(f"[expected]    {EXPECT_LABELS} labels / {EXPECT_FIGS} labelled figures -> "
          f"{'OK' if ok_labels else 'FAIL'}")

    # --- verdict ---
    checks = {
        "ID contiguity": contiguous,
        "Type casing normalised": not bad_case,
        "No premature ticks": not ticked,
        "No phantom figure rows": not phantom,
        "No label doubling": not dupe_labels,
        "Label/figure counts as expected": ok_labels,
        "29 heading rows": len(heads) == 29,
        "28 opener rows": len(opens) == 28,
        "11 label rows": len(labels_rows) == 11,
        "346 rows total": len(rows) == 346,
    }
    print("\n" + "=" * 66)
    for k, v in checks.items():
        print(f"  {'PASS' if v else 'FAIL'}  {k}")
    allok = all(checks.values())
    print("=" * 66)
    print(f"GATE 1 DERIVATION: {'ALL GREEN' if allok else 'RED'}")
    return 0 if allok else 1


if __name__ == "__main__":
    sys.exit(main())
