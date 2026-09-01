"""Ch19 Gate 1 — session 1-H (heading sweep) and machine support for 1-Z (summary sweep).

1-H: enumerate every heading the source actually prints and assert a row exists for each.
1-Z: split the SUMMARY into sentences and, for each, rank the BODY rows (rows whose Src is a
     body page 1-10) by content-word overlap. A high-overlap body row is candidate proof that
     the summary sentence is BODY-PRESENT; a low ceiling is evidence it is SUMMARY-UNIQUE.
     The verdict itself is a judgement call recorded in the inventory, but the evidence that
     drives it is produced here rather than asserted.
"""
import re
import sys

RAW = "scratch/ch19_gate1/ch19_raw.txt"
INV = ("notes/class 11/Ch19_ChemicalCoordinationAndIntegration/"
       "Ch19_ChemicalCoordinationAndIntegration_inventory.md")

STOP = set("""a an the of and or in on to for with as is are was were be been by at from that
which this these those it its our we you have has had also their them then than but not no
such very major role plays play important into other some only two three all can may".""".split())


def norm(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())


def toks(s):
    return {w for w in re.findall(r"[a-z0-9]+", s.lower()) if w not in STOP and len(w) > 2}


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


# ----------------------------------------------------------------- 1-H
EXPECTED_HEADINGS = [
    ("chapter title",  "CHEMICAL COORDINATION AND INTEGRATION"),
    ("chapter label",  "CHAPTER  19"),
    ("contents 19.1",  "19.1 Endocrine Glands and Hormones"),
    ("contents 19.2",  "19.2 Human Endocrine System"),
    ("contents 19.3",  "19.3 Hormones of Heart, Kidney and Gastrointestinal Tract"),
    ("contents 19.4",  "19.4 Mechanism of Hormone Action"),
    ("19.1",     "ENDOCRINE GLANDS AND HORMONES"),
    ("19.2",     "HUMAN ENDOCRINE SYSTEM"),
    ("19.2.1",   "The Hypothalamus"),
    ("19.2.2",   "The Pituitary Gland"),
    ("19.2.3",   "The Pineal Gland"),
    ("19.2.4",   "Thyroid Gland"),
    ("19.2.5",   "Parathyroid Gland"),
    ("19.2.6",   "Thymus"),
    ("19.2.7",   "Adrenal Gland"),
    ("19.2.8",   "Pancreas"),
    ("19.2.9",   "Testis"),
    ("19.2.10",  "Ovary"),
    ("19.3",     "HORMONES OF HEART, KIDNEY AND GASTROINTESTINAL TRACT"),
    ("19.4",     "MECHANISM OF HORMONE ACTION"),
    ("summary",  "SUMMARY"),
    ("exercises", "EXERCISES"),
    ("trailing page label", "NOTE"),
]


def sweep_h(pages, rows):
    """A heading is covered only by a heading/opener-TYPED row whose wording, once its
    section number is stripped, equals the heading text exactly. Substring matching is
    unusable here: 'Thymus' occurs inside the gland list of a concept row and 'NOTE' occurs
    inside the word 'note', both of which would score a bogus hit."""
    src = norm("\n".join(pages[k] for k in sorted(pages)))
    heads = [r for r in rows if r["typ"] in ("heading", "opener")]
    print("=" * 74)
    print("SESSION 1-H — HEADING COVERAGE SWEEP (strict: typed rows, exact match)")
    print("=" * 74)
    miss = []
    for label, text in EXPECTED_HEADINGS:
        in_src = norm(text) in src
        want = norm(text)
        hit = None
        for r in heads:
            # strip any leading section number from the row wording before comparing
            bare = norm(re.sub(r"^\s*\d+(\.\d+)*\s*", "", r["word"]))
            if bare == want or norm(r["word"]) == want:
                hit = r
                break
        status = "OK " if hit else "GAP"
        if not hit:
            miss.append((label, text, in_src))
        print(f"  {status}  {label:22} | in source: {str(in_src):5} | "
              f"row: {hit['rid'] if hit else '-- NONE --'}")
    print(f"\n  heading/opener-typed rows in inventory : {len(heads)}")
    print(f"  expected headings enumerated           : {len(EXPECTED_HEADINGS)}")
    print(f"  GAPS                                   : {len(miss)}")
    for label, text, in_src in miss:
        print(f"    !! {label}: {text!r} (present in source: {in_src})")
    return miss


# ----------------------------------------------------------------- 1-Z
def get_summary(pages):
    """SUMMARY runs from the SUMMARY heading on p11 to the EXERCISES heading on p13."""
    t = pages[11].split("SUMMARY", 1)[1]
    t = t.split("Figure 19.5")[0]
    t2 = pages[12]
    for junk in ("BIOLOGY", "250", "Reprint 2026-27"):
        t2 = t2.replace(junk, " ")
    return re.sub(r"\s+", " ", t + " " + t2).strip()


def sweep_z(pages, rows):
    body = [r for r in rows
            if r["src"].isdigit() and 1 <= int(r["src"]) <= 10
            and not re.match(r"Figure(\s*\([a-z]\))?\s*labels", r["word"], re.I)]
    summ_rows = [r for r in rows if r["src"].isdigit() and int(r["src"]) in (11, 12)]

    text = get_summary(pages)
    sents = [s.strip() for s in re.split(r"(?<=\.)\s+(?=[A-Z])", text) if s.strip()]

    print("\n" + "=" * 74)
    print("SESSION 1-Z — SUMMARY SENTENCE vs BODY EVIDENCE")
    print("=" * 74)
    print(f"  body rows (Src p1-10)        : {len(body)}")
    print(f"  already-folded summary rows  : {len(summ_rows)} "
          f"({', '.join(r['rid'] for r in summ_rows)})")
    print(f"  SUMMARY sentences split out  : {len(sents)}\n")

    for i, s in enumerate(sents, 1):
        st = toks(s)
        if not st:
            continue
        scored = sorted(((len(st & toks(r["word"])) / len(st), r) for r in body),
                        key=lambda x: -x[0])[:3]
        folded = next((r for r in summ_rows
                       if len(toks(r["word"]) & st) / max(1, len(st)) > 0.75), None)
        tag = f"ALREADY FOLDED -> {folded['rid']}" if folded else ""
        print(f"S{i:02d} [{scored[0][0]:.2f}] {tag}")
        print(f"    {s[:200]}")
        for sc, r in scored:
            print(f"      {sc:.2f}  {r['rid']}  {r['word'][:110]}")
        print()
    return sents


def main():
    pages = load_pages(RAW)
    rows = parse_facts(INV)
    sweep_h(pages, rows)
    sweep_z(pages, rows)
    return 0


if __name__ == "__main__":
    sys.exit(main())
