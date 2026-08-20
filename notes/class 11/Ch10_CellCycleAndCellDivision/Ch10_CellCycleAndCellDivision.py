#!/usr/bin/env python3
"""
Class 11 Chapter 10 - Cell Cycle and Cell Division  ->  NEET replacement notes.

Built per SUPREME COMMAND PROMPT.md v6, normal-chapter 3-pass protocol.
Every style, colour, font and layout helper is imported from the repo-level
neet_template.py; nothing visual is re-declared here (v6 s0.6).

Content source of truth: Ch10_CellCycleAndCellDivision_inventory.md
(frozen 2026-08-20, F001-F167 facts + L01-L08 figure-label rows).
This script is one linear story.append(...) sequence with `# ---- N.N ----`
markers so a Pass 3 fix stays surgical.

Figures: the 8 verified monochrome assets in assets/ only. This chapter has no
scientist profile box and no photograph of any person, so v6 s4.4's hard no and
s5 item 3 are both satisfied trivially - nothing portrait-like was extracted.

Notation: phase names are written as the plain ASCII "G1", "S", "G2", "G0" and
DNA amounts as "2C"/"4C", chromosome sets as "2n"/"n" - v6 s4 bans Unicode
sub/superscript codepoints, and Times subscript tags would render below the
linter's legibility floor inside table cells.
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
OUT_PDF = os.path.join(HERE, "Ch10_CellCycleAndCellDivision.pdf")


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

    v6 s4.4 requires every in-figure label catalogued in the inventory
    (L01-L08) to appear in the running text, so a reader working from a bad
    photocopy of the diagram can still name every part. NCERT's own spelling of
    each label is preserved exactly - including Figure 10.3's "Metaphase 1" /
    "Anaphase 1" / "Telophase 1" with the digit 1, where the body text uses the
    roman "I" (Rule 4, and the source-spelling note in the inventory).
    """
    return P("<i>Labels printed in the figure:</i> " + "; ".join(labels))


story = []

# ---- Title block ----
story.extend(title_block("Cell Cycle and Cell Division"))
story.append(P("<i>Class 11 - Chapter 10 - NEET replacement notes built from the NCERT "
               "chapter text, its 4 figures (8 panels), its summary and its 16 exercises.</i>"))
story.append(Spacer(1, 0.18 * cm))

# ---- Chapter opener ---- (F001-F005)
story.append(P("Every organism, even the largest, starts its life from a <b>single cell</b>. "
               "Growth and reproduction are characteristics of cells, indeed of all living "
               "organisms. All cells reproduce by dividing into two, with each parental cell "
               "giving rise to two <b>daughter cells</b> each time they divide. These newly "
               "formed daughter cells can themselves grow and divide, giving rise to a new cell "
               "population formed by the growth and division of a single parental cell and its "
               "progeny. Such cycles of growth and division allow a single cell to form a "
               "structure consisting of millions of cells."))

# ---- 10.1 Cell Cycle ---- (F157-F159 summary-unique opener, F006-F013)
story.append(H("10.1", "Cell Cycle", 1,
               P("According to the <b>cell theory</b>, cells arise from preexisting cells. Any "
                 "sexually reproducing organism starts its life cycle from a single-celled "
                 "<b>zygote</b>. Cell division does not stop with the formation of the mature "
                 "organism but continues throughout its life cycle.")))
story.append(P("Cell division is a very important process in all living organisms. During the "
                "division of a cell, DNA replication and cell growth also take place. All these "
                "processes, i.e., cell division, DNA replication, and cell growth, hence, have to "
                "take place in a coordinated way to ensure correct division and formation of "
                "progeny cells containing intact genomes."))
story.append(keyterm("The <b>cell cycle</b> is the sequence of events by which a cell duplicates "
                     "its genome, synthesises the other constituents of the cell and eventually "
                     "divides into two daughter cells."))
story.append(P("Although cell growth (in terms of cytoplasmic increase) is a continuous process, "
               "DNA synthesis occurs <b>only</b> during one specific stage in the cell cycle. The "
               "replicated chromosomes (DNA) are then distributed to daughter nuclei by a complex "
               "series of events during cell division. These events are themselves under genetic "
               "control."))

# ---- 10.1.1 Phases of Cell Cycle ---- (F014-F045, F160-F162)
story.append(H("10.1.1", "Phases of Cell Cycle", 2,
               P("A typical eukaryotic cell cycle is illustrated by human cells in culture. These "
                 "cells divide once in approximately every <b>24 hours</b>. However, this duration "
                 "of cell cycle <b>can vary</b> from organism to organism and also from cell type "
                 "to cell type: yeast, for example, can progress through the cell cycle in only "
                 "about <b>90 minutes</b>.")))
story.append(P("The cell cycle is divided into two basic phases:"))
story.append(B("&bull; <b>Interphase</b> - the phase between two successive M phases."))
story.append(B("&bull; <b>M Phase (Mitosis phase)</b> - the phase when the actual cell division "
               "or mitosis occurs."))
