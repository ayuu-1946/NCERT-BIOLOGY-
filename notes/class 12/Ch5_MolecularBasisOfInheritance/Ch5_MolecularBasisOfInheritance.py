"""
NCERT Biology -> NEET replacement notes
Class 12, Chapter 5 : Molecular Basis of Inheritance

Source  : Chapter/class 12/Chapter 5 - Molecular Basis of Inheritance.pdf
Built to: SUPREME COMMAND PROMPT.md v6 (fixed-pass gated edition, shared canon module)

Run from the repository root:
    python3 "notes/class 12/Ch5_MolecularBasisOfInheritance/Ch5_MolecularBasisOfInheritance.py"

=== BUILD STATE: PASS 2a (FIRST HALF ONLY) ===
This chapter is a big chapter (646 inventory rows, 19 figures), so it is built under the
§6 big-chapter split protocol: Pass 2 is divided into 2a (first half) and 2b (second half).

  Pass 2a  -- THIS SESSION -- source pp. 1-17, NCERT sections 5.1 .. 5.5.3.
              Inventory rows carried: F001-F264 (facts, headings, openers of the first
              half) + F511-F601 (figure-label rows for figures 5.1-5.10 and the
              unnumbered central-dogma panel). 355 rows total.
  Pass 2b  -- NOT YET WRITTEN -- source pp. 17-33, sections 5.5.4 .. 5.10 + QUICK RECAP
              + APPENDIX, rows F265-F510 and F602-F646.

Because 2b has not run, this file deliberately ends after 5.5.3 and there is NO
QUICK RECAP and NO APPENDIX block yet -- those are chapter-closing blocks and belong to
the pass that finishes the chapter. Do not add them here; do not treat their absence as
a defect of 2a. Pass 3 (layout/vision audit) and the check_pdf.py full gate run only
after 2b, on the complete story.

Figures: every asset in assets/ was clip-extracted at 300 dpi and pushed through
convert_figures_mono.py (PIL convert("L") + autocontrast). figure() re-asserts
mode == "L" at build time, so a raw or colour asset cannot silently reach the PDF (§4.4).

Structure of this file:
  1. Imports from neet_template.py -- the frozen canon (page geometry, colours, Times New
     Roman styles, and every sanctioned helper: heading, keyterm, process_flow, note,
     memory_aid, data_table, figure, title_block). Nothing here redeclares the canon (§0.6).
  2. One linear sequence of story.append(...) calls in Content Order (§5),
     each block commented with its NCERT section number for fast auditing.
"""

import os
import sys

from reportlab.lib.units import cm
from reportlab.platypus import Paragraph, Spacer, KeepTogether

# neet_template.py lives at the repository root; chapter scripts live several
# directories deep, so walk upward from this file until the module is found and
# put that directory on sys.path. This is the standard bootstrap for every
# chapter script (§0.6) -- it lets the file be run directly from anywhere.
_here = os.path.dirname(os.path.abspath(__file__))
_root = _here
while not os.path.exists(os.path.join(_root, "neet_template.py")):
    _parent = os.path.dirname(_root)
    if _parent == _root:
        raise RuntimeError("neet_template.py not found in any parent directory of this script")
    _root = _parent
if _root not in sys.path:
    sys.path.insert(0, _root)

from neet_template import (
    STYLES,
    heading, keyterm, process_flow, note, memory_aid, data_table, title_block,
    build_pdf,
)
from neet_template import figure as _shared_figure

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "assets")
OUT_PDF = os.path.join(HERE, "Ch5_MolecularBasisOfInheritance.pdf")


def figure(asset_name: str, caption_text: str, max_width_cm: float = 15.9):
    """Chapter-local wrapper: binds the shared figure() helper to this chapter's own
    assets/ folder so every call below stays unchanged (asset_name, caption_text,
    max_width_cm=...)."""
    return _shared_figure(asset_name, caption_text, ASSETS, max_width_cm=max_width_cm)


story = []

# --------------------------------------------------------------------------------------
# TITLE BLOCK  (F232 chapter title)
# --------------------------------------------------------------------------------------
story.extend(title_block("MOLECULAR BASIS OF INHERITANCE"))

# Chapter opener: what this chapter is for. F225-F231 carry the chapter's framing -- the
# jump from Mendel's abstract "factor" to the actual molecule.
story.append(Paragraph(
    "In the previous chapter you learnt about inheritance as a pattern: Mendel's "
    "<b>factors</b>, later called <b>genes</b>, passed from parent to offspring in "
    "predictable ratios. That account never said what a gene <i>is</i> made of. This "
    "chapter answers that question at the level of the molecule. It establishes that "
    "<b>DNA</b> is the genetic material, works out how DNA is built and packaged, how it "
    "is copied (<b>replication</b>), how its information is read out into RNA "
    "(<b>transcription</b>), and -- in the second half of the chapter -- how that RNA is "
    "translated into protein and how gene expression is regulated.",
    STYLES["Body"]))
story.append(Paragraph(
    "The logic of the chapter is a chain of questions, each answered experimentally: "
    "What molecule carries heredity? How is it structured? How does it copy itself "
    "faithfully? How is its message expressed? Keep that chain in view -- NEET questions "
    "very often test <i>which experiment proved which link</i>, not just the end result.",
    STYLES["Body"]))
story.append(Spacer(1, 4))
story.append(note(
    "<b>The central dogma.</b> Francis Crick proposed the flow of genetic information in "
    "a cell as DNA to RNA to protein: DNA makes RNA (transcription), and RNA makes "
    "protein (translation). This single arrow-chain is the skeleton on which the whole "
    "chapter hangs, so it is worth fixing before anything else."))
story.append(figure(
    "fig_5_central_dogma.png",
    "The central dogma of molecular biology: DNA is transcribed to RNA, and RNA is "
    "translated to protein. (DNA to RNA to Protein; transcription; translation.)"))

# --------------------------------------------------------------------------------------
# 5.1  THE DNA   (F233 heading, F249 opener, F001-F058 facts)
# --------------------------------------------------------------------------------------
story.append(heading("5.1", "THE DNA", 1))

story.append(keyterm(
    "<b>DNA</b> (deoxyribonucleic acid) is a <b>long polymer of deoxyribonucleotides</b>. "
    "This is the definition NCERT gives for DNA, and the whole of 5.1 unpacks it."))
story.append(Paragraph(
    "The <b>length</b> of a DNA molecule is normally quoted as the <b>number of "
    "nucleotides</b> (or of nucleotide pairs, called <b>base pairs</b>, bp) present in "
    "it. That number is also what defines the size of an organism's genome, so the "
    "figures below are characteristic of the organism.",
    STYLES["Body"]))
story.append(Spacer(1, 3))
story.append(data_table([
    ["Organism / genome", "Length of DNA", "What to notice"],
    ["Bacteriophage <b>phi x 174</b>",
     "<b>5386</b> nucleotides (single-stranded)",
     "The smallest of the standard examples; quoted in <i>nucleotides</i>, not base "
     "pairs, because the DNA is single-stranded."],
    ["Bacteriophage <b>lambda</b>",
     "<b>48502</b> base pairs (bp)",
     "Double-stranded, so quoted in base pairs."],
    ["<b>Escherichia coli</b>",
     "<b>4.6 x 10<super>6</super></b> base pairs",
     "A typical bacterial genome -- about a thousand times the lambda phage."],
    ["<b>Haploid human</b> genome",
     "<b>3.3 x 10<super>9</super></b> base pairs",
     "About 700 times the E. coli genome. This is the number to remember for humans."],
], col_widths=[2.3, 2.3, 4.4]))
story.append(Spacer(1, 4))
story.append(memory_aid(
    "The four standard genome sizes climb in rough powers of ten: phi x 174 about "
    "5 thousand, lambda about 48 thousand, E. coli about 4.6 million, human (haploid) "
    "about 3.3 billion. Remember the sequence <b>5386 - 48502 - 4.6 million - 3.3 "
    "billion</b> as one ladder rather than four unrelated numbers."))

# --- 5.1.1 Structure of Polynucleotide Chain (F234 heading, F250 opener, F001-F051) ---
story.append(heading("5.1.1", "Structure of Polynucleotide Chain", 2))

story.append(Paragraph(
    "Let us recapitulate the chemical structure of a polynucleotide chain, whether DNA or "
    "RNA. A nucleotide is built up in three stages, and each stage adds one component.",
    STYLES["Body"]))
story.append(process_flow([
    "<b>Nitrogenous base.</b> Start with a nitrogen-containing ring compound. There are "
    "two classes: <b>purines</b> and <b>pyrimidines</b>.",
    "<b>Nucleoside = base + sugar.</b> A nitrogenous base is linked to the "
    "<b>pentose sugar</b> through an <b>N-glycosidic linkage</b>, forming a "
    "<b>nucleoside</b> -- for example adenosine or deoxyadenosine, guanosine or "
    "deoxyguanosine, thymidine, cytidine and uridine.",
    "<b>Nucleotide = nucleoside + phosphate.</b> When a <b>phosphate group</b> is linked "
    "to the 5'-OH of a nucleoside through a <b>phosphoester linkage</b>, a corresponding "
    "<b>nucleotide</b> is formed (or deoxynucleotide, depending on the sugar present).",
]))
story.append(Spacer(1, 3))
story.append(Paragraph(
    "The bases fall into two structural classes, and this distinction matters for the "
    "geometry of the helix:",
    STYLES["Body"]))
story.append(data_table([
    ["Class", "Members", "Ring structure"],
    ["<b>Purines</b>", "<b>Adenine (A)</b> and <b>Guanine (G)</b>",
     "Double-ring (fused) bases -- physically the larger of the two classes."],
    ["<b>Pyrimidines</b>",
     "<b>Cytosine (C)</b>, and <b>Thymine (T)</b> in DNA or <b>Uracil (U)</b> in RNA",
     "Single-ring bases -- physically the smaller class."],
], col_widths=[1.6, 3.4, 4.0]))
story.append(Spacer(1, 4))
story.append(note(
    "<b>Cytosine is common to both DNA and RNA.</b> The base that differs is the second "
    "pyrimidine: <b>thymine is present in DNA</b>, while <b>uracil is present in RNA</b> "
    "in its place. Adenine and guanine, the two purines, are common to both."))
story.append(Spacer(1, 3))
story.append(Paragraph(
    "The <b>sugar</b> is the other point of difference between the two nucleic acids. Two "
    "kinds of pentose sugar are found: <b>ribose</b>, present in RNA, and "
    "<b>2'-deoxyribose</b>, present in DNA. Deoxyribose is ribose with the hydroxyl group "
    "at the 2' position replaced by hydrogen -- which is exactly what the prefix "
    "<i>deoxy</i> records.",
    STYLES["Body"]))
story.append(Spacer(1, 4))
story.append(figure(
    "fig_5_1.png",
    "Figure 5.1 Polynucleotide chain. The 5' end carries a phosphate; the chain runs to "
    "the 3' end, which carries a free hydroxyl. Successive sugars are joined by "
    "3'-5' phosphodiester linkages, and each sugar bears a nitrogenous base "
    "(the 5' Phosphate, Nitrogenous base, and 3' OH end are marked)."))

story.append(Paragraph(
    "Two nucleotides are linked through a <b>3'-5' phosphodiester linkage</b> to form a "
    "<b>dinucleotide</b>. More than two nucleotides joined this way give a "
    "<b>polynucleotide chain</b>. Because the linkage always runs from the 3' position of "
    "one sugar to the 5' position of the next, the chain has a direction, and its two "
    "ends are chemically different:",
    STYLES["Body"]))
story.append(data_table([
    ["End of the chain", "What is free there"],
    ["<b>5' end</b>",
     "A free <b>phosphate</b> group at the 5'-OH of the sugar. This is the 5'-end of the "
     "polynucleotide chain."],
    ["<b>3' end</b>",
     "A free <b>3'-OH</b> group (a hydroxyl). This is the 3'-end of the polynucleotide "
     "chain."],
], col_widths=[1.8, 7.2]))
story.append(Spacer(1, 4))
story.append(Paragraph(
    "Stripping the bases off a polynucleotide leaves a repeating <b>sugar-phosphate</b> "
    "backbone, and the nitrogenous bases project from that backbone. In RNA, every "
    "nucleotide residue carries an <b>additional -OH group at the 2' position</b> of the "
    "ribose. RNA also uses uracil in place of thymine -- and note that uracil is simply "
    "<b>5-methyl uracil</b> seen from the other direction: thymine <i>is</i> 5-methyl "
    "uracil.",
    STYLES["Body"]))
story.append(Spacer(1, 3))
story.append(Paragraph(
    "<b>How the double helix was established.</b> In 1953, <b>James Watson</b> and "
    "<b>Francis Crick</b> proposed a strikingly simple but famous <b>Double Helix</b> "
    "model for the structure of DNA. The model rested on two pieces of evidence supplied "
    "by others:",
    STYLES["Body"]))
story.append(process_flow([
    "<b>Base equivalence (Erwin Chargaff).</b> Chargaff's observation that, for a "
    "double-stranded DNA, the <b>ratios between adenine and thymine, and between guanine "
    "and cytosine, are constant and equal one</b>.",
    "<b>X-ray diffraction data.</b> The X-ray diffraction data produced by "
    "<b>Maurice Wilkins</b> and <b>Rosalind Franklin</b>, which gave the physical "
    "dimensions the model had to satisfy.",
]))
story.append(Spacer(1, 3))
story.append(figure(
    "fig_5_2.png",
    "Figure 5.2 A double-stranded polynucleotide chain drawn flat. The two strands run "
    "with opposite polarity -- 5' to 3' on the upper strand and 3' to 5' on the lower -- "
    "and the base pairs A with T and G with C are held together by hydrogen bonds "
    "(the hydrogen bonds are marked; note two between A and T, three between G and C)."))
story.append(Spacer(1, 3))
# Rule 2 gap (inventory exercise-gap scan, Q2; carry-over 18). The body gives Chargaff's
# constant ratios and the A-T / G-C pairing rule but never the step that the four base
# percentages of a duplex sum to 100, so the arithmetic the exercise asks for is
# unreachable. Derived here from those two facts only, as a NOTE box so it reads as the
# rewrite's scaffolding and not as an NCERT sentence.
story.append(note(
    "<b>Working out one base percentage from another.</b> The exercises ask: <i>if a double "
    "stranded DNA has 20 per cent of cytosine, calculate the per cent of adenine.</i> Two "
    "facts already stated above are all you need. Because <b>C pairs only with G</b>, "
    "<b>%C = %G</b>, so <b>%G is also 20</b>. Together C and G therefore account for "
    "<b>40 per cent</b> of the bases. The DNA has <b>only four bases</b>, so their "
    "percentages must <b>add up to 100</b>, leaving <b>60 per cent</b> to be shared by A "
    "and T. Because <b>A pairs only with T</b>, <b>%A = %T</b>, so each is half of 60: "
    "<b>%A = 30 per cent</b> (and %T = 30 per cent). The general form worth remembering is "
    "<b>%A = %T</b>, <b>%G = %C</b>, and <b>%A + %T + %G + %C = 100</b>."))
story.append(Spacer(1, 3))

story.append(Paragraph(
    "The salient features of the Double-helix structure of DNA are these:",
    STYLES["Body"]))
story.append(Paragraph(
    "<bullet>&bull;</bullet> It is made of <b>two polynucleotide chains</b>, where the "
    "<b>backbone is constituted by sugar-phosphate</b>, and the <b>bases project "
    "inside</b>.",
    STYLES["Bullet1"]))
story.append(Paragraph(
    "<bullet>&bull;</bullet> The two chains have <b>anti-parallel polarity</b>. If one "
    "chain has the polarity 5' to 3', the other has 3' to 5'.",
    STYLES["Bullet1"]))
story.append(Paragraph(
    "<bullet>&bull;</bullet> The bases in the two strands are paired through "
    "<b>hydrogen bonds (H-bonds)</b>, forming <b>base pairs (bp)</b>. Adenine forms "
    "<b>two hydrogen bonds</b> with thymine from the opposite strand, and "
    "<b>vice versa</b>. Guanine is bonded with cytosine by <b>three H-bonds</b>. As a "
    "result, <b>always a purine comes opposite to a pyrimidine</b>. This generates "
    "<b>approximately uniform distance between the two strands of the helix</b>.",
    STYLES["Bullet1"]))
story.append(Paragraph(
    "<bullet>&bull;</bullet> The two chains are <b>coiled in a right-handed fashion</b>. "
    "The <b>pitch of the helix is 3.4 nm</b> (a nanometre is one billionth of a metre, "
    "that is 10<super>-9</super> m) and there are roughly <b>10 bp in each turn</b>. "
    "Consequently, the <b>distance between a base pair in a helix is approximately "
    "0.34 nm</b>.",
    STYLES["Bullet1"]))
story.append(Paragraph(
    "<bullet>&bull;</bullet> The <b>plane of one base pair stacks over the other</b> in "
    "the double helix. This, in addition to H-bonds, confers <b>stability of the helical "
    "structure</b>.",
    STYLES["Bullet1"]))
story.append(Spacer(1, 4))
story.append(figure(
    "fig_5_3.png",
    "Figure 5.3 DNA double helix. The two chains are coiled in a right-handed fashion; the "
    "<b>Base pairs</b> lie stacked inside the helix and the <b>Sugar phosphate "
    "backbone</b> runs outside. The pairing legend shows <b>Adenine</b> with "
    "<b>Thymine</b> and <b>Guanine</b> with <b>Cytosine</b>."))
