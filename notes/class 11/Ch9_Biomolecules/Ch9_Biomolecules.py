#!/usr/bin/env python3
"""
Class 11 Chapter 9 - Biomolecules  ->  NEET replacement notes.

Built per SUPREME COMMAND PROMPT.md v6, normal-chapter 3-pass protocol.
Every style, colour, font and layout helper is imported from the repo-level
neet_template.py; nothing visual is re-declared here (v6 s0.6).

Content source of truth: Ch9_Biomolecules_inventory.md
(frozen 2026-08-20, F001-F277 facts + L01-L15 figure-label rows). This script
is one linear story.append(...) sequence with `# ---- N.N ----` markers so a
Pass 3 fix stays surgical.

Figures: the 15 verified monochrome assets in assets/ only (Figure 9.1 split
six ways, 9.3 four ways, 9.5 three ways, 9.2 and 9.4 whole). This chapter has
no scientist profile box and no photograph of any person, so v6 s4.4's hard no
and s5 item 3 are both satisfied trivially - the only named person, CNR Rao, is
a bibliographic credit on Table 9.1 (F255), not a portrait.

Notation: chemical formulae are written in plain ASCII with digits on the line
("CO2", "H2CO3", "C6H12O6", "PO4 3-", "Ca++"), and Greek letters as the spelled
words "alpha"/"beta" - v6 s4 bans Unicode sub/superscript and Greek codepoints,
and Times subscript tags render below the linter's legibility floor inside table
cells. The three summary-unique wordings the body states differently (oxygen in
F267, nitrogenous in F271, "only three macromolecules" in F272) are BOTH carried
per Rule 4; neither is silently harmonised.

Source problems handled inline (see inventory Source problems): the "section
9.10" forward-reference in F073 is dropped rather than repointed; NCERT's typos
"the the" (F244), "cordination" (F252), "physiologial" (F076) are normalised in
the rewritten body only; the unnumbered A/B/C zwitterion scheme (F044) is carried
as words since it is not an extractable numbered figure.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))

from reportlab.platypus import Spacer, Paragraph, KeepTogether  # noqa: E402
from reportlab.lib.units import cm  # noqa: E402

from neet_template import (  # noqa: E402
    STYLES,
    heading, keyterm, process_flow, note, memory_aid, data_table, title_block, build_pdf,
)
from neet_template import figure as _shared_figure  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "assets")
OUT_PDF = os.path.join(HERE, "Ch9_Biomolecules.pdf")


def figure(asset_name, caption_text, max_width_cm=15.9):
    return _shared_figure(asset_name, caption_text, ASSETS, max_width_cm=max_width_cm)


def P(text, style="Body"):
    return Paragraph(text, STYLES[style])


def B(text, level=1):
    return Paragraph(text, STYLES[f"Bullet{level}"])


def H(number, text, level, follow, has_table=False):
    """Heading kept together with the flowable that follows it (v6 s4 tech rules)."""
    return KeepTogether([heading(number, text, level, has_table=has_table), follow])


def labels_line(labels):
    """Reproduce the in-figure labels verbatim beneath a figure.

    v6 s4.4 requires every in-figure label catalogued in the inventory (L01-L15)
    to appear in the running text, so a reader working from a bad photocopy of the
    diagram can still name every part. NCERT's own spelling of each label is
    preserved exactly - including the secondary-structure labels "Alpha- Helix"
    (space after the hyphen) and "Beta-pleated sheet" (no space), whose source
    en-dashes are rendered as ASCII hyphens per s4 (see inventory spelling note).
    """
    return P("<i>Labels printed in the figure:</i> " + "; ".join(labels))


story = []

# ---- Title block ----
story.extend(title_block("Biomolecules"))
story.append(P("<i>Class 11 - Chapter 9 - NEET replacement notes built from the NCERT chapter "
               "text, its 5 figures (15 panels), its 5 tables, its summary and its 11 "
               "exercises.</i>"))
story.append(Spacer(1, 0.18 * cm))

# ---- Chapter opener ---- (F001-F007, summary-unique F265, F266, F267 folded here)
story.append(P("There is a wide diversity in living organisms in our biosphere. Are all living "
               "organisms made of the same chemicals, i.e., elements and compounds? "
               "<b>Although there is a bewildering diversity of living organisms, their chemical "
               "composition and metabolic reactions appear to be remarkably similar.</b>"))
story.append(P("If we perform a chemical analysis on a plant tissue, animal tissue or a microbial "
               "paste, we obtain a list of elements like carbon, hydrogen, oxygen and several "
               "others, and their respective content per unit mass of a living tissue. If the same "
               "analysis is performed on a piece of earth's crust as an example of non-living "
               "matter, we obtain a similar list. In absolute terms, no such differences could be "
               "made out; <b>the elemental composition of living tissues and non-living matter "
               "appear also to be similar when analysed qualitatively.</b>"))
story.append(P("All the elements present in a sample of earth's crust are also present in a sample "
               "of living tissue. However, a closer examination reveals that <b>the relative "
               "abundance of carbon and hydrogen with respect to other elements is higher in any "
               "living organism than in earth's crust</b> - and taking the summary's fuller list, "
               "the relative abundance of <b>carbon, hydrogen and oxygen</b> is higher in living "
               "systems when compared to inanimate matter."))
story.append(data_table([
    ["Element", "% Weight of Earth's crust", "% Weight of Human body"],
    ["Hydrogen (H)", "0.14", "9.5"],
    ["Carbon (C)", "0.03", "18.5"],
    ["Oxygen (O)", "46.6", "65.0"],
    ["Nitrogen (N)", "very little", "3.3"],
    ["Sulphur (S)", "0.03", "0.3"],
    ["Sodium (Na)", "2.8", "0.2"],
    ["Calcium (Ca)", "3.6", "1.5"],
    ["Magnesium (Mg)", "2.1", "0.1"],
    ["Silicon (Si)", "27.7", "negligible"],
], col_widths=[2.2, 2.4, 2.4]))
story.append(P("<i>Table 9.1 - A Comparison of Elements Present in Non-living and Living Matter. "
               "Adapted from CNR Rao, Understanding Chemistry, Universities Press, Hyderabad.</i>"))

# ---- 9.1 How to Analyse Chemical Composition? ---- (F008-F071)
story.append(H("9.1", "How to Analyse Chemical Composition?", 1,
               P("We wish to know what type of organic compounds are found in living organisms. "
                 "How does one go about finding the answer? To get an answer, one has to perform a "
                 "chemical analysis.")))
story.append(P("We can take any living tissue (a vegetable or a piece of liver, etc.) and grind it "
               "in trichloroacetic acid (Cl3CCOOH) using a mortar and a pestle. We obtain a thick "
               "slurry. If we were to strain this through a cheesecloth or cotton we would obtain "
               "two fractions."))
story.append(keyterm("One is called the <b>filtrate</b> or, more technically, the <b>acid-soluble "
                     "pool</b>, and the second, the <b>retentate</b> or the <b>acid-insoluble "
                     "fraction</b>. Scientists have found thousands of organic compounds in the "
                     "acid-soluble pool."))
story.append(P("To identify a compound, one extracts the compounds, then subjects the extract to "
               "various separation techniques till one has separated a compound from all other "
               "compounds. In other words, one isolates and purifies a compound. Analytical "
               "techniques, when applied to the compound, give us an idea of the molecular formula "
               "and the probable structure of the compound."))
story.append(keyterm("All the carbon compounds that we get from living tissues can be called "
                     "<b>biomolecules</b>. However, living organisms have also got inorganic "
                     "elements and compounds in them."))
story.append(P("<b>Finding the inorganic constituents.</b> A slightly different but destructive "
               "experiment has to be done. One weighs a small amount of a living tissue (say a leaf "
               "or liver - this is called <b>wet weight</b>) and dries it. All the water "
               "evaporates; the remaining material gives the <b>dry weight</b>. Now if the tissue "
               "is fully burnt, all the carbon compounds are oxidised to gaseous form (CO2, water "
               "vapour) and are removed. What is remaining is called <b>'ash'</b>."))
story.append(P("This ash contains inorganic elements (like calcium, magnesium etc). Inorganic "
               "compounds like sulphate, phosphate, etc., are also seen in the acid-soluble "
               "fraction. Therefore elemental analysis gives elemental composition of living "
               "tissues in the form of hydrogen, oxygen, chlorine, carbon etc. while analysis for "
               "compounds gives an idea of the kind of organic (Figure 9.1) and inorganic (Table "
               "9.2) constituents present in living tissues."))
story.append(data_table([
    ["Component", "Formula"],
    ["Sodium", "Na+"],
    ["Potassium", "K+"],
    ["Calcium", "Ca++"],
    ["Magnesium", "Mg++"],
    ["Water", "H2O"],
    ["Compounds", "NaCl, CaCO3, PO4 3-, SO4 2-"],
], col_widths=[2.2, 4.0]))
story.append(P("<i>Table 9.2 - A List of Representative Inorganic Constituents of Living "
               "Tissues.</i>"))
story.append(P("From a chemistry point of view, one can identify functional groups like aldehydes, "
               "ketones, aromatic compounds, etc. But from a biological point of view, we shall "
               "classify them into amino acids, nucleotide bases, fatty acids etc."))

# ---- 9.1 Amino acids ---- (F030-F044) + Fig 9.1 (b)
story.append(H("9.1", "Amino Acids", 2,
               keyterm("<b>Amino acids</b> are organic compounds containing an amino group and an "
                       "acidic group as substituents on the same carbon, i.e., the alpha-carbon. "
                       "Hence, they are called <b>alpha-amino acids</b>.")))
story.append(P("They are substituted methanes. There are <b>four</b> substituent groups occupying "
               "the four valency positions: these are hydrogen, carboxyl group, amino group and a "
               "variable group designated as <b>R group</b>. Based on the nature of the R group "
               "there are many amino acids."))
story.append(P("However, those which occur in proteins are only of <b>twenty types</b>. The R group "
               "in these proteinaceous amino acids could be a hydrogen (the amino acid is called "
               "<b>glycine</b>), a methyl group (<b>alanine</b>), hydroxy methyl (<b>serine</b>), "
               "etc. Three of the twenty are shown in Figure 9.1."))
story.append(P("The chemical and physical properties of amino acids are essentially of the amino, "
               "carboxyl and the R functional groups. Based on the number of amino and carboxyl "
               "groups, there are <b>acidic</b> (e.g., glutamic acid), <b>basic</b> (lysine) and "
               "<b>neutral</b> (valine) amino acids. Similarly, there are <b>aromatic</b> amino "
               "acids (tyrosine, phenylalanine, tryptophan)."))
story.append(P("A particular property of amino acids is the ionizable nature of the -NH2 and -COOH "
               "groups. Hence in solutions of different pH, the structure of amino acids changes: "
               "in the intermediate protonation state (structure B of the inline scheme), both "
               "groups are ionised and the molecule is a dipolar ion - this is called the "
               "<b>zwitterionic form</b>."))
story.append(figure("fig_9_1b.png",
                    "Fig. 9.1 (b) - Amino acids: three of the twenty proteinaceous amino acids "
                    "(glycine, alanine, serine), each an alpha-amino acid built on a substituted "
                    "methane.", max_width_cm=9.0))
story.append(labels_line(["Amino acids", "Glycine", "Alanine", "Serine"]))
story.append(figure("fig_9_1a.png",
                    "Fig. 9.1 (a) - Sugars (carbohydrates): glucose (C6H12O6) and ribose "
                    "(C5H10O5), the small-molecular-weight sugars of living tissue.",
                    max_width_cm=9.0))
story.append(labels_line(["Sugars (Carbohydrates)", "Glucose", "Ribose"]))

# ---- 9.1 Lipids ---- (F045-F063, summary-unique F271) + Fig 9.1 (c)
story.append(H("9.1", "Lipids", 2,
               P("<b>Lipids</b> are generally water insoluble. They could be simple fatty acids. A "
                 "<b>fatty acid</b> has a carboxyl group attached to an R group.")))
story.append(P("The R group could be a methyl (-CH3), or ethyl (-C2H5) or a higher number of -CH2 "
               "groups (1 carbon to 19 carbons). For example, <b>palmitic acid</b> has 16 carbons "
               "including the carboxyl carbon; <b>arachidonic acid</b> has 20 carbon atoms "
               "including the carboxyl carbon. Fatty acids could be <b>saturated</b> (without "
               "double bond) or <b>unsaturated</b> (with one or more C=C double bonds)."))
story.append(P("Another simple lipid is <b>glycerol</b> which is trihydroxy propane. Many lipids "
               "have both glycerol and fatty acids; here the fatty acids are found <b>esterified</b> "
               "with glycerol. They can then be <b>monoglycerides, diglycerides and "
               "triglycerides</b>. These are also called <b>fats and oils</b> based on melting "
               "point. Oils have lower melting point (e.g., gingelly oil) and hence remain as oil "
               "in winters. Can you identify a fat from the market?"))
story.append(P("Some lipids have phosphorous and a phosphorylated organic compound in them. These "
               "are <b>phospholipids</b>. They are found in cell membrane; <b>lecithin</b> is one "
               "example. Some tissues, especially the neural tissues, have lipids with more complex "
               "structures."))
# [VERIFICATION FIX] summary-unique F271 was ticked but never written into the body; folded in here.
story.append(P("As the summary states it, <b>phospholipids</b> contain, in addition, a "
               "<b>phosphorylated nitrogenous compound</b>."))
story.append(figure("fig_9_1c.png",
                    "Fig. 9.1 (c) - Fats and oils (lipids): a fatty acid (palmitic acid), "
                    "glycerol, a triglyceride (R1, R2, R3 are fatty acids), a phospholipid "
                    "(lecithin) and cholesterol.", max_width_cm=9.5))
story.append(labels_line(["Fats and oils (lipids)", "Fatty acid", "Palmitic acid", "Glycerol",
                          "Triglyceride", "are fatty acids", "Phospholipid (Lecithin)",
                          "Cholesterol"]))

# ---- 9.1 Nitrogen bases, nucleosides, nucleotides ---- (F064-F071) + Fig 9.1 (d,e,f)
story.append(H("9.1", "Nitrogen Bases, Nucleosides and Nucleotides", 2,
               P("Living organisms have a number of carbon compounds in which <b>heterocyclic "
                 "rings</b> can be found. Some of these are nitrogen bases - <b>adenine, guanine, "
                 "cytosine, uracil, and thymine</b>.")))
story.append(keyterm("When found attached to a sugar, they are called <b>nucleosides</b>. If a "
                     "phosphate group is also found esterified to the sugar they are called "
                     "<b>nucleotides</b>."))
story.append(P("<b>Adenosine, guanosine, thymidine, uridine and cytidine</b> are nucleosides. "
               "<b>Adenylic acid, thymidylic acid, guanylic acid, uridylic acid and cytidylic "
               "acid</b> are nucleotides. Nucleic acids like DNA and RNA consist of nucleotides "
               "only. DNA and RNA function as <b>genetic material</b>."))
story.append(figure("fig_9_1d.png",
                    "Fig. 9.1 (d) - Nitrogen bases: adenine (a purine) and uracil (a "
                    "pyrimidine).", max_width_cm=8.0))
story.append(labels_line(["Nitrogen bases", "Adenine (Purine)", "Uracil (Pyrimidine)"]))
story.append(figure("fig_9_1e.png",
                    "Fig. 9.1 (e) - Nucleosides: a base attached to a sugar - adenine gives "
                    "adenosine, uracil gives uridine.", max_width_cm=8.5))
story.append(labels_line(["Nucleosides", "Adenine", "Adenosine", "Uracil", "Uridine"]))
story.append(figure("fig_9_1f.png",
                    "Fig. 9.1 (f) - Nucleotide: a base and sugar with a phosphate esterified to "
                    "the sugar - adenine gives adenylic acid.", max_width_cm=8.0))
story.append(labels_line(["Nucleotide", "Adenine", "Adenylic acid"]))
story.append(P("<i>Figure 9.1 - Diagrammatic representation of small molecular weight organic "
               "compounds in living tissues.</i>"))
# [VERIFICATION FIX] summary-unique F269 was ticked but never written into the body; folded in here.
story.append(P("As the summary catalogues them, <b>amino acids, monosaccharide and disaccharide "
               "sugars, fatty acids, glycerol, nucleotides, nucleosides and nitrogen bases</b> are "
               "some of the organic compounds seen in living organisms."))

# ---- 9.2 Primary and Secondary Metabolites ---- (F072-F078)
story.append(H("9.2", "Primary and Secondary Metabolites", 1,
               P("The most exciting aspect of chemistry deals with isolating thousands of "
                 "compounds, small and big, from living organisms, determining their structure and "
                 "if possible synthesising them.")))
story.append(keyterm("If one were to make a list of biomolecules, such a list would have thousands "
                     "of organic compounds including amino acids, sugars, etc. We can call these "
                     "biomolecules <b>'metabolites'</b>."))
story.append(P("In animal tissues, one notices the presence of all such categories of compounds "
               "shown in Figure 9.1. These are <b>primary metabolites</b>. However, when one "
               "analyses plant, fungal and microbial cells, one would see thousands of compounds "
               "other than these primary metabolites - e.g. alkaloids, flavonoids, rubber, "
               "essential oils, antibiotics, coloured pigments, scents, gums, spices. These are "
               "called <b>secondary metabolites</b>."))
story.append(P("While primary metabolites have identifiable functions and play known roles in "
               "normal physiological processes, we do not, at the moment, understand the role or "
               "functions of all the secondary metabolites in host organisms. However, many of "
               "them are useful to <b>human welfare</b> (e.g., rubber, drugs, spices, scents and "
               "pigments). Some secondary metabolites have <b>ecological importance</b>."))
story.append(data_table([
    ["Class of secondary metabolite", "Examples"],
    ["Pigments", "Carotenoids, Anthocyanins, etc."],
    ["Alkaloids", "Morphine, Codeine, etc."],
    ["Terpenoides", "Monoterpenes, Diterpenes, etc."],
    ["Essential oils", "Lemon grass oil, etc."],
    ["Toxins", "Abrin, Ricin"],
    ["Lectins", "Concanavalin A"],
    ["Drugs", "Vinblastin, curcumin, etc."],
    ["Polymeric substances", "Rubber, gums, cellulose"],
], col_widths=[2.8, 4.0]))
story.append(P("<i>Table 9.3 - Some Secondary Metabolites.</i>"))

# ---- 9.3 Biomacromolecules ---- (F079-F093, summary-unique F268, F272)
story.append(H("9.3", "Biomacromolecules", 1,
               P("There is one feature common to all those compounds found in the acid-soluble "
                 "pool: they have molecular weights ranging from <b>18 to around 800 daltons "
                 "(Da)</b> approximately. The acid-insoluble fraction has only <b>four</b> types "
                 "of organic compounds, i.e., proteins, nucleic acids, polysaccharides and "
                 "lipids.")))
story.append(P("These classes of compounds - with the exception of lipids - have molecular weights "
               "in the range of <b>ten thousand daltons and above</b>. This is the basis of the "
               "acid-soluble/acid-insoluble divide:"))
story.append(keyterm("Those which have molecular weights <b>less than one thousand daltons</b> are "
                     "usually referred to as <b>micromolecules</b> or simply biomolecules, while "
                     "those found in the acid-insoluble fraction are called <b>macromolecules</b> "
                     "or biomacromolecules. (The summary notes there are thousands of such small "
                     "molecular weight, under 1000 Da, biomolecules.)"))
story.append(P("The molecules in the insoluble fraction, with the exception of lipids, are "
               "<b>polymeric substances</b>. Then why do lipids, whose molecular weights do not "
               "exceed 800 Da, come under the acid-insoluble (macromolecular) fraction?"))
story.append(note("Lipids are indeed small molecular weight compounds and are present not only as "
                  "such but also arranged into structures like cell membrane and other membranes. "
                  "When we grind a tissue, we disrupt the cell structure: cell membrane and other "
                  "membranes are broken into pieces and form vesicles which are not water soluble. "
                  "Therefore these membrane fragments, in the form of vesicles, get separated along "
                  "with the acid-insoluble pool and hence appear in the macromolecular fraction. "
                  "For this reason lipids are not strictly macromolecules - which is why the "
                  "chapter summary counts <b>only three</b> true macromolecules (proteins, nucleic "
                  "acids and polysaccharides) even though the acid-insoluble fraction holds four "
                  "classes of organic compound."))
story.append(P("The <b>acid-soluble pool</b> represents roughly the cytoplasmic composition. The "
               "macromolecules from cytoplasm and organelles become the <b>acid-insoluble "
               "fraction</b>. Together they represent the entire chemical composition of living "
               "tissues or organisms. In summary, if we represent the chemical composition of "
               "living tissue from an abundance point of view and arrange them class-wise, we "
               "observe that <b>water is the most abundant chemical in living organisms</b>."))
story.append(data_table([
    ["Component", "% of the total cellular mass"],
    ["Water", "70-90"],
    ["Proteins", "10-15"],
    ["Carbohydrates", "3"],
    ["Lipids", "2"],
    ["Nucleic acids", "5-7"],
    ["Ions", "1"],
], col_widths=[3.0, 3.8]))
story.append(P("<i>Table 9.4 - Average Composition of Cells.</i>"))

# ---- 9.4 Proteins ---- (F094-F105, summary-unique F275) + Table 9.5
story.append(H("9.4", "Proteins", 1,
               keyterm("<b>Proteins</b> are polypeptides. They are linear chains of amino acids "
                       "linked by <b>peptide bonds</b> as shown in Figure 9.3. Each protein is a "
                       "polymer of amino acids.")))
story.append(P("As there are 20 types of amino acids (e.g., alanine, cysteine, proline, "
               "tryptophan, lysine, etc.), a protein is a <b>heteropolymer</b> and not a "
               "homopolymer. A <b>homopolymer</b> has only one type of monomer repeating 'n' "
               "number of times."))
story.append(keyterm("Certain amino acids are <b>essential</b> for our health and they have to be "
                     "supplied through our diet. Hence, dietary proteins are the source of "
                     "essential amino acids. Amino acids can be essential or non-essential: the "
                     "<b>non-essential</b> ones are those which our body can make, while we get "
                     "<b>essential</b> amino acids through our diet/food."))
story.append(P("Proteins carry out many functions in living organisms: some transport nutrients "
               "across the cell membrane, some fight infectious organisms, some are hormones, some "
               "are enzymes, etc. As the summary puts it, many of them are enzymes, some are "
               "antibodies, some are receptors, some are hormones and some others are "
               "<b>structural proteins</b>."))
story.append(P("<b>Collagen</b> is the most abundant protein in the animal world, and <b>Ribulose "
               "bisphosphate Carboxylase-Oxygenase (RuBisCO)</b> is the most abundant protein in "
               "the whole of the biosphere."))
story.append(data_table([
    ["Protein", "Functions"],
    ["Collagen", "Intercellular ground substance"],
    ["Trypsin", "Enzyme"],
    ["Insulin", "Hormone"],
    ["Antibody", "Fights infectious agents"],
    ["Receptor", "Sensory reception (smell, taste, hormone, etc.)"],
    ["GLUT-4", "Enables glucose transport into cells"],
], col_widths=[1.8, 5.0]))
story.append(P("<i>Table 9.5 - Some Proteins and their Functions.</i>"))

# ---- 9.5 Polysaccharides ---- (F106-F125, summary-unique F274) + Fig 9.2
story.append(H("9.5", "Polysaccharides", 1,
               P("The acid-insoluble pellet also has <b>polysaccharides</b> (carbohydrates) as "
                 "another class of macromolecules. Polysaccharides are long chains of sugars - "
                 "they are threads (literally a cotton thread) containing different "
                 "monosaccharides as building blocks.")))
story.append(P("For example, <b>cellulose</b> is a polymeric polysaccharide consisting of only one "
               "type of monosaccharide, i.e., glucose; cellulose is a <b>homopolymer</b>. "
               "<b>Starch</b> is a variant of this but present as a store house of energy in plant "
               "tissues. Animals have another variant called <b>glycogen</b>. <b>Inulin</b> is a "
               "polymer of fructose."))
story.append(keyterm("In a polysaccharide chain (say glycogen), the right end is called the "
                     "<b>reducing end</b> and the left end is called the <b>non-reducing end</b>. "
                     "It has branches, as shown in the form of a cartoon (Figure 9.2)."))
story.append(figure("fig_9_2.png",
                    "Fig. 9.2 - Diagrammatic representation of a portion of glycogen, a branched "
                    "polysaccharide, showing its reducing and non-reducing ends.",
                    max_width_cm=12.0))
story.append(labels_line(["glycogen"]))
story.append(P("<b>Starch, iodine and cellulose.</b> Starch forms <b>helical</b> secondary "
               "structures. In fact, starch can hold I2 molecules in the helical portion; the "
               "starch-I2 is <b>blue</b> in colour. Cellulose does not contain complex helices and "
               "hence cannot hold I2."))
story.append(P("Plant cell walls are made of cellulose. Paper made from plant pulp and cotton "
               "fibre is cellulosic. There are more complex polysaccharides in nature: they have "
               "as building blocks amino-sugars and chemically modified sugars (e.g., glucosamine, "
               "N-acetyl galactosamine, etc.). Exoskeletons of arthropods, for example, have a "
               "complex polysaccharide called <b>chitin</b>. These complex polysaccharides are "
               "mostly homopolymers."))
story.append(note("The summary generalises this section: polysaccharides are components of the "
                  "<b>cell wall in plants, fungi</b> and also of the <b>exoskeleton of "
                  "arthropods</b>, and they are storage forms of energy (e.g., starch and "
                  "glycogen). The body names plant cell walls and arthropod exoskeletons directly; "
                  "the mention of <b>fungi</b> comes from the summary."))

# ---- 9.6 Nucleic Acids ---- (F126-F135, summary-unique F270, F277)
story.append(H("9.6", "Nucleic Acids", 1,
               P("The other type of macromolecule that one would find in the acid-insoluble "
                 "fraction of any living tissue is the <b>nucleic acid</b>. These are "
                 "<b>polynucleotides</b>. Together with polysaccharides and polypeptides these "
                 "comprise the true macromolecular fraction of any living tissue or cell.")))
story.append(keyterm("For nucleic acids, the building block is a <b>nucleotide</b>. A nucleotide "
                     "has three chemically distinct components: one is a <b>heterocyclic "
                     "compound</b>, the second is a <b>monosaccharide</b> and the third a "
                     "<b>phosphoric acid or phosphate</b>."))
story.append(P("As you notice in Figure 9.1, the heterocyclic compounds in nucleic acids are the "
               "nitrogenous bases named <b>adenine, guanine, uracil, cytosine, and thymine</b>. "
               "Adenine and Guanine are substituted <b>purines</b> while the rest are substituted "
               "<b>pyrimidines</b>. The skeletal heterocyclic ring is called purine and pyrimidine "
               "respectively."))
story.append(P("The sugar found in polynucleotides is either <b>ribose</b> (a monosaccharide "
               "pentose) or <b>2' deoxyribose</b>. A nucleic acid containing deoxyribose is called "
               "<b>deoxyribonucleic acid (DNA)</b> while that which contains ribose is called "
               "<b>ribonucleic acid (RNA)</b>."))
# [VERIFICATION FIX] summary-unique F270 was ticked but never written into the body; folded in here.
story.append(P("The summary fixes the counts: there are <b>20 types of amino acids</b> and "
               "<b>5 types of nucleotides</b>."))
story.append(note("Nucleic acids serve as genetic material: DNA and RNA carry <b>hereditary "
                  "information</b> and are passed on from the parental generation to the progeny "
                  "(the parent-to-progeny transmission clause is stated in the summary; the body "
                  "states that DNA and RNA function as genetic material)."))

# ---- 9.7 Structure of Proteins ---- (F136-F157, summary-unique F273) + Fig 9.3
story.append(H("9.7", "Structure of Proteins", 1,
               P("Proteins, as mentioned earlier, are heteropolymers containing strings of amino "
                 "acids. Structure of molecules means different things in different contexts.")))
story.append(P("In inorganic chemistry, the structure invariably refers to the molecular formulae "
               "(e.g., NaCl, MgCl2, etc.). Organic chemists always write a two-dimensional view of "
               "the molecules while representing their structure (e.g., benzene, naphthalene, "
               "etc.). Physicists conjure up the three-dimensional views of molecular structures, "
               "while biologists describe the protein structure at <b>four levels</b>."))
story.append(keyterm("The sequence of amino acids - i.e., the positional information in a protein, "
                     "which is the first amino acid, which is second, and so on - is called the "
                     "<b>primary structure</b> (Figure 9.3 a) of a protein."))
story.append(P("A protein is imagined as a line, the left end represented by the first amino acid "
               "and the right end represented by the last amino acid. The first amino acid is also "
               "called the <b>N-terminal amino acid</b>; the last amino acid is called the "
               "<b>C-terminal amino acid</b>."))
story.append(figure("fig_9_3a.png",
                    "Fig. 9.3 (a) - Primary structure: a polypeptide, the linear sequence of "
                    "amino acids from the N-terminal to the C-terminal end.", max_width_cm=9.0))
story.append(labels_line(["Primary", "Polypeptide"]))
story.append(P("A protein thread does not exist throughout as an extended rigid rod. The thread is "
               "folded in the form of a <b>helix</b> (similar to a revolving staircase). Of "
               "course, only some portions of the protein thread are arranged in the form of a "
               "helix; in proteins, only <b>right-handed helices</b> are observed. Other regions "
               "of the protein thread are folded into other forms in what is called the "
               "<b>secondary structure</b> (Fig. 9.3 b)."))
story.append(figure("fig_9_3b.png",
                    "Fig. 9.3 (b) - Secondary structure: regions folded as the right-handed "
                    "alpha-helix and the beta-pleated sheet.", max_width_cm=9.0))
story.append(labels_line(["Secondary", "Alpha- Helix", "Beta-pleated sheet"]))
story.append(P("In addition, the long protein chain is also folded upon itself like a hollow "
               "woollen ball, giving rise to the <b>tertiary structure</b> (Fig. 9.3 c). This "
               "gives us a 3-dimensional view of a protein. Tertiary structure is absolutely "
               "necessary for the many biological activities of proteins."))
story.append(figure("fig_9_3c.png",
                    "Fig. 9.3 (c) - Tertiary structure: the whole chain folded upon itself into a "
                    "3-D shape, held by hydrogen bonds and disulphide bonds.", max_width_cm=9.0))
story.append(labels_line(["Tertiary", "Hydrogen bond", "Disulphide bond"]))
story.append(P("Some proteins are an assembly of more than one polypeptide or subunits. The manner "
               "in which these individual folded polypeptides or subunits are arranged with "
               "respect to each other (e.g. a linear string of spheres, or spheres arranged one "
               "upon each other in the form of a cube or plate, etc.) is the architecture of a "
               "protein, otherwise called the <b>quaternary structure</b> (Fig. 9.3 d)."))
story.append(figure("fig_9_3d.png",
                    "Fig. 9.3 (d) - Quaternary structure: the arrangement of several folded "
                    "subunits with respect to one another.", max_width_cm=9.0))
story.append(labels_line(["Quaternary"]))
story.append(P("<i>Figure 9.3 - Various levels of Protein Structure.</i>"))
story.append(P("<b>Adult human haemoglobin</b> consists of 4 subunits. Two of these are identical "
               "to each other. Hence, two subunits of <b>alpha</b> type and two subunits of "
               "<b>beta</b> type together constitute the human haemoglobin (Hb)."))
story.append(memory_aid("Four levels of protein structure - <b>Primary</b> = sequence (which amino "
                        "acid is first, second, ...); <b>Secondary</b> = right-handed alpha-helix "
                        "and beta-pleated sheet; <b>Tertiary</b> = whole chain folded like a "
                        "woollen ball (needed for biological activity); <b>Quaternary</b> = "
                        "several subunits assembled together (e.g. haemoglobin's 2 alpha + 2 "
                        "beta). The summary generalises this hierarchy - primary, secondary, "
                        "tertiary and quaternary - to all biomacromolecules."))

# ---- 9.8 Enzymes ---- (F158-F170)
story.append(H("9.8", "Enzymes", 1,
               keyterm("Almost all <b>enzymes</b> are proteins. There are some nucleic acids that "
                       "behave like enzymes; these are called <b>ribozymes</b>.")))
story.append(P("One can depict an enzyme by a line diagram. An enzyme, like any protein, has a "
               "<b>primary structure</b> (amino acid sequence) and also the <b>secondary</b> and "
               "the <b>tertiary structure</b>. When you look at a tertiary structure upon itself, "
               "the chain criss-crosses itself and hence many crevices or pockets are made."))
story.append(keyterm("One such pocket is the <b>'active site'</b>. An active site of an enzyme is a "
                     "crevice or pocket into which the substrate fits. Thus enzymes, through their "
                     "active site, catalyse reactions at a high rate."))
story.append(P("Enzyme catalysts differ from inorganic catalysts in many ways, but one major "
               "difference needs mention: inorganic catalysts work efficiently at high "
               "temperatures and high pressures, while enzymes get damaged at high temperatures "
               "(say above 40 degrees C). However, enzymes isolated from organisms who normally "
               "live under extremely high temperatures (e.g., hot vents and sulphur springs) are "
               "stable and retain their catalytic power even at high temperatures (up to 80-90 "
               "degrees C). <b>Thermal stability</b> is thus an important quality of such enzymes "
               "isolated from <b>thermophilic</b> organisms."))

# ---- 9.8.1 Chemical Reactions ---- (F171-F194)
story.append(H("9.8.1", "Chemical Reactions", 2,
               P("Chemical compounds undergo two types of changes. A <b>physical change</b> simply "
                 "refers to a change in shape without breaking of bonds - this is a physical "
                 "process. Another physical process is a change in the state of matter: when ice "
                 "melts into water, or when water becomes vapour.")))
story.append(keyterm("However, when bonds are broken and new bonds are formed during "
                     "transformation, this is called a <b>chemical reaction</b>. For example, "
                     "Ba(OH)2 + H2SO4 -> BaSO4 + 2H2O is an inorganic chemical reaction; "
                     "similarly, hydrolysis of starch into glucose is an organic chemical "
                     "reaction."))
story.append(P("<b>Rate</b> of a physical or chemical process refers to the amount of product "
               "formed per unit time: rate = delta P / delta t. Rate can also be called "
               "<b>velocity</b> if the direction is specified. Rates of physical and chemical "
               "processes are influenced by <b>temperature</b> among other factors: a general rule "
               "of thumb is that rate doubles or decreases by half for every 10 degrees C change "
               "in either direction."))
story.append(P("Catalysed reactions proceed at rates vastly higher than that of uncatalysed ones. "
               "When enzyme-catalysed reactions are observed, the rate is vastly higher than the "
               "same but uncatalysed reaction."))
story.append(note("Take CO2 + H2O -> H2CO3 (carbon dioxide + water -> carbonic acid). In the "
                  "absence of any enzyme this reaction is very slow, with about <b>200 molecules "
                  "of H2CO3</b> being formed in an hour. However, using the enzyme present within "
                  "the cytoplasm called <b>carbonic anhydrase</b>, the reaction speeds dramatically "
                  "with about <b>600,000 molecules</b> being formed every second - the enzyme has "
                  "accelerated the reaction rate by about <b>10 million times</b>. The power of "
                  "enzymes is incredible indeed!"))
story.append(keyterm("There are thousands of types of enzymes, each catalysing a unique chemical "
                     "or metabolic reaction. A multistep chemical reaction, when each of the steps "
                     "is catalysed by the same enzyme complex or by different enzymes, is called a "
                     "<b>metabolic pathway</b>."))
story.append(P("For example, Glucose -> 2 Pyruvic acid (C6H12O6 + O2 -> 2 C3H4O3 + 2 H2O) is "
               "actually a metabolic pathway in which glucose becomes pyruvic acid through "
               "<b>ten</b> different enzyme-catalysed metabolic reactions. This very metabolic "
               "pathway, with one or two additional reactions, gives rise to a variety of "
               "metabolic end products."))
story.append(P("In our skeletal muscle, under anaerobic conditions, <b>lactic acid</b> is formed. "
               "Under normal aerobic conditions, <b>pyruvic acid</b> is formed. In yeast, during "
               "fermentation, the same pathway leads to the production of <b>ethanol</b> "
               "(alcohol). Hence, in different conditions different products are possible."))

# ---- 9.8.2 How do Enzymes bring about High Rates of Catalysis? ---- (F195-F212) + Fig 9.4
story.append(H("9.8.2", "How do Enzymes bring about such High Rates of Catalysis?", 2,
               keyterm("The chemical which is converted into a product is called a "
                       "<b>'substrate'</b>. Enzymes - i.e. proteins with three-dimensional "
                       "structures including an active site - convert a substrate (S) into a "
                       "product (P). Symbolically: S -> P.")))
story.append(P("It is now understood that the substrate 'S' has to bind the enzyme at its active "
               "site within a given cleft or pocket. The substrate has to <b>diffuse</b> towards "
               "the active site. There is thus an obligatory formation of an <b>'ES' complex</b> "
               "(E stands for enzyme); this complex formation is a <b>transient</b> phenomenon."))
story.append(P("During the state where substrate is bound to the enzyme active site, a new "
               "structure of the substrate, called the <b>transition state structure</b>, is "
               "formed. Very soon, after the expected bond breaking/making is completed, the "
               "product is released from the active site. In other words, the structure of the "
               "substrate gets transformed into the structure of the product(s)."))
story.append(P("The pathway of this transformation must go through the transition state structure. "
               "There could be many more 'altered structural states' between the stable substrate "
               "and the product; implicit in this is the fact that all other intermediate "
               "structural states are <b>unstable</b>. Stability is something related to the "
               "energy status of the molecule or the structure."))
story.append(figure("fig_9_4.png",
                    "Fig. 9.4 - Concept of activation energy: potential energy rises from the "
                    "substrate (S) to a high-energy transition state and falls to the product "
                    "(P); the enzyme lowers the activation energy barrier.", max_width_cm=11.0))
story.append(labels_line(["Transition state", "Activation energy without enzyme",
                          "Activation energy with enzyme", "Potential Energy", "Substrate (s)",
                          "Product (P)", "Progress of reaction"]))
story.append(P("In the graph, the <b>y-axis</b> represents the potential energy content and the "
               "<b>x-axis</b> represents the progression of the structural transformation or "
               "states through the transition state. Consider the energy-level difference between "
               "S and P: if 'P' is at a lower level than 'S', the reaction is an <b>exothermic</b> "
               "reaction and one need not supply energy (by heating) in order to form the product."))
story.append(keyterm("However, whether it is an exothermic (spontaneous) reaction or an "
                     "<b>endothermic</b> (energy-requiring) reaction, the 'S' has to go through a "
                     "much higher energy state or transition state. The difference in average "
                     "energy content of 'S' from that of this transition state is called "
                     "<b>'activation energy'</b>. Enzymes eventually bring down this energy "
                     "barrier, making the transition of 'S' to 'P' easier."))

# ---- 9.8.3 Nature of Enzyme Action ---- (F213-F220)
story.append(H("9.8.3", "Nature of Enzyme Action", 2,
               P("Each enzyme (E) has a substrate (S) binding site in its molecule so that a highly "
                 "reactive enzyme-substrate complex (ES) is produced. This complex is short-lived "
                 "and dissociates into its product(s) P and the unchanged enzyme, with an "
                 "intermediate formation of the enzyme-product complex (EP). The formation of the "
                 "ES complex is essential for catalysis:")))
story.append(P("<b>E + S -> ES -> EP -> E + P</b>", "Body"))
story.append(process_flow([
    "First, the substrate binds to the <b>active site</b> of the enzyme, fitting into the active "
    "site.",
    "The binding of the substrate <b>induces the enzyme to alter its shape</b>, fitting more "
    "tightly around the substrate.",
    "The active site, now in close proximity to the substrate, <b>breaks the chemical bonds</b> of "
    "the substrate and the new enzyme-product complex is formed.",
    "The enzyme <b>releases the products</b> of the reaction and the free enzyme is ready to bind "
    "to another substrate molecule and run through the catalytic cycle once again.",
]))

# ---- 9.8.4 Factors Affecting Enzyme Activity ---- (F221-F234, summary-unique F276) + Fig 9.5
story.append(H("9.8.4", "Factors Affecting Enzyme Activity", 2,
               P("The activity of an enzyme can be affected by a change in the conditions which can "
                 "alter the tertiary structure of the protein. These include <b>temperature, pH, "
                 "change in substrate concentration</b> or binding of specific chemicals that "
                 "regulate its activity.")))
story.append(keyterm("Enzymes generally function in a narrow range of temperature and pH (Figure "
                     "9.5). Each enzyme shows its highest activity at a particular temperature and "
                     "pH called the <b>optimum temperature</b> and <b>optimum pH</b>. Activity "
                     "declines both below and above the optimum value. (Proteinaceous enzymes thus "
                     "exhibit <b>substrate specificity</b> and require optimum temperature and pH "
                     "for maximal activity.)"))
story.append(P("<b>Low temperature</b> preserves the enzyme in a temporarily inactive state, "
               "whereas <b>high temperature</b> destroys enzymatic activity because proteins are "
               "<b>denatured</b> by heat."))
story.append(figure("fig_9_5a.png",
                    "Fig. 9.5 (a) - Effect of change in pH on enzyme activity: activity peaks at "
                    "the optimum pH and falls on either side.", max_width_cm=7.5))
story.append(labels_line(["Enzyme activity", "pH"]))
story.append(figure("fig_9_5b.png",
                    "Fig. 9.5 (b) - Effect of change in temperature on enzyme activity: activity "
                    "peaks at the optimum temperature and falls on either side.",
                    max_width_cm=7.5))
story.append(labels_line(["Temperature"]))
story.append(P("With the increase in substrate concentration, the velocity of the enzymatic "
               "reaction rises at first. The reaction ultimately reaches a <b>maximum velocity "
               "(Vmax)</b> which is not exceeded by any further rise in the concentration of the "
               "substrate. This is because the enzyme molecules are fewer than the substrate "
               "molecules and, after saturation of these molecules, there are no free enzyme "
               "molecules to bind with the additional substrate molecules (Figure 9.5)."))
story.append(figure("fig_9_5c.png",
                    "Fig. 9.5 (c) - Effect of change in substrate concentration on enzyme "
                    "activity: velocity rises then plateaus at Vmax.", max_width_cm=7.5))
story.append(labels_line(["Vmax", "Velocity of reaction (V)", "Km"]))
story.append(P("<i>Figure 9.5 - Effect of change in: (a) pH (b) Temperature and (c) Concentration "
               "of substrate on enzyme activity.</i>"))
story.append(keyterm("The activity of an enzyme is also sensitive to the presence of specific "
                     "chemicals that bind to the enzyme. When the binding of the chemical shuts "
                     "off enzyme activity, the process is called <b>inhibition</b> and the "
                     "chemical is called an <b>inhibitor</b>."))
story.append(P("When the inhibitor closely resembles the substrate in its molecular structure and "
               "inhibits the activity of the enzyme, it is known as a <b>competitive inhibitor</b>. "
               "Due to its close structural similarity with the substrate, the inhibitor competes "
               "with the substrate for the substrate-binding site of the enzyme. Consequently, the "
               "substrate cannot bind and the enzyme action declines - e.g., inhibition of "
               "<b>succinic dehydrogenase</b> by <b>malonate</b>, which closely resembles the "
               "substrate <b>succinate</b> in structure. Such competitive inhibitors are often "
               "used in the control of bacterial pathogens."))

# ---- 9.8.5 Classification and Nomenclature of Enzymes ---- (F235-F242)
story.append(H("9.8.5", "Classification and Nomenclature of Enzymes", 2,
               P("Thousands of enzymes have been discovered, isolated and studied. Most of these "
                 "enzymes have been classified into different groups based on the type of "
                 "reactions they catalyse. Enzymes are divided into <b>6 classes</b>, each with "
                 "4-13 subclasses, and named accordingly by a <b>four-digit number</b>."),
               has_table=True))
story.append(data_table([
    ["Class", "Reaction catalysed"],
    ["<b>Oxidoreductases / dehydrogenases</b>",
     "Catalyse oxidoreduction between two substrates S and S', e.g., S reduced + S' oxidised -> S "
     "oxidised + S' reduced."],
    ["<b>Transferases</b>",
     "Catalyse a transfer of a group G (other than hydrogen) between a pair of substrates S and "
     "S', e.g., S-G + S' -> S + S'-G."],
    ["<b>Hydrolases</b>",
     "Catalyse hydrolysis of ester, ether, peptide, glycosidic, C-C, C-halide or P-N bonds."],
    ["<b>Lyases</b>",
     "Catalyse removal of groups from substrates by mechanisms other than hydrolysis, leaving "
     "double bonds."],
    ["<b>Isomerases</b>",
     "Include all enzymes catalysing inter-conversion of optical, geometric or positional "
     "isomers."],
    ["<b>Ligases</b>",
     "Catalyse the linking together of 2 compounds, e.g., joining of C-O, C-S, C-N, P-O etc. "
     "bonds."],
], col_widths=[2.3, 4.5]))
story.append(memory_aid("Six enzyme classes - <b>O</b>xidoreductases, <b>T</b>ransferases, "
                        "<b>H</b>ydrolases, <b>L</b>yases, <b>I</b>somerases, <b>L</b>igases. "
                        "Mnemonic: <b>\"Over The Hill, Little Indians Ligate.\"</b> (memory aid, "
                        "not in NCERT)."))

# ---- 9.8.6 Co-factors ---- (F243-F253)
story.append(H("9.8.6", "Co-factors", 2,
               P("Enzymes are composed of one or several polypeptide chains. However, there are a "
                 "number of cases in which non-protein constituents called <b>co-factors</b> are "
                 "bound to the enzyme to make the enzyme catalytically active. In these instances, "
                 "the protein portion of the enzyme is called the <b>apoenzyme</b>.")))
story.append(P("Three kinds of cofactors may be identified: <b>prosthetic groups, co-enzymes and "
               "metal ions</b>."))
story.append(B("&bull; <b>Prosthetic groups</b> are organic compounds and are distinguished from "
               "other cofactors in that they are <b>tightly bound</b> to the apoenzyme. For "
               "example, in peroxidase and catalase, which catalyse the breakdown of hydrogen "
               "peroxide to water and oxygen, <b>haem</b> is the prosthetic group and it is a part "
               "of the active site of the enzyme."))
story.append(B("&bull; <b>Co-enzymes</b> are also organic compounds but their association with the "
               "apoenzyme is only <b>transient</b>, usually occurring during the course of "
               "catalysis. Co-enzymes serve as co-factors in a number of different enzyme-catalysed "
               "reactions. The essential chemical components of many coenzymes are <b>vitamins</b>, "
               "e.g., coenzyme nicotinamide adenine dinucleotide (NAD) and NADP contain the vitamin "
               "niacin."))
story.append(B("&bull; <b>Metal ions</b>: a number of enzymes require metal ions for their "
               "activity which form coordination bonds with side chains at the active site and at "
               "the same time form one or more coordination bonds with the substrate, e.g., "
               "<b>zinc</b> is a cofactor for the proteolytic enzyme <b>carboxypeptidase</b>."))
story.append(P("Catalytic activity is lost when the co-factor is removed from the enzyme, which "
               "testifies that they play a crucial role in the catalytic activity of the enzyme."))

# ---- Quick Recap ---- (rewritten, denser version of the NCERT summary)
# [VERIFICATION FIX] Pass 3 audit: the mandatory Quick Recap (Content Order item 8) was
# absent - the chapter ran from 9.8.6 Co-factors straight into the Appendix. Added here.
story.append(H("QR", "Quick Recap", 1,
               P("Despite a bewildering diversity of living organisms, their chemical composition "
                 "and metabolic reactions are remarkably similar. Qualitatively the elemental "
                 "composition of living tissue and of non-living matter look alike, but a closer "
                 "examination shows the relative abundance of <b>carbon, hydrogen and oxygen</b> is "
                 "higher in living systems than in inanimate matter. The most abundant chemical in "
                 "living organisms is <b>water</b>.")))
story.append(B("&bull; <b>Small molecules.</b> There are thousands of low-molecular-weight "
               "(under 1000 Da) biomolecules - amino acids, monosaccharide and disaccharide sugars, "
               "fatty acids, glycerol, nucleotides, nucleosides and nitrogen bases. There are "
               "<b>20</b> types of amino acids and <b>5</b> types of nucleotides. Fats and oils are "
               "glycerides in which fatty acids are esterified to glycerol; <b>phospholipids</b> "
               "contain, in addition, a phosphorylated nitrogenous compound."))
story.append(B("&bull; <b>Macromolecules.</b> Only <b>three</b> types are found in living systems - "
               "proteins, nucleic acids and polysaccharides; <b>lipids</b>, because of their "
               "association with membranes, separate into the macromolecular fraction. "
               "Biomacromolecules are <b>polymers</b> made of building blocks which are different, "
               "so proteins are <b>heteropolymers</b> of amino acids and nucleic acids (RNA and DNA) "
               "are composed of nucleotides. Biomacromolecules have a hierarchy of structures - "
               "<b>primary, secondary, tertiary and quaternary</b>."))
story.append(B("&bull; <b>Functions.</b> Nucleic acids serve as the <b>genetic material</b>, "
               "carrying hereditary information passed from the parental generation to the progeny. "
               "Polysaccharides are components of the cell wall in plants and fungi and of the "
               "exoskeleton of arthropods, and are also storage forms of energy (e.g., starch and "
               "glycogen). Proteins serve a variety of cellular functions - many are enzymes, some "
               "antibodies, some receptors, some hormones and some structural proteins. "
               "<b>Collagen</b> is the most abundant protein in the animal world and <b>RuBisCO</b> "
               "(Ribulose bisphosphate Carboxylase-Oxygenase) is the most abundant protein in the "
               "whole of the biosphere."))
story.append(B("&bull; <b>Enzymes.</b> Enzymes are proteins which catalyse biochemical reactions in "
               "the cells, while <b>ribozymes</b> are nucleic acids with catalytic power. "
               "Proteinaceous enzymes exhibit <b>substrate specificity</b>, require an optimum "
               "temperature and pH for maximal activity, and are <b>denatured</b> at high "
               "temperatures. Enzymes <b>lower the activation energy</b> of reactions and thereby "
               "enhance their rate greatly."))

# ---- Appendix: Terms used in the exercises ---- (exercise-gap scan, Rule 5)
story.append(H("A", "Appendix - Terms Assumed by the NCERT Exercises", 1,
               P("This appendix records what the chapter itself supplies for each exercise "
                 "question. Where a question assumes information the chapter does not contain, that "
                 "part is flagged as beyond this chapter rather than answered from outside the "
                 "source (Rule 5).")))
story.append(B("&bull; <b>Q1 Macromolecules.</b> Defined in 9.3: molecules of the acid-insoluble "
               "fraction (over ~10,000 Da, polymeric). Examples are the four acid-insoluble classes "
               "- proteins, nucleic acids, polysaccharides and lipids. Note the chapter's own "
               "tension: the summary counts only <b>three</b> macromolecules because 'Lipids are "
               "not strictly macromolecules'."))
story.append(B("&bull; <b>Q2 Tertiary structure.</b> Defined in 9.7: the long chain folded upon "
               "itself like a hollow woollen ball, giving a 3-D shape, absolutely necessary for "
               "biological activity."))
story.append(B("&bull; <b>Q3 Ten small-molecular-weight biomolecules.</b> The chapter supplies the "
               "biomolecules (Figure 9.1) and the size criteria (18-800 Da acid-soluble; under 1000 "
               "Da micromolecules). The industry and buyer half is <b>beyond this chapter</b>."))
story.append(B("&bull; <b>Q4 Proteins as therapeutic agents.</b> The chapter gives protein "
               "functions (Table 9.5: insulin as hormone, antibody, trypsin as enzyme). The "
               "therapeutic and cosmetic applications are <b>beyond this chapter</b>."))
story.append(B("&bull; <b>Q5 Composition of triglyceride.</b> In 9.1: fatty acids esterified to "
               "glycerol, in the mono/di/tri series; Figure 9.1 (c) shows a triglyceride (R1, R2, "
               "R3 are fatty acids)."))
story.append(B("&bull; <b>Q6 Ball-and-stick models.</b> An activity; 'ball and stick' is not a "
               "chapter term, though Figure 9.3 (a) is drawn as a ball-and-stick chain. Pointed at "
               "the chapter's structural plates (Figures 9.1 and 9.3); the model-building itself is "
               "<b>beyond this chapter</b>."))
story.append(B("&bull; <b>Q7 Structure of alanine.</b> Named in the body and drawn in Figure 9.1 "
               "(b); in words, it is an alpha-amino acid on a substituted methane with four "
               "substituents (H, -COOH, -NH2 and R), the R group here being a <b>methyl</b> group."))
story.append(B("&bull; <b>Q8 Gums.</b> Gums appear as secondary metabolites (9.2) and in Table 9.3 "
               "('Rubber, gums, cellulose'). What gums are made of, and any comparison with "
               "Fevicol, are <b>beyond this chapter</b>."))
story.append(B("&bull; <b>Q9 Qualitative tests.</b> The chapter's one colour test is the "
               "<b>starch-I2 blue</b> reaction (9.5), which is for a polysaccharide. Tests for "
               "proteins, fats and amino acids are <b>beyond this chapter</b>."))
story.append(B("&bull; <b>Q10 Cellulose vs paper tonnage.</b> The chapter has cellulose in cell "
               "walls, paper as cellulosic, and RuBisCO as the biosphere's most abundant protein, "
               "but <b>no tonnage figures</b> - the quantitative comparison is beyond this chapter."))
story.append(B("&bull; <b>Q11 Properties of enzymes.</b> Scattered across 9.8-9.8.6: proteinaceous "
               "(with ribozyme exception), active-site fit and substrate specificity, lower "
               "activation energy, high catalytic rate, optimum temperature and pH, denaturation "
               "by heat, thermal stability in thermophiles."))

if __name__ == "__main__":
    sys.exit(build_pdf(OUT_PDF, story,
                       title="Class 11 Chapter 9 - Biomolecules (NEET notes)",
                       subject="NEET Biology"))
