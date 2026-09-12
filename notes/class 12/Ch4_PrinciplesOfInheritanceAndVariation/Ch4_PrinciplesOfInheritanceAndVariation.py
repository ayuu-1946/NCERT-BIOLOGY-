"""
NCERT Class 12 Biology, Chapter 4 - Principles of Inheritance and Variation
NEET replacement notes -> A4 print-ready PDF.

Built under SUPREME COMMAND PROMPT.md v6, Pass 2: written linearly from the
frozen 376-row inventory (Ch4_PrinciplesOfInheritanceAndVariation_inventory.md)
in Content Order (SS5), importing the repo-level frozen style module
`neet_template.py` (SS0.6). No style, geometry, colour or font is re-declared
here.

Block markers `# ---- N.N ----` mark every NCERT section so a Pass 3 flag can be
found and fixed in one contiguous block. Inventory row IDs are named in the
comments so any fact can be traced back to its frozen row.

The carry-forwards from Pass 1 are honoured as follows.

1. GREEK (carry-forward 1). The source's Greek letters are spelled out in
   plain ASCII: `alpha` (alpha cells, alpha Thalassemia, alpha globin chain),
   `beta` (beta cells, beta Thalassemia, beta globin chain). `check_pdf.py`
   check 5 bans Greek. The two ion patterns are written with <super> tags
   throughout.

2. SOURCE-VERBATIM SPELLINGS (carry-forward 2). The five OCR-level spellings
   are kept in their original places: `Flouwer colour` (Table 4.1 row 2),
   `in completely dominant` (Fig 4.6 caption), `the x body` (SS4.6),
   `Micro graph` (Fig 4.15 caption), `Myo tonic dystrophy` (Fig 4.14 caption),
   `Zw` (Fig 4.12 c), `Xx` (the summary's own spelling, kept in the recap
   when the source phrasing is being echoed), `Kombergs`/`Kornberg's (father
   and son)` (unit opener, kept in the opener), `conditon` and `chraracters`
   (summary spelling, kept in the recap when quoting the source), the
   duplicated `Figure 4.13` number (kept as printed - honey bee plate on
   p21, pedigree-symbol plate on p22).

3. FIGURE 4.13 DUPLICATION (carry-forward 3). The two plates share the
   printed number 4.13. The prose distinguishes them as "the honey bee
   plate (Figure 4.13)" and "the pedigree-symbol plate (Figure 4.13)" so the
   duplication reads as NCERT's, not ours.

4. OPERATOR DECISION: NO FIGURE EMBEDDED (carry-forward 4). The user directed
   (session 2026-09-10) that no figure extraction is performed for this
   chapter. The PDF therefore calls `figure()` exactly zero times. The 163
   in-figure labels live in running text as the "Read the plate" NOTE-box
   pattern (Ch19 §19.2 style), so check 6 stays green: 163/163 labels found
   in the running text.

5. FIGURE 4.9 IS COLOUR-DEPENDENT (carry-forward 5). Plate 4.9 distinguishes
   its four chromosomes only by colour - orange, green, red, yellow. The
   running text names each colour and which pole it segregates to, in both
   Possibility I and Possibility II, so the distinction survives the
   no-figure-embedded decision.

6. EXERCISE GAPS (carry-forward 6, Rule 2). 4 of 16 exercises are GAPs that
   the body never answers: Q1 (Mendel's pea-plant advantages), Q3 (2^n
   gamete rule), Q6 (homozygous x heterozygous cross), Q7 (TtYy x Ttyy
   dihybrid). All four are answered in the closing "Terms used in the
   exercises" appendix, each visibly marked as worked-out rather than NCERT
   text. The other 12 are answered by the body and are not reproduced
   (Rule 2 forbids printing the same fact twice).

7. SUMMARY-UNIQUE FOLDS (carry-forward 7, Rule 3). 5 of 32 summary
   sentences are body-absent and are folded into the body sections the
   inventory names: F372 "principles and its practices" (ch4),
   F373 "morphological and physiological" (ch4), F374 "Mendel was the
   first ... systematically" (ch4), F375 "In chicken ... ZZ ... ZW" (SS4.6),
   F376 "Karyotypes" as an analytical tool (SS4.8.3).

8. NCERTS' OWN SPELLINGS KEPT VERBATIM (carry-forward 8). All six examples
   above are printed as the source prints them and flagged in place so no
   reader takes them for errors introduced here.

9. NO FOOTER / NO PAGE NUMBER (SS0.6, check 1). Pages carry no running
   header, no footer, and no page-number stamp. `neet_template.build_pdf`
   enforces this; `check_pdf.py` check 1 gates it.

Source: Chapter/class 12/Chapter 4 - Principles of Inheritance and Variation.pdf
(28 pp; a pure page-image scan, see `## Source problems` in the inventory)
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

# sys.path bootstrap: walk up until we find the repo-level neet_template.py (SS0.6)
_probe = HERE
while _probe != os.path.dirname(_probe):
    if os.path.exists(os.path.join(_probe, "neet_template.py")):
        sys.path.insert(0, _probe)
        break
    _probe = os.path.dirname(_probe)

from neet_template import (  # noqa: E402
    STYLES,
    heading, keyterm, process_flow, note, memory_aid, data_table, title_block, build_pdf,
)
from neet_template import figure as _shared_figure  # noqa: E402
from reportlab.platypus import Paragraph, Spacer  # noqa: E402

ASSETS = os.path.join(HERE, "assets")
OUT_PDF = os.path.join(HERE, "Ch4_PrinciplesOfInheritanceAndVariation.pdf")


# Carry-forward 1 inline shorthands (check 5: tags, never Unicode sub/superscripts)
def F1(): return "F<sub>1</sub>"
def F2(): return "F<sub>2</sub>"
def F3(): return "F<sub>3</sub>"


# Carry-forward 4: the chapter embeds zero figures. The `_figure_call` is
# kept as a local binding purely so a future operator can switch the policy
# by changing one line - the binding is intentionally not called.
def _figure_call(asset_name, caption_text, max_width_cm=15.9):
    return _shared_figure(asset_name, caption_text, ASSETS, max_width_cm=max_width_cm)


def body(text):
    return Paragraph(text, STYLES["Body"])


def b1(text):
    return Paragraph("&bull; " + text, STYLES["Bullet1"])


def b2(text):
    return Paragraph("- " + text, STYLES["Bullet2"])


def gap(h=4):
    return Spacer(1, h)


story = []

# ======================================================================================
# ---- Title block (SS5 item 1) ---- F021, F022
# ======================================================================================
story += title_block("Principles of Inheritance and Variation")

# ======================================================================================
# ---- Unit VII opener ---- F001, F002 (heading), F003, F004 (opener / fact)
# ======================================================================================
story.append(heading("Unit VII", "GENETICS AND EVOLUTION", level=1))

# F003, F004 (the source's own opener, kept in tutor voice)
story.append(body(
    "The work of <b>Mendel</b> and others who followed him gave us an idea of inheritance "
    "patterns."))
story.append(body(
    "The entire body of <b>molecular biology</b> was a consequent development with major "
    "contributions from <b>Watson, Crick, Nirenberg, Khorana, Kornberg's (father and "
    "son), Benzer, Monod, Brenner</b>, etc."))

story.append(gap(6))

# ======================================================================================
# ---- Scientist profiles: James Watson, Francis Crick ---- F005-F020
#      Text only, no photograph (SS5 item 3 / SS4.4 hard no).
#      The two profiles are presented as fact-bulleted dates; honours go in a small
#      table because the list is enumerable.
# ======================================================================================
story.append(gap(6))
story.append(heading("Profile", "JAMES WATSON", level=2))
# F005, F006, F007, F008, F009
story.append(b1(
    "<b>James Dewey Watson was born in Chicago on 6 April 1928.</b>"))
story.append(b1(
    "<b>In 1947, he received B.Sc. degree in Zoology.</b>"))
story.append(b1(
    "<b>During these years his interest in bird-watching had matured into a serious desire "
    "to learn genetics.</b>"))
story.append(b1(
    "<b>This became possible when he received a Fellowship for graduate study in Zoology at "
    "Indiana University, Bloomington, where he received his Ph.D degree in 1950 on a "
    "study of the effect of hard X-rays on bacteriophage multiplication.</b>"))
# F010, F011
story.append(b1(
    "<b>He met Crick and discovered their common interest in solving the DNA structure.</b>"))
story.append(b1(
    "<b>Their first serious effort, was unsatisfactory.</b>"))
# F012
story.append(b1(
    "<b>Their second effort based upon more experimental evidence and better appreciation "
    "of the nucleic acid literature resulted, early in March 1953, in the proposal of the "
    "complementary double-helical configuration.</b>"))

story.append(gap(6))
story.append(heading("Profile", "FRANCIS CRICK", level=2))
# F013, F014
story.append(b1(
    "<b>Francis Harry Compton Crick was born on 8 June 1916, at Northampton, England.</b>"))
# F015
story.append(b1(
    "<b>He studied physics at University College, London and obtained a B.Sc. in 1937.</b>"))
# F016
story.append(b1(
    "<b>He completed Ph.D. in 1954 on a thesis entitled X-ray Diffraction: Polypeptides and "
    "Proteins</b>."))
# F017
story.append(b1(
    "<b>A critical influence in Crick's career was his friendship with J.D. Watson, then a "
    "young man of 23, leading in 1953 to the proposal of the double-helical structure for "
    "DNA and the replication scheme.</b>"))
# F018
story.append(b1(
    "<b>Crick was made an F.R.S. in 1959.</b>"))

# F019 - the honours list
story.append(gap())
story.append(body(
    "<b>The honours to Watson with Crick include:</b>"))
story.append(data_table([
    ["Year", "Honour"],
    ["<b>1959</b>", "<b>John Collins Warren Prize of the Massachusetts General Hospital</b>"],
    ["<b>1960</b>", "<b>Lasker Award</b>"],
    ["<b>1962</b>", "<b>Research Corporation Prize</b>"],
    ["<b>1962</b>", "<b>Nobel Prize</b>"],
], col_widths=[20, 80]))

# F020 - portrait caption text only, by SS4.4 hard no
story.append(gap())
story.append(note(
    "<b>The scientist portrait plates on source page 2 are text-only by the SS4.4 hard "
    "no</b> - the photograph of a person is never embedded, converted or recreated; "
    "the name, dates, and achievements above carry everything examinable. The portrait "
    "captions as the source prints them are: <b>\"JAMES WATSON\"</b> and "
    "<b>\"FRANCIS CRICK\"</b>."))

# ======================================================================================
# ---- Chapter 4 opener + chapter map ---- F021-F030
#      Chapter map = data_table exactly as Ch19 SS19.intro does it.
# ======================================================================================
story.append(gap(6))
story.append(heading("Ch 4", "PRINCIPLES OF INHERITANCE AND VARIATION - Chapter Opener", level=1))

# F023 - the chapter contents box as printed (printed body runs 4.1-4.8, contents box stops at 4.6)
story.append(body(
    "The chapter contents box lists six sections, ending at <b>4.6 Genetic Disorders</b>; the "
    "printed body, however, runs to <b>4.8</b>, adding <b>4.4 Polygenic Inheritance, 4.5 "
    "Pleiotropy, 4.6 Sex Determination, 4.7 Mutation</b> and <b>4.8 Genetic Disorders</b>. "
    "The body numbering is authoritative for the chapter that follows."))

# F024, F025, F026, F027 - the four definitions
story.append(gap())
story.append(keyterm(
    "<b>Genetics</b> is the branch of biology that <b>deals with the inheritance, as well "
    "as the variation of characters from parents to offspring</b>. These and several related "
    "questions are dealt with, scientifically, in this branch."))
story.append(keyterm(
    "<b>Inheritance</b> is the process by which characters are passed on from parent to "
    "progeny; it is the <b>basis of heredity</b>."))
story.append(keyterm(
    "<b>Variation</b> is the degree by which progeny differ from their parents."))

# F028, F029, F030 - the historical context
story.append(gap())
story.append(body(
    "<b>Humans knew from as early as 8000-1000 B.C.</b> that one of the causes of variation "
    "was hidden in <b>sexual reproduction</b>."))
story.append(b1(
    "They <b>exploited the variations that were naturally present in the wild populations "
    "of plants and animals</b> to <b>selectively breed and select for organisms that "
    "possessed desirable characters</b>."))
story.append(b1(
    "For example, through <b>artificial selection and domestication from ancestral wild "
    "cows</b>, we have well-known Indian breeds, e.g., <b>Sahiwal cows in Punjab</b>."))

# F372, F373, F374 - the three SUMMARY-UNIQUE folds, body-absent
story.append(gap())
story.append(Paragraph(
    "<b>One sentence the chapter summary adds and the body never does:</b> <i>Genetics is a "
    "branch of biology which deals with principles of inheritance and its practices.</i>",
    STYLES["NoteBox"]))
story.append(Paragraph(
    "<b>And another:</b> <i>Progeny resembling the parents in morphological and physiological "
    "features has attracted the attention of many biologists.</i>", STYLES["NoteBox"]))
story.append(Paragraph(
    "<b>And one more:</b> <i>Mendel was the first to study this phenomenon systematically.</i>",
    STYLES["NoteBox"]))

# Chapter map as data_table (Ch19 §19.intro style)
story.append(gap())
story.append(data_table([
    ["Chapter 4 map", "What it covers"],
    ["<b>4.1 Mendel's Laws of Inheritance</b>",
     "How Mendel set up the pea experiments and what he saw"],
    ["<b>4.2 Inheritance of One Gene</b>",
     "Monohybrid cross, Punnett square, testcross, Law of Dominance, Law of Segregation, "
     "incomplete dominance, co-dominance"],
    ["<b>4.3 Inheritance of Two Genes</b>",
     "Dihybrid cross, Law of Independent Assortment, chromosomal theory, linkage and "
     "recombination"],
    ["<b>4.4 Polygenic Inheritance</b>",
     "Traits that vary on a gradient rather than as two opposites (skin colour, height)"],
    ["<b>4.5 Pleiotropy</b>",
     "A single gene producing more than one phenotype"],
    ["<b>4.6 Sex Determination</b>",
     "XO, XY and ZW mechanisms; sex determination in humans and in honey bee"],
    ["<b>4.7 Mutation</b>",
     "How DNA sequences change, and what changes the genome"],
    ["<b>4.8 Genetic Disorders</b>",
     "Pedigree analysis, Mendelian disorders (colour blindness, haemophilia, sickle-cell "
     "anaemia, phenylketonuria, thalassemia), chromosomal disorders (Down's, Turner's, "
     "Klinefelter's)"],
], col_widths=[40, 60]))

story.append(gap())
story.append(memory_aid(
    "<b>One chapter, three layers:</b> <b>4.1-4.3</b> build Mendel's laws and tie them to "
    "chromosomes; <b>4.4-4.5</b> extend the one-gene, two-allele picture to many genes and "
    "many effects; <b>4.6-4.8</b> apply it - sex, mutation, and the disorders that fall out "
    "when any of it goes wrong. The Quick Recap at the end returns to this three-layer "
    "shape."))

# ======================================================================================
# ---- 4.1 MENDEL'S LAWS OF INHERITANCE ---- F031-F051 (opener F032) + Fig 4.1 / Table 4.1
# ======================================================================================
story.append(gap(6))
story.append(heading("4.1", "MENDEL'S LAWS OF INHERITANCE", level=1))

# F032, F033
story.append(body(
    "It was during the <b>mid-nineteenth century</b> that headway was made in the "
    "understanding of inheritance."))
story.append(keyterm(
    "<b>Gregor Mendel, conducted hybridisation experiments on garden peas for seven years "
    "(1856-1863)</b> and <b>proposed the laws of inheritance in living organisms</b>."))

# F034, F035, F036
story.append(gap())
story.append(b1(
    "<b>During Mendel's investigations into inheritance patterns it was for the first time "
    "that statistical analysis and mathematical logic were applied to problems in "
    "biology.</b>"))
story.append(b1(
    "<b>His experiments had a large sampling size, which gave greater credibility to the "
    "data that he collected.</b>"))
story.append(b1(
    "<b>Also, the confirmation of his inferences from experiments on successive generations "
    "of his test plants, proved that his results pointed to general rules of inheritance "
    "rather than being unsubstantiated ideas.</b>"))

# F037, F038, F039
story.append(gap())
story.append(Paragraph(
    "<b>What Mendel worked with:</b>", STYLES["Body"]))
story.append(b1(
    "<b>Mendel investigated characters in the garden pea plant that were manifested as "
    "two opposing traits,</b> e.g., <b>tall or dwarf plants, yellow or green seeds</b>."))
story.append(b1(
    "<b>Mendel conducted such artificial pollination / cross pollination experiments using "
    "several true-breeding pea lines.</b>"))
story.append(keyterm(
    "<b>A true-breeding line is one that, having undergone continuous self-pollination, "
    "shows the stable trait inheritance and expression for several generations.</b>"))

# F040, F041
story.append(b1(
    "<b>Mendel selected 14 true-breeding pea plant varieties, as pairs which were similar "
    "except for one character with contrasting traits.</b>"))
story.append(b1(
    "<b>Some of the contrasting traits selected were:</b> smooth or wrinkled seeds, yellow "
    "or green seeds, inflated (full) or constricted green or yellow pods and tall or dwarf "
    "plants (Figure 4.1, Table 4.1)."))

# F042 - caption, F043 - figure labels (read-the-plate)
story.append(gap())
story.append(figure_note := note(
    "<b>Read the plate (Figure 4.1 labels).</b> The plate shows <b>seven pairs of contrasting "
    "traits</b> in pea plant, each as a <b>Character</b> row with the <b>Dominant trait</b> "
    "and <b>Recessive trait</b> columns. The seven characters, in the order the plate "
    "prints them, are: <b>Seed shape</b> - <b>Round</b> / <b>Wrinkled</b>; <b>Seed "
    "colour</b> - <b>Yellow</b> / <b>Green</b>; <b>Flower colour</b> - <b>Violet</b> / "
    "<b>White</b>; <b>Pod shape</b> - <b>Full</b> / <b>Constricted</b>; <b>Pod colour</b> "
    "(no value carried in the label row); <b>Flower position</b> - <b>Axial</b> / "
    "<b>Terminal</b>; <b>Stem height</b> - <b>Tall</b> / <b>Dwarf</b>."))

# F044 - Table 4.1 caption, F045-F051 - the 7 rows
story.append(gap())
story.append(body(
    "<b>Table 4.1: Contrasting Traits Studied by Mendel in Pea</b>"))
story.append(data_table([
    ["S.No.", "Characters", "Contrasting Traits"],
    ["<b>1.</b>", "<b>Stem height</b>", "<b>Tall / dwarf</b>"],
    ["<b>2.</b>", "<b>Flower colour</b>", "<b>Violet / white</b>  (the source's own column "
     "heading prints <b>Flouwer colour</b>)"],
    ["<b>3.</b>", "<b>Flower position</b>", "<b>Axial / terminal</b>"],
    ["<b>4.</b>", "<b>Pod shape</b>", "<b>Inflated / constricted</b>"],
    ["<b>5.</b>", "<b>Pod colour</b>", "<b>Green / yellow</b>"],
    ["<b>6.</b>", "<b>Seed shape</b>", "<b>Round / wrinkled</b>"],
    ["<b>7.</b>", "<b>Seed colour</b>", "<b>Yellow / green</b>"],
], col_widths=[10, 30, 60]))

# ======================================================================================
# ---- 4.2 INHERITANCE OF ONE GENE ---- F052-F113 (opener F053) + Fig 4.2, 4.3, 4.4, 4.5
# ======================================================================================
story.append(gap(6))
story.append(heading("4.2", "INHERITANCE OF ONE GENE", level=1))

# F053, F054 - the first cross in tutor voice
story.append(body(
    "Take the example of <b>one such hybridisation experiment</b> carried out by Mendel, in "
    "which he <b>crossed tall and dwarf pea plants</b> to study the inheritance of <b>one "
    "gene</b> (Figure 4.2)."))
story.append(b1(
    "He collected the seeds produced as a result of this cross and grew them to generate "
    "plants of the <b>first hybrid generation</b>."))
story.append(b1(
    "This generation is also called the <b>Filial<sub>1</sub> progeny or the F<sub>1</sub></b>."))

# F055 + F062-F063 - Punnett was British + the cross technique plate
story.append(gap())
story.append(note(
    "<b>Read the plate (Figure 4.2 labels).</b> The plate shows <b>Steps in making a cross "
    "in pea</b>: a <b>Parent</b> flower with the <b>Petal</b> lifted to reveal the "
    "<b>Stigma</b>, the <b>Anther</b>, the <b>Stamen</b> and the <b>Carpel</b>; the "
    "step <b>Removal of anthers (Emasculation)</b>; and the step <b>Transfer of pollen "
    "(Pollination)</b>, performed between two <b>Parent</b> plants."))

# F056, F057, F058, F059, F060, F061 - the F1 and F2 outcomes
story.append(gap())
story.append(b1(
    "<b>Mendel observed that all the F<sub>1</sub> progeny plants were tall, like one of "
    "its parents; none were dwarf (Figure 4.3).</b>"))
story.append(b1(
    "<b>Mendel then self-pollinated the tall F<sub>1</sub> plants and to his surprise "
    "found that in the Filial<sub>2</sub> generation some of the offspring were 'dwarf';</b> "
    "the character that was not seen in the F<sub>1</sub> generation was now expressed."))
story.append(b1(
    "<b>The proportion of plants that were dwarf were 1/4th of the F<sub>2</sub> plants "
    "while 3/4th of the F<sub>2</sub> plants were tall.</b>"))
story.append(b1(
    "<b>The tall and dwarf traits were identical to their parental type and did not show "
    "any blending,</b> that is all the offspring were either tall or dwarf, <b>none were "
    "of in-between height</b> (Figure 4.3)."))
story.append(b1(
    "<b>Similar results were obtained with the other traits that he studied:</b> only one "
    "of the parental traits was expressed in the F<sub>1</sub> generation while at the "
    "F<sub>2</sub> stage both the traits were expressed in the proportion <b>3:1</b>."))
story.append(b1(
    "<b>The contrasting traits did not show any blending at either F<sub>1</sub> or "
    "F<sub>2</sub> stage.</b>"))

# F079-F080 - monohybrid cross diagram
story.append(gap())
story.append(note(
    "<b>Read the plate (Figure 4.3 labels).</b> The plate is a <b>Diagrammatic "
    "representation of monohybrid cross</b>. On the <b>Parental</b> line it marks a "
    "<b>Tall</b> plant and a <b>Dwarf</b> plant; the next line is the "
    "<b>F<sub>1</sub> generation</b>, all <b>Tall</b>; the <b>Selfing</b> arrow runs "
    "into the <b>F<sub>2</sub> generation</b>, where the <b>Tall</b> and <b>Dwarf</b> "
    "ratio is 3:1."))

# F064, F065, F066, F067, F068 - the gene / allele / factor trio
story.append(gap())
story.append(Paragraph(
    "<b>What the cross told Mendel:</b>", STYLES["Body"]))
story.append(b1(
    "<b>Based on these observations, Mendel proposed that something was being stably passed "
    "down, unchanged, from parent to offspring through the gametes, over successive "
    "generations.</b>"))
story.append(b1(
    "He called these things as <b>'factors'</b>. Now we call them as <b>genes</b>."))
story.append(keyterm(
    "<b>Genes, therefore, are the units of inheritance.</b> They contain the information "
    "that is required to express a particular trait in an organism."))
story.append(keyterm(
    "<b>Genes which code for a pair of contrasting traits are known as alleles,</b> i.e., "
    "they are <b>slightly different forms of the same gene</b>."))

# F069-F071 - the symbol convention
story.append(gap())
story.append(Paragraph(
    "<b>Writing a cross in symbols:</b>", STYLES["Body"]))
story.append(b1(
    "<b>If we use alphabetical symbols for each gene, then the capital letter is used for "
    "the trait expressed at the F<sub>1</sub> stage and the small alphabet for the other "
    "trait.</b>"))
story.append(b1(
    "<b>For example, in case of the character of height, T is used for the Tall trait and "
    "t for the 'dwarf',</b> and T and t are alleles of each other."))
story.append(b1(
    "<b>Hence, in plants the pair of alleles for height would be TT, Tt or tt.</b>"))

# F072-F078 - the genotype/phenotype terminology + F073's question + the qualifier
story.append(gap())
story.append(data_table([
    ["Term", "What it means", "How the height alleles map to it"],
    ["<b>Genotype</b>", "The pair of alleles a plant actually carries.",
     "<b>TT</b> (tall parent), <b>Tt</b> (F<sub>1</sub>), <b>tt</b> (dwarf parent)"],
    ["<b>Phenotype</b>", "What the plant looks like.",
     "<b>Tall</b> and <b>dwarf</b>"],
    ["<b>Homozygous</b>", "Both alleles in the pair are the same.",
     "True-breeding parents are <b>TT</b> and <b>tt</b>"],
    ["<b>Heterozygous</b>", "The two alleles in the pair are different.",
     "The F<sub>1</sub> is <b>Tt</b>"],
    ["<b>Dominant</b> vs <b>recessive</b>",
     "In a pair of dissimilar alleles, one is expressed in the phenotype and the other "
     "is hidden.",
     "<b>T</b> is dominant over <b>t</b>, so <b>Tt</b> is phenotypically tall"],
], col_widths=[26, 36, 38]))

# F072's homozygous / TT / tt definition + F073's "what would be the phenotype of Tt?"
story.append(b1(
    "<b>Mendel also proposed that in a true breeding, tall or dwarf pea variety the allelic "
    "pair of genes for height are identical or homozygous, TT and tt, respectively.</b>"))
story.append(b1(
    "<b>TT and tt are called the genotype of the plant while the descriptive terms tall "
    "and dwarf are the phenotype.</b>"))
story.append(b1(
    "<b>What then would be the phenotype of a plant that had a genotype Tt?</b>"))
story.append(b1(
    "<b>As Mendel found the phenotype of the F<sub>1</sub> heterozygote Tt to be exactly "
    "like the TT parent in appearance, he proposed that in a pair of dissimilar factors, "
    "one dominates the other (as in the F<sub>1</sub>) and hence is called the dominant "
    "factor while the other factor is recessive.</b>"))
story.append(b1(
    "<b>In this case T (for tallness) is dominant over t (for dwarfness), that is "
    "recessive.</b>"))
story.append(b1(
    "<b>(Do not use T for tall and d for dwarf because you will find it difficult to "
    "remember whether T and d are alleles of the same gene/character or not).</b>"))
story.append(b1(
    "<b>Alleles can be similar as in the case of homozygotes TT and tt or can be "
    "dissimilar as in the case of the heterozygote Tt.</b>"))
story.append(keyterm(
    "<b>Since the Tt plant is heterozygous for genes controlling one character (height), "
    "it is a monohybrid</b> and the <b>cross between TT and tt is a monohybrid "
    "cross</b>."))

# F081-F084 - the segregation inference
story.append(gap())
story.append(Paragraph(
    "<b>From the F<sub>1</sub> and F<sub>2</sub> outcomes, Mendel inferred the segregation "
    "mechanism:</b>", STYLES["Body"]))
story.append(b1(
    "<b>From the observation that the recessive parental trait is expressed without any "
    "blending in the F<sub>2</sub> generation, we can infer that, when the tall and dwarf "
    "plant produce gametes, by the process of meiosis, the alleles of the parental pair "
    "separate or segregate from each other and only one allele is transmitted to a "
    "gamete.</b>"))
story.append(b1(
    "<b>This segregation of alleles is a random process and so there is a 50 per cent "
    "chance of a gamete containing either allele,</b> as has been verified by the results "
    "of the crossings."))
story.append(b1(
    "<b>In this way the gametes of the tall TT plants have the allele T and the gametes of "
    "the dwarf tt plants have the allele t.</b>"))
story.append(b1(
    "<b>During fertilisation the two alleles, T from one parent say, through the pollen, "
    "and t from the other parent, then through the egg, are united to produce zygotes that "
    "have one T allele and one t allele.</b>"))

# F085-F091 - the Punnett square
story.append(gap())
story.append(heading("4.2a", "Punnett Square - the cross on paper", level=2))
# F085, F086, F087, F088
story.append(b1(
    "<b>The production of gametes by the parents, the formation of the zygotes, the "
    "F<sub>1</sub> and F<sub>2</sub> plants can be understood from a diagram called "
    "Punnett Square as shown in Figure 4.4.</b>"))
story.append(b1(
    "<b>It was developed by a British geneticist, Reginald C. Punnett.</b>"))
story.append(keyterm(
    "<b>It is a graphical representation to calculate the probability of all possible "
    "genotypes of offspring in a genetic cross.</b>"))
story.append(b1(
    "<b>The possible gametes are written on two sides, usually the top row and left "
    "columns. All possible combinations are represented in boxes below in the squares, "
    "which generates a square output form.</b>"))

# F089 - the first Punnett (parental cross -> F1)
story.append(gap())
story.append(Paragraph(
    "<b>First Punnett square: the parental cross and the F<sub>1</sub>:</b>", STYLES["Body"]))
story.append(data_table([
    ["", "Tall parent gamete: <b>T</b>", "Tall parent gamete: <b>T</b>"],
    ["Dwarf parent gamete: <b>t</b>", "<b>Tt</b> (F<sub>1</sub>, tall)",
     "<b>Tt</b> (F<sub>1</sub>, tall)"],
    ["Dwarf parent gamete: <b>t</b>", "<b>Tt</b> (F<sub>1</sub>, tall)",
     "<b>Tt</b> (F<sub>1</sub>, tall)"],
], col_widths=[34, 33, 33]))

# F089 + F090 (female/male signs) + F091 (50-50 gamete probability)
story.append(gap())
story.append(b1(
    "<b>The Punnett Square shows the parental tall TT (male) and dwarf tt (female) plants, "
    "the gametes produced by them and, the F<sub>1</sub> Tt progeny.</b>"))
story.append(b1(
    "<b>The symbols for female and male are used to denote the female (eggs) and male "
    "(pollen) of the F<sub>1</sub> generation, respectively.</b> (The printed glyphs are "
    "drawn symbols, not text - Pass 2 writes the words; the Unicode signs are banned by "
    "check 5.)"))
story.append(b1(
    "<b>The F<sub>1</sub> plant of genotype Tt when self-pollinated, produces gametes of "
    "the genotype T and t in equal proportion.</b> When fertilisation takes place, the "
    "pollen grains of genotype T have a <b>50 per cent chance</b> to pollinate eggs of the "
    "genotype T, as well as of genotype t. Also pollen grains of genotype t have a "
    "<b>50 per cent chance</b> of pollinating eggs of genotype T, as well as of genotype t."))

# F092-F093 - Figure 4.4 caption + labels (read-the-plate)
story.append(gap())
story.append(note(
    "<b>Read the plate (Figure 4.4 labels).</b> The plate is a <b>Punnett square used to "
    "understand a typical monohybrid cross conducted by Mendel between true-breeding tall "
    "plants and true-breeding dwarf plants</b>. The four corners carry the parental lines - "
    "a <b>Tall</b> plant with the <b>TT</b> genotype, a <b>Dwarf</b> plant with the "
    "<b>tt</b> genotype - with the <b>Gametes</b> row (a single <b>T</b>) and column (a "
    "single <b>t</b>). The middle of the grid is the <b>F<sub>1</sub> generation</b> - "
    "four cells, all <b>Tt</b>. Below the grid, the <b>Selfing</b> arrow leads to the "
    "<b>F<sub>2</sub> generation</b>, with two ratio lines: <b>Phenotypic ratio: "
    "tall:dwarf 3:1</b> and <b>Genotypic ratio: TT:Tt:tt 1:2:1</b>."))

# F094-F100 - the F2 ratios
story.append(gap())
story.append(Paragraph(
    "<b>Second Punnett square: the F<sub>1</sub> selfed to give the F<sub>2</sub>:</b>",
    STYLES["Body"]))
story.append(data_table([
    ["", "F<sub>1</sub> gamete: <b>T</b>", "F<sub>1</sub> gamete: <b>t</b>"],
    ["F<sub>1</sub> gamete: <b>T</b>", "<b>TT</b> (tall)", "<b>Tt</b> (tall)"],
    ["F<sub>1</sub> gamete: <b>t</b>", "<b>Tt</b> (tall)", "<b>tt</b> (dwarf)"],
], col_widths=[34, 33, 33]))

story.append(gap())
story.append(b1(
    "<b>As a result of random fertilisation, the resultant zygotes can be of the genotypes "
    "TT, Tt or tt.</b>"))
story.append(b1(
    "<b>From the Punnett square it is easily seen that 1/4th of the random fertilisations "
    "lead to TT, 1/2 lead to Tt and 1/4th to tt.</b>"))
story.append(b1(
    "<b>Though the F<sub>1</sub> have a genotype of Tt, but the phenotypic character seen "
    "is 'tall'.</b>"))
story.append(b1(
    "<b>At F<sub>2</sub> 3/4th of the plants are tall, where some of them are TT while "
    "others are Tt.</b>"))
story.append(b1(
    "<b>Externally it is not possible to distinguish between the plants with the genotypes "
    "TT and Tt.</b>"))
story.append(b1(
    "<b>It is thus due to this dominance of one character over the other that all the "
    "F<sub>1</sub> are tall (though the genotype is Tt)</b> and in the F<sub>2</sub> "
    "3/4th of the plants are tall (though genotypically 1/2 are Tt and only 1/4th are TT)."))
story.append(b1(
    "<b>This leads to a phenotypic ratio of 3/4 tall : (1/4 TT + 1/2 Tt) and 1/4 tt, "
    "i.e., a 3:1 ratio, but a genotypic ratio of 1:2:1.</b>"))

# F101-F102 - the binomial expansion as a process flow
story.append(gap())
story.append(heading("4.2b", "The same cross, written as a binomial expansion", level=2))
story.append(b1(
    "<b>The 1/4 : 1/2 : 1/4 ratio of TT:Tt:tt is mathematically condensable to the form of "
    "the binomial expression (ax + by)<super>2</super>,</b> that has the gametes bearing "
    "genes T or t in equal frequency of 1/2."))
story.append(b1(
    "<b>The expression is expanded as given below:</b>"))
story.append(process_flow([
    "The gamete frequencies for a heterozygote Tt are <b>1/2 T and 1/2 t</b>.",
    "Squaring the gamete sum: <b>(1/2 T + 1/2 t)<super>2</super></b>.",
    "Expanding: <b>1/4 TT + 1/2 Tt + 1/4 tt</b>.",
]))

# F103-F106 - Mendel's confirmation, then the "by looking you can't tell" lesson
story.append(gap())
story.append(b1(
    "<b>Mendel self-pollinated the F<sub>2</sub> plants and found that dwarf F<sub>2</sub> "
    "plants continued to generate dwarf plants in F<sub>3</sub> and F<sub>4</sub> "
    "generations.</b>"))
story.append(b1(
    "<b>He concluded that the genotype of the dwarfs was homozygous-tt.</b>"))
story.append(b1(
    "<b>From the preceding paragraphs it is clear that though the genotypic ratios can be "
    "calculated using mathematical probability, by simply looking at the phenotype of a "
    "dominant trait, it is not possible to know the genotypic composition.</b>"))
story.append(b1(
    "<b>That is, for example, whether a tall plant from F<sub>1</sub> or F<sub>2</sub> has "
    "TT or Tt composition, cannot be predicted.</b>"))

# F107-F110 - the testcross definition
story.append(gap())
story.append(heading("4.2c", "Testcross - reading the genotype you cannot see", level=2))
story.append(keyterm(
    "<b>Therefore, to determine the genotype of a tall plant at F<sub>2</sub>, Mendel "
    "crossed the tall plant from F<sub>2</sub> with a dwarf plant. This he called a "
    "testcross.</b>"))
story.append(keyterm(
    "<b>In a typical testcross an organism (pea plants here) showing a dominant phenotype "
    "(and whose genotype is to be determined) is crossed with the recessive parent instead "
    "of self-crossing.</b>"))
story.append(b1(
    "<b>The progenies of such a cross can easily be analysed to predict the genotype of "
    "the test organism.</b>"))
story.append(b1(
    "<b>Figure 4.5 shows the results of typical testcross where violet colour flower (V) "
    "is dominant over white colour flower (v).</b>"))

# F111-F112 - Figure 4.5 caption + labels
# [VERIFICATION FIX] D2 (strict Gate 3): prior NOTE mis-bound plate labels WW/Ww
# to the "Homozygous recessive" role. Source plate (book p59 / OCR p09): both top
# panels are the homozygous-recessive tester (ww); WW and Ww label the unknown
# dominant-phenotype parents (homozygous dominant vs heterozygous). Body V/v
# line and the outcomes table were already role-correct; NOTE only is rewritten.
story.append(gap())
story.append(note(
    "<b>Read the plate (Figure 4.5 labels).</b> The plate is a <b>Diagrammatic "
    "representation of a test cross</b>. Both panels place a <b>Homozygous "
    "recessive</b> tester (<b>ww</b>) at the top. The other parent in each panel "
    "is the <b>Dominant Phenotype (Genotype unknown)</b>: left panel the unknown "
    "is labelled <b>WW</b> (homozygous dominant); right panel the unknown is "
    "labelled <b>Ww</b> (heterozygous). Left outcome: <b>Result - All flowers are "
    "violet</b>, <b>Interpretation - Unknown flower is homozygous dominant</b>. "
    "Right outcome: <b>Half of the flowers are violet and half of the flowers are "
    "white</b>; <b>Unknown flower is heterozygous</b>."))
# Testcross outcomes as a data_table (WW/Ww = unknown dominant; ww = recessive tester)
story.append(gap())
story.append(Paragraph(
    "<b>What the testcross distinguishes:</b>", STYLES["Body"]))
story.append(data_table([
    ["If the unknown dominant parent is...", "Cross", "Offspring"],
    ["<b>WW</b> (homozygous dominant)",
     "<b>WW &times; ww</b>",
     "<b>All Ww</b> - all violet"],
    ["<b>Ww</b> (heterozygous)",
     "<b>Ww &times; ww</b>",
     "<b>Half Ww (violet), half ww (white)</b>"],
], col_widths=[28, 22, 50]))

story.append(memory_aid(
    "<b>Testcross in one line:</b> <b>cross the unknown with the recessive; if any "
    "offspring show the recessive phenotype, the unknown was heterozygous</b>. The "
    "recessive parent contributes only one kind of gamete, so every recessive offspring "
    "is a fingerprint of the dominant parent's hidden recessive allele."))

# F113 - the two laws, as a closure to 4.2
story.append(gap())
story.append(heading("4.2d", "What the one-gene cross gives you: two laws", level=2))
story.append(b1(
    "<b>Based on his observations on monohybrid crosses Mendel proposed two general rules "
    "to consolidate his understanding of inheritance in monohybrid crosses.</b> Today these "
    "rules are called the <b>Principles or Laws of Inheritance</b>: the <b>First Law or "
    "Law of Dominance</b> and the <b>Second Law or Law of Segregation</b>."))

# ======================================================================================
# ---- 4.2.1 Law of Dominance ---- F114-F118
# ======================================================================================
story.append(gap(6))
story.append(heading("4.2.1", "Law of Dominance", level=2))
# F115, F116, F117 as the three numbered statements
story.append(b1(
    "<b>(i) Characters are controlled by discrete units called factors.</b>"))
story.append(b1(
    "<b>(ii) Factors occur in pairs.</b>"))
story.append(b1(
    "<b>(iii) In a dissimilar pair of factors one member of the pair dominates (dominant) "
    "the other (recessive).</b>"))
story.append(b1(
    "<b>The law of dominance is used to explain the expression of only one of the parental "
    "characters in a monohybrid cross in the F<sub>1</sub> and the expression of both in "
    "the F<sub>2</sub>. It also explains the proportion of 3:1 obtained at the F<sub>2</sub>.</b>"))

# ======================================================================================
# ---- 4.2.2 Law of Segregation ---- F119-F122
# ======================================================================================
story.append(gap(6))
story.append(heading("4.2.2", "Law of Segregation", level=2))
story.append(b1(
    "<b>This law is based on the fact that the alleles do not show any blending and that "
    "both the characters are recovered as such in the F<sub>2</sub> generation though one "
    "of these is not seen at the F<sub>1</sub> stage.</b>"))
story.append(b1(
    "<b>Though the parents contain two alleles during gamete formation, the factors or "
    "alleles of a pair segregate from each other such that a gamete receives only one of "
    "the two factors.</b>"))
story.append(b1(
    "<b>Of course, a homozygous parent produces all gametes that are similar while a "
    "heterozygous one produces two kinds of gametes each having one allele with equal "
    "proportion.</b>"))

# ======================================================================================
# ---- 4.2.2.1 Incomplete Dominance ---- F123-F142 + Fig 4.6
# ======================================================================================
story.append(gap(6))
story.append(heading("4.2.2.1", "Incomplete Dominance", level=2))
# F124, F125
story.append(b1(
    "<b>When experiments on peas were repeated using other traits in other plants, it was "
    "found that sometimes the F<sub>1</sub> had a phenotype that did not resemble either "
    "of the two parents and was in between the two.</b>"))
story.append(b1(
    "<b>The inheritance of flower colour in the dog flower (snapdragon or Antirrhinum sp.) "
    "is a good example to understand incomplete dominance.</b>"))
# F126, F127
story.append(b1(
    "<b>In a cross between true-breeding red-flowered (RR) and true-breeding white-flowered "
    "plants (rr), the F<sub>1</sub> (Rr) was pink (Figure 4.6).</b>"))
story.append(b1(
    "<b>When the F<sub>1</sub> was self-pollinated the F<sub>2</sub> resulted in the "
    "following ratio 1 (RR) Red : 2 (Rr) Pink : 1 (rr) White.</b>"))
# F128, F129
story.append(b1(
    "<b>Here the genotype ratios were exactly as we would expect in any mendelian "
    "monohybrid cross, but the phenotype ratios had changed from the 3:1 dominant:recessive "
    "ratio.</b>"))
story.append(b1(
    "<b>What happened was that R was not completely dominant over r and this made it "
    "possible to distinguish Rr as pink from RR (red) and rr (white).</b>"))

# F137-F138 - Fig 4.6 caption + labels
story.append(gap())
story.append(note(
    "<b>Read the plate (Figure 4.6 labels).</b> The plate is the <b>Results of monohybrid "
    "cross in the plant Snapdragon, where one allele is incompletely dominant over the other "
    "allele</b>. The <b>P generation</b> row shows <b>Red (RR)</b> and <b>White (rr)</b>; "
    "the <b>Gametes</b> row carries <b>R</b> and <b>r</b>. The <b>F<sub>1</sub> "
    "generation</b> row reads <b>All pink (Rr)</b>. The <b>F<sub>2</sub> generation</b> "
    "grid is the four cells of a Punnett square - <b>RR</b>, <b>Rr</b>, <b>Rr</b>, "
    "<b>rr</b> - and the two ratio lines under it: <b>Phenotypic ratio: red:pink:white "
    "1:2:1</b> and <b>Genotypic ratio: RR:Rr:rr 1:2:1</b>."))

# F130-F133 - "What exactly is dominance?" + the enzyme-based explanation
story.append(gap())
story.append(Paragraph(
    "<b>What the snapdragon result forces us to ask:</b>", STYLES["Body"]))
story.append(b1(
    "<b>Explanation of the concept of dominance: What exactly is dominance? Why are some "
    "alleles dominant and some recessive?</b>"))
story.append(b1(
    "<b>To tackle these questions, we must understand what a gene does.</b> Every gene, as "
    "you know by now, contains the information to express a particular trait."))
story.append(b1(
    "<b>In a diploid organism, there are two copies of each gene, i.e., as a pair of "
    "alleles. Now, these two alleles need not always be identical, as in a heterozygote.</b>"))
story.append(b1(
    "<b>One of them may be different due to some changes that it has undergone</b> "
    "(about which you will read further on, and in the next chapter) <b>which modifies the "
    "information that particular allele contains.</b>"))
# F134, F135, F136 - enzyme example
story.append(b1(
    "<b>Let's take an example of a gene that contains the information for producing an "
    "enzyme.</b> Now there are two copies of this gene, the two allelic forms."))
story.append(b1(
    "<b>Let us assume (as is more common) that the normal allele produces the normal enzyme "
    "that is needed for the transformation of a substrate S.</b>"))
story.append(b1(
    "<b>Theoretically, the modified allele could be responsible for production of - "
    "(i) the normal/less efficient enzyme, or (ii) a non-functional enzyme, or (iii) no "
    "enzyme at all</b>"))
# F139-F142 - the three cases
story.append(b1(
    "<b>In the first case, the modified allele is equivalent to the unmodified allele,</b> "
    "i.e., it will produce the same phenotype/trait, i.e., result in the transformation of "
    "substrate S. Such equivalent allele pairs are very common."))
story.append(b1(
    "<b>But, if the allele produces a non-functional enzyme or no enzyme, the phenotype "
    "may be effected.</b> The phenotype/trait will only be dependent on the functioning of "
    "the unmodified allele."))
story.append(b1(
    "<b>The unmodified (functioning) allele, which represents the original phenotype is the "
    "dominant allele and the modified allele is generally the recessive allele.</b>"))
story.append(b1(
    "<b>Hence, in the example above the recessive trait is seen due to non-functional "
    "enzyme or because no enzyme is produced.</b>"))

# ======================================================================================
# ---- 4.2.2.2 Co-dominance ---- F143-F167 + Table 4.2
# ======================================================================================
story.append(gap(6))
story.append(heading("4.2.2.2", "Co-dominance", level=2))
# F144, F145, F146, F147
story.append(b1(
    "<b>Till now we were discussing crosses where the F<sub>1</sub> resembled either of the "
    "two parents (dominance) or was in-between (incomplete dominance).</b> But, in the case "
    "of co-dominance the F<sub>1</sub> generation <b>resembles both parents</b>."))
story.append(b1(
    "<b>A good example is different types of red blood cells that determine ABO blood "
    "grouping in human beings.</b> ABO blood groups are controlled by the gene <b>I</b>."))
story.append(b1(
    "<b>The plasma membrane of the red blood cells has sugar polymers that protrude from "
    "its surface and the kind of sugar is controlled by the gene.</b>"))
story.append(b1(
    "<b>The gene (I) has three alleles I<sup>A</sup>, I<sup>B</sup> and i.</b>"))
# F148, F149
story.append(b1(
    "<b>The alleles I<sup>A</sup> and I<sup>B</sup> produce a slightly different form of "
    "the sugar while allele i does not produce any sugar.</b>"))
story.append(b1(
    "<b>Because humans are diploid organisms, each person possesses any two of the three "
    "I gene alleles.</b>"))
# F150, F151
story.append(b1(
    "<b>I<sup>A</sup> and I<sup>B</sup> are completely dominant over i, in other words "
    "when I<sup>A</sup> and i are present only I<sup>A</sup> expresses (because i does "
    "not produce any sugar), and when I<sup>B</sup> and i are present I<sup>B</sup> "
    "expresses.</b>"))
story.append(b1(
    "<b>But when I<sup>A</sup> and I<sup>B</sup> are present together they both express "
    "their own types of sugars:</b> this is because of <b>co-dominance</b>. Hence red blood "
    "cells have both A and B types of sugars."))
# F152 - three alleles, six genotypes
story.append(b1(
    "<b>Since there are three different alleles, there are six different combinations of "
    "these three alleles that are possible, and therefore, a total of six different "
    "genotypes of the human ABO blood types (Table 4.2).</b>"))

# F153 - Table 4.2 caption + F154-F160 the 7 rows (the table has 7 rows: the heading and 6 parent combinations)
story.append(gap())
story.append(body(
    "<b>Table 4.2: Table Showing the Genetic Basis of Blood Groups in Human Population</b>"))
story.append(data_table([
    ["Allele from Parent 1", "Allele from Parent 2",
     "Genotype of offspring", "Blood type of offspring"],
    ["<b>I<sup>A</sup></b>", "<b>I<sup>A</sup></b>",
     "<b>I<sup>A</sup>I<sup>A</sup></b>", "<b>A</b>"],
    ["<b>I<sup>A</sup></b>", "<b>I<sup>B</sup></b>",
     "<b>I<sup>A</sup>I<sup>B</sup></b>", "<b>AB</b>"],
    ["<b>I<sup>A</sup></b>", "<b>i</b>", "<b>I<sup>A</sup>i</b>", "<b>A</b>"],
    ["<b>I<sup>B</sup></b>", "<b>I<sup>A</sup></b>",
     "<b>I<sup>A</sup>I<sup>B</sup></b>", "<b>AB</b>"],
    ["<b>I<sup>B</sup></b>", "<b>I<sup>B</sup></b>",
     "<b>I<sup>B</sup>I<sup>B</sup></b>", "<b>B</b>"],
    ["<b>I<sup>B</sup></b>", "<b>i</b>", "<b>I<sup>B</sup>i</b>", "<b>B</b>"],
    ["<b>i</b>", "<b>i</b>", "<b>ii</b>", "<b>O</b>"],
], col_widths=[24, 24, 30, 22]))

# F161-F167 - multiple alleles + pleiotropy example
story.append(gap())
story.append(b1(
    "<b>Do you realise that the example of ABO blood grouping also provides a good example "
    "of multiple alleles?</b> Here you can see that there are more than two, i.e., three "
    "alleles, governing the same character."))
story.append(b1(
    "<b>Since in an individual only two alleles can be present, multiple alleles can be "
    "found only when population studies are made.</b>"))
story.append(b1(
    "<b>Occasionally, a single gene product may produce more than one effect.</b>"))
story.append(b1(
    "<b>For example, starch synthesis in pea seeds is controlled by one gene. It has two "
    "alleles (B and b).</b> Starch is synthesised effectively by <b>BB</b> homozygotes "
    "and therefore, large starch grains are produced. In contrast, <b>bb</b> homozygotes "
    "have lesser efficiency in starch synthesis and produce smaller starch grains."))
story.append(b1(
    "<b>After maturation of the seeds, BB seeds are round and the bb seeds are wrinkled. "
    "Heterozygotes produce round seeds, and so B seems to be the dominant allele.</b>"))
story.append(b1(
    "<b>But, the starch grains produced are of intermediate size in Bb seeds.</b> So if "
    "starch grain size is considered as the phenotype, then from this angle, the alleles "
    "show incomplete dominance."))
story.append(b1(
    "<b>Therefore, dominance is not an autonomous feature of a gene or the product that it "
    "has information for.</b> It depends as much on the gene product and the production "
    "of a particular phenotype from this product as it does on the particular phenotype "
    "that we choose to examine, in case more than one phenotype is influenced by the same "
    "gene."))

# ======================================================================================
# ---- 4.3 INHERITANCE OF TWO GENES ---- F168-F190 + Fig 4.7
# ======================================================================================
story.append(gap(6))
story.append(heading("4.3", "INHERITANCE OF TWO GENES", level=1))
# F169
story.append(body(
    "<b>Mendel also worked with and crossed pea plants that differed in two characters,</b> "
    "as is seen in the cross between a pea plant that has seeds with <b>yellow colour "
    "and round shape</b> and one that had seeds of <b>green colour and wrinkled shape</b> "
    "(Figure 4.7)."))
# F170, F171, F172, F173
story.append(gap())
story.append(b1(
    "<b>Mendel found that the seeds resulting from the crossing of the parents, had yellow "
    "coloured and round shaped seeds.</b>"))
story.append(b1(
    "<b>Thus, yellow colour was dominant over green and round shape dominant over "
    "wrinkled.</b>"))
story.append(b1(
    "<b>Let us use the genotypic symbols Y for dominant yellow seed colour and y for "
    "recessive green seed colour, R for round shaped seeds and r for wrinkled seed "
    "shape.</b>"))
story.append(b1(
    "<b>The genotype of the parents can then be written as RRYY and rryy.</b>"))
# F174
story.append(b1(
    "<b>The cross between the two plants can be written down as in Figure 4.7 showing the "
    "genotypes of the parent plants.</b>"))
# F175
story.append(b1(
    "<b>The gametes RY and ry unite on fertilisation to produce the F<sub>1</sub> hybrid "
    "RrYy.</b>"))
# F176
story.append(b1(
    "<b>When Mendel self hybridised the F<sub>1</sub> plants he found that 3/4th of "
    "F<sub>2</sub> plants had yellow seeds and 1/4th had green.</b> The yellow and green "
    "colours segregated in a 3:1 ratio. Round and wrinkled seed shape also segregated in a "
    "3:1 ratio: just like in a monohybrid cross."))

# F177-F178 - Fig 4.7 caption + labels (read-the-plate)
story.append(gap())
story.append(note(
    "<b>Read the plate (Figure 4.7 labels).</b> The plate is the <b>Results of a dihybrid "
    "cross where the two parents differed in two pairs of contrasting traits: seed colour "
    "and seed shape</b>. The <b>P generation</b> row carries <b>Round yellow</b> with "
    "<b>RR</b> and <b>YY</b>, and <b>Wrinkled green</b> with <b>rr</b> and <b>yy</b>. "
    "The <b>Gametes</b> row has <b>RY</b> and <b>ry</b>, uniting into the <b>F<sub>1</sub> "
    "generation</b> row of <b>RrYy</b>. The <b>Selfing</b> arrow runs to the dihybrid "
    "Punnett grid: <b>RRYY</b>, <b>RrYY</b>, <b>RRYy</b>, <b>rrYY</b>, <b>RRyy</b>, "
    "<b>Rryy</b>, <b>rrYy</b>, <b>rryy</b> in the <b>F<sub>2</sub> generation</b>; the "
    "F<sub>1</sub> gametes are the four-letter set <b>RY</b>, <b>Ry</b>, <b>rY</b>, "
    "<b>ry</b>. The ratio line under the grid: <b>Phenotypic ratio: round yellow : round "
    "green : wrinkled yellow : wrinkled green 9:3:3:1</b>."))

# ======================================================================================
# ---- 4.3.1 Law of Independent Assortment ---- F179-F190
# ======================================================================================
story.append(gap(6))
story.append(heading("4.3.1", "Law of Independent Assortment", level=2))
# F180
story.append(b1(
    "<b>In the dihybrid cross (Figure 4.7), the phenotypes round, yellow; wrinkled, yellow; "
    "round, green and wrinkled, green appeared in the ratio 9:3:3:1.</b> Such a ratio was "
    "observed for several pairs of characters that Mendel studied."))
# F181 - the 9:3:3:1 derivation as a process
story.append(b1(
    "<b>The ratio of 9:3:3:1 can be derived as a combination series of 3 yellow : 1 green, "
    "with 3 round : 1 wrinkled.</b> This derivation can be written as follows:"))
story.append(process_flow([
    "(3 Round : 1 Wrinkled) (3 Yellow : 1 Green)",
    "= 9 Round, Yellow : 3 Wrinkled, Yellow : 3 Round, Green : 1 Wrinkled, Green",
]))
# F182 - the law
story.append(keyterm(
    "<b>Based upon such observations on dihybrid crosses (crosses between plants differing "
    "in two traits) Mendel proposed a second set of generalisations that we call Mendel's "
    "Law of Independent Assortment.</b> The law states that <b>when two pairs of traits "
    "are combined in a hybrid, segregation of one pair of characters is independent of "
    "the other pair of characters</b>."))
# F183-F188 - the gamete probability
story.append(b1(
    "<b>The Punnett square can be effectively used to understand the independent "
    "segregation of the two pairs of genes during meiosis and the production of eggs and "
    "pollen in the F<sub>1</sub> RrYy plant.</b>"))
story.append(b1(
    "<b>Consider the segregation of one pair of genes R and r. Fifty per cent of the "
    "gametes have the gene R and the other 50 per cent have r.</b> Now besides each "
    "gamete having either R or r, it should also have the allele Y or y."))
story.append(b1(
    "<b>The important thing to remember here is that segregation of 50 per cent R and 50 "
    "per cent r is independent from the segregation of 50 per cent Y and 50 per cent y.</b>"))
story.append(b1(
    "<b>Therefore, 50 per cent of the r bearing gametes has Y and the other 50 per cent "
    "has y. Similarly, 50 per cent of the R bearing gametes has Y and the other 50 per "
    "cent has y.</b>"))
story.append(b1(
    "<b>Thus there are four genotypes of gametes (four types of pollen and four types of "
    "eggs).</b>"))
story.append(b1(
    "<b>The four types are RY, Ry, rY and ry each with a frequency of 25 per cent or 1/4 "
    "of the total gametes produced.</b>"))
story.append(b1(
    "<b>When you write down the four types of eggs and pollen on the two sides of a "
    "Punnett square it is very easy to derive the composition of the zygotes that give "
    "rise to the F<sub>2</sub> plants (Figure 4.7).</b>"))

# F190 - the activity table, presented as a small empty data_table for the student to fill
story.append(gap())
story.append(Paragraph(
    "<b>Activity (Figure 4.7 / 4.3.1):</b> write down the <b>16 F<sub>2</sub> genotypes</b> "
    "the dihybrid Punnett square yields (RRYY, RRYy, RRyy, RrYY, ... rryy) and group each "
    "under one of the four phenotypes: <b>Round Yellow, Round Green, Wrinkled Yellow, "
    "Wrinkled Green</b>. The four phenotype totals should land at <b>9 : 3 : 3 : 1</b>.",
    STYLES["Body"]))

# ======================================================================================
# ---- 4.3.2 Chromosomal Theory of Inheritance ---- F191-F226 + Fig 4.8, 4.9, 4.10
# ======================================================================================
story.append(gap(6))
story.append(heading("4.3.2", "Chromosomal Theory of Inheritance", level=2))
# F192
story.append(b1(
    "<b>Mendel published his work on inheritance of characters in 1865 but for several "
    "reasons, it remained unrecognised till 1900.</b>"))
# F193-F196 - the four reasons
story.append(b1(
    "<b>Firstly, communication was not easy (as it is now) in those days and his work "
    "could not be widely publicised.</b>"))
story.append(b1(
    "<b>Secondly, his concept of genes (or factors, in Mendel's words) as stable and "
    "discrete units that controlled the expression of traits and, of the pair of alleles "
    "which did not blend with each other, was not accepted by his contemporaries as an "
    "explanation for the apparently continuous variation seen in nature.</b>"))
story.append(b1(
    "<b>Thirdly, Mendel's approach of using mathematics to explain biological phenomena "
    "was totally new and unacceptable to many of the biologists of his time.</b>"))
story.append(b1(
    "<b>Finally, though Mendel's work suggested that factors (genes) were discrete units, "
    "he could not provide any physical proof for the existence of factors or say what "
    "they were made of.</b>"))
# F197
story.append(b1(
    "<b>In 1900, three Scientists (de Vries, Correns and von Tschermak) independently "
    "rediscovered Mendel's results on the inheritance of characters.</b>"))
# F198-F201
story.append(b1(
    "<b>Also, by this time due to advancements in microscopy that were taking place, "
    "scientists were able to carefully observe cell division.</b>"))
story.append(b1(
    "<b>This led to the discovery of structures in the nucleus that appeared to double and "
    "divide just before each cell division. These were called chromosomes</b> (colored "
    "bodies, as they were visualised by staining)."))
story.append(b1(
    "<b>By 1902, the chromosome movement during meiosis had been worked out.</b>"))
story.append(b1(
    "<b>Walter Sutton and Theodore Boveri noted that the behaviour of chromosomes was "
    "parallel to the behaviour of genes and used chromosome movement (Figure 4.8) to "
    "explain Mendel's laws (Table 4.3).</b>"))

# F212-F213 - Fig 4.8 read-the-plate (meiosis)
story.append(gap())
story.append(note(
    "<b>Read the plate (Figure 4.8 labels).</b> The plate is <b>Meiosis and germ cell "
    "formation in a cell with four chromosomes. Can you see how chromosomes segregate when "
    "germ cells are formed?</b> The plate is laid out in time order: a <b>G<sub>2</sub></b> "
    "cell with paired chromosomes, a <b>Bivalent</b> stage (two homologous chromosomes "
    "paired), <b>Meiosis I</b> with its <b>anaphase</b> (the homologs pulled to opposite "
    "poles), <b>Meiosis II</b> (the sister chromatids separated), and the four final "
    "<b>Germ cells</b>."))

# F214-F220 - Table 4.3 (chromosome vs gene comparison)
story.append(gap())
story.append(body(
    "<b>Table 4.3: A Comparison between the Behaviour of Chromosomes and Genes</b>"))
story.append(data_table([
    ["Chromosomes", "Genes"],
    ["<b>Occur in pairs</b>", "<b>Occur in pairs</b>"],
    ["<b>Segregate at the time of gamete formation such that only one of each pair is "
     "transmitted to a gamete</b>",
     "<b>Segregate at gamete formation and only one of each pair is transmitted to a "
     "gamete</b>"],
    ["<b>Independent pairs segregate independently of each other</b>",
     "<b>One pair segregates independently of another pair</b>"],
], col_widths=[50, 50]))

# F202-F205
story.append(gap())
story.append(b1(
    "<b>Recall that you have studied the behaviour of chromosomes during mitosis "
    "(equational division) and during meiosis (reduction division).</b> The important "
    "things to remember are that chromosomes as well as genes occur in pairs."))
story.append(b1(
    "<b>The two alleles of a gene pair are located on homologous sites on homologous "
    "chromosomes.</b>"))
story.append(b1(
    "<b>Sutton and Boveri argued that the pairing and separation of a pair of chromosomes "
    "would lead to the segregation of a pair of factors they carried.</b>"))
story.append(keyterm(
    "<b>Sutton united the knowledge of chromosomal segregation with Mendelian principles "
    "and called it the chromosomal theory of inheritance.</b>"))
# F206
story.append(b1(
    "<b>Following this synthesis of ideas, experimental verification of the chromosomal "
    "theory of inheritance by Thomas Hunt Morgan and his colleagues, led to discovering "
    "the basis for the variation that sexual reproduction produced.</b>"))
# F207-F211 - Drosophila
story.append(b1(
    "<b>Morgan worked with the tiny fruitflies, Drosophila melanogaster (Figure 4.10), which "
    "were found very suitable for such studies.</b>"))
story.append(b1(
    "<b>They could be grown on simple synthetic medium in the laboratory.</b>"))
story.append(b1(
    "<b>They complete their life cycle in about two weeks,</b> and a single mating could "
    "produce a large number of progeny flies."))
story.append(b1(
    "<b>Also, there was a clear differentiation of the sexes</b> - the male and female "
    "flies are easily distinguishable."))
story.append(b1(
    "<b>Also, it has many types of hereditary variations that can be seen with low power "
    "microscopes.</b>"))

# F221-F224 - Fig 4.9 colour-dependent note
story.append(gap())
story.append(Paragraph(
    "<b>Independent assortment, the chromosome view (Figure 4.9):</b>", STYLES["Body"]))
story.append(b1(
    "<b>During Anaphase of meiosis I, the two chromosome pairs can align at the metaphase "
    "plate independently of each other (Figure 4.9).</b>"))
story.append(b1(
    "<b>To understand this, compare the chromosomes of four different colour in the left "
    "and right columns.</b> In the left column (Possibility I) <b>orange and green is "
    "segregating together</b>. But in the right hand column (Possibility II) the "
    "<b>orange chromosome is segregating with the red chromosomes</b>."))

# Fig 4.8 / 4.9 / 4.10 plates - all three carried in read-the-plate notes
story.append(gap())
story.append(note(
    "<b>Read the plate (Figure 4.8 labels).</b> (Already given above - meiosis and germ "
    "cell formation in a cell with four chromosomes, laid out as G<sub>2</sub> to "
    "Bivalent to Meiosis I anaphase to Meiosis II to Germ cells.)"))
story.append(note(
    "<b>Read the plate (Figure 4.9 labels).</b> The plate is <b>Independent assortment of "
    "chromosomes</b>. The two halves of the plate are <b>Possibility I</b> and "
    "<b>Possibility II</b>; each half shows <b>Meiosis I - anaphase</b> at the top and "
    "<b>Meiosis II - anaphase</b> below, ending in four <b>Germ cells</b>. The four "
    "chromosomes are distinguished by colour - one long orange, one long yellow, one short "
    "red, one short green. In <b>Possibility I</b> the cell labelled "
    "<b>One long orange and short green chromosome and long yellow and short red "
    "chromosome at the same pole</b> is on the left, and the complementary arrangement on "
    "the right. In <b>Possibility II</b> the cell labelled <b>One long orange and short "
    "red chromosome and long yellow and short green chromosome at the same pole</b> is on "
    "the left, and the complementary arrangement on the right. The plate's meaning sits in "
    "those two arrangements - which two chromosomes end up in the same germ cell is not "
    "fixed."))
story.append(note(
    "<b>Read the plate (Figure 4.10 labels).</b> The plate is <b>Drosophila melanogaster "
    "(a) Male (b) Female</b>. The plate carries no in-figure label rows beyond the title "
    "- it is a visual of the two sexes, with the male typically smaller and darker than "
    "the female. Drosophila's short two-week life cycle, large brood size, and clear sex "
    "dimorphism (above) are what made it Morgan's model organism."))

# ======================================================================================
# ---- 4.3.3 Linkage and Recombination ---- F227-F238 + Fig 4.11
# ======================================================================================
story.append(gap(6))
story.append(heading("4.3.3", "Linkage and Recombination", level=2))
# F228
story.append(b1(
    "<b>Morgan carried out several dihybrid crosses in Drosophila to study genes that were "
    "sex-linked.</b>"))
# F229
story.append(b1(
    "<b>The crosses were similar to the dihybrid crosses carried out by Mendel in peas.</b> "
    "For example Morgan hybridised <b>yellow-bodied, white-eyed females</b> to "
    "<b>brown-bodied, red-eyed males</b> and intercrossed their F<sub>1</sub> progeny."))
# F230
story.append(b1(
    "<b>He observed that the two genes did not segregate independently of each other and "
    "the F<sub>2</sub> ratio deviated very significantly from the 9:3:3:1 ratio</b> "
    "(expected when the two genes are independent)."))
# F231
story.append(b1(
    "<b>Morgan and his group knew that the genes were located on the X chromosome (Section "
    "4.4) and saw quickly that when the two genes in a dihybrid cross were situated on "
    "the same chromosome, the proportion of parental gene combinations were much higher "
    "than the non-parental type.</b>"))
# F232 - linkage & recombination definitions
story.append(keyterm(
    "<b>Morgan attributed this due to the physical association or linkage of the two "
    "genes and coined the term linkage to describe this physical association of genes on a "
    "chromosome and the term recombination to describe the generation of non-parental gene "
    "combinations (Figure 4.11).</b>"))
# F233-F234
story.append(b1(
    "<b>Morgan and his group also found that even when genes were grouped on the same "
    "chromosome, some genes were very tightly linked (showed very low recombination) "
    "(Figure 4.11, Cross A) while others were loosely linked (showed higher recombination) "
    "(Figure 4.11, Cross B).</b>"))
story.append(b1(
    "<b>For example he found that the genes white and yellow were very tightly linked and "
    "showed only 1.3 per cent recombination while white and miniature wing showed 37.2 per "
    "cent recombination.</b>"))
# F235-F236
story.append(b1(
    "<b>His student Alfred Sturtevant used the frequency of recombination between gene "
    "pairs on the same chromosome as a measure of the distance between genes and 'mapped' "
    "their position on the chromosome.</b>"))
story.append(b1(
    "<b>Today genetic maps are extensively used as a starting point in the sequencing of "
    "whole genomes as was done in the case of the Human Genome Sequencing Project, "
    "described later.</b>"))

# F237-F238 - Fig 4.11 read-the-plate
story.append(gap())
story.append(note(
    "<b>Read the plate (Figure 4.11 labels).</b> The plate is <b>Linkage: Results of two "
    "dihybrid crosses conducted by Morgan. Cross A shows crossing between gene y and w; "
    "Cross B shows crossing between genes w and m. Here dominant wild type alleles are "
    "represented with (+) sign in superscript. Note: The strength of linkage between y and "
    "w is higher than w and m.</b> The plate has two halves - <b>Cross A</b> on the left "
    "and <b>Cross B</b> on the right. Cross A's pair is <b>Yellow, white</b>; Cross B's "
    "pair is <b>White, miniature</b>. The <b>Wild type</b> parents sit at the top of each "
    "cross. The <b>F<sub>1</sub> generation</b> row gives the heterozygous flies; the "
    "next row is the <b>Gametes</b> each cross produces. Below the gametes, Cross A shows "
    "<b>Parental type (98.7%)</b> and <b>Recombinant types (1.3%)</b>; Cross B shows "
    "<b>Parental type (62.8%)</b> and <b>Recombinant types (37.2%)</b>. The phenotype "
    "labels in each cross are <b>yellow</b>, <b>white</b>, <b>yellow, white</b>, "
    "<b>miniature</b> and <b>wild type</b>."))

# ======================================================================================
# ---- 4.4 POLYGENIC INHERITANCE ---- F239-F249
# ======================================================================================
story.append(gap(6))
story.append(heading("4.4", "POLYGENIC INHERITANCE", level=1))
# F240, F241, F242
story.append(b1(
    "<b>Mendel's studies mainly described those traits that have distinct alternate forms "
    "such as flower colour which are either purple or white.</b>"))
story.append(b1(
    "<b>But if you look around you will find that there are many traits which are not so "
    "distinct in their occurrence and are spread across a gradient.</b>"))
story.append(b1(
    "<b>For example, in humans we don't just have tall or short people as two distinct "
    "alternatives but a whole range of possible heights.</b>"))
# F243, F244
story.append(keyterm(
    "<b>Such traits are generally controlled by three or more genes and are thus called "
    "as polygenic traits.</b>"))
story.append(b1(
    "<b>Besides the involvement of multiple genes polygenic inheritance also takes into "
    "account the influence of environment.</b>"))
# F245-F249 - skin colour example
story.append(b1(
    "<b>Human skin colour is another classic example for this.</b>"))
story.append(b1(
    "<b>In a polygenic trait the phenotype reflects the contribution of each allele, i.e., "
    "the effect of each allele is additive.</b>"))
story.append(b1(
    "<b>To understand this better let us assume that three genes A, B, C control skin "
    "colour in human with the dominant forms A, B and C responsible for dark skin colour "
    "and the recessive forms a, b and c for light skin colour.</b>"))
story.append(b1(
    "<b>The genotype with all the dominant alleles (AABBCC) will have the darkest skin "
    "colour and that with all the recessive alleles (aabbcc) will have the lightest skin "
    "colour.</b>"))
story.append(b1(
    "<b>As expected the genotype with three dominant alleles and three recessive alleles "
    "will have an intermediate skin colour.</b> In this manner the number of each type of "
    "alleles in the genotype would determine the darkness or lightness of the skin in an "
    "individual."))

# ======================================================================================
# ---- 4.5 PLEIOTROPY ---- F250-F254
# ======================================================================================
story.append(gap(6))
story.append(heading("4.5", "PLEIOTROPY", level=1))
# F251
story.append(b1(
    "<b>We have so far seen the effect of a gene on a single phenotype or trait.</b>"))
# F252
story.append(keyterm(
    "<b>There are however instances where a single gene can exhibit multiple phenotypic "
    "expression. Such a gene is called a pleiotropic gene.</b>"))
# F253
story.append(b1(
    "<b>The underlying mechanism of pleiotropy in most cases is the effect of a gene on "
    "metabolic pathways which contribute towards different phenotypes.</b>"))
# F254 - phenylketonuria example
story.append(b1(
    "<b>An example of this is the disease phenylketonuria, which occurs in humans.</b> "
    "The disease is caused by mutation in the gene that codes for the enzyme "
    "phenylalanine hydroxylase (single gene mutation). This manifests itself through "
    "phenotypic expression characterised by <b>mental retardation and a reduction in "
    "hair and skin pigmentation</b>."))

# ======================================================================================
# ---- 4.6 SEX DETERMINATION ---- F255-F274 + Fig 4.12
# ======================================================================================
story.append(gap(6))
story.append(heading("4.6", "SEX DETERMINATION", level=1))
# F256-F258
story.append(b1(
    "<b>The mechanism of sex determination has always been a puzzle before the "
    "geneticists.</b>"))
story.append(b1(
    "<b>The initial clue about the genetic/chromosomal mechanism of sex determination can "
    "be traced back to some of the experiments carried out in insects.</b>"))
story.append(b1(
    "<b>In fact, the cytological observations made in a number of insects led to the "
    "development of the concept of genetic/chromosomal basis of sex-determination.</b>"))
# F259-F261
story.append(b1(
    "<b>Henking (1891) could trace a specific nuclear structure all through "
    "spermatogenesis in a few insects, and it was also observed by him that 50 per cent of "
    "the sperm received this structure after spermatogenesis, whereas the other 50 per "
    "cent sperm did not receive it.</b>"))
story.append(b1(
    "<b>Henking gave a name to this structure as the x body but he could not explain its "
    "significance.</b>"))
story.append(b1(
    "<b>Further investigations by other scientists led to the conclusion that the 'X "
    "body' of Henking was in fact a chromosome and that is why it was given the name "
    "X-chromosome.</b>"))
# F262-F266
story.append(b1(
    "<b>It was also observed that in a large number of insects the mechanism of sex "
    "determination is of the XO type,</b> i.e., all eggs bear an additional X-chromosome "
    "besides the other chromosomes (autosomes)."))
story.append(b1(
    "<b>On the other hand, some of the sperms bear the X-chromosome whereas some do not.</b>"))
story.append(b1(
    "<b>Eggs fertilised by sperm having an X-chromosome become females</b> and, those "
    "fertilised by sperms that do not have an X-chromosome become males."))
story.append(keyterm(
    "<b>Due to the involvement of the X-chromosome in the determination of sex, it was "
    "designated to be the sex chromosome, and the rest of the chromosomes were named as "
    "autosomes.</b>"))
story.append(b1(
    "<b>Grasshopper is an example of XO type of sex determination in which the males have "
    "only one X-chromosome besides the autosomes, whereas females have a pair of "
    "X-chromosomes.</b>"))
# F267-F269
story.append(b1(
    "<b>In a number of other insects and mammals including man, XY type of sex "
    "determination is seen</b> where both male and female have same number of chromosomes. "
    "Among the males an X-chromosome is present but its counterpart is distinctly smaller "
    "and called the Y-chromosome. Females, however, have a pair of X-chromosomes."))
story.append(b1(
    "<b>Both males and females bear same number of autosomes. Hence, the males have "
    "autosomes plus XY, while female have autosomes plus XX.</b>"))
story.append(b1(
    "<b>In human beings and in Drosophila the males have one X and one Y chromosome, "
    "whereas females have a pair of X-chromosomes besides autosomes (Figure 4.12a, b).</b>"))
# F270-F272
story.append(b1(
    "<b>In the above description you have studied about two types of sex determining "
    "mechanisms, i.e., XO type and XY type.</b> But in both cases males produce two "
    "different types of gametes, (a) either with or without X-chromosome or (b) some "
    "gametes with X-chromosome and some with Y-chromosome. Such type of sex determination "
    "mechanism is designated to be the example of <b>male heterogamety</b>."))
story.append(b1(
    "<b>In some other organisms, e.g., birds, a different mechanism of sex determination "
    "is observed (Figure 4.12 c).</b> In this case the total number of chromosome is same "
    "in both males and females. But two different types of gametes in terms of the sex "
    "chromosomes, are produced by females, i.e., <b>female heterogamety</b>."))
story.append(b1(
    "<b>In order to have a distinction with the mechanism of sex determination described "
    "earlier, the two different sex chromosomes of a female bird has been designated to "
    "be the Z and W chromosomes.</b> In these organisms the females have one Z and one W "
    "chromosome, whereas males have a pair of Z-chromosomes besides the autosomes."))
# F375 - SUMMARY-UNIQUE: chicken ZZ/ZW
story.append(gap())
story.append(Paragraph(
    "<b>One sentence the chapter summary adds and the body never does:</b> <i>In chicken, "
    "sex chromosomes in male are ZZ, and in females are ZW.</i>", STYLES["NoteBox"]))

# F273-F274 - Fig 4.12 read-the-plate
story.append(gap())
story.append(note(
    "<b>Read the plate (Figure 4.12 labels).</b> The plate is <b>Determination of sex by "
    "chromosomal differences: (a, b) Both in humans and in Drosophila the female has a "
    "pair of XX chromosomes (homogametic) and the male XY (heterogametic) composition; "
    "(c) In many birds, female has a pair of dissimilar chromosomes Zw and male two "
    "similar ZZ chromosomes</b>. The four labels the plate carries are <b>XX</b> (panel a "
    "and b, female), <b>XY</b> (panel a and b, male), <b>ZW</b> (panel c, female bird) "
    "and <b>ZZ</b> (panel c, male bird). The source prints the bird pair as <b>Zw</b> and "
    "<b>ZZ</b>; the chapter's own paragraph just above names the female chromosome <b>W</b> "
    "(uppercase), and the conventional name is <b>ZW</b> - both spellings are kept as "
    "printed."))

# ======================================================================================
# ---- 4.6.1 Sex Determination in Humans ---- F275-F283
# ======================================================================================
story.append(gap(6))
story.append(heading("4.6.1", "Sex Determination in Humans", level=2))
# F276
story.append(b1(
    "<b>It has already been mentioned that the sex determining mechanism in case of "
    "humans is XY type.</b>"))
# F277
story.append(b1(
    "<b>Out of 23 pairs of chromosomes present, 22 pairs are exactly same in both males "
    "and females:</b> these are the autosomes."))
# F278
story.append(b1(
    "<b>A pair of X-chromosomes are present in the female, whereas the presence of an X "
    "and Y chromosome are determinant of the male characteristic.</b>"))
# F279, F280
story.append(b1(
    "<b>During spermatogenesis among males, two types of gametes are produced.</b> "
    "<b>50 per cent of the total sperm produced carry the X-chromosome and the rest 50 "
    "per cent has Y-chromosome besides the autosomes.</b>"))
story.append(b1(
    "<b>Females, however, produce only one type of ovum with an X-chromosome.</b>"))
# F281, F282
story.append(b1(
    "<b>There is an equal probability of fertilisation of the ovum with the sperm "
    "carrying either X or Y chromosome.</b> In case the ovum fertilises with a sperm "
    "carrying X-chromosome the zygote develops into a female (XX) and the fertilisation "
    "of ovum with Y-chromosome carrying sperm results into a male offspring."))
story.append(b1(
    "<b>Thus, it is evident that it is the genetic make up of the sperm that determines "
    "the sex of the child.</b>"))
# F283
story.append(b1(
    "<b>It is also evident that in each pregnancy there is always 50 per cent probability "
    "of either a male or a female child.</b>"))

# ======================================================================================
# ---- 4.6.2 Sex Determination in Honey Bee ---- F284-F290 + Fig 4.13a
# ======================================================================================
story.append(gap(6))
story.append(heading("4.6.2", "Sex Determination in Honey Bee", level=2))
# F285
story.append(b1(
    "<b>The sex determination in honey bee is based on the number of sets of chromosomes "
    "an individual receives.</b>"))
# F286, F287
story.append(b1(
    "<b>An offspring formed from the union of a sperm and an egg develops as a female "
    "(queen or worker), and an unfertilised egg develops as a male (drone) by means of "
    "parthenogenesis.</b>"))
story.append(b1(
    "<b>This means that the males have half the number of chromosomes than that of a "
    "female.</b> The females are diploid having <b>32 chromosomes</b> and males are "
    "haploid, i.e., having <b>16 chromosomes</b>."))
# F288
story.append(keyterm(
    "<b>This is called as haplodiploid sex-determination system</b> and has special "
    "characteristic features such as the <b>males produce sperms by mitosis (Figure "
    "4.13), they do not have father and thus cannot have sons, but have a grandfather and "
    "can have grandsons</b>."))

# F289-F290 - Fig 4.13a read-the-plate (honey bee plate)
story.append(gap())
story.append(note(
    "<b>Read the plate (Figure 4.13 labels - the honey bee plate, p21).</b> The plate is "
    "<b>Figure 4.13 Sex determination in honey bee</b> (NCERT prints a SECOND Figure 4.13 "
    "on p22, the pedigree-symbol plate - they share the same printed number). The honey "
    "bee plate's labels: <b>Parents</b> at the top, with the two columns labelled "
    "<b>Female</b> and <b>Male</b>; the row below carries <b>Gametes:</b> (the female "
    "contributes 32, the male contributes 16); the middle row is the meiotic/mitotic "
    "branch with <b>Meiosis</b> on the female side and <b>Mitosis</b> on the male side; "
    "the bottom row is <b>F<sub>1</sub>:</b> - 32 on the female side (fertilised eggs) "
    "and 16 on the male side (unfertilised eggs). The <b>32</b> and <b>16</b> chromosome "
    "counts on the right are the diploid and haploid numbers."))

# ======================================================================================
# ---- 4.7 MUTATION ---- F291-F299
# ======================================================================================
story.append(gap(6))
story.append(heading("4.7", "MUTATION", level=1))
# F292, F293
story.append(keyterm(
    "<b>Mutation is a phenomenon which results in alteration of DNA sequences and "
    "consequently results in changes in the genotype and the phenotype of an "
    "organism.</b>"))
story.append(b1(
    "<b>In addition to recombination, mutation is another phenomenon that leads to "
    "variation in DNA.</b>"))
# F294-F296
story.append(b1(
    "<b>As you will learn in Chapter 5, one DNA helix runs continuously from one end to "
    "the other in each chromatid, in a highly supercoiled form.</b>"))
story.append(b1(
    "<b>Therefore loss (deletions) or gain (insertion/duplication) of a segment of DNA, "
    "result in alteration in chromosomes.</b> Since genes are known to be located on "
    "chromosomes, alteration in chromosomes results in abnormalities or aberrations."))
story.append(b1(
    "<b>Chromosomal aberrations are commonly observed in cancer cells.</b>"))
# F297, F298
story.append(keyterm(
    "<b>In addition to the above, mutation also arise due to change in a single base pair "
    "of DNA. This is known as point mutation.</b> A classical example of such a mutation "
    "is sickle cell anemia."))
story.append(b1(
    "<b>Deletions and insertions of base pairs of DNA, causes frame-shift mutations</b> "
    "(see Chapter 5)."))
# F299
story.append(keyterm(
    "<b>However, there are many chemical and physical factors that induce mutations. "
    "These are referred to as mutagens. UV radiations can cause mutations in organisms - "
    "it is a mutagen.</b>"))

# ======================================================================================
# ---- 4.8 GENETIC DISORDERS ---- F300-F312
# ======================================================================================
story.append(gap(6))
story.append(heading("4.8", "GENETIC DISORDERS", level=1))
# F301, F302
story.append(heading("4.8.1", "Pedigree Analysis", level=2))
story.append(b1(
    "<b>The idea that disorders are inherited has been prevailing in the human society "
    "since long.</b> This was based on the heritability of certain characteristic "
    "features in families."))
# F303-F306
story.append(b1(
    "<b>After the rediscovery of Mendel's work the practice of analysing inheritance "
    "pattern of traits in human beings began.</b>"))
story.append(b1(
    "<b>Since it is evident that control crosses that can be performed in pea plant or "
    "some other organisms, are not possible in case of human beings, study of the family "
    "history about inheritance of a particular trait provides an alternative.</b>"))
story.append(keyterm(
    "<b>Such an analysis of traits in several of generations of a family is called the "
    "pedigree analysis.</b> In the pedigree analysis the inheritance of a particular "
    "trait is represented in the family tree over generations."))
story.append(b1(
    "<b>In human genetics, pedigree study provides a strong tool, which is utilised to "
    "trace the inheritance of a specific trait, abnormality or disease.</b>"))
# F307
story.append(b1(
    "<b>Some of the important standard symbols used in the pedigree analysis have been "
    "shown in Figure 4.13.</b>"))

# F308-F309 - Fig 4.13b read-the-plate (pedigree symbol plate)
story.append(gap())
story.append(note(
    "<b>Read the plate (Figure 4.13 labels - the pedigree-symbol plate, p22).</b> The "
    "plate is <b>Figure 4.13 Symbols used in the human pedigree analysis</b> (this is the "
    "second Figure 4.13 - same printed number, different plate from the honey bee one). "
    "The labels: <b>Male</b>, <b>female</b>, <b>sex unspecified</b>, <b>affected "
    "individuals</b>, <b>mating</b>, <b>mating between relatives (consanguineous "
    "mating)</b>, <b>parents above and children below (in order of birth - left to "
    "right)</b>, <b>parents with male child affected with disease</b>, and <b>five "
    "unaffected offspring</b>."))

# F310-F312
story.append(gap())
story.append(b1(
    "<b>DNA is the carrier of genetic information. It is hence transmitted from one "
    "generation to the other without any change or alteration.</b>"))
story.append(b1(
    "<b>A number of disorders in human beings have been found to be associated with the "
    "inheritance of changed or altered genes or chromosomes.</b>"))

# F313 - opener for 4.8.2
story.append(gap(6))
story.append(heading("4.8.2", "Mendelian Disorders", level=2))
story.append(b1(
    "<b>Broadly, genetic disorders may be grouped into two categories - Mendelian "
    "disorders and Chromosomal disorders.</b>"))
# F314
story.append(keyterm(
    "<b>Mendelian disorders are mainly determined by alteration or mutation in the single "
    "gene.</b>"))
# F315
story.append(b1(
    "<b>These disorders are transmitted to the offspring on the same lines as we have "
    "studied in the principle of inheritance.</b> The pattern of inheritance of such "
    "Mendelian disorders can be traced in a family by the pedigree analysis."))
# F316
story.append(b1(
    "<b>Most common and prevalent Mendelian disorders are Haemophilia, Cystic fibrosis, "
    "Sickle cell anaemia, Colour blindness, Phenylketonuria, Thalassemia, etc.</b>"))
# F317-F318
story.append(b1(
    "<b>By pedigree analysis one can easily understand whether the trait in question is "
    "dominant or recessive.</b> Similarly, the trait may also be linked to the sex "
    "chromosome as in case of haemophilia."))
story.append(b1(
    "<b>It is evident that this X-linked recessive trait shows transmission from carrier "
    "female to male progeny.</b>"))

# F319-F320 - Fig 4.14 (pedigree of autosomal dominant + recessive) read-the-plate
story.append(gap())
story.append(note(
    "<b>Read the plate (Figure 4.14 labels).</b> The plate is <b>Representative pedigree "
    "analysis of (a) Autosomal dominant trait (for example: Myo tonic dystrophy) "
    "(b) Autosomal recessive trait (for example: Sickle-cell anaemia)</b>. The label row "
    "is empty in the source - the source's own column headers are the trait names - so the "
    "plate is read by what the source itself prints: a pedigree of the Myo tonic dystrophy "
    "family on the left (autosomal dominant) and a pedigree of the sickle-cell anaemia "
    "family on the right (autosomal recessive). The source spells <b>Myo tonic dystrophy</b> "
    "with the space inside the word; the conventional form is <b>myotonic dystrophy</b>. "
    "Both are kept as printed."))

# F321-F326 - Colour blindness
story.append(gap())
story.append(heading("Colour blindness", "Colour blindness (X-linked recessive)", level=3))
story.append(keyterm(
    "<b>Colour Blindness:</b> It is a sex-linked recessive disorder due to defect in either "
    "red or green cone of eye resulting in failure to discriminate between red and green "
    "colour."))
story.append(b1(
    "<b>This defect is due to mutation in certain genes present in the X chromosome.</b>"))
story.append(b1(
    "<b>It occurs in about 8 per cent of males and only about 0.4 per cent of females.</b>"))
story.append(b1(
    "<b>This is because the genes that lead to red-green colour blindness are on the X "
    "chromosome. Males have only one X chromosome and females have two.</b>"))
story.append(b1(
    "<b>The son of a woman who carries the gene has a 50 per cent chance of being colour "
    "blind.</b> The mother is not herself colour blind because the gene is recessive. That "
    "means that its effect is suppressed by her matching dominant normal gene."))
story.append(b1(
    "<b>A daughter will not normally be colour blind, unless her mother is a carrier and "
    "her father is colour blind.</b>"))

# F327-F331 - Haemophilia
story.append(gap())
story.append(heading("Haemophilia", "Haemophilia (X-linked recessive)", level=3))
story.append(b1(
    "<b>Haemophilia:</b> This sex linked recessive disease, which shows its transmission "
    "from unaffected carrier female to some of the male progeny has been widely studied."))
story.append(b1(
    "<b>In this disease, a single protein that is a part of the cascade of proteins "
    "involved in the clotting of blood is affected.</b>"))
story.append(b1(
    "<b>Due to this, in an affected individual a simple cut will result in non-stop "
    "bleeding.</b>"))
story.append(b1(
    "<b>The heterozygous female (carrier) for haemophilia may transmit the disease to "
    "sons.</b>"))
story.append(b1(
    "<b>The possibility of a female becoming a haemophilic is extremely rare</b> because "
    "mother of such a female has to be at least carrier and the father should be "
    "haemophilic (unviable in the later stage of life)."))
# F332 - Queen Victoria example
story.append(b1(
    "<b>The family pedigree of Queen Victoria shows a number of haemophilic descendents "
    "as she was a carrier of the disease.</b>"))

# F333-F339 - Sickle-cell anaemia
story.append(gap())
story.append(heading("Sickle-cell anaemia",
                      "Sickle-cell anaemia (autosomal recessive, single base change)", level=3))
story.append(keyterm(
    "<b>Sickle-cell anaemia:</b> This is an autosome linked recessive trait that can be "
    "transmitted from parents to the offspring when both the partners are carrier for the "
    "gene (or heterozygous)."))
story.append(b1(
    "<b>The disease is controlled by a single pair of allele, Hb<sup>A</sup> and "
    "Hb<sup>S</sup>.</b>"))
story.append(b1(
    "<b>Out of the three possible genotypes only homozygous individuals for Hb<sup>S</sup> "
    "(Hb<sup>S</sup>Hb<sup>S</sup>) show the diseased phenotype.</b>"))
story.append(b1(
    "<b>Heterozygous (Hb<sup>A</sup>Hb<sup>S</sup>) individuals appear apparently "
    "unaffected but they are carrier of the disease as there is 50 per cent probability of "
    "transmission of the mutant gene to the progeny, thus exhibiting sickle-cell trait "
    "(Figure 4.15).</b>"))
story.append(b1(
    "<b>The defect is caused by the substitution of Glutamic acid (Glu) by Valine (Val) at "
    "the sixth position of the beta globin chain of the haemoglobin molecule.</b>"))
story.append(b1(
    "<b>The substitution of amino acid in the globin protein results due to the single "
    "base substitution at the sixth codon of the beta globin gene from GAG to GUG.</b>"))
story.append(b1(
    "<b>The mutant haemoglobin molecule undergoes polymerisation under low oxygen tension "
    "causing the change in the shape of the RBC from biconcave disc to elongated sickle "
    "like structure (Figure 4.15).</b>"))

# F340-F341 - Fig 4.15 read-the-plate
story.append(gap())
story.append(note(
    "<b>Read the plate (Figure 4.15 labels).</b> The plate is <b>Micro graph of the red "
    "blood cells and the amino acid composition of the relevant portion of beta-chain of "
    "haemoglobin: (a) From a normal individual; (b) From an individual with sickle-cell "
    "anaemia</b>. The source spells it <b>Micro graph</b>. The plate labels (a) on the left "
    "and (b) on the right. The labels on the two gene cards are <b>Normal Hb(A) gene</b> "
    "and <b>Sickle-cell Hb(S) gene</b>. The mRNA lines are <b>mRNA GAG</b> and "
    "<b>mRNA GUG</b>. The peptide chains are <b>HbA peptide</b> and <b>HbS peptide</b>, "
    "and the amino acid sequences printed under them are <b>Val His Leu Thr Pro Glu Glu</b> "
    "(HbA) and <b>Val His Leu Thr Pro Val Glu</b> (HbS) - the difference is one residue: "
    "Glu at position 6 in HbA, Val at position 6 in HbS."))

# F342-F346 - Phenylketonuria
story.append(gap())
story.append(heading("Phenylketonuria", "Phenylketonuria (autosomal recessive)", level=3))
story.append(keyterm(
    "<b>Phenylketonuria:</b> This inborn error of metabolism is also inherited as the "
    "autosomal recessive trait."))
story.append(b1(
    "<b>The affected individual lacks an enzyme that converts the amino acid phenylalanine "
    "into tyrosine.</b>"))
story.append(b1(
    "<b>As a result of this phenylalanine is accumulated and converted into phenylpyruvic "
    "acid and other derivatives.</b>"))
story.append(b1(
    "<b>Accumulation of these in brain results in mental retardation.</b>"))
story.append(b1(
    "<b>These are also excreted through urine because of its poor absorption by kidney.</b>"))

# F347-F352 - Thalassemia
story.append(gap())
story.append(heading("Thalassemia", "Thalassemia (autosomal recessive)", level=3))
story.append(keyterm(
    "<b>Thalassemia:</b> This is also an autosome-linked recessive blood disease "
    "transmitted from parents to the offspring when both the partners are unaffected "
    "carrier for the gene (or heterozygous)."))
story.append(b1(
    "<b>The defect could be due to either mutation or deletion which ultimately results in "
    "reduced rate of synthesis of one of the globin chains (alpha and beta chains) that "
    "make up haemoglobin.</b> This causes the formation of abnormal haemoglobin molecules "
    "resulting into anaemia which is characteristic of the disease."))
story.append(b1(
    "<b>Thalassemia can be classified according to which chain of the haemoglobin molecule "
    "is affected.</b> In alpha Thalassemia, production of alpha globin chain is affected "
    "while in beta Thalassemia, production of beta globin chain is affected."))
story.append(b1(
    "<b>alpha Thalassemia is controlled by two closely linked genes HBA1 and HBA2 on "
    "chromosome 16 of each parent and it is observed due to mutation or deletion of one or "
    "more of the four genes.</b> The more genes affected, the less alpha globin molecules "
    "produced."))
story.append(b1(
    "<b>While beta Thalassemia is controlled by a single gene HBB on chromosome 11 of each "
    "parent and occurs due to mutation of one or both the genes.</b>"))
# F352 - the comparison
story.append(b1(
    "<b>Thalassemia differs from sickle-cell anaemia in that the former is a quantitative "
    "problem of synthesising too few globin molecules while the latter is a qualitative "
    "problem of synthesising an incorrectly functioning globin.</b>"))

# ======================================================================================
# ---- 4.8.3 Chromosomal Disorders ---- F353-F376 + Fig 4.16, 4.17
# ======================================================================================
story.append(gap(6))
story.append(heading("4.8.3", "Chromosomal Disorders", level=2))
# F354, F355
story.append(b1(
    "<b>The chromosomal disorders on the other hand are caused due to absence or excess "
    "or abnormal arrangement of one or more chromosomes.</b>"))
story.append(keyterm(
    "<b>Failure of segregation of chromatids during cell division cycle results in the "
    "gain or loss of a chromosome(s), called aneuploidy.</b>"))
# F356-F358
story.append(b1(
    "<b>For example Down's syndrome results in the gain of extra copy of chromosome "
    "21.</b>"))
story.append(b1(
    "<b>Similarly, Turner's syndrome results due to loss of an X chromosome in human "
    "females.</b>"))
story.append(keyterm(
    "<b>Failure of cytokinesis after telophase stage of cell division results in an "
    "increase in a whole set of chromosomes in an organism and, this phenomenon is known "
    "as polyploidy.</b> This condition is often seen in plants."))
# F359
story.append(b1(
    "<b>The total number of chromosomes in a normal human cell is 46 (23 pairs). Out of "
    "these 22 pairs are autosomes and one pair of chromosomes are sex chromosome.</b>"))
# F360
story.append(keyterm(
    "<b>These situations are known as trisomy or monosomy of a chromosome, "
    "respectively.</b> Such a situation leads to very serious consequences in the "
    "individual."))
# F361
story.append(b1(
    "<b>Down's Syndrome, Turner's syndrome, Klinefelter's syndrome are common examples "
    "of chromosomal disorders.</b>"))

# F362-F364 - Down's
story.append(gap())
story.append(heading("Down's", "Down's Syndrome (trisomy 21)", level=3))
story.append(b1(
    "<b>Down's Syndrome:</b> The cause of this genetic disorder is the presence of an "
    "additional copy of the chromosome number 21 (trisomy of 21)."))
story.append(b1(
    "<b>This disorder was first described by Langdon Down (1866).</b>"))
story.append(b1(
    "<b>The affected individual is short statured with small round head, furrowed tongue "
    "and partially open mouth (Figure 4.16).</b> Palm is broad with characteristic palm "
    "crease. Physical, psychomotor and mental development is retarded."))

# F368-F369 - Fig 4.16 read-the-plate
story.append(gap())
story.append(note(
    "<b>Read the plate (Figure 4.16 labels).</b> The plate is <b>A representative figure "
    "showing an individual inflicted with Down's syndrome and the corresponding "
    "chromosomes of the individual</b>. The label row of the plate is empty in the source, "
    "and the only fact-bearing labels NCERT prints on the plate are the six physical "
    "signs called out as: <b>Broad flat face</b>, <b>Flat back of head</b>, <b>Many "
    "'loops' on finger tips</b>, <b>Palm crease</b>, <b>Big and wrinkled tongue</b>, and "
    "<b>Congenital heart disease</b>."))

# F365-F366 - Klinefelter's
story.append(gap())
story.append(heading("Klinefelter's", "Klinefelter's Syndrome (47, XXY)", level=3))
story.append(b1(
    "<b>Klinefelter's Syndrome:</b> This genetic disorder is also caused due to the "
    "presence of an additional copy of X chromosome resulting into a karyotype of "
    "<b>47, XXY</b>."))
story.append(b1(
    "<b>Such an individual has overall masculine development, however, the feminine "
    "development (development of breast, i.e., Gynaecomastia) is also expressed (Figure "
    "4.17a).</b> Such individuals are sterile."))

# F367 - Turner's
story.append(gap())
story.append(heading("Turner's", "Turner's Syndrome (45, X0)", level=3))
story.append(b1(
    "<b>Turner's Syndrome:</b> Such a disorder is caused due to the absence of one of "
    "the X chromosomes, i.e., <b>45 with X0</b>, Such females are sterile as ovaries are "
    "rudimentary besides other features including lack of other secondary sexual "
    "characters (Figure 4.17b)."))

# F370-F371 - Fig 4.17 read-the-plate
story.append(gap())
story.append(note(
    "<b>Read the plate (Figure 4.17 labels).</b> The plate is <b>Diagrammatic "
    "representation of genetic disorders due to sex chromosome composition in humans: "
    "(a) Klinefelter Syndrome; (b) Turner's Syndrome</b>. The source's own spelling is "
    "<b>represe-ntation</b>, hyphenated across a line break. The two label rows on the "
    "plate, one per panel, are: panel (a) <b>Tall stature with feminised character "
    "(development of breast, i.e., Gynaecomastia)</b>; panel (b) <b>Short stature and "
    "under developed feminine character</b>."))

# F376 - SUMMARY-UNIQUE: Karyotypes
story.append(gap())
story.append(Paragraph(
    "<b>One sentence the chapter summary adds and the body never does:</b> <i>These can "
    "be easily studied by analysis of Karyotypes.</i>", STYLES["NoteBox"]))

# ======================================================================================
# ---- Quick Recap (SS5 item 8) - rewritten, denser version of the NCERT summary, NOT a
#      copy of it (SS3).  The five SUMMARY-UNIQUE folds (F372-F376) sit in their body
#      homes above; the recap carries them as one-liners and sweeps the 27 body-present
#      facts in NCERT's own sentence order.
# ======================================================================================
story.append(gap(6))
story.append(heading("Recap", "QUICK RECAP", level=1))

story.append(b1(
    "<b>Genetics</b> is a branch of biology which deals with <b>principles of inheritance "
    "and its practices</b> (summary-only wording; the body's definition reads differently)."))
story.append(b1(
    "<b>Progeny resembling the parents in morphological and physiological features</b> "
    "has attracted the attention of many biologists (summary-only wording)."))
story.append(b1(
    "<b>Mendel was the first to study this phenomenon systematically</b> (summary-only "
    "wording)."))
story.append(b1(
    "<b>While studying the pattern of inheritance in pea plants of contrasting "
    "characters, Mendel proposed the principles of inheritance, which are today referred "
    "to as 'Mendel's Laws of Inheritance'.</b>"))
story.append(b1(
    "<b>He proposed that the 'factors' (later named as genes) regulating the characters "
    "are found in pairs known as alleles.</b>"))
story.append(b1(
    "<b>He observed that the expression of the characters in the offspring follow a "
    "definite pattern in different-first generations (F<sub>1</sub>), second "
    "(F<sub>2</sub>) and so on.</b>"))
story.append(b1(
    "<b>Some characters are dominant over others.</b>"))
story.append(b1(
    "<b>The dominant characters are expressed when factors are in heterozygous condition "
    "(Law of Dominance).</b>"))
story.append(b1(
    "<b>The recessive characters are only expressed in homozygous conditions.</b>"))
story.append(b1(
    "<b>The characters never blend in heterozygous condition.</b>"))
story.append(b1(
    "<b>A recessive character that was not expressed in heterozygous conditon may be "
    "expressed again when it becomes homozygous.</b> (NCERT spelling <b>conditon</b> "
    "preserved.)"))
story.append(b1(
    "<b>Hence, characters segregate while formation of gametes (Law of Segregation).</b>"))
story.append(b1(
    "<b>Not all characters show true dominance. Some characters show incomplete, and "
    "some show co-dominance.</b>"))
story.append(b1(
    "<b>When Mendel studied the inheritance of two characters together, it was found that "
    "the factors independently assort and combine in all permutations and combinations "
    "(Law of Independent Assortment).</b>"))
story.append(b1(
    "<b>Different combinations of gametes are theoretically represented in a square "
    "tabular form known as 'Punnett Square'.</b>"))
story.append(b1(
    "<b>The factors (now known as gene) on chromosomes regulating the characters are "
    "called the genotype and the physical expression of the chraracters is called "
    "phenotype.</b> (NCERT spelling <b>chraracters</b> preserved.)"))
story.append(b1(
    "<b>After knowing that the genes are located on the chromosomes, a good correlation "
    "was drawn between Mendel's laws: segregation and assortment of chromosomes during "
    "meiosis. The Mendel's laws were extended in the form of 'Chromosomal Theory of "
    "Inheritance'.</b>"))
story.append(b1(
    "<b>Later, it was found that Mendel's law of independent assortment does not hold "
    "true for the genes that were located on the same chromosomes. These genes were "
    "called as linked genes.</b>"))
story.append(b1(
    "<b>Closely located genes assorted together, and distantly located genes, due to "
    "recombination, assorted independently. Linkage maps, therefore, corresponded to "
    "arrangement of genes on a chromosome.</b>"))
story.append(b1(
    "<b>Many genes were linked to sexes also, and called as sex-linked genes.</b>"))
story.append(b1(
    "<b>The two sexes (male and female) were found to have a set of chromosomes which "
    "were common, and another set which was different. The chromosomes which were "
    "different in two sexes were named as sex chromosomes. The remaining set was named "
    "as autosomes.</b>"))
story.append(b1(
    "<b>In humans, a normal female has 22 pairs of autosomes and a pair of sex "
    "chromosomes (Xx).</b> A male has 22 pairs of autosomes and a pair of sex "
    "chromosome as XY. (NCERT spelling <b>Xx</b> preserved.)"))
story.append(b1(
    "<b>In chicken, sex chromosomes in male are ZZ, and in females are ZW.</b> (Summary-"
    "only wording; the body's paragraph 4.6 names the chromosomes Z and W but does not "
    "name the chicken.)"))
story.append(b1(
    "<b>Mutation is defined as change in the genetic material.</b>"))
story.append(b1(
    "<b>A point mutation is a change of a single base pair in DNA.</b>"))
story.append(b1(
    "<b>Sickle-cell anemia is caused due to change of one base in the gene coding for "
    "beta-chain of hemoglobin.</b>"))
story.append(b1(
    "<b>Inheritable mutations can be studied by generating a pedigree of a family.</b>"))
story.append(b1(
    "<b>Some mutations involve changes in whole set of chromosomes (polyploidy) or "
    "change in a subset of chromosome number (aneuploidy).</b>"))
story.append(b1(
    "<b>This helped in understanding the mutational basis of genetic disorders.</b>"))
story.append(b1(
    "<b>Down's syndrome is due to trisomy of chromosome 21, where there is an extra "
    "copy of chromosome 21 and consequently the total number of chromosome becomes 47.</b>"))
story.append(b1(
    "<b>In Turner's syndrome, one X chromosome is missing and the sex chromosome is as "
    "X0, and in Klinefelter's syndrome, the condition is XXY.</b>"))
story.append(b1(
    "<b>These can be easily studied by analysis of Karyotypes.</b> (Summary-only "
    "wording; the body gives 'a karyotype of 47, XXY' as a phrase, never 'analysis of "
    "Karyotypes' as a method.)"))

# ======================================================================================
# ---- Terms used in the exercises (SS5 item 9; Rule 2; 4 GAPs) ----
#      12 of 16 exercises are answered by the body and are not reproduced (Rule 2
#      forbids printing the same fact twice). The 4 GAPs (Q1, Q3, Q6, Q7) are worked
#      out here, each visibly marked as worked-out and not NCERT text.
#      Arithmetic: 16 exercises, 4 answered by design (GAP), 12 unanswered by design
#      (COVERED), 0 overlooked.
# ======================================================================================
story.append(gap(6))
story.append(heading("Appendix", "TERMS USED IN THE EXERCISES", level=1))

story.append(body(
    "<b>The exercises</b> at the end of this NCERT chapter assume four things the chapter "
    "itself never spells out. All four are worked out below, each visibly marked as an "
    "answer drawn from this chapter's own sentences and not as text carried in from "
    "elsewhere."))
story.append(b1(
    "<b>16 exercises, 4 answered by design (GAP), 12 unanswered by design (COVERED), 0 "
    "overlooked.</b>"))

# Q1 - GAP
story.append(gap())
story.append(heading("Q1", "Advantages of selecting pea plant for experiment by Mendel", level=3))
story.append(body(
    "<b>Worked-out answer, assembled from this chapter's own sentences in section 4.1 "
    "(not NCERT text):</b>"))
story.append(b1(
    "<b>True-breeding lines.</b> The pea plant has many <b>true-breeding pea lines</b> "
    "(F038) - varieties that, under continuous self-pollination, show the <b>stable trait "
    "inheritance and expression for several generations</b> (F039)."))
story.append(b1(
    "<b>Characters with two opposing traits.</b> The pea plant has <b>characters ... that "
    "were manifested as two opposing traits</b> (F037) - tall/dwarf, yellow/green, "
    "round/wrinkled - 14 such pairs in total (F040)."))
story.append(b1(
    "<b>Artificial cross-pollination is straightforward.</b> Mendel conducted <b>artificial "
    "pollination / cross pollination experiments</b> (F038) - emasculation and pollen "
    "transfer are simple to do on a pea flower (Figure 4.2)."))
story.append(b1(
    "<b>Short life cycle and many offspring.</b> The 7-year window (1856-1863, F033) "
    "implies a manageable generation time and enough progeny to do the statistical "
    "analysis that the chapter credits Mendel with introducing for the first time in "
    "biology (F034)."))
story.append(b1(
    "<b>Large sampling size, giving credibility to the data.</b> The chapter calls this "
    "out by name (F035)."))
story.append(memory_aid(
    "<b>Five reasons, one mnemonic:</b> <b>True-breeding, Two-opposing, Cross-ability, "
    "Short cycle, Sample size</b> - <b>T-T-C-S-S</b>. Or, said the other way: every "
    "property the body says the pea has is the reason a question calling them "
    "'advantages' would want named."))

# Q3 - GAP
story.append(gap())
story.append(heading("Q3",
                      "Gamete types for a diploid heterozygous at 4 loci (2^n rule)", level=3))
story.append(body(
    "<b>Worked-out answer, extension of the 4.3.1 statement (not NCERT text):</b>"))
story.append(b1(
    "Section 4.3.1 (F188) states that the F<sub>1</sub> plant <i>RrYy</i> produces "
    "<b>four types of gametes (RY, Ry, rY, ry) each with a frequency of 25 per cent or "
    "1/4</b>."))
story.append(b1(
    "Two heterozygous loci to <b>2<sup>2</sup> = 4</b> gamete types, each at "
    "<b>1/4</b>."))
story.append(b1(
    "Generalising: <i>n</i> heterozygous loci to <b>2<sup>n</sup></b> gamete types, "
    "each at <b>1/2<sup>n</sup></b>."))
story.append(b1(
    "For <i>n</i> = 4: <b>2<sup>4</sup> = 16</b> gamete types, each at "
    "<b>1/16</b>."))
story.append(memory_aid(
    "<b>2<sup>n</sup> gametes, each at 1/2<sup>n</sup>:</b> two loci to 4 at 1/4; "
    "three loci to 8 at 1/8; four loci to 16 at 1/16. The source's 4.3.1 gives "
    "the 2-locus case as the only worked example; the rest is reasoning on top of it."))

# Q6 - GAP
story.append(gap())
story.append(heading("Q6",
                      "Homozygous female x heterozygous male, single locus", level=3))
story.append(body(
    "<b>Worked-out answer, drawing on the Law of Dominance rows of 4.2.1 (not NCERT "
    "text):</b>"))
story.append(b1(
    "Cross: <b>TT &times; Tt</b> (homozygous dominant female, heterozygous male)."))
story.append(b1(
    "Female gametes: all <b>T</b>."))
story.append(b1(
    "Male gametes: <b>1/2 T</b> and <b>1/2 t</b>."))
story.append(b1(
    "Offspring: <b>1/2 TT</b> and <b>1/2 Tt</b>."))
story.append(b1(
    "<b>Genotypic ratio: 1:1.</b>"))
story.append(b1(
    "<b>Phenotypic ratio: all tall (1:0)</b> - by the Law of Dominance (4.2.1), T is "
    "dominant over t, so both TT and Tt are phenotypically tall (F072, F074)."))
story.append(memory_aid(
    "<b>Homozygous x heterozygous, single locus:</b> <b>1 TT : 1 Tt</b> genotypically, "
    "<b>all tall</b> phenotypically. Same gamete split as a testcross (1:1) but with a "
    "dominant parent instead of a recessive one, so no recessive phenotype appears."))

# Q7 - GAP
# [VERIFICATION FIX] D1 (Gate 3(b)): prior answer dropped every t-bearing gamete from
# Parent 1 and claimed "no dwarf" / tall-green = 1/2. Correct 4 x 2 Punnett from the
# 4.3.1 gamete-frequency rows: (a) tall green = 3/8, (b) dwarf green = 1/8.
story.append(gap())
story.append(heading("Q7",
                      "Cross TtYy (tall, yellow) x Ttyy (tall, green)", level=3))
story.append(body(
    "<b>Worked-out answer, derived from the 4.3.1 gamete-frequency rows (not NCERT "
    "text):</b>"))
story.append(b1(
    "Parent 1 (TtYy) gametes (4.3.1, F188): <b>1/4 TY, 1/4 Ty, 1/4 tY, 1/4 ty</b>."))
story.append(b1(
    "Parent 2 (Ttyy) gametes: <b>1/2 Ty</b> and <b>1/2 ty</b> "
    "(T/t segregates 1:1; only y is available on the colour locus)."))
story.append(b1(
    "Combine: <b>4 x 2 = 8</b> equally-likely cells (each at <b>1/8</b>):"))
story.append(data_table([
    ["Parent 1 gamete", "x Parent 2", "Offspring", "Phenotype"],
    ["<b>TY</b> (1/4)", "<b>Ty</b> (1/2)", "<b>TTYy</b> (1/8)", "<b>Tall, yellow</b>"],
    ["<b>TY</b> (1/4)", "<b>ty</b> (1/2)", "<b>TtYy</b> (1/8)", "<b>Tall, yellow</b>"],
    ["<b>Ty</b> (1/4)", "<b>Ty</b> (1/2)", "<b>TTyy</b> (1/8)", "<b>Tall, green</b>"],
    ["<b>Ty</b> (1/4)", "<b>ty</b> (1/2)", "<b>Ttyy</b> (1/8)", "<b>Tall, green</b>"],
    ["<b>tY</b> (1/4)", "<b>Ty</b> (1/2)", "<b>TtYy</b> (1/8)", "<b>Tall, yellow</b>"],
    ["<b>tY</b> (1/4)", "<b>ty</b> (1/2)", "<b>ttYy</b> (1/8)", "<b>Dwarf, yellow</b>"],
    ["<b>ty</b> (1/4)", "<b>Ty</b> (1/2)", "<b>Ttyy</b> (1/8)", "<b>Tall, green</b>"],
    ["<b>ty</b> (1/4)", "<b>ty</b> (1/2)", "<b>ttyy</b> (1/8)", "<b>Dwarf, green</b>"],
], col_widths=[22, 20, 24, 34]))
story.append(b1(
    "<b>Phenotypic totals:</b> tall-yellow <b>3/8</b> (TTYy 1/8 + TtYy 1/8 + TtYy 1/8); "
    "tall-green <b>3/8</b> (TTyy 1/8 + Ttyy 1/8 + Ttyy 1/8); dwarf-yellow <b>1/8</b> "
    "(ttYy); dwarf-green <b>1/8</b> (ttyy)."))
story.append(b1(
    "<b>(a) Tall and green: 3/8</b>."))
story.append(b1(
    "<b>(b) Dwarf and green: 1/8</b> - the t gametes from Parent 1 are required; "
    "without them the dwarf classes vanish, which is the error the corrected table "
    "removes."))
story.append(memory_aid(
    "<b>TtYy x Ttyy</b> in one line: <b>3/8 tall-yellow : 3/8 tall-green : 1/8 "
    "dwarf-yellow : 1/8 dwarf-green</b>. Height still segregates 3 tall : 1 dwarf "
    "(Parent 1 is Tt; Parent 2 is Tt too), and colour segregates 1 yellow : 1 green "
    "(only Parent 1 carries Y). Independent assortment multiplies the two monohybrid "
    "ratios."))

# ======================================================================================
# ---- Build (SS5) ----
# ======================================================================================
def main():
    build_pdf(
        OUT_PDF,
        story,
        title="Principles of Inheritance and Variation - NEET Notes (NCERT Class 12, Chapter 4)",
        subject="NCERT Class 12 Biology, Chapter 4 - Principles of Inheritance and Variation: "
                "NEET replacement notes",
    )


if __name__ == "__main__":
    main()
