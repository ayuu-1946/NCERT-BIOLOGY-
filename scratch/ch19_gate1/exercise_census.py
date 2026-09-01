#!/usr/bin/env python
r"""Ch19 exercise census, derived by machine with an explicit sub-part rule.

RULE (stated so the count is reproducible and auditable):
  * a QUESTION is a line-initial 'N.' at the left margin of p.13, N in 1..9;
  * a LETTERED SUB-PART is a '(x)' label whose x is a single a-z letter AND
    which STARTS a labelled item, i.e. it sits at start-of-line or after
    whitespace. This second condition is load-bearing, not decoration: Q6's
    stem reads 'Give example(s) of:', and a naive '\(([a-z])\)' scan counts
    that inflectional '(s)' as a sub-part, reporting 40 where the truth is 39.
    A label is never glued to the end of a word; inflection always is.
  * Q9's Column II '(i)..(iv)' are MATCHING OPTIONS, not sub-parts: they are
    the answer set that the Column I sub-parts are matched *against*. They are
    counted separately so the header never has to hide the distinction.
  * '(i)' inside Q3's (a)..(l) run IS a lettered sub-part ('i' the letter), and
    is disambiguated from a roman numeral by the run it belongs to: Q3's labels
    are a contiguous a..l alphabet, Q9 Column II's are a contiguous i..iv roman
    sequence in a second column.
"""
import re, sys
import pdfplumber

SRC = "Chapter/class 11/Chapter 19 - Chemical Coordination and Integration.pdf"
with pdfplumber.open(SRC) as pdf:
    text = pdf.pages[12].extract_text()

# split into question blocks on line-initial 'N.'
lines = text.splitlines()
blocks, cur, qno = {}, [], None
for ln in lines:
    m = re.match(r"^(\d)\.\s", ln)
    if m:
        if qno: blocks[qno] = "\n".join(cur)
        qno, cur = int(m.group(1)), [ln]
    elif qno:
        cur.append(ln)
if qno: blocks[qno] = "\n".join(cur)

ROMAN = {"i","ii","iii","iv","v","vi","vii","viii","ix","x"}
total_lettered = total_roman = 0
print(f"{'Q':>2} | {'lettered sub-parts':<22} | {'roman options':<16}")
print("-"*66)
for q in sorted(blocks):
    labels = re.findall(r"(?:^|(?<=\s))\(([a-z]{1,4})\)", blocks[q], re.M)
    # a contiguous roman run in a second column = matching options (Q9 Col II)
    roman_run = [l for l in labels if l in ROMAN and len(l) > 1]
    if roman_run:  # multi-char romans present -> this block has a roman option set
        romans = [l for l in labels if l in ROMAN and labels.count(l) == 1
                  and l in {"i","ii","iii","iv"}]
        lettered = [l for l in labels if l not in romans]
    else:
        romans, lettered = [], labels
    total_lettered += len(lettered); total_roman += len(romans)
    print(f"{q:>2} | {len(lettered):>2}  {','.join(lettered):<17} | "
          f"{len(romans):>2}  {','.join(romans)}")
print("-"*66)
print(f"questions             : {len(blocks)}")
print(f"lettered sub-parts    : {total_lettered}")
print(f"Q9 Column II options  : {total_roman}")
print(f"labelled items total  : {total_lettered + total_roman}")