story.append(P("In the 24 hour average duration of cell cycle of a human cell, cell division "
               "proper lasts for <b>only about an hour</b>, while the interphase lasts <b>more "
               "than 95%</b> of the duration of cell cycle."))
story.append(P("The M Phase starts with the nuclear division, corresponding to the separation of "
               "daughter chromosomes (<b>karyokinesis</b>), and <b>usually</b> ends with division "
               "of cytoplasm (<b>cytokinesis</b>)."))
story.append(P("The interphase, though called the <b>resting phase</b>, is the time during which "
               "the cell is preparing for division by undergoing both cell growth and DNA "
               "replication in an orderly manner. It is divided into three further phases:"))
story.append(data_table([
    ["Phase of interphase", "What defines it", "What happens in it"],
    ["<b>G1 phase</b> (Gap 1)",
     "The interval between mitosis and initiation of DNA replication.",
     "The cell is metabolically active and continuously grows but <b>does not</b> replicate its "
     "DNA. It is the period when the cell grows and carries out normal metabolism; most of the "
     "organelle duplication also occurs during this phase."],
    ["<b>S phase</b> (Synthesis)",
     "The period during which DNA synthesis or replication takes place; it marks DNA replication "
     "and chromosome duplication.",
     "The amount of DNA per cell doubles - if the initial amount of DNA is denoted as 2C then it "
     "increases to 4C. However, there is <b>no increase in the chromosome number</b>. In animal "
     "cells, DNA replication begins in the nucleus and the <b>centriole duplicates</b> in the "
     "cytoplasm."],
    ["<b>G2 phase</b> (Gap 2)",
     "The period of cytoplasmic growth, between S phase and mitosis.",
     "Proteins are synthesised in preparation for mitosis while cell growth continues."],
], col_widths=[1.5, 2.3, 4.2]))
story.append(note("The S phase doubles the DNA (2C to 4C) but not the chromosome number: if the "
                  "cell had diploid or 2n number of chromosomes at G1, even after S phase the "
                  "number of chromosomes remains the same, i.e., 2n. Each chromosome simply now "
                  "carries two chromatids instead of one."))
story.append(figure("fig_10_1.png",
                    "Fig. 10.1 - A diagrammatic view of cell cycle indicating formation of two "
                    "cells from one cell.", max_width_cm=10.4))
story.append(labels_line(["M Phase", "Cytokinesis", "Telophase", "Anaphase", "Metaphase",
                          "Prophase", "G1", "S", "G2", "G0"]))
story.append(P("The cycle runs continuously, one round feeding the next:"))
story.append(process_flow([
    "<b>G1</b> - cell grows, metabolises normally, duplicates most organelles; DNA is not yet "
    "replicated.",
    "<b>S</b> - DNA replication and chromosome duplication; DNA goes 2C to 4C, chromosome number "
    "stays 2n; in animal cells the centriole duplicates.",
    "<b>G2</b> - cytoplasmic growth continues and proteins are synthesised in preparation for "
    "mitosis.",
    "<b>M Phase</b> - karyokinesis through prophase, metaphase, anaphase and telophase, usually "
    "followed by cytokinesis, giving two daughter cells.",
], cyclic=True))
story.append(P("<b>Chromosome number and DNA content through the cycle</b> (the figures NCERT "
               "gives, collected in one place):"))
story.append(data_table([
    ["Stage", "Chromosome number", "DNA content"],
    ["At G1", "2n (diploid)", "2C"],
    ["After S phase", "2n - unchanged, no increase in chromosome number", "4C"],
    ["At G2", "2n", "4C"],
    ["After M phase (each daughter cell of mitosis)", "2n - the same as the parent, which is why "
     "mitosis is equational division", "2C"],
    ["At the end of meiosis II (each of the four cells)", "n (haploid) - reduced by half", "C"],
], col_widths=[2.6, 3.4, 1.6]))
story.append(note("Onion root tip cells have 16 chromosomes in each cell. The chromosome number "
                  "is therefore 16 at G1, 16 after S phase (S doubles DNA, not chromosome number) "
                  "and 16 after M phase. If the DNA content after M phase is 2C, then it is 2C at "
                  "G1, 4C after S phase and 4C at G2. NCERT poses exactly this question in the "
                  "text; the reasoning uses only the S-phase rule above."))
story.append(P("<b>Cells that stop dividing.</b> Some cells in the adult animals do not appear to "
               "exhibit division (e.g., <b>heart cells</b>). Many other cells divide <b>only "
               "occasionally</b>, as needed to replace cells that have been lost because of injury "
               "or cell death."))
story.append(keyterm("Cells that do not divide further exit G1 phase to enter an inactive stage "
                     "called <b>quiescent stage (G0)</b> of the cell cycle. Cells in this stage "
                     "remain metabolically active but no longer proliferate unless called on to do "
                     "so depending on the requirement of the organism."))
