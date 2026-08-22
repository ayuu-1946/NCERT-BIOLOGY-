"""Gate 3b Direction 1 — trace every frozen inventory row to the NCERT SOURCE.

Unlike Gate 2's tickaudit.py (which compared rows against our own BUILT PDF, so
both sides of that comparison came from us), this puts the SOURCE on one side.

Three extraction hazards are neutralised first, because each one manufactures
fake "drift" and would drown a real finding:

1. COLUMN INTERLEAVE. p1 carries a section-list sidebar beside body prose, so
   naive extraction shuffles a TOC line into the middle of every intro
   sentence. Fixed by pymupdf block extraction sorted into column bands.
2. RUNNING HEADERS / FOOTERS. A sentence that straddles a page break has
   "Reprint 2026-27", "BIOLOGY" or "MOLECULAR BASIS OF INHERITANCE" spliced
   into it. Fixed by stripping those lines, then concatenating pages into one
   continuous stream (page offsets retained so a hit can still cite its page).
3. AUTHORING TRANSLITERATIONS REQUIRED BY DOCTRINE. The inventory may not
   carry Unicode arrows, Greek letters or true superscripts (check 5), so the
   source's "5'->3'" arrow glyph (which extracts as "a"/"à" from the Symbol
   font), "phi-x174" and "10^-9" are written flat. These are correct authoring,
   never drift, so both sides are compared in a flattened form.

Verdicts:
  EXACT — verbatim substring of the cleaned source under normalisation.
  NEAR  — >= 0.93 best-window difflib ratio; punctuation-level difference only.
  MISS  — neither; MUST be eye-read against the cited source page. NOT
          automatically a defect: heading / opener / figure-label / table rows
          are legitimately not running-prose sentences.
"""
import re
import sys
import difflib
import unicodedata
from collections import Counter
from pathlib import Path

INV = Path("notes/class 12/Ch5_MolecularBasisOfInheritance/"
           "Ch5_MolecularBasisOfInheritance_inventory.md")
CORPORA = [Path("scratch/ch5_3b/source_blocks.txt"),
           Path("scratch/ch5_3b/source_fresh.txt")]

RUNNING = re.compile(
    r"^(?:biology|molecular basis of inheritance|reprint\s*20\d\d-\d\d|\d{1,3})$",
    re.I)

LIG = {"\ufb01": "fi", "\ufb02": "fl", "\ufb00": "ff", "\ufb03": "ffi",
       "\ufb04": "ffl"}
PUNCT = {"\u2018": "'", "\u2019": "'", "\u201c": '"', "\u201d": '"',
         "\u2013": "-", "\u2014": "-", "\u2212": "-", "\u00ad": "",
         "\u00d7": "x", "\u2032": "'", "\u2033": "''", "\u00b7": ".",
         "\u2026": "...", "\u00a0": " "}
SUP = {"\u2070": "0", "\u00b9": "1", "\u00b2": "2", "\u00b3": "3",
       "\u2074": "4", "\u2075": "5", "\u2076": "6", "\u2077": "7",
       "\u2078": "8", "\u2079": "9", "\u207a": "+", "\u207b": "-",
       "\u207f": "n"}
SUB = {"\u2080": "0", "\u2081": "1", "\u2082": "2", "\u2083": "3",
       "\u2084": "4", "\u2085": "5", "\u2086": "6", "\u2087": "7",
       "\u2088": "8", "\u2089": "9"}
SUPRE = re.compile("[" + "".join(SUP) + "]+")
SUBRE = re.compile("[" + "".join(SUB) + "]+")
GREEK = {"\u03c6": "phi", "\u03bb": "lambda", "\u03b1": "alpha",
         "\u03b2": "beta", "\u03b3": "gamma", "\u03bc": "micro"}
# the Symbol-font arrow in this PDF extracts as one of these
ARROWLIKE = re.compile(r"\s*(?:\u2192|\u21d2|\u00e0|\bà\b)\s*")


def strip_running(page_text: str) -> str:
    keep = [ln for ln in page_text.splitlines()
            if not RUNNING.match(ln.strip())]
    return "\n".join(keep)


