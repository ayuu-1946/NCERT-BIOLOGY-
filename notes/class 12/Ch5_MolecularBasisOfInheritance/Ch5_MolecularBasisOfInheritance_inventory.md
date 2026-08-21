# Working Inventory (NOT FROZEN) — Molecular Basis of Inheritance (Class 12, Chapter 5)

> The `# Frozen Inventory` title used by completed chapters is deliberately **withheld** until `1-Z` actually freezes this file. A naive `grep -i frozen` on the old title would have reported this chapter as frozen while six sweeps were still outstanding.

Source: `Chapter/class 12/Chapter 5 - Molecular Basis of Inheritance.pdf` (31 pp) | Status: **NOT FROZEN — all six text sweeps (1a-S/H/O, 1b-S/H/O) complete; `1-F` and `1-Z` outstanding** | Rows so far: **506** (`F001`..`F506`)

**Big-chapter protocol (§6, 5 passes).** 31 source pages, 10 numbered sections plus summary and exercises, so this chapter runs `1a → 1b → 2a → 2b → 3`. The source seam is:

- **Pass 1a — first half:** chapter introduction + §5.1 The DNA, §5.2 The Search for Genetic Material, §5.3 RNA World, §5.4 Replication, §5.5 Transcription (source pp. 1–17, book pp. 79–95, up to but excluding the `5.6 GENETIC CODE` banner).
- **Pass 1b — second half:** §5.6 Genetic Code, §5.7 Translation, §5.8 Regulation of Gene Expression, §5.9 Human Genome Project, §5.10 DNA Fingerprinting, Summary and Exercises (source pp. 17–31).

Per §6, `1a/1b` halve the **source**; `1-S / 1-H / 1-O / 1-F / 1-Z` separate the **kinds of work**. The sweeps therefore run per half (1a-S, 1a-H, 1a-O, then 1b-S, 1b-H, 1b-O), while **figures run as one whole-chapter 1-F session** and the freeze as one whole-chapter 1-Z. Gate 1 is evaluated over the whole chapter only after 1b.

Tick legend: `x` = written into the script and verified present in the generated PDF. **No row is ticked — Pass 2 has not started.**

## Session log — Pass 1

| Session | Scope | State | Rows added (machine-derived) |
|---|---|---|---|
| **1a-S** — source read & prose inventory, first half | intro + §5.1–§5.5 | **done** | **231** (`F001`..`F231`) |
| **1a-H** — heading sweep, first half | intro + §5.1–§5.5 | **done** | **17** (`F232`..`F248`) — 16 in-body + the p1 chapter title |
| **1a-O** — opener sweep, first half | intro + §5.1–§5.5 | **done** | **16** (`F249`..`F264`) — one per heading-bearing section |
| **1b-S** — source read & prose inventory, second half | §5.6–§5.10 + Exercises | **done** | **218** (`F265`..`F482`) — §5.6 onward from the mid-p17 seam, incl. the 14 Exercises questions |
| **1b-H** — heading sweep, second half | §5.6–§5.10 + Summary + Exercises | **done** | **13** (`F483`..`F495`) — 10 numbered + `Goals of HGP` + `SUMMARY` + `EXERCISES` |
| **1b-O** — opener sweep, second half | §5.6–§5.10 | **done** | **11** (`F496`..`F506`) — one per heading-bearing section; `SUMMARY`/`EXERCISES` deliberately excluded (see note) |
| **1-F** — figures, whole chapter (single session) | all figures 5.1–5.16 | not started | — |
| **1-Z** — gaps, summary & freeze, whole chapter | steps 7–10 | not started | — |

**Why `1b-H` wrote 13 rows but `1b-O` wrote 11.** Three of the 13 headings do not take an opener row: `EXERCISES` runs straight into question 1 with no prose, and `SUMMARY`'s sentences are owned by **`1-Z` step 8** (BODY-PRESENT / SUMMARY-UNIQUE classification) — giving the Summary an opener row here would put the same sentence under two owners, which is how a sentence gets written twice into the script. `Goals of HGP` *does* take one (`F503`) because it has a genuine stem sentence. So 13 headings − `SUMMARY` − `EXERCISES` = 11 openers.

**Prose/opener boundary was checked, not assumed.** All 11 openers were confirmed *absent* from the 218 `1b-S` prose rows before `1b-O` ran: each section's `1b-S` block starts at sentence 2 (e.g. §5.7's prose starts `F314` "The order and sequence of amino acids…", with the defining opener "Translation refers to…" left to `F499`). Zero overlap, so no sentence is inventoried twice.

Environment re-established this session per §0.2–§0.3: `/vercel/share/neetenv` was **absent** (expected — it does not survive a session boundary) and was rebuilt. CPython 3.13.11 @ `/vercel/share/neetenv`, reportlab 5.0.1, pdfplumber OK, pymupdf 1.28.2, Pillow 12.3.0.

## Header counts — machine-derived (§6 Pass 1 step 10), never hand-tallied

| Count | Value |
|---|---|
| Facts rows so far | **506** (`F001`..`F506`) — **whole chapter, all text swept** |
| ID range / contiguity | F001..F506 — 0 gaps, 0 duplicates, IDs monotonically increasing (re-parsed from the table below) |
| `Type: heading` rows | **30** = `1a-H` 17 (`F232`..`F248`) + `1b-H` 13 (`F483`..`F495`). Chapter title is 1 of the 30, so **in-body headings = 29**. |
| `Type: opener` rows | **27** = `1a-O` 16 (`F249`..`F264`) + `1b-O` 11 (`F496`..`F506`) |
| Figure-label rows | **0** — owned by session 1-F |
| Label strings parsed by `check_pdf.py`'s own `_extract_labels` | **0 labels, 0 figures, no phantom `Fig #` row** — re-run against this file this session under the rebuilt venv; the empty-matrix state is the expected pre-1-F result |
| `Type` values used (normalized, lower-case) | `concept` 260 · `definition` 56 · `number` 37 · `list` 33 · `question` 31 · `heading` 30 · `opener` 27 · `name` 18 · `example` 13 · `table` 1 = 506; no other value present |
| Rows ticked | **0** — Pass 2 not started |
| Summary sentences classified | not started (1-Z) |
| Exercise-gap terms | not started (1-Z) |
| Figures in manifest | not started (1-F) |

Every number above was produced by re-parsing this file's Facts table with a script (§6 step 10), not by hand tally: 506 rows, `F001..F506`, **0 gaps, 0 duplicates, monotonic**, and the `Type` column asserted to contain only the ten values listed. The census is derivable from its own list — `260 + 56 + 37 + 33 + 31 + 30 + 27 + 18 + 13 + 1 = 506`, matching the row total.

`table` (1 row, `F280`) is a **new `Type` value introduced by `1b-S`**, for the `Table 5.1` codon checker-board caption. It is neither prose nor a figure; see carry-over 9, which records that the table's 64 cells are not text-extractable and that **no session currently owns rebuilding them**.

