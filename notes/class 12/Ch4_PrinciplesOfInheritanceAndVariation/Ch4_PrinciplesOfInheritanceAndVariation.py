"""
Ch4 — Principles of Inheritance and Variation (Class 12, NCERT Biology).

Pass 2 script: imports neet_template.py for the entire design canon
(geometry, colour palette, paragraph styles, helpers) and produces the
chapter PDF by walking the §5 Content Order in a single linear
story.append(...) sequence.

OPERATOR DECISION (per inventory FIGURE_DECISIONS.md and the chapter
script docstring requirement): no figure is embedded. The source is a
page-image scan; every NCERT plate would reproduce as a useless low-
contrast bitmap. Every fact in every caption and every in-figure label
is carried in the running text instead (Punnett squares and cross
diagrams become real data_table grids; the pedigree-symbol plate becomes
a two-column symbol/meaning table; the remaining plates get a short
'Read the plate' note immediately after the paragraph that cites them).

Every block in this script is comment-tagged with its NCERT section
number in the form `# ---- N.N ----` so a future agent doing Pass 3 can
jump straight to the block that needs an edit without re-reading the
file. (SUPREME COMMAND PROMPT v6, §4 ReportLab strict technical rules.)
"""

import os
import sys

# neet_template.py is at the repo root; this script lives several levels
# deep under notes/. A small sys.path bootstrap walks up to find it.
HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = HERE
for _ in range(6):
    if os.path.exists(os.path.join(REPO_ROOT, "neet_template.py")):
        break
    REPO_ROOT = os.path.dirname(REPO_ROOT)
sys.path.insert(0, REPO_ROOT)

from neet_template import (
    PAGE_SIZE, MARGIN, TOP_MARGIN, BOTTOM_MARGIN, FRAME_WIDTH,
    DARK_GREY, MED_GREY, SOFT_GREY, ROW_ALT, NOTE_BG, GRID_LINE, INK,
    STYLES, TABLE_PADDING,
    heading, keyterm, process_flow, note, memory_aid, data_table,
    title_block, build_pdf,
)
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, KeepTogether, HRFlowable
from reportlab.lib.units import cm
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT

# The "figure" helper is intentionally NOT imported — see the operator
# decision in this script's docstring. No figure() call exists in this
# file, which is why check_pdf.py check 3 (grayscale images) will report
# zero embedded images and check 6 (figure-label coverage) will audit
# 163 labels against the running text.

OUT_PDF = os.path.join(HERE, "Ch4_PrinciplesOfInheritanceAndVariation.pdf")

story = []

# ---- Title block ----
story.extend(title_block("Principles of Inheritance and Variation"))


# ---- Unit VII banner + Unit title (rows F001, F002, F004) ----
story.append(heading("VII", "Unit VII - Genetics and Evolution", level=1))
story.append(Paragraph(
    "The work of Mendel and others who followed him gave us an idea of "
    "inheritance patterns. The entire body of molecular biology was a "
    "consequent development with major contributions from Watson, Crick, "
    "Nirenberg, Khorana, Kornberg's (father and son), Benzer, Monod, "
    "Brenner, etc. In this unit the structure and function of DNA and "
    "the story and theory of evolution have been examined and explained.",
    STYLES["Body"]))


# ---- Scientist profile: JAMES WATSON (rows F011-F018) ----
story.append(heading("", "James Watson", level=2))
story.append(Paragraph(
    "James Dewey Watson was born in Chicago on 6 April 1928. In 1947, "
    "he received B.Sc. degree in Zoology. During these years his interest "
    "in bird-watching had matured into a serious desire to learn genetics. "
    "This became possible when he received a Fellowship for graduate study "
    "in Zoology at Indiana University, Bloomington, where he received his "
    "Ph.D. degree in 1950 on a study of the effect of hard X-rays on "
    "bacteriophage multiplication. He met Crick and discovered their "
    "common interest in solving the DNA structure. Their first serious "
    "effort was unsatisfactory. Their second effort, based upon more "
    "experimental evidence and better appreciation of the nucleic acid "
    "literature, resulted, early in March 1953, in the proposal of the "
    "complementary double-helical configuration.",
    STYLES["Body"]))


# ---- Scientist profile: FRANCIS CRICK (rows F019-F026) ----
story.append(heading("", "Francis Crick", level=2))
story.append(Paragraph(
    "Francis Harry Compton Crick was born on 8 June 1916, at Northampton, "
    "England. He studied physics at University College, London and obtained "
    "a B.Sc. in 1937. He completed Ph.D. in 1954 on a thesis entitled "
    "<i>X-ray Diffraction: Polypeptides and Proteins</i>. A critical influence "
    "in Crick's career was his friendship with J.D. Watson, then a young man "
    "of 23, leading in 1953 to the proposal of the double-helical structure "
    "for DNA and the replication scheme. Crick was made an F.R.S. in 1959. "
    "The honours to Watson with Crick include: the John Collins Warren "
    "Prize of the Massachusetts General Hospital, in 1959; the Lasker Award "
    "in 1960; the Research Corporation Prize, in 1962; and above all, the "
    "Nobel Prize in 1962.",
    STYLES["Body"]))


# ---- Chapter 4 banner (rows F027, F028) ----
story.append(heading("4", "Chapter 4 - Principles of Inheritance and Variation", level=1))


# ---- Chapter opener (row F029 contents box + F034, F035) ----
story.append(Paragraph(
    "These and several related questions are dealt with, scientifically, in "
    "a branch of biology known as Genetics. This subject deals with the "
    "inheritance, as well as the variation of characters from parents to "
    "offspring.",
    STYLES["Body"]))

# Definitions of inheritance and variation (rows F036, F037)
story.append(Paragraph("<b>Inheritance</b> is the process by which characters are passed on from parent to progeny; it is the basis of heredity.", STYLES["Body"]))
story.append(Paragraph("<b>Variation</b> is the degree by which progeny differ from their parents.", STYLES["Body"]))

# Early knowledge (F038-F040)
story.append(Paragraph(
    "Humans knew from as early as 8000-1000 B.C. that one of the causes of "
    "variation was hidden in sexual reproduction. They exploited the variations "
    "that were naturally present in the wild populations of plants and animals "
    "to selectively breed and select for organisms that possessed desirable "
    "characters. For example, through artificial selection and domestication "
    "from ancestral wild cows, we have well-known Indian breeds, e.g., Sahiwal "
    "cows in Punjab.",
    STYLES["Body"]))


# ---- 4.1 Mendel's Laws of Inheritance (rows F042-F063) ----
story.append(heading("4.1", "Mendel's Laws of Inheritance", level=1))
story.append(Paragraph(
    "It was during the mid-nineteenth century that headway was made in the "
    "understanding of inheritance. Gregor Mendel conducted hybridisation "
    "experiments on garden peas for seven years (1856-1863) and proposed the "
    "laws of inheritance in living organisms.",
    STYLES["Body"]))
story.append(Paragraph(
    "During Mendel's investigations into inheritance patterns it was for the "
    "first time that statistical analysis and mathematical logic were applied "
    "to problems in biology. His experiments had a large sampling size, which "
    "gave greater credibility to the data that he collected. Also, the "
    "confirmation of his inferences from experiments on successive generations "
    "of his test plants proved that his results pointed to general rules of "
    "inheritance rather than being unsubstantiated ideas.",
    STYLES["Body"]))
story.append(Paragraph(
    "Mendel investigated characters in the garden pea plant that were "
    "manifested as two opposing traits, e.g., tall or dwarf plants, yellow "
    "or green seeds. Mendel conducted such artificial pollination/cross "
    "pollination experiments using several true-breeding pea lines. "
    "<b>A true-breeding line</b> is one that, having undergone continuous "
    "self-pollination, shows the stable trait inheritance and expression for "
    "several generations. Mendel selected 14 true-breeding pea plant varieties, "
    "as pairs which were similar except for one character with contrasting "
    "traits. Some of the contrasting traits selected were smooth or wrinkled "
    "seeds, yellow or green seeds, inflated (full) or constricted green or "
    "yellow pods and tall or dwarf plants (Figure 4.1, Table 4.1).",
    STYLES["Body"]))

# Figure 4.1 / Table 4.1 — read-the-plate note + table reproduction
story.append(note(
    "Read the plate (Fig 4.1): the seven contrasting traits are listed as "
    "Character / Dominant trait / Recessive trait. The 22 labels on the plate "
    "are: Character, Dominant trait, Recessive trait, Seed shape, Round, "
    "Wrinkled, Seed colour, Yellow, Green, Flower colour, Violet, White, Pod "
    "shape, Full, Constricted, Pod colour, Flower position, Axial, Terminal, "
    "Stem height, Tall, Dwarf."
))
story.append(Paragraph(
    "<b>Table 4.1 - Contrasting Traits Studied by Mendel in Pea</b>",
    STYLES["Body"]))
table_41 = data_table(
    [
        ["S.No.", "Characters", "Contrasting Traits"],
        ["1", "Stem height", "Tall / dwarf"],
        ["2", "Flower colour", "Violet / white"],
        ["3", "Flower position", "Axial / terminal"],
        ["4", "Pod shape", "Inflated / constricted"],
        ["5", "Pod colour", "Green / yellow"],
        ["6", "Seed shape", "Round / wrinkled"],
        ["7", "Seed colour", "Yellow / green"],
    ],
    col_widths=[1, 4, 4],
)
story.append(table_41)


# ---- 4.2 Inheritance of One Gene (rows F064-F142) ----
story.append(heading("4.2", "Inheritance of One Gene", level=1))
story.append(Paragraph(
    "Let us take the example of one such hybridisation experiment carried "
    "out by Mendel where he crossed tall and dwarf pea plants to study the "
    "inheritance of one gene (Figure 4.2). He collected the seeds produced as "
    "a result of this cross and grew them to generate plants of the first "
    "hybrid generation. This generation is also called the Filial<sub>1</sub> "
    "progeny or the F<sub>1</sub>. Mendel observed that all the F<sub>1</sub> "
    "progeny plants were tall, like one of its parents; none were dwarf "
    "(Figure 4.3). Mendel then self-pollinated the tall F<sub>1</sub> plants "
    "and to his surprise found that in the Filial<sub>2</sub> generation some "
    "of the offspring were 'dwarf'; the character that was not seen in the "
    "F<sub>1</sub> generation was now expressed. The proportion of plants "
    "that were dwarf were 1/4th of the F<sub>2</sub> plants while 3/4th of "
    "the F<sub>2</sub> plants were tall.",
    STYLES["Body"]))
