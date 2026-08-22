"""Gate 3b Direction 2, second sweep — atom-level, structurally different.

d2 (sentence coverage) has one blind spot by construction: a source sentence
whose whole fact was dropped, but whose *vocabulary* happens to repeat
elsewhere in the inventory, scores high on tok_cover and never reaches the
suspect list. That is exactly the shape of a real Pass-1 gap in a chapter that
says "DNA", "mRNA" and "polymerase" on nearly every page.

So this sweep ignores sentences entirely and checks ATOMS instead — the two
token classes that are (a) heaviest in NEET marking and (b) least likely to be
coincidentally present:

  NUMBERS  — every numeric literal in the source (5386, 3.4, 10^-9, 1953,
             2.2, 64, 20, 24, 28S ...). A missing number is a missing fact,
             full stop.
  PROPER   — every capitalised non-sentence-initial token (Meselson, Nirenberg,
             Escherichia, Alu, EcoRI ...), i.e. names of people, organisms,
             enzymes and institutions.

Presence is tested against the inventory blob, not against sentences, because a
number legitimately reaches the inventory inside a differently-worded row.
Everything absent is printed for the eye read.
"""
import re
import sys
import importlib.util
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path("scratch/ch5_3b_d2")
spec = importlib.util.spec_from_file_location(
    "trace_d1", Path("scratch/ch5_3b/trace_d1.py"))
t1 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(t1)

NUM = re.compile(r"\d+(?:[.,]\d+)?")
PROPER = re.compile(r"\b([A-Z][a-z]{2,})\b")

# capitalised because they open a sentence / are headings / are generic
NOT_NAMES = set("""The This That These Those There Then Thus However While
Since Although Though When Where What Which Who Why How And But For From With
Also Both Each Some Many Most More Such Very Now Here They Their Them About
Into Over Under After Before Above Below Once Only Just Later Soon Very
Figure Table Chapter Summary Exercises Reprint Biology Molecular Basis
Inheritance Note Answer Answers Question Questions Section Chapters Fig
Nucleotide Nucleotides Polymer Sugar Base Bases Phosphate Adenine Guanine
Cytosine Thymine Uracil Purine Purines Pyrimidine Pyrimidines Protein
Proteins Genetic Genes Gene Chromosome Chromosomes Nucleus Cell Cells
Ribose Deoxyribose Histone Histones Chromatin Nucleosome Nucleosomes
Transcription Translation Replication Polymerase Ribosome Ribosomes
Codon Codons Anticodon Mutation Operon Inducer Repressor Promoter Terminator
Enzyme Enzymes Amino Acid Acids Bacteria Bacterial Virus Viruses Phage
Human Genome Project Sequencing Sequence Sequences Length Total Number
Studies Study Later Every During Being Because Being Given Taken Using
Structure Structures Model Double Helix Strand Strands Life Living Organism
Organisms Even Once Whole Part Parts Central Dogma Eukaryotes Prokaryotes
Eukaryotic Prokaryotic""".split())


def main():
    stream, index = t1.build_stream(dehyphen=True)   # normalised, lowercased
    inv_norm = " ".join(
        t1.norm(t1.unquote(r["text"])[0], True) for r in t1.load_rows())
    inv_flat = inv_norm.replace(" ", "")

    # ---- raw (case-preserving) source, same cleaning, for proper nouns ----
    raw_pages = []
    for path in t1.CORPORA:
        for chunk in path.read_text().split("===== PAGE ")[1:]:
            head, _, body = chunk.partition(" =====\n")
            raw_pages.append((int(head), t1.strip_running(body)))

    # ---------------- numbers ----------------
    src_nums = Counter()
    where = defaultdict(set)
    for pno, body in raw_pages:
        for m in NUM.finditer(t1.norm(body, True)):
            src_nums[m.group()] += 1
            where[m.group()].add(pno)
    inv_nums = set(NUM.findall(inv_norm))

    missing_nums = sorted(
        (n for n in src_nums if n not in inv_nums and n.replace(",", "") not in inv_nums),
        key=lambda n: (-src_nums[n], n))
    print(f"distinct numbers in source: {len(src_nums)}   "
          f"in inventory: {len(inv_nums)}   absent: {len(missing_nums)}")
    lines = []
    for n in missing_nums:
        pages = ",".join(str(p) for p in sorted(where[n]))
        lines.append(f"NUM {n!r:12} x{src_nums[n]:<3} pages {pages}")
        print(" ", lines[-1])

    # ---------------- proper nouns ----------------
    src_names = Counter()
    nwhere = defaultdict(set)
    for pno, body in raw_pages:
        for m in PROPER.finditer(body):
            w = m.group(1)
            if w in NOT_NAMES:
                continue
            # sentence-initial? then it is probably not a name
            pre = body[max(0, m.start() - 2):m.start()].strip()
            if pre.endswith(".") or pre == "":
                continue
            src_names[w] += 1
            nwhere[w].add(pno)
    missing_names = sorted(
        (w for w in src_names if w.lower() not in inv_norm
         and w.lower() not in inv_flat),
        key=lambda w: (-src_names[w], w))
    print(f"\ndistinct proper nouns in source: {len(src_names)}   "
          f"absent from inventory: {len(missing_names)}")
    for w in missing_names:
        pages = ",".join(str(p) for p in sorted(nwhere[w]))
        lines.append(f"NAME {w!r:16} x{src_names[w]:<3} pages {pages}")
        print(" ", lines[-1])

    p = HERE / "d2b_atoms.txt"
    p.write_text("\n".join(lines) + "\n")
    print("\nwrote", p)


if __name__ == "__main__":
    sys.exit(main())
