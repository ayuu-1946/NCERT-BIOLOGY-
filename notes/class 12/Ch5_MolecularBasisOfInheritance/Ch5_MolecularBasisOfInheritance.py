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
story.append(note(
    "<b>End of Pass 2a (source pp. 1-17, sections 5.1 to 5.5.3).</b> The chapter "
    "continues with 5.5.4 (transcription in eukaryotes and RNA splicing), 5.6 (genetic "
    "code), 5.7 (translation), 5.8 (regulation of gene expression / lac operon), "
    "5.9 (Human Genome Project) and 5.10 (DNA fingerprinting), followed by the QUICK "
    "RECAP and APPENDIX blocks. Those are written in Pass 2b."))


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
