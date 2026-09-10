# -*- coding: utf-8 -*-
"""Pass-1 rows, part D — the five SUMMARY-UNIQUE sentences (p27), folded into
their body homes so Pass 2 cannot drop them.

Every other summary sentence is BODY-PRESENT: see SUMMARY_CLASS below, which
is rendered into the inventory's "Summary classification" table.
"""

ROWS = [
    ("ch4", "summary-unique",
     '"Genetics is a branch of biology which deals with principles of inheritance and its practices." '
     '(SUMMARY-UNIQUE wording - the body defines Genetics by what it deals with, not by "principles ... and '
     'its practices")'),
    ("ch4", "summary-unique",
     '"Progeny resembling the parents in morphological and physiological features has attracted the attention of '
     'many biologists." (SUMMARY-UNIQUE - "morphological and physiological" appears nowhere in the body)'),
    ("ch4", "summary-unique",
     '"Mendel was the first to study this phenomenon systematically." (SUMMARY-UNIQUE - the body never claims '
     'Mendel was first, nor uses "systematically")'),
    ("4.6", "summary-unique",
     '"In chicken, sex chromosomes in male are ZZ, and in females are ZW." (SUMMARY-UNIQUE - the body speaks of '
     'birds generally, never names the chicken)'),
    ("4.8.3", "summary-unique",
     '"These can be easily studied by analysis of Karyotypes." (SUMMARY-UNIQUE - "Karyotypes" as an analytical '
     'tool appears only here; the body gives "a karyotype of 47, XXY")'),
]

# (summary sentence as printed, BODY-PRESENT / SUMMARY-UNIQUE, fold target)
SUMMARY_CLASS = [
    ('"Genetics is a branch of biology which deals with principles of inheritance and its practices."',
     "SUMMARY-UNIQUE", "F-fold 1"),
    ('"Progeny resembling the parents in morphological and physiological features has attracted the attention of '
     'many biologists."', "SUMMARY-UNIQUE", "F-fold 2"),
    ('"Mendel was the first to study this phenomenon systematically."', "SUMMARY-UNIQUE", "F-fold 3"),
    ('"While studying the pattern of inheritance in pea plants of contrasting characters, Mendel proposed the '
     "principles of inheritance, which are today referred to as 'Mendel's Laws of Inheritance'.\"",
     "BODY-PRESENT", "4.1 rows"),
    ('"He proposed that the \'factors\' (later named as genes) regulating the characters are found in pairs known '
     'as alleles."', "BODY-PRESENT", "4.2 rows"),
    ('"He observed that the expression of the characters in the offspring follow a definite pattern in '
     'different-first generations (F1), second (F2) and so on."', "BODY-PRESENT", "4.2 rows"),
    ('"Some characters are dominant over others."', "BODY-PRESENT", "4.2 rows"),
    ('"The dominant characters are expressed when factors are in heterozygous condition (Law of Dominance)."',
     "BODY-PRESENT", "4.2.1 rows"),
    ('"The recessive characters are only expressed in homozygous conditions."', "BODY-PRESENT",
     "4.2.1 rows"),
    ('"The characters never blend in heterozygous condition."', "BODY-PRESENT", "4.2 rows"),
    ('"A recessive character that was not expressed in heterozygous conditon may be expressed again when it '
     'becomes homozygous." (NCERT spelling "conditon" preserved)', "BODY-PRESENT", "4.2 rows"),
    ('"Hence, characters segregate while formation of gametes (Law of Segregation)."', "BODY-PRESENT",
     "4.2.2 rows"),
    ('"Not all characters show true dominance. Some characters show incomplete, and some show co-dominance."',
     "BODY-PRESENT", "4.2.2.1 / 4.2.2.2 rows"),
    ('"When Mendel studied the inheritance of two characters together, it was found that the factors '
     'independently assort and combine in all permutations and combinations (Law of Independent Assortment)."',
     "BODY-PRESENT", "4.3.1 rows"),
    ("\"Different combinations of gametes are theoretically represented in a square tabular form known as "
     "'Punnett Square'.\"", "BODY-PRESENT", "4.2 rows (Punnett square)"),
    ('"The factors (now known as gene) on chromosomes regulating the characters are called the genotype and the '
     'physical expression of the chraracters is called phenotype." (NCERT spelling "chraracters" preserved)',
     "BODY-PRESENT", "4.2 rows (genotype/phenotype)"),
    ('"After knowing that the genes are located on the chromosomes, a good correlation was drawn between '
     "Mendel's laws: segregation and assortment of chromosomes during meiosis. The Mendel's laws were extended "
     "in the form of 'Chromosomal Theory of Inheritance'.\"", "BODY-PRESENT", "4.3.2 rows"),
    ('"Later, it was found that Mendel\'s law of independent assortment does not hold true for the genes that '
     'were located on the same chromosomes. These genes were called as linked genes."', "BODY-PRESENT",
     "4.3.3 rows"),
    ("\"'Closely located genes assorted together, and distantly located genes, due to recombination, assorted "
     'independently. Linkage maps, therefore, corresponded to arrangement of genes on a chromosome."',
     "BODY-PRESENT", "4.3.3 rows (Sturtevant)"),
    ('"Many genes were linked to sexes also, and called as sex-linked genes."', "BODY-PRESENT",
     "4.3.3 / 4.8.2 rows"),
    ('"The two sexes (male and female) were found to have a set of chromosomes which were common, and another '
     'set which was different. The chromosomes which were different in two sexes were named as sex chromosomes. '
     'The remaining set was named as autosomes."', "BODY-PRESENT", "4.6 rows"),
    ('"In humans, a normal female has 22 pairs of autosomes and a pair of sex chromosomes (Xx). A male has 22 '
     'pairs of autosomes and a pair of sex chromosome as XY." (NCERT prints "Xx")', "BODY-PRESENT",
     "4.6.1 rows"),
    ('"In chicken, sex chromosomes in male are ZZ, and in females are ZW."', "SUMMARY-UNIQUE", "F-fold 4"),
    ('"Mutation is defined as change in the genetic material."', "BODY-PRESENT", "4.8.1 rows"),
    ('"A point mutation is a change of a single base pair in DNA."', "BODY-PRESENT", "4.7 rows"),
    ('"Sickle-cell anemia is caused due to change of one base in the gene coding for beta-chain of hemoglobin."',
     "BODY-PRESENT", "4.8.2 rows"),
    ('"Inheritable mutations can be studied by generating a pedigree of a family."', "BODY-PRESENT",
     "4.8.1 rows"),
    ('"Some mutations involve changes in whole set of chromosomes (polyploidy) or change in a subset of '
     'chromosome number (aneuploidy)."', "BODY-PRESENT", "4.8.3 rows"),
    ('"This helped in understanding the mutational basis of genetic disorders."', "BODY-PRESENT",
     "4.8.3 rows"),
    ('"Down\'s syndrome is due to trisomy of chromosome 21, where there is an extra copy of chromosome 21 and '
     'consequently the total number of chromosome becomes 47."', "BODY-PRESENT", "4.8.3 rows"),
    ('"In Turner\'s syndrome, one X chromosome is missing and the sex chromosome is as X0, and in '
     "Klinefelter's syndrome, the condition is XXY.\"", "BODY-PRESENT", "4.8.3 rows"),
    ('"These can be easily studied by analysis of Karyotypes."', "SUMMARY-UNIQUE", "F-fold 5"),
]

