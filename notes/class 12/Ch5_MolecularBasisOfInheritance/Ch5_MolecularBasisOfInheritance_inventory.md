# Working Inventory (NOT FROZEN) — Molecular Basis of Inheritance (Class 12, Chapter 5)

> The `# Frozen Inventory` title used by completed chapters is deliberately **withheld** until `1-Z` actually freezes this file. A naive `grep -i frozen` on the old title would have reported this chapter as frozen while six sweeps were still outstanding.

Source: `Chapter/class 12/Chapter 5 - Molecular Basis of Inheritance.pdf` (31 pp) | Status: **NOT FROZEN — Pass 1a in progress** | Rows so far: **231** (`F001`..`F231`)

**Big-chapter protocol (§6, 5 passes).** 31 source pages, 10 numbered sections plus summary and exercises, so this chapter runs `1a → 1b → 2a → 2b → 3`. The source seam is:

- **Pass 1a — first half:** chapter introduction + §5.1 The DNA, §5.2 The Search for Genetic Material, §5.3 RNA World, §5.4 Replication, §5.5 Transcription (source pp. 1–17, book pp. 79–95, up to but excluding the `5.6 GENETIC CODE` banner).
- **Pass 1b — second half:** §5.6 Genetic Code, §5.7 Translation, §5.8 Regulation of Gene Expression, §5.9 Human Genome Project, §5.10 DNA Fingerprinting, Summary and Exercises (source pp. 17–31).

Per §6, `1a/1b` halve the **source**; `1-S / 1-H / 1-O / 1-F / 1-Z` separate the **kinds of work**. The sweeps therefore run per half (1a-S, 1a-H, 1a-O, then 1b-S, 1b-H, 1b-O), while **figures run as one whole-chapter 1-F session** and the freeze as one whole-chapter 1-Z. Gate 1 is evaluated over the whole chapter only after 1b.

Tick legend: `x` = written into the script and verified present in the generated PDF. **No row is ticked — Pass 2 has not started.**

## Session log — Pass 1

| Session | Scope | State | Rows added (machine-derived) |
|---|---|---|---|
| **1a-S** — source read & prose inventory, first half | intro + §5.1–§5.5 | **done** (this session) | **231** (`F001`..`F231`) |
| **1a-H** — heading sweep, first half | intro + §5.1–§5.5 | not started | — |
| **1a-O** — opener sweep, first half | intro + §5.1–§5.5 | not started | — |
| **1b-S** — source read & prose inventory, second half | §5.6–§5.10 + Summary + Exercises | not started | — |
| **1b-H** — heading sweep, second half | §5.6–§5.10 | not started | — |
| **1b-O** — opener sweep, second half | §5.6–§5.10 | not started | — |
| **1-F** — figures, whole chapter (single session) | all figures 5.1–5.16 | not started | — |
| **1-Z** — gaps, summary & freeze, whole chapter | steps 7–10 | not started | — |

Environment re-established this session per §0.2–§0.3: `/vercel/share/neetenv` was **absent** (expected — it does not survive a session boundary) and was rebuilt. CPython 3.13.11 @ `/vercel/share/neetenv`, reportlab 5.0.1, pdfplumber OK, pymupdf 1.28.2, Pillow 12.3.0.

## Header counts — machine-derived (§6 Pass 1 step 10), never hand-tallied

| Count | Value |
|---|---|
| Facts rows so far | **231** (`F001`..`F231`) — first half only |
| ID range / contiguity | F001..F231 — 0 gaps, 0 duplicates (re-parsed from the table below) |
| `Type: heading` rows | **0** — owned by sessions 1a-H / 1b-H, deliberately absent here |
| `Type: opener` rows | **0** — owned by sessions 1a-O / 1b-O, deliberately absent here |
| Figure-label rows | **0** — owned by session 1-F |
| Label strings parsed by `check_pdf.py`'s own `_extract_labels` | **0 labels, 0 figures, no phantom `Fig #` row** — re-run against this file this session; the empty-matrix state is the expected pre-1-F result |
| `Type` values used (normalized, lower-case) | `concept` 149 · `definition` 28 · `number` 16 · `list` 15 · `question` 11 · `name` 9 · `example` 3 = 231; no other value present |
| Rows ticked | **0** — Pass 2 not started |
| Summary sentences classified | not started (1-Z) |
| Exercise-gap terms | not started (1-Z) |
| Figures in manifest | not started (1-F) |

Every number above was produced by re-parsing this file's Facts table with a script (§6 step 10), not by hand tally: 231 rows, `F001..F231`, **0 gaps, 0 duplicates**, and the `Type` column asserted to contain only the seven values listed. The census is derivable from its own list — `149 + 28 + 16 + 15 + 11 + 9 + 3 = 231`, matching the row total.

> ## GATE 1 STATUS: **OPEN — blocked. Pass 2 may not begin.**
>
> | Gate 1 requirement (§6) | State |
> |---|---|
> | Environment (§0.2–0.3) re-established | done — venv rebuilt, all four imports verified under that interpreter |
> | Every fact has a Facts row (three source reads) | **partial** — first half done (231 rows); second half is 1b-S |
> | Every heading has a row incl. unnumbered sub-headings | **not started** — 1a-H, 1b-H |
> | Every section's opening sentence has a row | **not started** — 1a-O, 1b-O |
> | Every in-figure label has a matrix row, harvested by opening each rendered asset | **not started** — 1-F |
> | Every figure `Mono: yes` and `Verified: yes` | **not started** — 1-F |
> | Inventory validated by running `check_pdf.py`'s own `_extract_labels` | **not started** — meaningful only after 1-F |
> | Header counts match a re-parse of the table; IDs contiguous | done for the rows that exist — re-parsed this session |
> | Exercise-gap terms and SUMMARY-UNIQUE folding | **not started** — 1-Z |
> | Pass 1's sessions have each run and reported a machine-derived count | **1 of 8 sweep sessions** (`1a-S`) — this file's Session log counts the 8 sweeps only; `Ch5_TRACKER.md` §2 counts **9** because it adds the closing step-10 machine re-parse as its own row. Same state, two denominators: 8 sweeps + 1 verification = 9 ledger sessions. |
> | Inventory file saved to the chapter folder | done — this file |