story.append(P("<b>Which cells divide by mitosis.</b> In animals, mitotic cell division is "
               "<b>only</b> seen in the diploid somatic cells. However, there are <b>few "
               "exceptions</b> to this where haploid cells divide by mitosis, for example, "
               "<b>male honey bees</b>. Against this, the plants can show mitotic divisions in "
               "<b>both</b> haploid and diploid cells."))
story.append(note("NCERT stops the reader three times inside this section to think, and each "
                  "question is answerable from the chapter itself. (i) How do plants and animals "
                  "continue to grow all their lives? Do all cells in a plant divide all the time? "
                  "Do you think all cells continue to divide in all plants and animals? Can you "
                  "tell the name and the location of tissues having cells that divide all their "
                  "life in higher plants? Do animals have similar meristematic tissues? - the "
                  "meristematic tissues, the apical and the lateral cambium, are the plant tissues "
                  "whose mitotic divisions continue lifelong (10.3), and heart cells and G0 cells "
                  "show that not all cells keep dividing. (ii) From your recollection of examples "
                  "of alternation of generations in plants (Chapter 3) identify plant species and "
                  "stages at which mitosis is seen in haploid cells - the chapter's own answer is "
                  "that plants can show mitotic divisions in both haploid and diploid cells. "
                  "(iii) You have studied mitosis in onion root tip cells. It has 16 chromosomes "
                  "in each cell. Can you tell how many chromosomes will the cell have at G1 phase, "
                  "after S phase, and after M phase? Also, what will be the DNA content of the "
                  "cells at G1, after S and at G2, if the content after M phase is 2C? - worked "
                  "out in the NOTE above."))

# ---- 10.2 M Phase ---- (F046-F050)
story.append(H("10.2", "M Phase (Mitosis) - Equational Division", 1,
               P("This is the most dramatic period of the cell cycle, involving a major "
                 "reorganisation of virtually all components of the cell. Since the number of "
                 "chromosomes in the parent and progeny cells is the same, it is also called as "
                 "<b>equational division</b>.")))
story.append(P("Though for convenience mitosis has been divided into four stages of nuclear "
               "division (karyokinesis), it is very essential to understand that cell division is "
               "a progressive process and very clear-cut lines <b>cannot</b> be drawn between "
               "various stages. Karyokinesis involves the following four stages:"))
story.append(process_flow([
    "<b>Prophase</b> - chromosomal material condenses into compact mitotic chromosomes; the "
    "mitotic apparatus is assembled.",
    "<b>Metaphase</b> - all the chromosomes come to lie at the equator on the metaphase plate.",
    "<b>Anaphase</b> - centromeres split and the daughter chromatids move to opposite poles.",
    "<b>Telophase</b> - chromosomes decondense at the poles and two daughter nuclei form.",
]))

# ---- 10.2.1 Prophase ---- (F051-F060, F163, F164)
story.append(H("10.2.1", "Prophase", 3,
               P("Prophase, which is the first stage of karyokinesis of mitosis, follows the S and "
                 "G2 phases of interphase. In the S and G2 phases, the new DNA molecules formed "
                 "are <b>not distinct but intertwined</b>. Prophase is marked by the initiation of "
                 "<b>condensation of chromosomal material</b>: the chromosomal material becomes "
                 "untangled during the process of chromatin condensation. The centrosome, which "
                 "had undergone duplication during S phase of interphase, now begins to move "
                 "towards opposite poles of the cell; simultaneously, the centrioles move to the "
                 "opposite poles.")))
story.append(P("<b>Key events of prophase:</b>"))
story.append(B("&bull; Chromosomal material condenses to form compact mitotic chromosomes."))
story.append(B("&bull; Chromosomes are seen to be composed of two chromatids attached together at "
               "the <b>centromere</b>."))
# [VERIFICATION FIX] Pass 3(b) DRIFTED -> F055/F058: NCERT's own key-event bullet opens
# "Centrosome which had undergone duplication during interphase, begins to move towards
# opposite poles of the cell." That clause was present only in the narrative paragraph
# above, not in this examinable bullet list. Restored verbatim in the bullet.
story.append(B("&bull; Centrosome which had undergone duplication <b>during interphase</b>, begins "
               "to move towards opposite poles of the cell. Each centrosome radiates out "
               "microtubules called <b>asters</b>."))
story.append(B("&bull; The two asters together with spindle fibres forms the <b>mitotic "
               "apparatus</b>."))
story.append(B("&bull; The nuclear envelope and the nucleolus disappear and the spindle fibres "
               "start appearing."))
story.append(P("Cells at the end of prophase, when viewed under the microscope, <b>do not</b> show "
               "golgi complexes, endoplasmic reticulum, nucleolus and the nuclear envelope."))
story.append(figure("fig_10_2a.png",
                    "Fig. 10.2 (a) - A diagrammatic view of stages in mitosis: early prophase and "
                    "late prophase.", max_width_cm=8.6))
story.append(labels_line(["Early Prophase", "Late Prophase"]))