story.append(note(
    "<b>Compare the ring structures, then read the geometry off them.</b> NCERT asks: "
    "compare the structure of purines and pyrimidines, and find out why the distance "
    "between two polynucleotide chains in DNA remains almost constant. Purines are "
    "double-ring (large) and pyrimidines single-ring (small). Since base pairing always "
    "puts a purine opposite a pyrimidine (A with T, G with C), every rung of the ladder "
    "is one large plus one small base -- so every rung spans the same width, and the two "
    "backbones stay an almost constant distance apart. A purine-purine rung would bulge "
    "and a pyrimidine-pyrimidine rung would pinch."))
story.append(Spacer(1, 3))
story.append(memory_aid(
    "Two numbers and two bond-counts carry most of the marks here: pitch <b>3.4 nm</b> "
    "with <b>10 bp per turn</b>, hence <b>0.34 nm</b> per base pair; and "
    "<b>A=T is two H-bonds, G=C is three</b>. The stronger G-C pair (three bonds) is why "
    "GC-rich DNA is harder to melt apart."))

# --- 5.1.2 Packaging of DNA Helix (F235 heading, F251 opener, F059-F079) ---
story.append(heading("5.1.2", "Packaging of DNA Helix", 2))

story.append(Paragraph(
    "Take the distance between two consecutive base pairs as <b>0.34 nm</b> "
    "(0.34 x 10<super>-9</super> m). Then the length of the DNA double helix in a typical "
    "mammalian cell -- with its <b>6.6 x 10<super>9</super> bp</b> (the diploid figure, "
    "twice the haploid 3.3 x 10<super>9</super>) -- comes to "
    "<b>6.6 x 10<super>9</super> bp x 0.34 x 10<super>-9</super> m/bp = 2.2 metres</b>. "
    "A length of DNA far greater than the dimension of a typical nucleus, which is "
    "approximately <b>10<super>-6</super> m</b>. How is such a long polymer packaged in a "
    "cell?",
    STYLES["Body"]))
story.append(Spacer(1, 3))
story.append(note(
    "<b>Working the E. coli figure the other way.</b> NCERT asks: if the length of "
    "E. coli DNA is 1.36 mm, calculate the number of base pairs. Divide length by the "
    "0.34 nm rise per base pair: 1.36 x 10<super>-3</super> m divided by "
    "0.34 x 10<super>-9</super> m/bp = <b>4 x 10<super>6</super> bp</b>, which agrees "
    "with the 4.6 x 10<super>6</super> bp genome quoted for E. coli in 5.1. Length and "
    "base-pair count are interconvertible through the single constant 0.34 nm per bp."))
story.append(Spacer(1, 3))
story.append(Paragraph(
    "<b>In prokaryotes</b>, such as E. coli, though they do not have a defined nucleus, "
    "the DNA is not scattered throughout the cell. It is held (as a large loop) in a "
    "region termed as <b>nucleoid</b>, and the DNA in the nucleoid is organised in large "
    "loops held by proteins.",
    STYLES["Body"]))
story.append(Spacer(1, 3))
story.append(Paragraph(
    "<b>In eukaryotes</b> the packaging is more elaborate, and it begins with a set of "
    "positively charged basic proteins:",
    STYLES["Body"]))
story.append(process_flow([
    "<b>Histones carry positive charge.</b> Histones are rich in the basic amino acid "
    "residues <b>lysine</b> and <b>arginine</b>, both of which carry positive charges in "
    "their side chains. DNA, being an acid, is negatively charged -- so the two bind "
    "electrostatically.",
    "<b>Histone octamer.</b> Histones are organised to form a unit of eight molecules "
    "called a <b>histone octamer</b>.",
    "<b>Nucleosome.</b> The negatively charged DNA is wrapped around the positively "
    "charged histone octamer to form a structure called a <b>nucleosome</b>. A typical "
    "nucleosome contains <b>200 bp of DNA helix</b>.",
    "<b>Chromatin.</b> Nucleosomes constitute the repeating unit of a structure in "
    "nucleus called <b>chromatin</b>, thread-like stained (coloured) bodies seen in "
    "nucleus.",
    "<b>Chromosome.</b> The nucleosomes in chromatin are packed to form "
    "<b>chromatin fibers</b> that are further coiled and condensed at metaphase stage of "
    "cell division to form <b>chromosomes</b>.",
]))
story.append(Spacer(1, 3))
story.append(figure(
    "fig_5_4a.png",
    "Figure 5.4a Nucleosome. The <b>DNA</b> is wrapped around the <b>Histone octamer</b> -- "
    "the <b>Core of histone molecules</b> -- with the <b>H1 histone</b> sitting where the "
    "DNA enters and leaves; a typical nucleosome carries about 200 bp of DNA helix."))
story.append(Paragraph(
    "The packaging of chromatin at higher level requires additional set of proteins that "
    "collectively are referred to as <b>Non-histone Chromosomal (NHC) proteins</b>. In a "
    "typical nucleus, some region of chromatin is loosely packed (and stains light) and "
    "is referred to as <b>euchromatin</b>. The chromatin that is more densely packed and "
    "stains dark is called as <b>heterochromatin</b>. <b>Euchromatin is said to be "
    "transcriptionally active chromatin, whereas heterochromatin is inactive.</b>",
    STYLES["Body"]))
story.append(Spacer(1, 3))
story.append(figure(
    "fig_5_4b.png",
    "Figure 5.4b EM picture -- 'Beads-on-String'. In the electron micrograph the "
    "nucleosomes of chromatin appear as dark beads threaded on the lighter string of the "
    "intervening DNA."))
story.append(Spacer(1, 3))
story.append(note(
    "<b>Counting the nucleosomes in a mammalian cell.</b> NCERT asks how many such beads "
    "you imagine are present in a mammalian cell. With <b>6.6 x 10<super>9</super> bp</b> "
    "of DNA and about <b>200 bp per nucleosome</b>, the estimate is "
    "6.6 x 10<super>9</super> divided by 200, that is approximately "
    "<b>3.3 x 10<super>7</super> nucleosomes</b> -- of the order of thirty million beads "
    "on the string."))
story.append(Spacer(1, 3))
story.append(memory_aid(
    "The packaging hierarchy is a single ladder of increasing order: "
    "<b>DNA to nucleosome (200 bp on a histone octamer) to chromatin to chromatin fiber "
    "to chromosome</b>. For staining and activity, pair them: "
    "<b>eu</b>chromatin is loose, light-staining and <b>active</b>; "
    "<b>hetero</b>chromatin is dense, dark-staining and <b>inactive</b>."))

# --------------------------------------------------------------------------------------
# 5.2  THE SEARCH FOR GENETIC MATERIAL  (F236 heading, F252 opener, F080-F118)
# --------------------------------------------------------------------------------------
story.append(heading("5.2", "THE SEARCH FOR GENETIC MATERIAL", 1))

story.append(Paragraph(
    "Even though the discovery of <b>nuclein</b> by <b>Meischer</b> and the proposition "
    "for principles of inheritance by Mendel were almost at the same time, but the "
    "question of what molecule was actually the genetic material had not been answered. "
    "For a long time, <b>protein</b> was the favoured candidate, because proteins are "
    "chemically diverse and abundant. The experiments in this section settle the question "
    "in favour of DNA.",
    STYLES["Body"]))

# --- Transforming Principle (F237 unnumbered heading, F253 opener) ---
story.append(heading("5.2", "Transforming Principle", 2))

story.append(Paragraph(
    "In <b>1928</b>, <b>Frederick Griffith</b>, in a series of experiments with "
    "<b>Streptococcus pneumoniae</b> (bacterium responsible for pneumonia), witnessed a "
    "miraculous transformation in the bacteria. During the course of his experiment, a "
    "living organism (bacteria) had changed in physical form.",
    STYLES["Body"]))
story.append(Paragraph(
    "When Streptococcus pneumoniae bacteria are grown on a culture plate, some produce "
    "<b>smooth shiny colonies (S)</b> while others produce <b>rough colonies (R)</b>. "
    "This is because the <b>S strain bacteria have a mucous (polysaccharide) coat, while "
    "R strain does not</b>. Mice infected with the S strain (virulent) die from pneumonia "
    "infection but mice infected with the R strain do not develop pneumonia.",
    STYLES["Body"]))
story.append(Spacer(1, 3))
story.append(data_table([
    ["Griffith's injection", "Result in mice", "What it shows"],
    ["<b>S strain</b> (live) injected into mice",
     "Mice <b>die</b>",
     "The S strain is virulent -- the mucous coat protects it."],
    ["<b>R strain</b> (live) injected into mice",
     "Mice <b>live</b>",
     "The R strain, lacking the coat, is non-virulent."],
    ["<b>S strain killed by heat</b>, injected into mice",
     "Mice <b>live</b>",
     "Heat-killed virulent bacteria alone cannot cause disease."],
    ["<b>S strain killed by heat + live R strain</b>, injected into mice",
     "Mice <b>die</b>",
     "The decisive result: something from the dead S cells converted live R into "
     "virulent S."],
], col_widths=[2.9, 1.5, 4.6]))
story.append(Spacer(1, 4))
story.append(Paragraph(
    "Griffith concluded that the <b>R strain bacteria had somehow been transformed by the "
    "heat-killed S strain bacteria</b>. Some <b>'transforming principle'</b>, transferred "
    "from the heat-killed S strain, had enabled the R strain to synthesise a smooth "
    "polysaccharide coat and become virulent. This must be due to the transfer of the "
    "<b>genetic material</b>. However, the <b>biochemical nature of genetic material was "
    "not defined</b> from his experiments.",
    STYLES["Body"]))

# --- Biochemical Characterisation (F238 heading, F254 opener, F101 question) ---
story.append(heading("5.2", "Biochemical Characterisation of Transforming Principle", 2))

story.append(Paragraph(
    "Prior to the work of <b>Oswald Avery, Colin MacLeod and Maclyn McCarty "
    "(1933-44)</b>, the genetic material was thought to be protein. They worked to "
    "determine the biochemical nature of the 'transforming principle' in Griffith's "
    "experiment.",
    STYLES["Body"]))
story.append(Paragraph(
    "They purified biochemicals (proteins, DNA, RNA, etc.) from the heat-killed S cells "
    "to see which ones could transform live R cells into S cells, and then destroyed each "
    "class of molecule in turn with a specific enzyme:",
    STYLES["Body"]))
story.append(data_table([
    ["Treatment of the extract", "Did transformation still occur?", "Conclusion"],
    ["<b>Proteases</b> (digest protein) and <b>RNases</b> (digest RNA) added",
     "<b>Yes</b> -- transformation was <b>not</b> affected",
     "Neither protein nor RNA is the transforming principle."],
    ["<b>DNase</b> (digests DNA) added",
     "<b>No</b> -- DNA digestion <b>did</b> inhibit transformation",
     "DNA is the transforming principle."],
], col_widths=[3.2, 2.6, 3.2]))
story.append(Spacer(1, 4))
story.append(Paragraph(
    "They concluded that <b>DNA is the hereditary material</b>, but not all biologists "
    "were convinced at this stage.",
    STYLES["Body"]))
story.append(Spacer(1, 3))
story.append(note(
    "<b>DNA versus DNase -- do not confuse the two names.</b> NCERT asks whether you can "
    "think of any difference between DNAs and DNase. <b>DNA</b> is the nucleic acid, the "
    "genetic material itself. <b>DNase</b> is an <b>enzyme</b> (a protein) that "
    "<i>degrades</i> DNA -- the suffix <b>-ase</b> marks an enzyme, as in protease "
    "(degrades protein) and RNase (degrades RNA). One is the substrate, the other is the "
    "scissors."))

# --- 5.2.1 The Genetic Material is DNA (F239 heading, F255 opener) ---
story.append(heading("5.2.1", "The Genetic Material is DNA", 2))

story.append(Paragraph(
    "The unequivocal proof that DNA is the genetic material came from the experiments of "
    "<b>Alfred Hershey</b> and <b>Martha Chase (1952)</b>. They worked with viruses that "
    "infect bacteria called <b>bacteriophages</b>.",
    STYLES["Body"]))
story.append(Paragraph(
    "The bacteriophage attaches to the bacteria and its genetic material then enters the "
    "bacterial cell. The bacterial cell treats the viral genetic material as if it was "
    "its own and subsequently manufactures more virus particles. Hershey and Chase worked "
    "to discover whether it was protein or DNA from the viruses that entered the "
    "bacteria. Their design turned on <b>radioactive labelling</b>:",
    STYLES["Body"]))
story.append(process_flow([
    "<b>Label the two candidate molecules differently.</b> They grew some viruses on a "
    "medium that contained <b>radioactive phosphorus</b> and some others on medium with "
    "<b>radioactive sulfur</b>.",
    "<b>Why those two elements.</b> Viruses grown in the presence of radioactive "
    "phosphorus contained <b>radioactive DNA but not radioactive protein</b>, because "
    "<b>DNA contains phosphorus but protein does not</b>. Similarly, viruses grown on "
    "radioactive sulfur contained <b>radioactive protein but not radioactive DNA</b>, "
    "because <b>DNA does not contain sulfur</b>.",
    "<b>Infect and wait.</b> Radioactive phages were allowed to attach to E. coli "
    "bacteria and, as infection proceeded, the viral coats were removed from the bacteria "
    "by agitating them in a <b>blender</b>.",
    "<b>Separate cells from coats.</b> The virus particles were separated from the "
    "bacteria by spinning them in a <b>centrifuge</b>.",
    "<b>Ask which label went inside.</b> Bacteria which were infected with viruses that "
    "had <b>radioactive DNA were radioactive</b>, indicating that DNA was the material "
    "that passed from the virus to the bacteria. Bacteria that were infected with viruses "
    "that had <b>radioactive proteins were not radioactive</b>, indicating that proteins "
    "did not enter the bacteria from the viruses.",
]))
story.append(Spacer(1, 3))
story.append(figure(
    "fig_5_5.png",
    "Figure 5.5 The Hershey-Chase experiment. The two panels follow one "
    "<b>Bacteriophage</b> each through <b>1. Infection</b>, <b>2. Blending</b> and "
    "<b>3. Centrifugation</b>. With the <b>Radioactive (35S) labelled protein "
    "capsule</b>, <b>No Radioactive (35S)</b> is <b>detected in cells</b> and the "
    "<b>Radioactive (35S)</b> is <b>detected in supernatant</b>; with the "
    "<b>Radioactive (32P) labelled DNA</b>, <b>Radioactive (32P)</b> is "
    "<b>detected in cells</b> and <b>No Radioactivity</b> is <b>detected in "
    "supernatant</b>."))
story.append(Paragraph(
    "<b>DNA is therefore the genetic material that is passed from virus to bacteria.</b>",
    STYLES["Body"]))
story.append(Spacer(1, 3))
story.append(memory_aid(
    "The whole Hershey-Chase design rests on two element facts: "
    "<b>DNA has phosphorus but no sulfur; protein has sulfur but no phosphorus</b>. So "
    "<b>32P tracks DNA, 35S tracks protein</b> -- and only the phosphorus label turns up "
    "inside the bacterium. Sequence of the three experiments: "
    "<b>Griffith (something transforms) - Avery, MacLeod and McCarty (that something is "
    "DNA) - Hershey and Chase (unequivocal proof)</b>."))

# --- 5.2.2 Properties of Genetic Material (F240 heading, F256 opener, F118-F124) ---
story.append(heading("5.2.2", "Properties of Genetic Material (DNA versus RNA)", 2))

story.append(Paragraph(
    "From the foregoing discussion, it is clear that the debate between proteins versus "
    "DNA as the genetic material is settled in favour of DNA. But the question of why DNA "
    "is the predominant genetic material, whereas RNA performs the dynamic functions of "
    "messenger and adapter, has to be answered from the <b>differences between the "
    "chemical structures of the two nucleic acid molecules</b>. A molecule that can act "
    "as a genetic material must fulfil the following criteria:",
    STYLES["Body"]))
story.append(process_flow([
    "It should be able to <b>generate its replica</b> (replication).",
    "It should be <b>chemically and structurally stable</b>.",
    "It should provide the <b>scope for slow changes (mutation)</b> that are required for "
    "evolution.",
    "It should be able to <b>express itself</b> in the form of <b>Mendelian "
    "characters</b>.",
]))
story.append(Spacer(1, 3))
story.append(note(
    "<b>Recall the two chemical differences between DNA and RNA.</b> NCERT asks this "
    "directly, and both answers have already appeared in 5.1.1: (i) the <b>sugar</b> -- "
    "RNA has <b>ribose</b>, with an extra -OH at the 2' position, whereas DNA has "
    "<b>2'-deoxyribose</b>; (ii) the <b>pyrimidine base</b> -- RNA has <b>uracil</b> "
    "where DNA has <b>thymine</b>. Every stability argument below follows from these two "
    "differences."))
story.append(Spacer(1, 3))
story.append(Paragraph(
    "Now judge the two nucleic acids against those criteria:",
    STYLES["Body"]))
