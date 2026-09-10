# -*- coding: utf-8 -*-
"""Pass-1 rows, part C — source pages 15-28 (4.3.2 end through the exercises)."""

ROWS = [
    # ---------------------------------------------------------------- page 15
    ("4.3.2", "fact", '"Sutton and Boveri argued that the pairing and separation of a pair of chromosomes would '
                      'lead to the segregation of a pair of factors they carried."'),
    ("4.3.2", "definition", '"Sutton united the knowledge of chromosomal segregation with Mendelian principles and '
                            'called it the chromosomal theory of inheritance."'),
    ("4.3.2", "fact", '"Following this synthesis of ideas, experimental verification of the chromosomal theory of '
                      'inheritance by Thomas Hunt Morgan and his colleagues, led to discovering the basis for the '
                      'variation that sexual reproduction produced."'),
    ("4.3.2", "example", '"Morgan worked with the tiny fruitflies, Drosophila melanogaster (Figure 4.10), which '
                         'were found very suitable for such studies."'),
    ("4.3.2", "fact", '"They could be grown on simple synthetic medium in the laboratory."'),
    ("4.3.2", "number", '"They complete their life cycle in about two weeks, and a single mating could produce a '
                        'large number of progeny flies." (duration: about two weeks)'),
    ("4.3.2", "fact", '"Also, there was a clear differentiation of the sexes - the male and female flies are easily '
                      'distinguishable."'),
    ("4.3.2", "fact", '"Also, it has many types of hereditary variations that can be seen with low power '
                      'microscopes."'),

    ("Fig 4.8", "caption", 'Figure 4.8 caption (verbatim): "Figure 4.8 Meiosis and germ cell formation in a cell '
                           'with four chromosomes. Can you see how chromosomes segregate when germ cells are '
                           'formed?"'),
    ("Fig 4.8", "figure-labels", 'Figure labels: "G2"; "Bivalent"; "Meiosis I"; "anaphase"; "Meiosis II"; '
                                 '"anaphase"; "Germ cells"'),

    # ---------------------------------------------------------------- page 16
    ("Table 4.3", "caption", 'Table 4.3 caption (verbatim): "Table 4.3: A Comparison between the Behaviour of '
                             'Chromosomes and Genes"'),
    ("Table 4.3", "table", 'Table 4.3 column A row 1: "Occur in pairs"'),
    ("Table 4.3", "table", 'Table 4.3 column A row 2: "Segregate at the time of gamete formation such that only one '
                           'of each pair is transmitted to a gamete"'),
    ("Table 4.3", "table", 'Table 4.3 column A row 3: "Independent pairs segregate independently of each other"'),
    ("Table 4.3", "table", 'Table 4.3 column B row 1: "Occur in pairs"'),
    ("Table 4.3", "table", 'Table 4.3 column B row 2: "Segregate at gamete formation and only one of each pair is '
                           'transmitted to a gamete"'),
    ("Table 4.3", "table", 'Table 4.3 column B row 3: "One pair segregates independently of another pair"'),
    ("Table 4.3", "question", '"Can you tell which of these columns A or B represent the chromosome and which '
                              'represents the gene? How did you decide?"'),
    ("4.3.2", "fact", '"During Anaphase of meiosis I, the two chromosome pairs can align at the metaphase plate '
                      'independently of each other (Figure 4.9)."'),
    ("4.3.2", "fact", '"To understand this, compare the chromosomes of four different colour in the left and right '
                      'columns. In the left column (Possibility I) orange and green is segregating together. But in '
                      'the right hand column (Possibility II) the orange chromosome is segregating with the red '
                      'chromosomes."'),

    ("Fig 4.9", "caption", 'Figure 4.9 caption (verbatim): "Figure 4.9 Independent assortment of chromosomes"'),
    ("Fig 4.9", "figure-labels", 'Figure labels: "Possibility I"; "Possibility II"; "Meiosis I - anaphase"; "Meiosis '
                                 'II - anaphase"; "Germ cells"; "One long orange and short green chromosome and long '
                                 'yellow and short red chromosome at the same pole"; "One long orange and short red '
                                 'chromosome and long yellow and short green chromosome at the same pole" '
                                 '(the figure carries the chromosome distinction by COLOUR: orange, green, red, '
                                 'yellow)'),

    # ---------------------------------------------------------------- page 17
    ("Fig 4.10", "caption", 'Figure 4.10 caption (verbatim): "Figure 4.10 Drosophila melanogaster (a) Male '
                            '(b) Female"'),
    ("Fig 4.10", "figure-labels", 'Figure labels: "(a)"; "(b)"'),

    ("4.3.3", "heading", '"4.3.3 Linkage and Recombination"'),
    ("4.3.3", "opener", '"Morgan carried out several dihybrid crosses in Drosophila to study genes that were '
                        'sex-linked."'),
    ("4.3.3", "fact", '"The crosses were similar to the dihybrid crosses carried out by Mendel in peas. For example '
                      'Morgan hybridised yellow-bodied, white-eyed females to brown-bodied, red-eyed males and '
                      'intercrossed their F1 progeny."'),
    ("4.3.3", "number", '"He observed that the two genes did not segregate independently of each other and the F2 '
                        'ratio deviated very significantly from the 9:3:3:1 ratio (expected when the two genes are '
                        'independent)." (ratio: 9:3:3:1)'),
    ("4.3.3", "fact", '"Morgan and his group knew that the genes were located on the X chromosome (Section 4.4) and '
                      'saw quickly that when the two genes in a dihybrid cross were situated on the same '
                      'chromosome, the proportion of parental gene combinations were much higher than the '
                      'non-parental type."'),
    ("4.3.3", "definition", '"Morgan attributed this due to the physical association or linkage of the two genes '
                            'and coined the term linkage to describe this physical association of genes on a '
                            'chromosome and the term recombination to describe the generation of non-parental gene '
                            'combinations (Figure 4.11)."'),
    ("4.3.3", "fact", '"Morgan and his group also found that even when genes were grouped on the same chromosome, '
                      'some genes were very tightly linked (showed very low recombination) (Figure 4.11, Cross A) '
                      'while others were loosely linked (showed higher recombination) (Figure 4.11, Cross B)."'),
    ("4.3.3", "number", '"For example he found that the genes white and yellow were very tightly linked and showed '
                        'only 1.3 per cent recombination while white and miniature wing showed 37.2 per cent '
                        'recombination." (percentages: 1.3 per cent, 37.2 per cent)'),
    ("4.3.3", "fact", '"His student Alfred Sturtevant used the frequency of recombination between gene pairs on the '
                      'same chromosome as a measure of the distance between genes and \'mapped\' their position on '
                      'the chromosome."'),

    # ---------------------------------------------------------------- page 18
    ("4.3.3", "fact", '"Today genetic maps are extensively used as a starting point in the sequencing of whole '
                      'genomes as was done in the case of the Human Genome Sequencing Project, described later."'),
    ("Fig 4.11", "caption", 'Figure 4.11 caption (verbatim): "Figure 4.11 Linkage: Results of two dihybrid crosses '
                            'conducted by Morgan. Cross A shows crossing between gene y and w; Cross B shows '
                            'crossing between genes w and m. Here dominant wild type alleles are represented with '
                            '(+) sign in superscript. Note: The strength of linkage between y and w is higher than '
                            'w and m."'),
    ("Fig 4.11", "figure-labels", 'Figure labels: "Cross A"; "Cross B"; "Yellow, white"; "White, miniature"; "Wild '
                                  'type"; "F1 generation"; "Gametes"; "Parental type (98.7%)"; "Recombinant types '
                                  '(1.3%)"; "Parental type (62.8%)"; "Recombinant types (37.2%)"; "yellow"; '
                                  '"white"; "yellow, white"; "miniature"; "white"; "White, miniature"; "wild type"'),

    # ---------------------------------------------------------------- page 19
    ("4.4", "heading", '"4.4 POLYGENIC INHERITANCE"'),
    ("4.4", "opener", '"Mendel\'s studies mainly described those traits that have distinct alternate forms such as '
                      'flower colour which are either purple or white."'),
    ("4.4", "fact", '"But if you look around you will find that there are many traits which are not so distinct in '
                    'their occurrence and are spread across a gradient."'),
    ("4.4", "example", '"For example, in humans we don\'t just have tall or short people as two distinct '
                       'alternatives but a whole range of possible heights."'),
    ("4.4", "definition", '"Such traits are generally controlled by three or more genes and are thus called as '
                          'polygenic traits."'),
    ("4.4", "fact", '"Besides the involvement of multiple genes polygenic inheritance also takes into account the '
                    'influence of environment."'),
    ("4.4", "example", '"Human skin colour is another classic example for this."'),
    ("4.4", "fact", '"In a polygenic trait the phenotype reflects the contribution of each allele, i.e., the effect '
                    'of each allele is additive."'),
    ("4.4", "example", '"To understand this better let us assume that three genes A, B, C control skin colour in '
                       'human with the dominant forms A, B and C responsible for dark skin colour and the recessive '
                       'forms a, b and c for light skin colour."'),
    ("4.4", "fact", '"The genotype with all the dominant alleles (AABBCC) will have the darkest skin colour and '
                    'that with all the recessive alleles (aabbcc) will have the lightest skin colour."'),
    ("4.4", "fact", '"As expected the genotype with three dominant alleles and three recessive alleles will have an '
                    'intermediate skin colour. In this manner the number of each type of alleles in the genotype '
                    'would determine the darkness or lightness of the skin in an individual."'),

    ("4.5", "heading", '"4.5 PLEIOTROPY"'),
    ("4.5", "opener", '"We have so far seen the effect of a gene on a single phenotype or trait."'),
    ("4.5", "definition", '"There are however instances where a single gene can exhibit multiple phenotypic '
                          'expression. Such a gene is called a pleiotropic gene."'),
    ("4.5", "fact", '"The underlying mechanism of pleiotropy in most cases is the effect of a gene on metabolic '
                    'pathways which contribute towards different phenotypes."'),
    ("4.5", "example", '"An example of this is the disease phenylketonuria, which occurs in humans. The disease is '
                       'caused by mutation in the gene that codes for the enzyme phenylalanine hydroxylase (single '
                       'gene mutation). This manifests itself through phenotypic expression characterised by mental '
                       'retardation and a reduction in hair and skin pigmentation."'),

    ("4.6", "heading", '"4.6 SEX DETERMINATION"'),
    ("4.6", "opener", '"The mechanism of sex determination has always been a puzzle before the geneticists."'),
    ("4.6", "fact", '"The initial clue about the genetic/chromosomal mechanism of sex determination can be traced '
                    'back to some of the experiments carried out in insects."'),
    ("4.6", "fact", '"In fact, the cytological observations made in a number of insects led to the development of '
                    'the concept of genetic/chromosomal basis of sex-determination."'),
    ("4.6", "number", '"Henking (1891) could trace a specific nuclear structure all through spermatogenesis in a '
                      'few insects, and it was also observed by him that 50 per cent of the sperm received this '
                      'structure after spermatogenesis, whereas the other 50 per cent sperm did not receive it." '
                      '(date: 1891; percentage: 50 per cent)'),
    ("4.6", "fact", "\"Henking gave a name to this structure as the x body but he could not explain its "
                    'significance."'),
    ("4.6", "fact", '"Further investigations by other scientists led to the conclusion that the \'X body\' of '
                    'Henking was in fact a chromosome and that is why it was given the name X-chromosome."'),

    # ---------------------------------------------------------------- page 20
    ("4.6", "fact", '"It was also observed that in a large number of insects the mechanism of sex determination is '
                    'of the XO type, i.e., all eggs bear an additional X-chromosome besides the other chromosomes '
                    '(autosomes)."'),
    ("4.6", "fact", '"On the other hand, some of the sperms bear the X-chromosome whereas some do not."'),
    ("4.6", "fact", '"Eggs fertilised by sperm having an X-chromosome become females and, those fertilised by '
                    'sperms that do not have an X-chromosome become males."'),
    ("4.6", "question", '"Do you think the number of chromosomes in the male and female are equal?"'),
    ("4.6", "definition", '"Due to the involvement of the X-chromosome in the determination of sex, it was '
                          'designated to be the sex chromosome, and the rest of the chromosomes were named as '
                          'autosomes."'),
    ("4.6", "example", '"Grasshopper is an example of XO type of sex determination in which the males have only one '
                       'X-chromosome besides the autosomes, whereas females have a pair of X-chromosomes."'),
    ("4.6", "fact", '"These observations led to the investigation of a number of species to understand the '
                    'mechanism of sex determination."'),
    ("4.6", "fact", '"In a number of other insects and mammals including man, XY type of sex determination is seen '
                    'where both male and female have same number of chromosomes. Among the males an X-chromosome is '
                    'present but its counterpart is distinctly smaller and called the Y-chromosome. Females, '
                    'however, have a pair of X-chromosomes."'),
    ("4.6", "fact", '"Both males and females bear same number of autosomes. Hence, the males have autosomes plus '
                    'XY, while female have autosomes plus XX."'),
    ("4.6", "fact", '"In human beings and in Drosophila the males have one X and one Y chromosome, whereas females '
                    'have a pair of X-chromosomes besides autosomes (Figure 4.12a, b)."'),
    ("4.6", "term", '"In the above description you have studied about two types of sex determining mechanisms, '
                    'i.e., XO type and XY type. But in both cases males produce two different types of gametes, '
                    '(a) either with or without X-chromosome or (b) some gametes with X-chromosome and some with '
                    'Y-chromosome. Such type of sex determination mechanism is designated to be the example of '
                    'male heterogamety."'),
    ("4.6", "fact", '"In some other organisms, e.g., birds, a different mechanism of sex determination is observed '
                    '(Figure 4.12 c). In this case the total number of chromosome is same in both males and '
                    'females. But two different types of gametes in terms of the sex chromosomes, are produced by '
                    'females, i.e., female heterogamety."'),
    ("4.6", "term", '"In order to have a distinction with the mechanism of sex determination described earlier, the '
                    'two different sex chromosomes of a female bird has been designated to be the Z and W '
                    'chromosomes. In these organisms the females have one Z and one W chromosome, whereas males '
                    'have a pair of Z-chromosomes besides the autosomes."'),

    ("Fig 4.12", "caption", 'Figure 4.12 caption (verbatim): "Figure 4.12 Determination of sex by chromosomal '
                            'differences: (a, b) Both in humans and in Drosophila the female has a pair of XX '
                            'chromosomes (homogametic) and the male XY (heterogametic) composition; (c) In many '
                            'birds, female has a pair of dissimilar chromosomes Zw and male two similar ZZ '
                            'chromosomes" (NCERT prints "Zw" and "ZZ")'),
    ("Fig 4.12", "figure-labels", 'Figure labels: "XX"; "XY"; "(a)"; "XX"; "XY"; "(b)"; "ZW"; "ZZ"; "(c)"'),

    # ---------------------------------------------------------------- page 21
    ("4.6.1", "heading", '"4.6.1 Sex Determination in Humans"'),
    ("4.6.1", "opener", '"It has already been mentioned that the sex determining mechanism in case of humans is XY '
                        'type."'),
    ("4.6.1", "number", '"Out of 23 pairs of chromosomes present, 22 pairs are exactly same in both males and '
                        'females: these are the autosomes." (counts: 23 pairs, 22 pairs)'),
    ("4.6.1", "fact", '"A pair of X-chromosomes are present in the female, whereas the presence of an X and Y '
                      'chromosome are determinant of the male characteristic."'),
    ("4.6.1", "number", '"During spermatogenesis among males, two types of gametes are produced. 50 per cent of the '
                        'total sperm produced carry the X-chromosome and the rest 50 per cent has Y-chromosome '
                        'besides the autosomes." (percentage: 50 per cent)'),
    ("4.6.1", "fact", '"Females, however, produce only one type of ovum with an X-chromosome."'),
    ("4.6.1", "fact", '"There is an equal probability of fertilisation of the ovum with the sperm carrying either X '
                      'or Y chromosome. In case the ovum fertilises with a sperm carrying X-chromosome the zygote '
                      'develops into a female (XX) and the fertilisation of ovum with Y-chromosome carrying sperm '
                      'results into a male offspring."'),
    ("4.6.1", "fact", '"Thus, it is evident that it is the genetic make up of the sperm that determines the sex of '
                      'the child."'),
    ("4.6.1", "number", '"It is also evident that in each pregnancy there is always 50 per cent probability of '
                        'either a male or a female child." (percentage: 50 per cent)'),
    ("4.6.1", "fact", '"It is unfortunate that in our society women are blamed for giving birth to female children '
                      'and have been ostracised and ill-treated because of this false notion."'),

    ("4.6.2", "heading", '"4.6.2 Sex Determination in Honey Bee"'),
    ("4.6.2", "opener", '"The sex determination in honey bee is based on the number of sets of chromosomes an '
                        'individual receives."'),
    ("4.6.2", "fact", '"An offspring formed from the union of a sperm and an egg develops as a female (queen or '
                      'worker), and an unfertilised egg develops as a male (drone) by means of parthenogenesis."'),
    ("4.6.2", "number", '"This means that the males have half the number of chromosomes than that of a female. The '
                        'females are diploid having 32 chromosomes and males are haploid, i.e., having 16 '
                        'chromosomes." (counts: 32, 16)'),
    ("4.6.2", "definition", '"This is called as haplodiploid sex-determination system and has special '
                            'characteristic features such as the males produce sperms by mitosis (Figure 4.13), '
                            'they do not have father and thus cannot have sons, but have a grandfather and can '
                            'have grandsons."'),
    ("4.6.2", "question", '"How is the sex-determination mechanism different in the birds?"'),
    ("4.6.2", "question", '"Is the sperm or the egg responsible for the sex of the chicks?"'),

    ("Fig 4.13a", "caption", 'Figure 4.13 caption (verbatim, p21): "Figure 4.13 Sex determination in honey bee" '
                             '(the source prints a SECOND Figure 4.13 on p22 - see the pedigree-symbol row)'),
    ("Fig 4.13a", "figure-labels", 'Figure labels: "Parents"; "Gametes:"; "Female"; "32"; "Male"; "16"; "Meiosis"; '
                                   '"Mitosis"; "F1:"; "Female"; "32"; "Male"; "16"'),

    # ---------------------------------------------------------------- page 22
    ("4.7", "heading", '"4.7 MUTATION"'),
    ("4.7", "opener", '"Mutation is a phenomenon which results in alteration of DNA sequences and consequently '
                      'results in changes in the genotype and the phenotype of an organism."'),
    ("4.7", "fact", '"In addition to recombination, mutation is another phenomenon that leads to variation in '
                    'DNA."'),
    ("4.7", "fact", '"As you will learn in Chapter 5, one DNA helix runs continuously from one end to the other in '
                    'each chromatid, in a highly supercoiled form."'),
    ("4.7", "fact", '"Therefore loss (deletions) or gain (insertion/duplication) of a segment of DNA, result in '
                    'alteration in chromosomes. Since genes are known to be located on chromosomes, alteration in '
                    'chromosomes results in abnormalities or aberrations."'),
    ("4.7", "fact", '"Chromosomal aberrations are commonly observed in cancer cells."'),
    ("4.7", "definition", '"In addition to the above, mutation also arise due to change in a single base pair of '
                          'DNA. This is known as point mutation. A classical example of such a mutation is sickle '
                          'cell anemia."'),
    ("4.7", "fact", '"Deletions and insertions of base pairs of DNA, causes frame-shift mutations (see Chapter 5)."'),
    ("4.7", "fact", '"The mechanism of mutation is beyond the scope of this discussion, at this level."'),
    ("4.7", "definition", '"However, there are many chemical and physical factors that induce mutations. These are '
                          'referred to as mutagens. UV radiations can cause mutations in organisms - it is a '
                          'mutagen."'),

    ("4.8", "heading", '"4.8 GENETIC DISORDERS"'),
    ("4.8.1", "heading", '"4.8.1 Pedigree Analysis"'),
    ("4.8.1", "opener", '"The idea that disorders are inherited has been prevailing in the human society since '
                        'long. This was based on the heritability of certain characteristic features in families."'),
    ("4.8.1", "fact", '"After the rediscovery of Mendel\'s work the practice of analysing inheritance pattern of '
                      'traits in human beings began."'),
    ("4.8.1", "fact", '"Since it is evident that control crosses that can be performed in pea plant or some other '
                      'organisms, are not possible in case of human beings, study of the family history about '
                      'inheritance of a particular trait provides an alternative."'),
    ("4.8.1", "definition", '"Such an analysis of traits in several of generations of a family is called the '
                            'pedigree analysis. In the pedigree analysis the inheritance of a particular trait is '
                            'represented in the family tree over generations."'),
    ("4.8.1", "fact", '"In human genetics, pedigree study provides a strong tool, which is utilised to trace the '
                      'inheritance of a specific trait, abnormality or disease."'),
    ("4.8.1", "fact", '"Some of the important standard symbols used in the pedigree analysis have been shown in '
                      'Figure 4.13."'),
    ("4.8.1", "fact", '"As you have studied in this chapter, each and every feature in any organism is controlled '
                      'by one or the other gene located on the DNA present in the chromosome."'),

    ("Fig 4.13b", "caption", 'Figure 4.13 caption (verbatim, p22): "Figure 4.13 Symbols used in the human pedigree '
                             'analysis" - the source re-uses the number 4.13 here; the honey bee plate on p21 is '
                             'also numbered 4.13'),
    ("Fig 4.13b", "figure-labels", 'Figure labels: "Male"; "female"; "sex unspecified"; "affected individuals"; '
                                   '"mating"; "mating between relatives (consanguineous mating)"; "parents above '
                                   'and children below (in order of birth - left to right)"; "parents with male '
                                   'child affected with disease"; "five unaffected offspring"'),

    # ---------------------------------------------------------------- page 23
    ("4.8.1", "fact", '"DNA is the carrier of genetic information. It is hence transmitted from one generation to '
                      'the other without any change or alteration."'),
    ("4.8.1", "fact", '"However, changes or alteration do take place occasionally. Such an alteration or change in '
                      'the genetic material is referred to as mutation."'),
    ("4.8.1", "fact", '"A number of disorders in human beings have been found to be associated with the inheritance '
                      'of changed or altered genes or chromosomes."'),

    ("4.8.2", "heading", '"4.8.2 Mendelian Disorders"'),
    ("4.8.2", "opener", '"Broadly, genetic disorders may be grouped into two categories - Mendelian disorders and '
                        'Chromosomal disorders."'),
    ("4.8.2", "definition", '"Mendelian disorders are mainly determined by alteration or mutation in the single '
                            'gene."'),
    ("4.8.2", "fact", '"These disorders are transmitted to the offspring on the same lines as we have studied in '
                      'the principle of inheritance. The pattern of inheritance of such Mendelian disorders can be '
                      'traced in a family by the pedigree analysis."'),
    ("4.8.2", "example", '"Most common and prevalent Mendelian disorders are Haemophilia, Cystic fibrosis, Sickle '
                         'cell anaemia, Colour blindness, Phenylketonuria, Thalassemia, etc."'),
    ("4.8.2", "fact", '"It is important to mention here that such Mendelian disorders may be dominant or '
                      'recessive."'),
    ("4.8.2", "fact", '"By pedigree analysis one can easily understand whether the trait in question is dominant or '
                      'recessive. Similarly, the trait may also be linked to the sex chromosome as in case of '
                      'haemophilia."'),
    ("4.8.2", "fact", '"It is evident that this X-linked recessive trait shows transmission from carrier female to '
                      'male progeny."'),
    ("4.8.2", "question", '"A representative pedigree is shown in Figure 4.14 for dominant and recessive traits. '
                          'Discuss with your teacher and design pedigrees for characters linked to both autosomes '
                          'and sex chromosome."'),

    ("Fig 4.14", "caption", 'Figure 4.14 caption (verbatim): "Figure 4.14 Representative pedigree analysis of '
                            '(a) Autosomal dominant trait (for example: Myo tonic dystrophy) (b) Autosomal recessive '
                            'trait (for example: Sickle-cell anaemia)" (NCERT prints "Myo tonic" split across the '
                            'line break)'),
    ("Fig 4.14", "figure-labels", 'Figure labels: "(a)"; "(b)"'),

    ("4.8.2", "definition", '"Colour Blindness: It is a sex-linked recessive disorder due to defect in either red '
                            'or green cone of eye resulting in failure to discriminate between red and green '
                            'colour."'),
    ("4.8.2", "fact", '"This defect is due to mutation in certain genes present in the X chromosome."'),
    ("4.8.2", "number", '"It occurs in about 8 per cent of males and only about 0.4 per cent of females." '
                        '(percentages: 8 per cent, 0.4 per cent)'),
    ("4.8.2", "fact", '"This is because the genes that lead to red-green colour blindness are on the X chromosome. '
                      'Males have only one X chromosome and females have two."'),
    ("4.8.2", "number", '"The son of a woman who carries the gene has a 50 per cent chance of being colour blind. '
                        'The mother is not herself colour blind because the gene is recessive. That means that its '
                        'effect is suppressed by her matching dominant normal gene." (percentage: 50 per cent)'),
    ("4.8.2", "fact", '"A daughter will not normally be colour blind, unless her mother is a carrier and her father '
                      'is colour blind."'),

    # ---------------------------------------------------------------- page 24
    ("4.8.2", "fact", '"Haemophilia: This sex linked recessive disease, which shows its transmission from '
                      'unaffected carrier female to some of the male progeny has been widely studied."'),
    ("4.8.2", "fact", '"In this disease, a single protein that is a part of the cascade of proteins involved in the '
                      'clotting of blood is affected."'),
    ("4.8.2", "fact", '"Due to this, in an affected individual a simple cut will result in non-stop bleeding."'),
    ("4.8.2", "fact", '"The heterozygous female (carrier) for haemophilia may transmit the disease to sons."'),
    ("4.8.2", "exception", '"The possibility of a female becoming a haemophilic is extremely rare because mother of '
                           'such a female has to be at least carrier and the father should be haemophilic (unviable '
                           'in the later stage of life)."'),
    ("4.8.2", "example", '"The family pedigree of Queen Victoria shows a number of haemophilic descendents as she '
                         'was a carrier of the disease."'),
    ("4.8.2", "definition", '"Sickle-cell anaemia: This is an autosome linked recessive trait that can be '
                            'transmitted from parents to the offspring when both the partners are carrier for the '
                            'gene (or heterozygous)."'),
    ("4.8.2", "fact", '"The disease is controlled by a single pair of allele, HbA and HbS."'),
    ("4.8.2", "fact", '"Out of the three possible genotypes only homozygous individuals for HbS (HbSHbS) show the '
                      'diseased phenotype."'),
    ("4.8.2", "number", '"Heterozygous (HbAHbS) individuals appear apparently unaffected but they are carrier of '
                        'the disease as there is 50 per cent probability of transmission of the mutant gene to the '
                        'progeny, thus exhibiting sickle-cell trait (Figure 4.15)." (percentage: 50 per cent)'),
    ("4.8.2", "fact", '"The defect is caused by the substitution of Glutamic acid (Glu) by Valine (Val) at the '
                      'sixth position of the beta globin chain of the haemoglobin molecule."'),
    ("4.8.2", "fact", '"The substitution of amino acid in the globin protein results due to the single base '
                      'substitution at the sixth codon of the beta globin gene from GAG to GUG."'),
    ("4.8.2", "fact", '"The mutant haemoglobin molecule undergoes polymerisation under low oxygen tension causing '
                      'the change in the shape of the RBC from biconcave disc to elongated sickle like structure '
                      '(Figure 4.15)."'),

    ("Fig 4.15", "caption", 'Figure 4.15 caption (verbatim): "Figure 4.15 Micro graph of the red blood cells and '
                            'the amino acid composition of the relevant portion of beta-chain of haemoglobin: '
                            '(a) From a normal individual; (b) From an individual with sickle-cell anaemia" '
                            '(NCERT prints "Micro graph" split across the line break)'),
    ("Fig 4.15", "figure-labels", 'Figure labels: "(a)"; "(b)"; "Normal Hb(A) gene"; "Sickle-cell Hb(S) gene"; '
                                  '"mRNA GAG"; "mRNA GUG"; "HbA peptide"; "HbS peptide"; "Val His Leu Thr Pro Glu '
                                  'Glu"; "Val His Leu Thr Pro Val Glu"; "1"; "2"; "3"; "4"; "5"; "6"; "7"; "8"'),

    # ---------------------------------------------------------------- page 25
    ("4.8.2", "definition", '"Phenylketonuria: This inborn error of metabolism is also inherited as the autosomal '
                            'recessive trait."'),
    ("4.8.2", "fact", '"The affected individual lacks an enzyme that converts the amino acid phenylalanine into '
                      'tyrosine."'),
    ("4.8.2", "fact", '"As a result of this phenylalanine is accumulated and converted into phenylpyruvic acid and '
                      'other derivatives."'),
    ("4.8.2", "fact", '"Accumulation of these in brain results in mental retardation."'),
    ("4.8.2", "fact", '"These are also excreted through urine because of its poor absorption by kidney."'),
    ("4.8.2", "definition", '"Thalassemia: This is also an autosome-linked recessive blood disease transmitted from '
                            'parents to the offspring when both the partners are unaffected carrier for the gene '
                            '(or heterozygous)."'),
    ("4.8.2", "fact", '"The defect could be due to either mutation or deletion which ultimately results in reduced '
                      'rate of synthesis of one of the globin chains (alpha and beta chains) that make up '
                      'haemoglobin. This causes the formation of abnormal haemoglobin molecules resulting into '
                      'anaemia which is characteristic of the disease."'),
    ("4.8.2", "fact", '"Thalassemia can be classified according to which chain of the haemoglobin molecule is '
                      'affected. In alpha Thalassemia, production of alpha globin chain is affected while in beta '
                      'Thalassemia, production of beta globin chain is affected."'),
    ("4.8.2", "number", '"alpha Thalassemia is controlled by two closely linked genes HBA1 and HBA2 on chromosome '
                        '16 of each parent and it is observed due to mutation or deletion of one or more of the '
                        'four genes. The more genes affected, the less alpha globin molecules produced." '
                        '(chromosome: 16; counts: two genes, four genes)'),
    ("4.8.2", "number", '"While beta Thalassemia is controlled by a single gene HBB on chromosome 11 of each parent '
                        'and occurs due to mutation of one or both the genes." (chromosome: 11)'),
    ("4.8.2", "comparison", '"Thalassemia differs from sickle-cell anaemia in that the former is a quantitative '
                            'problem of synthesising too few globin molecules while the latter is a qualitative '
                            'problem of synthesising an incorrectly functioning globin."'),

    ("4.8.3", "heading", '"4.8.3 Chromosomal Disorders"'),
    ("4.8.3", "opener", '"The chromosomal disorders on the other hand are caused due to absence or excess or '
                        'abnormal arrangement of one or more chromosomes."'),
    ("4.8.3", "definition", '"Failure of segregation of chromatids during cell division cycle results in the gain '
                            'or loss of a chromosome(s), called aneuploidy."'),
    ("4.8.3", "example", '"For example Down\'s syndrome results in the gain of extra copy of chromosome 21."'),
    ("4.8.3", "example", '"Similarly, Turner\'s syndrome results due to loss of an X chromosome in human '
                         'females."'),
    ("4.8.3", "definition", '"Failure of cytokinesis after telophase stage of cell division results in an increase '
                            'in a whole set of chromosomes in an organism and, this phenomenon is known as '
                            'polyploidy. This condition is often seen in plants."'),
    ("4.8.3", "number", '"The total number of chromosomes in a normal human cell is 46 (23 pairs). Out of these 22 '
                        'pairs are autosomes and one pair of chromosomes are sex chromosome." '
                        '(counts: 46, 23 pairs, 22 pairs)'),
    ("4.8.3", "fact", '"Sometimes, though rarely, either an additional copy of a chromosome may be included in an '
                      'individual or an individual may lack one of any one pair of chromosomes."'),

    # ---------------------------------------------------------------- page 26
    ("4.8.3", "definition", '"These situations are known as trisomy or monosomy of a chromosome, respectively. '
                            'Such a situation leads to very serious consequences in the individual."'),
    ("4.8.3", "example", '"Down\'s Syndrome, Turner\'s syndrome, Klinefelter\'s syndrome are common examples of '
                         'chromosomal disorders."'),
    ("4.8.3", "fact", '"Down\'s Syndrome: The cause of this genetic disorder is the presence of an additional copy '
                      'of the chromosome number 21 (trisomy of 21)."'),
    ("4.8.3", "number", '"This disorder was first described by Langdon Down (1866)." (date: 1866)'),
    ("4.8.3", "fact", '"The affected individual is short statured with small round head, furrowed tongue and '
                      'partially open mouth (Figure 4.16). Palm is broad with characteristic palm crease. Physical, '
                      'psychomotor and mental development is retarded."'),
    ("4.8.3", "number", '"Klinefelter\'s Syndrome: This genetic disorder is also caused due to the presence of an '
                        'additional copy of X chromosome resulting into a karyotype of 47, XXY." '
                        '(karyotype: 47, XXY)'),
    ("4.8.3", "fact", '"Such an individual has overall masculine development, however, the feminine development '
                      '(development of breast, i.e., Gynaecomastia) is also expressed (Figure 4.17a). Such '
                      'individuals are sterile."'),
    ("4.8.3", "number", '"Turner\'s Syndrome: Such a disorder is caused due to the absence of one of the X '
                        'chromosomes, i.e., 45 with X0, Such females are sterile as ovaries are rudimentary besides '
                        'other features including lack of other secondary sexual characters (Figure 4.17b)." '
                        '(karyotype: 45, X0)'),

    ("Fig 4.16", "caption", 'Figure 4.16 caption (verbatim): "Figure 4.16 A representative figure showing an '
                            'individual inflicted with Down\'s syndrome and the corresponding chromosomes of the '
                            'individual"'),
    ("Fig 4.16", "figure-labels", 'Figure labels: "Broad flat face"; "Flat back of head"; "Many \'loops\' on finger '
                                  'tips"; "Palm crease"; "Big and wrinkled tongue"; "Congenital heart disease"; '
                                  '"60"'),
    ("Fig 4.17", "caption", 'Figure 4.17 caption (verbatim): "Figure 4.17 Diagrammatic representation of genetic '
                            'disorders due to sex chromosome composition in humans: (a) Klinefelter Syndrome; '
                            '(b) Turner\'s Syndrome" (NCERT prints "represe-ntation" hyphenated at the line break)'),
    ("Fig 4.17", "figure-labels", 'Figure labels: "(a)"; "(b)"; "Tall stature with feminised character (development '
                                  'of breast, i.e., Gynaecomastia)"; "Short stature and under developed feminine '
                                  'character"'),
]