# ---- 10.2.2 Metaphase ---- (F061-F071)
story.append(H("10.2.2", "Metaphase", 3,
               P("The complete disintegration of the nuclear envelope marks the start of the second "
                 "phase of mitosis, hence the chromosomes are spread through the cytoplasm of the "
                 "cell. By this stage, condensation of chromosomes is completed and they can be "
                 "observed clearly under the microscope. This then, is the stage at which "
                 "<b>morphology of chromosomes is most easily studied</b>.")))
story.append(P("At this stage, metaphase chromosome is made up of two <b>sister chromatids</b>, "
               "which are held together by the centromere."))
story.append(keyterm("Small disc-shaped structures at the surface of the centromeres are called "
                     "<b>kinetochores</b>. These structures serve as the sites of attachment of "
                     "spindle fibres to the chromosomes that are moved into position at the centre "
                     "of the cell."))
story.append(P("The metaphase is characterised by <b>all</b> the chromosomes coming to lie at the "
               "equator with one chromatid of each chromosome connected by its kinetochore to "
               "spindle fibres from one pole and its sister chromatid connected by its kinetochore "
               "to spindle fibres from the opposite pole. The plane of alignment of the "
               "chromosomes at metaphase is referred to as the <b>metaphase plate</b>."))
story.append(P("<b>Key events of metaphase:</b>"))
story.append(B("&bull; Spindle fibres attach to kinetochores of chromosomes."))
story.append(B("&bull; Chromosomes are moved to spindle equator and get aligned along metaphase "
               "plate through spindle fibres to both poles."))
story.append(figure("fig_10_2b.png",
                    "Fig. 10.2 (b) - A diagrammatic view of stages in mitosis: transition to "
                    "metaphase and metaphase.", max_width_cm=8.6))
story.append(labels_line(["Transition to Metaphase", "Metaphase"]))

# ---- 10.2.3 Anaphase ---- (F072-F076)
story.append(H("10.2.3", "Anaphase", 3,
               P("At the onset of anaphase, each chromosome arranged at the metaphase plate is "
                 "split <b>simultaneously</b> and the two daughter chromatids, now referred to as "
                 "<b>daughter chromosomes</b> of the future daughter nuclei, begin their migration "
                 "towards the two opposite poles.")))
story.append(P("As each chromosome moves away from the equatorial plate, the <b>centromere</b> of "
               "each chromosome remains directed towards the pole and hence at the leading edge, "
               "with the arms of the chromosome trailing behind."))
story.append(P("<b>Key events of anaphase:</b>"))
story.append(B("&bull; Centromeres split and chromatids separate."))
story.append(B("&bull; Chromatids move to opposite poles."))
story.append(figure("fig_10_2c.png",
                    "Fig. 10.2 (c) - A diagrammatic view of stages in Mitosis: anaphase.",
                    max_width_cm=8.0))
story.append(labels_line(["Anaphase"]))

# ---- 10.2.4 Telophase ---- (F077-F081, F165)
story.append(H("10.2.4", "Telophase", 3,
               P("At the beginning of the final stage of karyokinesis, i.e., telophase, the "
                 "chromosomes that have reached their respective poles <b>decondense and lose "
                 "their individuality</b>. The individual chromosomes can no longer be seen and "
                 "each set of chromatin material tends to collect at each of the two poles. Once "
                 "the chromatids reach the two poles, the chromosomal elongation starts, nucleolus "
                 "and the nuclear membrane reappear.")))
story.append(P("<b>Key events of telophase:</b>"))
story.append(B("&bull; Chromosomes cluster at opposite spindle poles and their identity is lost as "
               "discrete elements."))
story.append(B("&bull; Nuclear envelope develops around the chromosome clusters at each pole "
               "forming two daughter nuclei."))
story.append(B("&bull; Nucleolus, golgi complex and ER reform."))
story.append(figure("fig_10_2d.png",
                    "Fig. 10.2 (d) - A diagrammatic view of stages in Mitosis: telophase.",
                    max_width_cm=8.0))
story.append(labels_line(["Telophase"]))

# ---- 10.2.5 Cytokinesis ---- (F082-F089)
story.append(H("10.2.5", "Cytokinesis", 3,
               P("Mitosis accomplishes not only the segregation of duplicated chromosomes into "
                 "daughter nuclei (karyokinesis), but the cell itself is divided into two daughter "
                 "cells by the separation of cytoplasm called <b>cytokinesis</b>, at the end of "
                 "which cell division gets completed.")))
