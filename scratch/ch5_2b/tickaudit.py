#!/usr/bin/env python3
"""Pass 2 tick audit for Ch5 — direction: inventory row -> generated PDF text.

A row may be ticked only when its facts are demonstrably present in the built
PDF. Because this workflow REWRITES rather than transcribes, verbatim matching
is the wrong test; what must survive is every load-bearing token:

  Tier A (hard)  numbers/measurements and proper nouns  -> a miss is a real gap
  Tier B (soft)  other content words                    -> low coverage = review

Usage:
  python tickaudit.py            # summary + tier-A misses
  python tickaudit.py --all      # also list tier-B low-coverage rows
  python tickaudit.py F123 F124  # detail for specific rows
"""
import re
import sys
import unicodedata

BASE = "notes/class 12/Ch5_MolecularBasisOfInheritance/"
INV = BASE + "Ch5_MolecularBasisOfInheritance_inventory.md"
PDF = BASE + "Ch5_MolecularBasisOfInheritance.pdf"

STOP = set("""a an the and or but if then than that this these those there their them they
it its is are was were be been being of to in on at by for from with without within into
as not no nor so such which who whom whose what when where while how why all any both each
few more most other some only own same too very can will just should now have has had do
does did done also may might must would could shall about above after again against before
below between during further here once out over under up down off again both because
you your we our i he she his her him one two three both many much per cent example
learnt learn class xi xii chapter section figure fig note table see also called call
called known name named term terms thus hence therefore however since given form forms
formed using used use like unlike among along still yet even ever able etc via
""".split())

def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s)
    for a, b in [("\u2018", "'"), ("\u2019", "'"), ("\u201c", '"'), ("\u201d", '"'),
                 ("\u2013", "-"), ("\u2014", "-"), ("\u2212", "-"), ("\u00a0", " "),
                 ("\u2032", "'"), ("\u2033", "'"), ("\u2026", "...")]:
        s = s.replace(a, b)
    s = s.lower()
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def load_pdf_text() -> str:
    import pymupdf
    doc = pymupdf.open(PDF)
    return "\n".join(p.get_text() for p in doc)


def parse_rows():
    rows, in_facts = [], False
    for line in open(INV, encoding="utf-8"):
        line = line.rstrip("\n")
        if line.startswith("## "):
            in_facts = line.strip() == "## Facts"
            continue
        if not in_facts or not re.match(r"\|\s*F\d+\s*\|", line):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 5:
            print("MALFORMED:", line[:80])
            continue
        rows.append(dict(id=cells[0], section=cells[1], type=cells[2],
                         wording=cells[3], ticked=cells[4], raw=line))
    return rows


def payload(r):
    """The text of a row whose presence must be verified."""
    w = r["wording"]
    # drop editorial parentheticals written by the inventory author, keep quotes
    quoted = re.findall(r'"([^"]+)"', w)
    if quoted:
        return " ; ".join(quoted)
    return re.sub(r"\(\*\*.*?\*\*.*?\)", " ", w)


NUM_RE = re.compile(r"\d[\d,\.]*")

def tokens(text):
    """(tier_a, tier_b) token sets for a payload string."""
    t = norm(text)
    a = set(m.group(0).rstrip(".,") for m in NUM_RE.finditer(t))
    # proper nouns: capitalised words in the ORIGINAL casing, not sentence-initial-only
    caps = set()
    for m in re.finditer(r"(?<![.!?\"]\s)(?<!^)\b([A-Z][a-zA-Z']{2,})\b", text, re.M):
        w = m.group(1)
        if w.lower() not in STOP:
            caps.add(w.lower())
    a |= caps
    b = set()
    for w in re.findall(r"[a-z][a-z'\-]{4,}", t):
        w = w.strip("'-")
        if w and w not in STOP and w not in a:
            b.add(w)
    return a, b


def present(tok, hay, hay_nospace):
    if tok in hay:
        return True
    if tok.replace(" ", "") in hay_nospace:
        return True
    # singular/plural and simple morphology
    for v in (tok.rstrip("s"), tok + "s", tok.rstrip("e") + "ing", tok + "es"):
        if len(v) > 3 and v in hay:
            return True
    return False


def main():
    args = [a for a in sys.argv[1:]]
    show_all = "--all" in args
    wanted = [a.upper() for a in args if re.fullmatch(r"[Ff]\d+", a)]

    pdf_text = load_pdf_text()
    hay = norm(pdf_text)
    hay_nospace = hay.replace(" ", "")

    rows = parse_rows()
    hard_miss, soft_low, clean = [], [], []
    for r in rows:
        if r["type"] == "figure-label":
            # gated already by check_pdf.py check 6
            clean.append(r)
            r["verdict"] = "figure-label (check 6)"
            continue
        pl = payload(r)
        A, B = tokens(pl)
        ma = sorted(t for t in A if not present(t, hay, hay_nospace))
        mb = sorted(t for t in B if not present(t, hay, hay_nospace))
        cov = 1.0 if not B else 1 - len(mb) / len(B)
        r.update(A=A, B=B, ma=ma, mb=mb, cov=cov)
        if ma:
            hard_miss.append(r)
        elif cov < 0.5:
            soft_low.append(r)
        else:
            clean.append(r)

    if wanted:
        for r in rows:
            if r["id"] in wanted:
                print("=" * 70)
                print(r["id"], "|", r["section"], "|", r["type"])
                print(r["wording"][:600])
                print("  tierA missing:", r.get("ma"))
                print("  tierB missing:", r.get("mb"))
                print("  coverage: %.2f" % r.get("cov", 1.0))
        return

    print("rows: %d | clean: %d | tier-A misses: %d | tier-B low(<0.5): %d"
          % (len(rows), len(clean), len(hard_miss), len(soft_low)))
    print("\n" + "=" * 70)
    print("TIER-A MISSES (numbers / proper nouns absent from the PDF)")
    print("=" * 70)
    for r in hard_miss:
        print("%s [%s/%s] missing %s" % (r["id"], r["section"], r["type"], r["ma"]))
        print("    %s" % payload(r)[:220].replace("\n", " "))
    if show_all:
        print("\n" + "=" * 70)
        print("TIER-B LOW COVERAGE (<0.5) — review for genuine omission")
        print("=" * 70)
        for r in soft_low:
            print("%s [%s/%s] cov=%.2f missing %s" % (r["id"], r["section"], r["type"],
                                                      r["cov"], r["mb"][:12]))
            print("    %s" % payload(r)[:220].replace("\n", " "))


if __name__ == "__main__":
    main()
