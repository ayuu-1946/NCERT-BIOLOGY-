import re, collections
p = "/vercel/share/v0-project/notes/class 12/Ch5_MolecularBasisOfInheritance/Ch5_MolecularBasisOfInheritance_inventory.md"
lines = open(p, encoding="utf-8").read().split("\n")

# locate H2 sections
h2 = [(i+1, l.strip()) for i,l in enumerate(lines) if l.startswith("## ")]
print("=== H2 SECTIONS ===")
for n,t in h2: print(f"  L{n}: {t}")

def block(title):
    start = None
    for i,l in enumerate(lines):
        if l.startswith("## ") and title.lower() in l.lower():
            start = i; break
    if start is None: return None, None, []
    end = len(lines)
    for j in range(start+1, len(lines)):
        if lines[j].startswith("## "):
            end = j; break
    return start+1, end, lines[start:end]

def datarows(bl):
    out=[]
    for l in bl:
        s=l.strip()
        if not s.startswith("|"): continue
        cells=[c.strip() for c in s.strip("|").split("|")]
        if not cells: continue
        joined="".join(cells)
        if set(joined) <= set("-: "): continue           # separator
        if re.match(r"^(summary sentence|term/fact|fig #|id|asset|count|group|session)\b", cells[0], re.I): continue
        if cells[0].startswith("**") and cells[0].strip("* ").lower() in ("count","group","session"): continue
        out.append(cells)
    return out

for name in ("Summary classification", "Exercise-gap"):
    s,e,bl = block(name)
    rows = datarows(bl)
    print(f"\n=== {name} (L{s}..{e}) : {len(rows)} data rows ===")
    if "Summary" in name:
        cls = collections.Counter()
        for c in rows:
            txt = " ".join(c).upper()
            if "SUMMARY-UNIQUE" in txt: cls["SUMMARY-UNIQUE"] += 1
            elif "BODY-PRESENT" in txt: cls["BODY-PRESENT"] += 1
            else: cls["?UNCLASSIFIED"] += 1
        print("  ", dict(cls), " sum:", sum(cls.values()))
    else:
        gaps = sum(1 for c in rows if "GAP" in " ".join(c).upper())
        print("   rows containing 'GAP':", gaps)

# manifest rows
s,e,bl = block("Figure manifest")
rows = datarows(bl)
print(f"\n=== Figure manifest (L{s}..{e}) : {len(rows)} asset rows ===")
mono = sum(1 for c in rows if len(c)>3 and c[3].lower()=="yes")
ver  = sum(1 for c in rows if len(c)>4 and c[4].lower()=="yes")
print("   Mono yes:", mono, " Verified yes:", ver)
import os
d="/vercel/share/v0-project/notes/class 12/Ch5_MolecularBasisOfInheritance/assets"
disk=set(os.listdir(d))
listed=set()
for c in rows:
    mm=re.search(r"fig_5_[a-z0-9_]+\.png", c[0])
    if mm: listed.add(mm.group(0))
print("   assets listed in manifest:", len(listed))
print("   on disk but NOT in manifest:", sorted(disk-listed) or "none")
print("   in manifest but NOT on disk:", sorted(listed-disk) or "none")