story.append(data_table([
    ["Criterion", "How DNA and RNA compare"],
    ["<b>Rule-based replication</b>",
     "<b>Both</b> nucleic acids can direct duplication, because the <b>base pairing</b> "
     "and <b>complementarity</b> rules let each strand template the other. Proteins "
     "cannot do this, which straight away rules them out as genetic material."],
    ["<b>Chemical stability</b>",
     "<b>DNA is more stable.</b> The <b>2'-OH group present at every nucleotide in RNA "
     "is a reactive group and makes RNA labile and easily degradable</b>. RNA is also "
     "known to be <b>catalytic, hence reactive</b>. Therefore <b>DNA is chemically "
     "more stable</b> and is the better store of genetic information."],
    ["<b>Thymine versus uracil</b>",
     "The presence of <b>thymine in place of uracil</b> also confers <b>additional "
     "stability</b> to DNA."],
    ["<b>Double versus single strand</b>",
     "The <b>two strands of DNA, being complementary, if separated by heating come "
     "together when appropriate conditions are provided</b>. Further, being "
     "<b>double-stranded, DNA can resist changes brought about by evolution</b> -- one "
     "strand can be repaired using the other as reference."],
    ["<b>Mutation rate</b>",
     "<b>RNA mutates at a faster rate</b>. Consequently, <b>viruses having RNA genome "
     "and having shorter life span mutate and evolve faster</b>."],
    ["<b>Ability to express</b>",
     "<b>RNA can directly code for the synthesis of proteins, hence can easily express "
     "the characters.</b> DNA, however, is <b>dependent on RNA for synthesis of "
     "proteins</b>."],
], col_widths=[2.1, 6.9]))
story.append(Spacer(1, 4))
story.append(Paragraph(
    "Both DNA and RNA are therefore able to <b>mutate</b>. Putting all of this together: "
    "<b>DNA, being more stable, is preferred for storage of genetic information</b>. "
    "For the <b>transmission of genetic information</b>, <b>RNA is better</b>.",
    STYLES["Body"]))
story.append(Spacer(1, 3))
story.append(memory_aid(
    "One split does the work: <b>DNA stores, RNA expresses</b>. Stability comes from what "
    "DNA <i>lacks</i> (no reactive 2'-OH) and what it <i>has</i> (thymine, a second "
    "strand for repair); RNA's reactivity is exactly what makes it a good short-lived "
    "messenger and a catalyst."))

# --------------------------------------------------------------------------------------
# 5.3  RNA WORLD  (F241 heading, F257 opener, F125-F130)
# --------------------------------------------------------------------------------------
story.append(heading("5.3", "RNA WORLD", 1))

story.append(Paragraph(
    "From the foregoing discussion, an immediate question becomes evident -- <b>which is "
    "the first genetic material?</b> The properties just compared give the answer.",
    STYLES["Body"]))
story.append(Paragraph(
    "<b>RNA was the first genetic material.</b> There is now enough evidence to suggest "
    "that essential life processes (such as <b>metabolism</b>, <b>translation</b>, "
    "<b>splicing</b>, etc.) evolved around RNA. <b>RNA used to act as a genetic material "
    "as well as a catalyst</b> -- there are still <b>some important biochemical reactions "
    "in living systems that are catalysed by RNA catalysts and not by protein "
    "enzymes</b>.",
    STYLES["Body"]))
story.append(Paragraph(
    "But <b>RNA being a catalyst was reactive and hence unstable</b>. Therefore, "
    "<b>DNA has evolved from RNA with chemical modifications that make it more "
    "stable</b>. DNA being <b>double stranded and having complementary strand</b> further "
    "<b>resists changes by evolving a process of repair</b>.",
    STYLES["Body"]))

# --------------------------------------------------------------------------------------
# 5.4  REPLICATION  (F242 heading, F258 opener, F131-F180)
# --------------------------------------------------------------------------------------
story.append(heading("5.4", "REPLICATION", 1))

story.append(Paragraph(
    "While proposing the double helical structure for DNA, <b>Watson and Crick had "
    "immediately proposed a scheme for replication of DNA</b>. To quote their original "
    "statement: <i>\"Now our model for deoxyribonucleic acid is, in effect, a pair of "
    "templates, each of which is complementary to the other. We imagine that prior to "
    "duplication the hydrogen bonds are broken, and the two chains unwind and separate. "
    "Each chain then acts as a template for the formation of a new fellow chain, so that "
    "eventually we shall have two pairs of chains, where we only had one before. "
    "Moreover, the sequence of the pairs of bases will have been duplicated "
    "exactly.\"</i>",
    STYLES["Body"]))
story.append(Spacer(1, 3))
story.append(figure(
    "fig_5_6.png",
    "Figure 5.6 Watson-Crick model for semiconservative DNA replication. The parental "
    "double helix unzips from the middle -- the <b>5'</b> and <b>3'</b> ends of the two "
    "separating chains are marked -- and each parental strand templates a new chain by "
    "base pairing (GC, AT, TA, CG rungs), so each daughter helix ends up with one "
    "parental and one newly synthesised strand."))
story.append(Paragraph(
    "The scheme suggested that the two strands would separate and act as a template for "
    "the synthesis of new complementary strands. After the completion of replication, "
    "each DNA molecule would have <b>one parental and one newly synthesised strand</b>. "
    "This scheme was termed as <b>semiconservative DNA replication</b>.",
    STYLES["Body"]))

# --- 5.4.1 The Experimental Proof (F243 heading, F259 opener, F155-F168) ---
story.append(heading("5.4.1", "The Experimental Proof", 2))

story.append(Paragraph(
    "It is now proven that <b>DNA replicates semiconservatively</b>. It was shown first "
    "in <b>Escherichia coli</b> and subsequently in plants and animals. "
    "<b>Matthew Meselson</b> and <b>Franklin Stahl</b> performed the following experiment "
    "in <b>1958</b>:",
    STYLES["Body"]))
story.append(process_flow([
    "They grew <b>E. coli</b> in a medium containing <b>15NH4Cl</b> "
    "(<b>15N is the heavy isotope of nitrogen</b>) as the only nitrogen source for "
    "<b>many generations</b>. The result was that <b>15N was incorporated into newly "
    "synthesised DNA (as well as other nitrogen containing compounds)</b>. This heavy DNA "
    "molecule could be <b>distinguished from normal DNA by centrifugation in a caesium "
    "chloride (CsCl) density gradient</b>. (Note that <b>15N is not a radioactive "
    "isotope</b>, and it can be separated from 14N only based on densities.)",
    "Then they <b>transferred the cells into a medium with normal 14NH4Cl</b> and took "
    "samples at various definite time intervals as the cells multiplied, and "
    "<b>extracted the DNA that remained as double-stranded helices</b>.",
    "The various samples were <b>separated independently on CsCl gradients</b> to measure "
    "the densities of DNA molecules.",
]))
story.append(Spacer(1, 3))
story.append(note(
    "<b>Why a density gradient separates the molecules at all.</b> NCERT asks you to "
    "recall what centrifugal force is and why a molecule with higher mass or density "
    "would sediment faster. Spinning the tube pushes material outward from the axis of "
    "rotation; the denser the molecule, the further down the CsCl gradient it travels "
    "before its density matches the surrounding solution and it stops. So "
    "<b>15N-15N DNA (heaviest) bands lowest, 14N-14N (lightest) bands highest, and the "
    "hybrid 15N-14N bands in between</b> -- the position of a band <i>is</i> the "
    "measurement."))
story.append(Spacer(1, 3))
story.append(Paragraph(
    "The results, read generation by generation, are what make the experiment decisive:",
    STYLES["Body"]))
story.append(data_table([
    ["Time in 14N medium", "Density of the extracted DNA", "Interpretation"],
    ["<b>After 20 minutes</b> (one generation)",
     "<b>Hybrid</b> or <b>intermediate</b> density",
     "Thus, the DNA that was extracted from the culture one generation after the transfer "
     "from 15N to 14N medium had a hybrid density. Each molecule has one heavy (parental) "
     "and one light (new) strand -- exactly the semiconservative prediction."],
    ["<b>After 40 minutes</b> (two generations)",
     "<b>Equal amounts of hybrid DNA and of light DNA</b>",
     "DNA extracted after two generations was composed of equal amounts of hybrid DNA and "
     "of light DNA. The hybrid molecules each yield one hybrid and one fully light "
     "daughter."],
], col_widths=[2.2, 2.6, 4.2]))
story.append(Spacer(1, 4))
story.append(figure(
    "fig_5_7.png",
    "Figure 5.7 Meselson and Stahl's Experiment. Starting from <b>15N-DNA</b>, "
    "<b>20 min</b> in 14N medium gives <b>Generation I</b> (one 15N-DNA strand with one "
    "14N-DNA strand) and <b>40 min</b> gives <b>Generation II</b>. Under "
    "<b>Gravitational force</b> the tubes below show the bands -- 15N15N <b>Heavy</b>, "
    "14N15N <b>Hybrid</b> and 14N14N <b>Light</b> -- the caption noting the "
    "<b>Separation of DNA by Centrifugation</b>."))
story.append(Spacer(1, 2))
story.append(note(
    "<b>Extending the count to 80 minutes.</b> NCERT asks what the proportions of light "
    "and hybrid DNA would be if E. coli were allowed to grow for 80 minutes. Since one "
    "generation is 20 minutes, 80 minutes is <b>four generations</b>, giving "
    "<b>16 molecules</b> from one. The <b>two original heavy strands</b> are conserved "
    "and remain in <b>2 hybrid molecules</b>; the other <b>14 are light</b>. So the "
    "proportion is <b>2 hybrid : 14 light</b>, that is <b>1/8 hybrid and 7/8 light</b>. "
    "The number of hybrid molecules stays fixed at two forever -- only the light ones "
    "multiply."))
story.append(Spacer(1, 3))
story.append(Paragraph(
    "Very similar experiments involving use of radioactive thymidine to detect "
    "distribution of newly synthesised DNA in the chromosomes were performed on "
    "<b>Vicia faba (faba beans)</b> by <b>Taylor and colleagues</b> in <b>1958</b>. The "
    "experiments proved that <b>the DNA in chromosomes also replicate "
    "semiconservatively</b>.",
    STYLES["Body"]))
story.append(Spacer(1, 3))
story.append(memory_aid(
    "Meselson-Stahl in one line: <b>grow heavy, shift to light, watch the bands</b>. "
    "One generation gives <b>all hybrid</b> (this alone kills the conservative model); "
    "two generations give <b>half hybrid, half light</b> (this kills the dispersive "
    "model). The two heavy parental strands are never destroyed, so hybrid molecules stay "
    "at exactly two."))

# --- 5.4.2 The Machinery and the Enzymes (F244 heading, F260 opener, F169-F186) ---
story.append(heading("5.4.2", "The Machinery and the Enzymes", 2))

story.append(Paragraph(
    "In living cells, such as E. coli, the process of replication requires a set of "
    "catalysts (<b>enzymes</b>). The main enzyme is referred to as <b>DNA-dependent DNA "
    "polymerase</b>, since it uses a DNA template to catalyse the polymerisation of "
    "deoxynucleotides. These enzymes are <b>highly efficient</b> because they have to "
    "catalyse polymerisation of a large number of nucleotides in a very short time.",
    STYLES["Body"]))
story.append(Spacer(1, 3))
# Rule 2 gap (inventory exercise-gap scan, Q6; carry-over 18). The body names only
# DNA-dependent DNA polymerase (here) and DNA-dependent RNA polymerase (5.5.1 / 5.5.3);
# the RNA-templated classes are alluded to only by the chapter's own remark that in some
# viruses the flow of information runs in reverse, from RNA to DNA. The grid below names
# the four classes that follow from the chapter's own naming convention -- template first,
# product second -- and adds no enzyme name, organism or number the source does not carry.
story.append(note(
    "<b>Naming the nucleic-acid polymerases.</b> The exercises ask you to <i>list the types "
    "of nucleic acid polymerases</i> by the <b>chemical nature of the template (DNA or "
    "RNA)</b> and the <b>nature of the nucleic acid synthesised from it (DNA or RNA)</b>. "
    "The chapter's own naming convention does the work: the enzyme is named "
    "<b>[template]-dependent [product] polymerase</b>. That gives <b>four</b> "
    "combinations.<br/><br/>"
    "<b>DNA-dependent DNA polymerase</b> -- DNA template, DNA product: the <b>replication</b> "
    "enzyme named in this section. <b>DNA-dependent RNA polymerase</b> -- DNA template, RNA "
    "product: the <b>transcription</b> enzyme of section 5.5. <b>RNA-dependent DNA "
    "polymerase</b> -- RNA template, DNA product: this is the direction the chapter refers "
    "to when it notes that <b>in some viruses the flow of information is in reverse "
    "direction, that is, from RNA to DNA</b>. <b>RNA-dependent RNA polymerase</b> -- RNA "
    "template, RNA product: the remaining combination, used by viruses whose genome is RNA "
    "and which must copy it as RNA."))
story.append(Spacer(1, 3))
story.append(Paragraph(
    "E. coli, that has only <b>4.6 x 10<super>6</super> bp</b>, completes the process of "
    "replication within <b>18 minutes</b>; that means the <b>average rate of "
    "polymerisation has to be approximately 2000 bp per second</b>. Not only do these "
    "enzymes have to be fast, they also have to catalyse the reaction with <b>high degree "
    "of energetic efficiency and accuracy</b>. Failure to do so would lead to mutation, "
    "and further, the <b>DNA molecule being very long, any mistake would result in "
    "mutations</b>.",
    STYLES["Body"]))
story.append(Spacer(1, 3))
story.append(Paragraph(
    "The energetics and the chemistry of the reaction are worth stating explicitly:",
    STYLES["Body"]))
story.append(Paragraph(
    "<bullet>&bull;</bullet> <b>Deoxyribonucleoside triphosphates serve a dual "
    "purpose</b>. In addition to acting as <b>substrates</b>, they provide <b>energy for "
    "polymerisation reaction</b> -- the two terminal phosphates in a nucleoside "
    "triphosphate are high-energy phosphates.",
    STYLES["Bullet1"]))
story.append(Paragraph(
    "<bullet>&bull;</bullet> The <b>energetically less favourable process of separation "
    "of the two strands of the helix</b> means the DNA-dependent DNA polymerases "
    "<b>catalyse polymerisation only in one direction, that is 5' to 3'</b>.",
    STYLES["Bullet1"]))
story.append(Paragraph(
    "<bullet>&bull;</bullet> This single-direction rule creates additional complications. "
    "On one strand -- the <b>template with polarity 3' to 5'</b> -- the replication is "
    "<b>continuous</b>. On the other -- the <b>template with polarity 5' to 3'</b> -- it "
    "is <b>discontinuous</b>. The <b>discontinuously synthesised fragments are later "
    "joined by the enzyme DNA ligase</b>.",
    STYLES["Bullet1"]))
story.append(Paragraph(
    "<bullet>&bull;</bullet> The <b>DNA polymerases on their own cannot initiate the "
    "process of replication</b>. Also, <b>replication does not initiate randomly at any "
    "place in DNA</b>. There is a definite region in E. coli DNA where the replication "
    "originates, and such a region is termed as <b>origin of replication</b>. It is due "
    "to this that <b>a recombinant DNA, if needs to be propagated during (particularly) "
    "in vivo, requires a vector</b> -- a point taken up in Chapter 9.",
    STYLES["Bullet1"]))
story.append(Spacer(1, 4))
story.append(figure(
    "fig_5_8.png",
    "Figure 5.8 Replicating fork. The <b>Template DNA (parental strands)</b> separates at "
    "the fork; on the 3' to 5' template the <b>Newly synthesised strands</b> grow by "
    "<b>Continuous synthesis</b>, while on the 5' to 3' template the growth is by "
    "<b>Discontinuous synthesis</b> -- every arrow still running 5' to 3'."))
story.append(Paragraph(
    "In eukaryotes, the replication of DNA takes place at <b>S-phase of the cell-cycle</b>. "
    "The replication of DNA and cell division cycle should be highly coordinated. A "
    "<b>failure in cell division after DNA replication results into polyploidy</b> (a "
    "chromosomal anomaly).",
    STYLES["Body"]))
story.append(Spacer(1, 3))
story.append(memory_aid(
    "Three consequences all flow from the single rule <b>polymerase works only 5' to "
    "3'</b>: one new strand is <b>continuous</b> and the other <b>discontinuous</b>; "
    "the fragments need <b>ligase</b> to be sealed; and synthesis must start at a defined "
    "<b>origin of replication</b>, not anywhere. Speed benchmark for E. coli: "
    "<b>4.6 million bp in 18 minutes, about 2000 bp per second</b>."))

# --------------------------------------------------------------------------------------
# 5.5  TRANSCRIPTION  (F245 heading, F261 opener, F187-F224)
# --------------------------------------------------------------------------------------
story.append(heading("5.5", "TRANSCRIPTION", 1))

story.append(keyterm(
    "<b>Transcription</b> is the process of copying genetic information from "
    "<b>one strand of the DNA into RNA</b>. The principle of complementarity governs the "
    "process of transcription, except that here <b>adenosine forms base pair with uracil "
    "instead of thymine</b>."))
story.append(Paragraph(
    "However, unlike in replication, where the total DNA is duplicated, in transcription "
    "<b>only a segment of DNA and only one of the strands is copied into RNA</b>. This "
    "raises two questions that the section must answer: why both strands are not copied, "
    "and why only a segment is copied.",
    STYLES["Body"]))