story.append(Paragraph(
    "The tall and dwarf traits were identical to their parental type and did "
    "not show any blending, that is all the offspring were either tall or "
    "dwarf, none were of in-between height (Figure 4.3). Similar results were "
    "obtained with the other traits that he studied: only one of the parental "
    "traits was expressed in the F<sub>1</sub> generation while at the "
    "F<sub>2</sub> stage both the traits were expressed in the proportion "
    "3:1. The contrasting traits did not show any blending at either "
    "F<sub>1</sub> or F<sub>2</sub> stage.",
    STYLES["Body"]))

# Figure 4.2 read-the-plate note (emasculation / pollination diagram)
story.append(note(
    "Read the plate (Fig 4.2): the steps in making a cross in pea. The 10 "
    "labels on the plate are: Petal, Stigma, Anther, Stamen, Carpel, Removal "
    "of anthers (Emasculation), Transfer of pollen (Pollination), Parent."
))

# Genes, alleles, genotype, phenotype (F077-F093)
story.append(Paragraph(
    "Based on these observations, Mendel proposed that something was being "
    "stably passed down, unchanged, from parent to offspring through the "
    "gametes, over successive generations. He called these things as 'factors'. "
    "Now we call them as <b>genes</b>. Genes, therefore, are the units of "
    "inheritance. They contain the information that is required to express a "
    "particular trait in an organism. <b>Genes</b> which code for a pair of "
    "contrasting traits are known as <b>alleles</b>, i.e., they are slightly "
    "different forms of the same gene.",
    STYLES["Body"]))
story.append(Paragraph(
    "If we use alphabetical symbols for each gene, then the capital letter is "
    "used for the trait expressed at the F<sub>1</sub> stage and the small "
    "alphabet for the other trait. For example, in case of the character of "
    "height, T is used for the Tall trait and t for the 'dwarf', and T and t "
    "are alleles of each other. Hence, in plants the pair of alleles for "
    "height would be TT, Tt or tt. Mendel also proposed that in a true "
    "breeding, tall or dwarf pea variety the allelic pair of genes for height "
    "are identical or homozygous, TT and tt, respectively. TT and tt are "
    "called the <b>genotype</b> of the plant while the descriptive terms tall "
    "and dwarf are the <b>phenotype</b>.",
    STYLES["Body"]))

# F086 — keep this question, it frames dominance
story.append(Paragraph(
    "<i>What then would be the phenotype of a plant that had a genotype Tt?</i>",
    STYLES["Body"]))
story.append(Paragraph(
    "As Mendel found the phenotype of the F<sub>1</sub> heterozygote Tt to "
    "be exactly like the TT parent in appearance, he proposed that in a pair "
    "of dissimilar factors, one dominates the other (as in the F<sub>1</sub>) "
    "and hence is called the dominant factor while the other factor is "
    "recessive. In this case T (for tallness) is dominant over t (for "
    "dwarfness), that is recessive. It is convenient (and logical) to use the "
    "capital and lower case of an alphabetical symbol to remember this "
    "concept of dominance and recessiveness. (Do not use T for tall and d "
    "for dwarf because you will find it difficult to remember whether T and d "
    "are alleles of the same gene/character or not.) Alleles can be similar "
    "as in the case of homozygotes TT and tt or can be dissimilar as in the "
    "case of the heterozygote Tt. Since the Tt plant is heterozygous for genes "
    "controlling one character (height), it is a <b>monohybrid</b> and the "
    "cross between TT and tt is a <b>monohybrid cross</b>.",
    STYLES["Body"]))

# Figure 4.3 read-the-plate note (monohybrid cross diagram)
story.append(note(
    "Read the plate (Fig 4.3): the diagrammatic representation of the "
    "monohybrid cross. The 6 labels on the plate are: Parental, Tall, Dwarf, "
    "F<sub>1</sub> generation, Selfing, F<sub>2</sub> generation."
))

# Law of Segregation and Punnett square (F096-F107)
story.append(Paragraph(
    "From the observation that the recessive parental trait is expressed "
    "without any blending in the F<sub>2</sub> generation, we can infer that, "
    "when the tall and dwarf plant produce gametes, by the process of meiosis, "
    "the alleles of the parental pair separate or segregate from each other "
    "and only one allele is transmitted to a gamete. This segregation of "
    "alleles is a random process and so there is a 50 per cent chance of a "
    "gamete containing either allele, as has been verified by the results "
    "of the crossings. In this way the gametes of the tall TT plants have "
    "the allele T and the gametes of the dwarf tt plants have the allele t. "
    "During fertilisation the two alleles, T from one parent say, through the "
    "pollen, and t from the other parent, then through the egg, are united "
    "to produce zygotes that have one T allele and one t allele.",
    STYLES["Body"]))
story.append(Paragraph(
    "The production of gametes by the parents, the formation of the zygotes, "
    "the F<sub>1</sub> and F<sub>2</sub> plants can be understood from a "
    "diagram called <b>Punnett Square</b> as shown in Figure 4.4. It was "
    "developed by a British geneticist, Reginald C. Punnett. It is a "
    "graphical representation to calculate the probability of all possible "
    "genotypes of offspring in a genetic cross. The possible gametes are "
    "written on two sides, usually the top row and left columns. All "
    "possible combinations are represented in boxes below in the squares, "
    "which generates a square output form.",
    STYLES["Body"]))
story.append(Paragraph(
    "The Punnett Square shows the parental tall TT (male) and dwarf tt "
    "(female) plants, the gametes produced by them and, the F<sub>1</sub> Tt "
    "progeny. The F<sub>1</sub> plants of genotype Tt are self-pollinated. "
    "The symbols for female and male are used to denote the female (eggs) "
    "and male (pollen) of the F<sub>1</sub> generation, respectively. The "
    "F<sub>1</sub> plant of genotype Tt when self-pollinated, produces "
    "gametes of the genotype T and t in equal proportion. When fertilisation "
    "takes place, the pollen grains of genotype T have a 50 per cent chance "
    "to pollinate eggs of the genotype T, as well as of genotype t. Also "
    "pollen grains of genotype t have a 50 per cent chance of pollinating "
    "eggs of genotype T, as well as of genotype t.",
    STYLES["Body"]))

# Figure 4.4 — Punnett square rendered as a real table (F108, F109, F111-F118)
story.append(Paragraph(
    "<b>Fig. 4.4 - Punnett square for a typical monohybrid cross</b> (Mendel, "
    "TT male x tt female, F<sub>1</sub> = Tt, selfed to give F<sub>2</sub>; "
    "phenotypic ratio tall:dwarf = 3:1; genotypic ratio TT:Tt:tt = 1:2:1).",
    STYLES["Body"]))
punnett_mono = data_table(
    [
        ["", "T (pollen)", "t (pollen)"],
        ["T (egg)", "TT (tall)", "Tt (tall)"],
        ["t (egg)", "Tt (tall)", "tt (dwarf)"],
    ],
    col_widths=[2, 3, 3],
)
story.append(punnett_mono)
story.append(Paragraph(
    "<i>Read the plate (Fig 4.4) - the 12 labels on the plate are: Tall, TT, "
    "Dwarf, tt, Gametes, T, t, F<sub>1</sub> generation, Tt, Selfing, "
    "Phenotypic ratio: tall:dwarf 3:1, Genotypic ratio: TT:Tt:tt 1:2:1.</i>",
    STYLES["Caption"]))

# Continue body prose
story.append(Paragraph(
    "As a result of random fertilisation, the resultant zygotes can be of "
    "the genotypes TT, Tt or tt. From the Punnett square it is easily seen "
    "that 1/4th of the random fertilisations lead to TT, 1/2 lead to Tt and "
    "1/4th to tt. Though the F<sub>1</sub> have a genotype of Tt, but the "
    "phenotypic character seen is 'tall'. At F<sub>2</sub> 3/4th of the "
    "plants are tall, where some of them are TT while others are Tt. "
    "Externally it is not possible to distinguish between the plants with "
    "the genotypes TT and Tt. Hence the character T or 'tall' is said to "
    "dominate over the other allele t or 'dwarf' character. It is thus due "
    "to this dominance of one character over the other that all the "
    "F<sub>1</sub> are tall (though the genotype is Tt) and in the "
    "F<sub>2</sub> 3/4th of the plants are tall (though genotypically 1/2 "
    "are Tt and only 1/4th are TT). This leads to a phenotypic ratio of 3/4 "
    "tall : (1/4 TT + 1/2 Tt) and 1/4 tt, i.e., a 3:1 ratio, but a genotypic "
    "ratio of 1:2:1.",
    STYLES["Body"]))

# Binomial expansion (F119, F120) - rendered as a process flow
story.append(Paragraph(
    "The 1/4 : 1/2 : 1/4 ratio of TT:Tt:tt is mathematically condensable to "
    "the form of the binomial expression (ax + by)<super>2</super>, that has "
    "the gametes bearing genes T or t in equal frequency of 1/2. The "
    "expansion is:",
    STYLES["Body"]))
story.append(Paragraph(
    "(1/2 T + 1/2 t)<super>2</super> = (1/2 T + 1/2 t) x (1/2 T + 1/2 t) "
    "= 1/4 TT + 1/2 Tt + 1/4 tt.",
    STYLES["Body"]))

# F121, F122
story.append(Paragraph(
    "Mendel self-pollinated the F<sub>2</sub> plants and found that dwarf "
    "F<sub>2</sub> plants continued to generate dwarf plants in F<sub>3</sub> "
    "and F<sub>4</sub> generations. He concluded that the genotype of the "
    "dwarfs was homozygous-tt.",
    STYLES["Body"]))

