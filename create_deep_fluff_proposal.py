"""
Deep, unit-wise fluff-removal / rewording proposal (Human Physiology excluded).

Every row is a real passage pulled from a chapter build script under notes/ (file + line
number), with an action and a proposed replacement. Source hits come from
scratch/scan_fluff.py -> scratch/strong.json (regenerated here if missing).
Output: NCERT_Biology_Fluff_Removal_Proposal_DEEP.docx

Revision 2 - aligned to SUPREME COMMAND PROMPT v6:
  * Rule 1/4 - every NCERT fact and qualifier word is preserved verbatim in the rewrite.
  * Rule 2   - exercise sections are titled "Terms used in the exercises" and hold only GAP
               questions; COVERED questions are deleted, never cross-referenced.
  * Rule 3   - summary-only facts move into the body; reader prompts are cut.
  * Rule 5   - any answer not stated by NCERT goes in a MEMORY AID box or the appendix,
               labelled as an addition.
  * Rule 6   - no scope lines, roadmaps-by-script, or notes about what NCERT does/doesn't say.
  * The "Think Box" device is gone: neet_template.py only has note() and memory_aid().
"""
import json, os, subprocess, sys, glob
from docx import Document
from docx.shared import Pt, RGBColor, Inches
from docx.enum.section import WD_ORIENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

ROOT = os.path.dirname(os.path.abspath(__file__))
HITS = os.path.join(ROOT, "scratch", "strong.json")
ALL = os.path.join(ROOT, "scratch", "fluff_hits.json")
if not os.path.exists(HITS):
    subprocess.run([sys.executable, os.path.join(ROOT, "scratch", "scan_fluff.py")], check=True)

D, R, N, M, A, K = "DELETE", "REWORD", "NOTE", "MEMORY AID", "APPENDIX", "KEEP"
ACTIONS = [D, R, N, M, A, K]
EX_TITLE = "Terms used in the exercises"
EX_DEL = (f"Delete the preamble. The exercise appendix is titled '{EX_TITLE}' and exists only if "
          "the chapter has GAP questions (Rule 2); COVERED questions are not reproduced.")