def norm(s: str, dehyphen: bool = True) -> str:
    for k, v in LIG.items():
        s = s.replace(k, v)
    for k, v in GREEK.items():
        s = s.replace(k, v)
    s = SUPRE.sub(lambda m: "".join(SUP[c] for c in m.group()), s)
    s = SUBRE.sub(lambda m: "".join(SUB[c] for c in m.group()), s)
    s = unicodedata.normalize("NFKC", s)
    for k, v in PUNCT.items():
        s = s.replace(k, v)
    s = s.lower()
    if dehyphen:
        s = re.sub(r"-\s*\n\s*", "", s)
    s = ARROWLIKE.sub("-to-", s)
    s = s.replace("^", "")
    s = re.sub(r"[\s]+", " ", s)
    s = re.sub(r"\s*-\s*", "-", s)      # hyphen spacing is not content
    s = re.sub(r"\s*'\s*", "'", s)      # prime spacing is not content
    return s.strip()


def build_stream(dehyphen: bool):
    """One continuous normalised stream + (start_offset -> page) index."""
    stream_parts, index = [], []
    pos = 0
    for path in CORPORA:
        raw = path.read_text()
        for chunk in raw.split("===== PAGE ")[1:]:
            head, _, body = chunk.partition(" =====\n")
            n = norm(strip_running(body), dehyphen)
            if not n:
                continue
            stream_parts.append(n)
            index.append((pos, pos + len(n), int(head)))
            pos += len(n) + 1
    return " ".join(stream_parts), index


def page_of(index, offset):
    for a, b, p in index:
        if a <= offset <= b:
            return p
    return "?"


def load_rows():
    rows = []
    for line in INV.read_text().splitlines():
        if not line.strip().startswith("|"):
            continue
        c = [x.strip() for x in line.strip().strip("|").split("|")]
        if len(c) >= 5 and re.fullmatch(r"F\d+[a-z]?", c[0]):
            rows.append({"id": c[0], "section": c[1], "type": c[2],
                         "text": c[3], "tick": c[4]})
    return rows


def unquote(t: str):
    """Return (body, annotation).

    An inventory cell is `"the row wording" (authoring note ...)`. The note is
    OUR commentary -- font sizes, trap references, carry-over pointers -- and is
    deliberately NOT source text. Comparing it against the source manufactures
    drift: it was what dragged every heading row to a ~0.4 ratio and hid the
    real signal. Only the FIRST quoted span is the claim about the source.
    """
    t = t.strip()
    m = re.match(r'^["\u201c\u201d](.*?)["\u201c\u201d](.*)$', t, re.S)
    if m:
        return m.group(1).strip(), m.group(2).strip()
    return t, ""


def best_ratio(needle: str, hay: str):
    n = len(needle)
    if n == 0 or n > len(hay):
        return 0.0, ""
    sm = difflib.SequenceMatcher()
    sm.set_seq2(needle)
    best, bestw = 0.0, ""
    step = max(1, n // 6)
    for i in range(0, len(hay) - n + 1, step):
        w = hay[i:i + n + step]
        sm.set_seq1(w)
        if sm.real_quick_ratio() < best or sm.quick_ratio() < best:
            continue
        r = sm.ratio()
        if r > best:
            best, bestw = r, w
    return best, bestw


def main():
    streams = {d: build_stream(d) for d in (True, False)}
    rows = load_rows()
    results = []
    for r in rows:
        body, annot = unquote(r["text"])
        body = re.sub(r"\s*\[(?:label|heading|opener|figure)[^\]]*\]\s*", " ",
                      body, flags=re.I)
        hit_page, verdict, ratio, win = None, "MISS", 0.0, ""
        for d in (True, False):
            stream, index = streams[d]
            n = norm(body, d)
            if n and n in stream:
                hit_page = page_of(index, stream.index(n))
                verdict, ratio = "EXACT", 1.0
                break
        if verdict != "EXACT":
            stream, index = streams[True]
            ratio, win = best_ratio(norm(body, True), stream)
            verdict = "NEAR" if ratio >= 0.93 else "MISS"
        results.append({**r, "verdict": verdict, "page": hit_page or "",
                        "ratio": round(ratio, 3), "window": win,
                        "body": body, "annot": annot})

    print("rows:", len(results))
    print("verdicts:", dict(Counter(x["verdict"] for x in results)))
    print("\nverdict x type:")
    for (v, t), c in sorted(Counter((x["verdict"], x["type"])
                                    for x in results).items()):
        print(f"   {v:6} {t:14} {c}")

    out = Path("scratch/ch5_3b/d1_trace.tsv")
    with out.open("w") as f:
        f.write("id\tsection\ttype\tverdict\tratio\tpage\tbody\twindow\n")
        for x in results:
            f.write(f"{x['id']}\t{x['section']}\t{x['type']}\t{x['verdict']}\t"
                    f"{x['ratio']}\t{x['page']}\t{x['body']}\t{x['window']}\n")
    print("\nwrote", out)


if __name__ == "__main__":
    sys.exit(main())
