import re, sys, importlib.util, collections

CHECK = "check_pdf.py"
INV = "notes/class 12/Ch2_HumanReproduction/Ch2_HumanReproduction_inventory.md"

spec = importlib.util.spec_from_file_location("check_pdf", CHECK)
cp = importlib.util.module_from_spec(spec); spec.loader.exec_module(cp)

inv = open(INV).read()

def rows_of_table(text, header_name):
    """Yield cell-lists for pipe rows under a '## header_name' section."""
    in_sec = False
    for line in text.splitlines():
        low = line.strip().lower()
        if low.startswith("## "):
            in_sec = low.startswith("## " + header_name.lower())
            continue
        if in_sec and line.strip().startswith("|"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            yield cells

# --- Parse Facts table ---
facts = [c for c in rows_of_table(inv, "facts")
         if c and re.match(r"[A-Za-z]?\d", c[0]) and c[0].lower() not in ("id",)]
print("== FACTS TABLE ==")
print("parsed fact rows:", len(facts))

# ID contiguity (numeric core, ignoring suffix letters)
ids = [f[0] for f in facts]
dupes = [k for k,v in collections.Counter(ids).items() if v>1]
print("duplicate IDs:", dupes or "none")
nums = sorted({int(re.match(r"[A-Za-z]?(\d+)", i).group(1)) for i in ids})
lo, hi = nums[0], nums[-1]
full = set(range(lo, hi+1))
gaps = sorted(full - set(nums))
print(f"numeric ID range: F{lo:03d}..F{hi:03d}; distinct numbers: {len(nums)}")
print("gaps in numbering:", [f"F{g:03d}" for g in gaps] or "none")
suffixed = [i for i in ids if re.match(r"[A-Za-z]?\d+[a-z]$", i)]
print("suffixed (folded/opener-variant) IDs:", suffixed or "none")

# Type vocabulary
types = collections.Counter(f[2] for f in facts)
print("\n== TYPE VOCAB ==")
for t,n in sorted(types.items()): print(f"  {t!r}: {n}")
allowed = {"title","opener","heading","caption","fact","number","term","process",
           "structure","function","hormone","comparison","exception"}
bad = [t for t in types if t not in allowed]
print("non-normalized/unexpected types:", bad or "none")

# Heading + opener rows
headings = [f for f in facts if f[2]=="heading"]
openers  = [f for f in facts if f[2]=="opener"]
captions = [f for f in facts if f[2]=="caption"]
print("\n== STRUCTURE ROWS ==")
print("heading rows:", len(headings), "->", [f[0] for f in headings])
print("opener rows :", len(openers), "->", [f[0] for f in openers])
print("caption rows:", len(captions), "->", [f[0] for f in captions])

# --- Gate-1 machine check: run check_pdf's own _extract_labels ---
print("\n== _extract_labels (check_pdf.py) ==")
labels = cp._extract_labels(inv)
fig_ids = [fid for fid,_ in labels]
per_fig = collections.Counter(fig_ids)
print("total (fig,label) pairs:", len(labels))
print("distinct figure rows parsed:", len(per_fig), "->", list(per_fig.keys()))
# doubling: any identical (fig,label) twice?
pair_dupes = [k for k,v in collections.Counter(labels).items() if v>1]
print("doubled (fig,label) pairs:", pair_dupes or "none")
# phantom: fig_id that isn't Fxxx
phantom = [fid for fid in per_fig if not re.match(r"F\d", fid)]
print("phantom fig rows (non-F id):", phantom or "none")
print("labels per figure:")
for fid,n in per_fig.items(): print(f"   {fid}: {n}")

# --- Figure manifest table ---
man = [c for c in rows_of_table(inv, "figure manifest")
       if c and re.match(r"\d\.\d", c[0])]
print("\n== FIGURE MANIFEST ==")
print("manifest figure rows:", len(man))
mono_bad = [c[0] for c in man if len(c)>4 and c[4].lower()!="yes"]
ver_bad  = [c[0] for c in man if len(c)>5 and c[5].lower()!="yes"]
print("rows not Mono=yes:", mono_bad or "none")
print("rows not Verified=yes:", ver_bad or "none")

# --- Header count assertions ---
print("\n== HEADER CLAIM CROSS-CHECK ==")
print(f"claim heading rows=10  actual={len(headings)}  {'OK' if len(headings)==10 else 'MISMATCH'}")
print(f"claim opener rows=8    actual={len(openers)}   {'OK' if len(openers)==8 else 'MISMATCH'}")
print(f"claim figure-label rows=14  actual_distinct={len(per_fig)}  {'OK' if len(per_fig)==14 else 'MISMATCH'}")
print(f"claim manifest figs=14  actual={len(man)}  {'OK' if len(man)==14 else 'MISMATCH'}")
