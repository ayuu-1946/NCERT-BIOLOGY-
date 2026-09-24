"""Gate 1 machine re-derivation for Ch1 (Sexual Reproduction in Flowering Plants).

Re-parses the frozen inventory from disk:
  - Facts table row count, ID contiguity F001..FNNN (no gaps/dups)
  - Type census (case-sensitive; flags any non-lowercase value)
  - heading / opener / figure-label / caption sub-censuses
  - real check_pdf.py _extract_labels parse (no doubling, no phantom rows)
  - per-figure label counts vs the header claim
  - Summary classification counts
  - Figure manifest rows vs assets on disk
Prints a machine-readable report; exits 0 only if every invariant holds.
"""
import importlib.util
import os
import re
import sys

ROOT = "/home/user/NCERT-BIOLOGY-"
CH = os.path.join(ROOT, "notes/class 12/Ch1_SexualReproductionInFloweringPlants")
INV = os.path.join(CH, "Ch1_SexualReproductionInFloweringPlants_inventory.md")

# ---- import the REAL label parser from the frozen linter (never replicate) ----
spec = importlib.util.spec_from_file_location("check_pdf", os.path.join(ROOT, "check_pdf.py"))
cp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cp)
_extract_labels = cp._extract_labels

text = open(INV, encoding="utf-8").read()
lines = text.splitlines()

errors, notes = [], []

# ---- locate sections ----
def section_body(name):
    out, on = [], False
    for ln in lines:
        if ln.startswith("## " + name):
            on = True
            continue
        if on and ln.startswith("## "):
            break
        if on:
            out.append(ln)
    return out

facts_lines = [l for l in section_body("Facts") if l.strip().startswith("|")]
data = []
for l in facts_lines:
    cells = [c.strip() for c in l.strip().strip("|").split("|")]
    if len(cells) >= 5 and cells[0].startswith("F"):
        data.append(cells)

# ---- 1. row count + ID contiguity ----
ids = [r[0] for r in data]
nums = [int(r[0][1:]) for r in data]
contiguous = nums == list(range(1, len(nums) + 1))
dups = sorted({n for n in nums if nums.count(n) > 1})
n_rows = len(data)
if not contiguous:
    errors.append(f"IDs not contiguous 1..{n_rows}")
if dups:
    errors.append(f"duplicate IDs: {dups}")
notes.append(f"facts_rows={n_rows} contiguous={contiguous} dups={dups or 'none'}")

# ---- 2. type census (case-sensitive) ----
from collections import Counter
types = Counter(r[2] for r in data)
lower_ok = all(t == t.lower() for t in types)
for t in types:
    if t != t.lower():
        errors.append(f"non-lowercase Type value: {t!r}")
notes.append("type_census=" + " ".join(f"{k}:{v}" for k, v in sorted(types.items())))
notes.append(f"all_types_lowercase={lower_ok}")

# ---- 3. sub-censuses ----
heads = [r for r in data if r[2] == "heading"]
openers = [r for r in data if r[2] == "opener"]
flabel = [r for r in data if r[2] == "figure" and r[3].startswith("Figure labels")]
captions = [r for r in data if r[2] == "caption"]
notes.append(f"heading_rows={len(heads)} ids={','.join(r[0] for r in heads)}")
notes.append(f"opener_rows={len(openers)}")
notes.append(f"figure_label_rows={len(flabel)} ids={','.join(r[0] for r in flabel)}")
notes.append(f"caption_rows={len(captions)}")

def unquoted(s):
    return s.strip().strip('"').strip()

numbered = [r for r in heads if re.match(r"^\d", unquoted(r[3]))]
unnumbered = [r for r in heads if not re.match(r"^\d", unquoted(r[3]))]
notes.append(f"headings: numbered={len(numbered)} unnumbered={len(unnumbered)}")
notes.append("numbered_ids=" + ",".join(r[0] for r in numbered))
notes.append("unnumbered_ids=" + ",".join(r[0] for r in unnumbered))

