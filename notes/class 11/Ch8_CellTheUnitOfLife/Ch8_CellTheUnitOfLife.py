#!/usr/bin/env python3
"""
Class 11 Chapter 8 - Cell: The Unit of Life  ->  NEET replacement notes.

Built per SUPREME COMMAND PROMPT.md v6, big-chapter 5-pass protocol.
Every style, colour, font and layout helper is imported from the repo-level
neet_template.py; nothing visual is re-declared here (v6 s0.6).

Content source of truth: Ch8_CellTheUnitOfLife_inventory.md (frozen, F001-F325).
This script is one linear story.append(...) sequence with `# ---- N.N ----`
markers so a Pass 3 fix stays surgical.

Figures: the 14 verified monochrome assets in assets/ only. The G.N. Ramachandran
photograph is deliberately NOT embedded (v6 s4.4 hard no); the profile is text-only.

Unit notation: the source's micron symbol is written here as the ASCII letters
`um` (micrometre). Raw Greek letters are banned by v6 s4 technical rules.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))

from reportlab.platypus import Spacer
from reportlab.lib.units import cm

from neet_template import (  # noqa: E402
    STYLES,
    heading, keyterm, process_flow, note, memory_aid, data_table, figure,
    title_block, build_pdf,
)
from reportlab.platypus import Paragraph  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "assets")
OUT_PDF = os.path.join(HERE, "Ch8_CellTheUnitOfLife.pdf")


def P(text, style="Body"):
    return Paragraph(text, STYLES[style])


def B(text, level=1):
    return Paragraph(text, STYLES[f"Bullet{level}"])


def labels_line(labels):
    """Reproduce the in-figure labels verbatim beneath a figure.

    v6 s0.4 check 6 requires every in-figure label catalogued in the inventory to
    appear in the running text, so a reader working from the grey diagram can name
    every part. The NCERT spelling of each label is preserved exactly (Rule 4).
    """
    return P("<i>Labels printed in the figure:</i> " + "; ".join(labels))


story = []

story.extend(title_block("Cell: The Unit of Life"))
story.append(P("<i>Class 11 - Chapter 8 - NEET replacement notes built from the NCERT "
               "chapter text, its 13 figures, its summary and its 14 exercises.</i>"))
story.append(Spacer(1, 0.18 * cm))

# ---- 0.1 ---- Unit 3 opener: why the cell is the unit of study  (F001-F011)
story.append(heading("U3", "Unit Opener - Cell: Structure and Functions", level=1))
story.append(keyterm("<b>Biology</b> is the study of living organisms."))
story.append(P("The detailed description of their form and appearance only brought out their "
               "diversity. It is the cell theory that emphasised the unity underlying this "
               "diversity of forms, i.e., the cellular organisation of all life forms."))
story.append(P("Cell theory also created a sense of mystery around living phenomena, i.e., "
               "physiological and behavioural processes. This mystery was the requirement of "
               "integrity of cellular organisation for living phenomena to be demonstrated or "
               "observed."))
story.append(P("Alternatively, one can take a physico-chemical approach and use cell-free "
               "systems to investigate. This approach enables us to describe the various "
               "processes in molecular terms. The approach is established by analysis of living "
               "tissues for elements and compounds."))
story.append(keyterm("This physico-chemical approach to study and understand living organisms "
                     "is called <b>'Reductionist Biology'</b>."))
story.append(P("The concepts and techniques of physics and chemistry are applied to understand "
               "biology. It can also explain the abnormal processes that occur during any "
               "diseased condition."))
story.append(note("Throughout these notes the micron unit of the source is written as the ASCII "
                  "letters <b>um</b> (micrometre) and <b>nm</b> stands for nanometre. This is a "
                  "notation choice only - no value has been changed. The source's own text layer "
                  "renders the micron symbol as 'mm'; every such number was re-read from the page "
                  "image and is reproduced here as the true micrometre."))

# ---- 0.2 ---- Scientist profile, text-only (F012-F019)
story.append(heading("U3", "Scientist Profile (printed in the unit opener)", level=2))
story.append(note("<b>G.N. RAMACHANDRAN (1922 - 2001).</b> Born on October 8, 1922, in a small "
                  "town, not far from Cochin on the southwestern coast of India. He passed away "
                  "at the age of 78, on April 7, 2001. He was an outstanding figure in the field "
                  "of protein structure, and was the founder of the 'Madras school' of "
                  "conformational analysis of biopolymers. His discovery of the triple helical "
                  "structure of collagen published in Nature in 1954, and his analysis of the "
                  "allowed conformations of proteins through the use of the 'Ramachandran plot' "
                  "rank among the most outstanding contributions in structural biology. His "
                  "father was a professor of mathematics at a local college and thus had "
                  "considerable influence in shaping Ramachandran's interest in mathematics. "
                  "Ramachandran graduated in 1942 as the top-ranking student in the B.Sc. "
                  "(Honors) Physics course of the University of Madras. He received a Ph.D. from "
                  "Cambridge University in 1949. While at Cambridge, Ramachandran met Linus "
                  "Pauling and was deeply influenced by his publications on models of the "
                  "alpha-helix and beta-sheet structures that directed his attention to solving "
                  "the structure of collagen. <i>(The portrait photograph printed beside this "
                  "profile in the source is deliberately not reproduced; the profile is "
                  "text-only.)</i>"))

# ---- 8.1 ---- What is a Cell?  (F020-F028)
story.append(heading("8.1", "What is a Cell?", level=1))
story.append(P("The answer to this is the presence of the basic unit of life - the cell in all "
               "living organisms. All organisms are composed of cells."))
story.append(keyterm("Some are composed of a single cell and are called <b>unicellular "
                     "organisms</b> while others, like us, composed of many cells, are called "
                     "<b>multicellular organisms</b>."))
story.append(P("Unicellular organisms are capable of (i) independent existence and (ii) "
               "performing the essential functions of life. Anything less than a complete "
               "structure of a cell does not ensure independent living."))
story.append(keyterm("Hence, <b>cell</b> is the fundamental structural and functional unit of "
                     "all living organisms."))
story.append(P("<b>Antonie Von Leeuwenhoek</b> first saw and described a live cell. "
               "<b>Robert Brown</b> later discovered the nucleus. The invention of the microscope "
               "and its improvement leading to the electron microscope revealed all the "
               "structural details of the cell."))
story.append(memory_aid("Leeuwenhoek saw the <b>cell</b>; Brown found the <b>nucleus</b>. "
                        "Exercise Q1 turns on exactly this split - 'Robert Brown discovered the "
                        "cell' is the statement that is <b>not</b> correct."))

# ---- 8.2 ---- Cell Theory  (F029-F037)
story.append(heading("8.2", "Cell Theory", level=1))
story.append(process_flow([
    "<b>Matthias Schleiden (1838), a German botanist</b> - examined a large number of plants and "
    "observed that all plants are composed of different kinds of cells which form the tissues of "
    "the plant.",
    "<b>Schwann (1839), a German Zoologist</b> - studied different types of animal cells and "
    "reported that cells had a thin outer layer which is today known as the 'plasma membrane'. He "
    "also concluded, based on his studies on plant tissues, that the presence of cell wall is a "
    "unique character of the plant cells. On the basis of this, Schwann proposed the hypothesis "
    "that the bodies of animals and plants are composed of cells and products of cells.",
    "<b>Schleiden and Schwann together</b> formulated the cell theory. This theory however, did "
    "not explain as to how new cells were formed.",
    "<b>Rudolf Virchow (1855)</b> first explained that cells divided and new cells are formed "
    "from pre-existing cells (<i>Omnis cellula-e cellula</i>). He modified the hypothesis of "
    "Schleiden and Schwann to give the cell theory a final shape.",
]))
story.append(keyterm("<b>Cell theory</b> as understood today is: (i) all living organisms are "
                     "composed of cells and products of cells. (ii) all cells arise from "
                     "pre-existing cells."))

# ---- 8.3 ---- An Overview of Cell  (F038-F060, Fig 8.1)
story.append(heading("8.3", "An Overview of Cell", level=1))
story.append(P("The onion cell which is a typical plant cell, has a distinct cell wall as its "
               "outer boundary and just within it is the cell membrane. The cells of the human "
               "cheek have an outer membrane as the delimiting structure of the cell."))
story.append(P("Inside each cell is a dense membrane bound structure called <b>nucleus</b>. This "
               "nucleus contains the chromosomes which in turn contain the genetic material, "
               "DNA."))
story.append(keyterm("Cells that have membrane bound nuclei are called <b>eukaryotic</b> whereas "
                     "cells that lack a membrane bound nucleus are <b>prokaryotic</b>."))
story.append(keyterm("In both prokaryotic and eukaryotic cells, a semi-fluid matrix called "
                     "<b>cytoplasm</b> occupies the volume of the cell."))
story.append(P("The cytoplasm is the main arena of cellular activities in both the plant and "
               "animal cells. Various chemical reactions occur in it to keep the cell in the "
               "'living state'."))
story.append(P("Besides the nucleus, the eukaryotic cells have other membrane bound distinct "
               "structures called <b>organelles</b> like the endoplasmic reticulum (ER), the "
               "golgi complex, lysosomes, mitochondria, microbodies and vacuoles. The prokaryotic "
               "cells lack such membrane bound organelles."))
story.append(P("<b>Ribosomes</b> are non-membrane bound organelles found in all cells - both "
               "eukaryotic as well as prokaryotic. Within the cell, ribosomes are found not only "
               "in the cytoplasm but also within the two organelles - chloroplasts (in plants) "
               "and mitochondria and on rough ER. Animal cells contain another non-membrane bound "
               "organelle called <b>centrosome</b> which helps in cell division."))

story.append(heading("8.3", "Size, shape and activity of cells", level=3))
story.append(P("Cells differ greatly in size, shape and activities (Figure 8.1)."))
story.append(B("- <b>Mycoplasmas</b>, the smallest cells, are only <b>0.3 um</b> in length, "
               "while <b>bacteria</b> could be <b>3 to 5 um</b>."))
story.append(B("- The largest isolated single cell is the <b>egg of an ostrich</b>."))
story.append(B("- Among multicellular organisms, <b>human red blood cells</b> are about "
               "<b>7.0 um</b> in diameter."))
story.append(B("- <b>Nerve cells</b> are some of the longest cells."))
story.append(P("They may be disc-like, polygonal, columnar, cuboid, thread like, or even "
               "irregular. The shape of the cell may vary with the function they perform."))
story.append(figure("fig_8_1.png",
                    "Figure 8.1 Diagram showing different shapes of the cells",
                    ASSETS))
story.append(labels_line([
    "Red blood cells (round and biconcave)",
    "White blood cells (amoeboid)",
    "Columnar epithelial cells (long and narrow)",
    "Nerve cell (Branched and long)",
    "A tracheid (elongated)",
    "Mesophyll cells (round and oval)",
]))

# ---- 8.4 ---- Prokaryotic Cells  (F061-F080, Fig 8.2)
story.append(heading("8.4", "Prokaryotic Cells", level=1))
story.append(P("The prokaryotic cells are represented by <b>bacteria</b>, <b>blue-green "
               "algae</b>, <b>mycoplasma</b> and <b>PPLO</b> (Pleuro Pneumonia Like Organisms). "
               "They are generally smaller and multiply more rapidly than the eukaryotic cells "
               "(Figure 8.2). They may vary greatly in shape and size."))
story.append(data_table([
    ["The four basic shapes of bacteria", "Shape described in the source"],
    ["Bacillus", "rod like"],
    ["Coccus", "spherical"],
    ["Vibrio", "comma shaped"],
    ["Spirillum", "spiral"],
], col_widths=[1, 1]))
story.append(Spacer(1, 0.15 * cm))
story.append(P("The organisation of the prokaryotic cell is fundamentally similar even though "
               "prokaryotes exhibit a wide variety of shapes and functions."))
story.append(B("- All prokaryotes have a <b>cell wall</b> surrounding the cell membrane "
               "<b>except in mycoplasma</b>."))
story.append(B("- The semi-fluid matrix filling the cell is the <b>cytoplasm</b>."))
story.append(B("- There is <b>no well-defined nucleus</b>. The genetic material is basically "
               "naked, not enveloped by a nuclear membrane. (Nuclear membrane is found in "
               "eukaryotes.)"))
story.append(P("In addition to the genomic DNA (the single chromosome/circular DNA), many "
               "bacteria have small circular DNA outside the genomic DNA."))
story.append(keyterm("These smaller DNA are called <b>plasmids</b>. The plasmid DNA confers "
                     "certain unique phenotypic characters to such bacteria. One such character "
                     "is <b>resistance to antibiotics</b>. In higher classes you will learn that "
                     "this plasmid DNA is used to monitor bacterial transformation with foreign "
                     "DNA."))
story.append(P("No organelles, like the ones in eukaryotes, are found in prokaryotic cells "
               "<b>except for ribosomes</b>. Prokaryotes have something unique in the form of "
               "<b>inclusions</b>."))
story.append(keyterm("A specialised differentiated form of cell membrane called <b>mesosome</b> "
                     "is the characteristic of prokaryotes. They are essentially infoldings of "
                     "cell membrane."))
story.append(figure("fig_8_2.png",
                    "Figure 8.2 Diagram showing comparison of eukaryotic cell with other "
                    "organisms",
                    ASSETS))
story.append(labels_line([
    "A typical eukaryotic cell (10-20 um)",
    "Typical bacteria (1-2 um)",
    "PPLO (about 0.1 um)",
    "Viruses (0.02-0.2 um)",
]))

# ---- 8.4.1 ---- Cell Envelope and its Modifications  (F081-F103)
story.append(heading("8.4.1", "Cell Envelope and its Modifications", level=2))
story.append(P("<b>Most</b> prokaryotic cells, particularly the bacterial cells, have a "
               "chemically complex cell envelope. The cell envelope consists of a tightly bound "
               "three layered structure i.e., the outermost <b>glycocalyx</b> followed by the "
               "<b>cell wall</b> and then the <b>plasma membrane</b>. Although each layer of the "
               "envelope performs distinct function, they act together as a single protective "
               "unit."))
story.append(P("Bacteria can be classified into two groups on the basis of the differences in "
               "the cell envelopes and the manner in which they respond to the staining procedure "
               "developed by Gram viz., those that take up the gram stain are <b>Gram "
               "positive</b> and the others that do not are called <b>Gram negative</b> "
               "bacteria."))
story.append(data_table([
    ["Layer of the cell envelope", "What the source says about it"],
    ["Glycocalyx (outermost)",
     "Differs in composition and thickness among different bacteria. It could be a loose sheath "
     "called the <b>slime layer</b> in some, while in others it may be thick and tough, called "
     "the <b>capsule</b>."],
    ["Cell wall",
     "Determines the shape of the cell and provides a strong structural support to prevent the "
     "bacterium from bursting or collapsing."],
    ["Plasma membrane",
     "Selectively permeable in nature and interacts with the outside world. This membrane is "
     "similar structurally to that of the eukaryotes."],
], col_widths=[1, 2.4]))
story.append(Spacer(1, 0.15 * cm))
story.append(keyterm("A special membranous structure is the <b>mesosome</b> which is formed by "
                     "the extensions of plasma membrane into the cell. These extensions are in "
                     "the form of <b>vesicles</b>, <b>tubules</b> and <b>lamellae</b>."))
story.append(B("- They help in cell wall formation, DNA replication and distribution to daughter "
               "cells."))
story.append(B("- They also help in respiration, secretion processes, to increase the surface "
               "area of the plasma membrane and enzymatic content."))
story.append(keyterm("In some prokaryotes like <b>cyanobacteria</b>, there are other membranous "
                     "extensions into the cytoplasm called <b>chromatophores</b> which contain "
                     "pigments."))

story.append(heading("8.4.1", "Surface structures: flagella, pili and fimbriae", level=3))
story.append(P("Bacterial cells <b>may</b> be motile or non-motile. If motile, they have thin "
               "filamentous extensions from their cell wall called <b>flagella</b>. Bacteria show "
               "a range in the number and arrangement of flagella."))
story.append(P("Bacterial flagellum is composed of three parts - <b>filament</b>, <b>hook</b> "
               "and <b>basal body</b>. The filament is the longest portion and extends from the "
               "cell surface to the outside."))
story.append(P("Besides flagella, <b>Pili</b> and <b>Fimbriae</b> are also surface structures of "
               "the bacteria but <b>do not play a role in motility</b>. The pili are elongated "
               "tubular structures made of a special protein. The fimbriae are small bristle like "
               "fibres sprouting out of the cell. In <b>some</b> bacteria, they are known to help "
               "attach the bacteria to rocks in streams and also to the host tissues."))

# ---- 8.4.2 ---- Ribosomes and Inclusion Bodies  (F104-F112)
story.append(heading("8.4.2", "Ribosomes and Inclusion Bodies", level=2))
story.append(P("In prokaryotes, ribosomes are associated with the plasma membrane of the cell. "
               "They are about <b>15 nm by 20 nm</b> in size and are made of two subunits - "
               "<b>50S</b> and <b>30S</b> units which when present together form <b>70S</b> "
               "prokaryotic ribosomes."))
story.append(keyterm("<b>Ribosomes are the site of protein synthesis.</b> Several ribosomes may "
                     "attach to a single mRNA and form a chain called <b>polyribosomes</b> or "
                     "<b>polysome</b>. The ribosomes of a polysome translate the mRNA into "
                     "proteins."))
story.append(keyterm("<b>Inclusion bodies:</b> Reserve material in prokaryotic cells are stored "
                     "in the cytoplasm in the form of inclusion bodies. These are <b>not bound by "
                     "any membrane system</b> and lie free in the cytoplasm, e.g., phosphate "
                     "granules, cyanophycean granules and glycogen granules."))
story.append(P("<b>Gas vacuoles</b> are found in blue green and purple and green photosynthetic "
               "bacteria."))

# ---- 8.5 ---- Eukaryotic Cells  (F113-F123, Fig 8.3a, Fig 8.3b)
story.append(heading("8.5", "Eukaryotic Cells", level=1))
story.append(P("The eukaryotes include all the <b>protists</b>, <b>plants</b>, <b>animals</b> "
               "and <b>fungi</b>."))
story.append(B("- In eukaryotic cells there is an extensive compartmentalisation of cytoplasm "
               "through the presence of membrane bound organelles."))
story.append(B("- Eukaryotic cells possess an organised nucleus with a nuclear envelope."))
story.append(B("- In addition, eukaryotic cells have a variety of complex locomotory and "
               "cytoskeletal structures."))
story.append(B("- Their genetic material is organised into chromosomes."))
story.append(P("<b>All eukaryotic cells are not identical.</b>"))
story.append(data_table([
    ["Feature", "Plant cell", "Animal cell"],
    ["Cell wall", "Present", "Absent"],
    ["Plastids", "Present", "Absent"],
    ["Large central vacuole", "Present", "Absent"],
    ["Centrioles", "Absent in <b>almost all</b> plant cells", "Present"],
], col_widths=[1.4, 1.4, 1.4]))
story.append(Spacer(1, 0.15 * cm))
story.append(P("Plant and animal cells are different as the former possess cell walls, plastids "
               "and a large central vacuole which are absent in animal cells. On the other hand, "
               "animal cells have centrioles which are absent in <b>almost all</b> plant cells "
               "(Figure 8.3)."))
story.append(figure("fig_8_3a.png",
                    "Figure 8.3 Diagram showing : (a) Plant cell (b) Animal cell "
                    "- part (a) Plant cell",
                    ASSETS))
story.append(labels_line([
    "Rough endoplasmic reticulum", "Lysosome", "Smooth endoplasmic reticulum", "Plasmodesmata",
    "Microtubule", "Nucleus", "Nucleolus", "Golgi apparatus", "Nuclear envelope",
    "Plasma membrane", "Vacuole", "Middle lamella", "Cell wall", "Mitochondrion", "Ribosomes",
    "Chloroplast", "Cytoplasm", "Peroxisome",
]))
story.append(figure("fig_8_3b.png",
                    "Figure 8.3 Diagram showing : (a) Plant cell (b) Animal cell "
                    "- part (b) Animal cell",
                    ASSETS))
story.append(labels_line([
    "Golgi apparatus", "Microvilli", "Plasma membrane", "Centriole", "Peroxisome", "Lysosome",
    "Ribosomes", "Mitochondrion", "Rough endoplasmic reticulum", "Cytoplasm", "Nucleus",
    "Nucleolus", "Nuclear envelope", "Smooth endoplasmic reticulum",
]))

# ---- 8.5.1 ---- Cell Membrane  (F124-F149, Fig 8.4)
story.append(heading("8.5.1", "Cell Membrane", level=2))
story.append(P("The detailed structure of the membrane was studied only after the advent of the "
               "electron microscope in the 1950s. Meanwhile, chemical studies on the cell "
               "membrane, especially in human <b>red blood cells (RBCs)</b>, enabled the "
               "scientists to deduce the possible structure of plasma membrane."))
story.append(P("These studies showed that the cell membrane is mainly composed of <b>lipids</b> "
               "and <b>proteins</b>. The major lipids are <b>phospholipids</b> that are arranged "
               "in a <b>bilayer</b>. Also, the lipids are arranged within the membrane with the "
               "<b>polar head</b> towards the outer sides and the <b>hydrophobic tails</b> "
               "towards the inner part. This ensures that the nonpolar tail of saturated "
               "hydrocarbons is protected from the aqueous environment (Figure 8.4)."))
story.append(P("In addition to phospholipids, membrane also contains <b>cholesterol</b>. Later, "
               "biochemical investigation clearly revealed that the cell membranes also possess "
               "<b>protein</b> and <b>carbohydrate</b>. The ratio of protein and lipid varies "
               "considerably in different cell types. In human beings, the membrane of the "
               "erythrocyte has approximately <b>52 per cent protein</b> and <b>40 per cent "
               "lipids</b>."))
story.append(data_table([
    ["Membrane proteins, classified by ease of extraction", "Where it lies"],
    ["Peripheral proteins", "Lie on the surface of membrane"],
    ["Integral proteins", "Partially or totally buried in the membrane"],
], col_widths=[1.5, 1.5]))
story.append(Spacer(1, 0.15 * cm))
story.append(keyterm("An improved model of the structure of cell membrane was proposed by "
                     "<b>Singer and Nicolson (1972)</b>, widely accepted as the <b>fluid mosaic "
                     "model</b> (Figure 8.4). According to this, the quasi-fluid nature of lipid "
                     "enables lateral movement of proteins within the overall bilayer. This "
                     "ability to move within the membrane is measured as its <b>fluidity</b>."))
story.append(P("The fluid nature of the membrane is also important from the point of view of "
               "functions like cell growth, formation of intercellular junctions, secretion, "
               "endocytosis, cell division etc."))

story.append(heading("8.5.1", "Transport across the membrane", level=3))
story.append(P("<b>One of the most important functions</b> of the plasma membrane is the "
               "transport of the molecules across it. The membrane is <b>selectively permeable</b> "
               "to <b>some</b> molecules present on either side of it."))
story.append(data_table([
    ["Mode of transport", "What moves, and how the source states it"],
    ["<b>Passive transport</b>",
     "<b>Many</b> molecules can move briefly across the membrane <b>without any requirement of "
     "energy</b> and this is called the passive transport."],
    ["Simple diffusion",
     "Neutral solutes <b>may</b> move across the membrane by the process of simple diffusion "
     "<b>along the concentration gradient</b>, i.e., from higher concentration to the lower."],
    ["Osmosis",
     "Water <b>may</b> also move across this membrane from higher to lower concentration. "
     "Movement of water by diffusion is called osmosis."],
    ["Facilitated by a carrier protein",
     "As the polar molecules cannot pass through the nonpolar lipid bilayer, they require a "
     "<b>carrier protein</b> of the membrane to facilitate their transport across the membrane."],
    ["<b>Active transport</b>",
     "<b>A few</b> ions or molecules are transported across the membrane <b>against</b> their "
     "concentration gradient, i.e., from lower to the higher concentration. Such a transport is "
     "an <b>energy dependent</b> process, in which <b>ATP is utilised</b> and is called active "
     "transport, e.g., Na+/K+ Pump."],
], col_widths=[1, 2.6]))
story.append(Spacer(1, 0.15 * cm))
story.append(figure("fig_8_4.png",
                    "Figure 8.4 Fluid mosaic model of plasma membrane. <b>Read this figure by "
                    "position and shape, not by colour:</b> the source prints the proteins in "
                    "red/orange, the phospholipid bilayer in blue, the sugar chains in orange and "
                    "cholesterol as a yellow rod, and those colours collapse to similar greys "
                    "here. The <b>phospholipid bilayer</b> is the double row of small spherical "
                    "heads with the zig-zag tails between them; the <b>integral protein</b> is "
                    "the large solid mass embedded in and spanning that bilayer; the "
                    "<b>peripheral proteins</b> are the long smooth strands lying on the membrane "
                    "surface; the <b>sugar</b> chains are the small branched chains projecting "
                    "outward from the outer surface; and <b>cholesterol</b> is the short rod "
                    "lying inside the bilayer among the tails.",
                    ASSETS))
story.append(labels_line([
    "Sugar", "Peripheral Protein", "Phospholipid bilayer", "Cholesterol", "Integral protein",
]))

# ---- 8.5.2 ---- Cell Wall  (F150-F155)
story.append(heading("8.5.2", "Cell Wall", level=2))
story.append(keyterm("A <b>non-living rigid structure</b> called the <b>cell wall</b> forms an "
                     "outer covering for the plasma membrane of <b>fungi</b> and <b>plants</b>."))
story.append(P("Cell wall not only gives shape to the cell and protects the cell from mechanical "
               "damage and infection, it also helps in cell-to-cell interaction and provides "
               "barrier to undesirable macromolecules."))
story.append(data_table([
    ["Group", "What the cell wall is made of"],
    ["Algae", "Cellulose, galactans, mannans and minerals like calcium carbonate"],
    ["Other plants", "Cellulose, hemicellulose, pectins and proteins"],
], col_widths=[1, 3]))
story.append(Spacer(1, 0.15 * cm))
story.append(P("The cell wall of a young plant cell, the <b>primary wall</b> is capable of "
               "growth, which gradually diminishes as the cell matures and the <b>secondary "
               "wall</b> is formed on the inner (towards membrane) side of the cell."))
story.append(keyterm("The <b>middle lamella</b> is a layer mainly of <b>calcium pectate</b> "
                     "which holds or glues the different neighbouring cells together."))
story.append(P("The cell wall and middle lamellae <b>may</b> be traversed by "
               "<b>plasmodesmata</b> which connect the cytoplasm of neighbouring cells."))

# ---- 8.5.3 ---- Endomembrane System  (F156-F158)
story.append(heading("8.5.3", "Endomembrane System", level=2))
story.append(P("While each of the membranous organelles is distinct in terms of its structure "
               "and function, <b>many</b> of these are considered together as an <b>endomembrane "
               "system</b> because their functions are coordinated. The endomembrane system "
               "include <b>endoplasmic reticulum (ER)</b>, <b>golgi complex</b>, <b>lysosomes</b> "
               "and <b>vacuoles</b>."))
story.append(note("Since the functions of the <b>mitochondria</b>, <b>chloroplast</b> and "
                  "<b>peroxisomes</b> are not coordinated with the above components, these are "
                  "<b>not</b> considered as part of the endomembrane system."))

# ---- 8.5.3.1 ---- The Endoplasmic Reticulum (ER)  (F159-F169, Fig 8.5, + F310 folded)
story.append(heading("8.5.3.1", "The Endoplasmic Reticulum (ER)", level=3))
story.append(keyterm("Electron microscopic studies of eukaryotic cells reveal the presence of a "
                     "network or reticulum of tiny tubular structures scattered in the cytoplasm "
                     "that is called the <b>endoplasmic reticulum (ER)</b> (Figure 8.5)."))
story.append(P("Hence, ER divides the intracellular space into two distinct compartments, i.e., "
               "<b>luminal</b> (inside ER) and <b>extra luminal</b> (cytoplasm) compartments."))
story.append(P("The ER <b>often</b> shows ribosomes attached to their outer surface."))
story.append(data_table([
    ["Type of ER", "How it is defined and where it is found"],
    ["Rough endoplasmic reticulum (RER)",
     "The endoplasmic reticulum bearing ribosomes on their surface is called rough endoplasmic "
     "reticulum. RER is <b>frequently</b> observed in the cells actively involved in protein "
     "synthesis and secretion. They are extensive and continuous with the outer membrane of the "
     "nucleus."],
    ["Smooth endoplasmic reticulum (SER)",
     "In the absence of ribosomes they appear smooth and are called smooth endoplasmic reticulum. "
     "The smooth endoplasmic reticulum is the <b>major site</b> for synthesis of lipid. In animal "
     "cells lipid-like steroidal hormones are synthesised in SER."],
], col_widths=[1, 2.6]))
story.append(Spacer(1, 0.15 * cm))
story.append(note("<b>From the printed summary (folded in here because the body never says it):</b> "
                  "ER helps in the <b>transport of substances</b>, synthesis of proteins, "
                  "<b>lipoproteins</b> and <b>glycogen</b>."))
story.append(figure("fig_8_5.png", "Figure 8.5 Endoplasmic reticulum", ASSETS))
story.append(labels_line([
    "Nucleus", "Nuclear pore", "Rough endoplasmic reticulum", "Ribosome",
    "Smooth Endoplasmic reticulum",
]))

# ---- 8.5.3.2 ---- Golgi Apparatus  (F170-F182, Fig 8.6)
story.append(heading("8.5.3.2", "Golgi Apparatus", level=3))
story.append(P("<b>Camillo Golgi (1898)</b> first observed densely stained reticular structures "
               "near the nucleus. These were later named <b>Golgi bodies</b> after him."))
story.append(P("They consist of many flat, disc-shaped sacs or <b>cisternae</b> of <b>0.5 um to "
               "1.0 um</b> diameter (Figure 8.6). These are stacked parallel to each other. "
               "<b>Varied</b> number of cisternae are present in a Golgi complex."))
story.append(P("The Golgi cisternae are concentrically arranged near the nucleus with distinct "
               "convex <b>cis</b> or the <b>forming face</b> and concave <b>trans</b> or the "
               "<b>maturing face</b>. The cis and the trans faces of the organelle are entirely "
               "different, but interconnected."))
story.append(keyterm("The golgi apparatus principally performs the function of <b>packaging "
                     "materials</b>, to be delivered either to the intra-cellular targets or "
                     "secreted outside the cell."))
story.append(process_flow([
    "Materials to be packaged in the form of <b>vesicles from the ER</b> fuse with the <b>cis "
    "face</b> of the golgi apparatus.",
    "They move towards the <b>maturing face</b>. This explains, why the golgi apparatus remains "
    "in close association with the endoplasmic reticulum.",
    "A number of proteins synthesised by ribosomes on the endoplasmic reticulum are <b>modified "
    "in the cisternae</b> of the golgi apparatus before they are released from its <b>trans "
    "face</b>.",
]))
story.append(keyterm("Golgi apparatus is the important site of formation of "
                     "<b>glycoproteins</b> and <b>glycolipids</b>."))
story.append(figure("fig_8_6.png", "Figure 8.6 Golgi apparatus", ASSETS))
story.append(labels_line(["Cisternae"]))

# ---- 8.5.3.3 ---- Lysosomes  (F183-F185, + F312 folded)
story.append(heading("8.5.3.3", "Lysosomes", level=3))
story.append(keyterm("<b>Lysosomes</b> are membrane bound vesicular structures formed by the "
                     "process of packaging in the golgi apparatus."))
story.append(P("The isolated lysosomal vesicles have been found to be very rich in <b>almost "
               "all</b> types of hydrolytic enzymes (hydrolases - lipases, proteases, "
               "carbohydrases) <b>optimally active at the acidic pH</b>. These enzymes are "
               "capable of digesting carbohydrates, proteins, lipids and nucleic acids."))
story.append(note("<b>From the printed summary (folded in here because the body never says it):</b> "
                  "Lysosomes are <b>single membrane</b> structures containing enzymes for "
                  "digestion of <b>all types of macromolecules</b>. This is the count that makes "
                  "the lysosome-versus-vacuole contrast in exercise Q12 statable."))

# ---- 8.5.3.4 ---- Vacuoles  (F186-F192)
story.append(heading("8.5.3.4", "Vacuoles", level=3))
story.append(keyterm("The <b>vacuole</b> is the membrane-bound space found in the cytoplasm. It "
                     "contains water, sap, excretory product and other materials not useful for "
                     "the cell."))
story.append(keyterm("The vacuole is bound by a <b>single membrane</b> called <b>tonoplast</b>."))
story.append(P("In plant cells the vacuoles can occupy up to <b>90 per cent</b> of the volume of "
               "the cell. In plants, the tonoplast facilitates the transport of a number of ions "
               "and other materials <b>against concentration gradients</b> into the vacuole, "
               "hence their concentration is significantly higher in the vacuole than in the "
               "cytoplasm."))
story.append(B("- In <b>Amoeba</b>, the <b>contractile vacuole</b> is important for "
               "osmoregulation and excretion."))
story.append(B("- In <b>many</b> cells, as in <b>protists</b>, <b>food vacuoles</b> are formed "
               "by engulfing the food particles."))

# ---- 8.5.4 ---- Mitochondria  (F193-F208, Fig 8.7, + F314 folded)
story.append(heading("8.5.4", "Mitochondria", level=2))
story.append(P("Mitochondria (sing.: mitochondrion), <b>unless specifically stained</b>, are not "
               "easily visible under the microscope. The number of mitochondria per cell is "
               "<b>variable</b> depending on the physiological activity of the cells. In terms of "
               "shape and size also, <b>considerable degree of variability</b> is observed."))
story.append(P("<b>Typically</b> it is sausage-shaped or cylindrical having a diameter of "
               "<b>0.2-1.0 um (average 0.5 um)</b> and length <b>1.0-4.1 um</b>."))
story.append(P("Each mitochondrion is a <b>double membrane-bound</b> structure with the outer "
               "membrane and the inner membrane dividing its lumen distinctly into two aqueous "
               "compartments, i.e., the <b>outer compartment</b> and the <b>inner "
               "compartment</b>."))
story.append(keyterm("The inner compartment is filled with a dense homogeneous substance called "
                     "the <b>matrix</b>."))
story.append(B("- The <b>outer membrane</b> forms the continuous limiting boundary of the "
               "organelle."))
story.append(B("- The <b>inner membrane</b> forms a number of infoldings called the <b>cristae</b> "
               "(sing.: crista) towards the matrix (Figure 8.7). The cristae increase the surface "
               "area."))
story.append(B("- The two membranes have their own specific enzymes associated with the "
               "mitochondrial function."))
story.append(keyterm("<b>Mitochondria are the sites of aerobic respiration.</b> They produce "
                     "cellular energy in the form of <b>ATP</b>, hence they are called <b>'power "
                     "houses' of the cell</b>."))
story.append(P("The matrix also possesses <b>single circular DNA molecule</b>, a few RNA "
               "molecules, <b>ribosomes (70S)</b> and the components required for the synthesis "
               "of proteins. The mitochondria divide by <b>fission</b>."))
story.append(note("<b>From the printed summary (folded in here because the body never says it):</b> "
                  "Mitochondria help in <b>oxidative phosphorylation</b> and generation of "
                  "<b>adenosine triphosphate</b>."))
story.append(figure("fig_8_7.png",
                    "Figure 8.7 Structure of mitochondrion (Longitudinal section)", ASSETS))
story.append(labels_line([
    "Outer membrane", "Inner membrane", "Inter-membrane space", "Matrix", "Crista",
]))

# ---- 8.5.5 ---- Plastids  (F209-F233, Fig 8.8, + F317 folded)
story.append(heading("8.5.5", "Plastids", level=2))
story.append(P("Plastids are found in <b>all plant cells and in euglenoides</b>. These are "
               "easily observed under the microscope as they are large. They bear <b>some "
               "specific pigments</b>, thus imparting specific colours to the plants."))
story.append(data_table([
    ["Type of plastid (classified by the type of pigments)", "What the source says"],
    ["Chloroplasts",
     "Contain <b>chlorophyll</b> and <b>carotenoid</b> pigments which are responsible for "
     "trapping light energy essential for photosynthesis."],
    ["Chromoplasts",
     "Fat soluble <b>carotenoid</b> pigments like <b>carotene</b>, <b>xanthophylls</b> and others "
     "are present. This gives the part of the plant a yellow, orange or red colour."],
    ["Leucoplasts",
     "The <b>colourless</b> plastids of varied shapes and sizes with stored nutrients. "
     "<b>Amyloplasts</b> store carbohydrates (starch), e.g., potato; <b>elaioplasts</b> store "
     "oils and fats whereas the <b>aleuroplasts</b> store proteins."],
], col_widths=[1, 2.4]))
story.append(Spacer(1, 0.15 * cm))
story.append(note("The source contradicts itself here and the contradiction is <b>not</b> "
                  "silently reconciled. The chapter body states plastids are found in all plant "
                  "cells <b>and in euglenoides</b>; the printed summary states plastids are found "
                  "in <b>plant cells only</b>. The body qualifier is kept above because it is the "
                  "more specific statement and it names the exception."))

story.append(heading("8.5.5", "Chloroplast structure", level=3))
story.append(P("<b>Majority</b> of the chloroplasts of the green plants are found in the "
               "<b>mesophyll cells</b> of the leaves. These are lens-shaped, oval, spherical, "
               "discoid or even ribbon-like organelles having variable length <b>(5-10 um)</b> "
               "and width <b>(2-4 um)</b>. Their number varies from <b>1 per cell</b> of the "
               "<b>Chlamydomonas</b>, a green alga to <b>20-40 per cell</b> in the mesophyll."))
story.append(P("<b>Like mitochondria, the chloroplasts are also double membrane bound.</b> Of the "
               "two, the <b>inner</b> chloroplast membrane is <b>relatively less permeable</b>."))
story.append(keyterm("The space limited by the inner membrane of the chloroplast is called the "
                     "<b>stroma</b>."))
story.append(keyterm("A number of organised flattened membranous sacs called the "
                     "<b>thylakoids</b>, are present in the stroma (Figure 8.8)."))
story.append(keyterm("Thylakoids are arranged in stacks like the piles of coins called "
                     "<b>grana</b> (singular: granum) or the <b>intergranal thylakoids</b>."))
story.append(keyterm("In addition, there are flat membranous tubules called the <b>stroma "
                     "lamellae</b> connecting the thylakoids of the different grana."))
story.append(P("The membrane of the thylakoids enclose a space called a <b>lumen</b>. The stroma "
               "of the chloroplast contains enzymes required for the synthesis of carbohydrates "
               "and proteins. It also contains small, double-stranded circular DNA molecules and "
               "ribosomes. <b>Chlorophyll pigments are present in the thylakoids.</b>"))
story.append(P("The ribosomes of the chloroplasts are <b>smaller (70S)</b> than the cytoplasmic "
               "ribosomes <b>(80S)</b>."))
story.append(note("<b>From the printed summary (folded in here because the body never says it):</b> "
                  "The <b>grana</b>, in the plastid, is the site of <b>light reactions</b> and the "
                  "<b>stroma</b> of <b>dark reactions</b>."))
story.append(figure("fig_8_8.png", "Figure 8.8 Sectional view of chloroplast", ASSETS))
story.append(labels_line([
    "Outer membrane", "Inner membrane", "Granum", "Thylakoid", "Stroma lamella", "Stroma",
]))

# ---- 8.5.6 ---- Ribosomes  (F234-F242, Fig 8.9)
story.append(heading("8.5.6", "Ribosomes", level=2))
story.append(P("Ribosomes are the granular structures first observed under the electron "
               "microscope as dense particles by <b>George Palade (1953)</b>. They are composed "
               "of <b>ribonucleic acid (RNA)</b> and <b>proteins</b> and are <b>not surrounded by "
               "any membrane</b>."))
story.append(data_table([
    ["Ribosome", "Whole", "Larger subunit", "Smaller subunit"],
    ["Eukaryotic", "80S", "60S", "40S"],
    ["Prokaryotic", "70S", "50S", "30S"],
], col_widths=[1.2, 1, 1, 1]))
story.append(Spacer(1, 0.15 * cm))
story.append(P("The eukaryotic ribosomes are <b>80S</b> while the prokaryotic ribosomes are "
               "<b>70S</b>. Each ribosome has two subunits, larger and smaller subunits "
               "(Fig 8.9). <b>Both 70S and 80S ribosomes are composed of two subunits.</b>"))
story.append(keyterm("Here <b>'S' (Svedberg's Unit)</b> stands for the <b>sedimentation "
                     "coefficient</b>; it is <b>indirectly</b> a measure of density and size."))
story.append(figure("fig_8_9.png", "Figure 8.9 Ribosome", ASSETS))
story.append(labels_line(["Large subunit", "Small subunit"]))

# ---- 8.5.7 ---- Cytoskeleton  (F243-F244)
story.append(heading("8.5.7", "Cytoskeleton", level=2))
story.append(keyterm("An elaborate network of filamentous proteinaceous structures consisting of "
                     "<b>microtubules</b>, <b>microfilaments</b> and <b>intermediate filaments</b> "
                     "present in the cytoplasm is collectively referred to as the "
                     "<b>cytoskeleton</b>."))
story.append(P("The cytoskeleton in a cell are involved in many functions such as <b>mechanical "
               "support</b>, <b>motility</b>, <b>maintenance of the shape of the cell</b>."))

# ---- 8.5.8 ---- Cilia and Flagella  (F245-F258, Fig 8.10)
story.append(heading("8.5.8", "Cilia and Flagella", level=2))
story.append(keyterm("<b>Cilia</b> (sing.: cilium) and <b>flagella</b> (sing.: flagellum) are "
                     "hair-like outgrowths of the cell membrane."))
story.append(data_table([
    ["Structure", "What the source says"],
    ["Cilia",
     "Small structures which work like <b>oars</b>, causing the movement of either the cell or "
     "the surrounding fluid."],
    ["Flagella (eukaryotic)",
     "<b>Comparatively longer</b> and responsible for cell movement."],
    ["Flagella (prokaryotic)",
     "The prokaryotic bacteria <b>also</b> possess flagella but these are <b>structurally "
     "different</b> from that of the eukaryotic flagella."],
], col_widths=[1, 2.6]))
story.append(Spacer(1, 0.15 * cm))
story.append(P("The electron microscopic study of a cilium or the flagellum show that they are "
               "covered with plasma membrane."))
story.append(keyterm("Their core called the <b>axoneme</b>, possesses a number of microtubules "
                     "running parallel to the long axis."))
story.append(P("The axoneme <b>usually</b> has <b>nine doublets</b> of radially arranged "
               "<b>peripheral microtubules</b>, and a pair of <b>centrally located "
               "microtubules</b>. Such an arrangement of axonemal microtubules is referred to as "
               "the <b>9+2 array</b> (Figure 8.10)."))
story.append(P("The central tubules are connected by <b>bridges</b> and is also enclosed by a "
               "<b>central sheath</b>, which is connected to one of the tubules of each peripheral "
               "doublets by a <b>radial spoke</b>. Thus, there are <b>nine radial spokes</b>. The "
               "peripheral doublets are also interconnected by <b>linkers</b>."))
story.append(P("Both the cilium and flagellum emerge from centriole-like structure called the "
               "<b>basal bodies</b>."))
story.append(figure("fig_8_10.png",
                    "Figure 8.10 Section of cilia/flagella showing different parts : "
                    "(a) Electron micrograph (b) Diagrammatic representation of internal "
                    "structure. <b>Read part (b) by position and geometry, not by colour:</b> the "
                    "source draws the plasma membrane green, the central sheath red, the radial "
                    "spokes pale green and the peripheral doublets dark blue, and those colours "
                    "reduce to near-identical greys here. The <b>plasma membrane</b> is the "
                    "complete outermost ring; the <b>central sheath</b> is the broken arc "
                    "immediately surrounding the two central microtubules; the <b>radial spoke</b> "
                    "lines are the nine thin lines running from that sheath out to each peripheral "
                    "doublet; the <b>interdoublet bridge</b> is the short bar joining the two "
                    "central tubules; and the <b>peripheral microtubules (doublets)</b> are the "
                    "nine paired rings arranged around the inside of the membrane.",
                    ASSETS))
story.append(labels_line([
    "Plasma membrane", "Peripheral microtubules (doublets)", "Central sheath",
    "Interdoublet bridge", "Central microtuble", "Radial spoke",
]))
story.append(note("The label above is printed in the source as <b>Central microtuble</b>, missing "
                  "the second 'u'. The NCERT spelling is reproduced exactly as printed; the "
                  "running text uses the correct <b>central microtubule</b>."))

# ---- 8.5.9 ---- Centrosome and Centrioles  (F259-F266)
story.append(heading("8.5.9", "Centrosome and Centrioles", level=2))
story.append(keyterm("<b>Centrosome</b> is an organelle <b>usually</b> containing two cylindrical "
                     "structures called <b>centrioles</b>. They are surrounded by amorphous "
                     "<b>pericentriolar materials</b>."))
story.append(P("Both the centrioles in a centrosome lie <b>perpendicular to each other</b> in "
               "which each has an organisation like the <b>cartwheel</b>. They are made up of "
               "<b>nine evenly spaced peripheral fibrils</b> of <b>tubulin</b> protein. Each of "
               "the peripheral fibril is a <b>triplet</b>. The adjacent triplets are also "
               "linked."))
story.append(keyterm("The central part of the proximal region of the centriole is also "
                     "proteinaceous and called the <b>hub</b>, which is connected with tubules of "
                     "the peripheral triplets by <b>radial spokes</b> made of protein."))
story.append(P("The centrioles form the <b>basal body</b> of cilia or flagella, and <b>spindle "
               "fibres</b> that give rise to <b>spindle apparatus</b> during cell division in "
               "animal cells."))

# ---- 8.5.10 ---- Nucleus  (F267-F302, Figs 8.11-8.13, + F308 & F319 folded)
story.append(heading("8.5.10", "Nucleus", level=2))
story.append(P("Nucleus as a cell organelle was first described by <b>Robert Brown</b> as early "
               "as <b>1831</b>. Later the material of the nucleus stained by the basic dyes was "
               "given the name <b>chromatin</b> by <b>Flemming</b>."))
story.append(keyterm("The <b>interphase nucleus</b> (nucleus of a cell when it is not dividing) "
                     "has highly extended and elaborate nucleoprotein fibres called "
                     "<b>chromatin</b>, <b>nuclear matrix</b> and one or more spherical bodies "
                     "called <b>nucleoli</b> (sing.: nucleolus) (Figure 8.11)."))
story.append(P("Electron microscopy has revealed that the <b>nuclear envelope</b>, which consists "
               "of two parallel membranes with a space between <b>(10 to 50 nm)</b> called the "
               "<b>perinuclear space</b>, forms a barrier between the materials present inside "
               "the nucleus and that of the cytoplasm."))
story.append(B("- The <b>outer membrane usually</b> remains continuous with the endoplasmic "
               "reticulum and also bears ribosomes on it."))
story.append(B("- At a number of places the nuclear envelope is interrupted by minute "
               "<b>pores</b>, which are formed by the fusion of its two membranes."))
story.append(B("- These <b>nuclear pores</b> are the passages through which movement of RNA and "
               "protein molecules takes place in <b>both directions</b> between the nucleus and "
               "the cytoplasm."))
story.append(note("<b>From the printed summary (folded in here because the body never says it):</b> "
                  "The <b>inner membrane</b> encloses the nucleoplasm and the chromatin material. "
                  "The nucleus not only <b>controls the activities of organelles</b> but also "
                  "<b>plays a major role in heredity</b>."))
story.append(P("<b>Normally</b>, there is only one nucleus per cell, variations in the number of "
               "nuclei are also <b>frequently</b> observed. <i>Can you recollect names of "
               "organisms that have more than one nucleus per cell?</i>"))
story.append(P("<b>Some</b> mature cells even <b>lack nucleus</b>, e.g., <b>erythrocytes of many "
               "mammals</b> and <b>sieve tube cells of vascular plants</b>. <i>Would you consider "
               "these cells as 'living'?</i>"))
story.append(keyterm("The <b>nuclear matrix</b> or the <b>nucleoplasm</b> contains nucleolus and "
                     "chromatin."))
story.append(P("The <b>nucleoli</b> are spherical structures present in the nucleoplasm. The "
               "content of nucleolus is continuous with the rest of the nucleoplasm as it is "
               "<b>not a membrane bound structure</b>. It is a site for <b>active ribosomal RNA "
               "synthesis</b>. <b>Larger and more numerous</b> nucleoli are present in cells "
               "actively carrying out protein synthesis."))
story.append(figure("fig_8_11.png", "Figure 8.11 Structure of nucleus", ASSETS))
story.append(labels_line([
    "Nucleoplasm", "Nucleolus", "Nuclear pore", "Nuclear membrane",
]))

story.append(heading("8.5.10", "Chromatin and chromosomes", level=3))
story.append(P("The interphase nucleus has a <b>loose and indistinct network</b> of nucleoprotein "
               "fibres called <b>chromatin</b>. But during different stages of cell division, "
               "cells show <b>structured chromosomes</b> in place of the nucleus."))
story.append(P("Chromatin contains <b>DNA</b> and some basic proteins called <b>histones</b>, "
               "some <b>non-histone proteins</b> and also <b>RNA</b>. A single human cell has "
               "approximately <b>two metre long thread of DNA</b> distributed among its <b>forty "
               "six (twenty three pairs)</b> chromosomes. You will study the details of DNA "
               "packaging in the form of a chromosome in class XII."))
story.append(keyterm("Every chromosome (<b>visible only in dividing cells</b>) essentially has a "
                     "<b>primary constriction</b> or the <b>centromere</b> on the sides of which "
                     "disc shaped structures called <b>kinetochores</b> are present "
                     "(Figure 8.12). <b>Centromere holds two chromatids of a chromosome.</b>"))
story.append(figure("fig_8_12.png", "Figure 8.12 Chromosome with kinetochore", ASSETS))
story.append(labels_line(["Kinetochore"]))
story.append(P("Based on the position of the centromere, the chromosomes can be classified into "
               "<b>four types</b> (Figure 8.13)."))
story.append(data_table([
    ["Type of chromosome", "Position of the centromere and the arms it forms"],
    ["Metacentric",
     "Has <b>middle</b> centromere forming <b>two equal arms</b> of the chromosome."],
    ["Sub-metacentric",
     "Has centromere <b>slightly away from the middle</b> of the chromosome resulting into "
     "<b>one shorter arm</b> and <b>one longer arm</b>."],
    ["Acrocentric",
     "The centromere is situated <b>close to its end</b> forming <b>one extremely short</b> and "
     "<b>one very long arm</b>."],
    ["Telocentric", "Has a <b>terminal</b> centromere."],
], col_widths=[1, 2.6]))
story.append(Spacer(1, 0.15 * cm))
story.append(P("<b>Sometimes</b> a few chromosomes have <b>non-staining secondary "
               "constrictions</b> at a constant location. This gives the appearance of a small "
               "fragment called the <b>satellite</b>."))
story.append(figure("fig_8_13.png",
                    "Figure 8.13 Types of chromosomes based on the position of centromere",
                    ASSETS))
story.append(labels_line([
    "Satellite", "Secondary constriction", "Short arm", "Long arm", "Centromere",
]))

# ---- 8.5.11 ---- Microbodies  (F303)
story.append(heading("8.5.11", "Microbodies", level=2))
story.append(keyterm("<b>Many</b> membrane bound minute vesicles called <b>microbodies</b> that "
                     "contain various enzymes, are present in <b>both plant and animal cells</b>."))

# ---- R ---- Quick Recap (printed summary sentences already present in the body)
story.append(heading("R", "Quick Recap - the printed summary, sentence by sentence", level=1))
story.append(note("Every sentence below is reproduced from the chapter's own printed SUMMARY. The "
                  "sentences that add something the body never states have already been folded "
                  "into their named section above, so nothing here is a new fact."))
story.append(B("- All organisms are made of cells or aggregates of cells."))
story.append(B("- Based on the presence or absence of a membrane bound nucleus and other "
               "organelles, cells and hence organisms can be named as eukaryotic or prokaryotic."))
story.append(B("- A typical eukaryotic cell consists of a cell membrane, nucleus and cytoplasm."))
story.append(B("- Centrosome and centriole form the basal body of cilia and flagella that "
               "facilitate locomotion."))
story.append(B("- Nucleus contains nucleoli and chromatin network. It not only controls the "
               "activities of organelles but also plays a major role in heredity."))
story.append(B("- Endoplasmic reticulum contains tubules or cisternae. They are of two types: "
               "rough and smooth."))
story.append(B("- ER helps in the transport of substances, synthesis of proteins, lipoproteins "
               "and glycogen."))
story.append(B("- The golgi body is a membranous organelle composed of flattened sacs. The "
               "secretions of cells are packed in them and transported from the cell."))
story.append(B("- Lysosomes are single membrane structures containing enzymes for digestion of "
               "all types of macromolecules."))
story.append(B("- Ribosomes are involved in protein synthesis. These occur freely in the "
               "cytoplasm or are associated with ER."))
story.append(B("- Mitochondria help in oxidative phosphorylation and generation of adenosine "
               "triphosphate. They are bound by double membrane; the outer membrane is smooth and "
               "inner one folds into several cristae."))
story.append(B("- Plastids are pigment containing organelles found in plant cells. The grana, in "
               "the plastid, is the site of light reactions and the stroma of dark reactions."))
story.append(B("- The green coloured plastids are chloroplasts, which contain chlorophyll, "
               "whereas the other coloured plastids are chromoplasts, which may contain pigments "
               "like carotene and xanthophyll."))
story.append(B("- The inner membrane encloses the nucleoplasm and the chromatin material."))
story.append(B("- Thus, cell is the structural and functional unit of life."))
story.append(note("The summary's phrase 'found in plant cells <b>only</b>' is deliberately not "
                  "reproduced above. The chapter body states plastids are found in all plant cells "
                  "<b>and in euglenoides</b>, and the body's more specific statement is the one "
                  "kept - see section 8.5.5."))

# ---- E ---- Terms used in the exercises  (F321-F325 + the two exercise gaps)
story.append(heading("E", "Terms Used in the Exercises", level=1))
story.append(P("All 14 printed exercises were read against the chapter. Only the rows below "
               "needed anything the chapter body does not already supply, and each is closed "
               "using chapter facts alone."))
story.append(keyterm("<b>Q1 - which statement is not correct.</b> 'Robert Brown discovered the "
                     "cell' is the option that is <b>not</b> correct. Brown discovered the "
                     "<b>nucleus</b>, not the cell; <b>Antonie Von Leeuwenhoek</b> first saw and "
                     "described a live cell."))
story.append(keyterm("<b>Q3 - matching.</b> <b>Cristae</b> are the infoldings in mitochondria; "
                     "<b>Cisternae</b> are the disc-shaped sacs in Golgi apparatus; "
                     "<b>Thylakoids</b> are the flat membranous sacs in stroma."))
story.append(keyterm("<b>Q4 - correct option.</b> In prokaryotes, there are no membrane bound "
                     "organelles."))
story.append(keyterm("<b>Q7 - the two double-membrane-bound organelles</b> are the "
                     "<b>mitochondria</b> and the <b>chloroplast</b> (plastids). Figure 8.7 and "
                     "Figure 8.8 above are the two labelled diagrams the question asks for."))
story.append(note("<b>Q9 - 'Multicellular organisms have division of labour.'</b> The phrase "
                  "<b>division of labour</b> appears nowhere in this chapter's text, so it is "
                  "explained here from chapter facts only. A unicellular organism must perform "
                  "<b>all</b> the essential functions of life within its one cell, because it is "
                  "capable of (i) independent existence and (ii) performing the essential "
                  "functions of life. A multicellular organism is composed of <b>many</b> cells, "
                  "and the shape of the cell <b>may</b> vary with the function they perform - so "
                  "different cells take on different functions instead of each one doing "
                  "everything. That distribution of functions among cells is what the exercise "
                  "calls division of labour. No fact from outside the chapter is used."))
story.append(note("<b>Q13 - 'Describe the nucleus and centrosome with the help of labelled "
                  "diagrams.'</b> The nucleus half is answered by Figure 8.11 above. For the "
                  "centrosome, <b>NCERT prints no figure at all in this chapter</b>, and none is "
                  "invented here. Answer it in words from section 8.5.9: a centrosome usually "
                  "contains two cylindrical centrioles surrounded by amorphous pericentriolar "
                  "materials; the two centrioles lie perpendicular to each other; each has a "
                  "cartwheel organisation made of nine evenly spaced peripheral fibrils of tubulin "
                  "protein, each fibril a triplet with adjacent triplets linked; the proteinaceous "
                  "hub at the centre of the proximal region is joined to the peripheral triplets "
                  "by radial spokes."))
story.append(memory_aid("Double-membrane organelles worth remembering as a pair: "
                        "<b>mitochondrion</b> and <b>chloroplast</b> - both double membrane bound, "
                        "both carrying their own circular DNA and their own 70S ribosomes."))


if __name__ == "__main__":
    sys.exit(build_pdf(OUT_PDF, story,
                       title="Class 11 Chapter 8 - Cell: The Unit of Life (NEET notes)",
                       subject="NEET Biology"))