P = {
"11/Ch1": {
 0: (R, "A group name (dogs, mammals, wheat) instantly recalls a set of shared characters - this is the basis of classification."),
 1: (K, "Functional definitions list; the '?' is part of a definition, not rhetoric."),
 2: (D, EX_DEL),
 3: (D, "Q8 is COVERED by the body definition of species - delete the exercise entry (Rule 2). Move the Ernst Mayr "
        "sentence ('Ernst Mayr pioneered the currently accepted definition of a biological species') into the body "
        "where species is defined, since it is NCERT unit-profile text. Drop 'In this chapter', 'The unit profile adds' "
        "and the 'left to discussion with your teacher' sentence (Rule 6)."),
},
"11/Ch2": {
 0: (R, "Table 2.1 - Five-kingdom comparison."),
 1: (R, "Three-domain system: Monera split into two domains; all eukaryotic kingdoms in the third -> six-kingdom classification. (Delete 'You will learn ... higher classes'.)"),
 2: (D, "Pure invitation; the next paragraph already explains the criteria."),
 3: (D, "Scope line - announces coming content (Rule 6); the section headings do this job. The name 'plant and animal "
        "kingdoms' for Plantae/Animalia stays in the 2.4 / 2.5 headings."),
 4: (R, "Viruses - living or non-living? Non-living: no cell structure; inert crystals outside host. Living: infectious genetic material; replicate using host machinery inside a cell."),
 5: (R, "The algal and fungal partners are so intimately associated that a lichen appears to be one organism."),
 6: (D, EX_DEL),
 7: (D, "Q12 is COVERED by the 2.6a note (both sides given there) - delete outright; no cross-reference (Rule 2: a question is answered once, in one place)."),
},
"11/Ch3": {
 0: (R, "Kingdom Plantae (Whittaker's 1969 Five Kingdom classification), popularly called the plant kingdom, comprises "
        "algae, bryophytes, pteridophytes, gymnosperms and angiosperms. (Delete 'The chapter map is' and 'In the previous chapter' - Rule 6.)"),
},
"11/Ch5": {
 0: (R, "Stem vs root: stems bear nodes and internodes, multicellular hairs, and are positively phototropic."),
},
"11/Ch7": {
 0: (R, "Protonema - first, green, branched, filamentous gametophyte stage of moss."),
},
"11/Ch8": {
 0: (R, "Plasmids: small extra-chromosomal DNA giving unique phenotypes, e.g. antibiotic resistance. Used to monitor bacterial transformation."),
 1: (R, "Normally, there is only one nucleus per cell; variations in the number of nuclei are also frequently observed. "
        "(Delete 'Can you recollect names of organisms...?'.)"),
 2: (R, "Some mature cells lack a nucleus - mammalian RBCs, sieve-tube cells."),
 3: (R, "Chromatin contains DNA and some basic proteins called histones, some non-histone proteins and also RNA. A single "
        "human cell has approximately two metre long thread of DNA distributed among its forty six (twenty three pairs) "
        "chromosomes. (Delete 'You will study ... in class XII'.)"),
 4: (A, f"'{EX_TITLE}' entry - Q9 is a GAP. Reproduce in full: 'Multicellular organisms have division of labour. Explain.' "
        "Answer (label: addition built from chapter facts): a unicellular organism performs all essential functions of life "
        "in its one cell; in a multicellular organism cell shape varies with function, so different cells take on different "
        "functions - this distribution of functions is division of labour. Delete 'appears nowhere in this chapter' and "
        "'No fact from outside the chapter' (Rule 6)."),
 5: (D, "Q13 is COVERED - nucleus by Figure 8.11, centrosome by section 8.5.9 - delete the exercise entry (Rule 2). "
        "Delete 'NCERT prints no figure ... none is invented here' (Rule 6)."),
},
"11/Ch9": {
 0: (R, "Despite enormous diversity, all organisms share remarkably similar chemical composition and metabolic reactions."),
 1: (R, "Delete the last sentence ('Can you identify a fat from the market?'). Keep the glycerides / oils-vs-fats facts."),
 2: (R, "Lipids (<800 Da) are not polymers, yet they appear in the acid-insoluble fraction because on grinding they form insoluble membrane vesicles."),
 3: (R, "Heading: 'Mechanism of Enzyme Action - How Rates Increase'."),
 4: (R, "The organic compounds in living tissue are identified by chemical analysis."),
},
"11/Ch10": {
 0: (N, "NOTE box (answer is NCERT text): Plant meristems (apical, lateral cambium) divide throughout life; most "
        "differentiated cells exit the cell cycle into G0. Drop the 'NCERT stops the reader three times' framing (Rule 6)."),
 1: (R, "Haploid animal cells can divide by mitosis - e.g. the male honey bee (10.1.1)."),
},
"11/Ch11": {
 0: (D, "Throat-clearing; the experiments follow immediately."),
 1: (R, "His later studies showed that the green substance in plants (chlorophyll) is located in special bodies (later "
        "called chloroplasts) within plant cells. (Keep 'His' - the subject is named in the preceding sentence.)"),
 2: (R, "Leaves differ in shade of green because they contain several pigments (Chl a, Chl b, xanthophylls, carotenoids) in different proportions."),
 3: (R, "PS II supplies electrons continuously by replacing them through splitting of water (photolysis)."),
 4: (R, "ATP synthesis in the chloroplast is explained by the chemiosmotic hypothesis."),
 5: (R, "Central question of the dark reaction: what is the primary CO2 acceptor and the first stable product of CO2 fixation?"),
 6: (R, "Mesophyll cells of C4 plants lack RuBisCO."),
 7: (N, "NOTE box: C3 and C4 plants differ in leaf anatomy - C4 leaves show Kranz anatomy (bundle-sheath cells). "
        "Delete the question 'can you tell ... externally?'."),
 8: (N, "NOTE box: Chlorophyll a is the chief pigment of photosynthesis; accessory pigments (Chl b, xanthophylls, "
        "carotenoids) absorb a wider range of wavelengths and protect chlorophyll a from photo-oxidation. Delete the hypothetical question."),
 9: (M, "MEMORY AID (not in NCERT): a leaf kept in the dark turns yellow / pale green because chlorophyll breaks down "
        "while the more stable carotenoids and xanthophylls remain. Delete the question from body text."),
 10: (D, "Observation activity - checked: contains no stated fact, only instructions and a question. Remove."),
},
"11/Ch12": {
 0: (R, "Pyruvate has three fates depending on cellular need: lactic acid fermentation, alcoholic fermentation, aerobic respiration."),
 1: (R, "ATP synthesis here follows the chemiosmotic mechanism (see Ch11)."),
},
"12/Ch2": {}, "12/Ch1": {},
"12/Ch3": {
 0: (K, "Q-and-A bullet format is functional; leave as is."),
 1: (K, "Q-and-A bullet format is functional; leave as is."),
},
"12/Ch4": {
 0: (R, "Genotype Tt -> tall phenotype (T is dominant)."),
 1: (R, "Use one letter for both alleles of a gene (T/t), never T/d."),
 2: (R, "Heading: 'Concept of Dominance'."),
 3: (R, "Each gene carries the information to express a particular trait."),
 4: (R, "One allele may be altered (mutated), modifying the information it carries."),
 5: (R, "Example: a gene coding for an enzyme, present as two alleles."),
 6: (R, "Usually the normal allele produces the normal enzyme that transforms substrate S."),
 7: (R, "ABO blood groups also show multiple alleles: three alleles (IA, IB, i) govern one character."),
 8: (R, "Symbols: Y yellow (dominant) / y green; R round (dominant) / r wrinkled."),
 9: (R, "Figure 4.8 - chromosome segregation during meiosis in a 4-chromosome cell: G2 -> bivalent -> Meiosis I (homologues separate) -> Meiosis II (sister chromatids separate). Delete 'Read the plate' / 'Can you see'."),
 10: (R, "Chromosomes and genes both occur in pairs (mitosis = equational, meiosis = reduction division)."),
 11: (R, "Many traits are not discrete but vary along a gradient -> polygenic inheritance."),
 12: (R, "Model: three genes A, B, C control human skin colour; dominant A, B, C -> dark, recessive a, b, c -> light."),
 13: (R, "In both XO and XY types, males produce two different types of gametes - (a) either with or without an X "
         "chromosome (XO type), or (b) some with an X chromosome and some with a Y chromosome (XY type). This is male "
         "heterogamety. (Delete 'In the above description you have studied'.)"),
 14: (R, "Each chromatid carries one continuous, highly supercoiled DNA double helix."),
},
"12/Ch5": {
 0: (R, "Polynucleotide structure: a nucleotide is built in three steps, each adding one component."),
 1: (R, "... 6.6 x 10^9 bp x 0.34 x 10^-9 m/bp = 2.2 metres - a length far greater than the dimension of a typical "
        "nucleus (approximately 10^-6 m). End there; the nucleosome paragraph that follows supplies the packaging. "
        "(Delete 'How is such a long polymer packaged in a cell?'.)"),
 2: (R, "Nucleosomes per mammalian cell = 6.6x10^9 bp / 200 bp ~ 3.3x10^7."),
 3: (R, "DNA = genetic material; DNase = enzyme that degrades DNA (-ase marks an enzyme)."),
 4: (R, "Which was the first genetic material? RNA - evidence below."),
 5: (R, "Only one strand is transcribed: (i) both strands would code for different proteins; (ii) two complementary RNAs would pair into dsRNA and block translation."),
 6: (K, "Mnemonic block (I/II/III -> rRNA/mRNA/tRNA) is high-yield; keep."),
 7: (N, "Keep the worked forward example (Met-Phe-Phe-Phe-Phe-Phe-Phe). Reverse case -> NOTE box: the reverse prediction "
        "is ambiguous because Phe is coded by both UUU and UUC - the genetic code is degenerate (5.6). Delete 'Now try the "
        "opposite' / 'Do you face any difficulty' / 'that is the point of the question'."),
 8: (R, "The gene-DNA relationship is best understood through mutation studies (Ch4)."),
 9: (R, "lac operon stays ON only while lactose lasts: lactose is both inducer and substrate of beta-galactosidase; once hydrolysed, the repressor rebinds the operator."),
 10: (R, "Genetic information lies in the DNA base sequence; individual differences reflect sequence differences - the rationale for HGP."),
 11: (R, "HGP - a mega project. Aims:"),
 12: (R, "99.9 per cent of base sequence among humans is the same; with the human genome taken as 3 x 10^9 bp, the "
         "remaining 0.1 per cent is about 3 x 10^6 bp (the figure NCERT itself uses next). These differences in DNA "
         "sequence make every individual unique in phenotypic appearance. (Delete 'in how many base sequences ...?'.)"),
 13: (R, "Sequencing DNA every time to compare individuals would be a daunting and expensive task - imagine comparing two "
         "sets of 3 x 10^6 base pairs -> DNA fingerprinting."),
 14: (D, "Delete the whole 'printing inconsistency' note. Checked against the source: NCERT's 3 x 10^6 is the number of "
         "base pairs that DIFFER (0.1% of 3 x 10^9), not a misprint of the genome size - the note is both Rule 6 "
         "meta-commentary and factually wrong."),
 15: (D, "Recall prompt - checked: contains no fact (points back to Ch4 only). Remove."),
 16: (R, "Variation accumulates in non-coding DNA (no immediate effect on reproduction) -> basis of polymorphism, from single-nucleotide changes to large-scale changes."),
 17: (R, "PCR (Ch9) raised sensitivity - DNA from a single cell suffices. Many probes are now used."),
},
"12/Ch6": {
 0: (M, "Delete the 'Recall:' sentence and the '(NCERT leaves this ... not detailed in this chapter)' remark (Rule 6). "
        "If the method is wanted, MEMORY AID (not in NCERT): radiometric dating - ratio of radioactive parent isotope to "
        "stable daughter isotope + known half-life gives the age of the rock/fossil."),
 1: (R, "Artificial selection argument: man created new breeds within hundreds of years; nature could do the same over millions."),
 2: (R, "Darwin could not explain the origin of variation or speciation; he ignored Mendel's inheritable factors."),
},
"12/Ch7": {
 0: (R, "Biotechnology (Ch10) is yielding newer, safer vaccines."),
 1: (R, "Every day we are exposed to a large number of infectious agents, yet only a few of these exposures result in "
        "disease, because the body is able to defend itself from most of these foreign agents."),
 2: (R, "Food/water-borne diseases in this chapter: typhoid, amoebiasis, ascariasis."),
 3: (D, "Meta-commentary about exercise wording; remove."),
},
"12/Ch8": {
 0: (R, "Microbes are major components of biological systems (Monera, Protista, Fungi - Class XI)."),
 1: (R, "Microbes cause disease (Ch7), but many are useful to humans; key contributions follow."),
 2: (R, "The dough used for making foods such as dosa and idli is also fermented by bacteria; its puffed-up appearance "
        "is due to the production of CO2 gas. Delete the two 'worth answering' questions (their answers are not in this chapter)."),
 3: (R, "Other antibiotics followed penicillin; they treat plague, whooping cough, diphtheria and leprosy. (Delete 'worth naming...' and 'cannot imagine a world...'.)"),
 4: (A, f"'{EX_TITLE}' entry - Q13(a) is a GAP. Reproduce the question in full; answer labelled as an addition: single "
        "cell protein (SCP) is microbial biomass - e.g. Spirulina grown in bulk - used as protein-rich food or animal feed. "
        "Delete 'appears nowhere in this chapter's body' and 'not an NCERT sentence' (Rule 6)."),
 5: (R, "Sewage is rich in organic matter and pathogens, so it is treated in STPs before discharge into water bodies."),
 6: (R, "N2 fixers: symbiotic Rhizobium (legume root nodules); free-living Azospirillum and Azotobacter."),
 7: (A, f"'{EX_TITLE}' entry - Q13(b) is a GAP (the general decomposer role is never stated). Reproduce in full; answer: "
        "N2 fixation (Rhizobium; Azospirillum, Azotobacter), phosphorus via mycorrhiza (Glomus), organic matter and "
        "fertility (cyanobacteria), and - labelled as addition - decomposition of organic matter. Delete 'Assembled only "
        "from facts ...' and 'not stated as such in this chapter's body' (Rule 6)."),
},
"12/Ch9": {
 0: (R, "Alien DNA multiplies in a host only when integrated into its genome (i.e. linked to an origin of replication) - it then replicates with the chromosome."),
},
"12/Ch10": {
 0: (R, "Biotechnology: industrial-scale production of biopharmaceuticals and biologicals using GM microbes, fungi, plants and animals."),
 1: (R, "Bt toxin does not kill Bacillus: it is stored as an inactive protoxin, activated only by the alkaline pH of the insect gut."),
 2: (R, "Management of adult-onset diabetes is possible by taking insulin at regular time intervals. Insulin from other "
        "animals (slaughtered cattle and pigs) can cause allergy or other immune reactions -> human insulin made by rDNA "
        "technology in E. coli (Eli Lilly, 1983). Delete the three rhetorical questions and 'The elegant answer'."),
},
"12/Ch11": {
 0: (R, "Ecology is studied at levels of organisation: organisms -> populations -> communities -> biomes."),
 1: (D, "List of rhetorical 'why' questions - checked: no stated fact. Remove."),
 2: (R, "Ecology: study of interactions of organisms with the abiotic (physico-chemical) and biotic (other species) components of their environment."),
 3: (R, "Four levels: organisms, populations, communities, biomes. Focus here: organism and population levels."),
 4: (R, "Population growth follows predictable patterns (exponential, logistic); natural populations show restraints on growth."),
 5: (R, "A Paramecium starting as one individual and doubling in numbers every day through binary fission would reach "
        "an enormous population in 64 days, provided food and space remain unlimited. (Delete 'Now think of', "
        "'imagine', 'mind-boggling'. No computed figure in body text - Rule 5.)"),
 6: (R, "Life-history traits evolve under the abiotic and biotic constraints of the habitat."),
 7: (R, "No natural habitat has a single species; every species needs at least one other species to feed on."),
 8: (R, "Even autotrophs depend on others: soil microbes (nutrient return) and animal pollinators."),
 9: (R, "Predation transfers energy fixed by plants to higher trophic levels."),
 10: (R, "Predation is not only tiger-deer: a sparrow eating seeds is also a predator."),
 11: (R, "Keep: 'Majority of the parasites harm the host: they may reduce the survival, growth and reproduction of the "
         "host and reduce its population density; they might render the host more vulnerable to predation by making it "
         "physically weak.' Delete 'NCERT asks' and the ideal-parasite questions."),
 12: (R, "Fold into the brood-parasitism sentence: 'the cuckoo (koel) lays its eggs in the nest of the crow; this is "
         "seen during the breeding season (spring to summer).' Delete the neighbourhood-park activity and the mosquito "
         "question. Optional MEMORY AID (not in NCERT): the female mosquito is not a parasite - it feeds briefly and "
         "does not live on or in the host."),
 13: (R, "Mutualisms must guard against 'cheaters' - e.g. nectar thieves that do not pollinate."),
 14: (D, EX_DEL),
},
"12/Ch12": {
 0: (D, "Duplicates the roadmap; merged into row 1's rewrite."),
 1: (R, "User-specified rewrite: 'We will first study the structure of an ecosystem to understand its inputs "
        "(productivity), energy transfer (food chains, food webs, and nutrient cycling), and outputs (degradation and "
        "energy loss). We will also examine the cycles, chains, and webs formed by these energy flows and how they "
        "interact.' Accurate to NCERT; note Rule 3 treats roadmap sentences as transitional - keep at your discretion."),
 2: (R, "Aquatic model - the pond: shallow, self-sustaining, and shows all four basic ecosystem components."),
 3: (R, "All steps of decomposition operate simultaneously on detritus; humification and mineralisation occur in soil."),
 4: (R, "Ecosystems obey both laws of thermodynamics: they need a constant energy input to build molecules and counter increasing disorder."),
 5: (R, "Keep: 'In nature it is possible to have many levels - producer, herbivore, primary carnivore, secondary "
        "carnivore - in the grazing food chain (Figure 12.3).' Delete the detritus-chain prompt."),
 6: (R, "Keep: 'A sparrow is a primary consumer when it eats seeds, fruits, peas, and a secondary consumer when it eats "
        "insects and worms.' Delete the human trophic-level prompt."),
 7: (R, "Pyramid of biomass in the sea is generally inverted because the biomass of fishes far exceeds that of "
        "phytoplankton. (Delete 'Isn't that a paradox? How would you explain this?'.)"),
 8: (D, EX_DEL),
 9: (D, "Restates exercises 7-11, all COVERED by the body - checked: no fact beyond the question text. Remove (Rule 2)."),
},
"12/Ch13": {
 0: (D, "Dangling rhetorical question - checked: no fact. Remove; the Tilman paragraph carries the content."),
 1: (R, "These estimates exclude prokaryotes."),
 2: (R, "Why the tropics are more diverse - three hypotheses:"),
 3: (R, "Whether species richness affects ecosystem function is not settled; Tilman's plots: more species -> less year-to-year variation in total biomass."),
 4: (D, "Rhetorical - checked: no fact; the rivet-popper hypothesis covers it."),
 5: (D, "Rhetorical - checked: no fact."),
 6: (R, "The 'Sixth Extinction' now in progress differs in rate: current species extinction rates are estimated to be "
        "100 to 1,000 times faster than in pre-human times, and human activities are responsible."),
 7: (A, f"'{EX_TITLE}' entry - Q10 is a GAP. Reproduce in full; answer labelled as an addition: a disease-causing "
        "organism, e.g. the smallpox virus (eradicated) or the polio virus - eradication ends human suffering. Delete "
        "'the chapter itself supplies no content ... not examinable as NCERT text' (Rule 6)."),
 8: (R, "The fast-dwindling Amazon forest is estimated to produce, through photosynthesis, 20 per cent of the total "
        "oxygen in the earth's atmosphere. (Delete the economic-value question and the hospital oxygen-cylinder suggestion.)"),
 9: (R, "Pollination by bees, bumblebees, birds and bats is a key ecosystem service; without it plants give no fruits or seeds."),
 10: (R, "Intangible benefits: aesthetic value (woods, flowers, birdsong) - cannot be priced."),
 11: (R, "Rule 3 - summary-only fact moves into the ecosystem-services body section: 'Besides direct benefits (food, "
         "fibre, firewood, pharmaceuticals), biodiversity provides indirect benefits through ecosystem services such as "
         "pollination, pest control, climate moderation and flood control.' The exercise 8 soil-erosion part goes to "
         f"'{EX_TITLE}' as a labelled addition. Delete 'Summary-sourced list' and 'necessary inference, not NCERT text' (Rule 6)."),
},
}