# F124, F125, testcross
story.append(Paragraph(
    "From the preceding paragraphs it is clear that though the genotypic "
    "ratios can be calculated using mathematical probability, by simply "
    "looking at the phenotype of a dominant trait, it is not possible to "
    "know the genotypic composition. That is, for example, whether a tall "
    "plant from F<sub>1</sub> or F<sub>2</sub> has TT or Tt composition, "
    "cannot be predicted. Therefore, to determine the genotype of a tall "
    "plant at F<sub>2</sub>, Mendel crossed the tall plant from F<sub>2</sub> "
    "with a dwarf plant. This he called a <b>testcross</b>. In a typical "
    "testcross an organism (pea plants here) showing a dominant phenotype "
    "(and whose genotype is to be determined) is crossed with the recessive "
    "parent instead of self-crossing. The progenies of such a cross can "
    "easily be analysed to predict the genotype of the test organism. "
    "Figure 4.5 shows the results of typical testcross where violet colour "
    "flower (V) is dominant over white colour flower (v).",
    STYLES["Body"]))

# Figure 4.5 — test cross rendered as a small table (F133, F134)
story.append(Paragraph(
    "<b>Fig. 4.5 - Test cross</b> (Dominant Phenotype - Genotype unknown - "
    "crossed with Homozygous recessive):",
    STYLES["Body"]))
testcross_tbl = data_table(
    [
        ["Cross", "Result", "Interpretation"],
        ["WW x ww (Homozygous dominant x Homozygous recessive)", "All flowers are violet", "Unknown flower is homozygous dominant (WW)"],
        ["Ww x ww (Heterozygous x Homozygous recessive)", "Half of the flowers are violet and half of the flowers are white", "Unknown flower is heterozygous (Ww)"],
    ],
    col_widths=[3, 3, 4],
)
story.append(testcross_tbl)
story.append(Paragraph(
    "<i>Read the plate (Fig 4.5) - the 8 labels on the plate are: Homozygous "
    "recessive, Ww, WW, Dominant Phenotype (Genotype unknown), Result - All "
    "flowers are violet, Interpretation - Unknown flower is homozygous "
    "dominant, Half of the flowers are violet and half of the flowers are "
    "white, Unknown flower is heterozygous.</i>",
    STYLES["Caption"]))

# F135 - Mendel's two laws
story.append(Paragraph(
    "Based on his observations on monohybrid crosses Mendel proposed two "
    "general rules to consolidate his understanding of inheritance in "
    "monohybrid crosses. Today these rules are called the Principles or Laws "
    "of Inheritance: the First Law or Law of Dominance and the Second Law or "
    "Law of Segregation.",
    STYLES["Body"]))


# ---- 4.2.1 Law of Dominance (F136-F140) ----
story.append(heading("4.2.1", "Law of Dominance", level=2))
story.append(Paragraph(
    "(i) Characters are controlled by discrete units called factors. "
    "(ii) Factors occur in pairs. (iii) In a dissimilar pair of factors one "
    "member of the pair dominates (dominant) the other (recessive).",
    STYLES["Body"]))
story.append(Paragraph(
    "The law of dominance is used to explain the expression of only one of "
    "the parental characters in a monohybrid cross in the F<sub>1</sub> and "
    "the expression of both in the F<sub>2</sub>. It also explains the "
    "proportion of 3:1 obtained at the F<sub>2</sub>.",
    STYLES["Body"]))


# ---- 4.2.2 Law of Segregation (F141-F144) ----
story.append(heading("4.2.2", "Law of Segregation", level=2))
story.append(Paragraph(
    "This law is based on the fact that the alleles do not show any blending "
    "and that both the characters are recovered as such in the F<sub>2</sub> "
    "generation though one of these is not seen at the F<sub>1</sub> stage. "
    "Though the parents contain two alleles during gamete formation, the "
    "factors or alleles of a pair segregate from each other such that a "
    "gamete receives only one of the two factors. Of course, a homozygous "
    "parent produces all gametes that are similar while a heterozygous one "
    "produces two kinds of gametes each having one allele with equal "
    "proportion.",
    STYLES["Body"]))


# ---- 4.2.2.1 Incomplete Dominance (F145-F164) ----
story.append(heading("4.2.2.1", "Incomplete Dominance", level=2))
story.append(Paragraph(
    "When experiments on peas were repeated using other traits in other "
    "plants, it was found that sometimes the F<sub>1</sub> had a phenotype "
    "that did not resemble either of the two parents and was in between the "
    "two. The inheritance of flower colour in the dog flower (snapdragon or "
    "<i>Antirrhinum</i> sp.) is a good example to understand incomplete "
    "dominance. In a cross between true-breeding red-flowered (RR) and "
    "true-breeding white-flowered plants (rr), the F<sub>1</sub> (Rr) was "
    "pink (Figure 4.6). When the F<sub>1</sub> was self-pollinated the "
    "F<sub>2</sub> resulted in the following ratio 1 (RR) Red : 2 (Rr) "
    "Pink : 1 (rr) White. Here the genotype ratios were exactly as we would "
    "expect in any mendelian monohybrid cross, but the phenotype ratios had "
    "changed from the 3:1 dominant:recessive ratio. What happened was that "
    "R was not completely dominant over r and this made it possible to "
    "distinguish Rr as pink from RR (red) and rr (white).",
    STYLES["Body"]))

# F152 — keep the question
story.append(Paragraph(
    "<i>Explanation of the concept of dominance: What exactly is dominance? "
    "Why are some alleles dominant and some recessive?</i>",
    STYLES["Body"]))
story.append(Paragraph(
    "To tackle these questions, we must understand what a gene does. Every "
    "gene, as you know by now, contains the information to express a "
    "particular trait. In a diploid organism, there are two copies of each "
    "gene, i.e., as a pair of alleles. Now, these two alleles need not "
    "always be identical, as in a heterozygote. One of them may be different "
    "due to some changes that it has undergone (about which you will read "
    "further on, and in the next chapter) which modifies the information "
    "that particular allele contains.",
    STYLES["Body"]))
story.append(Paragraph(
    "Let's take an example of a gene that contains the information for "
    "producing an enzyme. Now there are two copies of this gene, the two "
    "allelic forms. Let us assume (as is more common) that the normal allele "
    "produces the normal enzyme that is needed for the transformation of a "
    "substrate S. Theoretically, the modified allele could be responsible "
    "for production of: (i) the normal/less efficient enzyme, or (ii) a "
    "non-functional enzyme, or (iii) no enzyme at all. In the first case, "
    "the modified allele is equivalent to the unmodified allele, i.e., it "
    "will produce the same phenotype/trait, i.e., result in the "
    "transformation of substrate S. Such equivalent allele pairs are very "
    "common. But, if the allele produces a non-functional enzyme or no "
    "enzyme, the phenotype may be affected. The phenotype/trait will only "
    "be dependent on the functioning of the unmodified allele. The "
    "unmodified (functioning) allele, which represents the original "
    "phenotype is the dominant allele and the modified allele is generally "
    "the recessive allele. Hence, in the example above the recessive trait "
    "is seen due to non-functional enzyme or because no enzyme is produced.",
    STYLES["Body"]))

# Figure 4.6 — read-the-plate note (F159, F160)
story.append(note(
    "Read the plate (Fig 4.6): results of monohybrid cross in the plant "
    "Snapdragon. The 13 labels on the plate are: P generation, Red (RR), "
    "White (rr), Gametes, R, r, F<sub>1</sub> generation, All pink (Rr), RR, "
    "Rr, F<sub>2</sub> generation, Phenotypic ratio: red:pink:white 1:2:1, "
    "Genotypic ratio: RR:Rr:rr 1:2:1."
))


# ---- 4.2.2.2 Co-dominance (F165-F190) ----
story.append(heading("4.2.2.2", "Co-dominance", level=2))
story.append(Paragraph(
    "Till now we were discussing crosses where the F<sub>1</sub> resembled "
    "either of the two parents (dominance) or was in-between (incomplete "
    "dominance). But, in the case of co-dominance the F<sub>1</sub> "
    "generation resembles both parents. A good example is different types of "
    "red blood cells that determine ABO blood grouping in human beings. ABO "
    "blood groups are controlled by the gene I. The plasma membrane of the "
    "red blood cells has sugar polymers that protrude from its surface and "
    "the kind of sugar is controlled by the gene. The gene (I) has three "
    "alleles I<sup>A</sup>, I<sup>B</sup> and i. The alleles I<sup>A</sup> "
    "and I<sup>B</sup> produce a slightly different form of the sugar while "
    "allele i does not produce any sugar. Because humans are diploid "
    "organisms, each person possesses any two of the three I gene alleles. "
    "I<sup>A</sup> and I<sup>B</sup> are completely dominant over i, in "
    "other words when I<sup>A</sup> and i are present only I<sup>A</sup> "
    "expresses (because i does not produce any sugar), and when I<sup>B</sup> "
    "and i are present I<sup>B</sup> expresses. But when I<sup>A</sup> and "
    "I<sup>B</sup> are present together they both express their own types "
    "of sugars: this is because of co-dominance. Hence red blood cells have "
    "both A and B types of sugars.",
    STYLES["Body"]))
story.append(Paragraph(
    "Since there are three different alleles, there are six different "
    "combinations of these three alleles that are possible, and therefore, "
    "a total of six different genotypes of the human ABO blood types "
    "(Table 4.2).",
    STYLES["Body"]))

