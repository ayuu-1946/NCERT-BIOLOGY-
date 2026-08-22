import re
p="/vercel/share/v0-project/notes/class 12/Ch5_MolecularBasisOfInheritance/Ch5_MolecularBasisOfInheritance_inventory.md"
lines=open(p,encoding="utf-8").read().split("\n")
# exercise-gap block = L825..850 (1-indexed) per section scan
start=None
for i,l in enumerate(lines):
    if l.startswith("## Exercise-gap"): start=i
    elif start is not None and l.startswith("## "): end=i; break
bl=lines[start:end]
rows=[]
for l in bl:
    s=l.strip()
    if not s.startswith("|"): continue
    cells=[c.strip() for c in s.strip("|").split("|")]
    j="".join(cells)
    if set(j)<=set("-: "): continue
    if cells[0].lower().startswith("term/fact"): continue
    rows.append(cells)
print("data rows:", len(rows))
marked=[r for r in rows if re.search(r"\*\*GAP\.?\*\*", r[1])]
notgap=[r for r in rows if "not a Rule 2 gap" in r[1] or "Blocked" in r[1]]
covered=[r for r in rows if r[1].strip().startswith("Covered")]
print("rows marked **GAP**:", len(marked))
for r in marked: print("   ", re.sub(r"\s+"," ",r[0])[:70])
print("rows 'Covered':", len(covered))
print("rows blocked/not-a-gap:", len(notgap))
for r in notgap: print("   ", re.sub(r"\s+"," ",r[0])[:70])
print("partition check:", len(marked)+len(covered)+len(notgap), "==", len(rows))
