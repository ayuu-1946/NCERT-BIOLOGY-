"""Ch11 Gate 2 aid: locate Facts rows whose content may be absent from the PDF.

Pass 2 EVIDENCE ONLY (SUPREME COMMAND §6): token-coverage may LOCATE suspect
rows; it may never CLOSE Gate 3. Here it is used to decide which of the 270
frozen Facts rows need a human read before their inventory tick is applied.

Method mirrors scratch/ch19_gate3b/dir1_inventory_to_pdf.py:
* the PDF is a rewrite, so we score CONTENT-WORD coverage, not substrings
* stopwords dropped; numbers kept (marks-critical)
* Greek/charge/sub-super folded to the ASCII the PDF is forced to use (check 5)
"""
import json
import os
import re
import unicodedata

import pymupdf

REPO = "/vercel/share/v0-project"
CH = os.path.join(REPO, "notes/class 11/Ch11_PhotosynthesisInHigherPlants")
NAME = "Ch11_PhotosynthesisInHigherPlants"
PDF = os.path.join(CH, NAME + ".pdf")
INV = os.path.join(CH, NAME + "_inventory.md")

STOP = set("""a an the and or but of to in on at by for with from as is are was were be been being
it its this that these those their our we you your he she they them there here which who whom whose
also then thus hence however such other others than into over under about across only same both each
per etc eg ie so if not no nor do does did done have has had can may might will would shall should
because while when where what how all any some more most many much few very own out up down off
between during before after above below again further once too s t re ve ll d m o also within due
""".split())

FOLD = {
    "\u03b1": "alpha", "\u03b2": "beta", "\u03b3": "gamma", "\u0394": "delta",
    "\u2013": "-", "\u2014": "-", "\u2018": "'", "\u2019": "'",
    "\u201c": '"', "\u201d": '"', "\u00a0": " ", "\u2192": " ",
}


def norm(s):
    s = unicodedata.normalize("NFKC", s)
    for k, v in FOLD.items():
        s = s.replace(k, v)
    s = s.lower()
    s = s.replace("co2", "co2").replace("o2", "o2")
    return s


def words(s):
    return [w for w in re.findall(r"[a-z0-9]+", norm(s)) if w not in STOP and len(w) > 1]


def pdf_words():
    doc = pymupdf.open(PDF)
    full = norm("\n".join(p.get_text() for p in doc))
    doc.close()
    return set(re.findall(r"[a-z0-9]+", full))


def parse_facts():
    """Only rows under the '## Facts' section (F001..F270)."""
    rows = []
    in_facts = False
    for line in open(INV, encoding="utf-8"):
        low = line.strip().lower()
        if low.startswith("## "):
            in_facts = low.startswith("## facts")
            continue
        if not in_facts:
            continue
        m = re.match(r"^\|\s*(F\d+)\s*\|([^|]*)\|([^|]*)\|(.*)\|([^|]*)\|\s*$", line)
        if not m:
            continue
        fid, sec, typ, wording, tick = (x.strip() for x in m.groups())
        rows.append(dict(id=fid, section=sec, type=typ, wording=wording, tick=tick))
    return rows


def main():
    fullwords = pdf_words()
    rows = parse_facts()
    print(f"Facts rows parsed: {len(rows)}  ({rows[0]['id']} .. {rows[-1]['id']})")

    results = []
    for r in rows:
        # strip inventory scaffolding phrases that are not chapter content
        w = r["wording"]
        w = re.sub(r'Opening sentence of [\d.]+:', '', w)
        w = re.sub(r'SUMMARY-UNIQUE fold:', '', w)
        w = re.sub(r'Folded into [^.]*\.', '', w)
        w = re.sub(r'(Numbered|Unnumbered)[^:]*heading:', '', w)
        w = re.sub(r'Chapter heading:', '', w)
        rw = words(w)
        miss = [x for x in rw if x not in fullwords]
        results.append(dict(id=r["id"], section=r["section"], type=r["type"],
                            wording=r["wording"], n=len(rw), miss=miss,
                            cov=(len(rw) - len(miss)) / max(1, len(rw))))

    perfect = [x for x in results if not x["miss"]]
    print(f"rows with EVERY content word present: {len(perfect)}/{len(results)}")
    flagged = sorted((x for x in results if x["miss"]), key=lambda x: x["cov"])
    print(f"\n=== {len(flagged)} rows with >=1 content word absent (READ each) ===")
    for x in flagged:
        print(f"\n[{x['id']}] {x['section']} · {x['type']} · cov {x['cov']:.2f} ({x['n']-len(x['miss'])}/{x['n']})")
        print(f"   MISSING: {x['miss']}")
        print(f"   ROW: {x['wording'][:280]}")
    os.makedirs(os.path.join(REPO, "scratch/ch11_gate2"), exist_ok=True)
    with open(os.path.join(REPO, "scratch/ch11_gate2/coverage.json"), "w") as f:
        json.dump(results, f, indent=1)


if __name__ == "__main__":
    main()