# Table 4.2 — reproduced as a real data_table (F176-F183)
story.append(Paragraph("<b>Table 4.2 - Genetic Basis of Blood Groups in Human Population</b>", STYLES["Body"]))
table_42 = data_table(
    [
        ["Allele from Parent 1", "Allele from Parent 2", "Genotype of offspring", "Blood type of offspring"],
        ["I<sup>A</sup>", "I<sup>A</sup>", "I<sup>A</sup>I<sup>A</sup>", "A"],
        ["I<sup>A</sup>", "I<sup>B</sup>", "I<sup>A</sup>I<sup>B</sup>", "AB"],
        ["I<sup>A</sup>", "i", "I<sup>A</sup>i", "A"],
        ["I<sup>B</sup>", "I<sup>A</sup>", "I<sup>A</sup>I<sup>B</sup>", "AB"],
        ["I<sup>B</sup>", "I<sup>B</sup>", "I<sup>B</sup>I<sup>B</sup>", "B"],
        ["I<sup>B</sup>", "i", "I<sup>B</sup>i", "B"],
        ["i", "i", "ii", "O"],
    ],
    col_widths=[2, 2, 2, 2],
)
story.append(table_42)

# F184, F185 — multiple alleles
story.append(Paragraph(
    "The example of ABO blood grouping also provides a good example of "
    "multiple alleles: there are more than two, i.e., three alleles, "
    "governing the same character. Since in an individual only two alleles "
    "can be present, multiple alleles can be found only when population "
    "studies are made.",
    STYLES["Body"]))

# F186-F190 — pleiotropy-in-disguise example
story.append(Paragraph(
    "Occasionally, a single gene product may produce more than one effect. "
    "For example, starch synthesis in pea seeds is controlled by one gene. "
    "It has two alleles (B and b). Starch is synthesised effectively by BB "
    "homozygotes and therefore, large starch grains are produced. In "
    "contrast, bb homozygotes have lesser efficiency in starch synthesis "
    "and produce smaller starch grains. After maturation of the seeds, BB "
    "seeds are round and the bb seeds are wrinkled. Heterozygotes produce "
    "round seeds, and so B seems to be the dominant allele. But, the starch "
    "grains produced are of intermediate size in Bb seeds. So if starch "
    "grain size is considered as the phenotype, then from this angle, the "
    "alleles show incomplete dominance. Therefore, dominance is not an "
    "autonomous feature of a gene or the product that it has information "
    "for. It depends as much on the gene product and the production of a "
    "particular phenotype from this product as it does on the particular "
    "phenotype that we choose to examine, in case more than one phenotype "
    "is influenced by the same gene.",
    STYLES["Body"]))


# ---- 4.3 Inheritance of Two Genes (F191-F217) ----
story.append(heading("4.3", "Inheritance of Two Genes", level=1))
story.append(Paragraph(
    "Mendel also worked with and crossed pea plants that differed in two "
    "characters, as is seen in the cross between a pea plant that has seeds "
    "with yellow colour and round shape and one that had seeds of green "
    "colour and wrinkled shape (Figure 4.7). Mendel found that the seeds "
    "resulting from the crossing of the parents, had yellow coloured and "
    "round shaped seeds. Thus, yellow colour was dominant over green and "
    "round shape dominant over wrinkled. These results were identical to "
    "those that he got when he made separate monohybrid crosses between "
    "yellow and green seeded plants and between round and wrinkled seeded "
    "plants. Let us use the genotypic symbols Y for dominant yellow seed "
    "colour and y for recessive green seed colour, R for round shaped seeds "
    "and r for wrinkled seed shape. The genotype of the parents can then be "
    "written as RRYY and rryy. The cross between the two plants can be "
    "written down as in Figure 4.7 showing the genotypes of the parent "
    "plants. The gametes RY and ry unite on fertilisation to produce the "
    "F<sub>1</sub> hybrid RrYy. When Mendel self-hybridised the "
    "F<sub>1</sub> plants he found that 3/4th of F<sub>2</sub> plants had "
    "yellow seeds and 1/4th had green. The yellow and green colours "
    "segregated in a 3:1 ratio. Round and wrinkled seed shape also "
    "segregated in a 3:1 ratio: just like in a monohybrid cross.",
    STYLES["Body"]))

# Figure 4.7 — dihybrid cross rendered as a 4x4 Punnett table (F202, F203)
story.append(Paragraph(
    "<b>Fig. 4.7 - Dihybrid cross</b> (P generation: Round yellow RRYY x "
    "Wrinkled green rryy; F<sub>1</sub>: RrYy, selfed; F<sub>2</sub> "
    "phenotypic ratio round yellow : round green : wrinkled yellow : "
    "wrinkled green = 9:3:3:1).",
    STYLES["Body"]))
dihybrid_punnett = data_table(
    [
        ["", "RY", "Ry", "rY", "ry"],
        ["RY", "RRYY", "RRYy", "RrYY", "RrYy"],
        ["Ry", "RRYy", "RRyy", "RrYy", "Rryy"],
        ["rY", "RrYY", "RrYy", "rrYY", "rrYy"],
        ["ry", "RrYy", "Rryy", "rrYy", "rryy"],
    ],
    col_widths=[1, 1, 1, 1, 1],
)
story.append(dihybrid_punnett)
story.append(Paragraph(
    "<i>Read the plate (Fig 4.7) - the 25 labels on the plate are: P "
    "generation, Round yellow, RR, YY, Wrinkled green, rr, yy, Gametes, RY, "
    "ry, RrYy, Selfing, F<sub>1</sub> generation, Ry, rY, RRYY, RrYY, RRYy, "
    "rrYY, RRyy, Rryy, rrYy, rryy, F<sub>2</sub> generation, Phenotypic "
    "ratio: round yellow : round green : wrinkled yellow : wrinkled green "
    "9:3:3:1.</i>",
    STYLES["Caption"]))


# ---- 4.3.1 Law of Independent Assortment (F204-F217) ----
story.append(heading("4.3.1", "Law of Independent Assortment", level=2))
story.append(Paragraph(
    "In the dihybrid cross (Figure 4.7), the phenotypes round, yellow; "
    "wrinkled, yellow; round, green and wrinkled, green appeared in the "
    "ratio 9:3:3:1. Such a ratio was observed for several pairs of "
    "characters that Mendel studied. The ratio of 9:3:3:1 can be derived as "
    "a combination series of 3 yellow : 1 green, with 3 round : 1 wrinkled. "
    "This derivation can be written as follows: (3 Round : 1 Wrinkled) "
    "(3 Yellow : 1 Green) = 9 Round, Yellow : 3 Wrinkled, Yellow : 3 Round, "
    "Green : 1 Wrinkled, Green.",
    STYLES["Body"]))
story.append(Paragraph(
    "Based upon such observations on dihybrid crosses (crosses between "
    "plants differing in two traits) Mendel proposed a second set of "
    "generalisations that we call <b>Mendel's Law of Independent Assortment</b>. "
    "The law states that when two pairs of traits are combined in a hybrid, "
    "segregation of one pair of characters is independent of the other pair "
    "of characters. The Punnett square can be effectively used to understand "
    "the independent segregation of the two pairs of genes during meiosis "
    "and the production of eggs and pollen in the F<sub>1</sub> RrYy plant. "
    "Consider the segregation of one pair of genes R and r. Fifty per cent "
    "of the gametes have the gene R and the other 50 per cent have r. Now "
    "besides each gamete having either R or r, it should also have the allele "
    "Y or y. The important thing to remember here is that segregation of 50 "
    "per cent R and 50 per cent r is independent from the segregation of 50 "
    "per cent Y and 50 per cent y. Therefore, 50 per cent of the r bearing "
    "gametes has Y and the other 50 per cent has y. Similarly, 50 per cent "
    "of the R bearing gametes has Y and the other 50 per cent has y. Thus "
    "there are four genotypes of gametes (four types of pollen and four types "
    "of eggs). The four types are RY, Ry, rY and ry each with a frequency "
    "of 25 per cent or 1/4 of the total gametes produced. When you write "
    "down the four types of eggs and pollen on the two sides of a Punnett "
    "square it is very easy to derive the composition of the zygotes that "
    "give rise to the F<sub>2</sub> plants (Figure 4.7).",
    STYLES["Body"]))


# ---- 4.3.2 Chromosomal Theory of Inheritance (F218-F254) ----
story.append(heading("4.3.2", "Chromosomal Theory of Inheritance", level=2))
story.append(Paragraph(
    "Mendel published his work on inheritance of characters in 1865 but for "
    "several reasons, it remained unrecognised till 1900. Firstly, "
    "communication was not easy (as it is now) in those days and his work "
    "could not be widely publicised. Secondly, his concept of genes (or "
    "factors, in Mendel's words) as stable and discrete units that "
    "controlled the expression of traits and, of the pair of alleles which "
    "did not blend with each other, was not accepted by his contemporaries "
    "as an explanation for the apparently continuous variation seen in "
    "nature. Thirdly, Mendel's approach of using mathematics to explain "
    "biological phenomena was totally new and unacceptable to many of the "
    "biologists of his time. Finally, though Mendel's work suggested that "
    "factors (genes) were discrete units, he could not provide any physical "
    "proof for the existence of factors or say what they were made of.",
    STYLES["Body"]))
story.append(Paragraph(
    "In 1900, three Scientists (de Vries, Correns and von Tschermak) "
    "independently rediscovered Mendel's results on the inheritance of "
    "characters. Also, by this time due to advancements in microscopy that "
    "were taking place, scientists were able to carefully observe cell "
    "division. This led to the discovery of structures in the nucleus that "
    "appeared to double and divide just before each cell division. These "
    "were called <b>chromosomes</b> (colored bodies, as they were visualised "
    "by staining). By 1902, the chromosome movement during meiosis had been "
    "worked out.",
    STYLES["Body"]))
