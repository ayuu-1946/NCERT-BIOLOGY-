import importlib.util, collections
spec = importlib.util.spec_from_file_location("check_pdf", "check_pdf.py")
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
inv = "/vercel/share/v0-project/notes/class 12/Ch5_MolecularBasisOfInheritance/Ch5_MolecularBasisOfInheritance_inventory.md"
text = open(inv, encoding="utf-8").read()
pairs = m._extract_labels(text)
print("TOTAL label strings parsed:", len(pairs))
byfig = collections.OrderedDict()
for fid, lab in pairs:
    byfig.setdefault(fid, []).append(lab)
print("distinct figure keys:", len(byfig))
for k, v in byfig.items():
    dup = [x for x,c in collections.Counter(v).items() if c>1]
    print(f"  {k!r}: {len(v)} labels" + (f"   <-- INTERNAL DUP {dup}" if dup else ""))
print()
print("phantom keys (separator/junk):", [k for k in byfig if k.strip() in ("Fig #","-------","----") or set(k.strip())<=set("-: ")] or "none")
# global doubling: same (fig,label) twice
gd = [p for p,c in collections.Counter(pairs).items() if c>1]
print("exact (fig,label) duplicate pairs:", len(gd), gd[:5])
# label rows count vs figure-label Type rows
print()
print("expected 136 figure-label rows -> parsed", len(pairs), "labels; equal:", len(pairs)==136)
