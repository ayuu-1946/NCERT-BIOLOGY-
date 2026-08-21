#!/usr/bin/env python3
"""Direction 2: source -> inventory. Every source sentence must be represented
by some inventory row. Flags sentences whose content words are poorly covered.

This is the direction that can find UNINVENTORIED content (a Pass 1 gap).
"""
import re
import unicodedata

import fitz

SRC = "Chapter/class 12/Chapter 11 - Organisms and Populations.pdf"
INV = ("notes/class 12/Ch11_OrganismsAndPopulations/"
       "Ch11_OrganismsAndPopulations_inventory.md")

FURNITURE = re.compile(
    r"Reprint 2026-27|^\d{3}$|^ORGANISMS AND POPULATIONS$|^BIOLOGY$", re.M)

STOP = set("""a an the of and or to in is are was were be been being that this these those
it its it's for on at as by with from not no nor but so if then than when while
we us our you your they them their he she his her i which who whom what how why
can could may might will would shall should do does did done have has had having
also more most other another such only very much many some any all each both
here there now thus hence therefore however example instead about into over under
between during after before above below out up down off again further once
too s t d n k b e r x per cent""".split())


def norm(s):
    s = unicodedata.normalize("NFKD", s)
    for a, b in [("\u2018", "'"), ("\u2019", "'"), ("\u201c", '"'),
                 ("\u201d", '"'), ("\u2013", "-"), ("\u2014", "-"),
                 ("\u2212", "-"), ("\u00a0", " ")]:
        s = s.replace(a, b)
    return re.sub(r"\s+", " ", s.lower()).strip()


def content_words(s):
    ws = re.findall(r"[a-z]{3,}", norm(s))
    return [w for w in ws if w not in STOP]


doc = fitz.open(SRC)
pages = [p.get_text() for p in doc]

inv_norm = norm(open(INV, encoding="utf-8").read())
inv_words = set(re.findall(r"[a-z]{3,}", inv_norm))

flagged = []
total = 0
for pno, raw in enumerate(pages, 1):
    txt = FURNITURE.sub(" ", raw)
    txt = re.sub(r"\s+", " ", txt)
    # sentence split on . ? ! keeping it simple; NCERT prose is well punctuated
    sents = re.split(r"(?<=[.?!])\s+", txt)
    for s in sents:
        s = s.strip()
        if len(s) < 25:
            continue
        cw = content_words(s)
        if len(cw) < 3:
            continue
        total += 1
        # (a) is a long fragment of the sentence present verbatim?
        ns = norm(s)
        verbatim = ns in inv_norm
        # (b) content-word coverage
        hit = sum(1 for w in cw if w in inv_words)
        ratio = hit / len(cw)
        if not verbatim and ratio < 0.92:
            missing = [w for w in cw if w not in inv_words]
            flagged.append((pno, ratio, s, missing))

print("Source sentences examined:", total)
print("Flagged for manual adjudication:", len(flagged))
print("=" * 72)
for pno, ratio, s, missing in sorted(flagged, key=lambda x: x[1]):
    print("\np%-2d coverage=%.2f  missing words: %s" % (pno, ratio, missing))
    print("   %s" % s[:400])
