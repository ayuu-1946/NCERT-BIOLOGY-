#!/usr/bin/env python3
"""Session 1-S helper — repair RapidOCR's collapsed word spacing (strict mode).

RapidOCR reads the scanned Ch4 pages well (scores 0.93-1.00) but drops the
space between tightly-kerned words, emitting runs like
"littleideaaboutthescientificbasisofthese".

This segmenter is deliberately STRICT: it only splits a run when *every*
resulting piece is a known word (wordfreq zipf >= 2.0, or attested twice in
the chapter's own OCR corpus, or in the domain lexicon).  A run it cannot fully
explain is left alone and REPORTED, so the operator decides by hand rather than
the machine guessing.  That is the whole point — a wrong split silently
rewrites the source, a flagged one does not.
"""
import json
import os
import re
from collections import Counter

from wordfreq import zipf_frequency

HERE = os.path.dirname(os.path.abspath(__file__))

TWO_LETTER = set("of to in at is it as on be we he by or an if no so do go up "
                 "us an am are".split())

DOMAIN_EXTRA = """
Mendel Mendel's Mendelian mendelian genetics genetic genotype phenotype
allele alleles homozygous heterozygous heterozygote homozygote dominant
recessive gamete gametes zygote meiosis mitosis chromosome chromosomes
homologous autosome allosome haploid diploid triploid pollen pollination
emasculation bagging hybridization hybridisation hybrid progeny filial
segregation assortment epistasis pleiotropy polygenic complementation
testcross backcross Punnett punnett Drosophila melanogaster Neurospora
neurospora Pisum sativum Lathyrus odoratus Mirabilis jalapa Antirrhinum
majus snapdragon starch graminifolia primula Oenothera lamarckiana
haemophilia colorblindness colourblindness colour blindness thalassemia
thalassaemia phenylketonuria albinism alkaptonuria sickle anaemia anemia
erythroblastosis foetus fetus syndrome syndromes trisomy monosomy
Klinefelter Turner Cri nondisjunction aneuploidy euploidy polyploidy
mutagen mutagenic mutation mutations frameshift deletion insertion
substitution transition transversion tautomerisation tautomerization
nonsense missense codon codons anticon histones nucleosome nucleosomes
chromatin chromatid chromatids centromere kinetochore telomere satellite
honeybee drone queen workers haplodiploid Xist dosage compensation
pedigree proband carrier carriers genomics linkage recombination
deoxyribose ribose nucleotide nucleotides inbreeding outbreeding heterosis
Griffith Avery Hershey Chase Watson Crick Meselson Stahl Beadle Tatum
Garrod Sutton Boveri Morgan Sturtevant Bridges Muller McClintock Kornberg
Nirenberg Khorana Holley Sanger Mullis Nilsson Ehle East Correns
haemophilic haemophiliac haemoglobin hemoglobin erythrocyte erythrocytes
leukemia leukaemia lymphoma myeloma carcinogen mutagen
Robertsonian translocation inversion duplication
dicentric acentric paracentric pericentric
euploid aneuploid nullisomic monosomic trisomic tetrasomic
amniocentesis chorionic villus karyotype ideogram
autosomal X-linked Y-linked sex-linked holandric
barr Barr Lyon lyonization lyonisation
gynandromorph intersex sexduction
""".split()
DOMAIN = set(w.lower().strip("'") for w in DOMAIN_EXTRA) | set(DOMAIN_EXTRA)


def build_corpus_lexicon(texts):
    c = Counter()
    for t in texts:
        for tok in t.split():
            core = tok.strip(".,;:()[]\"'’")
            if re.fullmatch(r"[A-Za-z][A-Za-z'’]{1,}", core):
                c[core.lower()] += 1
    return {w for w, n in c.items() if n >= 2}


def known(word, lexicon):
    w = word.lower().strip("'’")
    if not w:
        return False
    if len(w) == 1:
        return w in "aAI"
    if len(w) == 2:
        return w.lower() in TWO_LETTER or w.lower() in lexicon
    if w in lexicon or w in DOMAIN:
        return True
    return zipf_frequency(w, "en") >= 2.0


def _score(word, lexicon):
    """Small = confident. Only ever called for words known()."""
    w = word.lower().strip("'’")
    if w in DOMAIN or w in lexicon:
        return 0.3
    z = zipf_frequency(w, "en")
    return max(0.2, 5.0 - z)          # zipf 7 -> 0.2 ; zipf 2 -> 3.0


def split_token(tok, lexicon, max_pieces=5):
    n = len(tok)
    if n < 6:
        return None, None
    INF = 1e9
    best = [INF] * (n + 1)
    pick = [None] * (n + 1)
    best[0] = 0.0
    for i in range(1, n + 1):
        lo = max(0, i - 24)
        for j in range(lo, i):
            if best[j] >= INF:
                continue
            piece = tok[j:i]
            if not known(piece, lexicon):
                continue
            cand = best[j] + _score(piece, lexicon) + 0.9     # per-piece penalty
            if cand < best[i]:
                best[i] = cand
                pick[i] = j
    if pick[n] is None:
        return None, None
    pieces, i = [], n
    while i > 0:
        j = pick[i]
        pieces.append(tok[j:i])
        i = j
    pieces.reverse()
    if len(pieces) < 2:
        return None, None
    return pieces, best[n]


def fix_line(line, lexicon):
    out, repairs, flagged = [], [], []
    for tok in line.split():
        core = re.fullmatch(r"[A-Za-z][A-Za-z'’]{4,}", tok)
        if not core:
            out.append(tok)
            continue
        if known(tok, lexicon) and len(tok) < 12:
            out.append(tok)
            continue
        pieces, cost = split_token(tok, lexicon)
        if pieces:
            out.extend(pieces)
            if pieces != [tok]:
                repairs.append((tok, " ".join(pieces)))
        else:
            out.append(tok)
            flagged.append(tok)
    return " ".join(out), repairs, flagged


def load_lines():
    d = json.load(open(os.path.join(HERE, "ocr_raw.json")))
    return [(int(p), r) for p, rows in d.items() for r in rows]


if __name__ == "__main__":
    entries = load_lines()
    lex = build_corpus_lexicon([r[4] for _, r in entries])
    # two bootstrap rounds: split, rebuild the lexicon from the repaired text,
    # split again - the repaired text exposes many more real words.
    for _ in range(2):
        fixed_lines = [fix_line(r[4], lex)[0] for _, r in entries]
        lex |= build_corpus_lexicon(fixed_lines)
    print("corpus lexicon:", len(lex), "domain:", len(DOMAIN))
    for pno, r in entries:
        fixed, rep, flag = fix_line(r[4], lex)
        if flag:
            print("FLAG  p%02d  %s" % (pno, " ".join(flag)))
    print("--- sample repairs ---")
    for pno, r in entries[:120]:
        fixed, rep, flag = fix_line(r[4], lex)
        if rep:
            print("p%02d  %s" % (pno, " | ".join("%s -> %s" % t for t in rep)))
