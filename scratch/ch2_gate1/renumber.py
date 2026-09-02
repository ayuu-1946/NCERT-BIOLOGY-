import re

INV = "notes/class 12/Ch2_HumanReproduction/Ch2_HumanReproduction_inventory.md"
text = open(INV).read()
lines = text.splitlines()

# --- locate the ## Facts table region ---
start = next(i for i,l in enumerate(lines) if l.strip().lower()=="## facts")
# find end = next '## ' header after start
end = next(i for i in range(start+1, len(lines)) if lines[i].strip().startswith("## "))

# rows inside facts region
region = lines[start:end]
# separate header rows (| ID | Section | ...| and |----|) from data rows
data_idx = [k for k,l in enumerate(region)
            if l.strip().startswith("|") and re.match(r"\|\s*[A-Za-z]?\d", l)]
data_rows = [region[k] for k in data_idx]

def cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]

# --- reorder: move F058b to sit right after F108b (content order, both §2.2) ---
def rowid(line): return cells(line)[0]
rows = list(data_rows)
f058 = next(r for r in rows if rowid(r)=="F058b")
rows.remove(f058)
pos = next(i for i,r in enumerate(rows) if rowid(r)=="F108b")
rows.insert(pos+1, f058)

# --- caption fig-number mapping (unique col1 per figure, in caption row order) ---
cap_fignos = ["2.1a","2.1b","2.2","2.3a","2.3b","2.4","2.5","2.6",
              "2.7","2.8","2.9","2.10","2.11","2.12"]

# --- assign contiguous new IDs in physical order; build old->new map ---
oldnew = {}
cap_i = 0
new_rows = []
n = 0
for r in rows:
    c = cells(r)
    n += 1
    new_id = f"F{n:03d}"
    oldnew[c[0]] = new_id
    c[0] = new_id
    if c[2] == "caption":
        c[1] = cap_fignos[cap_i]; cap_i += 1
    new_rows.append("| " + " | ".join(c) + " |")

assert cap_i == 14, cap_i
print("total rows renumbered:", n)
print("sample map:", {k:oldnew[k] for k in list(oldnew)[:6]})

# --- rebuild facts region: keep the 2 header lines, then new_rows ---
header_lines = [l for l in region if l.strip().startswith("|")][:2]  # title + separator
new_region = [region[0], "", header_lines[0], header_lines[1]] + new_rows
# region[0] is '## Facts'; keep a blank line after
lines_new = lines[:start] + new_region + lines[end:]
text2 = "\n".join(lines_new)

# --- global remap of every old ID token elsewhere in the file (single pass) ---
# match tokens like F058b, F108, F002 ; longest-first to avoid partial hits
tokens = sorted(oldnew.keys(), key=len, reverse=True)
pat = re.compile(r"\b(" + "|".join(re.escape(t) for t in tokens) + r")\b")
def repl(m): return oldnew[m.group(1)]
# only remap OUTSIDE the facts region we already rewrote:
before = "\n".join(lines_new[:start])
region_txt = "\n".join(new_region)
after = "\n".join(lines_new[start+len(new_region):])
before2 = pat.sub(repl, before)
after2  = pat.sub(repl, after)
text3 = before2 + "\n" + region_txt + "\n" + after2

open(INV,"w").write(text3)
print("written.")
# dump the structural lists for header rewrite
print("HEADINGS:", [oldnew[o] for o in ["F001"] if False])  # placeholder