**Heading census, derivable from its own list (§6 step 10).** The 30 `Type: heading` rows are `F232`..`F248` and `F483`..`F495`; each group's size is the **length of the ID list beside it**, machine-counted, not asserted:

| Group | IDs | Count |
|---|---|---|
| Chapter title (p1) | `F232` | 1 |
| Numbered section banners — first half | `F233` 5.1 · `F236` 5.2 · `F241` 5.3 · `F242` 5.4 · `F245` 5.5 | 5 |
| Numbered section banners — second half | `F483` 5.6 · `F486` 5.7 · `F487` 5.8 · `F489` 5.9 · `F493` 5.10 | 5 |
| Numbered sub-headings — first half | `F234` · `F235` · `F239` · `F240` · `F243` · `F244` · `F246` · `F247` · `F248` | 9 |
| Numbered sub-headings — second half | `F484` · `F485` · `F488` · `F491` · `F492` | 5 |
| Unnumbered sub-headings | `F237` · `F238` (first half) · `F490` `Goals of HGP` (second half) | 3 |
| Back-matter headings | `F494` SUMMARY · `F495` EXERCISES | 2 |

`1 + 5 + 5 + 9 + 5 + 3 + 2 = 30` ✓ equals the machine `Type: heading` count. **10 numbered section banners (5 + 5) matches the 10 sections the protocol choice was based on** — an independent cross-check that no banner was missed. In-body headings excluding the chapter title = **29**.

