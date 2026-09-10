# -*- coding: utf-8 -*-
"""Pass-1 rows, part A — source pages 1-7 (unit opener, profiles, chapter
opener, 4.1, 4.2 up to the Punnett square).

Every row is (section, type, wording).  IDs are assigned F001..Fnnn by the
builder so the table can never end up with a gap or a duplicate.

Wording rules used throughout this file:
  * subscripts are written flat (F1, F2, HbA, HbS) — the PDF will use
    <sub>/<super> tags, check_pdf.py's banned-glyph check forbids the Unicode
    forms;
  * Greek letters are spelled out (beta) so check 5 cannot fire;
  * NCERT's own spellings and its oddities are preserved verbatim
    ("Kombergs" appears only in OCR — see the note in the inventory).
"""

ROWS = [
    # ---------------------------------------------------------------- page 1
    ("unit7", "heading", 'Unit banner heading: "UNIT VII"'),
    ("unit7", "heading", 'Unit title: "GENETICS AND EVOLUTION"'),
    ("unit7", "term", 'Unit contents listed as "Chapter 4 Principles of Inheritance and Variation", '
                      '"Chapter 5 Molecular Basis of Inheritance", "Chapter 6 Evolution"'),
    ("unit7", "opener", '"The work of Mendel and others who followed him gave us an idea of inheritance patterns."'),
    ("unit7", "fact", '"However the nature of those factors which determine the phenotype was not very clear."'),
    ("unit7", "fact", '"As these factors represent the genetic basis of inheritance, understanding the structure of '
                      'genetic material and the structural basis of genotype and phenotype conversion became the '
                      'focus of attention in biology for the next century."'),
    ("unit7", "fact", '"The entire body of molecular biology was a consequent development with major contributions '
                      "from Watson, Crick, Nirenberg, Khorana, Kornberg's (father and son), Benzer, Monod, Brenner, "
                      'etc."'),
    ("unit7", "fact", '"A parallel problem being tackled was the mechanism of evolution."'),
    ("unit7", "fact", '"Awareness in the areas of molecular genetics, structural biology and bioinformatics have '
                      'enriched our understanding of the molecular basis of evolution."'),
    ("unit7", "fact", '"In this unit the structure and function of DNA and the story and theory of evolution have '
                      'been examined and explained."'),

    # ---------------------------------------------------------------- page 2
    ("profile", "heading", 'Unnumbered scientist-profile heading: "JAMES WATSON"'),
    ("profile", "number", '"James Dewey Watson was born in Chicago on 6 April 1928." (date: 6 April 1928)'),
    ("profile", "number", '"In 1947, he received B.Sc. degree in Zoology." (date: 1947)'),
    ("profile", "fact", '"During these years his interest in bird-watching had matured into a serious desire to '
                        'learn genetics."'),
    ("profile", "number", '"This became possible when he received a Fellowship for graduate study in Zoology at '
                          'Indiana University, Bloomington, where he received his Ph.D degree in 1950 on a study of '
                          'the effect of hard X-rays on bacteriophage multiplication." (date: 1950)'),
    ("profile", "fact", '"He met Crick and discovered their common interest in solving the DNA structure."'),
    ("profile", "fact", '"Their first serious effort, was unsatisfactory."'),
    ("profile", "number", '"Their second effort based upon more experimental evidence and better appreciation of the '
                          'nucleic acid literature resulted, early in March 1953, in the proposal of the '
                          'complementary double-helical configuration." (date: March 1953)'),
    ("profile", "heading", 'Unnumbered scientist-profile heading: "FRANCIS CRICK"'),
    ("profile", "number", '"Francis Harry Compton Crick was born on 8 June 1916, at Northampton, England." '
                          '(date: 8 June 1916)'),
    ("profile", "fact", '"He studied physics at University College, London and obtained a B.Sc. in 1937." '
                        '(date: 1937)'),
    ("profile", "number", '"He completed Ph.D. in 1954 on a thesis entitled X-ray Diffraction: Polypeptides and '
                          'Proteins". (date: 1954)'),
    ("profile", "number", '"A critical influence in Crick\'s career was his friendship with J.D. Watson, then a '
                          'young man of 23, leading in 1953 to the proposal of the double-helical structure for DNA '
                          'and the replication scheme." (ages/dates: 23, 1953)'),
    ("profile", "number", '"Crick was made an F.R.S. in 1959." (date: 1959)'),
    ("profile", "number", '"The honours to Watson with Crick include: the John Collins Warren Prize of the '
                          'Massachusetts General Hospital, in 1959; the Lasker Award in 1960; the Research '
                          'Corporation Prize, in 1962 and above all, the Nobel Prize in 1962." '
                          '(dates: 1959, 1960, 1962)'),
    ("profile", "caption", 'Scientist-portrait captions (verbatim): "JAMES WATSON", "FRANCIS CRICK" - human-subject '
                           'plates, text-only by section 4.4 rule, never reproduced'),

    # ---------------------------------------------------------------- page 3
    ("ch4", "heading", 'Chapter number: "CHAPTER 4"'),
    ("ch4", "heading", 'Chapter title: "PRINCIPLES OF INHERITANCE AND VARIATION"'),
    ("ch4", "term", 'Chapter contents listed as "4.1 Mendel\'s Laws of Inheritance", "4.2 Inheritance of One Gene", '
                    '"4.3 Inheritance of Two Genes", "4.4 Sex Determination", "4.5 Mutation", '
                    '"4.6 Genetic Disorders" (contents box list only - the printed body runs 4.1 to 4.8)'),
    ("ch4", "opener", '"Have you ever wondered why an elephant always gives birth only to a baby elephant and not '
                      'some other animal?"'),
    ("ch4", "question", '"Or why a mango seed forms only a mango plant and not any other plant?"'),
    ("ch4", "question", '"Given that they do, are the offspring identical to their parents? Or do they show '
                        'differences in some of their characteristics?"'),
    ("ch4", "question", '"Have you ever wondered why siblings sometimes look so similar to each other? Or sometimes '
                        'even so different?"'),
    ("ch4", "fact", '"These and several related questions are dealt with, scientifically, in a branch of biology '
                    'known as Genetics."'),
    ("ch4", "fact", '"This subject deals with the inheritance, as well as the variation of characters from parents '
                    'to offspring."'),
    ("ch4", "definition", '"Inheritance is the process by which characters are passed on from parent to progeny; it '
                          'is the basis of heredity."'),
    ("ch4", "definition", '"Variation is the degree by which progeny differ from their parents."'),
    ("ch4", "number", '"Humans knew from as early as 8000-1000 B.C. that one of the causes of variation was hidden '
                      'in sexual reproduction." (dates: 8000-1000 B.C.)'),
    ("ch4", "fact", '"They exploited the variations that were naturally present in the wild populations of plants '
                    'and animals to selectively breed and select for organisms that possessed desirable characters."'),
    ("ch4", "example", '"For example, through artificial selection and domestication from ancestral wild cows, we '
                       'have well-known Indian breeds, e.g., Sahiwal cows in Punjab."'),
    ("ch4", "qualifier", '"We must, however, recognise that though our ancestors knew about the inheritance of '
                         'characters and variation, they had very little idea about the scientific basis of these '
                         'phenomena."'),

    # ---------------------------------------------------------------- page 4 - 4.1
    ("4.1", "heading", "\"4.1 MENDEL'S LAWS OF INHERITANCE\""),
    ("4.1", "opener", '"It was during the mid-nineteenth century that headway was made in the understanding of '
                      'inheritance."'),
    ("4.1", "number", '"Gregor Mendel, conducted hybridisation experiments on garden peas for seven years '
                      '(1856-1863) and proposed the laws of inheritance in living organisms." '
                      '(dates: 1856-1863; duration: seven years)'),
    ("4.1", "fact", '"During Mendel\'s investigations into inheritance patterns it was for the first time that '
                    'statistical analysis and mathematical logic were applied to problems in biology."'),
    ("4.1", "fact", '"His experiments had a large sampling size, which gave greater credibility to the data that he '
                    'collected."'),
    ("4.1", "fact", '"Also, the confirmation of his inferences from experiments on successive generations of his '
                    'test plants, proved that his results pointed to general rules of inheritance rather than being '
                    'unsubstantiated ideas."'),
    ("4.1", "example", '"Mendel investigated characters in the garden pea plant that were manifested as two opposing '
                       'traits, e.g., tall or dwarf plants, yellow or green seeds."'),
    ("4.1", "fact", '"This allowed him to set up a basic framework of rules governing inheritance, which was '
                    'expanded on by later scientists to account for all the diverse natural observations and the '
                    'complexity inherent in them."'),
    ("4.1", "fact", '"Mendel conducted such artificial pollination/cross pollination experiments using several '
                    'true-breeding pea lines."'),
    ("4.1", "definition", '"A true-breeding line is one that, having undergone continuous self-pollination, shows '
                          'the stable trait inheritance and expression for several generations."'),
    ("4.1", "number", '"Mendel selected 14 true-breeding pea plant varieties, as pairs which were similar except for '
                      'one character with contrasting traits." (count: 14)'),
    ("4.1", "example", '"Some of the contrasting traits selected were smooth or wrinkled seeds, yellow or green '
                       'seeds, inflated (full) or constricted green or yellow pods and tall or dwarf plants '
                       '(Figure 4.1, Table 4.1)."'),

    # Figure 4.1 + Table 4.1
    ("Fig 4.1", "caption", 'Figure 4.1 caption (verbatim): "Figure 4.1 Seven pairs of contrasting traits in pea '
                           'plant studied by Mendel"'),
    ("Fig 4.1", "figure-labels", 'Figure labels: "Character"; "Dominant trait"; "Recessive trait"; "Seed shape"; '
                                 '"Round"; "Wrinkled"; "Seed colour"; "Yellow"; "Green"; "Flower colour"; "Violet"; '
                                 '"White"; "Pod shape"; "Full"; "Constricted"; "Pod colour"; "Green"; "Yellow"; '
                                 '"Flower position"; "Axial"; "Terminal"; "Stem height"; "Tall"; "Dwarf"'),
    ("Table 4.1", "caption", 'Table 4.1 caption (verbatim): "Table 4.1: Contrasting Traits Studied by Mendel in '
                             'Pea"'),
    ("Table 4.1", "table", 'Table 4.1 row 1: S.No. 1 - Characters: "Stem height"; Contrasting Traits: "Tall/dwarf"'),
    ("Table 4.1", "table", 'Table 4.1 row 2: S.No. 2 - Characters: "Flower colour"; Contrasting Traits: '
                           '"Violet/white" (NCERT prints "Flouwer colour" - source spelling)'),
    ("Table 4.1", "table", 'Table 4.1 row 3: S.No. 3 - Characters: "Flower position"; Contrasting Traits: '
                           '"Axial/terminal"'),
    ("Table 4.1", "table", 'Table 4.1 row 4: S.No. 4 - Characters: "Pod shape"; Contrasting Traits: '
                           '"Inflated/constricted"'),
    ("Table 4.1", "table", 'Table 4.1 row 5: S.No. 5 - Characters: "Pod colour"; Contrasting Traits: "Green/yellow"'),
    ("Table 4.1", "table", 'Table 4.1 row 6: S.No. 6 - Characters: "Seed shape"; Contrasting Traits: '
                           '"Round/wrinkled"'),
    ("Table 4.1", "table", 'Table 4.1 row 7: S.No. 7 - Characters: "Seed colour"; Contrasting Traits: '
                           '"Yellow/green"'),

    # ---------------------------------------------------------------- page 5 - 4.2
    ("4.2", "heading", '"4.2 INHERITANCE OF ONE GENE"'),
    ("4.2", "opener", '"Let us take the example of one such hybridisation experiment carried out by Mendel where he '
                      'crossed tall and dwarf pea plants to study the inheritance of one gene (Figure 4.2)."'),
    ("4.2", "fact", '"He collected the seeds produced as a result of this cross and grew them to generate plants of '
                    'the first hybrid generation."'),
    ("4.2", "term", '"This generation is also called the Filial1 progeny or the F1."'),
    ("4.2", "fact", '"Mendel observed that all the F1 progeny plants were tall, like one of its parents; none were '
                    'dwarf (Figure 4.3)."'),
    ("4.2", "fact", '"He made similar observations for the other pairs of traits - he found that the F1 always '
                    'resembled either one of the parents, and that the trait of the other parent was not seen in '
                    'them."'),
    ("4.2", "fact", "\"Mendel then self-pollinated the tall F1 plants and to his surprise found that in the Filial2 "
                    "generation some of the offspring were 'dwarf'; the character that was not seen in the F1 "
                    'generation was now expressed."'),
    ("4.2", "number", '"The proportion of plants that were dwarf were 1/4th of the F2 plants while 3/4th of the F2 '
                      'plants were tall." (ratios: 1/4th, 3/4th)'),
    ("4.2", "fact", '"The tall and dwarf traits were identical to their parental type and did not show any blending, '
                    'that is all the offspring were either tall or dwarf, none were of in-between height '
                    '(Figure 4.3)."'),
    ("4.2", "number", '"Similar results were obtained with the other traits that he studied: only one of the '
                      'parental traits was expressed in the F1 generation while at the F2 stage both the traits were '
                      'expressed in the proportion 3:1." (ratio: 3:1)'),
    ("4.2", "exception", '"The contrasting traits did not show any blending at either F1 or F2 stage."'),

    ("Fig 4.2", "caption", 'Figure 4.2 caption (verbatim): "Figure 4.2 Steps in making a cross in pea"'),
    ("Fig 4.2", "figure-labels", 'Figure labels: "Petal"; "Stigma"; "Anther"; "Stamen"; "Carpel"; "Removal of '
                                 'anthers"; "(Emasculation)"; "Transfer of pollen"; "(Pollination)"; "Parent"; '
                                 '"Parent"'),

    # ---------------------------------------------------------------- page 6 - 4.2 continued
    ("4.2", "fact", '"Based on these observations, Mendel proposed that something was being stably passed down, '
                    'unchanged, from parent to offspring through the gametes, over successive generations."'),
    ("4.2", "term", "\"He called these things as 'factors'. Now we call them as genes.\""),
    ("4.2", "definition", '"Genes, therefore, are the units of inheritance."'),
    ("4.2", "fact", '"They contain the information that is required to express a particular trait in an organism."'),
    ("4.2", "definition", '"Genes which code for a pair of contrasting traits are known as alleles, i.e., they are '
                          'slightly different forms of the same gene."'),
    ("4.2", "fact", '"If we use alphabetical symbols for each gene, then the capital letter is used for the trait '
                    'expressed at the F1 stage and the small alphabet for the other trait."'),
    ("4.2", "example", '"For example, in case of the character of height, T is used for the Tall trait and t for the '
                       "'dwarf', and T and t are alleles of each other.\""),
    ("4.2", "example", '"Hence, in plants the pair of alleles for height would be TT, Tt or tt."'),
    ("4.2", "definition", '"Mendel also proposed that in a true breeding, tall or dwarf pea variety the allelic pair '
                          'of genes for height are identical or homozygous, TT and tt, respectively. TT and tt are '
                          'called the genotype of the plant while the descriptive terms tall and dwarf are the '
                          'phenotype."'),
    ("4.2", "question", '"What then would be the phenotype of a plant that had a genotype Tt?"'),
    ("4.2", "fact", '"As Mendel found the phenotype of the F1 heterozygote Tt to be exactly like the TT parent in '
                    'appearance, he proposed that in a pair of dissimilar factors, one dominates the other (as in '
                    'the F1) and hence is called the dominant factor while the other factor is recessive."'),
    ("4.2", "example", '"In this case T (for tallness) is dominant over t (for dwarfness), that is recessive."'),
    ("4.2", "fact", '"He observed identical behaviour for all the other characters/trait-pairs that he studied."'),
    ("4.2", "fact", '"It is convenient (and logical) to use the capital and lower case of an alphabetical symbol to '
                    'remember this concept of dominance and recessiveness."'),
    ("4.2", "qualifier", '"(Do not use T for tall and d for dwarf because you will find it difficult to remember '
                         'whether T and d are alleles of the same gene/character or not)."'),
    ("4.2", "fact", '"Alleles can be similar as in the case of homozygotes TT and tt or can be dissimilar as in the '
                    'case of the heterozygote Tt."'),
    ("4.2", "definition", '"Since the Tt plant is heterozygous for genes controlling one character (height), it is a '
                          'monohybrid and the cross between TT and tt is a monohybrid cross."'),

    ("Fig 4.3", "caption", 'Figure 4.3 caption (verbatim): "Figure 4.3 Diagrammatic representation of monohybrid '
                           'cross"'),
    ("Fig 4.3", "figure-labels", 'Figure labels: "Parental"; "Tall"; "Dwarf"; "F1 generation"; "Selfing"; "Tall"; '
                                 '"Tall"; "Tall"; "F2 generation"; "Tall"; "Tall"; "Dwarf"'),

    # ---------------------------------------------------------------- page 7 - Punnett square
    ("4.2", "fact", '"From the observation that the recessive parental trait is expressed without any blending in '
                    'the F2 generation, we can infer that, when the tall and dwarf plant produce gametes, by the '
                    'process of meiosis, the alleles of the parental pair separate or segregate from each other and '
                    'only one allele is transmitted to a gamete."'),
    ("4.2", "number", '"This segregation of alleles is a random process and so there is a 50 per cent chance of a '
                      'gamete containing either allele, as has been verified by the results of the crossings." '
                      '(percentage: 50 per cent)'),
    ("4.2", "fact", '"In this way the gametes of the tall TT plants have the allele T and the gametes of the dwarf '
                    'tt plants have the allele t."'),
    ("4.2", "fact", '"During fertilisation the two alleles, T from one parent say, through the pollen, and t from '
                    'the other parent, then through the egg, are united to produce zygotes that have one T allele '
                    'and one t allele."'),
    ("4.2", "fact", '"In other words the hybrids have Tt. Since these hybrids contain alleles which express '
                    'contrasting traits, the plants are heterozygous."'),
    ("4.2", "fact", '"The production of gametes by the parents, the formation of the zygotes, the F1 and F2 plants '
                    'can be understood from a diagram called Punnett Square as shown in Figure 4.4."'),
    ("4.2", "fact", '"It was developed by a British geneticist, Reginald C. Punnett."'),
    ("4.2", "definition", '"It is a graphical representation to calculate the probability of all possible genotypes '
                          'of offspring in a genetic cross."'),
    ("4.2", "fact", '"The possible gametes are written on two sides, usually the top row and left columns. All '
                    'possible combinations are represented in boxes below in the squares, which generates a square '
                    'output form."'),
    ("4.2", "fact", '"The Punnett Square shows the parental tall TT (male) and dwarf tt (female) plants, the gametes '
                    'produced by them and, the F1 Tt progeny. The F1 plants of genotype Tt are self-pollinated."'),
    ("4.2", "term", '"The symbols for female and male are used to denote the female (eggs) and male (pollen) of '
                    'the F1 generation, respectively." (the printed glyphs are the female and male signs - drawn '
                    'symbols, NOT text: Pass 2 must draw them or use the words, because the Unicode signs are '
                    'banned by check 5)'),
    ("4.2", "number", '"The F1 plant of genotype Tt when self-pollinated, produces gametes of the genotype T and t '
                      'in equal proportion. When fertilisation takes place, the pollen grains of genotype T have a '
                      '50 per cent chance to pollinate eggs of the genotype T, as well as of genotype t. Also pollen '
                      'grains of genotype t have a 50 per cent chance of pollinating eggs of genotype T, as well as '
                      'of genotype t." (percentage: 50 per cent)'),

    ("Fig 4.4", "caption", 'Figure 4.4 caption (verbatim): "Figure 4.4 A Punnett square used to understand a typical '
                           'monohybrid cross conducted by Mendel between true-breeding tall plants and '
                           'true-breeding dwarf plants"'),
    ("Fig 4.4", "figure-labels", 'Figure labels: "Tall"; "TT"; "Dwarf"; "tt"; "Gametes"; "T"; "t"; "F1 generation"; '
                                 '"Tt"; "Selfing"; "Tall"; "Tt"; "Gametes"; "T"; "t"; "Tt"; "Phenotypic ratio: '
                                 'tall:dwarf 3:1"; "Genotypic ratio: TT:Tt:tt 1:2:1"'),
]