story.append(data_table([
    ["Cytokinesis in", "Mechanism", "Why"],
    ["Animal cell", "Achieved by the appearance of a <b>furrow</b> in the plasma membrane. The "
     "furrow gradually deepens and ultimately joins in the centre, dividing the cell cytoplasm "
     "into two.", "The plasma membrane can be pulled inward."],
    ["Plant cell", "Wall formation starts in the <b>centre</b> of the cell and grows <b>outward</b> "
     "to meet the existing lateral walls. The formation of the new cell wall begins with the "
     "formation of a simple precursor, called the <b>cell-plate</b>, that represents the middle "
     "lamella between the walls of two adjacent cells.",
     "Plant cells however, are enclosed by a relatively <b>inextensible cell wall</b>, therefore "
     "they undergo cytokinesis by a different mechanism."],
], col_widths=[1.3, 4.6, 2.1]))
story.append(P("At the time of cytoplasmic division, organelles like <b>mitochondria and "
               "plastids</b> get distributed between the two daughter cells."))
story.append(keyterm("In <b>some</b> organisms karyokinesis is not followed by cytokinesis, as a "
                     "result of which a multinucleate condition arises leading to the formation of "
                     "<b>syncytium</b> (e.g., liquid endosperm in coconut)."))
story.append(figure("fig_10_2e.png",
                    "Fig. 10.2 (e) - A diagrammatic view of stages in Mitosis: interphase, the "
                    "state the daughter cells return to once division is complete.",
                    max_width_cm=8.0))
story.append(labels_line(["Interphase"]))

# ---- 10.3 Significance of Mitosis ---- (F090-F099)
story.append(H("10.3", "Significance of Mitosis", 1,
               P("Mitosis or the equational division is <b>usually</b> restricted to the diploid "
                 "cells <b>only</b>. However, in <b>some</b> lower plants and in <b>some</b> social "
                 "insects haploid cells also divide by mitosis. It is very essential to understand "
                 "the significance of this division in the life of an organism. Mitosis "
                 "<b>usually</b> results in the production of diploid daughter cells with "
                 "identical genetic complement.")))
# [VERIFICATION FIX] Pass 3(b) MISSING -> 10.3: NCERT's linking sentence "It is very essential
# to understand the significance of this division in the life of an organism." was absent from
# this block; restored above, between F091 and F093, where NCERT places it.
story.append(P("NCERT asks here: are you aware of some examples where you have studied about "
               "haploid and diploid insects? The chapter's own example of a haploid animal cell "
               "dividing by mitosis is the <b>male honey bee</b> (10.1.1)."))
story.append(B("&bull; <b>Growth.</b> The growth of multicellular organisms is due to mitosis."))
story.append(B("&bull; <b>Restoring the nucleo-cytoplasmic ratio.</b> Cell growth results in "
               "disturbing the ratio between the nucleus and the cytoplasm. It therefore becomes "
               "essential for the cell to divide to restore the nucleo-cytoplasmic ratio."))
story.append(B("&bull; <b>Cell repair.</b> A very significant contribution of mitosis is cell "
               "repair. The cells of the upper layer of the epidermis, cells of the lining of the "
               "gut, and blood cells are being constantly replaced."))
story.append(B("&bull; <b>Continuous growth in plants.</b> Mitotic divisions in the meristematic "
               "tissues - the apical and the lateral cambium - result in a continuous growth of "
               "plants throughout their life."))

# ---- 10.4 Meiosis ---- (F100-F110, F166)
story.append(H("10.4", "Meiosis - Reduction Division", 1,
               P("The production of offspring by sexual reproduction includes the fusion of two "
                 "gametes, each with a complete <b>haploid</b> set of chromosomes. Gametes are "
                 "formed from specialised <b>diploid</b> cells.")))
story.append(keyterm("<b>Meiosis</b> is the specialised kind of cell division that reduces the "
                     "chromosome number by half and results in the production of haploid daughter "
                     "cells. It is called the <b>reduction division</b> since it reduces the "
                     "chromosome number by half while making the gametes."))
story.append(P("Meiosis ensures the production of the haploid phase in the life cycle of sexually "
               "reproducing organisms, whereas <b>fertilisation restores the diploid phase</b>. We "
               "come across meiosis during <b>gametogenesis</b> in plants and animals; this leads "
               "to the formation of haploid gametes."))
story.append(P("<b>Key features of meiosis:</b>"))
story.append(B("&bull; Meiosis involves two sequential cycles of nuclear and cell division called "
               "<b>meiosis I</b> and <b>meiosis II</b> but <b>only a single cycle</b> of DNA "
               "replication."))
story.append(B("&bull; Meiosis I is initiated after the parental chromosomes have replicated to "
               "produce identical sister chromatids at the S phase."))
story.append(B("&bull; Meiosis involves pairing of <b>homologous chromosomes</b> and "
               "<b>recombination</b> between non-sister chromatids of homologous chromosomes."))
story.append(B("&bull; <b>Four haploid cells</b> are formed at the end of meiosis II."))
story.append(P("Meiotic events can be grouped under the following phases:"))
story.append(data_table([
    ["Division", "Phases, in order"],
    ["<b>Meiosis I</b>", "Prophase I - Metaphase I - Anaphase I - Telophase I"],
    ["<b>Meiosis II</b>", "Prophase II - Metaphase II - Anaphase II - Telophase II"],
], col_widths=[1.4, 6.6]))
story.append(P("<b>Mitosis compared with meiosis</b> (every fact below is stated in 10.2-10.4; "
               "nothing new is added here):"))
