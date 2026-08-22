import re, sys, collections
p = "/vercel/share/v0-project/notes/class 12/Ch5_MolecularBasisOfInheritance/Ch5_MolecularBasisOfInheritance_inventory.md"
lines = open(p, encoding="utf-8").read().split("\n")

rows = []          # (lineno, id, section, type, wording, ticked)
for i, ln in enumerate(lines, 1):
    s = ln.strip()
    if not s.startswith("|"):
        continue
    cells = [c.strip() for c in s.strip("|").split("|")]
    if not cells: continue
    m = re.fullmatch(r"F(\d{3,4})", cells[0])
    if not m: continue
    rows.append((i, cells[0], cells[1] if len(cells)>1 else "",
                 cells[2] if len(cells)>2 else "",
                 cells[3] if len(cells)>3 else "",
                 cells[4] if len(cells)>4 else ""))

ids = [r[1] for r in rows]
nums = [int(r[1][1:]) for r in rows]
print("=== FACTS TABLE PARSE ===")
print("row lines matched (raw incl. dups):", len(rows))
dups = [k for k,v in collections.Counter(ids).items() if v>1]
print("duplicate IDs:", sorted(dups) or "none")
uniq = sorted(set(nums))
print("unique IDs:", len(uniq), "min F%03d max F%03d" % (min(nums), max(nums)))
expected = set(range(min(nums), max(nums)+1))
gaps = sorted(expected - set(nums))
print("gaps:", ["F%03d"%g for g in gaps] or "none")
print("monotonic in file order:", nums == sorted(nums))

types = collections.Counter(r[3] for r in rows)
print("\n=== TYPE CENSUS (raw, case-sensitive) ===")
tot=0
for t,c in sorted(types.items(), key=lambda x:(-x[1],x[0])):
    print(f"  {t!r}: {c}"); tot+=c
print("  sum:", tot)
lowered = collections.Counter(r[3].lower() for r in rows)
print("case-collisions:", [t for t in types if sum(1 for u in types if u.lower()==t.lower())>1] or "none")

ticked = [r for r in rows if r[5].lower() == "x"]
print("\nticked rows:", len(ticked))

print("\n=== KEY GROUPS ===")
for want in ("heading","opener","figure-label"):
    g = [r[1] for r in rows if r[3].lower()==want]
    print(f"{want}: {len(g)}  first={g[0] if g else '-'} last={g[-1] if g else '-'}")

# figure-label rows must begin with 'Figure labels:'
fl = [r for r in rows if r[3].lower()=="figure-label"]
bad = [r[1] for r in fl if not r[4].lstrip('*').strip().startswith("Figure labels:")]
print("figure-label rows NOT starting 'Figure labels:':", bad or "none")