UNITS = [
 ("UNIT 1 - Diversity in the Living World", ["11/Ch1", "11/Ch2", "11/Ch3", "11/Ch4"],
  [f"Delete both exercise preambles (Ch1, Ch2). Exercise content lives only in a '{EX_TITLE}' appendix, and only for GAP questions (Rule 2).",
   "Ch2 answers viruses living/non-living in 2.6a - the Q12 duplicate is deleted outright (a question is answered once).",
   "Delete chapter scope lines / chapter maps (Ch2, Ch3) - they announce coming content (Rule 6). Keep only the facts inside them."]),
 ("UNIT 2 - Structural Organisation in Plants and Animals", ["11/Ch5", "11/Ch6", "11/Ch7"],
  ["Cleanest unit - almost no narrative filler. Only convert question-led openers into statements."]),
 ("UNIT 3 - Cell: Structure and Functions", ["11/Ch8", "11/Ch9", "11/Ch10"],
  ["Delete every 'You will study ... in class XII' sentence; keep the fact that precedes it.",
   "Remove meta-sentences about what NCERT does or does not print ('appears nowhere', 'none is invented here') - Rule 6.",
   "Keep qualifiers exactly: 'Normally', 'frequently observed', 'basic proteins called histones' (Rules 1 and 4).",
   "Ch9 section heading 'How do Enzymes bring about...?' -> declarative heading."]),
 ("UNIT 4 - Plant Physiology", ["11/Ch11", "11/Ch12", "11/Ch13"],
  ["Ch11 end-of-section reader questions: where NCERT gives the answer (C3/C4 anatomy, accessory pigments) -> NOTE box; "
   "where the answer is ours (leaves yellowing in the dark) -> MEMORY AID box; pure activities -> delete.",
   "'Let us now...' openers (ATP synthesis, dark reaction) -> start with the mechanism name.",
   "Ch12 back-references to the chemiosmotic hypothesis -> '(see Ch11)'."]),
 ("UNIT 6 - Reproduction", ["12/Ch1", "12/Ch2", "12/Ch3"],
  ["Lowest fluff density of Class 12. Ch3 MTP 'Why? / When?' bullets are functional Q-A - keep.",
   "No structural changes proposed."]),
 ("UNIT 7 - Genetics and Evolution", ["12/Ch4", "12/Ch5", "12/Ch6"],
  ["Heaviest unit. Ch4 uses 'Let us assume / Let's take' five times in the dominance and polygenic sections - convert each to 'Model:' or 'Example:'.",
   "Ch4 male heterogamety: keep both gamete descriptions (XO: with/without X; XY: X or Y).",
   "Ch5 in-text calculations (DNA length, 99.9% identity) END in NCERT's own result, never in a question.",
   "Ch5 'printing inconsistency' note is wrong - NCERT's 3 x 10^6 is the count of differing bp - delete it.",
   "Ch5 'Recall ... Chapter 4' prompts - delete; keep the fact, add '(Ch4)'.",
   "Ch6 radiometric-dating method is not NCERT text - MEMORY AID or delete, never plain body text (Rule 5)."]),
 ("UNIT 8 - Biology in Human Welfare", ["12/Ch7", "12/Ch8"],
  ["Ch8 opener has two back-reference paragraphs (Class XI kingdoms, Ch7 diseases) - fuse into one line.",
   "Remove emotive closers ('we cannot imagine a world without antibiotics').",
   f"Ch8 SCP (Q13a) and soil microbes (Q13b) are GAPs -> '{EX_TITLE}' appendix, answers labelled as additions.",
   "Ch7: keep 'only a few of these exposures result in disease' - do not invert the qualifier."]),
 ("UNIT 9 - Biotechnology", ["12/Ch9", "12/Ch10"],
  ["Ch10 insulin paragraph: keep the adult-onset diabetes fact; compress the rhetorical chain to one causal line.",
   "Bt toxin Q-and-A -> a single 'because' sentence."]),
 ("UNIT 10 - Ecology", ["12/Ch11", "12/Ch12", "12/Ch13"],
  ["Second-heaviest unit. Ch11 intro is almost entirely philosophy - reduce to definition + levels of organisation.",
   "Ch11-12 NCERT prompts: delete the question, keep every fact around it (binary fission, koel/crow, breeding season, "
   "'generally inverted', 'far exceeds'). Our own answers go in MEMORY AID boxes only.",
   "Ch12 intro: two overlapping roadmap paragraphs -> one (your example rewrite).",
   "Ch13: keep 'estimated' and 'fast-dwindling'; the ecosystem-services block asks 'Can we put a price...?' three times - "
   "convert to a 3-row table: Service | Example | Note.",
   "Ch13 summary-only facts (indirect benefits list) move into the body (Rule 3)."]),
]

