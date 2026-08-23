#!/usr/bin/env python
"""
Gate 1 verbatim verifier for Ch7.

Checks that every double-quoted span in every Facts row actually occurs in the
chapter PDF's text layer. This is the mechanical backstop for `§6`'s "quote, do
not paraphrase" rule: a row whose wording drifted from the book fails here.

Three PDF quirks have to be neutralised first, or the checker reports garbage:

  1. Page furniture. NCERT interleaves a running header
     ("HUMAN HEALTH AND DISEASE 135"), a "Reprint 2026-27" stamp and bare page
     numbers into the text stream. A sentence that straddles a page break gets
     those tokens injected mid-sentence, so they are deleted before matching.

  2. Line-break hyphens. "self-\ncells" and "polymorpho-\nnuclear" are genuine
     hyphenated words in this chapter (proved by "the body attacks self-cells"
     appearing unbroken elsewhere), whereas "differ-\nentiate" is a soft break.
     There is no way to tell them apart from the glyph stream, so each candidate
     is matched against BOTH readings (hyphen kept, hyphen dropped) and passes
     if either occurs.

  3. Bold run-in heads are emitted 5x by the typesetter (the "Cellular barriers
     Cellular barriers Cellular barriers..." artefact), so runs of an immediately
     repeated phrase are collapsed.

Run:  /vercel/share/neetenv/bin/python scratch/ch7_1o/verify_verbatim.py
"""
import pathlib
import re
import sys

import pymupdf

PDF = "Chapter/class 12/Chapter 7 - Human Health and Disease.pdf"
INV = ("notes/class 12/Ch7_HumanHealthAndDisease/"
       "Ch7_HumanHealthAndDisease_inventory.md")

FURNITURE = [
    r"Reprint\s+20\d\d-\d\d",
    r"\(c\)\s*NCERT",
    r"not\s+to\s+be\s+republished",
]

# Running heads. Order matters: strip the header phrase together with the page
# number that hugs it, so a sentence spanning a page break closes up cleanly
# instead of leaving a stray "141" wedged mid-clause.
RUNNING_HEAD = [
    r"\d{0,3}\s*HUMAN\s+HEALTH\s+AND\s+DISEASE\s*\d{0,3}",
    r"\d{0,3}\s*BIOLOGY\s*\d{0,3}",
]

# Figure captions are injected into the text stream at the point the artwork sits,
# which can be the middle of an unrelated sentence (fig 7.7/7.8's captions land
# inside the cancer-genes sentence). The manifest owns caption wording, so they
# are removed here rather than matched.
CAPTIONS = r"Figure\s+7\.\d+\s+[A-Z][^.]{0,70}?(?=\s+[a-z]|\s+Figure\s+7\.|$)"

# Facts rows drop inline "(Figure 7.9)" cross-references, because the figure
# manifest is the single home for figure pointers. Remove them from the haystack
# so an otherwise-verbatim quote is not failed for that documented elision.
XREF = r"\s*\(\s*Figure\s+7\.\d+\s*\)"

failures = []


def check(cond, label):
    print(f"  {'ok  ' if cond else 'FAIL'} {label}")
    if not cond:
        failures.append(label)


def unify(s):
    """Fold typographic variants down to ASCII."""
    for a, b in (("\u2018", "'"), ("\u2019", "'"), ("\u201c", '"'),
                 ("\u201d", '"'), ("\u2013", "-"), ("\u2014", "-"),
                 ("\u2212", "-"), ("\xad", ""), ("\xa0", " "),
                 ("\u2026", "..."), ("\u00b0", " deg ")):
        s = s.replace(a, b)
    return s


def strip_furniture(s):
    for pat in FURNITURE:
        s = re.sub(pat, " ", s, flags=re.I)
    # bare page numbers left stranded between whitespace
    s = re.sub(r"\s\d{2,3}\s", " ", s)
    return s


def collapse_repeats(s):
    """Kill the typesetter's 5x-repeated bold run-in heads."""
    prev = None
    while prev != s:
        prev = s
        s = re.sub(r"\b([A-Z][A-Za-z /-]{3,40}?)(?: \1\b)+", r"\1", s)
    return s


def squash(s):
    return re.sub(r"\s+", " ", s).strip()


def variants(s):
    """Both readings of every line-break hyphen, plus a no-space form."""
    keep = squash(re.sub(r"-\s*\n\s*", "-", s))
    drop = squash(re.sub(r"-\s*\n\s*", "", s))
    return {keep, drop, keep.replace("- ", "-"), drop.replace("- ", "")}


def main():
    root = pathlib.Path(".")
    doc = pymupdf.open(root / PDF)
    raw = "\n".join(doc[p].get_text() for p in range(doc.page_count))

    hay_keep = squash(collapse_repeats(strip_furniture(
        unify(re.sub(r"-\s*\n\s*", "-", raw)))))
    hay_drop = squash(collapse_repeats(strip_furniture(
        unify(re.sub(r"-\s*\n\s*", "", raw)))))
    # a hyphen-insensitive haystack catches the remaining soft-break cases
    hay_nohy = hay_keep.replace("-", "")

    text = (root / INV).read_text()
    row = re.compile(r"^\|\s*(F\d{3})\s*\|([^|]*)\|([^|]*)\|(.*)\|[^|]*\|\s*$")

    rows = []
    for line in text.splitlines():
        m = row.match(line)
        if m:
            rows.append((m.group(1), m.group(2).strip(),
                         m.group(3).strip(), m.group(4)))

    print(f"\nFacts rows parsed: {len(rows)}")
    by_type = {}
    for fid, _sec, typ, _q in rows:
        by_type.setdefault(typ, []).append(fid)

    misses, checked = [], 0
    for fid, _sec, typ, body in rows:
        for quoted in re.findall(r'"([^"]{4,})"', body):
            checked += 1
            cands = variants(unify(quoted))
            hit = any(
                c in hay_keep or c in hay_drop
                or c.replace("-", "") in hay_nohy
                for c in cands
            )
            if not hit:
                misses.append((fid, typ, quoted))

    print(f"Quoted spans checked: {checked}")
    check(not misses, f"every quoted span occurs in the PDF text layer "
                      f"({len(misses)} miss(es))")
    for fid, typ, q in misses:
        print(f"       {fid} [{typ}] {q[:110]}")

    # openers: one per heading, minus EXERCISES which is a bare question list
    heads = by_type.get("heading", [])
    opens = by_type.get("opener", [])
    print(f"\nheading rows: {len(heads)}   opener rows: {len(opens)}")
    check(len(opens) == len(heads) - 1,
          f"openers == headings-1 ({len(opens)} vs {len(heads)}-1); "
          "EXERCISES is the one heading with no prose opener")

    dupes = [t for t in by_type if len(set(by_type[t])) != len(by_type[t])]
    check(not dupes, f"no duplicated IDs within a Type (offenders: {dupes})")

    print("\n" + ("ALL ASSERTIONS PASS" if not failures
                  else f"{len(failures)} ASSERTION(S) FAILED"))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
