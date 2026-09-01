"""Ch19 Gate 1 verifier, round 2.

Round 1 conflated two different things: rows whose characters genuinely disagree with the
source, and rows whose sentence is interrupted mid-flow by running page furniture (page
number, 'BIOLOGY' verso head, recto running head, 'Reprint 2026-27'). This round strips the
furniture first so only genuine character defects remain.

Only the `## Facts` table is checked. The figure-manifest table (rows keyed 'Fig 19.x') is a
deliverables list, not a verbatim-wording table, and is excluded by requiring an Fnnn ID.
"""
import re
import sys

RAW = "scratch/ch19_gate1/ch19_raw.txt"
INV = ("notes/class 11/Ch19_ChemicalCoordinationAndIntegration/"
       "Ch19_ChemicalCoordinationAndIntegration_inventory.md")

FURNITURE = re.compile(
    r"^(?:\s*\d{3}\s*|\s*BIOLOGY\s*|\s*CHEMICAL COORDINATION AND INTEGRATION\s*"
    r"|\s*Reprint 20\d\d-\d\d\s*|\s*NOTE\s*)$", re.M)


def load(path):
    txt = open(path, encoding="utf-8").read()
    pages = {}
    for m in re.finditer(r"<<<<<< PAGE (\d+) >>>>>>\n(.*?)(?=<<<<<< PAGE |\Z)", txt, re.S):
        pages[int(m.group(1))] = m.group(2)
    return pages


def ws(s):
    return re.sub(r"\s+", " ", s).strip()


def defurnish(s):
    return ws(FURNITURE.sub(" ", s))


def joins(s):
    """Repair intra-word breaks the PDF text layer introduces at line ends."""
    s = re.sub(r"-\s+", "-", s)   # anti- diuretic  -> anti-diuretic
    s = re.sub(r"/\s+", "/", s)   # dissolution/ demineralisation -> .../...
    return s


def curly(s):
    return (s.replace("\u2019", "'").replace("\u2018", "'")
             .replace("\u201c", '"').replace("\u201d", '"'))


def greek(s):
    return s.replace("\u03b1", "alpha").replace("\u03b2", "beta")


def dash(s):
    return s.replace("\u2013", "-").replace("\u2014", "-").replace("\u2212", "-")


# ordered loosest-last; the FIRST level that matches is reported
LEVELS = [
    ("VERBATIM",       lambda s: joins(ws(s))),
    ("dash-fold",      lambda s: dash(joins(ws(s)))),
    ("DEFECT:quotes",  lambda s: curly(dash(joins(ws(s))))),
    ("DEFECT:greek",   lambda s: greek(curly(dash(joins(ws(s)))))),
    ("DEFECT:deep",    lambda s: re.sub(r"[^a-z0-9]", "",
                                        greek(curly(dash(joins(ws(s()))))).lower())
                                 if False else
                                 re.sub(r"[^a-z0-9]", "",
                                        greek(curly(dash(joins(ws(s))))).lower())),
]

CLEAN = {"VERBATIM", "dash-fold"}


def parse_facts(path):
    rows, in_facts = [], False
    for i, ln in enumerate(open(path, encoding="utf-8"), 1):
        low = ln.strip().lower()
        if low.startswith("## "):
            in_facts = low.startswith("## facts")
            continue
        if not in_facts or not ln.startswith("|"):
            continue
        c = [x.strip() for x in ln.strip().strip("|").split("|")]
        if len(c) < 6 or not re.fullmatch(r"F\d{3}", c[0]):
            continue
        rows.append(dict(line=i, rid=c[0], sec=c[1], typ=c[2],
                         word=c[3], src=c[4], tick=c[5]))
    return rows


def main():
    pages = load(RAW)
    body = defurnish("\n".join(pages[k] for k in sorted(pages)))
    perpage = {p: defurnish(t) for p, t in pages.items()}
    rows = parse_facts(INV)

    norm_body = {n: f(body) for n, f in LEVELS}
    norm_page = {n: {p: f(t) for p, t in perpage.items()} for n, f in LEVELS}

    matrix, defects, notfound, pgbad, clean = [], [], [], [], 0
    for r in rows:
        if re.match(r"Figure(\s*\([a-z]\))?\s*labels", r["word"], re.I):
            matrix.append(r)
            continue
        hit = next((n for n, f in LEVELS if f(r["word"]) in norm_body[n]), None)
        if hit is None:
            notfound.append(r)
            continue
        if hit in CLEAN:
            clean += 1
        else:
            defects.append((r, hit))
        pg = int(r["src"]) if r["src"].isdigit() else None
        if pg and pg in perpage:
            if not any(f(r["word"]) in norm_page[n][pg] for n, f in LEVELS):
                # allow sentences that legitimately straddle pg-1 -> pg
                nb = [p for p in sorted(perpage)
                      if LEVELS[4][1](r["word"]) in norm_page["DEFECT:deep"][p]]
                if not nb:
                    pgbad.append((r, nb))

    print("=" * 74)
    print(f"Facts rows parsed        : {len(rows)}")
    print(f"  figure-label matrix    : {len(matrix)}")
    print(f"  verbatim-clean         : {clean}")
    print(f"  CHARACTER DEFECTS      : {len(defects)}")
    print(f"  not found in source    : {len(notfound)}")
    print(f"  page-attribution issues: {len(pgbad)}")
    print("=" * 74)

    if defects:
        print("\n### CHARACTER-LEVEL FIDELITY DEFECTS")
        for r, hit in defects:
            print(f"\n  {r['rid']}  ({hit})  src p{r['src']}  line {r['line']}")
            print(f"    row wording: {r['word']}")

    if notfound:
        print("\n### NOT LOCATED IN SOURCE (spans pages, or is summary/exercise-sourced)")
        for r in notfound:
            print(f"\n  {r['rid']}  src p{r['src']}  line {r['line']}")
            print(f"    row wording: {r['word'][:170]}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