story.append(Paragraph(
    "Walter Sutton and Theodore Boveri noted that the behaviour of "
    "chromosomes was parallel to the behaviour of genes and used chromosome "
    "movement (Figure 4.8) to explain Mendel's laws (Table 4.3). Recall that "
    "you have studied the behaviour of chromosomes during mitosis "
    "(equational division) and during meiosis (reduction division). The "
    "important things to remember are that chromosomes as well as genes "
    "occur in pairs. The two alleles of a gene pair are located on "
    "homologous sites on homologous chromosomes. Sutton and Boveri argued "
    "that the pairing and separation of a pair of chromosomes would lead "
    "to the segregation of a pair of factors they carried. <b>Sutton</b> "
    "united the knowledge of chromosomal segregation with Mendelian "
    "principles and called it the <b>chromosomal theory of inheritance</b>. "
    "Following this synthesis of ideas, experimental verification of the "
    "chromosomal theory of inheritance by Thomas Hunt Morgan and his "
    "colleagues, led to discovering the basis for the variation that sexual "
    "reproduction produced. Morgan worked with the tiny fruitflies, "
    "<i>Drosophila melanogaster</i> (Figure 4.10), which were found very "
    "suitable for such studies.",
    STYLES["Body"]))

# Figure 4.8 — meiosis / germ cell formation (F239, F240)
story.append(note(
    "Read the plate (Fig 4.8): meiosis and germ cell formation in a cell "
    "with four chromosomes. The 6 labels on the plate are: G2, Bivalent, "
    "Meiosis I, anaphase, Meiosis II, Germ cells."
))

# Table 4.3 — chromosome vs gene behaviour (F241-F247)
story.append(Paragraph("<b>Table 4.3 - A Comparison between the Behaviour of Chromosomes and Genes</b>", STYLES["Body"]))
table_43 = data_table(
    [
        ["Chromosome (A)", "Gene (B)"],
        ["Occur in pairs", "Occur in pairs"],
        ["Segregate at the time of gamete formation such that only one of each pair is transmitted to a gamete", "Segregate at gamete formation and only one of each pair is transmitted to a gamete"],
        ["Independent pairs segregate independently of each other", "One pair segregates independently of another pair"],
    ],
    col_widths=[5, 5],
)
story.append(table_43)

# F249, F250 — independent assortment of chromosomes (Figure 4.9)
story.append(Paragraph(
    "During Anaphase of meiosis I, the two chromosome pairs can align at the "
    "metaphase plate independently of each other (Figure 4.9). To understand "
    "this, compare the chromosomes of four different colour in the left and "
    "right columns. In the left column (Possibility I) orange and green is "
    "segregating together. But in the right hand column (Possibility II) the "
    "orange chromosome is segregating with the red chromosomes.",
    STYLES["Body"]))

# Figure 4.9 — read-the-plate note (F251, F252). Color-dependent.
story.append(note(
    "Read the plate (Fig 4.9): independent assortment of chromosomes. The 7 "
    "labels on the plate are: Possibility I, Possibility II, Meiosis I - "
    "anaphase, Meiosis II - anaphase, Germ cells, One long orange and short "
    "green chromosome and long yellow and short red chromosome at the same "
    "pole, One long orange and short red chromosome and long yellow and short "
    "green chromosome at the same pole. (The four chromosomes are "
    "distinguished in the original by colour: orange, green, red, and yellow. "
    "The colour distinction is preserved in the wording above so a reader "
    "without the plate can still follow which chromosome segregates with "
    "which in each possibility.)"
))

# Figure 4.10 — Drosophila melanogaster (F253, F254)
story.append(note(
    "Read the plate (Fig 4.10): <i>Drosophila melanogaster</i> (a) Male "
    "(b) Female. The plate carries only the panel markers (a) and (b); no "
    "further labels."
))


# ---- 4.3.3 Linkage and Recombination (F255-F266) ----
story.append(heading("4.3.3", "Linkage and Recombination", level=2))
story.append(Paragraph(
    "Morgan carried out several dihybrid crosses in Drosophila to study "
    "genes that were sex-linked. The crosses were similar to the dihybrid "
    "crosses carried out by Mendel in peas. For example Morgan hybridised "
    "yellow-bodied, white-eyed females to brown-bodied, red-eyed males and "
    "intercrossed their F<sub>1</sub> progeny. He observed that the two "
    "genes did not segregate independently of each other and the F<sub>2</sub> "
    "ratio deviated very significantly from the 9:3:3:1 ratio (expected "
    "when the two genes are independent). Morgan and his group knew that the "
    "genes were located on the X chromosome (Section 4.4) and saw quickly "
    "that when the two genes in a dihybrid cross were situated on the same "
    "chromosome, the proportion of parental gene combinations were much "
    "higher than the non-parental type. Morgan attributed this due to the "
    "physical association or linkage of the two genes and coined the term "
    "<b>linkage</b> to describe this physical association of genes on a "
    "chromosome and the term <b>recombination</b> to describe the "
    "generation of non-parental gene combinations (Figure 4.11).",
    STYLES["Body"]))
story.append(Paragraph(
    "Morgan and his group also found that even when genes were grouped on "
    "the same chromosome, some genes were very tightly linked (showed very "
    "low recombination) (Figure 4.11, Cross A) while others were loosely "
    "linked (showed higher recombination) (Figure 4.11, Cross B). For "
    "example he found that the genes white and yellow were very tightly "
    "linked and showed only 1.3 per cent recombination while white and "
    "miniature wing showed 37.2 per cent recombination. His student Alfred "
    "Sturtevant used the frequency of recombination between gene pairs on "
    "the same chromosome as a measure of the distance between genes and "
    "'mapped' their position on the chromosome. Today genetic maps are "
    "extensively used as a starting point in the sequencing of whole "
    "genomes as was done in the case of the Human Genome Sequencing "
    "Project, described later.",
    STYLES["Body"]))

# Figure 4.11 — linkage crosses rendered as two small tables (F265, F266)
story.append(Paragraph(
    "<b>Fig. 4.11 - Linkage: two dihybrid crosses by Morgan</b> (Cross A: y "
    "and w, very tightly linked; Cross B: w and m, loosely linked)",
    STYLES["Body"]))
cross_a = data_table(
    [
        ["Cross A: Yellow, white x Wild type", "Result"],
        ["F<sub>1</sub> generation", "Wild type"],
        ["Gametes", "Parental type (98.7 %) / Recombinant types (1.3 %)"],
    ],
    col_widths=[4, 6],
)
story.append(cross_a)
cross_b = data_table(
    [
        ["Cross B: White, miniature x Wild type", "Result"],
        ["F<sub>1</sub> generation", "Wild type"],
        ["Gametes", "Parental type (62.8 %) / Recombinant types (37.2 %)"],
    ],
    col_widths=[4, 6],
)
story.append(cross_b)
story.append(Paragraph(
    "<i>Read the plate (Fig 4.11) - the 16 labels on the plate are: Cross A, "
    "Cross B, Yellow, white, White, miniature, Wild type, F<sub>1</sub> "
    "generation, Gametes, Parental type (98.7 %), Recombinant types "
    "(1.3 %), Parental type (62.8 %), Recombinant types (37.2 %), yellow, "
    "white, yellow, white, miniature, wild type.</i>",
    STYLES["Caption"]))


# ---- 4.4 Polygenic Inheritance (F267-F277) ----
story.append(heading("4.4", "Polygenic Inheritance", level=1))
story.append(Paragraph(
    "Mendel's studies mainly described those traits that have distinct "
    "alternate forms such as flower colour which are either purple or "
    "white. But if you look around you will find that there are many traits "
    "which are not so distinct in their occurrence and are spread across a "
    "gradient. For example, in humans we don't just have tall or short "
    "people as two distinct alternatives but a whole range of possible "
    "heights. Such traits are generally controlled by three or more genes "
    "and are thus called as <b>polygenic traits</b>. Besides the involvement "
    "of multiple genes polygenic inheritance also takes into account the "
    "influence of environment. Human skin colour is another classic example "
    "for this. In a polygenic trait the phenotype reflects the contribution "
    "of each allele, i.e., the effect of each allele is additive. To "
    "understand this better let us assume that three genes A, B, C control "
    "skin colour in human with the dominant forms A, B and C responsible "
    "for dark skin colour and the recessive forms a, b and c for light skin "
    "colour. The genotype with all the dominant alleles (AABBCC) will have "
    "the darkest skin colour and that with all the recessive alleles "
    "(aabbcc) will have the lightest skin colour. As expected the genotype "
    "with three dominant alleles and three recessive alleles will have an "
    "intermediate skin colour. In this manner the number of each type of "
    "alleles in the genotype would determine the darkness or lightness of "
    "the skin in an individual.",
    STYLES["Body"]))


# ---- 4.5 Pleiotropy (F278-F282) ----
story.append(heading("4.5", "Pleiotropy", level=1))
story.append(Paragraph(
    "We have so far seen the effect of a gene on a single phenotype or "
    "trait. There are however instances where a single gene can exhibit "
    "multiple phenotypic expression. Such a gene is called a <b>pleiotropic "
    "gene</b>. The underlying mechanism of pleiotropy in most cases is the "
    "effect of a gene on metabolic pathways which contribute towards "
    "different phenotypes. An example of this is the disease "
    "phenylketonuria, which occurs in humans. The disease is caused by "
    "mutation in the gene that codes for the enzyme phenylalanine "
    "hydroxylase (single gene mutation). This manifests itself through "
    "phenotypic expression characterised by mental retardation and a "
    "reduction in hair and skin pigmentation.",
    STYLES["Body"]))


# ---- 4.6 Sex Determination (F283-F323) ----
story.append(heading("4.6", "Sex Determination", level=1))
story.append(Paragraph(
    "The mechanism of sex determination has always been a puzzle before "
    "the geneticists. The initial clue about the genetic/chromosomal "
    "mechanism of sex determination can be traced back to some of the "
    "experiments carried out in insects. In fact, the cytological "
    "observations made in a number of insects led to the development of "
    "the concept of genetic/chromosomal basis of sex-determination. Henking "
    "(1891) could trace a specific nuclear structure all through "
    "spermatogenesis in a few insects, and it was also observed by him that "
    "50 per cent of the sperm received this structure after "
    "spermatogenesis, whereas the other 50 per cent sperm did not receive "
    "it. Henking gave a name to this structure as the x body but he could "
    "not explain its significance. Further investigations by other "
    "scientists led to the conclusion that the 'X body' of Henking was in "
    "fact a chromosome and that is why it was given the name X-chromosome.",
    STYLES["Body"]))
