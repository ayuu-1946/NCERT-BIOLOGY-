"""Class 11 - Chapter 4: Animal Kingdom (NEET replacement notes).

Generated from the frozen 352-row inventory (Ch4_AnimalKingdom_inventory.md) under
SUPREME COMMAND PROMPT.md v6. All styles, geometry, badges, tables, figures and PDF
construction are imported from the repo-level frozen neet_template.py; nothing
style/geometry/font-level is re-declared here.

BIG CHAPTER (v6 §8). This file is built in two passes into ONE script:
  * Pass 2a  -> chapter intro, 4.1 (+4.1.1-4.1.6), 4.2 opener, 4.2.1-4.2.10
               (Porifera through Hemichordata, the non-chordates), Figs 4.1-4.15.
               Facts F001-F194, figure-label rows F343-F347, summary fold F350.
  * Pass 2b  -> 4.2.11 Chordata + the seven classes, TABLE 4.1, TABLE 4.2,
               Quick Recap, exercise-gap appendix. Facts F195-F349, F351-F352.
The seam below (### PASS 2b CONTINUES HERE ###) is where 2b appends; the two-pass
check_pdf.py gate is judged on the whole PDF after 2b.
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = HERE
while not os.path.exists(os.path.join(ROOT, "neet_template.py")):
    parent = os.path.dirname(ROOT)
    if parent == ROOT:
        raise RuntimeError("neet_template.py not found in any parent directory")
    ROOT = parent
sys.path.insert(0, ROOT)

from reportlab.platypus import Paragraph
from neet_template import (
    STYLES, heading, keyterm, process_flow, note, memory_aid,
    data_table, title_block, build_pdf,
)
from neet_template import figure as _shared_figure

ASSETS = os.path.join(HERE, "assets")
OUT_PDF = os.path.join(HERE, "Ch4_AnimalKingdom.pdf")


def figure(asset_name, caption_text, max_width_cm=15.9):
    return _shared_figure(asset_name, caption_text, ASSETS, max_width_cm=max_width_cm)


def body(text):
    return Paragraph(text, STYLES["Body"])


def b1(text):
    return Paragraph("&bull; " + text, STYLES["Bullet1"])


def b2(text):
    return Paragraph("- " + text, STYLES["Bullet2"])


story = []
story += title_block("Animal Kingdom")

# ---- 4.0 Chapter opening ----
story.append(heading("4", "Animal Kingdom", level=1))
story.append(body("When you look around, you will observe different animals with different "
                  "structures and forms. As over a <b>million species</b> of animals have been "
                  "described till now, the need for classification becomes all the more important. "
                  "The classification also helps in assigning a systematic position to newly "
                  "described species. This chapter runs in two parts: <b>4.1 Basis of "
                  "Classification</b> and <b>4.2 Classification of Animals</b>."))

# ---- 4.1 Basis of Classification ----
story.append(heading("4.1", "Basis of Classification", level=1))
story.append(body("Inspite of differences in structure and form of different animals, there are "
                  "fundamental features common to various individuals in relation to the "
                  "arrangement of cells, body symmetry, nature of coelom, and patterns of "
                  "digestive, circulatory or reproductive systems. These features are used as the "
                  "basis of animal classification and some of them are discussed here."))

# ---- 4.1.1 Levels of Organisation ----
story.append(heading("4.1.1", "Levels of Organisation", level=2))
story.append(body("Though all members of Animalia are multicellular, all of them do not exhibit "
                  "the same pattern of organisation of cells."))
story.append(b1("<b>Cellular level:</b> in sponges, the cells are arranged as loose cell "
                "aggregates. Some division of labour (activities) occurs among the cells."))
story.append(b1("<b>Tissue level:</b> in coelenterates, the arrangement of cells is more complex. "
                "Cells performing the same function are arranged into tissues."))
story.append(b1("<b>Organ level:</b> exhibited by Platyhelminthes and other higher phyla, where "
                "tissues are grouped together to form organs, each specialised for a particular "
                "function."))
story.append(b1("<b>Organ system level:</b> in Annelids, Arthropods, Molluscs, Echinoderms and "
                "Chordates, organs have associated to form functional systems, each system "
                "concerned with a specific physiological function."))
story.append(body("Organ systems in different groups of animals exhibit various patterns of "
                  "complexities. Two examples are the digestive and the circulatory systems:"))
story.append(b1("The <b>digestive system</b> in Platyhelminthes has only a single opening to the "
                "outside of the body that serves as both mouth and anus, and is hence called "
                "<b>incomplete</b>. A <b>complete</b> digestive system has two openings, mouth and "
                "anus."))
story.append(b1("The <b>circulatory system</b> is of two types: (i) <b>open type</b> in which the "
                "blood is pumped out of the heart and the cells and tissues are directly bathed in "
                "it; (ii) <b>closed type</b> in which the blood is circulated through a series of "
                "vessels of varying diameters (arteries, veins and capillaries)."))

# ---- 4.1.2 Symmetry ----
story.append(heading("4.1.2", "Symmetry", level=2))
story.append(body("Animals can be categorised on the basis of their symmetry."))
story.append(keyterm("<b>Asymmetry:</b> sponges are mostly asymmetrical, i.e., any plane that "
                     "passes through the centre does not divide them into equal halves."))
story.append(keyterm("<b>Radial symmetry:</b> when any plane passing through the central axis of "
                     "the body divides the organism into two identical halves. Coelenterates, "
                     "ctenophores and echinoderms have this kind of body plan (Figure 4.1a)."))
story.append(keyterm("<b>Bilateral symmetry:</b> animals like annelids, arthropods, etc., where "
                     "the body can be divided into identical left and right halves in only one "
                     "plane (Figure 4.1b)."))
story.append(figure("fig_4_1a.png", "<b>Fig. 4.1(a)</b> - Radial symmetry.", max_width_cm=6.0))
story.append(figure("fig_4_1b.png", "<b>Fig. 4.1(b)</b> - Bilateral symmetry.", max_width_cm=7.5))

# ---- 4.1.3 Diploblastic and Triploblastic Organisation ----
story.append(heading("4.1.3", "Diploblastic and Triploblastic Organisation", level=2))
story.append(b1("<b>Diploblastic animals:</b> those in which the cells are arranged in two "
                "embryonic layers, an external <b>ectoderm</b> and an internal <b>endoderm</b>, "
                "e.g., coelenterates. An undifferentiated layer, <b>mesoglea</b>, is present in "
                "between the ectoderm and the endoderm (Figure 4.2a)."))
story.append(b1("<b>Triploblastic animals:</b> those in which the developing embryo has a third "
                "germinal layer, <b>mesoderm</b>, in between the ectoderm and endoderm "
                "(platyhelminthes to chordates, Figure 4.2b)."))
story.append(figure("fig_4_2ab.png",
                    "<b>Fig. 4.2</b> - Showing germinal layers : (a) Diploblastic (b) Triploblastic. "
                    "Labels: Ectoderm, Mesoglea, Endoderm and Mesoderm.",
                    max_width_cm=11.0))

# ---- 4.1.4 Coelom ----
story.append(heading("4.1.4", "Coelom", level=2))
story.append(body("Presence or absence of a cavity between the body wall and the gut wall is very "
                  "important in classification. The body cavity, which is lined by mesoderm, is "
                  "called <b>coelom</b>."))
story.append(b1("<b>Coelomates:</b> animals possessing coelom, e.g., annelids, molluscs, "
                "arthropods, echinoderms, hemichordates and chordates (Figure 4.3a)."))
story.append(b1("<b>Pseudocoelomates:</b> in some animals the body cavity is not lined by "
                "mesoderm; instead the mesoderm is present as scattered pouches in between the "
                "ectoderm and endoderm. Such a body cavity is called <b>pseudocoelom</b>, e.g., "
                "aschelminthes (Figure 4.3b)."))
story.append(b1("<b>Acoelomates:</b> animals in which the body cavity is absent, e.g., "
                "platyhelminthes (Figure 4.3c)."))
story.append(figure("fig_4_3abc.png",
                    "<b>Fig. 4.3</b> - Diagrammatic sectional view of : (a) Coelomate "
                    "(b) Pseudocoelomate (c) Acoelomate. Labels: Coelom and Pseudocoelom.",
                    max_width_cm=11.5))

# ---- 4.1.5 Segmentation ----
story.append(heading("4.1.5", "Segmentation", level=2))
story.append(body("In some animals, the body is externally and internally divided into segments "
                  "with a serial repetition of at least some organs. For example, in earthworm, "
                  "the body shows this pattern called <b>metameric segmentation</b> and the "
                  "phenomenon is known as <b>metamerism</b>."))

# ---- 4.1.6 Notochord ----
story.append(heading("4.1.6", "Notochord", level=2))
story.append(body("<b>Notochord</b> is a mesodermally derived rod-like structure formed on the "
                  "dorsal side during embryonic development in some animals. Animals with "
                  "notochord are called <b>chordates</b> and those animals which do not form this "
                  "structure are called <b>non-chordates</b>, e.g., porifera to echinoderms."))

# ---- 4.2 Classification of Animals ----
story.append(heading("4.2", "Classification of Animals", level=1))
story.append(body("The broad classification of Animalia, based on common fundamental features as "
                  "mentioned in the preceding sections, is given in Figure 4.4. The important "
                  "characteristic features of the different phyla are described in the sections "
                  "that follow."))
story.append(b1("The classification chart branches the <b>Kingdom Animalia (multicellular)</b> by "
                "<b>Levels of Organisation</b>, then by <b>Symmetry</b>, and then by <b>Body "
                "Cavity or Coelom</b>, ending in the <b>Phylum</b> leaves. From the cellular "
                "level branch come <b>Porifera</b> (mostly asymmetrical). From the "
                "<b>Tissue/Organ/Organ system</b> levels branch, by <b>Radial</b> symmetry, come "
                "<b>Coelenterata (Cnidaria)</b> and <b>Ctenophora</b>."))
story.append(b1("Under <b>Bilateral</b> symmetry the animals are grouped by body cavity: "
                "<b>Without body cavity (acoelomates)</b> gives <b>Platyhelminthes</b>; "
                "<b>With false coelom (pseudocoelomates)</b> gives <b>Aschelminthes</b>; and "
                "<b>With true coelom (coelomates)</b> gives <b>Annelida</b>, <b>Arthropoda</b>, "
                "<b>Mollusca</b>, <b>Echinodermata</b>, <b>Hemichordata</b> and <b>Chordata</b>."))
story.append(figure("fig_4_4.png",
                    "<b>Fig. 4.4</b> - Broad classification of Kingdom Animalia based on common "
                    "fundamental features.",
                    max_width_cm=15.9))
story.append(note("Echinodermata exhibits radial or bilateral symmetry depending on the stage."))

# ---- 4.2.1 Phylum - Porifera ----
story.append(heading("4.2.1", "Phylum - Porifera", level=2))
story.append(b1("Members of this phylum are commonly known as <b>sponges</b>. They are generally "
                "marine and mostly asymmetrical animals (Figure 4.5). These are primitive "
                "multicellular animals and have <b>cellular level</b> of organisation."))
story.append(b1("Sponges have a <b>water transport or canal system</b>. This pathway of water "
                "transport is helpful in food gathering, respiratory exchange and removal of "
                "waste."))
story.append(process_flow([
    "Water enters through minute pores (<b>ostia</b>) in the body wall.",
    "It passes into a central cavity, the <b>spongocoel</b>.",
    "Water goes out through the <b>osculum</b>.",
]))
story.append(b1("<b>Choanocytes</b> or collar cells, which are flagellated, line the spongocoel "
                "and the canals. Digestion is <b>intracellular</b>. The body is supported by a "
                "skeleton made up of <b>spicules</b> or <b>spongin fibres</b>."))
story.append(b1("Sexes are not separate (<b>hermaphrodite</b>), i.e., eggs and sperms are produced "
                "by the same individual. Sponges reproduce asexually by fragmentation and sexually "
                "by formation of gametes. Fertilisation is internal and development is indirect, "
                "having a larval stage which is morphologically distinct from the adult."))
story.append(b1("<b>Examples:</b> <i>Sycon</i> (Scypha), <i>Spongilla</i> (Fresh water sponge) and "
                "<i>Euspongia</i> (Bath sponge)."))
story.append(figure("fig_4_5abc.png",
                    "<b>Fig. 4.5</b> - Examples of Porifera : (a) Sycon (b) Euspongia (c) Spongilla.",
                    max_width_cm=10.5))

# ---- 4.2.2 Phylum - Coelenterata (Cnidaria) ----
story.append(heading("4.2.2", "Phylum - Coelenterata (Cnidaria)", level=2))
story.append(b1("They are aquatic, mostly marine, sessile or free-swimming, radially symmetrical "
                "animals (Figure 4.6). The name cnidaria is derived from the <b>cnidoblasts</b> or "
                "cnidocytes (which contain the stinging capsules or <b>nematocysts</b>) present on "
                "the tentacles and the body. Cnidoblasts are used for anchorage, defense and for "
                "the capture of prey (Figure 4.7)."))
story.append(b1("Cnidarians exhibit <b>tissue level</b> of organisation and are <b>diploblastic</b>. "
                "They have a central <b>gastro-vascular cavity</b> with a single opening, mouth on "
                "hypostome. Digestion is extracellular and intracellular. Some cnidarians, e.g., "
                "corals, have a skeleton composed of calcium carbonate."))
story.append(b1("Cnidarians exhibit two basic body forms called <b>polyp</b> and <b>medusa</b> "
                "(Figure 4.6). The former is a sessile and cylindrical form like <i>Hydra</i>, "
                "<i>Adamsia</i>, etc., whereas the latter is umbrella-shaped and free-swimming like "
                "<i>Aurelia</i> or jelly fish."))
story.append(b1("Those cnidarians which exist in both forms exhibit <b>alternation of generations "
                "(Metagenesis)</b>, i.e., polyps produce medusae asexually and medusae form the "
                "polyps sexually (e.g., <i>Obelia</i>)."))
story.append(b1("<b>Examples:</b> <i>Physalia</i> (Portuguese man-of-war), <i>Adamsia</i> (Sea "
                "anemone), <i>Pennatula</i> (Sea-pen), <i>Gorgonia</i> (Sea-fan) and "
                "<i>Meandrina</i> (Brain coral)."))
story.append(figure("fig_4_6ab.png",
                    "<b>Fig. 4.6</b> - Examples of Coelenterata indicating outline of their body "
                    "form : (a) Aurelia (Medusa) (b) Adamsia (Polyp).",
                    max_width_cm=11.5))
story.append(figure("fig_4_7.png", "<b>Fig. 4.7</b> - Diagrammatic view of Cnidoblast.",
                    max_width_cm=5.0))

# ---- 4.2.3 Phylum - Ctenophora ----
story.append(heading("4.2.3", "Phylum - Ctenophora", level=2))
story.append(b1("Ctenophores, commonly known as <b>sea walnuts</b> or <b>comb jellies</b>, are "
                "exclusively marine, radially symmetrical, diploblastic organisms with tissue "
                "level of organisation. The body bears <b>eight external rows of ciliated comb "
                "plates</b>, which help in locomotion (Figure 4.8)."))
story.append(b1("Digestion is both extracellular and intracellular. <b>Bioluminescence</b> (the "
                "property of a living organism to emit light) is well-marked in ctenophores."))
story.append(b1("Sexes are not separate. Reproduction takes place only by sexual means. "
                "Fertilisation is external with indirect development."))
story.append(b1("<b>Examples:</b> <i>Pleurobrachia</i> and <i>Ctenoplana</i>."))
story.append(figure("fig_4_8.png", "<b>Fig. 4.8</b> - Example of Ctenophora (Pleurobrachia).",
                    max_width_cm=5.5))

# ---- 4.2.4 Phylum - Platyhelminthes ----
story.append(heading("4.2.4", "Phylum - Platyhelminthes", level=2))
story.append(b1("They have a dorso-ventrally flattened body, hence are called <b>flatworms</b> "
                "(Figure 4.9). These are mostly <b>endoparasites</b> found in animals including "
                "human beings. Flatworms are bilaterally symmetrical, triploblastic and "
                "<b>acoelomate</b> animals with organ level of organisation."))
story.append(b1("Hooks and suckers are present in the parasitic forms. Some of them absorb "
                "nutrients from the host directly through their body surface. Specialised cells "
                "called <b>flame cells</b> help in osmoregulation and excretion."))
story.append(b1("Sexes are not separate. Fertilisation is internal and development is through many "
                "larval stages. Some members like <i>Planaria</i> possess high regeneration "
                "capacity."))
story.append(b1("<b>Examples:</b> <i>Taenia</i> (Tapeworm), <i>Fasciola</i> (Liver fluke)."))
story.append(figure("fig_4_9ab.png",
                    "<b>Fig. 4.9</b> - Examples of Platyhelminthes : (a) Tape worm (b) Liver fluke.",
                    max_width_cm=11.0))

# ---- 4.2.5 Phylum - Aschelminthes ----
story.append(heading("4.2.5", "Phylum - Aschelminthes", level=2))
story.append(b1("The body of the aschelminthes is circular in cross-section, hence the name "
                "<b>roundworms</b> (Figure 4.10). They may be free-living, aquatic and terrestrial "
                "or parasitic in plants and animals. Roundworms have <b>organ-system level</b> of "
                "body organisation."))
story.append(b1("They are bilaterally symmetrical, triploblastic and <b>pseudocoelomate</b> "
                "animals. Alimentary canal is complete with a well-developed muscular pharynx. An "
                "excretory tube removes body wastes from the body cavity through the excretory "
                "pore."))
story.append(b1("Sexes are separate (<b>dioecious</b>), i.e., males and females are distinct. "
                "Often females are longer than males. Fertilisation is internal and development "
                "may be direct (the young ones resemble the adult) or indirect."))
story.append(b1("<b>Examples:</b> <i>Ascaris</i> (Roundworm), <i>Wuchereria</i> (Filaria worm), "
                "<i>Ancylostoma</i> (Hookworm)."))
story.append(figure("fig_4_10.png",
                    "<b>Fig. 4.10</b> - Example of Aschelminthes : Roundworm. Labels: Male and "
                    "Female.",
                    max_width_cm=6.5))

# ---- 4.2.6 Phylum - Annelida ----
story.append(heading("4.2.6", "Phylum - Annelida", level=2))
story.append(b1("They may be aquatic (marine and fresh water) or terrestrial; free-living, and "
                "sometimes parasitic. They exhibit organ-system level of body organisation and "
                "bilateral symmetry. They are triploblastic, <b>metamerically segmented</b> and "
                "coelomate animals."))
story.append(b1("Their body surface is distinctly marked out into segments or <b>metameres</b> "
                "and, hence, the phylum name Annelida (Latin, <i>annulus</i> : little ring) "
                "(Figure 4.11). They possess longitudinal and circular muscles which help in "
                "locomotion. Aquatic annelids like <i>Nereis</i> possess lateral appendages, "
                "<b>parapodia</b>, which help in swimming."))
story.append(b1("A <b>closed circulatory system</b> is present. <b>Nephridia</b> (sing. "
                "nephridium) help in osmoregulation and excretion. Neural system consists of "
                "paired ganglia (sing. ganglion) connected by lateral nerves to a double ventral "
                "nerve cord."))
story.append(b1("<i>Nereis</i>, an aquatic form, is dioecious, but earthworms and leeches are "
                "monoecious. Reproduction is sexual."))
story.append(b1("<b>Examples:</b> <i>Nereis</i>, <i>Pheretima</i> (Earthworm) and "
                "<i>Hirudinaria</i> (Blood sucking leech)."))
story.append(figure("fig_4_11ab.png",
                    "<b>Fig. 4.11</b> - Examples of Annelida : (a) Nereis (b) Hirudinaria.",
                    max_width_cm=9.0))

# ---- 4.2.7 Phylum - Arthropoda ----
story.append(heading("4.2.7", "Phylum - Arthropoda", level=2))
story.append(b1("This is the <b>largest phylum</b> of Animalia which includes insects. Over "
                "two-thirds of all named species on earth are arthropods (Figure 4.12). They have "
                "organ-system level of organisation."))
story.append(b1("They are bilaterally symmetrical, triploblastic, segmented and coelomate animals. "
                "The body of arthropods is covered by <b>chitinous exoskeleton</b>. The body "
                "consists of <b>head, thorax and abdomen</b>. They have jointed appendages "
                "(<i>arthros</i>-joint, <i>poda</i>-appendages)."))
story.append(b1("Respiratory organs are gills, book gills, book lungs or tracheal system. "
                "Circulatory system is of <b>open type</b>. Sensory organs like antennae, eyes "
                "(compound and simple), statocysts or balancing organs are present. Excretion "
                "takes place through <b>malpighian tubules</b>."))
story.append(b1("They are mostly dioecious. Fertilisation is usually internal. They are mostly "
                "oviparous. Development may be direct or indirect."))
story.append(b1("<b>Examples:</b> Economically important insects - <i>Apis</i> (Honey bee), "
                "<i>Bombyx</i> (Silkworm), <i>Laccifer</i> (Lac insect); Vectors - "
                "<i>Anopheles</i>, <i>Culex</i> and <i>Aedes</i> (Mosquitoes); Gregarious pest - "
                "<i>Locusta</i> (Locust); Living fossil - <i>Limulus</i> (King crab)."))
story.append(figure("fig_4_12abcd.png",
                    "<b>Fig. 4.12</b> - Examples of Arthropoda : (a) Locust (b) Butterfly "
                    "(c) Scorpion (d) Prawn.",
                    max_width_cm=11.0))

# ---- 4.2.8 Phylum - Mollusca ----
story.append(heading("4.2.8", "Phylum - Mollusca", level=2))
story.append(b1("This is the <b>second largest animal phylum</b> (Figure 4.13). Molluscs are "
                "terrestrial or aquatic (marine or fresh water) having an organ-system level of "
                "organisation. They are bilaterally symmetrical, triploblastic and coelomate "
                "animals."))
story.append(b1("Body is covered by a <b>calcareous shell</b> and is unsegmented with a distinct "
                "head, muscular foot and visceral hump. A soft and spongy layer of skin forms a "
                "<b>mantle</b> over the visceral hump. The space between the hump and the mantle is "
                "called the <b>mantle cavity</b> in which feather-like gills are present. They have "
                "respiratory and excretory functions."))
story.append(b1("The anterior head region has sensory tentacles. The mouth contains a file-like "
                "rasping organ for feeding, called <b>radula</b>. They are usually dioecious and "
                "oviparous with indirect development."))
story.append(b1("<b>Examples:</b> <i>Pila</i> (Apple snail), <i>Pinctada</i> (Pearl oyster), "
                "<i>Sepia</i> (Cuttlefish), <i>Loligo</i> (Squid), <i>Octopus</i> (Devil fish), "
                "<i>Aplysia</i> (Sea-hare), <i>Dentalium</i> (Tusk shell) and <i>Chaetopleura</i> "
                "(Chiton)."))
story.append(figure("fig_4_13ab.png",
                    "<b>Fig. 4.13</b> - Examples of Mollusca : (a) Pila (b) Octopus.",
                    max_width_cm=9.0))

# ---- 4.2.9 Phylum - Echinodermata ----
story.append(heading("4.2.9", "Phylum - Echinodermata", level=2))
story.append(b1("These animals have an endoskeleton of <b>calcareous ossicles</b> and, hence, the "
                "name Echinodermata (Spiny bodied, Figure 4.14). All are marine with organ-system "
                "level of organisation."))
story.append(b1("The adult echinoderms are radially symmetrical but larvae are bilaterally "
                "symmetrical. They are triploblastic and coelomate animals. Digestive system is "
                "complete with mouth on the lower (ventral) side and anus on the upper (dorsal) "
                "side."))
story.append(b1("The most distinctive feature of echinoderms is the presence of <b>water vascular "
                "system</b> which helps in locomotion, capture and transport of food and "
                "respiration. An excretory system is absent."))
story.append(b1("Sexes are separate. Reproduction is sexual. Fertilisation is usually external. "
                "Development is indirect with free-swimming larva."))
story.append(b1("<b>Examples:</b> <i>Asterias</i> (Star fish), <i>Echinus</i> (Sea urchin), "
                "<i>Antedon</i> (Sea lily), <i>Cucumaria</i> (Sea cucumber) and <i>Ophiura</i> "
                "(Brittle star)."))
story.append(figure("fig_4_14ab.png",
                    "<b>Fig. 4.14</b> - Examples of Echinodermata : (a) Asterias (b) Ophiura.",
                    max_width_cm=9.0))

# ---- 4.2.10 Phylum - Hemichordata ----
story.append(heading("4.2.10", "Phylum - Hemichordata", level=2))
story.append(b1("Hemichordata was earlier considered as a sub-phylum under phylum Chordata. But "
                "now it is placed as a separate phylum under non-chordata. Hemichordates have a "
                "rudimentary structure in the collar region called <b>stomochord</b>, a structure "
                "similar to notochord."))
story.append(b1("This phylum consists of a small group of worm-like marine animals with "
                "organ-system level of organisation. They are bilaterally symmetrical, "
                "triploblastic and coelomate animals. The body is cylindrical and is composed of "
                "an anterior <b>proboscis</b>, a <b>collar</b> and a long <b>trunk</b> "
                "(Figure 4.15)."))
story.append(b1("Circulatory system is of open type. Respiration takes place through gills. "
                "Excretory organ is <b>proboscis gland</b>. Sexes are separate. Fertilisation is "
                "external. Development is indirect."))
story.append(b1("<b>Examples:</b> <i>Balanoglossus</i> and <i>Saccoglossus</i>."))
story.append(figure("fig_4_15.png",
                    "<b>Fig. 4.15</b> - Balanoglossus. Labels: Proboscis, Collar and Trunk.",
                    max_width_cm=6.0))

# ############################################################################
# ### PASS 2b CONTINUES HERE ###
# 4.2.11 Chordata + the seven classes, TABLE 4.1, TABLE 4.2, Quick Recap,
# exercise-gap appendix. Facts F195-F349 (minus the 1a figure rows) and the
# summary folds F351-F352. Do not regenerate the 2a blocks above; append only.
# ############################################################################


def main():
    return build_pdf(OUT_PDF, story,
                     title="Class 11 Chapter 4 - Animal Kingdom (NEET notes)",
                     subject="NEET Biology")


if __name__ == "__main__":
    sys.exit(main())