story.append(data_table([
    ["Feature", "Mitosis", "Meiosis"],
    ["Also called", "Equational division", "Reduction division"],
    ["Cells in which it occurs", "Usually restricted to the diploid cells only; in some lower "
     "plants and some social insects haploid cells also divide by mitosis; in animals only in "
     "diploid somatic cells, except male honey bees",
     "Diploid cells destined to form gametes; met during gametogenesis in plants and animals"],
    ["Nuclear/cell division cycles", "One", "Two sequential cycles - meiosis I and meiosis II"],
    ["Cycles of DNA replication", "One", "Only a single cycle, before meiosis I"],
    ["Pairing of homologous chromosomes", "Does not occur", "Occurs (synapsis), forming bivalents"],
    ["Crossing over / recombination", "Does not occur", "Occurs between non-sister chromatids of "
     "homologous chromosomes"],
    ["What separates at anaphase", "Centromeres split and sister chromatids separate",
     "Anaphase I: homologous chromosomes separate while sister chromatids remain associated at "
     "their centromeres. Anaphase II: centromeres split and sister chromatids separate"],
    # [VERIFICATION FIX] Pass 3(b) DRIFTED -> F093: NCERT hedges this, "Mitosis <i>usually</i>
    # results in the production of diploid daughter cells with identical genetic complement",
    # and never prefixes it with the absolute "Two". The cell had smoothed the hedge into an
    # absolute - the exact qualifier-drift class v6 warns about. NCERT's "usually" restored.
    ["Products", "<b>Usually</b> diploid daughter cells with identical genetic complement",
     "Four haploid cells (a tetrad of cells)"],
    ["Chromosome number in products", "Same as the parent (2n from 2n)", "Half that of the parent "
     "(n from 2n)"],
], col_widths=[1.5, 2.6, 3.9]))

# ---- 10.4.1 Meiosis I ---- (F111-F143, F167)
story.append(H("10.4.1", "Meiosis I", 2,
               P("Prophase of the first meiotic division is typically <b>longer and more "
                 "complex</b> when compared to prophase of mitosis. It has been further subdivided "
                 "into the following five phases based on chromosomal behaviour, i.e., "
                 "<b>Leptotene, Zygotene, Pachytene, Diplotene</b> and <b>Diakinesis</b>.")))
story.append(process_flow([
    "<b>Leptotene</b> - the chromosomes become gradually visible under the light microscope. The "
    "compaction of chromosomes continues throughout leptotene.",
    "<b>Zygotene</b> - chromosomes start pairing together and this process of association is "
    "called <b>synapsis</b>. Such paired chromosomes are called <b>homologous chromosomes</b>. "
    "Electron micrographs of this stage indicate that chromosome synapsis is accompanied by the "
    "formation of a complex structure called the <b>synaptonemal complex</b>. The complex formed "
    "by a pair of synapsed homologous chromosomes is called a <b>bivalent</b> or a <b>tetrad</b>; "
    "however, these are more clearly visible at the next stage.",
    "<b>Pachytene</b> - the first two stages of prophase I are relatively short-lived compared to "
    "this stage. The four chromatids of each bivalent chromosome become distinct and clearly "
    "appear as tetrads. This stage is characterised by the appearance of <b>recombination "
    "nodules</b>, the sites at which crossing over occurs between non-sister chromatids of the "
    "homologous chromosomes. Recombination between homologous chromosomes is completed by the end "
    "of pachytene, leaving the chromosomes linked at the sites of crossing over.",
    "<b>Diplotene</b> - recognised by the dissolution of the synaptonemal complex and the tendency "
    "of the recombined homologous chromosomes of the bivalents to separate from each other "
    "<b>except</b> at the sites of crossovers. These X-shaped structures are called "
    "<b>chiasmata</b>. In oocytes of some vertebrates, diplotene can last for <b>months or "
    "years</b>.",
    "<b>Diakinesis</b> - the final stage of meiotic prophase I, marked by <b>terminalisation of "
    "chiasmata</b>. During this phase the chromosomes are fully condensed and the meiotic spindle "
    "is assembled to prepare the homologous chromosomes for separation. By the end of diakinesis, "
    "the nucleolus disappears and the nuclear envelope also breaks down. Diakinesis represents "
    "transition to metaphase.",
]))
story.append(keyterm("<b>Crossing over</b> is the exchange of genetic material between two "
                     "homologous chromosomes. It is also an enzyme-mediated process and the enzyme "
                     "involved is called <b>recombinase</b>. Crossing over leads to recombination "
                     "of genetic material on the two chromosomes."))
story.append(P("<b>Metaphase I.</b> The bivalent chromosomes align on the equatorial plate. The "
               "microtubules from the opposite poles of the spindle attach to the kinetochore of "
               "homologous chromosomes."))