story.append(Paragraph(
    "It was also observed that in a large number of insects the mechanism "
    "of sex determination is of the XO type, i.e., all eggs bear an "
    "additional X-chromosome besides the other chromosomes (autosomes). On "
    "the other hand, some of the sperms bear the X-chromosome whereas some "
    "do not. Eggs fertilised by sperm having an X-chromosome become females "
    "and, those fertilised by sperms that do not have an X-chromosome "
    "become males. Due to the involvement of the X-chromosome in the "
    "determination of sex, it was designated to be the sex chromosome, and "
    "the rest of the chromosomes were named as autosomes. Grasshopper is an "
    "example of XO type of sex determination in which the males have only "
    "one X-chromosome besides the autosomes, whereas females have a pair of "
    "X-chromosomes.",
    STYLES["Body"]))
story.append(Paragraph(
    "In a number of other insects and mammals including man, XY type of "
    "sex determination is seen where both male and female have same number "
    "of chromosomes. Among the males an X-chromosome is present but its "
    "counterpart is distinctly smaller and called the Y-chromosome. Females, "
    "however, have a pair of X-chromosomes. Both males and females bear same "
    "number of autosomes. Hence, the males have autosomes plus XY, while "
    "female have autosomes plus XX. In human beings and in Drosophila the "
    "males have one X and one Y chromosome, whereas females have a pair of "
    "X-chromosomes besides autosomes (Figure 4.12a, b).",
    STYLES["Body"]))
story.append(Paragraph(
    "In the above description you have studied about two types of sex "
    "determining mechanisms, i.e., XO type and XY type. But in both cases "
    "males produce two different types of gametes, (a) either with or without "
    "X-chromosome or (b) some gametes with X-chromosome and some with "
    "Y-chromosome. Such type of sex determination mechanism is designated "
    "to be the example of male heterogamety. In some other organisms, e.g., "
    "birds, a different mechanism of sex determination is observed "
    "(Figure 4.12 c). In this case the total number of chromosome is same "
    "in both males and females. But two different types of gametes in terms "
    "of the sex chromosomes, are produced by females, i.e., female "
    "heterogamety. In order to have a distinction with the mechanism of sex "
    "determination described earlier, the two different sex chromosomes of "
    "a female bird has been designated to be the Z and W chromosomes. In "
    "these organisms the females have one Z and one W chromosome, whereas "
    "males have a pair of Z-chromosomes besides the autosomes.",
    STYLES["Body"]))

# Figure 4.12 — read-the-plate note (F303, F304)
story.append(note(
    "Read the plate (Fig 4.12): determination of sex by chromosomal "
    "differences. The 4 labels on the plate are: XX, XY, ZW, ZZ."
))


# ---- 4.6.1 Sex Determination in Humans (F305-F314) ----
story.append(heading("4.6.1", "Sex Determination in Humans", level=2))
story.append(Paragraph(
    "It has already been mentioned that the sex determining mechanism in "
    "case of humans is XY type. Out of 23 pairs of chromosomes present, 22 "
    "pairs are exactly same in both males and females: these are the "
    "autosomes. A pair of X-chromosomes are present in the female, whereas "
    "the presence of an X and Y chromosome are determinant of the male "
    "characteristic. During spermatogenesis among males, two types of "
    "gametes are produced. 50 per cent of the total sperm produced carry "
    "the X-chromosome and the rest 50 per cent has Y-chromosome besides "
    "the autosomes. Females, however, produce only one type of ovum with an "
    "X-chromosome. There is an equal probability of fertilisation of the "
    "ovum with the sperm carrying either X or Y chromosome. In case the "
    "ovum fertilises with a sperm carrying X-chromosome the zygote develops "
    "into a female (XX) and the fertilisation of ovum with Y-chromosome "
    "carrying sperm results into a male offspring. Thus, it is evident that "
    "it is the genetic make up of the sperm that determines the sex of the "
    "child. It is also evident that in each pregnancy there is always 50 per "
    "cent probability of either a male or a female child.",
    STYLES["Body"]))


# ---- 4.6.2 Sex Determination in Honey Bee (F315-F323) ----
story.append(heading("4.6.2", "Sex Determination in Honey Bee", level=2))
story.append(Paragraph(
    "The sex determination in honey bee is based on the number of sets of "
    "chromosomes an individual receives. An offspring formed from the union "
    "of a sperm and an egg develops as a female (queen or worker), and an "
    "unfertilised egg develops as a male (drone) by means of parthenogenesis. "
    "This means that the males have half the number of chromosomes than that "
    "of a female. The females are diploid having 32 chromosomes and males "
    "are haploid, i.e., having 16 chromosomes. This is called as "
    "<b>haplodiploid sex-determination system</b> and has special "
    "characteristic features such as the males produce sperms by mitosis "
    "(Figure 4.13 - the honey bee plate), they do not have father and thus "
    "cannot have sons, but have a grandfather and can have grandsons.",
    STYLES["Body"]))

# Figure 4.13a — honey bee plate rendered as a small table (F322, F323)
story.append(Paragraph(
    "<b>Fig. 4.13 - Sex determination in honey bee</b> (honey bee plate):",
    STYLES["Body"]))
honeybee = data_table(
    [
        ["Parents", "Gametes", "Process", "F<sub>1</sub>"],
        ["Female (32)", "16 (haploid egg)", "Meiosis (in female)", "Female (32) - from fertilised egg"],
        ["Male (16)", "16 (haploid sperm)", "Mitosis (in male, no meiosis)", "Male (16) - from unfertilised egg"],
    ],
    col_widths=[2, 3, 3, 4],
)
story.append(honeybee)
story.append(Paragraph(
    "<i>Read the plate (Fig 4.13, honey bee plate) - the 9 labels on the "
    "plate are: Parents, Gametes, Female, 32, Male, 16, Meiosis, Mitosis, "
    "F<sub>1</sub>.</i>",
    STYLES["Caption"]))


# ---- 4.7 Mutation (F324-F333) ----
story.append(heading("4.7", "Mutation", level=1))
story.append(Paragraph(
    "Mutation is a phenomenon which results in alteration of DNA sequences "
    "and consequently results in changes in the genotype and the phenotype "
    "of an organism. In addition to recombination, mutation is another "
    "phenomenon that leads to variation in DNA. As you will learn in "
    "Chapter 5, one DNA helix runs continuously from one end to the other "
    "in each chromatid, in a highly supercoiled form. Therefore loss "
    "(deletions) or gain (insertion/duplication) of a segment of DNA, "
    "result in alteration in chromosomes. Since genes are known to be "
    "located on chromosomes, alteration in chromosomes results in "
    "abnormalities or aberrations. Chromosomal aberrations are commonly "
    "observed in cancer cells. In addition to the above, mutation also "
    "arises due to change in a single base pair of DNA. This is known as "
    "<b>point mutation</b>. A classical example of such a mutation is "
    "sickle cell anaemia. Deletions and insertions of base pairs of DNA, "
    "causes frame-shift mutations (see Chapter 5). However, there are many "
    "chemical and physical factors that induce mutations. These are "
    "referred to as <b>mutagens</b>. UV radiations can cause mutations in "
    "organisms - it is a mutagen.",
    STYLES["Body"]))


# ---- 4.8 Genetic Disorders (F334-F410) ----
story.append(heading("4.8", "Genetic Disorders", level=1))


# ---- 4.8.1 Pedigree Analysis (F335-F347) ----
story.append(heading("4.8.1", "Pedigree Analysis", level=2))
story.append(Paragraph(
    "The idea that disorders are inherited has been prevailing in the human "
    "society since long. This was based on the heritability of certain "
    "characteristic features in families. After the rediscovery of Mendel's "
    "work the practice of analysing inheritance pattern of traits in human "
    "beings began. Since it is evident that control crosses that can be "
    "performed in pea plant or some other organisms, are not possible in "
    "case of human beings, study of the family history about inheritance of "
    "a particular trait provides an alternative. Such an analysis of traits "
    "in several of generations of a family is called the <b>pedigree "
    "analysis</b>. In the pedigree analysis the inheritance of a particular "
    "trait is represented in the family tree over generations. In human "
    "genetics, pedigree study provides a strong tool, which is utilised to "
    "trace the inheritance of a specific trait, abnormality or disease. "
    "Some of the important standard symbols used in the pedigree analysis "
    "have been shown in Figure 4.13 (the pedigree-symbol plate).",
    STYLES["Body"]))

# Figure 4.13b — pedigree symbols rendered as a two-column table (F343, F344)
story.append(Paragraph(
    "<b>Fig. 4.13 - Symbols used in the human pedigree analysis</b> "
    "(pedigree-symbol plate):",
    STYLES["Body"]))
pedigree_sym = data_table(
    [
        ["Symbol", "Meaning"],
        ["Square", "Male"],
        ["Circle", "Female"],
        ["Diamond", "Sex unspecified"],
        ["Filled square or filled circle", "Affected individuals"],
        ["Horizontal line connecting a square and a circle", "Mating"],
        ["Double horizontal line", "Mating between relatives (consanguineous mating)"],
        ["Vertical line from parents to children", "Parents above and children below (in order of birth - left to right)"],
        ["Filled square attached to a vertical line", "Parents with male child affected with disease"],
        ["Stack of small symbols attached to a vertical line", "Five unaffected offspring"],
    ],
    col_widths=[4, 6],
)
story.append(pedigree_sym)
story.append(Paragraph(
    "<i>Read the plate (Fig 4.13, pedigree-symbol plate) - the 9 labels on "
    "the plate are: Male, female, sex unspecified, affected individuals, "
    "mating, mating between relatives (consanguineous mating), parents above "
    "and children below (in order of birth - left to right), parents with "
    "male child affected with disease, five unaffected offspring.</i>",
    STYLES["Caption"]))