## Facts

Scope of this table after session 1a-S: **prose facts of the first half only**. Headings and section-opening sentences are **deliberately excluded** — they are the sole deliverables of sessions 1a-H and 1a-O respectively (§6 Pass 1 step 3: "This step does not cover headings or openers"). Where an opener carries a definition that the rest of a section leans on, it is listed in the carry-over list below as a pointer for 1a-O, **not** absorbed as a row here.

| ID | Section | Type | Exact original wording | Ticked |
|----|---------|------|------------------------|--------|
| F001 | Intro | concept | "At the time of Mendel, the nature of those 'factors' regulating the pattern of inheritance was not clear." | |
| F002 | Intro | concept | "Over the next hundred years, the nature of the putative genetic material was investigated culminating in the realisation that DNA - deoxyribonucleic acid - is the genetic material, at least for the majority of organisms." | |
| F003 | Intro | concept | "In class XI you have learnt that nucleic acids are polymers of nucleotides." | |
| F004 | Intro | concept | "Deoxyribonucleic acid (DNA) and ribonucleic acid (RNA) are the two types of nucleic acids found in living systems." | |
| F005 | Intro | concept | "DNA acts as the genetic material in most of the organisms." | |
| F006 | Intro | concept | "RNA though it also acts as a genetic material in some viruses, mostly functions as a messenger." | |
| F007 | Intro | concept | "RNA has additional roles as well. It functions as adapter, structural, and in some cases as a catalytic molecule." | |
| F008 | Intro | concept | "In Class XI you have already learnt the structures of nucleotides and the way these monomer units are linked to form nucleic acid polymers." | |
| F009 | Intro | concept | "In this chapter we are going to discuss the structure of DNA, its replication, the process of making RNA from DNA (transcription), the genetic code that determines the sequences of amino acids in proteins, the process of protein synthesis (translation) and elementary basis of their regulation." | |
| F010 | Intro | concept | "The determination of complete nucleotide sequence of human genome during last decade has set in a new era of genomics." | |
| F011 | Intro | concept | "In the last section, the essentials of human genome sequencing and its consequences will also be discussed." | |
| F012 | Intro | concept | "Let us begin our discussion by first understanding the structure of the most interesting molecule in the living system, that is, the DNA." | |
| F013 | Intro | concept | "In subsequent sections, we will understand that why it is the most abundant genetic material, and what its relationship is with RNA." | |
| F014 | 5.1 | concept | "The length of DNA is usually defined as number of nucleotides (or a pair of nucleotide referred to as base pairs) present in it." | |
| F015 | 5.1 | concept | "This also is the characteristic of an organism." | |
| F016 | 5.1 | number | "a bacteriophage known as phi x 174 has 5386 nucleotides" | |
| F017 | 5.1 | number | "Bacteriophage lambda has 48502 base pairs (bp)" | |
| F018 | 5.1 | number | "Escherichia coli has 4.6 x 10^6 bp" | |
| F019 | 5.1 | number | "haploid content of human DNA is 3.3 x 10^9 bp" | |
| F020 | 5.1.1 | definition | "A nucleotide has three components - a nitrogenous base, a pentose sugar (ribose in case of RNA, and deoxyribose for DNA), and a phosphate group." | |
| F021 | 5.1.1 | definition | "There are two types of nitrogenous bases - Purines (Adenine and Guanine), and Pyrimidines (Cytosine, Uracil and Thymine)." | |
| F022 | 5.1.1 | concept | "Cytosine is common for both DNA and RNA and Thymine is present in DNA." | |
| F023 | 5.1.1 | concept | "Uracil is present in RNA at the place of Thymine." | |
| F024 | 5.1.1 | definition | "A nitrogenous base is linked to the OH of 1' C pentose sugar through a N-glycosidic linkage to form a nucleoside" | |
| F025 | 5.1.1 | example | "such as adenosine or deoxyadenosine, guanosine or deoxyguanosine, cytidine or deoxycytidine and uridine or deoxythymidine" | |
| F026 | 5.1.1 | definition | "When a phosphate group is linked to OH of 5' C of a nucleoside through phosphoester linkage, a corresponding nucleotide (or deoxynucleotide depending upon the type of sugar present) is formed." | |
| F027 | 5.1.1 | definition | "Two nucleotides are linked through 3'-5' phosphodiester linkage to form a dinucleotide." | |
| F028 | 5.1.1 | concept | "More nucleotides can be joined in such a manner to form a polynucleotide chain." | |
| F029 | 5.1.1 | concept | "A polymer thus formed has at one end a free phosphate moiety at 5'-end of sugar, which is referred to as 5'-end of polynucleotide chain." | |
| F030 | 5.1.1 | concept | "Similarly, at the other end of the polymer the sugar has a free OH of 3'C group which is referred to as 3'-end of the polynucleotide chain." | |
| F031 | 5.1.1 | concept | "The backbone of a polynucleotide chain is formed due to sugar and phosphates." | |
| F032 | 5.1.1 | concept | "The nitrogenous bases linked to sugar moiety project from the backbone (Figure 5.1)." | |
| F033 | 5.1.1 | concept | "In RNA, every nucleotide residue has an additional -OH group present at 2'-position in the ribose." | |
| F034 | 5.1.1 | concept | "Also, in RNA the uracil is found at the place of thymine (5-methyl uracil, another chemical name for thymine)." | |
| F035 | 5.1.1 | name | "DNA as an acidic substance present in nucleus was first identified by Friedrich Meischer in 1869. He named it as 'Nuclein'." | |
| F036 | 5.1.1 | concept | "However, due to technical limitation in isolating such a long polymer intact, the elucidation of structure of DNA remained elusive for a very long period of time." | |
| F037 | 5.1.1 | name | "It was only in 1953 that James Watson and Francis Crick, based on the X-ray diffraction data produced by Maurice Wilkins and Rosalind Franklin, proposed a very simple but famous Double Helix model for the structure of DNA." | |
| F038 | 5.1.1 | concept | "One of the hallmarks of their proposition was base pairing between the two strands of polynucleotide chains." | |
| F039 | 5.1.1 | name | "However, this proposition was also based on the observation of Erwin Chargaff that for a double stranded DNA, the ratios between Adenine and Thymine and Guanine and Cytosine are constant and equals one." | |
| F040 | 5.1.1 | concept | "The base pairing confers a very unique property to the polynucleotide chains. They are said to be complementary to each other, and therefore if the sequence of bases in one strand is known then the sequence in other strand can be predicted." | |
| F041 | 5.1.1 | concept | "Also, if each strand from a DNA (let us call it as a parental DNA) acts as a template for synthesis of a new strand, the two double stranded DNA (let us call them as daughter DNA) thus, produced would be identical to the parental DNA molecule." | |
| F042 | 5.1.1 | concept | "Because of this, the genetic implications of the structure of DNA became very clear." | |
| F043 | 5.1.1 | list | "(i) It is made of two polynucleotide chains, where the backbone is constituted by sugar-phosphate, and the bases project inside." | |
| F044 | 5.1.1 | list | "(ii) The two chains have anti-parallel polarity. It means, if one chain has the polarity 5'-to-3', the other has 3'-to-5'." | |
| F045 | 5.1.1 | list | "(iii) The bases in two strands are paired through hydrogen bond (H-bonds) forming base pairs (bp). Adenine forms two hydrogen bonds with Thymine from opposite strand and vice-versa. Similarly, Guanine is bonded with Cytosine with three H-bonds." | |
| F046 | 5.1.1 | concept | "As a result, always a purine comes opposite to a pyrimidine. This generates approximately uniform distance between the two strands of the helix (Figure 5.2)." | |
| F047 | 5.1.1 | list | "(iv) The two chains are coiled in a right-handed fashion." | |
| F048 | 5.1.1 | number | "The pitch of the helix is 3.4 nm (a nanometre is one billionth of a metre, that is 10^-9 m) and there are roughly 10 bp in each turn." | |
| F049 | 5.1.1 | number | "Consequently, the distance between a bp in a helix is approximately 0.34 nm." | |
| F050 | 5.1.1 | list | "(v) The plane of one base pair stacks over the other in double helix. This, in addition to H-bonds, confers stability of the helical structure (Figure 5.3)." | |
| F051 | 5.1.1 | question | "Compare the structure of purines and pyrimidines. Can you find out why the distance between two polynucleotide chains in DNA remains almost constant?" | |
| F052 | 5.1.1 | concept | "The proposition of a double helix structure for DNA and its simplicity in explaining the genetic implication became revolutionary." | |
| F053 | 5.1.1 | definition | "Very soon, Francis Crick proposed the Central dogma in molecular biology, which states that the genetic information flows from DNA-to-RNA-to-Protein." | |
| F054 | 5.1.1 | concept | "In some viruses the flow of information is in reverse direction, that is, from RNA to DNA." | |
| F055 | 5.1.1 | question | "Can you suggest a simple name to the process?" | |
| F056 | 5.1.2 | number | "Taken the distance between two consecutive base pairs as 0.34 nm (0.34x10^-9 m)" | |
| F057 | 5.1.2 | number | "6.6 x 10^9 bp x 0.34 x 10^-9 m/bp, it comes out to be approximately 2.2 metres" | |
| F058 | 5.1.2 | number | "A length that is far greater than the dimension of a typical nucleus (approximately 10^-6 m)." | |
| F059 | 5.1.2 | question | "How is such a long polymer packaged in a cell?" | |
| F060 | 5.1.2 | question | "If the length of E. coli DNA is 1.36 mm, can you calculate the number of base pairs in E.coli?" | |
| F061 | 5.1.2 | concept | "In prokaryotes, such as, E. coli, though they do not have a defined nucleus, the DNA is not scattered throughout the cell." | |
| F062 | 5.1.2 | definition | "DNA (being negatively charged) is held with some proteins (that have positive charges) in a region termed as 'nucleoid'." | |
| F063 | 5.1.2 | concept | "The DNA in nucleoid is organised in large loops held by proteins." | |
| F064 | 5.1.2 | concept | "In eukaryotes, this organisation is much more complex. There is a set of positively charged, basic proteins called histones." | |
| F065 | 5.1.2 | concept | "A protein acquires charge depending upon the abundance of amino acids residues with charged side chains." | |
| F066 | 5.1.2 | concept | "Histones are rich in the basic amino acid residues lysine and arginine. Both the amino acid residues carry positive charges in their side chains." | |
| F067 | 5.1.2 | definition | "Histones are organised to form a unit of eight molecules called histone octamer." | |
| F068 | 5.1.2 | definition | "The negatively charged DNA is wrapped around the positively charged histone octamer to form a structure called nucleosome (Figure 5.4 a)." | |
| F069 | 5.1.2 | number | "A typical nucleosome contains 200 bp of DNA helix." | |
| F070 | 5.1.2 | definition | "Nucleosomes constitute the repeating unit of a structure in nucleus called chromatin, thread-like stained (coloured) bodies seen in nucleus." | |
| F071 | 5.1.2 | concept | "The nucleosomes in chromatin are seen as 'beads-on-string' structure when viewed under electron microscope (EM) (Figure 5.4 b)." | |
| F072 | 5.1.2 | question | "Theoretically, how many such beads (nucleosomes) do you imagine are present in a mammalian cell?" | |
| F073 | 5.1.2 | concept | "The beads-on-string structure in chromatin is packaged to form chromatin fibers that are further coiled and condensed at metaphase stage of cell division to form chromosomes." | |
| F074 | 5.1.2 | definition | "The packaging of chromatin at higher level requires additional set of proteins that collectively are referred to as Non-histone Chromosomal (NHC) proteins." | |
| F075 | 5.1.2 | definition | "In a typical nucleus, some region of chromatin are loosely packed (and stains light) and are referred to as euchromatin." | |
| F076 | 5.1.2 | definition | "The chromatin that is more densely packed and stains dark are called as Heterochromatin." | |
| F077 | 5.1.2 | concept | "Euchromatin is said to be transcriptionally active chromatin, whereas heterochromatin is inactive." | |
| F078 | 5.2 | number | "By 1926, the quest to determine the mechanism for genetic inheritance had reached the molecular level." | |
| F079 | 5.2 | name | "Previous discoveries by Gregor Mendel, Walter Sutton, Thomas Hunt Morgan and numerous other scientists had narrowed the search to the chromosomes located in the nucleus of most cells." | |
| F080 | 5.2 | concept | "But the question of what molecule was actually the genetic material, had not been answered." | |
| F081 | 5.2 (Transforming Principle) | name | "In 1928, Frederick Griffith, in a series of experiments with Streptococcus pneumoniae (bacterium responsible for pneumonia), witnessed a miraculous transformation in the bacteria." | |
| F082 | 5.2 (Transforming Principle) | concept | "During the course of his experiment, a living organism (bacteria) had changed in physical form." | |
| F083 | 5.2 (Transforming Principle) | concept | "When Streptococcus pneumoniae (pneumococcus) bacteria are grown on a culture plate, some produce smooth shiny colonies (S) while others produce rough colonies (R)." | |
| F084 | 5.2 (Transforming Principle) | concept | "This is because the S strain bacteria have a mucous (polysaccharide) coat, while R strain does not." | |
| F085 | 5.2 (Transforming Principle) | concept | "Mice infected with the S strain (virulent) die from pneumonia infection but mice infected with the R strain do not develop pneumonia." | |
| F086 | 5.2 (Transforming Principle) | concept | "Griffith was able to kill bacteria by heating them." | |
| F087 | 5.2 (Transforming Principle) | concept | "He observed that heat-killed S strain bacteria injected into mice did not kill them." | |
| F088 | 5.2 (Transforming Principle) | concept | "When he injected a mixture of heat-killed S and live R bacteria, the mice died." | |
| F089 | 5.2 (Transforming Principle) | concept | "Moreover, he recovered living S bacteria from the dead mice." | |
| F090 | 5.2 (Transforming Principle) | concept | "He concluded that the R strain bacteria had somehow been transformed by the heat-killed S strain bacteria." | |
| F091 | 5.2 (Transforming Principle) | definition | "Some 'transforming principle', transferred from the heat-killed S strain, had enabled the R strain to synthesise a smooth polysaccharide coat and become virulent." | |
| F092 | 5.2 (Transforming Principle) | concept | "This must be due to the transfer of the genetic material." | |
| F093 | 5.2 (Transforming Principle) | concept | "However, the biochemical nature of genetic material was not defined from his experiments." | |
| F094 | 5.2 (Biochemical Characterisation) | name | "Prior to the work of Oswald Avery, Colin MacLeod and Maclyn McCarty (1933-44), the genetic material was thought to be a protein." | |
| F095 | 5.2 (Biochemical Characterisation) | concept | "They worked to determine the biochemical nature of 'transforming principle' in Griffith's experiment." | |
| F096 | 5.2 (Biochemical Characterisation) | concept | "They purified biochemicals (proteins, DNA, RNA, etc.) from the heat-killed S cells to see which ones could transform live R cells into S cells." | |
| F097 | 5.2 (Biochemical Characterisation) | concept | "They discovered that DNA alone from S bacteria caused R bacteria to become transformed." | |
| F098 | 5.2 (Biochemical Characterisation) | concept | "They also discovered that protein-digesting enzymes (proteases) and RNA-digesting enzymes (RNases) did not affect transformation, so the transforming substance was not a protein or RNA." | |
| F099 | 5.2 (Biochemical Characterisation) | concept | "Digestion with DNase did inhibit transformation, suggesting that the DNA caused the transformation." | |
| F100 | 5.2 (Biochemical Characterisation) | concept | "They concluded that DNA is the hereditary material, but not all biologists were convinced." | |
| F101 | 5.2 (Biochemical Characterisation) | question | "Can you think of any difference between DNAs and DNase?" | |
| F102 | 5.2.1 | name | "the experiments of Alfred Hershey and Martha Chase (1952)" | |
| F103 | 5.2.1 | definition | "They worked with viruses that infect bacteria called bacteriophages." | |
| F104 | 5.2.1 | concept | "The bacteriophage attaches to the bacteria and its genetic material then enters the bacterial cell." | |
| F105 | 5.2.1 | concept | "The bacterial cell treats the viral genetic material as if it was its own and subsequently manufactures more virus particles." | |
| F106 | 5.2.1 | concept | "Hershey and Chase worked to discover whether it was protein or DNA from the viruses that entered the bacteria." | |
| F107 | 5.2.1 | concept | "They grew some viruses on a medium that contained radioactive phosphorus and some others on medium that contained radioactive sulfur." | |
| F108 | 5.2.1 | concept | "Viruses grown in the presence of radioactive phosphorus contained radioactive DNA but not radioactive protein because DNA contains phosphorus but protein does not." | |
| F109 | 5.2.1 | concept | "Similarly, viruses grown on radioactive sulfur contained radioactive protein but not radioactive DNA because DNA does not contain sulfur." | |
| F110 | 5.2.1 | concept | "Radioactive phages were allowed to attach to E. coli bacteria." | |
| F111 | 5.2.1 | concept | "Then, as the infection proceeded, the viral coats were removed from the bacteria by agitating them in a blender." | |
| F112 | 5.2.1 | concept | "The virus particles were separated from the bacteria by spinning them in a centrifuge." | |
| F113 | 5.2.1 | concept | "Bacteria which was infected with viruses that had radioactive DNA were radioactive, indicating that DNA was the material that passed from the virus to the bacteria." | |
| F114 | 5.2.1 | concept | "Bacteria that were infected with viruses that had radioactive proteins were not radioactive. This indicates that proteins did not enter the bacteria from the viruses." | |
| F115 | 5.2.1 | concept | "DNA is therefore the genetic material that is passed from virus to bacteria (Figure 5.5)." | |
| F116 | 5.2.2 | concept | "the debate between proteins versus DNA as the genetic material was unequivocally resolved from Hershey-Chase experiment. It became an established fact that it is DNA that acts as genetic material." | |
| F117 | 5.2.2 | example | "However, it subsequently became clear that in some viruses, RNA is the genetic material (for example, Tobacco Mosaic viruses, QB bacteriophage, etc.)." | |
| F118 | 5.2.2 | concept | "Answer to some of the questions such as, why DNA is the predominant genetic material, whereas RNA performs dynamic functions of messenger and adapter has to be found from the differences between chemical structures of the two nucleic acid molecules." | |
| F119 | 5.2.2 | question | "Can you recall the two chemical differences between DNA and RNA?" | |
| F120 | 5.2.2 | list | "A molecule that can act as a genetic material must fulfill the following criteria: (i) It should be able to generate its replica (Replication)." | |
| F121 | 5.2.2 | list | "(ii) It should be stable chemically and structurally." | |
| F122 | 5.2.2 | list | "(iii) It should provide the scope for slow changes (mutation) that are required for evolution." | |
| F123 | 5.2.2 | list | "(iv) It should be able to express itself in the form of 'Mendelian Characters'." | |
| F124 | 5.2.2 | concept | "because of rule of base pairing and complementarity, both the nucleic acids (DNA and RNA) have the ability to direct their duplications." | |
| F125 | 5.2.2 | concept | "The other molecules in the living system, such as proteins fail to fulfill first criteria itself." | |
| F126 | 5.2.2 | concept | "The genetic material should be stable enough not to change with different stages of life cycle, age or with change in physiology of the organism." | |
| F127 | 5.2.2 | concept | "Stability as one of the properties of genetic material was very evident in Griffith's 'transforming principle' itself that heat, which killed the bacteria, at least did not destroy some of the properties of genetic material." | |
| F128 | 5.2.2 | concept | "This now can easily be explained in light of the DNA that the two strands being complementary if separated by heating come together, when appropriate conditions are provided." | |
| F129 | 5.2.2 | concept | "Further, 2'-OH group present at every nucleotide in RNA is a reactive group and makes RNA labile and easily degradable." | |
| F130 | 5.2.2 | concept | "RNA is also now known to be catalytic, hence reactive." | |
| F131 | 5.2.2 | concept | "Therefore, DNA chemically is less reactive and structurally more stable when compared to RNA. Therefore, among the two nucleic acids, the DNA is a better genetic material." | |
| F132 | 5.2.2 | concept | "In fact, the presence of thymine at the place of uracil also confers additional stability to DNA." | |
| F133 | 5.2.2 | concept | "(Detailed discussion about this requires understanding of the process of repair in DNA, and you will study these processes in higher classes.)" | |
| F134 | 5.2.2 | concept | "Both DNA and RNA are able to mutate. In fact, RNA being unstable, mutate at a faster rate." | |
| F135 | 5.2.2 | concept | "Consequently, viruses having RNA genome and having shorter life span mutate and evolve faster." | |
| F136 | 5.2.2 | concept | "RNA can directly code for the synthesis of proteins, hence can easily express the characters." | |
| F137 | 5.2.2 | concept | "DNA, however, is dependent on RNA for synthesis of proteins. The protein synthesising machinery has evolved around RNA." | |
| F138 | 5.2.2 | concept | "The above discussion indicate that both RNA and DNA can function as genetic material, but DNA being more stable is preferred for storage of genetic information. For the transmission of genetic information, RNA is better." | |
| F139 | 5.3 | concept | "It shall be discussed in detail in the chapter on chemical evolution, but briefly, we shall highlight some of the facts and points." | |
| F140 | 5.3 | concept | "RNA was the first genetic material." | |
| F141 | 5.3 | concept | "There is now enough evidence to suggest that essential life processes (such as metabolism, translation, splicing, etc.), evolved around RNA." | |
| F142 | 5.3 | concept | "RNA used to act as a genetic material as well as a catalyst (there are some important biochemical reactions in living systems that are catalysed by RNA catalysts and not by protein enzymes)." | |
| F143 | 5.3 | concept | "But, RNA being a catalyst was reactive and hence unstable." | |
| F144 | 5.3 | concept | "Therefore, DNA has evolved from RNA with chemical modifications that make it more stable." | |
| F145 | 5.3 | concept | "DNA being double stranded and having complementary strand further resists changes by evolving a process of repair." | |
| F146 | 5.4 | concept | "To quote their original statement that is as follows: 'It has not escaped our notice that the specific pairing we have postulated immediately suggests a possible copying mechanism for the genetic material' (Watson and Crick, 1953)." | |
| F147 | 5.4 | concept | "The scheme suggested that the two strands would separate and act as a template for the synthesis of new complementary strands." | |
| F148 | 5.4 | concept | "After the completion of replication, each DNA molecule would have one parental and one newly synthesised strand." | |
| F149 | 5.4 | definition | "This scheme was termed as semiconservative DNA replication (Figure 5.6)." | |
| F150 | 5.4.1 | concept | "It was shown first in Escherichia coli and subsequently in higher organisms, such as plants and human cells." | |
| F151 | 5.4.1 | name | "Matthew Meselson and Franklin Stahl performed the following experiment in 1958" | |
| F152 | 5.4.1 | list | "(i) They grew E. coli in a medium containing 15NH4Cl (15N is the heavy isotope of nitrogen) as the only nitrogen source for many generations." | |
| F153 | 5.4.1 | concept | "The result was that 15N was incorporated into newly synthesised DNA (as well as other nitrogen containing compounds)." | |
| F154 | 5.4.1 | concept | "This heavy DNA molecule could be distinguished from the normal DNA by centrifugation in a cesium chloride (CsCl) density gradient" | |
| F155 | 5.4.1 | concept | "(Please note that 15N is not a radioactive isotope, and it can be separated from 14N only based on densities)." | |
| F156 | 5.4.1 | list | "(ii) Then they transferred the cells into a medium with normal 14NH4Cl and took samples at various definite time intervals as the cells multiplied, and extracted the DNA that remained as double-stranded helices." | |
| F157 | 5.4.1 | concept | "The various samples were separated independently on CsCl gradients to measure the densities of DNA (Figure 5.7)." | |
| F158 | 5.4.1 | question | "Can you recall what centrifugal force is, and think why a molecule with higher mass/density would sediment faster?" | |
| F159 | 5.4.1 | list | "(iii) Thus, the DNA that was extracted from the culture one generation after the transfer from 15N to 14N medium [that is after 20 minutes; E. coli divides in 20 minutes] had a hybrid or intermediate density." | |
| F160 | 5.4.1 | number | "DNA extracted from the culture after another generation [that is after 40 minutes, II generation] was composed of equal amounts of this hybrid DNA and of 'light' DNA." | |
| F161 | 5.4.1 | question | "If E. coli was allowed to grow for 80 minutes then what would be the proportions of light and hybrid densities DNA molecule?" | |
| F162 | 5.4.1 | name | "Very similar experiments involving use of radioactive thymidine to detect distribution of newly synthesised DNA in the chromosomes was performed on Vicia faba (faba beans) by Taylor and colleagues in 1958." | |
| F163 | 5.4.1 | concept | "The experiments proved that the DNA in chromosomes also replicate semiconservatively." | |
| F164 | 5.4.2 | definition | "The main enzyme is referred to as DNA-dependent DNA polymerase, since it uses a DNA template to catalyse the polymerisation of deoxynucleotides." | |
| F165 | 5.4.2 | concept | "These enzymes are highly efficient enzymes as they have to catalyse polymerisation of a large number of nucleotides in a very short time." | |
| F166 | 5.4.2 | number | "E. coli that has only 4.6 x10^6 bp (compare it with human whose diploid content is 6.6 x 10^9 bp), completes the process of replication within 18 minutes" | |
| F167 | 5.4.2 | number | "that means the average rate of polymerisation has to be approximately 2000 bp per second" | |
| F168 | 5.4.2 | concept | "Not only do these polymerases have to be fast, but they also have to catalyse the reaction with high degree of accuracy. Any mistake during replication would result into mutations." | |
| F169 | 5.4.2 | concept | "Furthermore, energetically replication is a very expensive process." | |
| F170 | 5.4.2 | concept | "Deoxyribonucleoside triphosphates serve dual purposes. In addition to acting as substrates, they provide energy for polymerisation reaction" | |
| F171 | 5.4.2 | concept | "(the two terminal phosphates in a deoxynucleoside triphosphates are high-energy phosphates, same as in case of ATP)." | |
| F172 | 5.4.2 | concept | "In addition to DNA-dependent DNA polymerases, many additional enzymes are required to complete the process of replication with high degree of accuracy." | |
| F173 | 5.4.2 | definition | "For long DNA molecules, since the two strands of DNA cannot be separated in its entire length (due to very high energy requirement), the replication occur within a small opening of the DNA helix, referred to as replication fork." | |
| F174 | 5.4.2 | concept | "The DNA-dependent DNA polymerases catalyse polymerisation only in one direction, that is 5'-to-3'." | |
| F175 | 5.4.2 | concept | "This creates some additional complications at the replicating fork." | |
| F176 | 5.4.2 | concept | "Consequently, on one strand (the template with polarity 3'-to-5'), the replication is continuous, while on the other (the template with polarity 5'-to-3'), it is discontinuous." | |
| F177 | 5.4.2 | concept | "The discontinuously synthesised fragments are later joined by the enzyme DNA ligase (Figure 5.8)." | |
| F178 | 5.4.2 | concept | "The DNA polymerases on their own cannot initiate the process of replication." | |
| F179 | 5.4.2 | concept | "Also the replication does not initiate randomly at any place in DNA." | |
| F180 | 5.4.2 | definition | "There is a definite region in E. coli DNA where the replication originates. Such regions are termed as origin of replication." | |
| F181 | 5.4.2 | concept | "It is because of the requirement of the origin of replication that a piece of DNA if needed to be propagated during recombinant DNA procedures, requires a vector. The vectors provide the origin of replication." | |
| F182 | 5.4.2 | concept | "Further, not every detail of replication is understood well." | |
| F183 | 5.4.2 | concept | "In eukaryotes, the replication of DNA takes place at S-phase of the cell-cycle." | |
| F184 | 5.4.2 | concept | "The replication of DNA and cell division cycle should be highly coordinated." | |
| F185 | 5.4.2 | concept | "A failure in cell division after DNA replication results into polyploidy (a chromosomal anomaly)." | |
| F186 | 5.4.2 | concept | "You will learn the detailed nature of origin and the processes occurring at this site, in higher classes." | |
| F187 | 5.5 | concept | "Here also, the principle of complementarity governs the process of transcription, except the adenosine complements now forms base pair with uracil instead of thymine." | |
| F188 | 5.5 | concept | "However, unlike in the process of replication, which once set in, the total DNA of an organism gets duplicated, in transcription only a segment of DNA and only one of the strands is copied into RNA." | |
| F189 | 5.5 | concept | "This necessitates defining the boundaries that would demarcate the region and the strand of DNA that would be transcribed." | |
| F190 | 5.5 | concept | "First, if both strands act as a template, they would code for RNA molecule with different sequences (Remember complementarity does not mean identical), and in turn, if they code for proteins, the sequence of amino acids in the proteins would be different." | |
| F191 | 5.5 | concept | "Hence, one segment of the DNA would be coding for two different proteins, and this would complicate the genetic information transfer machinery." | |
| F192 | 5.5 | concept | "Second, the two RNA molecules if produced simultaneously would be complementary to each other, hence would form a double stranded RNA." | |
| F193 | 5.5 | concept | "This would prevent RNA from being translated into protein and the exercise of transcription would become a futile one." | |
| F194 | 5.5.1 | list | "A transcription unit in DNA is defined primarily by the three regions in the DNA: (i) A Promoter (ii) The Structural gene (iii) A Terminator" | |
| F195 | 5.5.1 | concept | "There is a convention in defining the two strands of the DNA in the structural gene of a transcription unit." | |
| F196 | 5.5.1 | definition | "Since the two strands have opposite polarity and the DNA-dependent RNA polymerase also catalyse the polymerisation in only one direction, that is, 5'-to-3', the strand that has the polarity 3'-to-5' acts as a template, and is also referred to as template strand." | |
| F197 | 5.5.1 | definition | "The other strand which has the polarity (5'-to-3') and the sequence same as RNA (except thymine at the place of uracil), is displaced during transcription. Strangely, this strand (which does not code for anything) is referred to as coding strand." | |
| F198 | 5.5.1 | concept | "All the reference point while defining a transcription unit is made with coding strand." | |
| F199 | 5.5.1 | example | "3'-ATGCATGCATGCATGCATGCATGC-5' Template Strand / 5'-TACGTACGTACGTACGTACGTACG-3' Coding Strand" | |
| F200 | 5.5.1 | question | "Can you now write the sequence of RNA transcribed from the above DNA?" | |
| F201 | 5.5.1 | concept | "The promoter and terminator flank the structural gene in a transcription unit." | |
| F202 | 5.5.1 | definition | "The promoter is said to be located towards 5'-end (upstream) of the structural gene (the reference is made with respect to the polarity of coding strand)." | |
| F203 | 5.5.1 | definition | "It is a DNA sequence that provides binding site for RNA polymerase, and it is the presence of a promoter in a transcription unit that also defines the template and coding strands." | |
| F204 | 5.5.1 | concept | "By switching its position with terminator, the definition of coding and template strands could be reversed." | |
| F205 | 5.5.1 | definition | "The terminator is located towards 3'-end (downstream) of the coding strand and it usually defines the end of the process of transcription (Figure 5.9)." | |
| F206 | 5.5.1 | concept | "There are additional regulatory sequences that may be present further upstream or downstream to the promoter. Some of the properties of these sequences shall be discussed while dealing with regulation of gene expression." | |
| F207 | 5.5.2 | concept | "Though there is no ambiguity that the genes are located on the DNA, it is difficult to literally define a gene in terms of DNA sequence." | |
| F208 | 5.5.2 | concept | "The DNA sequence coding for tRNA or rRNA molecule also define a gene." | |
| F209 | 5.5.2 | definition | "However by defining a cistron as a segment of DNA coding for a polypeptide, the structural gene in a transcription unit could be said as monocistronic (mostly in eukaryotes) or polycistronic (mostly in bacteria or prokaryotes)." | |
| F210 | 5.5.2 | concept | "In eukaryotes, the monocistronic structural genes have interrupted coding sequences - the genes in eukaryotes are split." | |
| F211 | 5.5.2 | definition | "The coding sequences or expressed sequences are defined as exons. Exons are said to be those sequence that appear in mature or processed RNA." | |
| F212 | 5.5.2 | definition | "The exons are interrupted by introns. Introns or intervening sequences do not appear in mature or processed RNA." | |
| F213 | 5.5.2 | concept | "The split-gene arrangement further complicates the definition of a gene in terms of a DNA segment." | |
| F214 | 5.5.2 | concept | "Inheritance of a character is also affected by promoter and regulatory sequences of a structural gene." | |
| F215 | 5.5.2 | definition | "Hence, sometime the regulatory sequences are loosely defined as regulatory genes, even though these sequences do not code for any RNA or protein." | |
| F216 | 5.5.3 | concept | "All three RNAs are needed to synthesise a protein in a cell." | |
| F217 | 5.5.3 | concept | "The mRNA provides the template, tRNA brings aminoacids and reads the genetic code, and rRNAs play structural and catalytic role during translation." | |
| F218 | 5.5.3 | concept | "There is single DNA-dependent RNA polymerase that catalyses transcription of all types of RNA in bacteria." | |
| F219 | 5.5.3 | concept | "RNA polymerase binds to promoter and initiates transcription (Initiation). It uses nucleoside triphosphates as substrate and polymerises in a template depended fashion following the rule of complementarity." | |
| F220 | 5.5.3 | concept | "It somehow also facilitates opening of the helix and continues elongation. Only a short stretch of RNA remains bound to the enzyme." | |
| F221 | 5.5.3 | concept | "Once the polymerases reaches the terminator region, the nascent RNA falls off, so also the RNA polymerase. This results in termination of transcription." | |
| F222 | 5.5.3 | question | "An intriguing question is that how is the RNA polymerases able to catalyse all the three steps, which are initiation, elongation and termination." | |
| F223 | 5.5.3 | concept | "The RNA polymerase is only capable of catalysing the process of elongation. It associates transiently with initiation-factor (sigma) and termination-factor (rho) to initiate and terminate the transcription, respectively." | |
| F224 | 5.5.3 | concept | "Association with these factors alter the specificity of the RNA polymerase to either initiate or terminate (Figure 5.10)." | |
| F225 | 5.5.3 | concept | "In bacteria, since the mRNA does not require any processing to become active, and also since transcription and translation take place in the same compartment (there is no separation of cytosol and nucleus in bacteria), many times the translation can begin much before the mRNA is fully transcribed. Consequently, the transcription and translation can be coupled in bacteria." | |
| F226 | 5.5.3 | list | "In eukaryotes, there are two additional complexities - (i) There are at least three RNA polymerases in the nucleus (in addition to the RNA polymerase found in the organelles). There is a clear cut division of labour." | |
| F227 | 5.5.3 | number | "The RNA polymerase I transcribes rRNAs (28S, 18S, and 5.8S), whereas the RNA polymerase III is responsible for transcription of tRNA, 5srRNA, and snRNAs (small nuclear RNAs). The RNA polymerase II transcribes precursor of mRNA, the heterogeneous nuclear RNA (hnRNA)." | |
| F228 | 5.5.3 | list | "(ii) The second complexity is that the primary transcripts contain both the exons and the introns and are non-functional. Hence, it is subjected to a process called splicing where the introns are removed and exons are joined in a defined order." | |
| F229 | 5.5.3 | number | "hnRNA undergoes additional processing called as capping and tailing. In capping an unusual nucleotide (methyl guanosine triphosphate) is added to the 5'-end of hnRNA. In tailing, adenylate residues (200-300) are added at 3'-end in a template independent manner." | |
| F230 | 5.5.3 | concept | "It is the fully processed hnRNA, now called mRNA, that is transported out of the nucleus for translation (Figure 5.11)." | |
| F231 | 5.5.3 | concept | "The significance of such complexities is now beginning to be understood. The split-gene arrangements represent probably an ancient feature of the genome. The presence of introns is reminiscent of antiquity, and the process of splicing represents the dominance of RNA-world. In recent times, the understanding of RNA and RNA-dependent processes in the living system have assumed more importance." | |