story.append(P("<b>Anaphase I.</b> The homologous chromosomes separate, while <b>sister chromatids "
               "remain associated at their centromeres</b>. Homologous chromosomes move to the "
               "opposite poles with <b>both</b> their chromatids, so each pole receives half the "
               "chromosome number of the parent cell."))
story.append(P("<b>Telophase I.</b> The nuclear membrane and nucleolus reappear, cytokinesis "
               "follows and this is called as <b>dyad of cells</b>. Although in many cases the "
               "chromosomes do undergo some dispersion, they <b>do not</b> reach the extremely "
               "extended state of the interphase nucleus."))
story.append(keyterm("The stage between the two meiotic divisions is called <b>interkinesis</b> "
                     "and is generally short lived. There is <b>no replication of DNA</b> during "
                     "interkinesis. Interkinesis is followed by prophase II, a much simpler "
                     "prophase than prophase I."))
story.append(figure("fig_10_3.png", "Fig. 10.3 - Stages of Meiosis I.", max_width_cm=15.9))
story.append(labels_line(["Prophase I", "Metaphase 1", "Anaphase 1", "Telophase 1"]))

# ---- 10.4.2 Meiosis II ---- (F144-F152)
story.append(H("10.4.2", "Meiosis II", 2,
               P("<b>Prophase II.</b> Meiosis II is initiated immediately after cytokinesis, "
                 "<b>usually</b> before the chromosomes have fully elongated. In contrast to "
                 "meiosis I, <b>meiosis II resembles a normal mitosis</b>. The nuclear membrane "
                 "disappears by the end of prophase II and the chromosomes again become compact.")))
story.append(P("<b>Metaphase II.</b> At this stage, the chromosomes align at the equator and the "
               "microtubules from opposite poles of the spindle get attached to the kinetochores "
               "of <b>sister chromatids</b>."))
story.append(P("<b>Anaphase II.</b> It begins with the simultaneous splitting of the centromere of "
               "each chromosome (which was holding the sister chromatids together), allowing them "
               "to move toward opposite poles of the cell by <b>shortening of microtubules</b> "
               "attached to kinetochores."))
story.append(P("<b>Telophase II.</b> Meiosis ends with telophase II, in which the two groups of "
               "chromosomes once again get enclosed by a nuclear envelope; cytokinesis follows, "
               "resulting in the formation of a <b>tetrad of cells</b>, i.e., four haploid "
               "daughter cells."))
story.append(figure("fig_10_4.png", "Fig. 10.4 - Stages of Meiosis II.", max_width_cm=15.9))
story.append(labels_line(["Prophase II", "Metaphase II", "Anaphase II", "Telophase II"]))
story.append(memory_aid("Prophase I substages in order - <b>L</b>eptotene, <b>Z</b>ygotene, "
                        "<b>P</b>achytene, <b>D</b>iplotene, <b>D</b>iakinesis: read them as "
                        "\"<b>LZ PDD</b>\". The two D stages are the late ones, and the pairing "
                        "(Z for zygotene, Z for zip-up) comes before the crossing over "
                        "(P for pachytene)."))

# ---- 10.5 Significance of Meiosis ---- (F153-F156)
story.append(H("10.5", "Significance of Meiosis", 1,
               P("Meiosis is the mechanism by which <b>conservation of specific chromosome number "
                 "of each species</b> is achieved across generations in sexually reproducing "
                 "organisms, even though the process, per se, <b>paradoxically</b>, results in "
                 "reduction of chromosome number by half.")))
story.append(P("It also increases the <b>genetic variability</b> in the population of organisms "
               "from one generation to the next. Variations are very important for the process of "
               "<b>evolution</b>."))

# ---- Quick Recap ---- (rewritten, denser version of the NCERT summary)
story.append(H("QR", "Quick Recap", 1,
               P("Cells arise from preexisting cells (cell theory); a sexually reproducing "
                 "organism starts its life cycle from a single-celled zygote, and cell division "
                 "does not stop with the mature organism but continues throughout its life cycle. "
                 "The stages through which a cell passes from one division to the next is the cell "
                 "cycle.")))
story.append(B("&bull; <b>Two phases:</b> interphase - a period of preparation for cell division; "
               "and mitosis (M phase) - the actual period of cell division. Interphase is "
               "subdivided into G1, S and G2. G1: cell grows and carries out normal metabolism, "
               "most organelle duplication too. S: DNA replication and chromosome duplication "
               "(2C to 4C, chromosome number unchanged). G2: cytoplasmic growth, proteins for "
               "mitosis. Human cells in culture divide once in about 24 hours, of which division "
               "proper is only about an hour and interphase is more than 95%; yeast takes only "
               "about 90 minutes. Non-dividing cells rest in G0."))