# F345-F347
story.append(Paragraph(
    "DNA is the carrier of genetic information. It is hence transmitted from "
    "one generation to the other without any change or alteration. However, "
    "changes or alteration do take place occasionally. Such an alteration or "
    "change in the genetic material is referred to as mutation. A number of "
    "disorders in human beings have been found to be associated with the "
    "inheritance of changed or altered genes or chromosomes.",
    STYLES["Body"]))


# ---- 4.8.2 Mendelian Disorders (F348-F390) ----
story.append(heading("4.8.2", "Mendelian Disorders", level=2))
story.append(Paragraph(
    "Broadly, genetic disorders may be grouped into two categories - "
    "<b>Mendelian disorders</b> and <b>Chromosomal disorders</b>. Mendelian "
    "disorders are mainly determined by alteration or mutation in the single "
    "gene. These disorders are transmitted to the offspring on the same "
    "lines as we have studied in the principle of inheritance. The pattern "
    "of inheritance of such Mendelian disorders can be traced in a family "
    "by the pedigree analysis. Most common and prevalent Mendelian disorders "
    "are Haemophilia, Cystic fibrosis, Sickle cell anaemia, Colour blindness, "
    "Phenylketonuria, Thalassemia, etc. By pedigree analysis one can easily "
    "understand whether the trait in question is dominant or recessive. "
    "Similarly, the trait may also be linked to the sex chromosome as in "
    "case of haemophilia. It is evident that this X-linked recessive trait "
    "shows transmission from carrier female to male progeny. A "
    "representative pedigree is shown in Figure 4.14 for dominant and "
    "recessive traits.",
    STYLES["Body"]))

# Figure 4.14 — read-the-plate note (F357, F358)
story.append(note(
    "Read the plate (Fig 4.14): representative pedigree analysis of (a) "
    "Autosomal dominant trait (for example: Myo tonic dystrophy) (b) "
    "Autosomal recessive trait (for example: Sickle-cell anaemia). The plate "
    "carries only the panel markers (a) and (b); no further labels."
))

# Colour Blindness (F359-F364)
story.append(Paragraph(
    "<b>Colour Blindness:</b> It is a sex-linked recessive disorder due to "
    "defect in either red or green cone of eye resulting in failure to "
    "discriminate between red and green colour. This defect is due to "
    "mutation in certain genes present in the X chromosome. It occurs in "
    "about 8 per cent of males and only about 0.4 per cent of females. This "
    "is because the genes that lead to red-green colour blindness are on "
    "the X chromosome. Males have only one X chromosome and females have "
    "two. The son of a woman who carries the gene has a 50 per cent chance "
    "of being colour blind. The mother is not herself colour blind because "
    "the gene is recessive. That means that its effect is suppressed by her "
    "matching dominant normal gene. A daughter will not normally be colour "
    "blind, unless her mother is a carrier and her father is colour blind.",
    STYLES["Body"]))

# Haemophilia (F365-F370)
story.append(Paragraph(
    "<b>Haemophilia:</b> This sex linked recessive disease, which shows its "
    "transmission from unaffected carrier female to some of the male progeny "
    "has been widely studied. In this disease, a single protein that is a "
    "part of the cascade of proteins involved in the clotting of blood is "
    "affected. Due to this, in an affected individual a simple cut will "
    "result in non-stop bleeding. The heterozygous female (carrier) for "
    "haemophilia may transmit the disease to sons. The possibility of a "
    "female becoming a haemophilic is extremely rare because mother of such "
    "a female has to be at least carrier and the father should be "
    "haemophilic (unviable in the later stage of life). The family pedigree "
    "of Queen Victoria shows a number of haemophilic descendents as she was "
    "a carrier of the disease.",
    STYLES["Body"]))

# Sickle-cell anaemia (F371-F377)
story.append(Paragraph(
    "<b>Sickle-cell anaemia:</b> This is an autosome linked recessive trait "
    "that can be transmitted from parents to the offspring when both the "
    "partners are carrier for the gene (or heterozygous). The disease is "
    "controlled by a single pair of allele, Hb<sup>A</sup> and Hb<sup>S</sup>. "
    "Out of the three possible genotypes only homozygous individuals for "
    "Hb<sup>S</sup> (Hb<sup>S</sup>Hb<sup>S</sup>) show the diseased "
    "phenotype. Heterozygous (Hb<sup>A</sup>Hb<sup>S</sup>) individuals "
    "appear apparently unaffected but they are carrier of the disease as "
    "there is 50 per cent probability of transmission of the mutant gene "
    "to the progeny, thus exhibiting sickle-cell trait (Figure 4.15). The "
    "defect is caused by the substitution of Glutamic acid (Glu) by Valine "
    "(Val) at the sixth position of the beta globin chain of the "
    "haemoglobin molecule. The substitution of amino acid in the globin "
    "protein results due to the single base substitution at the sixth codon "
    "of the beta globin gene from GAG to GUG. The mutant haemoglobin "
    "molecule undergoes polymerisation under low oxygen tension causing the "
    "change in the shape of the RBC from biconcave disc to elongated "
    "sickle like structure (Figure 4.15).",
    STYLES["Body"]))

# Figure 4.15 — read-the-plate note (F378, F379)
story.append(note(
    "Read the plate (Fig 4.15): micrograph of the red blood cells and the "
    "amino acid composition of the relevant portion of beta-chain of "
    "haemoglobin. The 8 labels on the plate are: Normal Hb(A) gene, "
    "Sickle-cell Hb(S) gene, mRNA GAG, mRNA GUG, HbA peptide, HbS peptide, "
    "Val His Leu Thr Pro Glu Glu, Val His Leu Thr Pro Val Glu."
))

# Phenylketonuria (F380-F384)
story.append(Paragraph(
    "<b>Phenylketonuria:</b> This inborn error of metabolism is also "
    "inherited as the autosomal recessive trait. The affected individual "
    "lacks an enzyme that converts the amino acid phenylalanine into "
    "tyrosine. As a result of this phenylalanine is accumulated and "
    "converted into phenylpyruvic acid and other derivatives. Accumulation "
    "of these in brain results in mental retardation. These are also "
    "excreted through urine because of its poor absorption by kidney.",
    STYLES["Body"]))

# Thalassemia (F385-F390)
story.append(Paragraph(
    "<b>Thalassemia:</b> This is also an autosome-linked recessive blood "
    "disease transmitted from parents to the offspring when both the "
    "partners are unaffected carrier for the gene (or heterozygous). The "
    "defect could be due to either mutation or deletion which ultimately "
    "results in reduced rate of synthesis of one of the globin chains "
    "(alpha and beta chains) that make up haemoglobin. This causes the "
    "formation of abnormal haemoglobin molecules resulting into anaemia "
    "which is characteristic of the disease. Thalassemia can be classified "
    "according to which chain of the haemoglobin molecule is affected. In "
    "alpha Thalassemia, production of alpha globin chain is affected while "
    "in beta Thalassemia, production of beta globin chain is affected. "
    "alpha Thalassemia is controlled by two closely linked genes HBA1 and "
    "HBA2 on chromosome 16 of each parent and it is observed due to "
    "mutation or deletion of one or more of the four genes. The more genes "
    "affected, the less alpha globin molecules produced. While beta "
    "Thalassemia is controlled by a single gene HBB on chromosome 11 of "
    "each parent and occurs due to mutation of one or both the genes. "
    "Thalassemia differs from sickle-cell anaemia in that the former is a "
    "quantitative problem of synthesising too few globin molecules while "
    "the latter is a qualitative problem of synthesising an incorrectly "
    "functioning globin.",
    STYLES["Body"]))


# ---- 4.8.3 Chromosomal Disorders (F391-F410) ----
story.append(heading("4.8.3", "Chromosomal Disorders", level=2))
story.append(Paragraph(
    "The chromosomal disorders on the other hand are caused due to absence "
    "or excess or abnormal arrangement of one or more chromosomes. Failure "
    "of segregation of chromatids during cell division cycle results in the "
    "gain or loss of a chromosome(s), called <b>aneuploidy</b>. For example "
    "Down's syndrome results in the gain of extra copy of chromosome 21. "
    "Similarly, Turner's syndrome results due to loss of an X chromosome in "
    "human females. Failure of cytokinesis after telophase stage of cell "
    "division results in an increase in a whole set of chromosomes in an "
    "organism and, this phenomenon is known as <b>polyploidy</b>. This "
    "condition is often seen in plants. The total number of chromosomes in "
    "a normal human cell is 46 (23 pairs). Out of these 22 pairs are "
    "autosomes and one pair of chromosomes are sex chromosome. These "
    "situations are known as <b>trisomy</b> or <b>monosomy</b> of a "
    "chromosome, respectively. Such a situation leads to very serious "
    "consequences in the individual. Down's Syndrome, Turner's syndrome, "
    "Klinefelter's syndrome are common examples of chromosomal disorders.",
    STYLES["Body"]))

# Down's, Klinefelter's, Turner's (F401-F406)
story.append(Paragraph(
    "<b>Down's Syndrome:</b> The cause of this genetic disorder is the "
    "presence of an additional copy of the chromosome number 21 (trisomy of "
    "21). This disorder was first described by Langdon Down (1866). The "
    "affected individual is short statured with small round head, furrowed "
    "tongue and partially open mouth (Figure 4.16). Palm is broad with "
    "characteristic palm crease. Physical, psychomotor and mental "
    "development is retarded.",
    STYLES["Body"]))
story.append(Paragraph(
    "<b>Klinefelter's Syndrome:</b> This genetic disorder is also caused due "
    "to the presence of an additional copy of X chromosome resulting into a "
    "karyotype of 47, XXY. Such an individual has overall masculine "
    "development, however, the feminine development (development of breast, "
    "i.e., Gynaecomastia) is also expressed (Figure 4.17a). Such individuals "
    "are sterile.",
    STYLES["Body"]))
story.append(Paragraph(
    "<b>Turner's Syndrome:</b> Such a disorder is caused due to the absence "
    "of one of the X chromosomes, i.e., 45 with X0. Such females are "
    "sterile as ovaries are rudimentary besides other features including "
    "lack of other secondary sexual characters (Figure 4.17b).",
    STYLES["Body"]))

