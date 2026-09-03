#!/usr/bin/env python3
"""1-Z machine validation for Ch4 Animal Kingdom inventory.
Re-derives row count, ID contiguity, Type histogram, and the _extract_labels
result (labelled figures + total label strings, doubling / phantom Fig # rows),
replicating check_pdf.py exactly."""
import re, sys, collections

INV = sys.argv[1] if len(sys.argv) > 1 else \
    "notes/class 11/Ch4_AnimalKingdom/Ch4_AnimalKingdom_inventory.md"

text = open(INV, encoding="utf-8").read()

# ---- Facts-table parse (same row logic as check_ticked) ----
rows = []
in_facts = False
for line in text.splitlines():
    low = line.strip().lower()
    if low.startswith("## "):
        in_facts = low.startswith("## facts")
        continue
    if not in_facts or not line.strip().startswith("|"):
        continue
    cells = [c.strip() for c in line.strip().strip("|").split("|")]
    if not cells or not re.match(r"[a-z]?\d{2,}", cells[0].lower()):
        continue
    rows.append(cells)

ids = [r[0] for r in rows]
print(f"Facts rows parsed: {len(rows)}")

# contiguity F001..FNNN
nums = [int(i[1:]) for i in ids if re.fullmatch(r"F\d+", i)]
dupes = [x for x, n in collections.Counter(ids).items() if n > 1]
lo, hi = min(nums), max(nums)
expected = set(range(lo, hi + 1))
gaps = sorted(expected - set(nums))
print(f"ID range: F{lo:03d}..F{hi:03d}  (expected {hi-lo+1} contiguous)")
print(f"Duplicate IDs: {dupes or 'none'}")
print(f"Gaps: {['F%03d'%g for g in gaps] or 'none'}")

# Type histogram (col index 2)
types = collections.Counter(r[2] for r in rows if len(r) > 2)
print("Type histogram:", dict(sorted(types.items(), key=lambda kv: -kv[1])))
# case-normalization assertion
lc = {t.lower() for t in types}
if len(lc) != len(types):
    print("!! Type casing split detected")
else:
    print("Type casing: single spelling per value (OK)")

# ---- _extract_labels replica (verbatim from check_pdf.py) ----
def extract_labels(inv_text):
    out = []
    for line in inv_text.splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 4:
            continue
        fig_id = cells[1] if len(cells) > 1 else "?"
        wording = cells[3]
        if re.match(r"figure(\s*\([a-z]\))?\s*labels", wording, re.I):
            quoted = re.findall(r'"([^"]+)"', wording)
            if not quoted:
                body = re.sub(r"^figure(\s*\([a-z]\))?\s*labels\s*:?", "", wording, flags=re.I)
                quoted = [p.strip() for p in body.split(";") if p.strip()]
            for lab in quoted:
                out.append((fig_id, lab))
    return out

labels = extract_labels(text)
figs = collections.Counter(f for f, _ in labels)
print(f"\n_extract_labels: {len(figs)} labelled figures, {len(labels)} individual label strings")
for f, n in figs.items():
    print(f"  {f}: {n}")
phantom = [f for f in figs if f.strip().lower().startswith("fig #") or set(f.strip()) <= set("- ")]
print(f"Phantom 'Fig #'/separator rows: {phantom or 'none'}")
# doubling check: any figure whose count is exactly 2x a plausible base is only a hint;
# real doubling shows as duplicate identical label lists — check duplicate label strings per fig
per_fig = collections.defaultdict(list)
for f, l in labels:
    per_fig[f].append(l)
doubled = {f: ls for f, ls in per_fig.items() if len(ls) != len(set(ls))}
print(f"Figures with duplicated label strings (doubling): {list(doubled) or 'none'}")
