import importlib.util, sys, collections
spec = importlib.util.spec_from_file_location("check_pdf", "/vercel/share/v0-project/check_pdf.py")
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
fn = getattr(m, "_extract_labels")
import inspect
print("signature:", inspect.signature(fn))
inv = "/vercel/share/v0-project/notes/class 12/Ch5_MolecularBasisOfInheritance/Ch5_MolecularBasisOfInheritance_inventory.md"
try:
    res = fn(inv)
except TypeError:
    from pathlib import Path
    res = fn(Path(inv))
print("type:", type(res))
if isinstance(res, dict):
    print("figures:", len(res))
    tot = 0
    for k, v in res.items():
        print(f"  {k!r}: {len(v)} labels")
        tot += len(v)
    print("TOTAL labels:", tot)
    # doubling check
    for k, v in res.items():
        d = [x for x,c in collections.Counter(v).items() if c>1]
        if d: print("  DOUBLED in", k, ":", d[:5])
    print("phantom 'Fig #' row present:", any(str(k).strip().strip('|').strip()=="Fig #" or "----" in str(k) for k in res))
else:
    print(res if not hasattr(res,'__len__') else f"len={len(res)}")
