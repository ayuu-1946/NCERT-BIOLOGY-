"""Machine-derive Gate-1a counts from the Ch4 inventory Facts table.

Re-parses the finished Facts table (never a hand tally): row count, ID
contiguity F001..FNNN, Type histogram, per-section census, and runs
check_pdf.py's own _extract_labels to confirm 0 labels / 0 phantom rows
before 1-F. Prints everything needed to update the inventory metadata.
"""
import re, sys, importlib.util
from collections import Counter, OrderedDict

INV = "notes/class 11/Ch4_AnimalKingdom/Ch4_AnimalKingdom_inventory.md"

# import check_pdf.py's real _extract_labels
spec = importlib.util.spec_from_file_location("check_pdf", "check_pdf.py")
cp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cp)

text = open(INV, encoding="utf-8").read()

# Parse only genuine Facts rows: | Fxxx | section | type | wording | tick |
rows = []
for line in text.splitlines():
    s = line.strip()
    if not s.startswith("|"):
        continue
    cells = [c.strip() for c in s.strip("|").split("|")]
    if len(cells) < 4:
        continue
    if re.fullmatch(r"F\d{3}", cells[0]):
        rows.append((cells[0], cells[1], cells[2], cells[3]))

ids = [r[0] for r in rows]
nums = [int(i[1:]) for i in ids]

print("== ROW COUNT ==")
print("Facts rows parsed:", len(rows))

print("\n== ID CONTIGUITY ==")
dupes = [i for i, c in Counter(ids).items() if c > 1]
lo, hi = min(nums), max(nums)
missing = sorted(set(range(lo, hi + 1)) - set(nums))
print(f"ID range: F{lo:03d}..F{hi:03d}")
print("duplicates:", dupes or "none")
print("gaps:", [f"F{n:03d}" for n in missing] or "none")
print("contiguous & unique:", (not dupes and not missing and len(rows) == hi - lo + 1))

print("\n== TYPE HISTOGRAM (machine-grouped, case-sensitive) ==")
th = Counter(r[2] for r in rows)
for t, n in th.most_common():
    print(f"  {t}: {n}")
print("  TOTAL:", sum(th.values()))
casing = {}
for t in th:
    casing.setdefault(t.lower(), set()).add(t)
splits = {k: v for k, v in casing.items() if len(v) > 1}
print("  casing splits:", splits or "none")

print("\n== PER-SECTION CENSUS (facts/heading/opener split) ==")
def section_hist(pred):
    h = OrderedDict()
    for _id, sec, typ, _w in rows:
        if pred(typ):
            h[sec] = h.get(sec, 0) + 1
    return h

for label, pred in [
    ("ALL types", lambda t: True),
    ("facts-only (excl heading/opener)", lambda t: t not in ("heading", "opener")),
    ("heading-only", lambda t: t == "heading"),
    ("opener-only", lambda t: t == "opener"),
]:
    h = section_hist(pred)
    total = sum(h.values())
    print(f"\n  [{label}] total={total}")
    print("   ", ", ".join(f"{k}={v}" for k, v in h.items()))

print("\n== LABEL PARSER (check_pdf._extract_labels) ==")
labels = cp._extract_labels(text)
fig_ids = sorted({fid for fid, _ in labels})
print("label rows returned:", len(labels))
print("distinct figure ids:", len(fig_ids), fig_ids or "none")
print("phantom 'Fig #' row:", any(f.strip() in ("Fig #", "Fig") for f in fig_ids))