story.append(Paragraph(
    "<b>Why not both strands?</b> There are two reasons. First, if both strands act as a "
    "template, they would code for RNA molecules with <b>different sequences</b> (as "
    "complementarity does not mean identical), and in turn, if they code for proteins, the "
    "sequence of amino acids in the proteins would be different. Hence, <b>one segment of "
    "the DNA would be coding for two different proteins</b>, and this would complicate "
    "the genetic information transfer machinery. Second, the <b>two RNA molecules if "
    "produced simultaneously would be complementary to each other</b>, hence would form a "
    "<b>double-stranded RNA</b>. This would prevent RNA from being translated into "
    "protein and the <b>exercise of transcription would become a futile one</b>.",
    STYLES["Body"]))

# --- 5.5.1 Transcription Unit (F246 heading, F262 opener, F191-F205) ---
story.append(heading("5.5.1", "Transcription Unit", 2))

story.append(Paragraph(
    "A <b>transcription unit</b> in DNA is defined primarily by the <b>three regions</b> "
    "in the DNA:",
    STYLES["Body"]))
story.append(process_flow([
    "A <b>Promoter</b>",
    "The <b>Structural gene</b>",
    "A <b>Terminator</b>",
]))
story.append(Paragraph(
    "Since the two strands have <b>opposite polarity</b> and the DNA-dependent RNA "
    "polymerase also catalyse the polymerisation in only one direction, that is "
    "<b>5' to 3'</b>, the strand that has the polarity <b>3' to 5' acts as a template</b>, "
    "and is referred to as <b>template strand</b>. The other strand which has the polarity "
    "<b>5' to 3'</b> and the sequence same as RNA (except thymine at the place of uracil), "
    "is displaced during transcription. This strand (which does not code for anything) is "
    "referred to as <b>coding strand</b>. All the reference point while defining a "
    "transcription unit is made with the coding strand.",
    STYLES["Body"]))
story.append(Spacer(1, 3))
story.append(data_table([
    ["Region / strand", "Polarity and role"],
    ["<b>Template strand</b>",
     "Polarity <b>3' to 5'</b>. This is the strand actually copied by RNA polymerase."],
    ["<b>Coding strand</b>",
     "Polarity <b>5' to 3'</b>; sequence same as the RNA except thymine in place of "
     "uracil. It is <b>displaced</b> during transcription and <b>does not code for "
     "anything</b> -- despite the name. All reference points of a transcription unit are "
     "written with respect to this strand."],
    ["<b>Promoter</b>",
     "Located <b>towards the 5' end (upstream)</b> of the structural gene. It is a "
     "<b>DNA sequence that provides binding site for RNA polymerase</b>, and the presence "
     "of a promoter in a transcription unit <b>defines the template and coding "
     "strands</b>. By switching its position with the terminator, the definition of "
     "coding and template strands could be reversed."],
    ["<b>Terminator</b>",
     "Located <b>towards the 3' end (downstream)</b> of the coding strand, and it usually "
     "<b>defines the end of the process of transcription</b>."],
], col_widths=[2.0, 7.0]))
story.append(Spacer(1, 4))
story.append(figure(
    "fig_5_9.png",
    "Figure 5.9 Schematic structure of a transcription unit. The <b>Promoter</b> lies "
    "upstream with the <b>Transcription start site</b> arrow on it, then the "
    "<b>Structural gene</b>, and the <b>Terminator</b> downstream; the upper strand runs "
    "3' to 5' and is the <b>Template strand</b>, the lower runs 5' to 3' and is the "
    "<b>Coding strand</b>."))
story.append(Paragraph(
    "There are additional regulatory sequences further upstream or downstream to the "
    "promoter, and an <b>enhancer</b> is one such example.",
    STYLES["Body"]))
story.append(Spacer(1, 3))
story.append(note(
    "<b>Writing the RNA from a given DNA sequence.</b> NCERT gives a DNA duplex and asks "
    "you to write the sequence of RNA transcribed from it. Work in three moves: "
    "(i) identify the <b>template strand</b> -- it is the one with 3' to 5' polarity; "
    "(ii) read it and write the <b>complement</b>; (iii) put <b>U wherever the rule would "
    "give T</b>. The quick check: the finished RNA is identical to the <b>coding "
    "strand</b> with every T replaced by U, and it runs 5' to 3'."))
story.append(Spacer(1, 3))
story.append(memory_aid(
    "The strand names are counter-intuitive and are examined for exactly that reason: the "
    "<b>template strand (3' to 5') is the one that is actually copied</b>, while the "
    "<b>coding strand (5' to 3') codes for nothing</b> and is merely displaced. "
    "Promoter sits <b>upstream (5' side)</b>, terminator <b>downstream (3' side)</b>."))

# --- 5.5.2 Transcription Unit and the Gene (F247 heading, F263 opener, F206-F216) ---
story.append(heading("5.5.2", "Transcription Unit and the Gene", 2))

story.append(keyterm(
    "A <b>gene</b> is defined as the <b>functional unit of inheritance</b>. This is the "
    "only place in the chapter where the gene is formally defined, so the wording is "
    "worth holding on to."))
story.append(Paragraph(
    "Though it is difficult to give a precise definition to gene, but since we know that "
    "the DNA sequence coding for tRNA or rRNA molecule also define a gene, we can say "
    "that <b>a cistron is a segment of DNA coding for a polypeptide</b>, and the "
    "<b>structural gene in a transcription unit could be said as monocistronic (mostly in "
    "eukaryotes) or polycistronic (mostly in bacteria or prokaryotes)</b>.",
    STYLES["Body"]))
story.append(Paragraph(
    "In eukaryotes, the <b>monocistronic structural genes have interrupted coding "
    "sequences</b> -- the genes in eukaryotes are <b>split</b>. The <b>exons</b> are the "
    "coding sequences or expressed sequences: they are the sequences that appear in mature "
    "or processed RNA. The <b>exons are interrupted by introns</b>. The <b>introns</b> or "
    "intervening sequences <b>do not appear in mature or processed RNA</b>.",
    STYLES["Body"]))
story.append(Spacer(1, 3))
story.append(data_table([
    ["Term", "Definition and where it ends up"],
    ["<b>Cistron</b>",
     "A <b>segment of DNA coding for a polypeptide</b>."],
    ["<b>Monocistronic</b>",
     "A structural gene coding for a single polypeptide -- <b>mostly in eukaryotes</b>."],
    ["<b>Polycistronic</b>",
     "A structural gene coding for more than one polypeptide -- <b>mostly in bacteria or "
     "prokaryotes</b>."],
    ["<b>Exon</b>",
     "<b>Coding / expressed sequence</b>. Exons are the sequences that <b>appear in "
     "mature or processed RNA</b>."],
    ["<b>Intron</b>",
     "<b>Intervening sequence</b>. Introns <b>do not appear in mature or processed "
     "RNA</b>; they interrupt the exons."],
], col_widths=[2.0, 7.0]))
story.append(Spacer(1, 4))
story.append(Paragraph(
    "The <b>promoter</b> and the <b>terminator</b> flank the structural gene in a "
    "transcription unit. Regulatory sequences may be defined in a broad sense as "
    "<b>regulatory genes</b>, even though these sequences do not code for any RNA or "
    "protein.",
    STYLES["Body"]))
story.append(Spacer(1, 3))
story.append(memory_aid(
    "<b>EX</b>ons are <b>EX</b>pressed and <b>EX</b>it into the mature RNA; "
    "<b>INT</b>rons are <b>INT</b>ervening and stay <b>IN</b>side the nucleus. "
    "For cistron counts: <b>mono</b>cistronic goes with <b>eukaryotes</b>, "
    "<b>poly</b>cistronic with <b>prokaryotes</b>."))

# --- 5.5.3 Types of RNA and the process of Transcription (F248, F264, F217-F224) ---
story.append(heading("5.5.3", "Types of RNA and the process of Transcription", 2))

story.append(Paragraph(
    "In bacteria, there are <b>three major types of RNAs</b>: <b>mRNA (messenger RNA)</b>, "
    "<b>tRNA (transfer RNA)</b>, and <b>rRNA (ribosomal RNA)</b>. All three RNAs are "
    "needed to synthesise a protein in a cell, and each has a distinct job:",
    STYLES["Body"]))
story.append(data_table([
    ["RNA type", "Role in protein synthesis"],
    ["<b>mRNA</b> (messenger RNA)",
     "Provides the <b>template</b> -- the sequence to be translated."],
    ["<b>tRNA</b> (transfer RNA)",
     "Brings <b>amino acids</b> and <b>reads the genetic code</b>."],
    ["<b>rRNA</b> (ribosomal RNA)",
     "Plays <b>structural and catalytic role</b> during translation."],
], col_widths=[2.4, 6.6]))
story.append(Spacer(1, 4))
story.append(Paragraph(
    "<b>In bacteria, there is a single DNA-dependent RNA polymerase</b> that catalyses "
    "transcription of all types of RNA. The polymerase binds to the promoter and "
    "initiates transcription (<b>initiation</b>). It uses <b>nucleoside "
    "triphosphates</b> as substrate and polymerises in a template-dependent fashion "
    "following the rule of complementarity. Somehow, it also facilitates opening of the "
    "helix and continues elongation. Only a <b>short stretch of RNA remains bound to the "
    "enzyme</b>; once the polymerases reaches the terminator region, the nascent RNA falls "
    "off, so also the RNA polymerase. This results in <b>termination</b> of "
    "transcription.",
    STYLES["Body"]))
story.append(Spacer(1, 3))
story.append(Paragraph(
    "An intriguing question is how the RNA polymerase is able to catalyse all the three "
    "steps -- <b>initiation</b>, <b>elongation</b> and <b>termination</b>. The answer is "
    "that the RNA polymerase is only capable of catalysing the process of elongation. It "
    "<b>associates transiently with initiation-factor (sigma) and termination-factor "
    "(rho)</b> to initiate and terminate the transcription, respectively. "
    "<b>Association with these factors alters the specificity of the RNA polymerase to "
    "either initiate or terminate.</b>",
    STYLES["Body"]))
story.append(Spacer(1, 3))
story.append(process_flow([
    "<b>Initiation.</b> RNA polymerase associates with the <b>initiation factor "
    "(sigma)</b>, binds the promoter and starts transcription.",
    "<b>Elongation.</b> The core RNA polymerase -- the only step it can catalyse "
    "unaided -- opens the helix and polymerises nucleoside triphosphates 5' to 3' "
    "following complementarity.",
    "<b>Termination.</b> On reaching the terminator, and with the "
    "<b>termination factor (rho)</b>, the nascent RNA and the polymerase both fall off.",
]))
story.append(Spacer(1, 4))
story.append(figure(
    "fig_5_10.png",
    "Figure 5.10 Process of transcription in bacteria. <b>Initiation</b>: the <b>RNA "
    "polymerase</b> with the <b>Sigma factor</b> binds the <b>Promoter</b> on the "
    "<b>DNA helix</b>. <b>Elongation</b>: the helix is opened and <b>RNA</b> is "
    "polymerised as the enzyme moves towards the <b>Terminator</b>, sigma having left. "
    "<b>Termination</b>: with the <b>Rho factor</b>, both the <b>RNA</b> and the "
    "<b>RNA Polymerase</b> fall off."))
story.append(Spacer(1, 3))
story.append(memory_aid(
    "Bacterial transcription needs <b>one polymerase plus two factors</b>: "
    "<b>sigma starts</b> it, <b>rho stops</b> it, and the polymerase itself only "
    "elongates. For the three RNAs: <b>mRNA is the message, tRNA transfers the amino "
    "acid, rRNA is the ribosome</b> -- structural and catalytic."))
story.append(Spacer(1, 4))

# ---- 5.5.3 (continued) Transcription in eukaryotes, splicing, capping and tailing ----
# (F225-F231; Figure 5.11 with labels F591-F601). Written in Pass 2b: Pass 2a stopped at
# F224, so this is the tail of 5.5.3 and not a separate numbered section -- NCERT has no
# section 5.5.4.
story.append(Paragraph(
    "In <b>bacteria</b>, since the mRNA does not require any processing to become active, "
    "and also since transcription and translation take place in the same compartment "
    "(there is no separation of cytosol and nucleus in bacteria), many times the "
    "<b>translation can begin much before the mRNA is fully transcribed</b>. Consequently, "
    "the <b>transcription and translation can be coupled in bacteria</b>.",
    STYLES["Body"]))
story.append(Spacer(1, 3))
story.append(Paragraph(
    "In <b>eukaryotes</b>, there are <b>two additional complexities</b>.",
    STYLES["Body"]))
story.append(Paragraph(
    "<b>(i)</b> There are <b>at least three RNA polymerases in the nucleus</b> (in addition "
    "to the RNA polymerase found in the organelles). There is a <b>clear cut division of "
    "labour</b>:",
    STYLES["Body"]))
story.append(data_table([
    ["Enzyme", "What it transcribes"],
    ["<b>RNA polymerase I</b>",
     "Transcribes <b>rRNAs</b> -- the <b>28S, 18S and 5.8S</b> rRNAs."],
    ["<b>RNA polymerase II</b>",
     "Transcribes the <b>precursor of mRNA</b>, the <b>heterogeneous nuclear RNA "
     "(hnRNA)</b>."],
    ["<b>RNA polymerase III</b>",
     "Transcribes <b>tRNA</b>, <b>5srRNA</b> and <b>snRNAs</b> (small nuclear RNAs)."],
], col_widths=[2.4, 6.6]))
story.append(Spacer(1, 4))
story.append(Paragraph(
    "<b>(ii)</b> The second complexity is that the <b>primary transcripts contain both the "
    "exons and the introns and are non-functional</b>. Hence, it is subjected to a process "
    "called <b>splicing</b> where the <b>introns are removed and exons are joined in a "
    "defined order</b>.",
    STYLES["Body"]))
story.append(Spacer(1, 3))
story.append(Paragraph(
    "hnRNA undergoes <b>additional processing called as capping and tailing</b>. In "
    "<b>capping</b>, an unusual nucleotide (<b>methyl guanosine triphosphate</b>) is added "
    "to the <b>5'-end</b> of hnRNA. In <b>tailing</b>, <b>adenylate residues (200-300)</b> "
    "are added at the <b>3'-end</b> in a <b>template independent manner</b>. It is the "
    "<b>fully processed hnRNA, now called mRNA</b>, that is <b>transported out of the "
    "nucleus for translation</b>.",
    STYLES["Body"]))
story.append(Spacer(1, 3))
story.append(process_flow([
    "<b>Transcription.</b> RNA polymerase II copies the split gene into <b>hnRNA</b>, "
    "which still carries every <b>Exon</b> and every <b>Intron</b>.",
    "<b>Capping.</b> Methyl guanosine triphosphate is added at the <b>5'</b> end -- the "
    "<b>Cap</b>.",
    "<b>Tailing / Polyadenylation.</b> 200-300 adenylate residues are added at the "
    "<b>3'</b> end, template independently -- the <b>Poly A tail</b>.",
    "<b>RNA splicing.</b> Introns are excised and exons joined in a defined order, giving "
    "the mature <b>Messenger RNA</b>.",
    "<b>Export.</b> The fully processed <b>3' mRNA</b> leaves the nucleus for "
    "translation.",
]))
story.append(Spacer(1, 4))
story.append(figure(
    "fig_5_11.png",
    "Figure 5.11 Process of transcription in eukaryotes. The primary transcript carries "
    "<b>Exon</b> and <b>Intron</b> stretches; <b>Capping</b> adds the <b>Cap</b> at the "
    "<b>5'</b> end and <b>Polyadenylation</b> adds the <b>Poly A tail</b> at the <b>3'</b> "
    "end, then <b>RNA splicing</b> removes the introns to give the mature "
    "<b>Messenger RNA</b> -- the <b>3' mRNA</b> that is exported for translation."))
story.append(Spacer(1, 3))
story.append(Paragraph(
    "The <b>significance of such complexities is now beginning to be understood</b>. The "
    "<b>split-gene arrangements represent probably an ancient feature of the genome</b>. "
    "The <b>presence of introns is reminiscent of antiquity</b>, and the <b>process of "
    "splicing represents the dominance of RNA-world</b>. In recent times, the understanding "
    "of RNA and RNA-dependent processes in the living system have assumed more importance.",
    STYLES["Body"]))
story.append(Spacer(1, 3))
story.append(memory_aid(
    "Eukaryotic processing in order: <b>cap the 5' end, tail the 3' end, then splice</b>. "
    "Remember the polymerase division of labour by the <b>rRNA / mRNA / tRNA</b> order of "
    "<b>I / II / III</b> -- polymerase <b>II</b> is the one that matters most in this "
    "chapter because it makes <b>hnRNA</b>, the precursor of mRNA. And note the contrast "
    "that NEET likes: in <b>bacteria</b> transcription and translation are <b>coupled</b> "
    "(no processing, no nucleus); in <b>eukaryotes</b> they are separated by processing and "
    "by the nuclear envelope."))


# --------------------------------------------------------------------------------------
# 5.6  GENETIC CODE
# --------------------------------------------------------------------------------------
# ---- 5.6 (F483 heading, F496 opener, F265-F291, Table 5.1 = F280) ----
story.append(heading("5.6", "GENETIC CODE", 1, has_table=True))

