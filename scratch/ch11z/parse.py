import re, collections, sys
p="notes/class 11/Ch11_PhotosynthesisInHigherPlants/Ch11_PhotosynthesisInHigherPlants_inventory.md"
rows=[]
for line in open(p, encoding="utf-8"):
    if not line.strip().startswith("|"): continue
    c=[x.strip() for x in line.strip().strip("|").split("|")]
    if len(c)<5: continue
    if re.fullmatch(r"F\d+[a-z]?", c[0]):
        rows.append(c)
ids=[r[0] for r in rows]
print("row count:", len(rows))
print("first/last:", ids[0], ids[-1])
nums=[int(re.sub(r"[a-z]","",i)[1:]) for i in ids]
print("dups:", [i for i,n in collections.Counter(ids).items() if n>1])
print("monotonic:", all(b>=a for a,b in zip(nums,nums[1:])))
expected=set(range(1,max(nums)+1))
print("gaps:", sorted(expected-set(nums)))
print("max id:", max(nums))
types=collections.Counter(r[2] for r in rows)
print("type census:", dict(sorted(types.items(), key=lambda kv:-kv[1])), "sum", sum(types.values()))
print("type casing variants:", sorted(set(r[2] for r in rows)))
# sections
secs=collections.Counter(r[1] for r in rows)
print("sections:", sorted(secs.items()))
# heading rows
for t in ("heading","opener","caption"):
    sel=[r[0] for r in rows if r[2]==t]
    print(f"{t} rows ({len(sel)}):", " ".join(sel))
