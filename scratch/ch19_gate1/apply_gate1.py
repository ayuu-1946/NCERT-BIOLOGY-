"""Ch19 Gate 1 — apply the 1-H / 1-O / 1-Z results to the inventory.

Three things happen here, all mechanically:

 1. FIDELITY FIXES  — five rows whose characters disagreed with the source (three ASCII
    apostrophes where the source prints curly quotes, two rows that spelled out the Greek
    alpha/beta the source actually prints) and one wrong Src start page.

 2. INSERTIONS       — nine new rows: four SUMMARY-UNIQUE facts, four EXERCISE-UNIQUE
    alternate hormone names, and the trailing `NOTE` page label found by the 1-H sweep.
    Rows are inserted at their topical anchor so the table stays in Content Order, then the
    WHOLE table is renumbered F001..Fnnn sequentially.

 3. CROSS-REF REWRITE — prose sections reference row IDs. Renumbering invalidates them, so
    every Fnnn token outside the Facts table is remapped through the same old->new map.

The old->new map is printed so the renumbering is auditable rather than trusted.
"""
import re
import sys

INV = ("notes/class 11/Ch19_ChemicalCoordinationAndIntegration/"
       "Ch19_ChemicalCoordinationAndIntegration_inventory.new.md")
OUT = ("notes/class 11/Ch19_ChemicalCoordinationAndIntegration/"
       "Ch19_ChemicalCoordinationAndIntegration_inventory.md")

RSQ = "\u2019"   # ’
LSQ = "\u2018"   # ‘
ALPHA = "\u03b1"
BETA = "\u03b2"

# ---------------------------------------------------------------- 1. fidelity fixes
# keyed by OLD id -> (field, old_substring, new_substring)
FIXES = {
    "F080": ("word", "Graves' disease", f"Graves{RSQ} disease"),
    "F110": ("word", "Addison's disease", f"Addison{RSQ} disease"),
    "F132": ("word", "'Islets of Langerhans'", f"{LSQ}Islets of Langerhans{RSQ}"),
    "F134": ("word", "alpha-cells and beta-cells", f"{ALPHA}-cells and {BETA}-cells"),
    "F135": ("word", "The alpha-cells secrete a hormone called glucagon, while the beta-cells",
             f"The {ALPHA}-cells secrete a hormone called glucagon, while the {BETA}-cells"),
    "F055": ("src", "4", "3"),
}

# ---------------------------------------------------------------- 2. insertions
# anchor OLD id -> list of new rows (sec, typ, wording, src)
INSERT = {
    "F019": [("19.1", "concept",
              "These hormones regulate metabolism, growth and development of our organs, "
              "the endocrine glands or certain cells.", "11")],
    "F022": [("19.2", "concept",
              "The endocrine system is composed of hypothalamus, pituitary and pineal, "
              "thyroid, adrenal, pancreas, parathyroid, thymus and gonads (testis and ovary).",
              "11")],
    "F044": [("19.2.2", "concept",
              "The pituitary gland is divided into three major parts, which are called as  "
              "pars distalis, pars intermedia and pars nervosa.", "11")],
    "F049": [("19.2.2", "definition", "(b) Thyrotrophin (TSH)", "13")],
    "F050": [("19.2.2", "definition", "(c) Corticotrophin (ACTH)", "13")],
    "F056": [("19.2.2", "definition", "(e) Melanotrophin (MSH)", "13")],
    "F061": [("19.2.2", "concept",
              "The pituitary hormones regulate the growth and development of somatic tissues "
              "and activities of peripheral endocrine glands.", "11")],
    "F170": [("19.2.10", "definition", "(d) Progestational hormone", "13")],
    "F199": [("Note", "heading", "NOTE", "14")],
}


def main():
    lines = open(INV, encoding="utf-8").read().split("\n")

    # locate the Facts table body
    in_facts = False
    fact_idx = []
    for i, ln in enumerate(lines):
        low = ln.strip().lower()
        if low.startswith("## "):
            in_facts = low.startswith("## facts")
            continue
        if in_facts and ln.startswith("|") and re.match(r"\|\s*F\d{3}\s*\|", ln):
            fact_idx.append(i)
    if not fact_idx:
        print("!! no Facts rows located")
        return 1
    start, end = fact_idx[0], fact_idx[-1]
    print(f"Facts table lines {start+1}..{end+1}  ({len(fact_idx)} rows)")

    # parse rows
    rows = []
    for i in fact_idx:
        c = [x.strip() for x in lines[i].strip().strip("|").split("|")]
        rows.append(dict(old=c[0], sec=c[1], typ=c[2], word=c[3], src=c[4], tick=c[5]))

    # 1. fidelity fixes
    applied = 0
    for r in rows:
        if r["old"] in FIXES:
            field, a, b = FIXES[r["old"]]
            if a not in r[field]:
                print(f"!! {r['old']}: fix target {a!r} not present in {field}={r[field]!r}")
                return 1
            r[field] = r[field].replace(a, b)
            applied += 1
    print(f"fidelity fixes applied: {applied}/{len(FIXES)}")

    # 2. insertions
    newrows, added = [], 0
    for r in rows:
        newrows.append(r)
        for sec, typ, word, src in INSERT.get(r["old"], []):
            newrows.append(dict(old=None, sec=sec, typ=typ, word=word, src=src, tick="x"))
            added += 1
    print(f"rows inserted: {added}/{sum(len(v) for v in INSERT.values())}")
    if added != sum(len(v) for v in INSERT.values()):
        print("!! not every anchor matched")
        return 1

    # renumber + build map
    mapping = {}
    for n, r in enumerate(newrows, 1):
        nid = f"F{n:03d}"
        if r["old"]:
            mapping[r["old"]] = nid
        r["new"] = nid

    print(f"\ntotal rows now: {len(newrows)}")
    print("old -> new (only where changed):")
    changed = [(o, n) for o, n in mapping.items() if o != n]
    for o, n in changed:
        print(f"   {o} -> {n}", end="")
    print(f"\n   ({len(changed)} ids shifted)")

    # render table
    rendered = [f"| {r['new']} | {r['sec']} | {r['typ']} | {r['word']} | {r['src']} | {r['tick']} |"
                for r in newrows]

    out = lines[:start] + rendered + lines[end + 1:]

    # 3. cross-ref rewrite outside the Facts table
    lo, hi = start, start + len(rendered)

    def remap(m):
        return mapping.get(m.group(0), m.group(0))

    nsub = 0
    for i in range(len(out)):
        if lo <= i < hi:
            continue
        new = re.sub(r"F\d{3}", remap, out[i])
        if new != out[i]:
            nsub += 1
            out[i] = new
    print(f"prose lines with remapped row ids: {nsub}")

    open(OUT, "w", encoding="utf-8").write("\n".join(out))
    print(f"\nwrote {OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