story.append(Paragraph(
    "During replication and transcription a nucleic acid was copied to form another "
    "nucleic acid. Hence, these <b>processes are easy to conceptualise on the basis of "
    "complementarity</b>. The process of <b>translation</b> requires <b>transfer of genetic "
    "information from a polymer of nucleotides to synthesise a polymer of amino acids</b>. "
    "<b>Neither does any complementarity exist between nucleotides and amino acids, nor "
    "could any be drawn theoretically.</b>",
    STYLES["Body"]))
story.append(Paragraph(
    "There existed ample evidences, though, to support the notion that <b>change in nucleic "
    "acids (genetic material) were responsible for change in amino acids in proteins</b>. "
    "This led to the <b>proposition of a genetic code that could direct the sequence of "
    "amino acids during synthesis of proteins</b>.",
    STYLES["Body"]))
story.append(Spacer(1, 3))
story.append(Paragraph(
    "If determining the biochemical nature of genetic material and the structure of DNA was "
    "very exciting, the <b>proposition and deciphering of genetic code were most "
    "challenging</b>. In a very true sense, it required involvement of <b>scientists from "
    "several disciplines -- physicists, organic chemists, biochemists and geneticists</b>.",
    STYLES["Body"]))
story.append(Spacer(1, 3))
story.append(data_table([
    ["Who", "Contribution to the genetic code"],
    ["<b>George Gamow</b><br/>(a physicist)",
     "Argued that since there are <b>only 4 bases</b> and if they have to <b>code for 20 "
     "amino acids</b>, the <b>code should constitute a combination of bases</b>. He "
     "suggested that in order to code for all the 20 amino acids, the <b>code should be "
     "made up of three nucleotides</b>. This was a <b>very bold proposition</b>, because a "
     "permutation combination of <b>4^3 (4 x 4 x 4) would generate 64 codons</b> -- "
     "generating <b>many more codons than required</b>."],
    ["<b>Har Gobind Khorana</b>",
     "The <b>chemical method</b> he developed was instrumental in <b>synthesising RNA "
     "molecules with defined combinations of bases</b> (<b>homopolymers and "
     "copolymers</b>)."],
    ["<b>Marshall Nirenberg</b>",
     "His <b>cell-free system for protein synthesis</b> finally <b>helped the code to be "
     "deciphered</b>."],
    ["<b>Severo Ochoa</b>",
     "His enzyme (<b>polynucleotide phosphorylase</b>) was also helpful in <b>polymerising "
     "RNA with defined sequences in a template independent manner</b> (enzymatic synthesis "
     "of RNA)."],
], col_widths=[2.0, 7.0]))
story.append(Spacer(1, 3))
story.append(Paragraph(
    "<b>Providing proof that the codon was a triplet, was a more daunting task.</b> "
    "Finally a <b>checker-board for genetic code was prepared</b>, which is given in "
    "<b>Table 5.1</b>.",
    STYLES["Body"]))
story.append(Spacer(1, 4))

# --------------------------------------------------------------------------------------
# Table 5.1 -- the 64-codon checker-board.
#
# Inventory carry-over 9 and 17: the 64 cells of the source table are NOT text-extractable
# (get_text returns no usable row/column order) and the table is not a figure, so session
# 1-F does not own it and it had no owner at all. Carry-over 17 required an owner to be
# named before Pass 2a; Pass 2a did not build it. It is built here, in the section that
# refers to it, because two in-body exercises (F288/F289) explicitly instruct the student
# to "take help of the checkerboard" and are unanswerable without it.
#
# The grid is generated from the mapping below rather than typed out as 64 literal cells,
# so that a proof-read is a read of 64 short entries in codon order instead of a read of
# rendered table syntax. Order is NCERT's: first base down the rows, second base across
# the columns, third base within each cell in U, C, A, G order.
# --------------------------------------------------------------------------------------
_BASES = ("U", "C", "A", "G")
_CODONS = {
    "UUU": "Phe", "UUC": "Phe", "UUA": "Leu", "UUG": "Leu",
    "UCU": "Ser", "UCC": "Ser", "UCA": "Ser", "UCG": "Ser",
    "UAU": "Tyr", "UAC": "Tyr", "UAA": "Stop", "UAG": "Stop",
    "UGU": "Cys", "UGC": "Cys", "UGA": "Stop", "UGG": "Trp",
    "CUU": "Leu", "CUC": "Leu", "CUA": "Leu", "CUG": "Leu",
    "CCU": "Pro", "CCC": "Pro", "CCA": "Pro", "CCG": "Pro",
    "CAU": "His", "CAC": "His", "CAA": "Gln", "CAG": "Gln",
    "CGU": "Arg", "CGC": "Arg", "CGA": "Arg", "CGG": "Arg",
    "AUU": "Ile", "AUC": "Ile", "AUA": "Ile", "AUG": "Met",
    "ACU": "Thr", "ACC": "Thr", "ACA": "Thr", "ACG": "Thr",
    "AAU": "Asn", "AAC": "Asn", "AAA": "Lys", "AAG": "Lys",
    "AGU": "Ser", "AGC": "Ser", "AGA": "Arg", "AGG": "Arg",
    "GUU": "Val", "GUC": "Val", "GUA": "Val", "GUG": "Val",
    "GCU": "Ala", "GCC": "Ala", "GCA": "Ala", "GCG": "Ala",
    "GAU": "Asp", "GAC": "Asp", "GAA": "Glu", "GAG": "Glu",
    "GGU": "Gly", "GGC": "Gly", "GGA": "Gly", "GGG": "Gly",
}
assert len(_CODONS) == 64, f"codon table must have 64 cells, has {len(_CODONS)}"
assert sum(1 for v in _CODONS.values() if v == "Stop") == 3, "there must be exactly 3 stop codons"


def _codon_cell(first: str, second: str) -> str:
    """The four codons sharing a first and second base, third base in U, C, A, G order."""
    lines = []
    for third in _BASES:
        codon = first + second + third
        aa = _CODONS[codon]
        marker = " <b>(Stop)</b>" if aa == "Stop" else ""
        shown = "" if aa == "Stop" else " " + aa
        lines.append(f"<b>{codon}</b>{shown}{marker}")
    return "<br/>".join(lines)


_codon_rows = [["1st base", "2nd base: U", "2nd base: C", "2nd base: A", "2nd base: G"]]
for _first in _BASES:
    _codon_rows.append(
        [f"<b>{_first}</b>"] + [_codon_cell(_first, _second) for _second in _BASES])

story.append(Paragraph(
    "<b>Table 5.1 The Codons for the Various Amino Acids</b>", STYLES["Body"]))
story.append(data_table(_codon_rows, col_widths=[0.7, 2.075, 2.075, 2.075, 2.075],
                        font_size=8))
story.append(Spacer(1, 3))
story.append(note(
    "<b>How to read the checker-board.</b> Take the codon's <b>first base from the row</b>, "
    "its <b>second base from the column</b>, and find the line inside that cell whose "
    "<b>third base</b> matches -- the third base always runs <b>U, C, A, G</b> down the "
    "cell. So <b>AUG</b> is row <b>A</b>, column <b>U</b>, third line <b>G</b>: "
    "<b>Met</b>. Reading the whole board confirms the counts quoted in the salient "
    "features below -- <b>64 codons</b> in all, of which <b>61 code for amino acids</b> and "
    "<b>3 (UAA, UAG, UGA) are stop codons</b>."))
story.append(Spacer(1, 4))

story.append(Paragraph(
    "The <b>salient features of genetic code</b> are as follows:", STYLES["Body"]))
story.append(data_table([
    ["Feature", "Statement"],
    ["<b>(i) Triplet</b>",
     "The <b>codon is triplet</b>. <b>61 codons code for amino acids</b> and <b>3 codons "
     "do not code for any amino acids</b>, hence they <b>function as stop codons</b>."],
    ["<b>(ii) Degenerate</b>",
     "<b>Some amino acids are coded by more than one codon</b>, hence the <b>code is "
     "degenerate</b>."],
    ["<b>(iii) Contiguous</b>",
     "The <b>codon is read in mRNA in a contiguous fashion</b>. <b>There are no "
     "punctuations.</b>"],
    ["<b>(iv) Nearly universal</b>",
     "The <b>code is nearly universal</b>: for example, <b>from bacteria to human UUU "
     "would code for Phenylalanine (phe)</b>. <b>Some exceptions to this rule have been "
     "found in mitochondrial codons, and in some protozoans.</b>"],
    ["<b>(v) AUG is dual</b>",
     "<b>AUG has dual functions.</b> It <b>codes for Methionine (met)</b>, and it also "
     "<b>act as initiator codon</b>."],
    ["<b>(vi) Stop codons</b>",
     "<b>UAA, UAG, UGA are stop terminator codons.</b>"],
], col_widths=[2.1, 6.9]))
story.append(Spacer(1, 4))
story.append(note(
    "<b>Worked exercise (NCERT, in-body).</b> <i>If following is the sequence of "
    "nucleotides in mRNA, predict the sequence of amino acid coded by it (take help of the "
    "checkerboard):</i> <b>-AUG UUU UUC UUC UUU UUU UUC-</b>. Reading Table 5.1 codon by "
    "codon: AUG = <b>Met</b>, UUU = <b>Phe</b>, UUC = <b>Phe</b>, UUC = <b>Phe</b>, "
    "UUU = <b>Phe</b>, UUU = <b>Phe</b>, UUC = <b>Phe</b>. So the peptide is "
    "<b>Met-Phe-Phe-Phe-Phe-Phe-Phe</b>.<br/><br/>"
    "<i>Now try the opposite. Following is the sequence of amino acids coded by an mRNA. "
    "Predict the nucleotide sequence in the RNA:</i> <b>Met-Phe-Phe-Phe-Phe-Phe-Phe</b>. "
    "<i>Do you face any difficulty in predicting the opposite?</i> Yes -- and that is the "
    "point of the question. <b>Met</b> is unambiguous (only <b>AUG</b>), but each "
    "<b>Phe</b> could be <b>UUU or UUC</b>, so six positions have two choices each and the "
    "answer is not unique.<br/><br/>"
    "<i>Can you now correlate which two properties of genetic code you have learnt?</i> "
    "The forward direction works unambiguously because the code is a <b>triplet</b> read "
    "<b>contiguously without punctuation</b>; the reverse direction is ambiguous because "
    "the code is <b>degenerate</b>. Degeneracy is why translation is one-way readable: "
    "<b>codon to amino acid is certain, amino acid to codon is not</b>."))
story.append(Spacer(1, 3))
story.append(memory_aid(
    "Fix the numbers: <b>4 bases, triplet code, 4^3 = 64 codons, 61 coding + 3 stop, for "
    "20 amino acids</b>. The three stops are <b>UAA, UAG, UGA</b> -- remember them as "
    "<b>U-A-A / U-A-G / U-G-A</b>, all beginning with U. <b>AUG</b> is the one codon with "
    "<b>two jobs</b>: <b>start</b> and <b>Met</b>. And keep the two contrasted properties "
    "straight: <b>degenerate</b> = one amino acid, many codons; <b>unambiguous</b> = one "
    "codon, never two amino acids."))


# ---- 5.6.1 Mutations and Genetic Code (F484 heading, F497 opener, F292-F305) ----
story.append(heading("5.6.1", "Mutations and Genetic Code", 2))

story.append(Paragraph(
    "The <b>relationships between genes and DNA are best understood by mutation "
    "studies</b>. You have studied about <b>mutation and its effect in Chapter 4</b>.",
    STYLES["Body"]))
story.append(Paragraph(
    "Effects of <b>large deletions and rearrangements</b> in a segment of DNA are easy to "
    "comprehend. It may result in <b>loss or gain of a gene and so a function</b>. The "
    "effect of <b>point mutations</b> will be explained here.",
    STYLES["Body"]))
story.append(Spacer(1, 3))
story.append(keyterm(
    "A <b>classical example of point mutation</b> is a <b>change of single base pair in the "
    "gene for beta globin chain</b> that results in the <b>change of amino acid residue "
    "glutamate to valine</b>. It results into a diseased condition called as <b>sickle cell "
    "anemia</b>."))
story.append(Paragraph(
    "Effect of point mutations that <b>inserts or deletes a base</b> in a structural gene "
    "can be better understood by the following simple example. Consider a statement that is "
    "made up of the following words <b>each having three letters like genetic code</b>:",
    STYLES["Body"]))
story.append(Spacer(1, 2))
story.append(data_table([
    ["What is done to the sentence", "How it now reads"],
    ["The original statement (every word a triplet)",
     "<b>RAM HAS RED CAP</b>"],
    ["<b>Insert one letter</b> B in between HAS and RED, and rearrange",
     "<b>RAM HAS BRE DCA P</b>"],
    ["<b>Insert two letters</b> at the same place, say <b>BI</b>",
     "<b>RAM HAS BIR EDC AP</b>"],
    ["<b>Insert three letters</b> together, say <b>BIG</b>",
     "<b>RAM HAS BIG RED CAP</b>"],
    ["<b>Delete one letter</b> (R), and rearrange",
     "<b>RAM HAS EDC AP</b>"],
    ["<b>Delete two letters</b> (R, E), and rearrange",
     "<b>RAM HAS DCA P</b>"],
    ["<b>Delete three letters</b> (R, E, D), and rearrange",
     "<b>RAM HAS CAP</b>"],
], col_widths=[4.6, 4.4]))
story.append(Spacer(1, 4))
story.append(Paragraph(
    "The <b>conclusion from the above exercise is very obvious</b>. <b>Insertion or "
    "deletion of one or two bases changes the reading frame from the point of insertion or "
    "deletion.</b> However, such mutations are referred to as <b>frameshift insertion or "
    "deletion mutations</b>.",
    STYLES["Body"]))
story.append(Paragraph(
    "<b>Insertion or deletion of three or its multiple bases</b> insert or delete in one or "
    "multiple codon hence <b>one or multiple amino acids</b>, and the <b>reading frame "
    "remains unaltered from that point onwards</b>.",
    STYLES["Body"]))
story.append(Spacer(1, 3))
story.append(memory_aid(
    "The whole point of <b>RAM HAS RED CAP</b> is the <b>multiple-of-three rule</b>: "
    "add or remove <b>1 or 2</b> bases and every codon downstream is garbled -- a "
    "<b>frameshift</b>; add or remove <b>3 or a multiple of 3</b> and you only gain or lose "
    "whole amino acids, with the <b>reading frame intact</b>. Note the contrast NEET tests: "
    "<b>sickle cell anemia is a substitution</b> (one base pair changed, glutamate to "
    "valine), <b>not</b> a frameshift."))


# ---- 5.6.2 tRNA - the Adapter Molecule (F485 heading, F498 opener, F306-F313; Fig 5.12) ----
story.append(heading("5.6.2", "tRNA - the Adapter Molecule", 2))

story.append(Paragraph(
    "From the very beginning of the proposition of code, it was <b>clear to Francis "
    "Crick</b> that there has to be a <b>mechanism to read the code and also to link it to "
    "the amino acids</b>, because <b>amino acids have no structural specialities to read "
    "the code uniquely</b>. He postulated the <b>presence of an adapter molecule</b> that "
    "would <b>on one hand read the code and on other hand would bind to specific amino "
    "acids</b>.",
    STYLES["Body"]))
story.append(Spacer(1, 3))
story.append(Paragraph(
    "The <b>tRNA, then called sRNA (soluble RNA)</b>, was <b>known before the genetic code "
    "was postulated</b>. However, its <b>role as an adapter molecule was assigned much "
    "later</b>.",
    STYLES["Body"]))
story.append(Spacer(1, 3))
story.append(keyterm(
    "<b>tRNA has an anticodon loop that has bases complementary to the code</b>, and it "
    "also has an <b>amino acid acceptor end to which it binds to amino acids</b>. "
    "<b>tRNAs are specific for each amino acid.</b>"))
story.append(Paragraph(
    "For <b>initiation</b>, there is <b>another specific tRNA</b> that is referred to as "
    "<b>initiator tRNA</b>. <b>There are no tRNAs for stop codons.</b>",
    STYLES["Body"]))
story.append(Spacer(1, 3))
story.append(Paragraph(
    "In Figure 5.12, the <b>secondary structure of tRNA</b> has been depicted that "
    "<b>looks like a clover-leaf</b>. In <b>actual structure, the tRNA is a compact "
    "molecule which looks like inverted L</b>.",
    STYLES["Body"]))
story.append(Spacer(1, 4))
story.append(figure(
    "fig_5_12.png",
    "Figure 5.12 tRNA -- the adapter molecule. The clover-leaf secondary structure of "
    "<b>tRNA</b> carries its amino acid at the acceptor end (shown for <b>Ser</b> and "
    "<b>Tyr</b>) and its <b>Anticodon</b> on the <b>anticodon loop</b>, which pairs with "
    "the matching <b>Codon</b> on the <b>mRNA</b> running <b>5'</b> to <b>3'</b>."))
story.append(Spacer(1, 3))
story.append(memory_aid(
    "tRNA is the <b>adapter</b>: <b>two ends, two jobs</b> -- the <b>anticodon loop reads "
    "the mRNA codon</b> by complementarity, the <b>amino acid acceptor end carries the "
    "amino acid</b>. Two shape facts are examined against each other: the <b>secondary</b> "
    "structure is a <b>clover-leaf</b>, the <b>actual</b> three-dimensional structure is an "
    "<b>inverted L</b>. And remember the two absences: <b>no tRNA for stop codons</b>, but "
    "there <b>is</b> a special <b>initiator tRNA</b>."))