# ---- 4. real _extract_labels ----
labels = _extract_labels(text)
fig_ids = sorted({f for f, _ in labels})
per_fig = Counter(f for f, _ in labels)
notes.append(f"extract_labels: {len(labels)} labels / {len(fig_ids)} figures")
notes.append("per_figure=" + " ".join(f"{f}:{per_fig[f]}" for f in fig_ids))
if "Fig #" in fig_ids:
    errors.append("PHANTOM 'Fig #' row parsed from a markdown separator")
# doubling: a (fig,label) pair appearing twice
pairs = Counter(labels)
dbl = {k: v for k, v in pairs.items() if v > 1}
if dbl:
    errors.append(f"doubled label pairs: {dbl}")
notes.append(f"doubled_pairs={len(dbl)}")

# ---- 5. header census claims (from the file's own prose) ----
m_factsh = re.search(r"^## Facts\s*$", text, re.M)
if not m_factsh:
    errors.append("could not locate the real '## Facts' section heading")
    header = text
else:
    header = text[: m_factsh.start()]
def claim(pat):
    m = re.search(pat, header)
    return m.group(1) if m else None

claims = {
    "total": claim(r"Rows: (\d+)"),
    "heading_rows": claim(r"heading rows: (\d+)"),
    "numbered_heads": claim(r"\((\d+) numbered"),
    "unnumbered_heads": claim(r"\+ (\d+) unnumbered sub-headings"),
    "opener_rows": claim(r"opener rows: (\d+)"),
    "figure_label_rows": claim(r"figure-label rows: (\d+)"),
    "caption_rows": claim(r"caption rows: (\d+)"),
    "number_rows": claim(r"number rows: (\d+)"),
    "term_rows": claim(r"term rows: (\d+)"),
    "fact_rows": claim(r"fact rows: (\d+)"),
}
notes.append("header_claims=" + str(claims))
# numbered/unnumbered breakdown: unnumbered includes SUMMARY + EXERCISES
n_unnum_sub = len(unnumbered) - 2  # minus SUMMARY, EXERCISES
if claims["numbered_heads"] and int(claims["numbered_heads"]) != len(numbered):
    errors.append(f"header numbered headings {claims['numbered_heads']} != parsed {len(numbered)}")
if claims["unnumbered_heads"] and int(claims["unnumbered_heads"]) != n_unnum_sub:
    errors.append(f"header unnumbered sub-headings {claims['unnumbered_heads']} != parsed {n_unnum_sub}")
if claims["total"] and int(claims["total"]) != n_rows:
    errors.append(f"header total {claims['total']} != parsed {n_rows}")
if claims["heading_rows"] and int(claims["heading_rows"]) != len(heads):
    errors.append(f"header heading rows {claims['heading_rows']} != parsed {len(heads)}")
if claims["opener_rows"] and int(claims["opener_rows"]) != len(openers):
    errors.append(f"header opener rows {claims['opener_rows']} != parsed {len(openers)}")
if claims["figure_label_rows"] and int(claims["figure_label_rows"]) != len(flabel):
    errors.append(f"header figure-label rows {claims['figure_label_rows']} != parsed {len(flabel)}")
if claims["caption_rows"] and int(claims["caption_rows"]) != len(captions):
    errors.append(f"header caption rows {claims['caption_rows']} != parsed {len(captions)}")
if claims["number_rows"] and int(claims["number_rows"]) != types.get("number", 0):
    errors.append(f"header number rows {claims['number_rows']} != parsed {types.get('number', 0)}")
if claims["term_rows"] and int(claims["term_rows"]) != types.get("term", 0):
    errors.append(f"header term rows {claims['term_rows']} != parsed {types.get('term', 0)}")
if claims["fact_rows"] and int(claims["fact_rows"]) != types.get("fact", 0):
    errors.append(f"header fact rows {claims['fact_rows']} != parsed {types.get('fact', 0)}")

