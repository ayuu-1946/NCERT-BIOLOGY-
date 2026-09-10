# -*- coding: utf-8 -*-
"""Pass-1 rows, part B — source pages 8-14 (4.2 continued through 4.3.2)."""

ROWS = [
    # ---------------------------------------------------------------- page 8
    ("4.2", "fact", '"As a result of random fertilisation, the resultant zygotes can be of the genotypes TT, Tt or '
                    'tt."'),
    ("4.2", "number", '"From the Punnett square it is easily seen that 1/4th of the random fertilisations lead to '
                      'TT, 1/2 lead to Tt and 1/4th to tt." (fractions: 1/4th, 1/2, 1/4th)'),
    ("4.2", "fact", "\"Though the F1 have a genotype of Tt, but the phenotypic character seen is 'tall'.\""),
    ("4.2", "number", '"At F2 3/4th of the plants are tall, where some of them are TT while others are Tt." '
                      '(fraction: 3/4th)'),
    ("4.2", "fact", '"Externally it is not possible to distinguish between the plants with the genotypes TT and Tt."'),
    ("4.2", "fact", "\"Hence, within the genotypic pair Tt only one character T 'tall' is expressed.\""),
    ("4.2", "fact", "\"Hence the character T or 'tall' is said to dominate over the other allele t or 'dwarf' "
                    'character."'),
    ("4.2", "fact", '"It is thus due to this dominance of one character over the other that all the F1 are tall '
                    '(though the genotype is Tt) and in the F2 3/4th of the plants are tall (though genotypically '
                    '1/2 are Tt and only 1/4th are TT)."'),
    ("4.2", "number", '"This leads to a phenotypic ratio of 3/4 tall : (1/4 TT + 1/2 Tt) and 1/4 tt, i.e., a 3:1 '
                      'ratio, but a genotypic ratio of 1:2:1." (ratios: 3:1 phenotypic, 1:2:1 genotypic)'),
    ("4.2", "number", '"The 1/4 : 1/2 : 1/4 ratio of TT:Tt:tt is mathematically condensable to the form of the '
                      'binomial expression (ax + by)2, that has the gametes bearing genes T or t in equal frequency '
                      'of 1/2."'),
    ("4.2", "process", '"The expression is expanded as given below: (1/2 T + 1/2 t)2 = (1/2 T + 1/2 t) x (1/2 T + '
                       '1/2 t) = 1/4 TT + 1/2 Tt + 1/4 tt" (displayed expansion)'),
    ("4.2", "fact", '"Mendel self-pollinated the F2 plants and found that dwarf F2 plants continued to generate '
                    'dwarf plants in F3 and F4 generations."'),
    ("4.2", "fact", '"He concluded that the genotype of the dwarfs was homozygous-tt."'),
    ("4.2", "question", '"What do you think he would have got had he self-pollinated a tall F2 plant?"'),
    ("4.2", "fact", '"From the preceding paragraphs it is clear that though the genotypic ratios can be calculated '
                    'using mathematical probability, by simply looking at the phenotype of a dominant trait, it is '
                    'not possible to know the genotypic composition."'),
    ("4.2", "fact", '"That is, for example, whether a tall plant from F1 or F2 has TT or Tt composition, cannot be '
                    'predicted."'),
    ("4.2", "definition", '"Therefore, to determine the genotype of a tall plant at F2, Mendel crossed the tall '
                          'plant from F2 with a dwarf plant. This he called a testcross."'),
    ("4.2", "definition", '"In a typical testcross an organism (pea plants here) showing a dominant phenotype (and '
                          'whose genotype is to be determined) is crossed with the recessive parent instead of '
                          'self-crossing."'),
    ("4.2", "fact", '"The progenies of such a cross can easily be analysed to predict the genotype of the test '
                    'organism."'),
    ("4.2", "fact", '"Figure 4.5 shows the results of typical testcross where violet colour flower (V) is dominant '
                    'over white colour flower (v)."'),
    ("4.2", "question", '"Using Punnett square, try to find out the nature of offspring of a test cross."'),
    ("4.2", "question", '"What ratio did you get?"'),
    ("4.2", "question", '"Using the genotypes of this cross, can you give a general definition for a test cross?"'),

    # ---------------------------------------------------------------- page 9
    ("Fig 4.5", "caption", 'Figure 4.5 caption (verbatim): "Figure 4.5 Diagrammatic representation of a test cross"'),
    ("Fig 4.5", "figure-labels", 'Figure labels: "Homozygous recessive"; "Ww"; "Ww"; "WW"; "Ww"; "Dominant Phenotype '
                                 '(Genotype unknown)"; "Ww"; "Result - All flowers are violet"; "Interpretation - '
                                 'Unknown flower is homozygous dominant"; "Half of the flowers are violet and half '
                                 'of the flowers are white."; "Unknown flower is heterozygous"'),
    ("4.2", "fact", '"Based on his observations on monohybrid crosses Mendel proposed two general rules to '
                    'consolidate his understanding of inheritance in monohybrid crosses. Today these rules are '
                    "called the Principles or Laws of Inheritance: the First Law or Law of Dominance and the Second "
                    'Law or Law of Segregation."'),

    ("4.2.1", "heading", '"4.2.1 Law of Dominance"'),
    ("4.2.1", "opener", '"(i) Characters are controlled by discrete units called factors."'),
    ("4.2.1", "fact", '"(ii) Factors occur in pairs."'),
    ("4.2.1", "fact", '"(iii) In a dissimilar pair of factors one member of the pair dominates (dominant) the other '
                      '(recessive)."'),
    ("4.2.1", "fact", '"The law of dominance is used to explain the expression of only one of the parental '
                      'characters in a monohybrid cross in the F1 and the expression of both in the F2. It also '
                      'explains the proportion of 3:1 obtained at the F2."'),

    ("4.2.2", "heading", '"4.2.2 Law of Segregation"'),
    ("4.2.2", "opener", '"This law is based on the fact that the alleles do not show any blending and that both the '
                        'characters are recovered as such in the F2 generation though one of these is not seen at '
                        'the F1 stage."'),
    ("4.2.2", "fact", '"Though the parents contain two alleles during gamete formation, the factors or alleles of a '
                      'pair segregate from each other such that a gamete receives only one of the two factors."'),
    ("4.2.2", "fact", '"Of course, a homozygous parent produces all gametes that are similar while a heterozygous '
                      'one produces two kinds of gametes each having one allele with equal proportion."'),

    # ---------------------------------------------------------------- page 10
    ("4.2.2.1", "heading", '"4.2.2.1 Incomplete Dominance"'),
    ("4.2.2.1", "opener", '"When experiments on peas were repeated using other traits in other plants, it was found '
                          'that sometimes the F1 had a phenotype that did not resemble either of the two parents '
                          'and was in between the two."'),
    ("4.2.2.1", "example", '"The inheritance of flower colour in the dog flower (snapdragon or Antirrhinum sp.) is '
                           'a good example to understand incomplete dominance."'),
    ("4.2.2.1", "fact", '"In a cross between true-breeding red-flowered (RR) and true-breeding white-flowered '
                        'plants (rr), the F1 (Rr) was pink (Figure 4.6)."'),
    ("4.2.2.1", "number", '"When the F1 was self-pollinated the F2 resulted in the following ratio 1 (RR) Red : 2 '
                          '(Rr) Pink : 1 (rr) White." (ratio: 1:2:1)'),
    ("4.2.2.1", "fact", '"Here the genotype ratios were exactly as we would expect in any mendelian monohybrid '
                        'cross, but the phenotype ratios had changed from the 3:1 dominant:recessive ratio."'),
    ("4.2.2.1", "fact", '"What happened was that R was not completely dominant over r and this made it possible to '
                        'distinguish Rr as pink from RR (red) and rr (white)."'),
    ("4.2.2.1", "question", '"Explanation of the concept of dominance: What exactly is dominance? Why are some '
                            'alleles dominant and some recessive?"'),
    ("4.2.2.1", "fact", '"To tackle these questions, we must understand what a gene does. Every gene, as you know '
                        'by now, contains the information to express a particular trait."'),
    ("4.2.2.1", "fact", '"In a diploid organism, there are two copies of each gene, i.e., as a pair of alleles. '
                        'Now, these two alleles need not always be identical, as in a heterozygote."'),
    ("4.2.2.1", "fact", '"One of them may be different due to some changes that it has undergone (about which you '
                        'will read further on, and in the next chapter) which modifies the information that '
                        'particular allele contains."'),
    ("4.2.2.1", "example", '"Let\'s take an example of a gene that contains the information for producing an '
                           'enzyme. Now there are two copies of this gene, the two allelic forms."'),
    ("4.2.2.1", "fact", '"Let us assume (as is more common) that the normal allele produces the normal enzyme that '
                        'is needed for the transformation of a substrate S."'),
    ("4.2.2.1", "process", '"Theoretically, the modified allele could be responsible for production of - (i) the '
                           'normal/less efficient enzyme, or (ii) a non-functional enzyme, or (iii) no enzyme at '
                           'all"'),

    ("Fig 4.6", "caption", 'Figure 4.6 caption (verbatim): "Figure 4.6 Results of monohybrid cross in the plant '
                           'Snapdragon, where one allele is in completely dominant over the other allele" '
                           '(NCERT prints "in completely" split across the line break)'),
    ("Fig 4.6", "figure-labels", 'Figure labels: "P generation"; "Red (RR)"; "White (rr)"; "Gametes"; "R"; "r"; '
                                 '"F1 generation"; "All pink (Rr)"; "Gametes"; "RR"; "Rr"; "F2 generation"; '
                                 '"Phenotypic ratio: red:pink:white 1:2:1"; "Genotypic ratio: RR:Rr:rr 1:2:1"'),

    # ---------------------------------------------------------------- page 11
    ("4.2.2.1", "fact", '"In the first case, the modified allele is equivalent to the unmodified allele, i.e., it '
                        'will produce the same phenotype/trait, i.e., result in the transformation of substrate S. '
                        'Such equivalent allele pairs are very common."'),
    ("4.2.2.1", "fact", '"But, if the allele produces a non-functional enzyme or no enzyme, the phenotype may be '
                        'effected. The phenotype/trait will only be dependent on the functioning of the unmodified '
                        'allele."'),
    ("4.2.2.1", "fact", '"The unmodified (functioning) allele, which represents the original phenotype is the '
                        'dominant allele and the modified allele is generally the recessive allele."'),
    ("4.2.2.1", "fact", '"Hence, in the example above the recessive trait is seen due to non-functional enzyme or '
                        'because no enzyme is produced."'),

    ("4.2.2.2", "heading", '"4.2.2.2 Co-dominance"'),
    ("4.2.2.2", "opener", '"Till now we were discussing crosses where the F1 resembled either of the two parents '
                          '(dominance) or was in-between (incomplete dominance). But, in the case of co-dominance '
                          'the F1 generation resembles both parents."'),
    ("4.2.2.2", "example", '"A good example is different types of red blood cells that determine ABO blood grouping '
                           'in human beings. ABO blood groups are controlled by the gene I."'),
    ("4.2.2.2", "fact", '"The plasma membrane of the red blood cells has sugar polymers that protrude from its '
                        'surface and the kind of sugar is controlled by the gene."'),
    ("4.2.2.2", "number", '"The gene (I) has three alleles IA, IB and i." (count: three alleles; the A and B are '
                          'printed as superscripts of I)'),
    ("4.2.2.2", "fact", '"The alleles IA and IB produce a slightly different form of the sugar while allele i does '
                        'not produce any sugar."'),
    ("4.2.2.2", "fact", '"Because humans are diploid organisms, each person possesses any two of the three I gene '
                        'alleles."'),
    ("4.2.2.2", "exception", '"IA and IB are completely dominant over i, in other words when IA and i are present '
                             'only IA expresses (because i does not produce any sugar), and when IB and i are '
                             'present IB expresses."'),
    ("4.2.2.2", "definition", '"But when IA and IB are present together they both express their own types of '
                              'sugars: this is because of co-dominance. Hence red blood cells have both A and B '
                              'types of sugars."'),
    ("4.2.2.2", "number", '"Since there are three different alleles, there are six different combinations of these '
                          'three alleles that are possible, and therefore, a total of six different genotypes of '
                          'the human ABO blood types (Table 4.2)." (counts: three alleles, six combinations, six '
                          'genotypes)'),
    ("4.2.2.2", "question", '"How many phenotypes are possible?"'),

    ("Table 4.2", "caption", 'Table 4.2 caption (verbatim): "Table 4.2: Table Showing the Genetic Basis of Blood '
                             'Groups in Human Population"'),
    ("Table 4.2", "table", 'Table 4.2 row 1: Allele from Parent 1 "IA"; Allele from Parent 2 "IA"; Genotype of '
                           'offspring "IAIA"; Blood types of offspring "A"'),
    ("Table 4.2", "table", 'Table 4.2 row 2: Allele from Parent 1 "IA"; Allele from Parent 2 "IB"; Genotype of '
                           'offspring "IAIB"; Blood types of offspring "AB"'),
    ("Table 4.2", "table", 'Table 4.2 row 3: Allele from Parent 1 "IA"; Allele from Parent 2 "i"; Genotype of '
                           'offspring "IAi"; Blood types of offspring "A"'),
    ("Table 4.2", "table", 'Table 4.2 row 4: Allele from Parent 1 "IB"; Allele from Parent 2 "IA"; Genotype of '
                           'offspring "IAIB"; Blood types of offspring "AB"'),
    ("Table 4.2", "table", 'Table 4.2 row 5: Allele from Parent 1 "IB"; Allele from Parent 2 "IB"; Genotype of '
                           'offspring "IBIB"; Blood types of offspring "B"'),
    ("Table 4.2", "table", 'Table 4.2 row 6: Allele from Parent 1 "IB"; Allele from Parent 2 "i"; Genotype of '
                           'offspring "IBi"; Blood types of offspring "B"'),
    ("Table 4.2", "table", 'Table 4.2 row 7: Allele from Parent 1 "i"; Allele from Parent 2 "i"; Genotype of '
                           'offspring "ii"; Blood types of offspring "O"'),

    # ---------------------------------------------------------------- page 12
    ("4.2.2.2", "fact", '"Do you realise that the example of ABO blood grouping also provides a good example of '
                        'multiple alleles? Here you can see that there are more than two, i.e., three alleles, '
                        'governing the same character."'),
    ("4.2.2.2", "fact", '"Since in an individual only two alleles can be present, multiple alleles can be found '
                        'only when population studies are made."'),
    ("4.2.2.2", "fact", '"Occasionally, a single gene product may produce more than one effect."'),
    ("4.2.2.2", "example", '"For example, starch synthesis in pea seeds is controlled by one gene. It has two '
                           'alleles (B and b). Starch is synthesised effectively by BB homozygotes and therefore, '
                           'large starch grains are produced. In contrast, bb homozygotes have lesser efficiency in '
                           'starch synthesis and produce smaller starch grains."'),
    ("4.2.2.2", "fact", '"After maturation of the seeds, BB seeds are round and the bb seeds are wrinkled. '
                        'Heterozygotes produce round seeds, and so B seems to be the dominant allele."'),
    ("4.2.2.2", "exception", '"But, the starch grains produced are of intermediate size in Bb seeds. So if starch '
                             'grain size is considered as the phenotype, then from this angle, the alleles show '
                             'incomplete dominance."'),
    ("4.2.2.2", "qualifier", '"Therefore, dominance is not an autonomous feature of a gene or the product that it '
                             'has information for. It depends as much on the gene product and the production of a '
                             'particular phenotype from this product as it does on the particular phenotype that we '
                             'choose to examine, in case more than one phenotype is influenced by the same gene."'),

    ("4.3", "heading", '"4.3 INHERITANCE OF TWO GENES"'),
    ("4.3", "opener", '"Mendel also worked with and crossed pea plants that differed in two characters, as is seen '
                      'in the cross between a pea plant that has seeds with yellow colour and round shape and one '
                      'that had seeds of green colour and wrinkled shape (Figure 4.7)."'),
    ("4.3", "fact", '"Mendel found that the seeds resulting from the crossing of the parents, had yellow coloured '
                    'and round shaped seeds."'),
    ("4.3", "question", '"Here can you tell which of the characters in the pairs yellow/green colour and '
                        'round/wrinkled shape was dominant?"'),
    ("4.3", "fact", '"Thus, yellow colour was dominant over green and round shape dominant over wrinkled."'),
    ("4.3", "fact", '"These results were identical to those that he got when he made separate monohybrid crosses '
                    'between yellow and green seeded plants and between round and wrinkled seeded plants."'),
    ("4.3", "term", '"Let us use the genotypic symbols Y for dominant yellow seed colour and y for recessive green '
                    'seed colour, R for round shaped seeds and r for wrinkled seed shape."'),
    ("4.3", "fact", '"The genotype of the parents can then be written as RRYY and rryy."'),
    ("4.3", "fact", '"The cross between the two plants can be written down as in Figure 4.7 showing the genotypes '
                    'of the parent plants."'),
    ("4.3", "fact", '"The gametes RY and ry unite on fertilisation to produce the F1 hybrid RrYy."'),
    ("4.3", "number", '"When Mendel self hybridised the F1 plants he found that 3/4th of F2 plants had yellow seeds '
                      'and 1/4th had green. The yellow and green colours segregated in a 3:1 ratio. Round and '
                      'wrinkled seed shape also segregated in a 3:1 ratio: just like in a monohybrid cross." '
                      '(fractions: 3/4th, 1/4th; ratio: 3:1)'),

    # ---------------------------------------------------------------- page 13
    ("Fig 4.7", "caption", 'Figure 4.7 caption (verbatim): "Figure 4.7 Results of a dihybrid cross where the two '
                           'parents differed in two pairs of contrasting traits: seed colour and seed shape"'),
    ("Fig 4.7", "figure-labels", 'Figure labels: "P generation"; "Round yellow"; "RR"; "YY"; "Wrinkled green"; "rr"; '
                                 '"yy"; "Gametes"; "RY"; "ry"; "Round yellow"; "RrYy"; "Selfing"; "F1 generation"; '
                                 '"Gametes"; "RY"; "Ry"; "rY"; "ry"; "RRYY"; "RrYY"; "RrYY"; "RRYy"; "rrYY"; '
                                 '"RRYy"; "RrYy"; "RrYy"; "RrYy"; "RrYy"; "RRyy"; "Rryy"; "rrYy"; "rrYy"; "Rryy"; '
                                 '"rryy"; "F2 generation"; "Phenotypic ratio: round yellow : round green : wrinkled '
                                 'yellow : wrinkled green 9:3:3:1"'),

    # ---------------------------------------------------------------- page 14
    ("4.3.1", "heading", '"4.3.1 Law of Independent Assortment"'),
    ("4.3.1", "opener", '"In the dihybrid cross (Figure 4.7), the phenotypes round, yellow; wrinkled, yellow; '
                        'round, green and wrinkled, green appeared in the ratio 9:3:3:1. Such a ratio was observed '
                        'for several pairs of characters that Mendel studied."'),
    ("4.3.1", "process", '"The ratio of 9:3:3:1 can be derived as a combination series of 3 yellow : 1 green, with '
                         '3 round : 1 wrinkled. This derivation can be written as follows: (3 Round : 1 Wrinkled) '
                         '(3 Yellow : 1 Green) = 9 Round, Yellow : 3 Wrinkled, Yellow : 3 Round, Green : 1 '
                         'Wrinkled, Green"'),
    ("4.3.1", "definition", '"Based upon such observations on dihybrid crosses (crosses between plants differing in '
                            "two traits) Mendel proposed a second set of generalisations that we call Mendel's Law "
                            'of Independent Assortment. The law states that when two pairs of traits are combined in '
                            "a hybrid, segregation of one pair of characters is independent of the other pair of "
                            "characters'.\""),
    ("4.3.1", "fact", '"The Punnett square can be effectively used to understand the independent segregation of the '
                      'two pairs of genes during meiosis and the production of eggs and pollen in the F1 RrYy '
                      'plant."'),
    ("4.3.1", "number", '"Consider the segregation of one pair of genes R and r. Fifty per cent of the gametes have '
                        'the gene R and the other 50 per cent have r. Now besides each gamete having either R or r, '
                        'it should also have the allele Y or y." (percentage: 50 per cent)'),
    ("4.3.1", "fact", '"The important thing to remember here is that segregation of 50 per cent R and 50 per cent r '
                      'is independent from the segregation of 50 per cent Y and 50 per cent y."'),
    ("4.3.1", "number", '"Therefore, 50 per cent of the r bearing gametes has Y and the other 50 per cent has y. '
                        'Similarly, 50 per cent of the R bearing gametes has Y and the other 50 per cent has y." '
                        '(percentage: 50 per cent)'),
    ("4.3.1", "number", '"Thus there are four genotypes of gametes (four types of pollen and four types of eggs)." '
                        '(count: four)'),
    ("4.3.1", "number", '"The four types are RY, Ry, rY and ry each with a frequency of 25 per cent or 1/4 of the '
                        'total gametes produced." (frequency: 25 per cent or 1/4)'),
    ("4.3.1", "fact", '"When you write down the four types of eggs and pollen on the two sides of a Punnett square '
                      'it is very easy to derive the composition of the zygotes that give rise to the F2 plants '
                      '(Figure 4.7)."'),
    ("4.3.1", "question", '"Although there are 16 squares how many different types of genotypes and phenotypes are '
                          'formed? Note them down in the format given."'),
    ("4.3.1", "table", 'Activity table header row: "S.No."; "Genotypes found in F2"; "Their expected Phenotypes" '
                       '(blank table for the student to fill)'),
    ("4.3.1", "question", '"Can you, using the Punnett square data work out the genotypic ratio at the F2 stage and '
                          'fill in the format given? Is the genotypic ratio also 9:3:3:1?"'),

    ("4.3.2", "heading", '"4.3.2 Chromosomal Theory of Inheritance"'),
    ("4.3.2", "opener", '"Mendel published his work on inheritance of characters in 1865 but for several reasons, '
                        'it remained unrecognised till 1900." (dates: 1865, 1900)'),
    ("4.3.2", "fact", '"Firstly, communication was not easy (as it is now) in those days and his work could not be '
                      'widely publicised."'),
    ("4.3.2", "fact", '"Secondly, his concept of genes (or factors, in Mendel\'s words) as stable and discrete '
                      'units that controlled the expression of traits and, of the pair of alleles which did not '
                      'blend with each other, was not accepted by his contemporaries as an explanation for the '
                      'apparently continuous variation seen in nature."'),
    ("4.3.2", "fact", '"Thirdly, Mendel\'s approach of using mathematics to explain biological phenomena was '
                      'totally new and unacceptable to many of the biologists of his time."'),
    ("4.3.2", "fact", '"Finally, though Mendel\'s work suggested that factors (genes) were discrete units, he could '
                      'not provide any physical proof for the existence of factors or say what they were made of."'),
    ("4.3.2", "number", '"In 1900, three Scientists (de Vries, Correns and von Tschermak) independently '
                        'rediscovered Mendel\'s results on the inheritance of characters." '
                        '(date: 1900; count: three Scientists)'),
    ("4.3.2", "fact", '"Also, by this time due to advancements in microscopy that were taking place, scientists '
                      'were able to carefully observe cell division."'),
    ("4.3.2", "fact", '"This led to the discovery of structures in the nucleus that appeared to double and divide '
                      'just before each cell division. These were called chromosomes (colored bodies, as they were '
                      'visualised by staining)."'),
    ("4.3.2", "number", '"By 1902, the chromosome movement during meiosis had been worked out." (date: 1902)'),
    ("4.3.2", "fact", '"Walter Sutton and Theodore Boveri noted that the behaviour of chromosomes was parallel to '
                      'the behaviour of genes and used chromosome movement (Figure 4.8) to explain Mendel\'s laws '
                      '(Table 4.3)."'),
    ("4.3.2", "fact", '"Recall that you have studied the behaviour of chromosomes during mitosis (equational '
                      'division) and during meiosis (reduction division). The important things to remember are that '
                      'chromosomes as well as genes occur in pairs."'),
    ("4.3.2", "fact", '"The two alleles of a gene pair are located on homologous sites on homologous chromosomes."'),
]