> ## GATE 1 STATUS: **OPEN — blocked. Pass 2 may not begin.**
>
> | Gate 1 requirement (§6) | State |
> |---|---|
> | Environment (§0.2–0.3) re-established | done — venv rebuilt, all four imports verified under that interpreter |
> | Every fact has a Facts row (three source reads) | **partial** — first half done (231 rows); second half is 1b-S |
> | Every heading has a row incl. unnumbered sub-headings | **partial** — first half done by `1a-H`: 17 rows `F232..F248`, including both unnumbered subs (`F237`, `F238`). Second half is `1b-H`. |
> | Every section's opening sentence has a row | **partial** — first half done by `1a-O`; second half is `1b-O` |
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
| F232 | — | heading | "MOLECULAR BASIS OF INHERITANCE" (chapter title, p1; set 30.0pt AvantGarde-**Book** over two lines "MOLECULAR BASIS OF" / "INHERITANCE", preceded by "CHAPTER 5" at 26.0pt — **not bold**, see trap 6) | |
| F233 | 5.1 | heading | "5.1 THE DNA" (p2, 14.0pt Bookman-Demi section banner) | |
| F234 | 5.1.1 | heading | "5.1.1 Structure of Polynucleotide Chain" (p2, 12.0pt) | |
| F235 | 5.1.2 | heading | "5.1.2 Packaging of DNA Helix" (p5, 12.0pt; source prints two spaces after the number) | |
| F236 | 5.2 | heading | "5.2 THE SEARCH FOR GENETIC MATERIAL" (p6, 14.0pt banner; 10 small-caps spans — see traps 2 and 7) | |
| F237 | 5.2 | heading | "Transforming Principle" (p6, 10.5pt full-bold, **unnumbered sub-heading** inside 5.2) | |
| F238 | 5.2 | heading | "Biochemical Characterisation of Transforming Principle" (p7, 10.5pt full-bold, **unnumbered sub-heading** inside 5.2) | |
| F239 | 5.2.1 | heading | "5.2.1 The Genetic Material is DNA" (p7, 12.0pt) | |
| F240 | 5.2.2 | heading | "5.2.2 Properties of Genetic Material (DNA versus RNA)" (p8, 12.0pt) | |
| F241 | 5.3 | heading | "5.3 RNA WORLD" (p10, 14.0pt banner) | |
| F242 | 5.4 | heading | "5.4 REPLICATION" (p10, 14.0pt banner) | |
| F243 | 5.4.1 | heading | "5.4.1 The Experimental Proof" (p10, 12.0pt) | |
| F244 | 5.4.2 | heading | "5.4.2 The Machinery and the Enzymes" (p12, 12.0pt) | |
| F245 | 5.5 | heading | "5.5 TRANSCRIPTION" (p13, 14.0pt banner) | |
| F246 | 5.5.1 | heading | "5.5.1 Transcription Unit" (p13, 12.0pt) | |
| F247 | 5.5.2 | heading | "5.5.2 Transcription Unit and the Gene" (p14, 12.0pt) | |
| F248 | 5.5.3 | heading | "5.5.3 Types of RNA and the process of Transcription" (p15, 12.0pt) | |
| F249 | 5.1 | opener | "DNA is a long polymer of deoxyribonucleotides." (p2 — **defines DNA**; the whole section leans on it) | |
| F250 | 5.1.1 | opener | "Let us recapitulate the chemical structure of a polynucleotide chain (DNA or RNA)." (p2) | |
| F251 | 5.1.2 | opener | "Taken the distance between two consecutive base pairs as 0.34 nm (0.34x10^-9 m), if the length of DNA double helix in a typical mammalian cell is calculated (simply by multiplying the total number of bp with distance between two consecutive bp, that is, 6.6 x 10^9 bp x 0.34 x 10^-9 m/bp), it comes out to be approximately 2.2 metres." (p5 — carries the 2.2 m calculation; overlaps F056/F057 by design, an opener row is still required) | |
| F252 | 5.2 | opener | "Even though the discovery of nuclein by Meischer and the proposition for principles of inheritance by Mendel were almost at the same time, but that the DNA acts as a genetic material took long to be discovered and proven." (p6) | |
| F253 | 5.2 (Transforming Principle) | opener | "In 1928, Frederick Griffith, in a series of experiments with Streptococcus pneumoniae (bacterium responsible for pneumonia), witnessed a miraculous transformation in the bacteria." (p6 — opener of the unnumbered sub-heading `F237`) | |
| F254 | 5.2 (Biochemical Characterisation) | opener | "Prior to the work of Oswald Avery, Colin MacLeod and Maclyn McCarty (1933-44), the genetic material was thought to be a protein." (p7 — opener of the unnumbered sub-heading `F238`) | |
| F255 | 5.2.1 | opener | "The unequivocal proof that DNA is the genetic material came from the experiments of Alfred Hershey and Martha Chase (1952)." (p7) | |
| F256 | 5.2.2 | opener | "From the foregoing discussion, it is clear that the debate between proteins versus DNA as the genetic material was unequivocally resolved from Hershey-Chase experiment." (p8) | |
| F257 | 5.3 | opener | "From foregoing discussion, an immediate question becomes evident - which is the first genetic material?" (p10) | |
| F258 | 5.4 | opener | "While proposing the double helical structure for DNA, Watson and Crick had immediately proposed a scheme for replication of DNA." (p10) | |
| F259 | 5.4.1 | opener | "It is now proven that DNA replicates semiconservatively." (p10) | |
| F260 | 5.4.2 | opener | "In living cells, such as E. coli, the process of replication requires a set of catalysts (enzymes)." (p12) | |
| F261 | 5.5 | opener | "The process of copying genetic information from one strand of the DNA into RNA is termed as transcription." (p13 — **the only place transcription is defined**; §6 step 5's load-bearing case. Recovered by column-aware reading: a naive y-sort splices the `Figure 5.8 Replicating Fork` caption into mid-sentence — see trap 8) | |
| F262 | 5.5.1 | opener | "A transcription unit in DNA is defined primarily by the three regions in the DNA: (i) A Promoter (ii) The Structural gene (iii) A Terminator" (p13 — the sentence ends at the three-item list; the "convention in defining the two strands" sentence that follows is a separate sentence, not part of the opener) | |
| F263 | 5.5.2 | opener | "A gene is defined as the functional unit of inheritance." (p14 — **the only place gene is defined**; §6 step 5's second load-bearing case, and the word sits in the heading `F247` directly above it) | |
| F264 | 5.5.3 | opener | "In bacteria, there are three major types of RNAs: mRNA (messenger RNA), tRNA (transfer RNA), and rRNA (ribosomal RNA)." (p15) | |
| F265 | 5.6 | concept | "Hence, these processes are easy to conceptualise on the basis of complementarity." | |
| F266 | 5.6 | concept | "The process of translation requires transfer of genetic information from a polymer of nucleotides to synthesise a polymer of amino acids." | |
| F267 | 5.6 | concept | "Neither does any complementarity exist between nucleotides and amino acids, nor could any be drawn theoretically." | |
| F268 | 5.6 | concept | "There existed ample evidences, though, to support the notion that change in nucleic acids (genetic material) were responsible for change in amino acids in proteins." | |
| F269 | 5.6 | concept | "This led to the proposition of a genetic code that could direct the sequence of amino acids during synthesis of proteins." | |
| F270 | 5.6 | concept | "If determining the biochemical nature of genetic material and the structure of DNA was very exciting, the proposition and deciphering of genetic code were most challenging." | |
| F271 | 5.6 | concept | "In a very true sense, it required involvement of scientists from several disciplines - physicists, organic chemists, biochemists and geneticists." | |
| F272 | 5.6 | name | "It was George Gamow, a physicist, who argued that since there are only 4 bases and if they have to code for 20 amino acids, the code should constitute a combination of bases." | |
| F273 | 5.6 | concept | "He suggested that in order to code for all the 20 amino acids, the code should be made up of three nucleotides." | |
| F274 | 5.6 | number | "This was a very bold proposition, because a permutation combination of 4^3 (4 x 4 x 4) would generate 64 codons; generating many more codons than required." | |
| F275 | 5.6 | concept | "Providing proof that the codon was a triplet, was a more daunting task." | |
| F276 | 5.6 | name | "The chemical method developed by Har Gobind Khorana was instrumental in synthesising RNA molecules with defined combinations of bases (homopolymers and copolymers)." | |
| F277 | 5.6 | name | "Marshall Nirenberg's cell-free system for protein synthesis finally helped the code to be deciphered." | |
| F278 | 5.6 | name | "Severo Ochoa enzyme (polynucleotide phosphorylase) was also helpful in polymerising RNA with defined sequences in a template independent manner (enzymatic synthesis of RNA)." | |
| F279 | 5.6 | concept | "Finally a checker-board for genetic code was prepared which is given in Table 5.1." | |
| F280 | 5.6 | table | "Table 5.1: The Codons for the Various Amino Acids" (p18, 10.0pt Bookman-Demi table caption; the 64-cell codon checker-board itself is **not text-extractable** - see carry-over 9) | |
| F281 | 5.6 | concept | "The salient features of genetic code are as follows:" | |
| F282 | 5.6 | list | "(i) The codon is triplet. 61 codons code for amino acids and 3 codons do not code for any amino acids, hence they function as stop codons." | |
| F283 | 5.6 | list | "(ii) Some amino acids are coded by more than one codon, hence the code is degenerate." | |
| F284 | 5.6 | list | "(iii) The codon is read in mRNA in a contiguous fashion. There are no punctuations." | |
| F285 | 5.6 | list | "(iv) The code is nearly universal: for example, from bacteria to human UUU would code for Phenylalanine (phe). Some exceptions to this rule have been found in mitochondrial codons, and in some protozoans." | |
| F286 | 5.6 | list | "(v) AUG has dual functions. It codes for Methionine (met) , and it also act as initiator codon." | |
| F287 | 5.6 | list | "(vi) UAA, UAG, UGA are stop terminator codons." | |
| F288 | 5.6 | question | "If following is the sequence of nucleotides in mRNA, predict the sequence of amino acid coded by it (take help of the checkerboard): -AUG UUU UUC UUC UUU UUU UUC-" | |
| F289 | 5.6 | question | "Now try the opposite. Following is the sequence of amino acids coded by an mRNA. Predict the nucleotide sequence in the RNA: Met-Phe-Phe-Phe-Phe-Phe-Phe" | |
| F290 | 5.6 | question | "Do you face any difficulty in predicting the opposite?" | |
| F291 | 5.6 | question | "Can you now correlate which two properties of genetic code you have learnt?" | |
| F292 | 5.6.1 | concept | "You have studied about mutation and its effect in Chapter 4." | |
| F293 | 5.6.1 | concept | "Effects of large deletions and rearrangements in a segment of DNA are easy to comprehend. It may result in loss or gain of a gene and so a function." | |
| F294 | 5.6.1 | concept | "The effect of point mutations will be explained here." | |
| F295 | 5.6.1 | example | "A classical example of point mutation is a change of single base pair in the gene for beta globin chain that results in the change of amino acid residue glutamate to valine." | |
| F296 | 5.6.1 | concept | "It results into a diseased condition called as sickle cell anemia." | |
| F297 | 5.6.1 | concept | "Effect of point mutations that inserts or deletes a base in structural gene can be better understood by following simple example." | |
| F298 | 5.6.1 | example | "Consider a statement that is made up of the following words each having three letters like genetic code. RAM HAS RED CAP" | |
| F299 | 5.6.1 | example | "If we insert a letter B in between HAS and RED and rearrange the statement, it would read as follows: RAM HAS BRE DCA P" | |
| F300 | 5.6.1 | example | "Similarly, if we now insert two letters at the same place, say BI'. Now it would read, RAM HAS BIR EDC AP" | |
| F301 | 5.6.1 | example | "Now we insert three letters together, say BIG, the statement would read RAM HAS BIG RED CAP" | |
| F302 | 5.6.1 | example | "The same exercise can be repeated, by deleting the letters R, E and D, one by one and rearranging the statement to make a triplet word. RAM HAS EDC AP / RAM HAS DCA P / RAM HAS CAP" | |
| F303 | 5.6.1 | concept | "The conclusion from the above exercise is very obvious. Insertion or deletion of one or two bases changes the reading frame from the point of insertion or deletion." | |
| F304 | 5.6.1 | definition | "However, such mutations are referred to as frameshift insertion or deletion mutations." | |
| F305 | 5.6.1 | concept | "Insertion or deletion of three or its multiple bases insert or delete in one or multiple codon hence one or multiple amino acids, and reading frame remains unaltered from that point onwards." | |
| F306 | 5.6.2 | concept | "He postulated the presence of an adapter molecule that would on one hand read the code and on other hand would bind to specific amino acids." | |
| F307 | 5.6.2 | concept | "The tRNA, then called sRNA (soluble RNA), was known before the genetic code was postulated. However, its role as an adapter molecule was assigned much later." | |
| F308 | 5.6.2 | definition | "tRNA has an anticodon loop that has bases complementary to the code, and it also has an amino acid acceptor end to which it binds to amino acids." | |
| F309 | 5.6.2 | concept | "tRNAs are specific for each amino acid (Figure 5.12)." | |
| F310 | 5.6.2 | definition | "For initiation, there is another specific tRNA that is referred to as initiator tRNA." | |
| F311 | 5.6.2 | concept | "There are no tRNAs for stop codons." | |
| F312 | 5.6.2 | concept | "In figure 5.12, the secondary structure of tRNA has been depicted that looks like a clover-leaf." | |
| F313 | 5.6.2 | concept | "In actual structure, the tRNA is a compact molecule which looks like inverted L." | |
| F314 | 5.7 | concept | "The order and sequence of amino acids are defined by the sequence of bases in the mRNA." | |
| F315 | 5.7 | definition | "The amino acids are joined by a bond which is known as a peptide bond." | |
| F316 | 5.7 | concept | "Formation of a peptide bond requires energy." | |
| F317 | 5.7 | definition | "Therefore, in the first phase itself amino acids are activated in the presence of ATP and linked to their cognate tRNA - a process commonly called as charging of tRNA or aminoacylation of tRNA to be more specific." | |
| F318 | 5.7 | concept | "If two such charged tRNAs are brought close enough, the formation of peptide bond between them would be favoured energetically." | |
| F319 | 5.7 | concept | "The presence of a catalyst would enhance the rate of peptide bond formation." | |
| F320 | 5.7 | definition | "The cellular factory responsible for synthesising proteins is the ribosome." | |
| F321 | 5.7 | number | "The ribosome consists of structural RNAs and about 80 different proteins." | |
| F322 | 5.7 | concept | "In its inactive state, it exists as two subunits; a large subunit and a small subunit." | |
| F323 | 5.7 | concept | "When the small subunit encounters an mRNA, the process of translation of the mRNA to protein begins." | |
| F324 | 5.7 | number | "There are two sites in the large subunit, for subsequent amino acids to bind to and thus, be close enough to each other for the formation of a peptide bond." | |
| F325 | 5.7 | concept | "The ribosome also acts as a catalyst (23S rRNA in bacteria is the enzyme- ribozyme) for the formation of peptide bond." | |
| F326 | 5.7 | definition | "A translational unit in mRNA is the sequence of RNA that is flanked by the start codon (AUG) and the stop codon and codes for a polypeptide." | |
| F327 | 5.7 | definition | "An mRNA also has some additional sequences that are not translated and are referred as untranslated regions (UTR)." | |
| F328 | 5.7 | concept | "The UTRs are present at both 5'-end (before start codon) and at 3'-end (after stop codon)." | |
| F329 | 5.7 | concept | "They are required for efficient translation process." | |
| F330 | 5.7 | concept | "For initiation, the ribosome binds to the mRNA at the start codon (AUG) that is recognised only by the initiator tRNA." | |
| F331 | 5.7 | concept | "The ribosome proceeds to the elongation phase of protein synthesis." | |
| F332 | 5.7 | concept | "During this stage, complexes composed of an amino acid linked to tRNA, sequentially bind to the appropriate codon in mRNA by forming complementary base pairs with the tRNA anticodon." | |
| F333 | 5.7 | concept | "The ribosome moves from codon to codon along the mRNA." | |
| F334 | 5.7 | concept | "Amino acids are added one by one, translated into Polypeptide sequences dictated by DNA and represented by mRNA." (source capitalises "Polypeptide" mid-sentence; reproduce NCERT's own casing) | |
| F335 | 5.7 | concept | "At the end, a release factor binds to the stop codon, terminating translation and releasing the complete polypeptide from the ribosome." | |
| F336 | 5.8 | concept | "Considering that gene expression results in the formation of a polypeptide, it can be regulated at several levels." | |
| F337 | 5.8 | list | "In eukaryotes, the regulation could be exerted at (i) transcriptional level (formation of primary transcript), (ii) processing level (regulation of splicing), (iii) transport of mRNA from nucleus to the cytoplasm, (iv) translational level." | |
| F338 | 5.8 | concept | "The genes in a cell are expressed to perform a particular function or a set of functions." | |
| F339 | 5.8 | example | "For example, if an enzyme called beta-galactosidase is synthesised by E. coli, it is used to catalyse the hydrolysis of a disaccharide, lactose into galactose and glucose; the bacteria use them as a source of energy." | |
| F340 | 5.8 | concept | "Hence, if the bacteria do not have lactose around them to be utilised for energy source, they would no longer require the synthesis of the enzyme beta-galactosidase." | |
| F341 | 5.8 | concept | "Therefore, in simple terms, it is the metabolic, physiological or environmental conditions that regulate the expression of genes." | |
| F342 | 5.8 | concept | "The development and differentiation of embryo into adult organisms are also a result of the coordinated regulation of expression of several sets of genes." | |
| F343 | 5.8 | concept | "In prokaryotes, control of the rate of transcriptional initiation is the predominant site for control of gene expression." | |
| F344 | 5.8 | concept | "In a transcription unit, the activity of RNA polymerase at a given promoter is in turn regulated by interaction with accessory proteins, which affect its ability to recognise start sites." | |
| F345 | 5.8 | definition | "These regulatory proteins can act both positively (activators) and negatively (repressors)." | |
| F346 | 5.8 | definition | "The accessibility of promoter regions of prokaryotic DNA is in many cases regulated by the interaction of proteins with sequences termed operators." | |
| F347 | 5.8 | concept | "The operator region is adjacent to the promoter elements in most operons and in most cases the sequences of the operator bind a repressor protein." | |
| F348 | 5.8 | concept | "Each operon has its specific operator and specific repressor." | |
| F349 | 5.8 | example | "For example, lac operator is present only in the lac operon and it interacts specifically with lac repressor only." | |
| F350 | 5.8.1 | name | "They were the first to elucidate a transcriptionally regulated system." | |
| F351 | 5.8.1 | definition | "In lac operon (here lac refers to lactose), a polycistronic structural gene is regulated by a common promoter and regulatory genes." | |
| F352 | 5.8.1 | definition | "Such arrangement is very common in bacteria and is referred to as operon." | |
| F353 | 5.8.1 | example | "To name few such examples, lac operon, trp operon, ara operon, his operon, val operon, etc." | |
| F354 | 5.8.1 | definition | "The lac operon consists of one regulatory gene (the i gene - here the term i does not refer to inducer, rather it is derived from the word inhibitor) and three structural genes (z, y, and a)." | |
| F355 | 5.8.1 | concept | "The i gene codes for the repressor of the lac operon." | |
| F356 | 5.8.1 | concept | "The z gene codes for beta-galactosidase (beta-gal), which is primarily responsible for the hydrolysis of the disaccharide, lactose into its monomeric units, galactose and glucose." | |
| F357 | 5.8.1 | concept | "The y gene codes for permease, which increases permeability of the cell to beta-galactosides." | |
| F358 | 5.8.1 | concept | "The a gene encodes a transacetylase." | |
| F359 | 5.8.1 | concept | "Hence, all the three gene products in lac operon are required for metabolism of lactose." | |
| F360 | 5.8.1 | concept | "In most other operons as well, the genes present in the operon are needed together to function in the same or related metabolic pathway (Figure 5.14)." | |
| F361 | 5.8.1 | definition | "Lactose is the substrate for the enzyme beta-galactosidase and it regulates switching on and off of the operon. Hence, it is termed as inducer." | |
| F362 | 5.8.1 | concept | "In the absence of a preferred carbon source such as glucose, if lactose is provided in the growth medium of the bacteria, the lactose is transported into the cells through the action of permease (Remember, a very low level of expression of lac operon has to be present in the cell all the time, otherwise lactose cannot enter the cells)." | |
| F363 | 5.8.1 | concept | "The lactose then induces the operon in the following manner." | |
| F364 | 5.8.1 | concept | "The repressor of the operon is synthesised (all-the-time - constitutively) from the i gene." | |
| F365 | 5.8.1 | concept | "The repressor protein binds to the operator region of the operon and prevents RNA polymerase from transcribing the operon." | |
| F366 | 5.8.1 | concept | "In the presence of an inducer, such as lactose or allolactose, the repressor is inactivated by interaction with the inducer." | |
| F367 | 5.8.1 | concept | "This allows RNA polymerase access to the promoter and transcription proceeds (Figure 5.14)." | |
| F368 | 5.8.1 | concept | "Essentially, regulation of lac operon can also be visualised as regulation of enzyme synthesis by its substrate." | |
| F369 | 5.8.1 | concept | "Remember, glucose or galactose cannot act as inducers for lac operon." | |
| F370 | 5.8.1 | question | "Can you think for how long the lac operon would be expressed in the presence of lactose?" | |
| F371 | 5.8.1 | definition | "Regulation of lac operon by repressor is referred to as negative regulation." | |
| F372 | 5.8.1 | concept | "Lac operon is under control of positive regulation as well, but it is beyond the scope of discussion at this level." | |
| F373 | 5.9 | concept | "In other words, genetic make-up of an organism or an individual lies in the DNA sequences." | |
| F374 | 5.9 | concept | "If two individuals differ, then their DNA sequences should also be different, at least at some places." | |
| F375 | 5.9 | concept | "These assumptions led to the quest of finding out the complete DNA sequence of human genome." | |
| F376 | 5.9 | number | "With the establishment of genetic engineering techniques where it was possible to isolate and clone any piece of DNA and availability of simple and fast techniques for determining DNA sequences, a very ambitious project of sequencing human genome was launched in the year 1990." | |
| F377 | 5.9 | concept | "Human Genome Project (HGP) was called a mega project." | |
| F378 | 5.9 | concept | "You can imagine the magnitude and the requirements for the project if we simply define the aims of the project as follows:" | |
| F379 | 5.9 | number | "Human genome is said to have approximately 3 x 10^9 bp, and if the cost of sequencing required is US $ 3 per bp (the estimated cost in the beginning), the total estimated cost of the project would be approximately 9 billion US dollars." | |
| F380 | 5.9 | number | "Further, if the obtained sequences were to be stored in typed form in books, and if each page of the book contained 1000 letters and each book contained 1000 pages, then 3300 such books would be required to store the information of DNA sequence from a single human cell." | |
| F381 | 5.9 | concept | "The enormous amount of data expected to be generated also necessitated the use of high speed computational devices for data storage and retrieval, and analysis." | |
| F382 | 5.9 | definition | "HGP was closely associated with the rapid development of a new area in biology called Bioinformatics." | |
| F383 | 5.9 (Goals of HGP) | number | "(i) Identify all the approximately 20,000-25,000 genes in human DNA;" | |
| F384 | 5.9 (Goals of HGP) | number | "(ii) Determine the sequences of the 3 billion chemical base pairs that make up human DNA;" | |
| F385 | 5.9 (Goals of HGP) | list | "(iiii) Store this information in databases;" (the source really prints the numeral as "(iiii)" - reproduce the item as "(iii)" in the rewrite but do not silently renumber the rest; see carry-over 12) | |
| F386 | 5.9 (Goals of HGP) | list | "(iv) Improve tools for data analysis;" | |
| F387 | 5.9 (Goals of HGP) | list | "(v) Transfer related technologies to other sectors, such as industries;" | |
| F388 | 5.9 (Goals of HGP) | list | "(vi) Address the ethical, legal, and social issues (ELSI) that may arise from the project." | |
| F389 | 5.9 | number | "The Human Genome Project was a 13-year project coordinated by the U.S. Department of Energy and the National Institute of Health." | |
| F390 | 5.9 | name | "During the early years of the HGP, the Wellcome Trust (U.K.) became a major partner; additional contributions came from Japan, France, Germany, China and others." | |
| F391 | 5.9 | number | "The project was completed in 2003." | |
| F392 | 5.9 | concept | "Knowledge about the effects of DNA variations among individuals can lead to revolutionary new ways to diagnose, treat and someday prevent the thousands of disorders that affect human beings." | |
| F393 | 5.9 | concept | "Besides providing clues to understanding human biology, learning about non-human organisms DNA sequences can lead to an understanding of their natural capabilities that can be applied toward solving challenges in health care, agriculture, energy production, environmental remediation." | |
| F394 | 5.9 | example | "Many non-human model organisms, such as bacteria, yeast, Caenorhabditis elegans (a free living non-pathogenic nematode), Drosophila (the fruit fly), plants (rice and Arabidopsis), etc., have also been sequenced." | |
| F395 | 5.9 | concept | "Methodologies : The methods involved two major approaches." (10.5pt bold run-in label, **not** a standalone heading - see carry-over 10) | |
| F396 | 5.9 | definition | "One approach focused on identifying all the genes that are expressed as RNA (referred to as Expressed Sequence Tags (ESTs)." | |
| F397 | 5.9 | definition | "The other took the blind approach of simply sequencing the whole set of genome that contained all the coding and non-coding sequence, and later assigning different regions in the sequence with functions (a term referred to as Sequence Annotation)." | |
| F398 | 5.9 | concept | "For sequencing, the total DNA from a cell is isolated and converted into random fragments of relatively smaller sizes (recall DNA is a very long polymer, and there are technical limitations in sequencing very long pieces of DNA) and cloned in suitable host using specialised vectors." | |
| F399 | 5.9 | concept | "The cloning resulted into amplification of each piece of DNA fragment so that it subsequently could be sequenced with ease." | |
| F400 | 5.9 | definition | "The commonly used hosts were bacteria and yeast, and the vectors were called as BAC (bacterial artificial chromosomes), and YAC (yeast artificial chromosomes)." | |
| F401 | 5.9 | name | "The fragments were sequenced using automated DNA sequencers that worked on the principle of a method developed by Frederick Sanger." | |
| F402 | 5.9 | name | "(Remember, Sanger is also credited for developing method for determination of amino acid sequences in proteins)." | |
| F403 | 5.9 | concept | "These sequences were then arranged based on some overlapping regions present in them. This required generation of overlapping fragments for sequencing." | |
| F404 | 5.9 | concept | "Alignment of these sequences was humanly not possible. Therefore, specialised computer based programs were developed (Figure 5.15)." | |
| F405 | 5.9 | concept | "These sequences were subsequently annotated and were assigned to each chromosome." | |
| F406 | 5.9 | number | "The sequence of chromosome 1 was completed only in May 2006 (this was the last of the 24 human chromosomes - 22 autosomes and X and Y - to be sequenced)." | |
| F407 | 5.9 | concept | "Another challenging task was assigning the genetic and physical maps on the genome." | |
| F408 | 5.9 | definition | "This was generated using information on polymorphism of restriction endonuclease recognition sites, and some repetitive DNA sequences known as microsatellites (one of the applications of polymorphism in repetitive DNA sequences shall be explained in next section of DNA fingerprinting)." | |
| F409 | 5.9.1 | number | "(i) The human genome contains 3164.7 million bp." | |
| F410 | 5.9.1 | number | "(ii) The average gene consists of 3000 bases, but sizes vary greatly, with the largest known human gene being dystrophin at 2.4 million bases." | |
| F411 | 5.9.1 | number | "(iii) The total number of genes is estimated at 30,000-much lower than previous estimates of 80,000 to 1,40,000 genes. Almost all (99.9 per cent) nucleotide bases are exactly the same in all humans." | |
| F412 | 5.9.1 | number | "(iv) The functions are unknown for over 50 per cent of the discovered genes." | |
| F413 | 5.9.1 | number | "(v) Less than 2 per cent of the genome codes for proteins." | |
| F414 | 5.9.1 | concept | "(vi) Repeated sequences make up very large portion of the human genome." | |
| F415 | 5.9.1 | definition | "(vii) Repetitive sequences are stretches of DNA sequences that are repeated many times, sometimes hundred to thousand times. They are thought to have no direct coding functions, but they shed light on chromosome structure, dynamics and evolution." | |
| F416 | 5.9.1 | number | "(viii) Chromosome 1 has most genes (2968), and the Y has the fewest (231)." | |
| F417 | 5.9.1 | number | "(ix) Scientists have identified about 1.4 million locations where single-base DNA differences (SNPs - single nucleotide polymorphism, pronounced as 'snips') occur in humans. This information promises to revolutionise the processes of finding chromosomal locations for disease-associated sequences and tracing human history." | |
| F418 | 5.9.2 | concept | "This enormous task will require the expertise and creativity of tens of thousands of scientists from varied disciplines in both the public and private sectors worldwide." | |
| F419 | 5.9.2 | concept | "One of the greatest impacts of having the HG sequence may well be enabling a radically new approach to biological research." | |
| F420 | 5.9.2 | concept | "In the past, researchers studied one or a few genes at a time." | |
| F421 | 5.9.2 | concept | "With whole-genome sequences and new high-throughput technologies, we can approach questions systematically and on a much broader scale." | |
| F422 | 5.9.2 | concept | "They can study all the genes in a genome, for example, all the transcripts in a particular tissue or organ or tumor, or how tens of thousands of genes and proteins work together in interconnected networks to orchestrate the chemistry of life." | |
| F423 | 5.10 | question | "Assuming human genome as 3 x 10^9 bp, in how many base sequences would there be differences?" | |
| F424 | 5.10 | concept | "It is these differences in sequence of DNA which make every individual unique in their phenotypic appearance." | |
| F425 | 5.10 | concept | "If one aims to find out genetic differences between two individuals or among individuals of a population, sequencing the DNA every time would be a daunting and expensive task." | |
| F426 | 5.10 | number | "Imagine trying to compare two sets of 3 x 10^6 base pairs." (the source prints the exponent as 6 here, two sentences after printing 3 x 10^9 for the same genome - reproduce as printed; see carry-over 11) | |
| F427 | 5.10 | definition | "DNA fingerprinting is a very quick way to compare the DNA sequences of any two individuals." | |
| F428 | 5.10 | definition | "DNA fingerprinting involves identifying differences in some specific regions in DNA sequence called as repetitive DNA, because in these sequences, a small stretch of DNA is repeated many times." | |
| F429 | 5.10 | concept | "These repetitive DNA are separated from bulk genomic DNA as different peaks during density gradient centrifugation." | |
| F430 | 5.10 | definition | "The bulk DNA forms a major peak and the other small peaks are referred to as satellite DNA." | |
| F431 | 5.10 | list | "Depending on base composition (A : T rich or G:C rich), length of segment, and number of repetitive units, the satellite DNA is classified into many categories, such as micro-satellites, mini-satellites etc." | |
| F432 | 5.10 | concept | "These sequences normally do not code for any proteins, but they form a large portion of human genome." | |
| F433 | 5.10 | concept | "These sequence show high degree of polymorphism and form the basis of DNA fingerprinting." | |
| F434 | 5.10 | concept | "Since DNA from every tissue (such as blood, hair-follicle, skin, bone, saliva, sperm etc.), from an individual show the same degree of polymorphism, they become very useful identification tool in forensic applications." | |
| F435 | 5.10 | concept | "Further, as the polymorphisms are inheritable from parents to children, DNA fingerprinting is the basis of paternity testing, in case of disputes." | |
| F436 | 5.10 | concept | "As polymorphism in DNA sequence is the basis of genetic mapping of human genome as well as of DNA fingerprinting, it is essential that we understand what DNA polymorphism means in simple terms." | |
| F437 | 5.10 | definition | "Polymorphism (variation at genetic level) arises due to mutations." | |
| F438 | 5.10 | concept | "(Recall different kind of mutations and their effects that you have already studied in Chapter 4, and in the preceding sections in this chapter.)" | |
| F439 | 5.10 | concept | "New mutations may arise in an individual either in somatic cells or in the germ cells (cells that generate gametes in sexually reproducing organisms)." | |
| F440 | 5.10 | concept | "If a germ cell mutation does not seriously impair individual's ability to have offspring who can transmit the mutation, it can spread to the other members of population (through sexual reproduction)." | |
| F441 | 5.10 | number | "Allelic (again recall the definition of alleles from Chapter 4) sequence variation has traditionally been described as a DNA polymorphism if more than one variant (allele) at a locus occurs in human population with a frequency greater than 0.01." | |
| F442 | 5.10 | definition | "In simple terms, if an inheritable mutation is observed in a population at high frequency, it is referred to as DNA polymorphism." | |
| F443 | 5.10 | concept | "The probability of such variation to be observed in non-coding DNA sequence would be higher as mutations in these sequences may not have any immediate effect/impact in an individual's reproductive ability." | |
| F444 | 5.10 | concept | "These mutations keep on accumulating generation after generation, and form one of the basis of variability/polymorphism." | |
| F445 | 5.10 | concept | "There is a variety of different types of polymorphisms ranging from single nucleotide change to very large scale changes." | |
| F446 | 5.10 | concept | "For evolution and speciation, such polymorphisms play very important role, and you will study these in details at higher classes." | |
| F447 | 5.10 | name | "The technique of DNA Fingerprinting was initially developed by Alec Jeffreys." | |
| F448 | 5.10 | definition | "He used a satellite DNA as probe that shows very high degree of polymorphism. It was called as Variable Number of Tandem Repeats (VNTR)." | |
| F449 | 5.10 | concept | "The technique, as used earlier, involved Southern blot hybridisation using radiolabelled VNTR as a probe." | |
| F450 | 5.10 | list | "(i) isolation of DNA," | |
| F451 | 5.10 | list | "(ii) digestion of DNA by restriction endonucleases," | |
| F452 | 5.10 | list | "(iii) separation of DNA fragments by electrophoresis," | |
| F453 | 5.10 | list | "(iv) transferring (blotting) of separated DNA fragments to synthetic membranes, such as nitrocellulose or nylon," | |
| F454 | 5.10 | list | "(v) hybridisation using labelled VNTR probe, and" | |
| F455 | 5.10 | list | "(vi) detection of hybridised DNA fragments by autoradiography." | |
| F456 | 5.10 | concept | "A schematic representation of DNA fingerprinting is shown in Figure 5.16." | |
| F457 | 5.10 | definition | "The VNTR belongs to a class of satellite DNA referred to as mini-satellite." | |
| F458 | 5.10 | concept | "A small DNA sequence is arranged tandemly in many copy numbers." | |
| F459 | 5.10 | concept | "The copy number varies from chromosome to chromosome in an individual." | |
| F460 | 5.10 | concept | "The numbers of repeat show very high degree of polymorphism." | |
| F461 | 5.10 | number | "As a result the size of VNTR varies in size from 0.1 to 20 kb." | |
| F462 | 5.10 | concept | "Consequently, after hybridisation with VNTR probe, the autoradiogram gives many bands of differing sizes." | |
| F463 | 5.10 | concept | "These bands give a characteristic pattern for an individual DNA (Figure 5.16)." | |
| F464 | 5.10 | concept | "It differs from individual to individual in a population except in the case of monozygotic (identical) twins." | |
| F465 | 5.10 | concept | "The sensitivity of the technique has been increased by use of polymerase chain reaction (PCR- you will study about it in Chapter 9)." | |
| F466 | 5.10 | concept | "Consequently, DNA from a single cell is enough to perform DNA fingerprinting analysis." | |
| F467 | 5.10 | concept | "In addition to application in forensic science, it has much wider application, such as in determining population and genetic diversities." | |
| F468 | 5.10 | concept | "Currently, many different probes are used to generate DNA fingerprints." | |
| F469 | Exercises | question | "1 Group the following as nitrogenous bases and nucleosides: Adenine, Cytidine, Thymine, Guanosine, Uracil and Cytosine." | |
| F470 | Exercises | question | "2. If a double stranded DNA has 20 per cent of cytosine, calculate the per cent of adenine in the DNA." | |
| F471 | Exercises | question | "3. If the sequence of one strand of DNA is written as follows: 5'-ATGCATGCATGCATGCATGCATGCATGC-3' Write down the sequence of complementary strand in 5'-to-3' direction." | |
| F472 | Exercises | question | "4. If the sequence of the coding strand in a transcription unit is written as follows: 5'-ATGCATGCATGCATGCATGCATGCATGC-3' Write down the sequence of mRNA." | |
| F473 | Exercises | question | "5. Which property of DNA double helix led Watson and Crick to hypothesise semi-conservative mode of DNA replication? Explain." | |
| F474 | Exercises | question | "6. Depending upon the chemical nature of the template (DNA or RNA) and the nature of nucleic acids synthesised from it (DNA or RNA), list the types of nucleic acid polymerases." | |
| F475 | Exercises | question | "7. How did Hershey and Chase differentiate between DNA and protein in their experiment while proving that DNA is the genetic material?" | |
| F476 | Exercises | question | "8. Differentiate between the followings: (a) Repetitive DNA and Satellite DNA (b) mRNA and tRNA (c) Template strand and Coding strand" | |
| F477 | Exercises | question | "9. List two essential roles of ribosome during translation." | |
| F478 | Exercises | question | "10. In the medium where E. coli was growing, lactose was added, which induced the lac operon. Then, why does lac operon shut down some time after addition of lactose in the medium?" | |
| F479 | Exercises | question | "11. Explain (in one or two lines) the function of the followings: (a) Promoter (b) tRNA (c) Exons" | |
| F480 | Exercises | question | "12. Why is the Human Genome project called a mega project?" | |
| F481 | Exercises | question | "13. What is DNA fingerprinting? Mention its application." | |
| F482 | Exercises | question | "14. Briefly describe the following: (a) Transcription (b) Polymorphism (c) Translation (d) Bioinformatics" | |
| F483 | 5.6 | heading | "5.6  GENETIC CODE" (p17, 13.0pt Bookman-Demi section banner; the seam banner - mid-page, with the tail of 5.5.3 above it) | |
| F484 | 5.6.1 | heading | "5.6.1 Mutations and Genetic Code" (p19, 12.0pt Bookman-Demi) | |
| F485 | 5.6.2 | heading | "5.6.2 tRNA– the Adapter Molecule" (p20, 12.0pt Bookman-Demi; source sets the en-dash flush against "tRNA" with no leading space - reproduce as "tRNA - the Adapter Molecule" in flat ASCII, see carry-over 3) | |
| F486 | 5.7 | heading | "5.7  TRANSLATION" (p20, 14.0pt Bookman-Demi section banner) | |
| F487 | 5.8 | heading | "5.8  REGULATION OF GENE EXPRESSION" (p21, 13.0pt Bookman-Demi section banner) | |
| F488 | 5.8.1 | heading | "5.8.1 The Lac operon" (p22, 12.0pt Bookman-Demi; source casing is "The Lac operon" - capital L, lowercase o, do not normalise to "lac operon") | |
| F489 | 5.9 | heading | "5.9 HUMAN GENOME PROJECT" (p24, 14.0pt Bookman,Bold section banner; note font family changes from Bookman-Demi to Bookman,Bold at p24 - see carry-over 15) | |
| F490 | 5.9 (Goals of HGP) | heading | "Goals of HGP" (p24, 10.5pt Bookman,Bold, **unnumbered boxed sub-heading** inside 5.9; its six list items are rows F383-F388) | |
| F491 | 5.9.1 | heading | "5.9.1 Salient Features of Human Genome" (p26, 12.0pt Bookman,Bold) | |
| F492 | 5.9.2 | heading | "5.9.2 Applications and Future Challenges" (p26, 12.0pt Bookman,Bold) | |
| F493 | 5.10 | heading | "5.10 DNA FINGERPRINTING" (p27, 14.0pt Bookman-Demi section banner) | |
| F494 | Summary | heading | "SUMMARY" (p30, 13.0pt Bookman-Demi) | |
| F495 | Exercises | heading | "EXERCISES" (p31, **30.0pt AvantGarde-Book - NOT bold**; an all-bold heading filter misses this heading entirely, see carry-over 14) | |
| F496 | 5.6 | opener | "During replication and transcription a nucleic acid was copied to form another nucleic acid." (p17) | |
| F497 | 5.6.1 | opener | "The relationships between genes and DNA are best understood by mutation studies." (p19) | |
| F498 | 5.6.2 | opener | "From the very beginning of the proposition of code, it was clear to Francis Crick that there has to be a mechanism to read the code and also to link it to the amino acids, because amino acids have no structural specialities to read the code uniquely." (p20 - the only place the adapter-molecule rationale is stated) | |
| F499 | 5.7 | opener | "Translation refers to the process of polymerisation of amino acids to form a polypeptide (Figure 5.13)." (p20 - **the chapter's only definition of translation**; if this opener is skipped the chapter ships without defining translation) | |
| F500 | 5.8 | opener | "Regulation of gene expression refers to a very broad term that may occur at various levels." (p21 - **the chapter's only definition of regulation of gene expression**) | |
| F501 | 5.8.1 | opener | "The elucidation of the lac operon was also a result of a close association between a geneticist, Francois Jacob and a biochemist, Jacque Monod." (p22 - carries both names; F350 records only "They were the first...", so this opener is the sole source of Jacob and Monod) | |
| F502 | 5.9 | opener | "In the preceding sections you have learnt that it is the sequence of bases in DNA that determines the genetic information of a given organism." (p24) | |
| F503 | 5.9 (Goals of HGP) | opener | "Some of the important goals of HGP were as follows:" (p24 - stem for the six list items F383-F388) | |
| F504 | 5.9.1 | opener | "Some of the salient observations drawn from human genome project are as follows:" (p26 - stem for the nine list items F409-F417) | |
| F505 | 5.9.2 | opener | "Deriving meaningful knowledge from the DNA sequences will define research through the coming decades leading to our understanding of biological systems." (p26) | |
| F506 | 5.10 | opener | "As stated in the preceding section, 99.9 per cent of base sequence among humans is the same." (p27 - the 99.9 per cent premise the whole DNA-fingerprinting section rests on) | |

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
9. **`Table 5.1` (the 64-codon checker-board, p18) is NOT text-extractable and is not a figure either.** F280 records only its caption. The 64 codon-to-amino-acid cells do not come back from `get_text` in any usable row/column order, so the table must be **hand-built in the script from an authoritative codon table and then proof-read cell-by-cell against the rendered source page**. It must not be clipped as an image (it is a table, not a figure, so `1-F` does not own it) and it must not be silently dropped — F288/F289 are exercises that explicitly instruct the student to "take help of the checkerboard", so the chapter is unusable without it. Decide the owner explicitly before Pass 2a; today it is owned by **nobody**, which is exactly how it will go missing.
10. **`Methodologies :` (p25) is a bold run-in label, not a heading.** 10.5pt bold, followed by light text on the *same* line ("The methods involved two major approaches."). It was deliberately **not** given a heading row by `1b-H`; its content is F395. Thirteen other bold run-in fragments on pp. 17-31 were checked and all are ordinary inline bold emphasis on defined terms mid-sentence (`frameshift insertion`, `aminoacylation of tRNA`, `Sequence Annotation`, `Polymorphism`, `heterogeneous nuclear RNA`, etc.). Do not promote any of them to headings, and do not let a "bold-at-line-start" heuristic do it either.
11. **NCERT prints the human genome size inconsistently inside §5.10.** F423 (from the opener's following sentence) has `3 x 10^9 bp`; two sentences later F426 has `Imagine trying to compare two sets of 3 x 10^6 base pairs.` The `10^6` is the source's own error. **Reproduce both exactly as printed** and do not "fix" the exponent — but flag it in the chapter's teaching note if one exists, because a student comparing the two lines will otherwise think they misread.
12. **NCERT mis-numbers the third Goals-of-HGP item as `(iiii)`** (p24, F385). The rewrite prints it as `(iii)` so the list reads i-ii-iii-iv-v-vi, and the remaining items are **not** renumbered. Do not treat the `(iiii)`/`(iii)` difference as a transcription error in a later verification pass.
13. **Second-half openers carrying load-bearing definitions — delivered by `1b-O`, listed here so no later pass drops them.** `§5.7` (F499) is **the chapter's only definition of translation** and `§5.8` (F500) **the only definition of regulation of gene expression** — the same failure mode as carry-over 1's §5.5/§5.5.2. `§5.8.1` (F501) is the sole source of the names **Francois Jacob and Jacque Monod**. `§5.10` (F506) carries the **99.9 per cent** premise the entire DNA-fingerprinting argument rests on. All four must survive into the script.
14. **`EXERCISES` (p31) is set in 30.0pt AvantGarde-**Book** — it is not bold.** Every other second-half heading is Demi/Bold, so an "all spans bold" heading filter silently drops the Exercises heading while appearing to work perfectly. The chapter-title row F232 is the same non-bold 30pt display class. Any heading re-parse must accept non-bold display type above ~13pt, or assert these two rows exist by name.
15. **Book-page folios are 14.0pt bold and outrank every sub-heading.** The printed page numbers `95`-`109` are set 14.0pt `AvantGarde-Demi` / `CenturyGothic,Bold` — they pass a `bold and size >= 10.5` heading filter and yield ~15 phantom heading rows, a *different* trap from the 9.0pt running heads already recorded in `Ch5_TRACKER.md` §4 trap 1 (a 10.5pt floor does **not** exclude these). **Filter numeric-only lines.** Related: the body font family switches from `Bookman-Demi`/`AvantGarde-Demi` to `Bookman,Bold`/`CenturyGothic,Bold` at **p24**, so a filter keyed on the literal string `Demi` misses the §5.9, §5.9.1 and §5.9.2 headings entirely.
16. **The `RAM HAS RED CAP` frameshift mnemonic is 10.5pt full-bold on its own line, seven times (p19).** Those seven lines are prose examples (F298-F302), **not** headings — full-bold standalone lines at exactly the unnumbered-sub-heading size and weight. `1b-H` excluded them deliberately. Also `anticodon loop` (p20, 10.5pt full-bold standalone) is an **in-figure label for Figure 5.12 owned by `1-F`** - the same class of trap as `Central dogma` in carry-over 2, and it must not become a heading row.
