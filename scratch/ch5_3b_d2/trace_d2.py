"""Gate 3b Direction 2 — the REVERSE trace: every SOURCE sentence checked for
facts no frozen inventory row covers.

Direction 1 asks "is every row in the source?". That can be 100% green while
the inventory is still missing half a page, because nothing in Direction 1 ever
looks at a source sentence that no row cites. Direction 2 is the only pass that
can find an UNINVENTORIED fact, which per the Ch13 precedent is where genuine
Pass-1 gaps live.

Method (machine-assisted, then eye-read — never machine-only):
  1. Rebuild the same cleaned, column-ordered, header-stripped source stream
     Direction 1 used (trace_d1.norm / strip_running are imported, not
     re-implemented, so the two directions cannot drift apart).
  2. Split it into sentences.
  3. For each sentence, score coverage two independent ways:
       best_ratio  — best difflib ratio against any candidate inventory row
                     (candidates found through an inverted token index, so this
                     stays cheap).
       tok_cover   — fraction of the sentence's CONTENT tokens that appear
                     anywhere in the inventory blob. Catches a sentence whose
                     facts are spread across several rows, which best_ratio
                     alone scores low and would flag as a false gap.
  4. Anything failing BOTH signals is written to d2_suspects.txt for the human
     read. Two signals is deliberate: one signal alone produces a suspect list
     too long to actually eye-read, which is how this step gets skipped.

The machine NEVER issues a verdict. It shortens the list a human must read.
"""
import re
import sys
import difflib
import importlib.util
from collections import Counter
from pathlib import Path

HERE = Path("scratch/ch5_3b_d2")
D1 = Path("scratch/ch5_3b/trace_d1.py")

spec = importlib.util.spec_from_file_location("trace_d1", D1)
t1 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(t1)

# words that carry no fact; their absence from the inventory means nothing
STOP = set("""a an the and or but if of in on at to for from with without by as
is are was were be been being it its this that these those which who whom whose
what when where why how not no nor so than then there here they them their we
us our you your he she his her him i also such very more most much many some
any all both each other another same own can could may might will would shall
should must do does did done have has had having about into over under between
during before after above below up down out off again further once only just
too now e g eg ie viz etc thus hence therefore however while because since
although though upon within among across against per via due able likely
called known seen given taken made using used use uses one two three
""".split())

SENT_SPLIT = re.compile(r"(?<=[a-z\)\'\"])[.?!]\s+(?=[a-z\(\"\'])")
TOKEN = re.compile(r"[a-z0-9][a-z0-9'\-]*")


def content_tokens(s: str):
    return [w for w in TOKEN.findall(s) if w not in STOP and len(w) > 1]


def main():
    HERE.mkdir(parents=True, exist_ok=True)

    stream, index = t1.build_stream(dehyphen=True)

    rows = t1.load_rows()
    bodies = []
    for r in rows:
        body, _annot = t1.unquote(r["text"])
        body = re.sub(r"\s*\[(?:label|heading|opener|figure)[^\]]*\]\s*", " ",
                      body, flags=re.I)
        bodies.append((r["id"], r["type"], t1.norm(body, True)))
    inv_blob = " ".join(b for _i, _t, b in bodies)
    inv_tokens = set(TOKEN.findall(inv_blob))

    # inverted index: content token -> row indices
    inv_index = {}
    for k, (_i, _t, b) in enumerate(bodies):
        for w in set(content_tokens(b)):
            inv_index.setdefault(w, set()).add(k)

    sentences = [s.strip() for s in SENT_SPLIT.split(stream)]
    sentences = [s for s in sentences if len(content_tokens(s)) >= 4]

    out, stats = [], Counter()
    sm = difflib.SequenceMatcher()
    for s in sentences:
        toks = content_tokens(s)
        cover = sum(1 for w in toks if w in inv_tokens) / len(toks)

        cand = Counter()
        for w in set(toks):
            for k in inv_index.get(w, ()):
                cand[k] += 1
        best, best_id = 0.0, ""
        sm.set_seq2(s)
        for k, _shared in cand.most_common(40):
            sm.set_seq1(bodies[k][2])
            r = sm.ratio()
            if r > best:
                best, best_id = r, bodies[k][0]

        off = stream.find(s[:60])
        page = t1.page_of(index, off) if off >= 0 else "?"
        rec = {"page": page, "sent": s, "cover": round(cover, 3),
               "best": round(best, 3), "best_id": best_id,
               "missing": [w for w in dict.fromkeys(toks)
                           if w not in inv_tokens]}
        suspect = best < 0.60 and cover < 0.86
        stats["suspect" if suspect else "covered"] += 1
        if suspect:
            out.append(rec)

    print("sentences scored:", len(sentences))
    print("verdicts:", dict(stats))

    out.sort(key=lambda r: (r["cover"], r["best"]))
    p = HERE / "d2_suspects.txt"
    with p.open("w") as f:
        for r in out:
            f.write(f"=== p{r['page']}  cover={r['cover']} "
                    f"best={r['best']} ({r['best_id']})\n")
            f.write(f"SENT: {r['sent']}\n")
            f.write(f"UNSEEN TOKENS: {', '.join(r['missing'][:18])}\n\n")
    print("wrote", p, f"({len(out)} suspects to eye-read)")


if __name__ == "__main__":
    sys.exit(main())