# --------------------------------------------------------------------------------------
# 5.7  TRANSLATION
# --------------------------------------------------------------------------------------
# ---- 5.7 (F486 heading, F499 opener = the chapter's only definition of translation,
#      F314-F335, F507 summary-unique; Figure 5.13 labels F611-F623) ----
story.append(heading("5.7", "TRANSLATION", 1))

story.append(keyterm(
    "<b>Translation</b> refers to the <b>process of polymerisation of amino acids to form a "
    "polypeptide</b>. The <b>order and sequence of amino acids are defined by the sequence "
    "of bases in the mRNA</b>."))
story.append(Paragraph(
    "The <b>amino acids are joined by a bond which is known as a peptide bond</b>. "
    "<b>Formation of a peptide bond requires energy.</b> Therefore, in the <b>first phase "
    "itself amino acids are activated in the presence of ATP and linked to their cognate "
    "tRNA</b> -- a process commonly called as <b>charging of tRNA</b> or <b>aminoacylation "
    "of tRNA</b> to be more specific.",
    STYLES["Body"]))
story.append(Paragraph(
    "If <b>two such charged tRNAs are brought close enough</b>, the <b>formation of peptide "
    "bond between them would be favoured energetically</b>. The <b>presence of a catalyst "
    "would enhance the rate of peptide bond formation</b>.",
    STYLES["Body"]))
story.append(Spacer(1, 3))
story.append(keyterm(
    "The <b>cellular factory responsible for synthesising proteins is the ribosome</b>. The "
    "ribosome consists of <b>structural RNAs and about 80 different proteins</b>."))
story.append(Paragraph(
    "In its <b>inactive state, it exists as two subunits: a large subunit and a small "
    "subunit</b>. When the <b>small subunit encounters an mRNA</b>, the <b>process of "
    "translation of the mRNA to protein begins</b>. There are <b>two sites in the large "
    "subunit</b>, for <b>subsequent amino acids to bind to</b> and thus, be <b>close enough "
    "to each other for the formation of a peptide bond</b>. The <b>ribosome also acts as a "
    "catalyst (23S rRNA in bacteria is the enzyme -- ribozyme) for the formation of peptide "
    "bond</b>.",
    STYLES["Body"]))
story.append(Spacer(1, 3))
story.append(data_table([
    ["Region of the mRNA", "What it is"],
    ["<b>Translational unit</b>",
     "A <b>translational unit in mRNA is the sequence of RNA that is flanked by the start "
     "codon (AUG) and the stop codon and codes for a polypeptide</b>."],
    ["<b>Untranslated regions (UTR)</b>",
     "An mRNA also has some <b>additional sequences that are not translated</b> and are "
     "referred as <b>untranslated regions (UTR)</b>. The <b>UTRs are present at both "
     "5'-end (before start codon) and at 3'-end (after stop codon)</b>. They are "
     "<b>required for efficient translation process</b>."],
], col_widths=[2.4, 6.6]))
story.append(Spacer(1, 4))
story.append(process_flow([
    "<b>Charging / aminoacylation.</b> Amino acids are <b>activated in the presence of "
    "ATP</b> and <b>linked to their cognate tRNA</b>.",
    "<b>Initiation.</b> The <b>ribosome binds to the mRNA at the start codon (AUG)</b> "
    "that is <b>recognised only by the initiator tRNA</b>.",
    "<b>Elongation.</b> Complexes of an <b>amino acid linked to tRNA</b> sequentially bind "
    "the <b>appropriate codon in mRNA by forming complementary base pairs with the tRNA "
    "anticodon</b>; the <b>ribosome moves from codon to codon along the mRNA</b> and "
    "<b>amino acids are added one by one</b>, translated into <b>Polypeptide</b> sequences "
    "dictated by DNA and represented by mRNA.",
    "<b>Termination.</b> A <b>release factor binds to the stop codon</b>, "
    "<b>terminating translation</b> and <b>releasing the complete polypeptide from the "
    "ribosome</b>.",
]))
story.append(Spacer(1, 4))
story.append(figure(
    "fig_5_13.png",
    "Figure 5.13 Translation. The <b>Ribosome</b> moves along the <b>mRNA</b> from "
    "<b>5'</b> to <b>3'</b> while each <b>tRNA</b> delivers its amino acid to the "
    "<b>Growing polypeptide chain</b> -- here the residues <b>Gly</b>, <b>Leu</b>, "
    "<b>Tyr</b>, <b>Ser</b>, <b>Ala</b>, <b>Val</b> and <b>Asn</b>."))
story.append(Spacer(1, 3))
story.append(note(
    "<b>Why translation is evidence for the RNA world.</b> Look at what does the work in "
    "this section: the <b>message is RNA</b> (mRNA), the <b>adapter is RNA</b> (tRNA), and "
    "the <b>catalyst is RNA</b> (the 23S rRNA ribozyme). Proteins are the product, not the "
    "machinery. <b>Translation is a process that has evolved around RNA, indicating that "
    "life began around RNA.</b>"))
story.append(Spacer(1, 3))
story.append(memory_aid(
    "Two ribosome facts answer the common two-mark question <i>\"list two essential roles "
    "of the ribosome\"</i>: it provides the <b>two binding sites in the large subunit</b> "
    "that hold successive amino acids close enough to react, and its <b>23S rRNA acts as a "
    "ribozyme</b> catalysing the peptide bond. Remember <b>charging comes before "
    "initiation</b> -- ATP is spent activating the amino acid, not making the peptide bond "
    "directly. UTRs sit <b>outside</b> the start and stop codons and are <b>not "
    "translated</b>, yet are needed for efficient translation."))


# --------------------------------------------------------------------------------------
# 5.8  REGULATION OF GENE EXPRESSION
# --------------------------------------------------------------------------------------
# ---- 5.8 (F487 heading, F500 opener = the chapter's only definition of regulation of
#      gene expression, F336-F349, F508 summary-unique) ----
story.append(heading("5.8", "REGULATION OF GENE EXPRESSION", 1))

story.append(keyterm(
    "<b>Regulation of gene expression</b> refers to a <b>very broad term that may occur at "
    "various levels</b>. Considering that <b>gene expression results in the formation of a "
    "polypeptide</b>, it can be <b>regulated at several levels</b>."))
story.append(Paragraph(
    "In <b>eukaryotes</b>, the regulation could be exerted at:",
    STYLES["Body"]))
story.append(data_table([
    ["Level", "What is regulated there"],
    ["<b>(i) Transcriptional level</b>", "Formation of the <b>primary transcript</b>."],
    ["<b>(ii) Processing level</b>", "<b>Regulation of splicing.</b>"],
    ["<b>(iii) Transport</b>",
     "<b>Transport of mRNA from nucleus to the cytoplasm.</b>"],
    ["<b>(iv) Translational level</b>", "<b>Translation</b> of the mRNA itself."],
], col_widths=[2.4, 6.6]))
story.append(Spacer(1, 4))
story.append(Paragraph(
    "The <b>genes in a cell are expressed to perform a particular function or a set of "
    "functions</b>. For example, if an enzyme called <b>beta-galactosidase</b> is "
    "synthesised by <b>E. coli</b>, it is used to <b>catalyse the hydrolysis of a "
    "disaccharide, lactose into galactose and glucose</b>; the <b>bacteria use them as a "
    "source of energy</b>. Hence, if the <b>bacteria do not have lactose around them</b> to "
    "be utilised for energy source, they would <b>no longer require the synthesis of the "
    "enzyme beta-galactosidase</b>.",
    STYLES["Body"]))
story.append(Spacer(1, 3))
story.append(keyterm(
    "Therefore, in simple terms, it is the <b>metabolic, physiological or environmental "
    "conditions that regulate the expression of genes</b>. The <b>development and "
    "differentiation of embryo into adult organisms</b> are also a result of the "
    "<b>coordinated regulation of expression of several sets of genes</b>."))
story.append(Spacer(1, 3))
story.append(note(
    "<b>Why regulation is not optional.</b> <b>Since transcription and translation are "
    "energetically very expensive processes, these have to be tightly regulated.</b> A cell "
    "that transcribed and translated every gene all the time would spend its energy budget "
    "producing enzymes for substrates that are not there."))
story.append(Spacer(1, 3))
story.append(Paragraph(
    "In <b>prokaryotes, control of the rate of transcriptional initiation is the "
    "predominant site for control of gene expression</b>. In a transcription unit, the "
    "<b>activity of RNA polymerase at a given promoter is in turn regulated by interaction "
    "with accessory proteins</b>, which <b>affect its ability to recognise start sites</b>. "
    "These <b>regulatory proteins can act both positively (activators) and negatively "
    "(repressors)</b>.",
    STYLES["Body"]))
story.append(Spacer(1, 3))
story.append(keyterm(
    "The <b>accessibility of promoter regions of prokaryotic DNA</b> is in many cases "
    "<b>regulated by the interaction of proteins with sequences termed operators</b>. The "
    "<b>operator region is adjacent to the promoter elements in most operons</b> and in "
    "most cases the <b>sequences of the operator bind a repressor protein</b>."))
story.append(Paragraph(
    "<b>Each operon has its specific operator and specific repressor.</b> For example, "
    "<b>lac operator is present only in the lac operon</b> and it <b>interacts specifically "
    "with lac repressor only</b>.",
    STYLES["Body"]))
story.append(Spacer(1, 3))
story.append(memory_aid(
    "Note the <b>qualifier</b>, because it is the difference between a right and a wrong "
    "answer: it is <b>in prokaryotes</b> that <b>transcriptional initiation</b> is the "
    "<b>predominant</b> control point. In eukaryotes there are <b>four</b> levels -- "
    "<b>transcription, processing, transport, translation</b>. Regulatory proteins come in "
    "two signs: <b>activators (positive)</b> and <b>repressors (negative)</b>."))


# ---- 5.8.1 The Lac operon (F488 heading, F501 opener = sole source of Jacob and Monod,
#      F350-F372, F509 summary-unique; Figure 5.14 labels F624-F636;
#      Rule 2 gap Q10 = NOTE box after F371, per inventory carry-over 18) ----
story.append(heading("5.8.1", "The Lac operon", 2))

story.append(Paragraph(
    "The <b>elucidation of the lac operon</b> was also a result of a <b>close association "
    "between a geneticist, Francois Jacob and a biochemist, Jacque Monod</b>. They were the "
    "<b>first to elucidate a transcriptionally regulated system</b>.",
    STYLES["Body"]))
story.append(Spacer(1, 3))
story.append(keyterm(
    "In <b>lac operon</b> (here <b>lac refers to lactose</b>), a <b>polycistronic "
    "structural gene is regulated by a common promoter and regulatory genes</b>. Such "
    "arrangement is <b>very common in bacteria</b> and is referred to as <b>operon</b>. "
    "<b>Lac operon is the prototype operon in bacteria</b>, which codes for genes "
    "<b>responsible for metabolism of lactose</b>."))
story.append(Paragraph(
    "To name few such examples: <b>lac operon, trp operon, ara operon, his operon, val "
    "operon</b>, etc.",
    STYLES["Body"]))
story.append(Spacer(1, 3))
story.append(Paragraph(
    "The <b>lac operon consists of one regulatory gene (the i gene</b> -- here the <b>term "
    "i does not refer to inducer, rather it is derived from the word inhibitor</b>) <b>and "
    "three structural genes (z, y, and a)</b>.",
    STYLES["Body"]))
story.append(data_table([
    ["Gene", "Product and its job"],
    ["<b>i gene</b> (regulatory)",
     "Codes for the <b>repressor of the lac operon</b>. It is synthesised "
     "<b>all-the-time (constitutively)</b>."],
    ["<b>z gene</b>",
     "Codes for <b>beta-galactosidase (beta-gal)</b>, which is <b>primarily responsible "
     "for the hydrolysis of the disaccharide, lactose into its monomeric units, galactose "
     "and glucose</b>."],
    ["<b>y gene</b>",
     "Codes for <b>permease</b>, which <b>increases permeability of the cell to "
     "beta-galactosides</b>."],
    ["<b>a gene</b>",
     "Encodes a <b>transacetylase</b>."],
], col_widths=[2.1, 6.9]))
story.append(Spacer(1, 4))
story.append(Paragraph(
    "Hence, <b>all the three gene products in lac operon are required for metabolism of "
    "lactose</b>. In <b>most other operons as well, the genes present in the operon are "
    "needed together to function in the same or related metabolic pathway</b>.",
    STYLES["Body"]))
story.append(Spacer(1, 3))
story.append(keyterm(
    "<b>Lactose is the substrate for the enzyme beta-galactosidase and it regulates "
    "switching on and off of the operon.</b> Hence, it is termed as <b>inducer</b>."))
story.append(Paragraph(
    "In the <b>absence of a preferred carbon source such as glucose</b>, if <b>lactose is "
    "provided in the growth medium</b> of the bacteria, the <b>lactose is transported into "
    "the cells through the action of permease</b>. (Remember, a <b>very low level of "
    "expression of lac operon has to be present in the cell all the time</b>, otherwise "
    "<b>lactose cannot enter the cells</b>.) The lactose then <b>induces the operon</b> in "
    "the following manner.",
    STYLES["Body"]))
story.append(Spacer(1, 3))
story.append(process_flow([
    "The <b>repressor of the operon is synthesised (all-the-time -- constitutively) from "
    "the i gene</b>, as <b>Repressor mRNA</b> and then <b>Repressor</b> protein.",
    "<b>In absence of inducer:</b> the <b>Repressor binds to the operator region (o) and "
    "prevents RNA polymerase from transcribing the operon</b>.",
    "<b>In presence of inducer:</b> in the presence of an <b>inducer, such as lactose or "
    "allolactose, the repressor is inactivated by interaction with the inducer</b> -- an "
    "<b>Inactive repressor</b>.",
    "This <b>allows RNA polymerase access to the promoter and transcription proceeds</b>, "
    "giving <b>lac mRNA</b>.",
    "<b>Transcription</b> then <b>Translation</b> of that polycistronic message yields "
    "<b>beta-galactosidase</b>, <b>permease</b> and <b>transacetylase</b>.",
]))
story.append(Spacer(1, 4))
story.append(figure(
    "fig_5_14.png",
    "Figure 5.14 The lac operon. <b>In absence of inducer</b>, the <b>Repressor mRNA</b> "
    "from the i gene gives the <b>Repressor</b>, and the <b>Repressor binds to the operator "
    "region (o) and prevents RNA polymerase from transcribing the operon</b>. "
    "<b>In presence of inducer</b>, the <b>Inducer</b> gives an <b>Inactive repressor</b>, "
    "so <b>lac mRNA</b> is made and <b>Transcription</b> followed by <b>Translation</b> "
    "yields <b>beta-galactosidase</b>, <b>permease</b> and <b>transacetylase</b>."))
story.append(Spacer(1, 3))
story.append(Paragraph(
    "Essentially, <b>regulation of lac operon can also be visualised as regulation of "
    "enzyme synthesis by its substrate</b>. Remember, <b>glucose or galactose cannot act as "
    "inducers for lac operon</b>. <b>Regulation of lac operon by repressor is referred to "
    "as negative regulation.</b> <b>Lac operon is under control of positive regulation as "
    "well, but it is beyond the scope of discussion at this level.</b>",
    STYLES["Body"]))
story.append(Spacer(1, 3))
story.append(note(
    "<b>Why the operon switches itself off again -- and the answer to <i>\"can you think "
    "for how long the lac operon would be expressed in the presence of lactose?\"</i></b> "
    "Only <b>as long as the lactose lasts</b>. Put the facts of this section in a line: "
    "<b>lactose is the inducer</b>, and <b>lactose is also the substrate of "
    "beta-galactosidase</b>, the very enzyme the operon switches on. So the induced enzyme "
    "<b>consumes the inducer</b> -- hydrolysing it to <b>galactose and glucose</b>, neither "
    "of which <b>can act as an inducer</b>. As the lactose is used up there is nothing left "
    "to <b>inactivate the repressor</b>, the repressor <b>binds the operator again</b>, and "
    "<b>transcription stops</b>. The operon is therefore self-limiting: it stays on only "
    "while its own substrate is present."))
story.append(Spacer(1, 3))
story.append(memory_aid(
    "Gene letters, in order: <b>i-z-y-a</b> = <b>inhibitor (repressor), beta-gal, permease, "
    "transacetylase</b>. The <b>i stands for inhibitor, not inducer</b> -- a favourite "
    "trap. The <b>inducer is lactose (or allolactose)</b>; <b>glucose and galactose are "
    "not inducers</b>. Repressor <b>on</b> the operator = operon <b>off</b>; inducer "
    "<b>inactivates</b> the repressor = operon <b>on</b>. This repressor-based control is "
    "<b>negative regulation</b>."))


# --------------------------------------------------------------------------------------
# 5.9  HUMAN GENOME PROJECT
# --------------------------------------------------------------------------------------
# ---- 5.9 (F489 heading, F502 opener, F373-F408; Goals sub-heading F490 + stem F503 +
#      items F383-F388; Figure 5.15; Rule 2 gap Q14(d) Bioinformatics extends F381/F382) ----
story.append(heading("5.9", "HUMAN GENOME PROJECT", 1))