# ---- 6. summary classification ----
sum_lines = [l for l in section_body("Summary classification") if l.strip().startswith("|")]
sum_data = [l for l in sum_lines if "BODY-PRESENT" in l or "SUMMARY-UNIQUE" in l]
n_sum = len(sum_data)
n_su = sum(1 for l in sum_data if "SUMMARY-UNIQUE" in l)
n_bp = sum(1 for l in sum_data if "BODY-PRESENT" in l)
notes.append(f"summary: scanned={n_sum} summary_unique={n_su} body_present={n_bp}")
m = re.search(r"Summary sentences scanned: (\d+)", text)
if m and int(m.group(1)) != n_sum:
    errors.append(f"summary scan claim {m.group(1)} != parsed {n_sum}")

# ---- 7. figure manifest vs disk ----
man_lines = [l for l in section_body("Figure manifest") if l.strip().startswith("|")]
man_rows = []
for l in man_lines:
    cells = [c.strip() for c in l.strip().strip("|").split("|")]
    if len(cells) >= 6 and re.match(r"^\d+\.\d+$", cells[0]):
        man_rows.append(cells)
notes.append(f"manifest_rows={len(man_rows)}")
missing_assets, mono_bad, ver_bad = [], [], []
asset_refs = set()
for cells in man_rows:
    fig, cap, asset, page, mono, ver = cells[0], cells[1], cells[2], cells[3], cells[4], cells[5]
    for a in re.split(r"\s*\+\s*", asset):
        a = a.strip()
        p = os.path.join(CH, a)
        asset_refs.add(os.path.basename(a))
        if not os.path.exists(p):
            missing_assets.append(a)
    if mono.lower() != "yes":
        mono_bad.append(fig)
    if ver.lower() != "yes":
        ver_bad.append(fig)
disk = sorted(f for f in os.listdir(os.path.join(CH, "assets")) if f.endswith(".png"))
notes.append(f"assets_on_disk={len(disk)}")
notes.append(f"manifest_table_asset_refs={len(asset_refs)}")
extra = sorted(set(disk) - asset_refs)
notes.append(f"on_disk_beyond_manifest_table={extra or 'none'} (whole plates + sub-panels coexist by design)")
# the manifest prose asserts a total asset count — verify it against disk
m_tot = re.search(r"Total assets on disk: (\d+)", text)
if m_tot and int(m_tot.group(1)) != len(disk):
    errors.append(f"manifest prose 'Total assets on disk: {m_tot.group(1)}' != {len(disk)} on disk")
else:
    notes.append(f"manifest_total_claim={m_tot.group(1) if m_tot else 'none'} matches disk" if m_tot else "no manifest total claim found")
if missing_assets:
    errors.append(f"manifest assets missing on disk: {missing_assets}")
if mono_bad:
    errors.append(f"manifest Mono != yes: {mono_bad}")
if ver_bad:
    errors.append(f"manifest Verified != yes: {ver_bad}")

# ---- 8. tick state (record only — ticking is Pass 2) ----
ticked = sum(1 for r in data if r[4].strip().lower() in ("x", "✔", "yes"))
notes.append(f"ticked={ticked}/{n_rows} (record only; not a Gate 1 criterion)")

# ---- 9. asset monochrome mode on disk ----
from PIL import Image
bad_mode = []
for f in disk:
    im = Image.open(os.path.join(CH, "assets", f))
    if im.mode != "L":
        bad_mode.append(f"{f}:{im.mode}")
notes.append(f"non_L_mode_assets={bad_mode or 'none'}")
if bad_mode:
    errors.append(f"assets not mode=L: {bad_mode}")

print("=" * 72)
for n in notes:
    print(" ", n)
print("=" * 72)
if errors:
    print("ERRORS:")
    for e in errors:
        print("  -", e)
    print("VERDICT: RED")
    sys.exit(1)
print("VERDICT: GREEN — all invariants hold")