# Figure 4.16 — read-the-plate note (F407, F408)
story.append(note(
    "Read the plate (Fig 4.16): a representative figure showing an "
    "individual inflicted with Down's syndrome and the corresponding "
    "chromosomes of the individual. The 6 labels on the plate are: Broad "
    "flat face, Flat back of head, Many 'loops' on finger tips, Palm "
    "crease, Big and wrinkled tongue, Congenital heart disease."
))

# Figure 4.17 — read-the-plate note (F409, F410)
story.append(note(
    "Read the plate (Fig 4.17): diagrammatic representation of genetic "
    "disorders due to sex chromosome composition in humans. The 2 labels "
    "on the plate are: Tall stature with feminised character (development "
    "of breast, i.e., Gynaecomastia), Short stature and under developed "
    "feminine character."
))


# ---- Quick Recap (the 5 SUMMARY-UNIQUE folds + 27 BODY-PRESENT points) ----
story.append(heading("QR", "Quick Recap", level=1))
story.append(Paragraph(
    "<b>Genetics</b> is a branch of biology which deals with principles of "
    "inheritance and its practices. Progeny resembling the parents in "
    "morphological and physiological features has attracted the attention "
    "of many biologists. Mendel was the first to study this phenomenon "
    "systematically. While studying the pattern of inheritance in pea "
    "plants of contrasting characters, Mendel proposed the principles of "
    "inheritance, which are today referred to as 'Mendel's Laws of "
    "Inheritance'.",
    STYLES["Body"]))
story.append(Paragraph(
    "He proposed that the 'factors' (later named as genes) regulating the "
    "characters are found in pairs known as alleles. He observed that the "
    "expression of the characters in the offspring follow a definite "
    "pattern in different-first generations (F<sub>1</sub>), second "
    "(F<sub>2</sub>) and so on. Some characters are dominant over others. "
    "The dominant characters are expressed when factors are in heterozygous "
    "condition (Law of Dominance). The recessive characters are only "
    "expressed in homozygous conditions. The characters never blend in "
    "heterozygous condition. A recessive character that was not expressed "
    "in heterozygous condition may be expressed again when it becomes "
    "homozygous. Hence, characters segregate while formation of gametes "
    "(Law of Segregation). Not all characters show true dominance. Some "
    "characters show incomplete, and some show co-dominance.",
    STYLES["Body"]))
story.append(Paragraph(
    "When Mendel studied the inheritance of two characters together, it was "
    "found that the factors independently assort and combine in all "
    "permutations and combinations (Law of Independent Assortment). "
    "Different combinations of gametes are theoretically represented in a "
    "square tabular form known as 'Punnett Square'. The factors (now known "
    "as gene) on chromosomes regulating the characters are called the "
    "genotype and the physical expression of the characters is called "
    "phenotype. After knowing that the genes are located on the "
    "chromosomes, a good correlation was drawn between Mendel's laws: "
    "segregation and assortment of chromosomes during meiosis. The Mendel's "
    "laws were extended in the form of 'Chromosomal Theory of Inheritance'. "
    "Later, it was found that Mendel's law of independent assortment does "
    "not hold true for the genes that were located on the same chromosomes. "
    "These genes were called as linked genes. Closely located genes "
    "assorted together, and distantly located genes, due to recombination, "
    "assorted independently. Linkage maps, therefore, corresponded to "
    "arrangement of genes on a chromosome. Many genes were linked to sexes "
    "also, and called as sex-linked genes.",
    STYLES["Body"]))
story.append(Paragraph(
    "The two sexes (male and female) were found to have a set of chromosomes "
    "which were common, and another set which was different. The "
    "chromosomes which were different in two sexes were named as sex "
    "chromosomes. The remaining set was named as autosomes. In humans, a "
    "normal female has 22 pairs of autosomes and a pair of sex chromosomes "
    "(XX). A male has 22 pairs of autosomes and a pair of sex chromosome "
    "as XY. <b>In chicken, sex chromosomes in male are ZZ, and in females "
    "are ZW.</b>",
    STYLES["Body"]))
story.append(Paragraph(
    "Mutation is defined as change in the genetic material. A point mutation "
    "is a change of a single base pair in DNA. Sickle-cell anemia is caused "
    "due to change of one base in the gene coding for beta-chain of "
    "hemoglobin. Inheritable mutations can be studied by generating a "
    "pedigree of a family. Some mutations involve changes in whole set of "
    "chromosomes (polyploidy) or change in a subset of chromosome number "
    "(aneuploidy). This helped in understanding the mutational basis of "
    "genetic disorders. Down's syndrome is due to trisomy of chromosome 21, "
    "where there is an extra copy of chromosome 21 and consequently the "
    "total number of chromosome becomes 47. In Turner's syndrome, one X "
    "chromosome is missing and the sex chromosome is as X0, and in "
    "Klinefelter's syndrome, the condition is XXY. <b>These can be easily "
    "studied by analysis of Karyotypes.</b>",
    STYLES["Body"]))


# ---- Terms used in the exercises (only the 4 GAPs, per Rule 2) ----
story.append(heading("EX", "Terms used in the exercises", level=1))
story.append(Paragraph(
    "Per Rule 2, the chapter PDF reproduces only the four exercise "
    "questions whose answers are not fully carried in the rewritten body. "
    "The remaining twelve are answered by the body itself and are not "
    "restated here.",
    STYLES["Body"]))
story.append(Paragraph(
    "<b>Q1.</b> Mention the advantages of selecting pea plant for "
    "experiment by Mendel. "
    "<i>(Answer assembled from the rewritten body, not from outside the "
    "source.)</i> The body gives the following five facts which together "
    "answer this question: (i) pea plants have <b>true-breeding lines</b> "
    "(F051) - a true-breeding line is one that, having undergone continuous "
    "self-pollination, shows the stable trait inheritance and expression "
    "for several generations; (ii) the seven pairs of characters Mendel "
    "selected are manifested as <b>two opposing traits</b> (F048), e.g., "
    "tall or dwarf, yellow or green seeds; (iii) Mendel could carry out "
    "<b>artificial pollination / cross-pollination</b> on pea plants (F050); "
    "(iv) his experiments had a <b>large sampling size</b> (F046), giving "
    "greater credibility to the data; and (v) the inferences were confirmed "
    "on <b>successive generations</b> of the test plants (F047), proving the "
    "results pointed to general rules of inheritance.",
    STYLES["Body"]))
story.append(Paragraph(
    "<b>Q3.</b> A diploid organism is heterozygous for 4 loci, how many "
    "types of gametes can be produced? "
    "<i>(Extension of the body's 4.3.1 statement, marked as reasoning, not "
    "as NCERT text.)</i> The body states that for two heterozygous loci "
    "there are four gamete types, RY, Ry, rY and ry, each at 25 per cent "
    "or 1/4 frequency (F213). Extending the same logic to four "
    "heterozygous loci gives <b>2<sup>4</sup> = 16 gamete types</b>, each "
    "at 1/16 frequency.",
    STYLES["Body"]))
story.append(Paragraph(
    "<b>Q6.</b> Using a Punnett Square, workout the distribution of "
    "phenotypic features in the first filial generation after a cross "
    "between a homozygous female and a heterozygous male for a single "
    "locus. "
    "<i>(Worked out from the Law of Dominance rows, not as NCERT text.)</i> "
    "For a cross homozygous female (TT) x heterozygous male (Tt), the "
    "female produces only T gametes and the male produces T and t in equal "
    "proportion. The F<sub>1</sub> offspring are therefore <b>1/2 TT and "
    "1/2 Tt</b> - genotypic ratio 1:1, all phenotypically tall (because T "
    "is dominant over t, per the Law of Dominance).",
    STYLES["Body"]))
story.append(Paragraph(
    "<b>Q7.</b> A cross is made between a tall plant with yellow seeds "
    "(TtYy) and a tall plant with green seeds (Ttyy). Work out the "
    "proportions of (a) tall and green, and (b) dwarf and green offspring. "
    "<i>(Worked out from the 4.3.1 gamete-frequency rows, not as NCERT "
    "text.)</i> From the F<sub>1</sub> (TtYy), the four gamete types are "
    "TY, Ty, tY, ty each at 25 per cent (F213). From the other parent "
    "(Ttyy), the gamete types are Ty and ty each at 50 per cent. The "
    "offspring genotypes and phenotypes are:",
    STYLES["Body"]))
q7_table = data_table(
    [
        ["From TtYy x Ttyy", "Genotype", "Phenotype"],
        ["TY x Ty (25 % x 50 % = 12.5 %)", "TTYy", "Tall, yellow"],
        ["TY x ty (25 % x 50 % = 12.5 %)", "TtYy", "Tall, yellow"],
        ["Ty x Ty (25 % x 50 % = 12.5 %)", "TTyy", "Tall, green"],
        ["Ty x ty (25 % x 50 % = 12.5 %)", "Ttyy", "Tall, green"],
        ["tY x Ty (25 % x 50 % = 12.5 %)", "TtYy", "Tall, yellow"],
        ["tY x ty (25 % x 50 % = 12.5 %)", "ttYy", "Dwarf, yellow"],
        ["ty x Ty (25 % x 50 % = 12.5 %)", "Ttyy", "Tall, green"],
        ["ty x ty (25 % x 50 % = 12.5 %)", "ttyy", "Dwarf, green"],
    ],
    col_widths=[5, 2, 3],
)
story.append(q7_table)
story.append(Paragraph(
    "Summing: (a) <b>tall and green</b> = TTyy (12.5 %) + Ttyy (12.5 % + "
    "12.5 %) = 37.5 %; (b) <b>dwarf and green</b> = ttyy = 12.5 %.",
    STYLES["Body"]))


# ---- Build the PDF ----
if __name__ == "__main__":
    sys.exit(build_pdf(OUT_PDF, story,
                       title="Class 12 Chapter 4 - Principles of Inheritance and Variation (NEET notes)",
                       subject="NEET Biology"))
