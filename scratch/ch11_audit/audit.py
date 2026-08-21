#!/usr/bin/env python3
"""Gate 1 third re-audit for Ch11 Organisms and Populations.

Direction 1: inventory -> source. Every quoted string in every Facts row must be
findable in the source text. Also re-counts rows, IDs, types and figure labels.
"""
import re
import sys
import unicodedata

INV = ("notes/class 12/Ch11_OrganismsAndPopulations/"
       "Ch11_OrganismsAndPopulations_inventory.md")
SRC = "scratch/ch11_audit/source_clean.txt"


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s)
    # unify quotes and dashes
    for a, b in [("\u2018", "'"), ("\u2019", "'"), ("\u201c", '"'),
                 ("\u201d", '"'), ("\u2013", "-"), ("\u2014", "-"),
                 ("\u2212", "-"), ("\u00a0", " ")]:
        s = s.replace(a, b)
    s = s.lower()
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def variants(s: str):
    """Source may hyphenate across line breaks and space out sub/superscripts."""
    n = norm(s)
    yield n
    yield n.replace("- ", "-")     # inter- specific -> inter-specific
    yield n.replace("-", "")
    yield n.replace(" ", "")


src_raw = open(SRC, encoding="utf-8").read()
src_norms = [norm(src_raw), norm(src_raw).replace("- ", "-"),
             norm(src_raw).replace("-", ""), norm(src_raw).replace(" ", "")]

rows = []
in_facts = False
for line in open(INV, encoding="utf-8"):
    line = line.rstrip("\n")
    if line.startswith("## "):
        in_facts = line.strip() == "## Facts"
        continue
    if not in_facts or not re.match(r"\| F\d+a?\s*\|", line):
        continue
    cells = [c.strip() for c in line.strip().strip("|").split("|")]
    if len(cells) < 5:
        print("MALFORMED ROW:", line[:90])
        continue
    rows.append(dict(id=cells[0], section=cells[1], type=cells[2],
                     wording=cells[3], ticked=cells[4]))

print("=" * 70)
print("A. TABLE STRUCTURE")
print("=" * 70)
print("Facts rows parsed:", len(rows))

ids = [r["id"] for r in rows]
dupes = {i for i in ids if ids.count(i) > 1}
print("Duplicate IDs:", sorted(dupes) or "none")

nums = sorted({int(re.match(r"F(\d+)", i).group(1)) for i in ids})
missing = [n for n in range(nums[0], nums[-1] + 1) if n not in nums]
print("Numeric range: F%03d-F%03d" % (nums[0], nums[-1]))
print("Gaps in numeric sequence:", missing or "none")
suffixed = sorted(i for i in ids if not re.fullmatch(r"F\d+", i))
print("Suffixed IDs:", suffixed)

from collections import Counter
tc = Counter(r["type"] for r in rows)
print("\nType histogram:")
for t, c in sorted(tc.items(), key=lambda kv: -kv[1]):
    print("   %-14s %3d" % (t, c))

heads = [r["id"] for r in rows if r["type"] == "heading"]
opens = [r["id"] for r in rows if r["type"] == "Opener"]
figlab = [r for r in rows if r["type"] == "Figure labels"]
print("\nheading rows: %d -> %s" % (len(heads), " ".join(heads)))
print("Opener rows : %d -> %s" % (len(opens), " ".join(opens)))

labels = []
for r in figlab:
    got = re.findall(r'"([^"]+)"', r["wording"])
    labels.append((r["id"], got))
print("Figure-label rows: %d" % len(figlab))
total_labels = 0
for rid, got in labels:
    print("   %-6s %d labels: %s" % (rid, len(got), "; ".join(got)))
    total_labels += len(got)
print("Total in-figure labels:", total_labels)

print("\nTicked cells non-empty (should be 0 at Gate 1):",
      sum(1 for r in rows if r["ticked"]))

print()
print("=" * 70)
print("B. DIRECTION 1 - every quoted string must exist in the source")
print("=" * 70)
misses = []
checked = 0
for r in rows:
    quoted = re.findall(r'"([^"]{6,})"', r["wording"])
    for q in quoted:
        if q.startswith("Figure labels"):
            continue
        checked += 1
        # strip internal ellipses -> check the fragments
        frags = [f for f in re.split(r"\.\.\.|\u2026", q) if len(f.strip()) > 5]
        ok = True
        for f in frags:
            if not any(v in s for v in variants(f) for s in src_norms):
                ok = False
        if not ok:
            misses.append((r["id"], r["type"], q))

print("Quoted strings checked:", checked)
print("NOT found verbatim in source:", len(misses))
for rid, typ, q in misses:
    print("\n  [%s / %s]" % (rid, typ))
    print("   %s" % (q[:300]))
sys.exit(0)
