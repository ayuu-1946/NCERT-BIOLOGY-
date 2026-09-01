"""Gate 3(b) DIRECTION 1: inventory -> delivered PDF.

For every one of the 218 frozen Facts rows, ask whether its *content* is present
in the delivered PDF's text stream. The machine's job is only to guarantee that
no row is skipped and to rank rows by how much of their wording is missing; the
verdict on every flagged row is made by reading it.

Deliberate design notes (each one exists because the naive version lies):

* The PDF is a *rewrite* of NCERT into tables, flows and notes -- not a reprint.
  So exact substring matching is the wrong instrument: it would flag ~all 218
  rows and tell us nothing. We score CONTENT-WORD coverage instead.
* Stopwords are dropped before scoring. A row like "Progesterone supports
  pregnancy." is 1 content word out of 3; scoring function words would let a row
  pass on "the" and "of" alone.
* Greek alpha/beta are folded to `alpha`/`beta` because carry-forward 1 requires
  the PDF to spell them out (check 5 bans Greek from the PDF). Ca2+ / T4 / IP3
  are folded to bare tokens because the PDF sets them with <super>/<sub> tags,
  which extract as separate characters.
* Numbers are kept as content words -- "six trophic hormones", "1 to 2 million",
  "four parathyroid glands" are exactly the marks-critical values a drift would
  damage, so they must not be stopworded away.
* Figure-label rows (F212-F218) are scored per LABEL, not per row, because a row
  holding 9 labels can score 90% while one whole label is absent.
"""
import json
import os
import re
import sys
import unicodedata

import pymupdf

REPO = "/vercel/share/v0-project"
CH = os.path.join(REPO, "notes/class 11/Ch19_ChemicalCoordinationAndIntegration")
NAME = "Ch19_ChemicalCoordinationAndIntegration"
PDF = os.path.join(CH, NAME + ".pdf")
INV = os.path.join(CH, NAME + "_inventory.md")

STOP = set("""a an the and or but of to in on at by for with from as is are was were be been being
it its this that these those their our we you your he she they them there here which who whom whose
also then thus hence however such other others than into over under about across only same both each
per etc eg ie so if not no nor do does did done have has had can may might will would shall should
because while when where what how all any some more most many much few very own out up down off
between during before after above below again further once no nor too s t re ve ll d m o
""".split())

FOLD = {
    "\u03b1": "alpha", "\u03b2": "beta", "\u2013": "-", "\u2014": "-",
    "\u2018": "'", "\u2019": "'", "\u201c": '"', "\u201d": '"', "\u00a0": " ",
}


def norm(s):
    s = unicodedata.normalize("NFKC", s)
    for k, v in FOLD.items():
        s = s.replace(k, v)
    s = s.lower()
    # ionic charge / sub-superscript folding: ca2+ -> ca, t4 -> t4 kept, ip3 -> ip3 kept
    s = s.replace("ca2+", "ca").replace("ca++", "ca")
    s = s.replace("na+", "na").replace("k+", "k")
    return s


def words(s):
    return [w for w in re.findall(r"[a-z0-9]+", norm(s)) if w not in STOP and len(w) > 1]


def pdf_text():
    doc = pymupdf.open(PDF)
    pages = [p.get_text() for p in doc]
    doc.close()
    return pages


def parse_rows():
    rows = []
    for line in open(INV, encoding="utf-8"):
        m = re.match(r"^\|\s*(F\d+)\s*\|([^|]*)\|([^|]*)\|(.*)\|([^|]*)\|([^|]*)\|\s*$", line)
        if not m:
            continue
        fid, sec, typ, wording, src, tick = (x.strip() for x in m.groups())
        rows.append(dict(id=fid, section=sec, type=typ, wording=wording,
                         src=src, tick=tick))
    return rows


def labels_of(wording):
    """Split a figure-label matrix row into its individual quoted labels."""
    return re.findall(r'"([^"]+)"', wording)


def main():
    pages = pdf_text()
    full = norm("\n".join(pages))
    fullwords = set(re.findall(r"[a-z0-9]+", full))

    rows = parse_rows()
    print(f"rows parsed: {len(rows)}  ({rows[0]['id']} .. {rows[-1]['id']})")
    assert len(rows) == 218, f"expected 218 rows, parsed {len(rows)}"

    results = []
    for r in rows:
        if re.match(r"^Figure (\([ab]\) )?labels:", r["wording"]) or r["id"] >= "F212":
            labs = labels_of(r["wording"])
            if labs:
                for i, lab in enumerate(labs):
                    lw = words(lab)
                    hit = [w for w in lw if w in fullwords]
                    results.append(dict(id=f"{r['id']}.L{i+1}", section=r["section"],
                                        type="label", src=r["src"], wording=lab,
                                        n=len(lw), hit=len(hit),
                                        miss=[w for w in lw if w not in fullwords],
                                        cov=len(hit) / max(1, len(lw))))
                continue
        rw = words(r["wording"])
        miss = [w for w in rw if w not in fullwords]
        results.append(dict(id=r["id"], section=r["section"], type=r["type"],
                            src=r["src"], wording=r["wording"], n=len(rw),
                            hit=len(rw) - len(miss), miss=miss,
                            cov=(len(rw) - len(miss)) / max(1, len(rw))))

    labels = [x for x in results if x["type"] == "label"]
    facts = [x for x in results if x["type"] != "label"]
    print(f"scored: {len(facts)} fact rows + {len(labels)} individual figure labels")

    perfect = [x for x in results if not x["miss"]]
    print(f"rows/labels with EVERY content word present in the PDF: "
          f"{len(perfect)}/{len(results)}")

    flagged = sorted((x for x in results if x["miss"]), key=lambda x: x["cov"])
    print(f"\n=== {len(flagged)} rows/labels with >=1 content word absent "
          f"(each must be READ, not scored) ===")
    for x in flagged:
        print(f"\n[{x['id']}] {x['section']} · {x['type']} · src p{x['src']} · "
              f"cov {x['hit']}/{x['n']}")
        print(f"   MISSING WORDS: {x['miss']}")
        print(f"   ROW: {x['wording'][:300]}")

    with open(os.path.join(REPO, "scratch/ch19_gate3b/dir1_results.json"), "w") as f:
        json.dump(results, f, indent=1)


if __name__ == "__main__":
    main()
