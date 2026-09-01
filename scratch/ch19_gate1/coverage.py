"""Ch19 Gate 1 — sessions 1-H / 1-O coverage sweep by residue analysis.

Rather than trying to reconstruct paragraph boundaries out of a PDF text layer whose reading
order interleaves figure labels with running text (which is exactly what defeated the naive
check), this works subtractively:

  1. Reduce each source page to an alphanumeric-only stream.
  2. Delete from that stream every inventoried row's wording, longest rows first.
  3. Whatever survives is source content that NO row covers.

Residue is then classified into known-benign page furniture vs. genuine coverage gaps. This
makes the coverage claim machine-derived instead of asserted, and it cannot be fooled by
reading order, hyphenation or page breaks.
"""
import re
import sys

RAW = "scratch/ch19_gate1/ch19_raw.txt"
INV = ("notes/class 11/Ch19_ChemicalCoordinationAndIntegration/"
       "Ch19_ChemicalCoordinationAndIntegration_inventory.md")

# Page furniture that is deliberately NOT inventoried, and the figure-label strings that are
# held in the matrix rows F200-F206 in aggregated form rather than as separate wordings.
BENIGN = [
    "reprint202627", "biology",
    "chemicalcoordinationandintegration",
    "note",
    # recto folio numbers appear twice per page
    "239", "240", "241", "242", "243", "244", "245", "246", "247", "248",
    "249", "250", "251",
]


def norm(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())


def load_pages(path):
    txt = open(path, encoding="utf-8").read()
    return {int(m.group(1)): m.group(2) for m in
            re.finditer(r"<<<<<< PAGE (\d+) >>>>>>\n(.*?)(?=<<<<<< PAGE |\Z)", txt, re.S)}


def parse_facts(path):
    rows, in_facts = [], False
    for ln in open(path, encoding="utf-8"):
        low = ln.strip().lower()
        if low.startswith("## "):
            in_facts = low.startswith("## facts")
            continue
        if not in_facts or not ln.startswith("|"):
            continue
        c = [x.strip() for x in ln.strip().strip("|").split("|")]
        if len(c) < 6 or not re.fullmatch(r"F\d{3}", c[0]):
            continue
        rows.append(dict(rid=c[0], sec=c[1], typ=c[2], word=c[3], src=c[4]))
    return rows


def main():
    pages = load_pages(RAW)
    rows = parse_facts(INV)

    # Build the pool of covering strings. Matrix rows contribute their quoted labels
    # individually, since the aggregated row wording is synthetic.
    pool = []
    for r in rows:
        if re.match(r"Figure(\s*\([a-z]\))?\s*labels", r["word"], re.I):
            pool.extend(re.findall(r'"([^"]+)"', r["word"]))
        else:
            pool.append(r["word"])
    pool = [norm(p) for p in pool if norm(p)]
    pool.sort(key=len, reverse=True)

    print(f"rows={len(rows)}  covering-strings={len(pool)}  pages={len(pages)}\n")

    total_src = total_res = 0
    gaps = []
    for p in sorted(pages):
        s = norm(pages[p])
        total_src += len(s)
        for c in pool:
            s = s.replace(c, "\x00")
        for b in sorted(BENIGN, key=len, reverse=True):
            s = s.replace(b, "\x00")
        # residue = maximal runs of surviving characters
        res = [seg for seg in s.split("\x00") if seg]
        res = [seg for seg in res if len(seg) >= 12]
        total_res += sum(len(x) for x in res)
        if res:
            gaps.append((p, res))

    pct = 100.0 * (total_src - total_res) / total_src
    print("=" * 74)
    print(f"source alnum chars      : {total_src}")
    print(f"uncovered residue chars : {total_res}  (segments >= 12 chars)")
    print(f"COVERAGE                : {pct:.2f}%")
    print("=" * 74)

    if gaps:
        print("\n### UNCOVERED RESIDUE BY PAGE")
        for p, res in gaps:
            print(f"\n  page {p}:")
            for seg in res:
                print(f"    ({len(seg):4d}) {seg[:220]}")
    else:
        print("\nNo residue segments >= 12 chars. Full coverage.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