story.append(Paragraph(
    "In the preceding sections you have learnt that it is the <b>sequence of bases in DNA "
    "that determines the genetic information of a given organism</b>. In other words, "
    "<b>genetic make-up of an organism or an individual lies in the DNA sequences</b>. If "
    "<b>two individuals differ, then their DNA sequences should also be different, at least "
    "at some places</b>. These assumptions led to the <b>quest of finding out the complete "
    "DNA sequence of human genome</b>.",
    STYLES["Body"]))
story.append(Spacer(1, 3))
story.append(Paragraph(
    "With the establishment of <b>genetic engineering techniques</b> where it was possible "
    "to <b>isolate and clone any piece of DNA</b> and availability of <b>simple and fast "
    "techniques for determining DNA sequences</b>, a very <b>ambitious project of "
    "sequencing human genome was launched in the year 1990</b>.",
    STYLES["Body"]))
story.append(Spacer(1, 3))
story.append(keyterm(
    "<b>Human Genome Project (HGP) was called a mega project.</b> You can imagine the "
    "magnitude and the requirements for the project if we simply define the aims of the "
    "project as follows."))
story.append(data_table([
    ["What makes it a mega project", "The figure NCERT gives"],
    ["<b>Size of the genome</b>",
     "Human genome is said to have approximately <b>3 x 10^9 bp</b>."],
    ["<b>Cost per base</b>",
     "<b>US $ 3 per bp</b> (the estimated cost in the beginning)."],
    ["<b>Total estimated cost</b>",
     "Approximately <b>9 billion US dollars</b>."],
    ["<b>Storage, if printed</b>",
     "If each page of a book contained <b>1000 letters</b> and each book contained "
     "<b>1000 pages</b>, then <b>3300 such books</b> would be required to store the "
     "information of DNA sequence <b>from a single human cell</b>."],
    ["<b>Computation</b>",
     "The <b>enormous amount of data</b> expected to be generated also necessitated the "
     "use of <b>high speed computational devices for data storage and retrieval, and "
     "analysis</b>."],
    ["<b>Duration and coordination</b>",
     "A <b>13-year project coordinated by the U.S. Department of Energy and the National "
     "Institute of Health</b>. During the early years, the <b>Wellcome Trust (U.K.)</b> "
     "became a major partner; additional contributions came from <b>Japan, France, "
     "Germany, China</b> and others. The project was <b>completed in 2003</b>."],
], col_widths=[2.4, 6.6]))
story.append(Spacer(1, 4))
story.append(keyterm(
    "<b>HGP was closely associated with the rapid development of a new area in biology "
    "called Bioinformatics.</b>"))
story.append(note(
    "<b>What Bioinformatics does.</b> NCERT names the field but does not say what it is, "
    "and the exercises ask you to describe it -- so read it off the need that created it. "
    "The project generated an <b>enormous amount of data</b> requiring <b>high speed "
    "computational devices for data storage and retrieval, and analysis</b>, and two of the "
    "HGP's own stated goals were to <b>store this information in databases</b> and to "
    "<b>improve tools for data analysis</b>. <b>Bioinformatics is that area of biology: the "
    "use of computational methods and databases to store, retrieve and analyse biological "
    "sequence information.</b>"))
story.append(Spacer(1, 4))

# Goals of HGP -- F490 is an unnumbered boxed sub-heading inside 5.9, not a numbered
# section, so it is set as a level-3 heading with no number.
story.append(heading("Goals", "Goals of HGP", 3))
story.append(Paragraph(
    "Some of the <b>important goals of HGP</b> were as follows:", STYLES["Body"]))
story.append(data_table([
    ["#", "Goal"],
    ["<b>(i)</b>",
     "<b>Identify all the approximately 20,000-25,000 genes in human DNA;</b>"],
    ["<b>(ii)</b>",
     "<b>Determine the sequences of the 3 billion chemical base pairs that make up human "
     "DNA;</b>"],
    ["<b>(iii)</b>", "<b>Store this information in databases;</b>"],
    ["<b>(iv)</b>", "<b>Improve tools for data analysis;</b>"],
    ["<b>(v)</b>",
     "<b>Transfer related technologies to other sectors, such as industries;</b>"],
    ["<b>(vi)</b>",
     "<b>Address the ethical, legal, and social issues (ELSI) that may arise from the "
     "project.</b>"],
], col_widths=[0.8, 8.2]))
story.append(Spacer(1, 4))
story.append(Paragraph(
    "<b>Knowledge about the effects of DNA variations among individuals can lead to "
    "revolutionary new ways to diagnose, treat and someday prevent the thousands of "
    "disorders that affect human beings.</b> Besides providing clues to understanding human "
    "biology, learning about <b>non-human organisms DNA sequences</b> can lead to an "
    "understanding of their <b>natural capabilities</b> that can be applied toward solving "
    "challenges in <b>health care, agriculture, energy production, environmental "
    "remediation</b>. <b>Many non-human model organisms</b>, such as <b>bacteria, yeast, "
    "Caenorhabditis elegans (a free living non-pathogenic nematode), Drosophila (the fruit "
    "fly), plants (rice and Arabidopsis)</b>, etc., have <b>also been sequenced</b>.",
    STYLES["Body"]))
story.append(Spacer(1, 3))
story.append(Paragraph(
    "<b>Methodologies :</b> The <b>methods involved two major approaches</b>.",
    STYLES["Body"]))
story.append(data_table([
    ["Approach", "What it sequenced"],
    ["<b>Expressed Sequence Tags (ESTs)</b>",
     "One approach focused on <b>identifying all the genes that are expressed as RNA</b>."],
    ["<b>Sequence Annotation</b>",
     "The other took the <b>blind approach of simply sequencing the whole set of genome "
     "that contained all the coding and non-coding sequence</b>, and <b>later assigning "
     "different regions in the sequence with functions</b>."],
], col_widths=[2.4, 6.6]))
story.append(Spacer(1, 4))
story.append(process_flow([
    "<b>Isolate and fragment.</b> The <b>total DNA from a cell is isolated</b> and "
    "<b>converted into random fragments of relatively smaller sizes</b> (recall DNA is a "
    "very long polymer, and there are <b>technical limitations in sequencing very long "
    "pieces of DNA</b>).",
    "<b>Clone.</b> The fragments are <b>cloned in suitable host using specialised "
    "vectors</b>. The <b>cloning resulted into amplification of each piece of DNA "
    "fragment</b> so that it subsequently <b>could be sequenced with ease</b>. The "
    "<b>commonly used hosts were bacteria and yeast</b>, and the vectors were called "
    "<b>BAC (bacterial artificial chromosomes)</b> and <b>YAC (yeast artificial "
    "chromosomes)</b>.",
    "<b>Sequence.</b> The fragments were sequenced using <b>automated DNA sequencers</b> "
    "that worked on the <b>principle of a method developed by Frederick Sanger</b>. "
    "(Remember, <b>Sanger is also credited for developing method for determination of amino "
    "acid sequences in proteins</b>.)",
    "<b>Assemble.</b> These sequences were then <b>arranged based on some overlapping "
    "regions present in them</b>. This required <b>generation of overlapping fragments for "
    "sequencing</b>. <b>Alignment of these sequences was humanly not possible</b>, "
    "therefore <b>specialised computer based programs were developed</b>.",
    "<b>Annotate and assign.</b> These sequences were <b>subsequently annotated and were "
    "assigned to each chromosome</b>. The <b>sequence of chromosome 1 was completed only in "
    "May 2006</b> -- this was the <b>last of the 24 human chromosomes (22 autosomes and X "
    "and Y) to be sequenced</b>.",
]))
story.append(Spacer(1, 4))
story.append(figure(
    "fig_5_15.png",
    "Figure 5.15 Human Genome Project -- the sequencing workflow, from total DNA through "
    "random fragments cloned in BAC and YAC vectors, to automated sequencing and "
    "computer-based alignment of overlapping fragments."))
story.append(Spacer(1, 3))
story.append(Paragraph(
    "Another <b>challenging task was assigning the genetic and physical maps on the "
    "genome</b>. This was generated using information on <b>polymorphism of restriction "
    "endonuclease recognition sites</b>, and some <b>repetitive DNA sequences known as "
    "microsatellites</b>.",
    STYLES["Body"]))
story.append(Spacer(1, 3))
story.append(memory_aid(
    "The mega-project numbers worth carrying: <b>launched 1990, completed 2003, a 13-year "
    "project</b>; <b>3 x 10^9 bp</b> at <b>US $3 per bp</b> = about <b>9 billion "
    "dollars</b>; <b>3300 books</b> to print one cell's sequence. <b>Chromosome 1 was "
    "last</b>, finished <b>May 2006</b> -- after the project itself was declared complete. "
    "Two methodologies, two names: <b>ESTs</b> = genes expressed as RNA only; <b>Sequence "
    "Annotation</b> = sequence everything, assign function later. <b>Sanger</b> for the "
    "sequencing method, <b>BAC and YAC</b> for the vectors."))


# ---- 5.9.1 Salient Features of Human Genome (F491 heading, F504 stem, F409-F417) ----
story.append(heading("5.9.1", "Salient Features of Human Genome", 2))

story.append(Paragraph(
    "Some of the <b>salient observations drawn from human genome project</b> are as "
    "follows:", STYLES["Body"]))
story.append(data_table([
    ["#", "Observation"],
    ["<b>(i)</b>",
     "The <b>human genome contains 3164.7 million bp</b>."],
    ["<b>(ii)</b>",
     "The <b>average gene consists of 3000 bases</b>, but <b>sizes vary greatly</b>, with "
     "the <b>largest known human gene being dystrophin at 2.4 million bases</b>."],
    ["<b>(iii)</b>",
     "The <b>total number of genes is estimated at 30,000</b> -- much <b>lower than "
     "previous estimates of 80,000 to 1,40,000 genes</b>. <b>Almost all (99.9 per cent) "
     "nucleotide bases are exactly the same in all humans.</b>"],
    ["<b>(iv)</b>",
     "The <b>functions are unknown for over 50 per cent of the discovered genes</b>."],
    ["<b>(v)</b>",
     "<b>Less than 2 per cent of the genome codes for proteins.</b>"],
    ["<b>(vi)</b>",
     "<b>Repeated sequences make up very large portion of the human genome.</b>"],
    ["<b>(vii)</b>",
     "<b>Repetitive sequences are stretches of DNA sequences that are repeated many times, "
     "sometimes hundred to thousand times.</b> They are <b>thought to have no direct coding "
     "functions</b>, but they <b>shed light on chromosome structure, dynamics and "
     "evolution</b>."],
    ["<b>(viii)</b>",
     "<b>Chromosome 1 has most genes (2968)</b>, and the <b>Y has the fewest (231)</b>."],
    ["<b>(ix)</b>",
     "Scientists have identified about <b>1.4 million locations where single-base DNA "
     "differences (SNPs -- single nucleotide polymorphism, pronounced as 'snips') occur in "
     "humans</b>. This information promises to <b>revolutionise the processes of finding "
     "chromosomal locations for disease-associated sequences and tracing human history</b>."],
], col_widths=[0.9, 8.1]))
story.append(Spacer(1, 4))
story.append(memory_aid(
    "The numbers most often asked: <b>3164.7 million bp</b>; <b>average gene 3000 bases</b>; "
    "<b>dystrophin is the largest at 2.4 million bases</b>; <b>about 30,000 genes</b>; "
    "<b>99.9 per cent of bases identical between humans</b>; <b>functions unknown for over "
    "50 per cent</b> of genes; <b>less than 2 per cent codes for protein</b>; "
    "<b>chromosome 1 has the most genes (2968), Y the fewest (231)</b>; <b>1.4 million "
    "SNPs</b>. Do not confuse <b>chromosome 1 has the most genes</b> with <b>chromosome 1 "
    "was sequenced last</b> -- both are true and both are examined."))


# ---- 5.9.2 Applications and Future Challenges (F492 heading, F505 opener, F418-F422) ----
story.append(heading("5.9.2", "Applications and Future Challenges", 2))

story.append(Paragraph(
    "<b>Deriving meaningful knowledge from the DNA sequences will define research through "
    "the coming decades leading to our understanding of biological systems.</b> This "
    "<b>enormous task will require the expertise and creativity of tens of thousands of "
    "scientists from varied disciplines in both the public and private sectors "
    "worldwide</b>.",
    STYLES["Body"]))
story.append(Spacer(1, 3))
story.append(Paragraph(
    "One of the <b>greatest impacts of having the HG sequence</b> may well be <b>enabling a "
    "radically new approach to biological research</b>. <b>In the past, researchers studied "
    "one or a few genes at a time.</b> With <b>whole-genome sequences and new "
    "high-throughput technologies</b>, we can <b>approach questions systematically and on a "
    "much broader scale</b>. They can <b>study all the genes in a genome</b>, for example, "
    "<b>all the transcripts in a particular tissue or organ or tumor</b>, or <b>how tens of "
    "thousands of genes and proteins work together in interconnected networks to orchestrate "
    "the chemistry of life</b>.",
    STYLES["Body"]))
story.append(Spacer(1, 3))
story.append(memory_aid(
    "The shift the HGP caused is the examinable idea here: <b>from one-or-a-few genes at a "
    "time to whole genomes at once</b>, made possible by <b>high-throughput "
    "technologies</b>. That is also the answer to why <b>Bioinformatics</b> had to be "
    "invented alongside it."))


# --------------------------------------------------------------------------------------
# 5.10  DNA FINGERPRINTING
# --------------------------------------------------------------------------------------
# ---- 5.10 (F493 heading, F506 opener = the 99.9 per cent premise, F423-F468,
#      F510 summary-unique; Figure 5.16 labels F637-F646; Q8(a) contrast presented as a
#      table per the inventory's exercise-gap scan -- no new fact added) ----
story.append(heading("5.10", "DNA FINGERPRINTING", 1))

story.append(keyterm(
    "As stated in the preceding section, <b>99.9 per cent of base sequence among humans is "
    "the same</b>. Assuming human genome as <b>3 x 10^9 bp</b>, in how many base sequences "
    "would there be differences? It is <b>these differences in sequence of DNA which make "
    "every individual unique in their phenotypic appearance</b>."))
story.append(Paragraph(
    "If one aims to <b>find out genetic differences between two individuals or among "
    "individuals of a population</b>, <b>sequencing the DNA every time would be a daunting "
    "and expensive task</b>. <b>Imagine trying to compare two sets of 3 x 10^6 base "
    "pairs.</b>",
    STYLES["Body"]))
story.append(Spacer(1, 3))
story.append(note(
    "<b>A printing inconsistency in the source, so you do not think you misread.</b> This "
    "section quotes the human genome as <b>3 x 10^9 bp</b> and then, two sentences later, "
    "as <b>3 x 10^6 base pairs</b>. Both are reproduced above exactly as NCERT prints "
    "them. The figure established by the Human Genome Project in the preceding section is "
    "<b>3 x 10^9</b> (about <b>3164.7 million bp</b>); the <b>10^6</b> is the source's own "
    "slip."))
story.append(Spacer(1, 4))
story.append(keyterm(
    "<b>DNA fingerprinting is a very quick way to compare the DNA sequences of any two "
    "individuals.</b> DNA fingerprinting involves <b>identifying differences in some "
    "specific regions in DNA sequence called as repetitive DNA</b>, because in these "
    "sequences, a <b>small stretch of DNA is repeated many times</b>."))
story.append(Paragraph(
    "These <b>repetitive DNA are separated from bulk genomic DNA as different peaks during "
    "density gradient centrifugation</b>. The <b>bulk DNA forms a major peak</b> and the "
    "<b>other small peaks are referred to as satellite DNA</b>.",
    STYLES["Body"]))
story.append(Spacer(1, 3))
# Q8(a) of the exercises asks for Repetitive DNA vs Satellite DNA. The inventory's
# exercise-gap scan found the contrast is present but scattered across F428-F431, so it is
# presented here as a two-column table. No fact is added.
story.append(data_table([
    ["Repetitive DNA", "Satellite DNA"],
    ["Sequences in which a <b>small stretch of DNA is repeated many times</b>. Identifying "
     "differences in these regions is what <b>DNA fingerprinting</b> does.",
     "The <b>small peaks other than the major bulk-DNA peak</b> obtained when repetitive "
     "DNA is <b>separated from bulk genomic DNA during density gradient "
     "centrifugation</b>."],
    ["The <b>general class</b> -- any many-times-repeated stretch, making up a <b>large "
     "portion of the human genome</b>.",
     "A <b>sub-class defined by its centrifugation behaviour</b>, and further classified "
     "<b>depending on base composition (A : T rich or G:C rich), length of segment, and "
     "number of repetitive units</b> into <b>micro-satellites, mini-satellites</b> etc."],
], col_widths=[4.5, 4.5]))
story.append(Spacer(1, 4))
story.append(Paragraph(
    "These <b>sequences normally do not code for any proteins</b>, but they <b>form a large "
    "portion of human genome</b>. These <b>sequence show high degree of polymorphism and "
    "form the basis of DNA fingerprinting</b>.",
    STYLES["Body"]))