# Exercise scan (Rule 2).  (question, classification, where answered)
EXERCISES = [
    ("Q1", "GAP",
     "Mention the advantages of selecting pea plant for experiment by Mendel. The body never lists them as "
     "'advantages': it gives true-breeding lines (4.1), stable expression over generations under continuous "
     "self-pollination (4.1), characters with two opposing traits (4.1), artificial cross-pollination (4.1) and a "
     "large sampling size (4.1). Answer must be assembled from exactly those five body facts and marked as such - "
     "no fact outside the source may be added."),
    ("Q2", "COVERED",
     "Differentiate between (a) Dominance and Recessive - 4.2 / 4.2.1; (b) Homozygous and Heterozygous - 4.2; "
     "(c) Monohybrid and Dihybrid - 4.2 and 4.3."),
    ("Q3", "GAP",
     "A diploid organism is heterozygous for 4 loci, how many types of gametes can be produced? The body states "
     "four gamete types for two heterozygous loci (4.3.1) but never gives the general 2^n rule. The answer must "
     "be presented as an extension of the 4.3.1 statement (16 types, each 1/16), visibly attributed as reasoning "
     "from the source rather than as source text."),
    ("Q4", "COVERED", "Explain the Law of Dominance using a monohybrid cross - 4.2.1 plus the 4.2 cross."),
    ("Q5", "COVERED", "Define and design a test-cross - 4.2 (testcross definition, Figure 4.5)."),
    ("Q6", "GAP",
     "Using a Punnett Square, workout the distribution of phenotypic features in the first filial generation "
     "after a cross between a homozygous female and a heterozygous male for a single locus. The body works "
     "TT x tt and the testcross (heterozygote x recessive parent) but never the homozygous x heterozygous case. "
     "Answer from the Law of Dominance rows (4.2.1): 1:1 genotypic, all dominant phenotypically."),
    ("Q7", "GAP",
     "Cross between tall plant with yellow seeds (TtYy) and tall plant with green seed (Ttyy) - proportions of "
     "(a) tall and green, (b) dwarf and green. The body never works this cross; answer must be derived from the "
     "4.3.1 gamete-frequency rows (RY, Ry, rY, ry at 25 per cent each) and marked as worked-out, not NCERT text."),
    ("Q8", "COVERED",
     "Two heterozygous parents crossed, two loci linked - distribution of phenotypic features in the F1 "
     "generation for a dihybrid cross: 4.3.3 (parental combinations much higher than non-parental)."),
    ("Q9", "COVERED", "Contribution of T.H. Morgan in genetics - 4.3.2 and 4.3.3."),
    ("Q10", "COVERED", "What is pedigree analysis and how is it useful - 4.8.1."),
    ("Q11", "COVERED", "How is sex determined in human beings - 4.6.1."),
    ("Q12", "COVERED",
     "Child has blood group O, father A, mother B - genotypes of the parents and of the other offspring: "
     "Table 4.2 plus 4.2.2.2 (IAIB/IAi/IBi/ii genotypes)."),
    ("Q13", "COVERED", "Co-dominance and incomplete dominance with example - 4.2.2.1 and 4.2.2.2."),
    ("Q14", "COVERED", "Point mutation with one example - 4.7 (sickle cell anemia)."),
    ("Q15", "COVERED", "Who proposed the chromosomal theory of inheritance - 4.3.2 (Walter Sutton and "
                       "Theodore Boveri)."),
    ("Q16", "COVERED",
     "Any two autosomal genetic disorders with their symptoms - 4.8.2 (Sickle-cell anaemia, Phenylketonuria, "
     "Thalassemia)."),
]