## Figure-label matrix

Empty — owned by session **1-F**, which runs once for the whole chapter after 1b. Rows will be added **into the Facts table above** as rows whose wording begins `Figure labels:`, per §6. No pipe-delimited table is written here, deliberately: a second copy of the matrix doubles every label and turns a markdown separator into a phantom `Fig #` figure (the Ch12 failure).

## Summary classification

Empty — owned by session **1-Z** (step 8). The chapter Summary sits in the second half of the source.

## Exercise-gap terms

Empty — owned by session **1-Z** (step 7). The Exercises sit in the second half of the source.

## Figure manifest

Empty — owned by session **1-F**. A first-half-only manifest cannot be checked for duplicate or missing `Fig #` numbering across the seam, so figures are deliberately deferred to a single whole-chapter session (§6 big-chapter protocol).

## Carry-over list

Numbered, added to freely; each is a defect that will not have to be rediscovered.

1. **Openers carrying load-bearing definitions — pointers for session 1a-O, not rows here.** Several first-half sections open by defining the very term in their heading, which is the §6 step-5 failure mode. 1a-O must produce a row for each of: §5.1 "DNA is a long polymer of deoxyribonucleotides."; §5.1.1 "Let us recapitulate the chemical structure of a polynucleotide chain (DNA or RNA)."; §5.1.2 the 0.34 nm / 2.2 metre calculation sentence; §5.2 the Meischer-and-Mendel timing sentence; §5.2.1 "The unequivocal proof that DNA is the genetic material came from the experiments of Alfred Hershey and Martha Chase (1952)."; §5.2.2 the "debate ... unequivocally resolved" sentence; §5.3 "which is the first genetic material?"; §5.4 "While proposing the double helical structure for DNA, Watson and Crick had immediately proposed a scheme for replication of DNA."; §5.4.1 "It is now proven that DNA replicates semiconservatively."; §5.4.2 "In living cells, such as E. coli, the process of replication requires a set of catalysts (enzymes)."; **§5.5 "The process of copying genetic information from one strand of the DNA into RNA is termed as transcription."** (the definition of transcription lives only in the opener); §5.5.1 the three-region sentence; **§5.5.2 "A gene is defined as the functional unit of inheritance."**; §5.5.3 "In bacteria, there are three major types of RNAs: mRNA (messenger RNA), tRNA (transfer RNA), and rRNA (ribosomal RNA)."
2. **Unnumbered sub-headings spotted in the first half — pointers for session 1a-H.** `Transforming Principle` (p. 6) and `Biochemical Characterisation of Transforming Principle` (p. 7), both inside §5.2, both 10.5pt full-bold. **CORRECTED:** this entry previously also listed "the boxed `Central dogma` label on source p. 4" as a 1a-H heading. Re-checked against the PDF — it is plain 10.5pt Bookman-**Light** text labelling the DNA-to-RNA-to-Protein diagram, not a bold sub-heading. It is **reassigned to `1-F` as an in-figure label** and must not become a heading row. 1a-H must still walk the skeleton independently and not rely on this list being complete; see `Ch5_TRACKER.md` for the full 17-line target and the running-header / small-caps-span traps.
3. **Banned-glyph traps for Pass 2 (check 5).** This chapter is dense in glyphs the linter rejects: the source's `5'→3'` arrows (write `5'-to-3'`), the Greek `σ` and `ρ` transcription factors (write `sigma` and `rho`), `φ×174` (write `phi x 174`), and superscripts/subscripts in `4.6 × 10^6`, `3.3 × 10^9`, `10^-9 m`, `15NH4Cl`, `14NH4Cl`, `28S/18S/5.8S`. All must be flat ASCII text in the script — never Unicode arrows, Greek letters, or real super/subscripts. Rows F016, F018, F019, F044, F048, F056, F057, F058, F152, F156, F166, F174, F176, F196, F197, F223, F227 are the ones carrying them.
4. **`QB bacteriophage` (F117) is the source's own spelling** of Qbeta. Reproduce it as NCERT prints it; do not "correct" it to a Greek beta, which would trip check 5.
5. **Central dogma direction must stay as words** (F053): render as `DNA-to-RNA-to-Protein`, never with arrow glyphs.
6. **The hypothetical transcription-unit sequence (F199) is marks-critical and must be reproduced base-for-base**, with the template strand written 3'-to-5' above the coding strand written 5'-to-3', exactly as NCERT orders them.
7. **Two different human genome figures appear in the first half** — `3.3 x 10^9 bp` haploid (F019) and `6.6 x 10^9 bp` diploid (F057, F166). Keep the haploid/diploid qualifier attached to each; dropping it is a silent factual error.
8. **F102 is a name row, not the §5.2.1 opener.** It records only the names and the 1952 date; the opening sentence itself is still owed by 1a-O. Do not treat F102 as satisfying that requirement.
