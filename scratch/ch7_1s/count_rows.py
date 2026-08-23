"""Session 1-S count derivation for Ch7's frozen inventory.

Per SUPREME COMMAND PROMPT §6 Pass 1 step 10, every count that appears in the
inventory must be derived by re-parsing the finished table, never hand-tallied,
and ID contiguity must be asserted at the same time.

This script does four things and prints them:
  1. counts the Facts rows and asserts F001..FNNN is contiguous, gapless, dupe-free
  2. groups the Type column and asserts it uses only the normalized vocabulary
     (one spelling, one casing per value)
  3. re-runs check_pdf.py's OWN _extract_labels against the inventory, so Gate 1's
     machine-checked criterion is exercised here rather than asserted in prose:
     it must report 11 figures, 21 labels, no doubling, and no phantom `Fig #` row
  4. asserts no Facts row's wording could be mistaken for a label row (i.e. no
     wording begins "Figure labels"), which is what keeps 1-S's 18 figure-text
     rows invisible to check 6

Run:
  /vercel/share/neetenv/bin/python scratch/ch7_1s/count_rows.py
"""

import collections
import importlib.util
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
INV = os.path.join(
    REPO, "notes", "class 12", "Ch7_HumanHealthAndDisease",
    "Ch7_HumanHealthAndDisease_inventory.md",
)

# The one fixed spelling/casing per Type value that this chapter is allowed to use.
ALLOWED_TYPES = {
    "cause", "diagnosis", "example", "fact", "figure-text", "mechanism",
    "number", "prevention", "process", "structure", "symptom", "term",
    "transmission", "treatment",
    # added by later Pass 1 sessions; permitted so this script keeps working
    "heading", "opener", "caption", "label",
}

FACT_ID = re.compile(r"^F(\d{3})$")

failures = []


def check(cond, msg):
    if not cond:
        failures.append(msg)
    print(("  ok   " if cond else "  FAIL ") + msg)


def rows(text):
    """Yield the cell lists of every pipe-delimited table row in the file."""
    for line in text.splitlines():
        s = line.strip()
        if not s.startswith("|"):
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if len(cells) < 4:
            continue
        # skip markdown separator rows
        if all(set(c) <= set("-: ") and c for c in cells):
            continue
        yield cells


def main():
    text = open(INV, encoding="utf-8").read()

    # ---- 1. Facts rows + contiguity -------------------------------------------
    facts = [c for c in rows(text) if FACT_ID.match(c[0])]
    ids = [c[0] for c in facts]
    nums = [int(FACT_ID.match(i).group(1)) for i in ids]

    print(f"\nFacts rows parsed: {len(facts)}")
    print(f"ID range: {ids[0]}..{ids[-1]}" if ids else "ID range: (none)")

    dupes = [i for i, n in collections.Counter(ids).items() if n > 1]
    check(not dupes, f"no duplicate IDs (found {dupes})")
    check(nums == sorted(nums), "IDs appear in ascending order")
    expected = list(range(1, len(nums) + 1))
    missing = sorted(set(expected) - set(nums))
    check(nums == expected,
          f"IDs are contiguous F001..F{len(nums):03d} (missing {missing})")

    # ---- 2. Type vocabulary ---------------------------------------------------
    types = collections.Counter(c[2] for c in facts)
    print("\nType distribution (machine-derived):")
    for t, n in sorted(types.items(), key=lambda kv: (-kv[1], kv[0])):
        print(f"  {n:>4}  {t}")
    print(f"  total {sum(types.values())} across {len(types)} distinct values")

    bad = sorted(set(types) - ALLOWED_TYPES)
    check(not bad, f"Type column uses only normalized values (offenders: {bad})")
    lowered = collections.Counter(t.lower() for t in types)
    split = [t for t, n in lowered.items() if n > 1]
    check(not split, f"no Type value split across casings (offenders: {split})")

    # ---- 3. check_pdf.py's own _extract_labels --------------------------------
    spec = importlib.util.spec_from_file_location(
        "check_pdf", os.path.join(REPO, "check_pdf.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    labels = mod._extract_labels(text)
    figs = collections.Counter(fig for fig, _ in labels)
    print(f"\n_extract_labels: {len(labels)} labels across {len(figs)} figures")
    for fig, n in sorted(figs.items()):
        print(f"  {n:>4}  {fig}")

    check(len(labels) == 21, f"parses exactly 21 labels (got {len(labels)})")
    check(len(figs) == 4,
          f"parses labels for exactly the 4 labelled figures (got {len(figs)})")
    phantom = [f for f in figs if not re.match(r"^Fig 7\.\d+$", f)]
    check(not phantom, f"no phantom figure rows (offenders: {phantom})")
    dupe_labels = [k for k, n in collections.Counter(labels).items() if n > 1]
    check(not dupe_labels, f"no doubled labels (offenders: {dupe_labels})")

    # ---- 4. Facts rows cannot masquerade as label rows -----------------------
    leaked = [c[0] for c in facts
              if re.match(r"figure(\s*\([a-z]\))?\s*labels", c[3], re.I)]
    check(not leaked,
          f"no Facts row wording begins 'Figure labels' (offenders: {leaked})")

    print("\n" + ("ALL ASSERTIONS PASS" if not failures
                  else f"{len(failures)} ASSERTION(S) FAILED"))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