story.append(B("&bull; <b>Mitosis</b> has four stages. Prophase: chromosome condensation, "
               "centrioles move to opposite poles, nuclear envelope and nucleolus disappear and "
               "spindle fibres start appearing. Metaphase: alignment of chromosomes at the "
               "equatorial plate (metaphase plate), kinetochores attached to spindle fibres. "
               "Anaphase: centromeres divide and the chromatids start moving towards the two "
               "opposite poles. Telophase: once the chromatids reach the two poles the chromosomal "
               "elongation starts, nucleolus and nuclear membrane reappear. Nuclear division is "
               "then followed by cytoplasmic division, cytokinesis - a furrow in animal cells, a "
               "cell-plate growing centre-outward in plant cells. Mitosis thus is the equational "
               "division in which the chromosome number of the parent is conserved in the daughter "
               "cell; it drives growth, restores the nucleo-cytoplasmic ratio and repairs tissue."))
story.append(B("&bull; <b>Meiosis</b>, in contrast, occurs in the diploid cells which are destined "
               "to form gametes. It is the reduction division: it halves the chromosome number "
               "while making the gametes, and fertilisation restores the parental value. Meiosis "
               "I has a long prophase of five substages - leptotene, zygotene, pachytene, "
               "diplotene, diakinesis - in which homologous chromosomes pair to form bivalents and "
               "undergo crossing over. Metaphase I: bivalents on the equatorial plate. Anaphase I: "
               "homologous chromosomes move to opposite poles with both their chromatids, so each "
               "pole receives half the parental chromosome number. Telophase I: nuclear membrane "
               "and nucleolus reappear. Meiosis II is similar to mitosis, and during anaphase II "
               "the sister chromatids separate. Thus at the end of meiosis four haploid cells are "
               "formed. Meiosis conserves each species' chromosome number across generations and "
               "increases genetic variability, which matters for evolution."))

# ---- Appendix ---- Terms used in the exercises (Rule 2)
story.append(H("EX", "Terms Used in the Exercises", 1,
               P("These are the points the end-of-chapter questions lean on that the chapter body "
                 "states in a scattered way, or does not state at all. Nothing here is imported "
                 "from outside this chapter; where the chapter genuinely does not supply an "
                 "answer, that is said plainly.")))
story.append(B("&bull; <b>\"Average cell cycle span for a mammalian cell\" (Q1).</b> The chapter "
               "never uses the word <i>mammalian</i>: it gives the figure for human cells in "
               "culture, which divide once in approximately every 24 hours, of which cell division "
               "proper lasts for only about an hour. That 24-hour figure is the average the "
               "question asks for."))
story.append(B("&bull; <b>Four daughter cells equal or unequal in size (Q9).</b> The chapter "
               "states that meiosis is met during gametogenesis in plants and animals and that "
               "cytokinesis after telophase II gives a tetrad of cells, i.e., four haploid "
               "daughter cells. It does <b>not</b> state their relative sizes anywhere, so the "
               "equal-versus-unequal comparison is beyond what this chapter supplies; answer it "
               "from the gametogenesis chapters rather than from here."))
story.append(B("&bull; <b>Haploid cells in higher plants where cell division does not occur "
               "(Q13 ii).</b> The chapter supplies the two halves of this discussion separately: "
               "cells that do not divide further exit G1 into the quiescent stage (G0), where they "
               "remain metabolically active but no longer proliferate unless called on to do so; "
               "and plants can show mitotic divisions in both haploid and diploid cells, with the "
               "haploid dividing stages to be identified from alternation of generations "
               "(Chapter 3). Haploid plant cells that are <b>not</b> dividing are therefore G0-type "
               "cells of the haploid generation; the chapter names no specific example."))
story.append(B("&bull; <b>\"Can there be mitosis without DNA replication in the S phase?\" "
               "(Q14).</b> No, as the chapter states the sequence: DNA synthesis occurs only "
               "during one specific stage of the cell cycle, the S phase, which marks DNA "
               "replication and chromosome duplication; and prophase, the first stage of "
               "karyokinesis of mitosis, follows the S and G2 phases of interphase. Mitosis "
               "distributes replicated chromosomes, so the replication must have happened first."))
story.append(B("&bull; <b>\"Can there be DNA replication without cell division?\" (Q15).</b> Yes. "
               "In some organisms karyokinesis is not followed by cytokinesis, giving a "
               "multinucleate condition and the formation of a syncytium, e.g., liquid endosperm "
               "in coconut. Note also that no DNA replication takes place during interkinesis, the "
               "stage between the two meiotic divisions."))
story.append(B("&bull; <b>Chromosome number (N) and DNA content (C) at every stage (Q16), and the "
               "mitosis-versus-meiosis differences (Q11).</b> Both are answered by the two tables "
               "in the body: the DNA-content table in 10.1.1 and the comparison table in 10.4. "
               "Neither adds a fact beyond 10.1.1-10.4."))


def main():
    return build_pdf(OUT_PDF, story,
                     title="Class 11 Chapter 10 - Cell Cycle and Cell Division (NEET notes)",
                     subject="NEET Biology")


if __name__ == "__main__":
    sys.exit(main())
