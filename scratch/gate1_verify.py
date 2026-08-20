#!/usr/bin/env python3
"""Gate 1 (pre-Pass-2) inventory-integrity verification for Ch9 Biomolecules.
Reuses check_pdf.py's own _extract_labels parser so the label audit matches the
machine gate exactly. No rendered PDF exists yet, so this checks the inventory
+ assets only (the parts Gate 1 owns)."""
import os, re, sys, importlib.util

ROOT = "/vercel/share/v0-project"
FOLDER = os.path.join(ROOT, "notes/class 11/Ch9_Biomolecules")
INV = os.path.join(FOLDER, "Ch9_Biomolecules_inventory.md")
ASSETS = os.path.join(FOLDER, "assets")

# _extract_labels copied verbatim from check_pdf.py (pure-text; no pymupdf needed)
def extract_labels(inv_text):
    out = []
    for line in inv_text.splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 4:
            continue
        fig_id = cells[1] if len(cells) > 1 else "?"
        wording = cells[3]
        if re.match(r"figure(\s*\([a-z]\))?\s*labels", wording, re.I):
            quoted = re.findall(r'"([^"]+)"', wording)
            if not quoted:
                body = re.sub(r"^figure(\s*\([a-z]\))?\s*labels\s*:?", "", wording, flags=re.I)
                quoted = [p.strip() for p in body.split(";") if p.strip()]
            for lab in quoted:
                out.append((fig_id, lab))
    return out

text = open(INV, encoding="utf-8").read()
lines = text.splitlines()

def section(name):
    """Return the list of lines belonging to a '## name' section."""
    out, cur = [], False
    for ln in lines:
        s = ln.strip().lower()
        if s.startswith("## "):
            cur = s.startswith("## " + name.lower())
            continue
        if cur:
            out.append(ln)
    return out

problems = []

# ---- 1. Facts rows parse + contiguous + ticked ----
fact_rows = []
for ln in section("facts"):
    if not ln.strip().startswith("|"):
        continue
    cells = [c.strip() for c in ln.strip().strip("|").split("|")]
    if len(cells) < 5 or not re.match(r"^F\d+$", cells[0]):
        continue
    fact_rows.append(cells)
fnums = [int(c[0][1:]) for c in fact_rows]
n_facts = len(fact_rows)
contiguous = fnums == list(range(1, n_facts + 1))
unticked = [c[0] for c in fact_rows if c[-1].lower() not in ("x", "[x]", "done", "yes")]
print(f"[Facts] {n_facts} rows parsed, range F001..F{n_facts:03d}, "
      f"contiguous={contiguous}, unticked={len(unticked)}")
if not contiguous:
    problems.append(f"Facts not contiguous: {fnums[:5]}...{fnums[-5:]}")
if unticked:
    problems.append(f"Unticked facts: {unticked}")

# ---- 2. Summary fact rows (section == 'Summary') ----
summary_fact_rows = [c for c in fact_rows if c[1].lower() == "summary"]
su_type = [c for c in summary_fact_rows if "summary-unique" in c[2].lower()]
bp_type = [c for c in summary_fact_rows if "summary-unique" not in c[2].lower()]
print(f"[Summary fact rows] {len(summary_fact_rows)} total "
      f"({len(su_type)} summary-unique, {len(bp_type)} other)")
if bp_type:
    problems.append(f"Non-summary-unique rows in Summary section: {[c[0] for c in bp_type]}")

# ---- 3. Summary classification table counts ----
bp = su = other = 0
class_rows = 0
for ln in section("summary classification"):
    if not ln.strip().startswith("|"):
        continue
    cells = [c.strip() for c in ln.strip().strip("|").split("|")]
    if len(cells) < 3 or cells[1].lower() in ("classification", "---", ":---") or set(cells[1]) <= {"-", ":"}:
        continue
    cl = cells[1].upper()
    class_rows += 1
    if "SUMMARY-UNIQUE" in cl:
        su += 1
    elif "BODY-PRESENT" in cl:
        bp += 1
    else:
        other += 1
print(f"[Summary classification] {class_rows} rows: {bp} BODY-PRESENT, {su} SUMMARY-UNIQUE, {other} unclassified")
if other:
    problems.append(f"{other} summary sentences left unclassified")

# ---- 4. Cross-check: #SUMMARY-UNIQUE classification == #summary-unique fact rows ----
if su != len(su_type):
    problems.append(f"SUMMARY-UNIQUE count ({su}) != summary-unique fact rows ({len(su_type)})")
else:
    print(f"[Cross-check] SUMMARY-UNIQUE ({su}) == summary-unique fact rows ({len(su_type)})  OK")

# ---- 4b. Stated audit tally must match the derived counts ----
m = re.search(r"(\d+)\s+BODY-PRESENT,\s+(\d+)\s+SUMMARY-UNIQUE", text)
if m:
    stated_bp, stated_su = int(m.group(1)), int(m.group(2))
    ok = (stated_bp == bp and stated_su == su)
    print(f"[Audit tally line] states {stated_bp} BODY-PRESENT, {stated_su} SUMMARY-UNIQUE "
          f"-> {'OK' if ok else 'MISMATCH vs derived %d/%d' % (bp, su)}")
    if not ok:
        problems.append(f"Audit tally line {stated_bp}/{stated_su} != derived {bp}/{su}")

# ---- 5. Figure-label matrix parses (via real check_pdf parser if available) ----
if extract_labels:
    labels = extract_labels(text)
    figs = sorted(set(f for f, _ in labels))
    print(f"[Figure labels] {len(labels)} labels across {len(figs)} figure rows (check_pdf parser)")
else:
    print("[Figure labels] check_pdf parser unavailable (pymupdf missing) - skipped")

# ---- 6. Figure manifest complete + assets on disk ----
manifest = []
for ln in section("figure manifest"):
    if not ln.strip().startswith("|"):
        continue
    cells = [c.strip() for c in ln.strip().strip("|").split("|")]
    if len(cells) < 6 or not cells[0].lower().startswith("figure"):
        continue
    manifest.append(cells)
disk_assets = sorted(f for f in os.listdir(ASSETS) if f.endswith(".png"))
print(f"[Figure manifest] {len(manifest)} rows; {len(disk_assets)} PNGs on disk")
mono_ok = all(c[4].lower() == "yes" and c[5].lower() == "yes" for c in manifest)
print(f"[Figure manifest] all rows Mono=yes & Verified=yes: {mono_ok}")
if len(manifest) != len(disk_assets):
    problems.append(f"manifest rows ({len(manifest)}) != assets on disk ({len(disk_assets)})")
if not mono_ok:
    problems.append("some manifest rows not Mono/Verified=yes")

# ---- 7. Exercise-gap scan exists ----
eg = section("exercise-gap terms")
eg_rows = [ln for ln in eg if ln.strip().startswith("|") and ln.strip().strip("|").split("|")[0].strip().lower().startswith("q")]
print(f"[Exercise-gap] section present={bool(eg)}, {len(eg_rows)} Q-rows")
if not eg:
    problems.append("Exercise-gap terms section missing")

# ---- verdict ----
print("=" * 60)
if problems:
    print(f"GATE 1: RED — {len(problems)} problem(s):")
    for p in problems:
        print("  - " + p)
    sys.exit(1)
print("GATE 1: GREEN — inventory integrity checks all pass")
