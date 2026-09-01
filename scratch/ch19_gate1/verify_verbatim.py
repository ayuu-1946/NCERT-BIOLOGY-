"""Ch19 Gate 1 — verify every inventory row's wording actually occurs in the source PDF text.

A tick in the inventory claims the wording was confirmed character-for-character against
the numbered source page. This script tests that claim mechanically instead of trusting it.

Strategy: build several progressively-looser normalisations of the source text and of the
row wording, and report the loosest normalisation at which each row matches. Anything that
only matches at a loose level is a real fidelity defect that must be reported.
"""
import re
import sys
import unicodedata

RAW = "scratch/ch19_gate1/ch19_raw.txt"
INV = ("notes/class 11/Ch19_ChemicalCoordinationAndIntegration/"
       "Ch19_ChemicalCoordinationAndIntegration_inventory.new.md")


def load_pages(path):
    txt = open(path, encoding="utf-8").read()
    pages = {}
    for m in re.finditer(r"<<<<<< PAGE (\d+) >>>>>>\n(.*?)(?=<<<<<< PAGE |\Z)", txt, re.S):
        pages[int(m.group(1))] = m.group(2)
    return pages


def ws(s):
    """Collapse all whitespace runs to a single space."""
    return re.sub(r"\s+", " ", s).strip()


def join_hyphen(s):
    """Join words broken across a line by a hyphen: 'anti- diuretic' -> 'anti-diuretic'."""
    return re.sub(r"-\s+", "-", s)


def ascii_punct(s):
    """Fold curly quotes/dashes to ASCII."""
    return (s.replace("\u2019", "'").replace("\u2018", "'")
             .replace("\u201c", '"').replace("\u201d", '"')
             .replace("\u2013", "-").replace("\u2014", "-")
             .replace("\u2212", "-"))


def greek(s):
    """Fold greek letters to the spelled-out latin names used by some rows."""
    return s.replace("\u03b1", "alpha").replace("\u03b2", "beta")


def strip_nonalnum(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())


LEVELS = [
    ("exact",            lambda s: ws(s)),
    ("hyphen-join",      lambda s: join_hyphen(ws(s))),
    ("ascii-punct",      lambda s: ascii_punct(join_hyphen(ws(s)))),
    ("greek-spelled",    lambda s: greek(ascii_punct(join_hyphen(ws(s))))),
    ("alnum-only",       lambda s: strip_nonalnum(greek(ascii_punct(join_hyphen(ws(s)))))),
]


def parse_rows(path):
    rows = []
    for i, ln in enumerate(open(path, encoding="utf-8"), 1):
        if not ln.startswith("| F"):
            continue
        c = [x.strip() for x in ln.strip().strip("|").split("|")]
        if len(c) < 6:
            print(f"  !! line {i}: only {len(c)} cols -> {c}")
            continue
        rows.append(dict(line=i, rid=c[0], sec=c[1], typ=c[2], word=c[3],
                         src=c[4], tick=c[5]))
    return rows


def main():
    pages = load_pages(RAW)
    allsrc = "\n".join(pages[k] for k in sorted(pages))
    rows = parse_rows(INV)
    print(f"parsed {len(rows)} rows; source pages {min(pages)}..{max(pages)}\n")

    # Precompute normalised source at each level (whole doc + per page)
    norm_all = {name: fn(allsrc) for name, fn in LEVELS}
    norm_page = {name: {p: fn(t) for p, t in pages.items()} for name, fn in LEVELS}

    results = []
    for r in rows:
        # figure-label matrix rows are synthesised, not verbatim sentences
        if r["word"].startswith("Figure labels:") or r["word"].startswith("Figure (a) labels:") \
           or r["word"].startswith("Figure (b) labels:"):
            results.append((r, "MATRIX", None))
            continue
        hit = None
        for name, fn in LEVELS:
            if fn(r["word"]) in norm_all[name]:
                hit = name
                break
        # also check the claimed page
        pg_ok = None
        try:
            pg = int(r["src"])
        except ValueError:
            pg = None
        if pg is not None and pg in pages:
            for name, fn in LEVELS:
                if fn(r["word"]) in norm_page[name][pg]:
                    pg_ok = name
                    break
        results.append((r, hit, pg_ok))

    # Report
    bad_exact = [x for x in results if x[1] not in ("exact", "hyphen-join", "MATRIX")]
    missing = [x for x in results if x[1] is None]
    wrong_pg = [x for x in results
                if x[1] not in (None, "MATRIX") and x[2] is None]

    print("=" * 78)
    print(f"ROWS TOTAL           : {len(rows)}")
    print(f"matrix rows (skipped): {sum(1 for x in results if x[1]=='MATRIX')}")
    print(f"verbatim OK          : {sum(1 for x in results if x[1] in ('exact','hyphen-join'))}")
    print(f"FIDELITY DEFECTS     : {len(bad_exact)}")
    print(f"NOT FOUND AT ALL     : {len(missing)}")
    print(f"WRONG Src PAGE       : {len(wrong_pg)}")
    print("=" * 78)

    if bad_exact:
        print("\n### FIDELITY DEFECTS (row wording differs from source characters)")
        for r, hit, pg in bad_exact:
            print(f"  {r['rid']} [matched only at: {hit}] src p{r['src']}")
            print(f"      row: {r['word'][:150]}")

    if wrong_pg:
        print("\n### Src PAGE MISMATCH (text exists but not on the claimed page)")
        for r, hit, pg in wrong_pg:
            found = [p for p in sorted(pages)
                     if LEVELS[4][1](r["word"]) in norm_page["alnum-only"][p]]
            print(f"  {r['rid']} claims p{r['src']}, actually on p{found}")
            print(f"      row: {r['word'][:120]}")

    return 0 if not (bad_exact or missing or wrong_pg) else 1


if __name__ == "__main__":
    sys.exit(main())