story.append(Paragraph(
    "Since <b>DNA from every tissue (such as blood, hair-follicle, skin, bone, saliva, "
    "sperm etc.), from an individual show the same degree of polymorphism</b>, they become "
    "<b>very useful identification tool in forensic applications</b>. Further, as the "
    "<b>polymorphisms are inheritable from parents to children</b>, <b>DNA fingerprinting "
    "is the basis of paternity testing, in case of disputes</b>.",
    STYLES["Body"]))
story.append(Spacer(1, 3))
story.append(Paragraph(
    "As <b>polymorphism in DNA sequence is the basis of genetic mapping of human genome as "
    "well as of DNA fingerprinting</b>, it is essential that we understand <b>what DNA "
    "polymorphism means</b> in simple terms.",
    STYLES["Body"]))
story.append(Spacer(1, 3))
story.append(keyterm(
    "<b>Polymorphism (variation at genetic level) arises due to mutations.</b> In simple "
    "terms, <b>if an inheritable mutation is observed in a population at high frequency, it "
    "is referred to as DNA polymorphism</b>. More precisely, <b>allelic sequence variation "
    "has traditionally been described as a DNA polymorphism if more than one variant "
    "(allele) at a locus occurs in human population with a frequency greater than "
    "0.01</b>."))
story.append(Paragraph(
    "(Recall different kind of <b>mutations</b> and their effects that you have already "
    "studied in <b>Chapter 4</b>, and in the preceding sections in this chapter. Recall "
    "also the definition of <b>alleles</b> from Chapter 4.)",
    STYLES["Body"]))
story.append(Paragraph(
    "<b>New mutations may arise in an individual either in somatic cells or in the germ "
    "cells</b> (cells that generate gametes in sexually reproducing organisms). If a "
    "<b>germ cell mutation does not seriously impair individual's ability to have offspring "
    "who can transmit the mutation, it can spread to the other members of population</b> "
    "(through sexual reproduction).",
    STYLES["Body"]))
story.append(Spacer(1, 3))
story.append(Paragraph(
    "The <b>probability of such variation to be observed in non-coding DNA sequence would "
    "be higher</b>, as <b>mutations in these sequences may not have any immediate "
    "effect/impact in an individual's reproductive ability</b>. These <b>mutations keep on "
    "accumulating generation after generation, and form one of the basis of "
    "variability/polymorphism</b>. There is a <b>variety of different types of "
    "polymorphisms ranging from single nucleotide change to very large scale changes</b>. "
    "For <b>evolution and speciation, such polymorphisms play very important role</b>, and "
    "you will study these in details at higher classes.",
    STYLES["Body"]))
story.append(Spacer(1, 3))
story.append(keyterm(
    "The <b>technique of DNA Fingerprinting was initially developed by Alec Jeffreys</b>. "
    "He used a <b>satellite DNA as probe that shows very high degree of polymorphism</b>. "
    "It was called as <b>Variable Number of Tandem Repeats (VNTR)</b>."))
story.append(Paragraph(
    "The technique, as used earlier, <b>involved Southern blot hybridisation using "
    "radiolabelled VNTR as a probe</b>. It <b>involved the following steps</b>:",
    STYLES["Body"]))
story.append(Spacer(1, 2))
story.append(process_flow([
    "<b>(i) Isolation of DNA.</b>",
    "<b>(ii) Digestion of DNA by restriction endonucleases.</b>",
    "<b>(iii) Separation of DNA fragments by electrophoresis.</b>",
    "<b>(iv) Transferring (blotting) of separated DNA fragments to synthetic "
    "membranes</b>, such as <b>nitrocellulose or nylon</b>.",
    "<b>(v) Hybridisation using labelled VNTR probe.</b>",
    "<b>(vi) Detection of hybridised DNA fragments by autoradiography.</b>",
]))
story.append(Spacer(1, 4))
story.append(Paragraph(
    "The <b>VNTR belongs to a class of satellite DNA referred to as mini-satellite</b>. A "
    "<b>small DNA sequence is arranged tandemly in many copy numbers</b>. The <b>copy "
    "number varies from chromosome to chromosome in an individual</b>. The <b>numbers of "
    "repeat show very high degree of polymorphism</b>. As a result the <b>size of VNTR "
    "varies in size from 0.1 to 20 kb</b>.",
    STYLES["Body"]))
story.append(Paragraph(
    "Consequently, after <b>hybridisation with VNTR probe, the autoradiogram gives many "
    "bands of differing sizes</b>. These <b>bands give a characteristic pattern for an "
    "individual DNA</b>. It <b>differs from individual to individual in a population except "
    "in the case of monozygotic (identical) twins</b>.",
    STYLES["Body"]))
story.append(Spacer(1, 4))
story.append(figure(
    "fig_5_16.png",
    "Figure 5.16 Schematic representation of DNA fingerprinting. Repeats on the "
    "<b>Paternal chromosome</b> and the <b>Maternal chromosome</b> -- shown for "
    "<b>Chromosome 7</b>, <b>Chromosome 2</b> and <b>Chromosome 16</b> -- differ in the "
    "<b>Number of short tandem repeats</b>. <b>Amplified repeats, separated by size on a "
    "gel, give a DNA fingerprint</b>, so that <b>DNA from individual A</b>, <b>DNA from "
    "individual B</b> and <b>DNA from crime scene (C)</b> can be compared band for band."))
story.append(Spacer(1, 3))
story.append(Paragraph(
    "The <b>sensitivity of the technique has been increased by use of polymerase chain "
    "reaction (PCR</b> -- you will study about it in <b>Chapter 9</b>). Consequently, "
    "<b>DNA from a single cell is enough to perform DNA fingerprinting analysis</b>. "
    "<b>Currently, many different probes are used to generate DNA fingerprints.</b>",
    STYLES["Body"]))
story.append(Spacer(1, 3))
story.append(Paragraph(
    "In addition to application in <b>forensic science</b>, it has much wider application, "
    "such as in <b>determining population and genetic diversities</b>. It has <b>immense "
    "applications in the field of forensic science, genetic biodiversity and evolutionary "
    "biology</b>.",
    STYLES["Body"]))
story.append(Spacer(1, 3))
story.append(memory_aid(
    "The chain of logic: <b>99.9 per cent of human DNA is identical</b>, so you look only "
    "where it varies -- the <b>repetitive / satellite DNA</b>, which is <b>non-coding</b> "
    "and therefore <b>free to accumulate mutations</b>, giving <b>high polymorphism</b>. "
    "<b>Alec Jeffreys</b>, probe = <b>VNTR</b>, a <b>mini-satellite</b>, size <b>0.1 to 20 "
    "kb</b>; the original readout was <b>Southern blot + autoradiography</b>, now made far "
    "more sensitive by <b>PCR</b> -- <b>a single cell is enough</b>. Two exam traps: "
    "<b>identical (monozygotic) twins share a fingerprint</b>, and <b>polymorphism counts "
    "as polymorphism only above a frequency of 0.01</b>."))


story.append(Spacer(1, 5))

# =============================== QUICK RECAP ========================================
# ---- Quick Recap (F494 SUMMARY heading; denser rewrite of the chapter summary, Rule 3).
# The inventory's Summary classification split the source Summary into 33 sentences:
# 29 BODY-PRESENT + 4 SUMMARY-UNIQUE. The 4 summary-unique facts are NOT repeated here --
# they were folded into the body above as F507 (5.7), F508 (5.8), F509 (5.8.1) and
# F510 (5.10). The 29 body-present sentences are recapped below and, per carry-over 19,
# appear only here and not as body rows. Carry-over 20: sentence 23's unqualified
# "primary step" phrasing is kept to the Recap; the body keeps NCERT's "in prokaryotes /
# predominant" qualifier.
story.append(heading("QR", "QUICK RECAP", 1))
story.append(Paragraph(
    "&bull; <b>Nucleic acids are long polymers of nucleotides.</b> While <b>DNA stores "
    "genetic information, RNA mostly helps in transfer and expression of information</b>.",
    STYLES["Bullet1"]))
story.append(Paragraph(
    "&bull; Though <b>DNA and RNA both function as genetic material</b>, <b>DNA being "
    "chemically and structurally more stable is a better genetic material</b>. However, "
    "<b>RNA is the first to evolve and DNA was derived from RNA</b>.",
    STYLES["Bullet1"]))
story.append(Paragraph(
    "&bull; The <b>hallmark of the double stranded helical structure of DNA is the hydrogen "
    "bonding between the bases from opposite strands</b>. The rule is that <b>Adenine pairs "
    "with Thymine through two H-bonds, and Guanine with Cytosine through three "
    "H-bonds</b>. This <b>makes one strand complementary to the other</b>.",
    STYLES["Bullet1"]))
story.append(Paragraph(
    "&bull; The <b>DNA replicates semiconservatively</b>, the process being <b>guided by "
    "the complementary H-bonding</b>.",
    STYLES["Bullet1"]))
story.append(Paragraph(
    "&bull; A <b>segment of DNA that codes for RNA</b> may in a simplistic term be referred "
    "to as a <b>gene</b>. During <b>transcription</b> also, <b>one of the strands of DNA "
    "acts as a template to direct the synthesis of complementary RNA</b>.",
    STYLES["Bullet1"]))
story.append(Paragraph(
    "&bull; In <b>bacteria, the transcribed mRNA is functional, hence can directly be "
    "translated</b>. In <b>eukaryotes, the gene is split</b>: the <b>coding sequences, "
    "exons, are interrupted by non-coding sequences, introns</b>. <b>Introns are removed "
    "and exons are joined to produce functional RNA by splicing.</b>",
    STYLES["Bullet1"]))
story.append(Paragraph(
    "&bull; The <b>messenger RNA contains the base sequences that are read in a combination "
    "of three (to make triplet genetic code) to code for an amino acid</b>.",
    STYLES["Bullet1"]))
story.append(Paragraph(
    "&bull; The <b>genetic code is read again on the principle of complementarity by tRNA "
    "that acts as an adapter molecule</b>. There are <b>specific tRNAs for every amino "
    "acid</b>. The <b>tRNA binds to specific amino acid at one end and pairs through "
    "H-bonding with codes on mRNA through its anticodons</b>.",
    STYLES["Bullet1"]))
story.append(Paragraph(
    "&bull; The <b>site of translation (protein synthesis) is ribosomes</b>, which <b>bind "
    "to mRNA and provide platform for joining of amino acids</b>. <b>One of the rRNA acts "
    "as a catalyst for peptide bond formation, which is an example of RNA enzyme "
    "(ribozyme).</b>",
    STYLES["Bullet1"]))
story.append(Paragraph(
    "&bull; <b>Regulation of transcription is the primary step for regulation of gene "
    "expression.</b> In <b>bacteria, more than one gene is arranged together and regulated "
    "in units called as operons</b>. The <b>operon is regulated by the amount of lactose in "
    "the medium where the bacteria are grown</b>; therefore this <b>regulation can also be "
    "viewed as regulation of enzyme synthesis by its substrate</b>.",
    STYLES["Bullet1"]))
story.append(Paragraph(
    "&bull; <b>Human genome project was a mega project that aimed to sequence every base in "
    "human genome.</b> This <b>project has yielded much new information</b>, and <b>many new "
    "areas and avenues have opened up as a consequence of the project</b>.",
    STYLES["Bullet1"]))
story.append(Paragraph(
    "&bull; <b>DNA Fingerprinting is a technique to find out variations in individuals of a "
    "population at DNA level.</b> It <b>works on the principle of polymorphism in DNA "
    "sequences</b>.",
    STYLES["Bullet1"]))
story.append(Spacer(1, 5))

# =============================== EXERCISE-GAP APPENDIX ==============================
# ---- Terms used in the exercises (F495 EXERCISES heading; F469-F482 are the 14 questions).
# The inventory's exercise-gap scan (session 1-Z step 7) found 5 genuine gaps out of 17
# item rows. Four of them were closed inline where they belong, as NOTE boxes, per Rule 2
# option 1 and carry-over 18: Q2 in 5.1.1, Q3/Q4 in 5.5.1, Q6 in 5.4.2, Q10 in 5.8.1 and
# Q14(d) in 5.9. This appendix is the index to those, so a reader working the exercises can
# find each one, plus the pointers for the questions the body already covers.
story.append(heading("EX", "TERMS USED IN THE EXERCISES", 1))
story.append(Paragraph(
    "The end-of-chapter questions were scanned one by one against the body of this chapter. "
    "Most are answerable directly from the sections above; the few that lean on a "
    "convention or a step the source never spells out are closed <b>using only facts from "
    "this chapter</b>, in a <b>NOTE box beside the facts they depend on</b>. This table "
    "says where each answer lives.",
    STYLES["Body"]))
story.append(data_table([
    ["Exercise", "Where its answer lives"],
    ["<b>Q1</b> bases vs nucleosides",
     "&sect;5.1.1 -- a <b>nucleoside</b> is base + sugar (N-glycosidic linkage), and "
     "<b>adenosine, guanosine, cytidine, uridine</b> are named there. So <b>Cytidine</b> "
     "and <b>Guanosine</b> are nucleosides; <b>Adenine, Thymine, Uracil, Cytosine</b> are "
     "bases."],
    ["<b>Q2</b> per cent of adenine",
     "&sect;5.1.1 -- <b>worked NOTE box</b> beside Chargaff's rule and the A-T / G-C "
     "pairing rule."],
    ["<b>Q3, Q4</b> complementary strand and mRNA of a given 28-mer",
     "&sect;5.5.1 -- <b>worked NOTE box</b> beside the template / coding strand "
     "definitions, doing the given sequence once for the complementary strand and once for "
     "the mRNA."],
    ["<b>Q5</b> which property suggested semi-conservative replication",
     "&sect;5.1.1 and &sect;5.4 -- <b>complementary base pairing</b>, and Watson and "
     "Crick's own statement that it <b>suggests a mechanism for copying</b>."],
    ["<b>Q6</b> types of nucleic acid polymerases",
     "&sect;5.4.2 -- <b>NOTE box</b> laying the classes out as a template-versus-product "
     "grid."],
    ["<b>Q7</b> how Hershey and Chase told DNA from protein",
     "&sect;5.2.1 -- <b>radioactive phosphorus</b> labels DNA only (protein has no P), "
     "<b>radioactive sulfur</b> labels protein only (DNA has no S)."],
    ["<b>Q8</b> (a) repetitive vs satellite DNA, (b) mRNA vs tRNA, (c) template vs coding "
     "strand",
     "(a) &sect;5.10 -- the <b>two-column table</b> in that section. "
     "(b) &sect;5.5.3 (mRNA is the template) and &sect;5.6.2 (tRNA is the adapter). "
     "(c) &sect;5.5.1 -- <b>template strand is 3'-to-5' and is copied</b>; <b>coding strand "
     "is 5'-to-3' and codes for nothing</b>."],
    ["<b>Q9</b> two essential roles of the ribosome",
     "&sect;5.7 -- the <b>two binding sites in the large subunit</b> that hold successive "
     "amino acids close enough to react, and the <b>23S rRNA ribozyme</b> that catalyses "
     "the peptide bond."],
    ["<b>Q10</b> why the lac operon shuts down again after lactose is added",
     "&sect;5.8.1 -- <b>NOTE box</b> after negative regulation: the induced "
     "beta-galactosidase <b>consumes the inducer</b>, so the repressor re-binds the "
     "operator."],
    ["<b>Q11</b> function of promoter, tRNA, exons",
     "&sect;5.5.1 (promoter -- binding site for RNA polymerase, defines template and coding "
     "strands), &sect;5.6.2 (tRNA -- adapter, reads codon and carries amino acid), "
     "&sect;5.5.2 (exons -- expressed sequences that appear in mature RNA)."],
    ["<b>Q12</b> why HGP is called a mega project",
     "&sect;5.9 -- the <b>mega project table</b>: 3 x 10^9 bp at US $3 per bp, about 9 "
     "billion dollars, 3300 books to print one cell's sequence, 13 years, high-speed "
     "computation."],
    ["<b>Q13</b> what DNA fingerprinting is, and its applications",
     "&sect;5.10 -- definition, <b>Alec Jeffreys</b> and the <b>VNTR</b> probe, the "
     "<b>six steps</b>, and the applications (<b>forensic science, paternity testing, "
     "population and genetic diversities, genetic biodiversity, evolutionary "
     "biology</b>)."],
    ["<b>Q14</b> (a) transcription, (b) polymorphism, (c) translation, (d) bioinformatics",
     "(a) &sect;5.5 opener, (b) &sect;5.10 (variation arising from mutation, above a "
     "frequency of 0.01), (c) &sect;5.7 opener, (d) &sect;5.9 -- <b>NOTE box</b> on what "
     "bioinformatics does."],
    ["<b>In-body exercises</b> beneath Table 5.1",
     "&sect;5.6 -- both are <b>worked in full</b> in the NOTE box under the codon "
     "checker-board, including why the reverse direction is ambiguous."],
], col_widths=[2.6, 6.4]))


# --------------------------------------------------------------------------------------
# BUILD
# --------------------------------------------------------------------------------------
# Spec section 4: no header, no footer, no page numbers, and no rule lines at the top or
# bottom of the page. Every page therefore carries content only -- there is deliberately
# no onFirstPage / onLaterPages canvas callback.

def main():
    return build_pdf(
        OUT_PDF, story,
        title="Class 12 Chapter 5 - Molecular Basis of Inheritance (NEET notes)",
    )


if __name__ == "__main__":
    sys.exit(main())