HP_SKIP = {"Ch14", "Ch15", "Ch16", "Ch17", "Ch18", "Ch19"}


def shade(cell, hexfill):
    cell._element.get_or_add_tcPr().append(parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hexfill}"/>'))


def run(p, text, bold=False, size=9, color=None, italic=False):
    r = p.add_run(text)
    r.bold, r.italic = bold, italic
    r.font.size = Pt(size)
    if color:
        r.font.color.rgb = RGBColor.from_string(color)
    return r


ACTION_COLOR = {D: "C0392B", R: "1F618D", N: "117A65", M: "B9770E", A: "6C3483", K: "566573"}
ACTION_FILL = {D: "FDEDEC", N: "E8F6F3", M: "FEF5E7", A: "F4ECF7"}


def main():
    hits = json.load(open(HITS))
    allhits = json.load(open(ALL))
    short = {f"{k.split('/')[0].split()[-1]}/{k.split('/')[1].split('_')[0]}": k for k in hits}

    doc = Document()
    sec = doc.sections[0]
    sec.orientation = WD_ORIENT.LANDSCAPE
    sec.page_width, sec.page_height = sec.page_height, sec.page_width
    for m in ("left_margin", "right_margin", "top_margin", "bottom_margin"):
        setattr(sec, m, Inches(0.6))
    doc.styles["Normal"].font.name = "Calibri"
    doc.styles["Normal"].font.size = Pt(10)

    doc.add_heading("NCERT Biology - Deep Fluff Removal & Rewording Proposal (Rev. 2)", 0)
    p = doc.add_paragraph()
    run(p, "Unit-wise, passage-level. Human Physiology (Class 11 Ch14-19) excluded. Every row is a real passage "
           "from the chapter build scripts in notes/, with file:line so it can be edited in place. Revision 2 "
           "aligns every row to the SUPREME COMMAND PROMPT v6 rules.", size=10, italic=True)

    doc.add_heading("Actions", 1)
    for a, desc in [(D, "Remove entirely - checked to contain no NCERT fact (Rule 1: when unsure, keep)."),
                    (R, "Replace with the proposed text - same facts, same qualifier words, no filler."),
                    (N, "Put the fact in a NOTE box (note() in neet_template.py) - the answer is NCERT text."),
                    (M, "Put the fact in a MEMORY AID box (memory_aid(), labelled 'not in NCERT') - the answer is our addition (Rule 5)."),
                    (A, f"Move to the '{EX_TITLE}' appendix - a GAP exercise, reproduced in full, answer labelled as an addition (Rule 2)."),
                    (K, "Flagged by the scanner but functional - leave (or trim as noted).")]:
        q = doc.add_paragraph(style="List Bullet")
        run(q, a + ": ", bold=True, size=10, color=ACTION_COLOR[a]); run(q, desc, size=10)

    doc.add_heading("Global rules applied", 1)
    for rule in ["Every NCERT fact and qualifier survives verbatim ('normally', 'generally', 'estimated', 'far exceeds', 'only a few') - Rules 1 and 4.",
                 "No back-references ('In earlier classes', 'You have studied', 'Recall') - use '(Ch X)' cross-refs.",
                 "No invitations ('Let us', 'Let's', 'We will now look') - start with the subject.",
                 "No rhetorical questions in body text - state NCERT's answer; if the answer is ours, it goes in a MEMORY AID box or nowhere.",
                 "No throat-clearing ('It is important to note', 'It is interesting') - state the fact.",
                 "No meta-commentary about NCERT or the script ('appears nowhere', 'none is invented here', 'this chapter supplies no', chapter maps / scope lines) - Rule 6.",
                 f"Exercises: COVERED questions are deleted; GAP questions go in full into a closing '{EX_TITLE}' appendix. No 'Exercise Support' sections - Rule 2.",
                 "Summary-only facts move into the body - Rule 3.",
                 "No emotive adjectives or closers ('fascinatingly', 'mind-boggling', 'cannot imagine a world').",
                 "Section headings are declarative, never questions.",
                 "Notation: '->', 'x10^9' and '~' in this document are shorthand; in the PDF write proper multiplication signs, superscripts and words."]:
        doc.add_paragraph(rule, style="List Number")

    doc.add_heading("Overview", 1)
    ov = doc.add_table(rows=1, cols=2 + len(ACTIONS)); ov.style = "Light Grid Accent 1"
    for i, t in enumerate(["Unit", "Rows"] + ACTIONS):
        ov.rows[0].cells[i].text = t
    totals = [0] * (1 + len(ACTIONS))
    for name, chs, _ in UNITS:
        c = {a: 0 for a in ACTIONS}
        for s in chs:
            for idx, (a, _) in P.get(s, {}).items():
                c[a] += 1
        vals = [name, sum(c.values())] + [c[a] for a in ACTIONS]
        row = ov.add_row().cells
        for i, v in enumerate(vals):
            row[i].text = str(v)
        for i, v in enumerate(vals[1:]):
            totals[i] += v
    row = ov.add_row().cells
    for i, v in enumerate(["TOTAL"] + totals):
        row[i].text = str(v)
        row[i].paragraphs[0].runs[0].bold = True

    for name, chs, structural in UNITS:
        doc.add_page_break()
        doc.add_heading(name, 1)
        doc.add_heading("Structural recommendations", 3)
        for s in structural:
            doc.add_paragraph(s, style="List Bullet")
        for s in chs:
            full = short.get(s)
            if not full:
                continue
            items = hits[full]
            weak = len(allhits.get(full, [])) - len(items)
            doc.add_heading(full.split("/")[1].replace("_", " - ", 1), 2)
            pth = glob.glob(os.path.join(ROOT, "notes", full.split("/")[0], full.split("/")[1], "*.py"))
            pth = [x for x in pth if "extract" not in x]
            rel = os.path.relpath(pth[0], ROOT) if pth else ""
            meta = doc.add_paragraph()
            run(meta, f"{rel}  |  {len(items)} passages  |  +{weak} minor wording hits (various, rather, basically...) for a light sweep",
                size=8, italic=True, color="566573")
            if not items:
                run(doc.add_paragraph(), "No narrative filler found - no action needed.", size=9, italic=True)
                continue
            tbl = doc.add_table(rows=1, cols=5); tbl.style = "Table Grid"
            widths = [Inches(0.55), Inches(3.9), Inches(1.0), Inches(0.9), Inches(3.9)]
            for i, t in enumerate(["Line", "Original", "Fluff type", "Action", "Proposed"]):
                c = tbl.rows[0].cells[i]; c.text = ""; run(c.paragraphs[0], t, bold=True, size=9, color="FFFFFF")
                shade(c, "1C2833"); c.width = widths[i]
            for idx, x in enumerate(items):
                a, prop = P.get(s, {}).get(idx, (K, "Review manually."))
                cells = tbl.add_row().cells
                run(cells[0].paragraphs[0], str(x["line"]), size=8)
                run(cells[1].paragraphs[0], x["text"], size=8, italic=True, color="424949")
                run(cells[2].paragraphs[0], ", ".join(x["tags"]), size=8)
                run(cells[3].paragraphs[0], a, bold=True, size=8, color=ACTION_COLOR[a])
                run(cells[4].paragraphs[0], prop, size=8)
                if a in ACTION_FILL:
                    shade(cells[4], ACTION_FILL[a])
                for i, c in enumerate(cells):
                    c.width = widths[i]

    out = os.path.join(ROOT, "NCERT_Biology_Fluff_Removal_Proposal_DEEP.docx")
    doc.save(out)
    print("saved", out)


if __name__ == "__main__":
    main()
