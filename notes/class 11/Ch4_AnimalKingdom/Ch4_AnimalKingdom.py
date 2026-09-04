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

from reportlab.platypus import Paragraph, Image, Table, TableStyle, KeepTogether, PageBreak
from reportlab.lib.units import cm
from neet_template import (
    STYLES, heading, keyterm, process_flow, note, memory_aid,
    data_table, title_block, build_pdf, FRAME_WIDTH, GRID_LINE,
)
from neet_template import figure as _shared_figure

ASSETS = os.path.join(HERE, "assets")
OUT_PDF = os.path.join(HERE, "Ch4_AnimalKingdom.pdf")


def figure(asset_name, caption_text, max_width_cm=15.9):
    from PIL import Image as PILImage
    path = os.path.join(ASSETS, asset_name)
    try:
        with PILImage.open(path) as im:
            px_w, px_h = im.size
            mode = im.mode
    except Exception as exc:
        raise RuntimeError(f"CANNOT READ FIGURE ASSET {path}: {exc}")
    if mode != "L":
        raise RuntimeError(
            f"FIGURE NOT MONOCHROME: {asset_name} has mode {mode!r}, expected 'L'. "
            f"Run convert_figures_mono.py before building (§4.4 Step 2).")

    width = min(max_width_cm * cm, FRAME_WIDTH)
    height = width * px_h / px_w
    img = Image(path, width=width, height=height)

    framed = Table([[img]], colWidths=[width + 10])
    framed.setStyle(TableStyle([
        ("BOX", (0, 0), (-1, -1), 0.5, GRID_LINE),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    framed.hAlign = "CENTER"
    return KeepTogether([framed, Paragraph(caption_text, STYLES["Caption"])])


def _framed_image(asset_name, width_cm):
    """Frame a single figure at an exact rendered width (cm), same box styling as
    the shared figure() helper. Returns (framed_flowable, framed_outer_width_pt)."""
    from PIL import Image as PILImage
    path = os.path.join(ASSETS, asset_name)
    with PILImage.open(path) as im:
        px_w, px_h = im.size
    width = width_cm * cm
    height = width * px_h / px_w
    img = Image(path, width=width, height=height)
    framed = Table([[img]], colWidths=[width + 10])
    framed.setStyle(TableStyle([
        ("BOX", (0, 0), (-1, -1), 0.5, GRID_LINE),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    return framed, width + 10


def figure_row(specs, cell_pad=6):
    """Place several figures side by side in one row, each with its own caption
    stacked beneath it. `specs` is a list of (asset_name, caption_text, width_cm).
    The whole row is kept together across page breaks."""
    cells, colwidths = [], []
    for asset_name, caption_text, width_cm in specs:
        framed, outer_w = _framed_image(asset_name, width_cm)
        cells.append([framed, Paragraph(caption_text, STYLES["Caption"])])
        colwidths.append(outer_w + 2 * cell_pad)
    row = Table([cells], colWidths=colwidths)
    row.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("LEFTPADDING", (0, 0), (-1, -1), cell_pad),
        ("RIGHTPADDING", (0, 0), (-1, -1), cell_pad),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))
    row.hAlign = "CENTER"
    return KeepTogether(row)


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
story.append(figure_row([
    ("fig_4_1a.png", "<b>Fig. 4.1(a)</b> - Radial symmetry.", 5.5),
    ("fig_4_1b.png", "<b>Fig. 4.1(b)</b> - Bilateral symmetry.", 5.5),
]))

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
                    max_width_cm=6.5))

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
                    max_width_cm=5.76))

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
                    max_width_cm=11.48))
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
                    max_width_cm=6.0))

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
story.append(figure_row([
    ("fig_4_6ab.png",
     "<b>Fig. 4.6</b> - Examples of Coelenterata indicating outline of their body "
     "form : (a) Aurelia (Medusa) (b) Adamsia (Polyp).", 8.5),
    ("fig_4_7.png", "<b>Fig. 4.7</b> - Diagrammatic view of Cnidoblast.", 3.2),
]))

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
                    max_width_cm=4.0))

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
                    max_width_cm=8.0))

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
                    max_width_cm=4.8))

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
                    max_width_cm=5.2))

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
                    max_width_cm=6.93))

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
                    max_width_cm=7.97))

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
                    max_width_cm=4.65))

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
                    max_width_cm=5.17))

# ############################################################################
# ### PASS 2b CONTINUES HERE ###
# 4.2.11 Chordata + the seven classes, TABLE 4.1, TABLE 4.2, Quick Recap,
# exercise-gap appendix. Facts F195-F349 (minus the 1a figure rows) and the
# summary folds F351-F352. Do not regenerate the 2a blocks above; append only.
# ############################################################################

# ---- 4.2.11 Phylum - Chordata ----
story.append(heading("4.2.11", "Phylum - Chordata", level=2))
story.append(b1("Animals belonging to phylum Chordata are fundamentally characterised by the "
                "presence of a <b>notochord</b>, a <b>dorsal hollow nerve cord</b> and "
                "<b>paired pharyngeal gill slits</b> (Figure 4.16)."))
story.append(b1("These are bilaterally symmetrical, triploblastic, coelomate with organ-system "
                "level of organisation."))
story.append(b1("They possess a <b>post-anal part</b> (tail) and a <b>closed circulatory "
                "system</b>. Table 4.1 presents a comparison of salient features of chordates "
                "and non-chordates."))
story.append(figure("fig_4_16.png",
                    "<b>Fig. 4.16</b> - Chordata characteristics. Labels: Nerve cord, "
                    "Notochord, Post-anal part and Gill slits.",
                    max_width_cm=11.30))
story.append(b1("Phylum Chordata is divided into three subphyla: <b>Urochordata</b> or "
                "Tunicata, <b>Cephalochordata</b> and <b>Vertebrata</b>."))
story.append(b1("Subphyla Urochordata and Cephalochordata are often referred to as "
                "<b>protochordates</b> (Figure 4.17) and are exclusively marine. In Urochordata, "
                "notochord is present only in the larval tail, while in Cephalochordata it "
                "extends from head to tail region and is persistent throughout their life."))
story.append(b1("<b>Examples:</b> Urochordata - <i>Ascidia</i>, <i>Salpa</i>, <i>Doliolum</i>; "
                "Cephalochordata - <i>Branchiostoma</i> (Amphioxus or Lancelet)."))
story.append(figure("fig_4_17.png",
                    "<b>Fig. 4.17</b> - Ascidia (a urochordate protochordate).",
                    max_width_cm=4.37))
story.append(b1("The members of subphylum Vertebrata possess notochord during the embryonic "
                "period. The notochord is replaced by a cartilaginous or bony vertebral column "
                "in the adult. Thus <b>all vertebrates are chordates but all chordates are not "
                "vertebrates</b>."))
story.append(b1("Besides the basic chordate characters, vertebrates have a ventral muscular "
                "heart with two, three or four chambers, kidneys for excretion and "
                "osmoregulation and paired appendages which may be fins or limbs."))

# TABLE 4.1 — kept on a single page (label + full table never split)
story.append(KeepTogether([
    body("<b>TABLE 4.1</b> Comparison of Chordates and Non-chordates"),
    data_table([
        ["Chordates", "Non-chordates"],
        ["Notochord present.", "Notochord absent."],
        ["Central nervous system is dorsal, hollow and single.",
         "Central nervous system is ventral, solid and double."],
        ["Pharynx perforated by gill slits.", "Gill slits are absent."],
        ["Heart is ventral.", "Heart is dorsal (if present)."],
        ["A post-anal part (tail) is present.", "Post-anal tail is absent."],
    ], col_widths=[1, 1]),
]))

# Vertebrata classification chart
story.append(body("<b>The subphylum Vertebrata is further divided as follows:</b>"))
story.append(b1("Subphylum <b>Vertebrata</b> is split into two divisions on the basis of jaws: "
                "<b>Division Agnatha (lacks jaw)</b> and <b>Division Gnathostomata (bears "
                "jaw)</b>."))
story.append(b2("Division Agnatha (lacks jaw) includes a single Class - <b>Cyclostomata</b>."))
story.append(b2("Division Gnathostomata (bears jaw) is divided into two super classes: "
                "<b>Super Class Pisces (bear fins)</b> and <b>Super Class Tetrapoda (bear "
                "limbs)</b>."))
story.append(b2("Super Class Pisces (bear fins): Classes <b>Chondrichthyes</b> and "
                "<b>Osteichthyes</b>."))
story.append(b2("Super Class Tetrapoda (bear limbs): Classes <b>Amphibia</b>, <b>Reptilia</b>, "
                "<b>Aves</b> and <b>Mammals</b>."))
story.append(figure("fig_vertebrata_chart.png",
                    "Classification chart of subphylum Vertebrata - Divisions Agnatha and "
                    "Gnathostomata; Super Class Pisces and Tetrapoda; Classes Cyclostomata, "
                    "Chondrichthyes, Osteichthyes, Amphibia, Reptilia, Aves and Mammals.",
                    max_width_cm=14.85))

# ---- 4.2.11.1 Class - Cyclostomata ----
# Whole section (heading -> Fig. 4.18) kept together so the figure never
# splits away from the Cyclostomata text onto the next page.
story.append(KeepTogether([
    heading("4.2.11.1", "Class - Cyclostomata", level=3),
    b1("All living members of the class Cyclostomata are ectoparasites on some fishes. "
       "They are the <b>most primitive chordates</b>."),
    b1("They have an elongated body bearing <b>6-15 pairs of gill slits</b> for "
       "respiration. Cyclostomes have a sucking and circular mouth without jaws "
       "(Fig. 4.18)."),
    b1("Their body is devoid of scales and paired fins. Cranium and vertebral column "
       "are cartilaginous. Circulation is of closed type."),
    b1("Cyclostomes are marine but migrate for spawning to fresh water. After "
       "spawning, within a few days, they die. Their larvae, after metamorphosis, "
       "return to the ocean."),
    b1("<b>Examples:</b> <i>Petromyzon</i> (Lamprey) and <i>Myxine</i> (Hagfish)."),
    figure("fig_4_18.png",
           "<b>Fig. 4.18</b> - A jawless vertebrate : Petromyzon.",
           max_width_cm=14.59),
]))

# ---- 4.2.11.2 Class - Chondrichthyes ----
story.append(heading("4.2.11.2", "Class - Chondrichthyes", level=3))
story.append(b1("They are marine animals with streamlined body and have <b>cartilaginous "
                "endoskeleton</b> (Figure 4.19). Mouth is located ventrally. Notochord is "
                "persistent throughout life."))
story.append(b1("Gill slits are separate and without operculum (gill cover). The skin is tough, "
                "containing minute <b>placoid scales</b>. Teeth are modified placoid scales "
                "which are backwardly directed. Their jaws are very powerful."))
story.append(b1("These animals are predaceous. Due to the absence of <b>air bladder</b>, they "
                "have to swim constantly to avoid sinking. Heart is two-chambered (one auricle "
                "and one ventricle)."))
story.append(b1("Some of them have electric organs (e.g., <i>Torpedo</i>) and some possess "
                "poison sting (e.g., <i>Trygon</i>). They are <b>cold-blooded "
                "(poikilothermous)</b> animals, i.e., they lack the capacity to regulate their "
                "body temperature."))
story.append(b1("Sexes are separate. In males pelvic fins bear <b>claspers</b>. They have "
                "internal fertilisation and many of them are viviparous."))
story.append(b1("<b>Examples:</b> <i>Scoliodon</i> (Dog fish), <i>Pristis</i> (Saw fish), "
                "<i>Carcharodon</i> (Great white shark), <i>Trygon</i> (Sting ray)."))
story.append(figure("fig_4_19ab.png",
                    "<b>Fig. 4.19</b> - Cartilaginous fishes : (a) Scoliodon (b) Pristis.",
                    max_width_cm=7.14))

# ---- 4.2.11.3 Class - Osteichthyes ----
story.append(heading("4.2.11.3", "Class - Osteichthyes", level=3))
story.append(b1("It includes both marine and fresh water fishes with <b>bony endoskeleton</b>. "
                "Their body is streamlined. Mouth is mostly terminal (Figure 4.20)."))
story.append(b1("They have four pairs of gills which are covered by an <b>operculum</b> on each "
                "side. Skin is covered with cycloid/ctenoid scales. <b>Air bladder</b> is "
                "present which regulates buoyancy."))
story.append(b1("Heart is two-chambered (one auricle and one ventricle). They are cold-blooded "
                "animals. Sexes are separate. Fertilisation is usually external. They are mostly "
                "oviparous and development is direct."))
story.append(b1("<b>Examples:</b> Marine - <i>Exocoetus</i> (Flying fish), <i>Hippocampus</i> "
                "(Sea horse); Freshwater - <i>Labeo</i> (Rohu), <i>Catla</i> (Katla), "
                "<i>Clarias</i> (Magur); Aquarium - <i>Betta</i> (Fighting fish), "
                "<i>Pterophyllum</i> (Angel fish)."))
story.append(figure("fig_4_20ab.png",
                    "<b>Fig. 4.20</b> - Bony fishes : (a) Hippocampus (b) Catla.",
                    max_width_cm=5.3))

# ---- 4.2.11.4 Class - Amphibia ----
story.append(heading("4.2.11.4", "Class - Amphibia", level=3))
story.append(b1("As the name indicates (Gr., <i>Amphi</i> : dual, <i>bios</i>, life), "
                "amphibians can live in aquatic as well as terrestrial habitats (Figure 4.21). "
                "Most of them have two pairs of limbs. Body is divisible into head and trunk. "
                "Tail may be present in some."))
story.append(b1("The amphibian skin is moist (without scales). The eyes have eyelids. A "
                "<b>tympanum</b> represents the ear. Alimentary canal, urinary and reproductive "
                "tracts open into a common chamber called <b>cloaca</b> which opens to the "
                "exterior."))
story.append(b1("Respiration is by gills, lungs and through skin. The heart is three-chambered "
                "(two auricles and one ventricle). These are cold-blooded animals."))
story.append(b1("Sexes are separate. Fertilisation is external. They are oviparous and "
                "development is indirect."))
story.append(b1("<b>Examples:</b> <i>Bufo</i> (Toad), <i>Rana</i> (Frog), <i>Hyla</i> (Tree "
                "frog), <i>Salamandra</i> (Salamander), <i>Ichthyophis</i> (Limbless "
                "amphibia)."))
story.append(figure("fig_4_21ab.png",
                    "<b>Fig. 4.21</b> - Examples of Amphibia : (a) Salamandra (b) Rana.",
                    max_width_cm=5.09))

# ---- 4.2.11.5 Class - Reptilia ----
story.append(heading("4.2.11.5", "Class - Reptilia", level=3))
story.append(b1("The class name refers to their creeping or crawling mode of locomotion (Latin, "
                "<i>repere</i> or <i>reptum</i>, to creep or crawl). They are mostly terrestrial "
                "animals and their body is covered by dry and cornified skin, epidermal scales "
                "or scutes (Fig. 4.22)."))
story.append(b1("They do not have external ear openings. Tympanum represents ear. Limbs, when "
                "present, are two pairs; <b>limbs are absent in snakes</b>."))
story.append(b1("Heart is usually three-chambered, but <b>four-chambered in crocodiles</b>. "
                "Reptiles are poikilotherms. Snakes and lizards shed their scales as skin cast."))
story.append(b1("Sexes are separate. Fertilisation is internal. They are oviparous and "
                "development is direct."))
story.append(b1("<b>Examples:</b> <i>Chelone</i> (Turtle), <i>Testudo</i> (Tortoise), "
                "<i>Chameleon</i> (Tree lizard), <i>Calotes</i> (Garden lizard), "
                "<i>Crocodilus</i> (Crocodile), <i>Alligator</i> (Alligator), "
                "<i>Hemidactylus</i> (Wall lizard); Poisonous snakes - <i>Naja</i> (Cobra), "
                "<i>Bangarus</i> (Krait), <i>Vipera</i> (Viper)."))
story.append(figure("fig_4_22abcd.png",
                    "<b>Fig. 4.22</b> - Reptiles : (a) Chameleon (b) Crocodilus (c) Chelone "
                    "(d) Naja.",
                    max_width_cm=11.10))

# ---- 4.2.11.6 Class - Aves ----
story.append(heading("4.2.11.6", "Class - Aves", level=3))
story.append(b1("The characteristic features of Aves (birds) are the presence of <b>feathers</b> "
                "and most of them can fly except flightless birds (e.g., Ostrich). They possess "
                "<b>beak</b> (Figure 4.23)."))
story.append(b1("The forelimbs are modified into <b>wings</b>. The hind limbs generally have "
                "scales and are modified for walking, swimming or clasping the tree branches. "
                "Skin is dry without glands except the oil gland at the base of the tail."))
story.append(b1("Endoskeleton is fully ossified (bony) and the long bones are hollow with air "
                "cavities (<b>pneumatic</b>). The digestive tract of birds has additional "
                "chambers, the <b>crop and gizzard</b>. Heart is completely four-chambered."))
story.append(b1("They are <b>warm-blooded (homoiothermous)</b> animals, i.e., they are able to "
                "maintain a constant body temperature. Respiration is by lungs. Air sacs "
                "connected to lungs supplement respiration."))
story.append(b1("Sexes are separate. Fertilisation is internal. They are oviparous and "
                "development is direct."))
story.append(b1("<b>Examples:</b> <i>Corvus</i> (Crow), <i>Columba</i> (Pigeon), "
                "<i>Psittacula</i> (Parrot), <i>Struthio</i> (Ostrich), <i>Pavo</i> (Peacock), "
                "<i>Aptenodytes</i> (Penguin), <i>Neophron</i> (Vulture)."))
story.append(figure("fig_4_23abcd.png",
                    "<b>Fig. 4.23</b> - Some birds : (a) Neophron (b) Struthio (c) Psittacula "
                    "(d) Pavo.",
                    max_width_cm=13.56))

# ---- 4.2.11.7 Class - Mammalia ----
story.append(heading("4.2.11.7", "Class - Mammalia", level=3))
story.append(b1("They are found in a variety of habitats - polar ice caps, deserts, mountains, "
                "forests, grasslands and dark caves. Some of them have adapted to fly or live in "
                "water."))
story.append(b1("The most unique mammalian characteristic is the presence of milk producing "
                "glands (<b>mammary glands</b>) by which the young ones are nourished. They have "
                "two pairs of limbs, adapted for walking, running, climbing, burrowing, swimming "
                "or flying (Figure 4.24)."))
story.append(b1("The skin of mammals is unique in possessing <b>hair</b>. External ears or "
                "<b>pinnae</b> are present. Different types of teeth are present in the jaw. "
                "Heart is four-chambered. They are homoiothermous. Respiration is by lungs."))
story.append(b1("Sexes are separate and fertilisation is internal. They are <b>viviparous</b> "
                "with few exceptions and development is direct."))
story.append(b1("<b>Examples:</b> Oviparous - <i>Ornithorhynchus</i> (Platypus); Viviparous - "
                "<i>Macropus</i> (Kangaroo), <i>Pteropus</i> (Flying fox), <i>Camelus</i> "
                "(Camel), <i>Macaca</i> (Monkey), <i>Rattus</i> (Rat), <i>Canis</i> (Dog), "
                "<i>Felis</i> (Cat), <i>Elephas</i> (Elephant), <i>Equus</i> (Horse), "
                "<i>Delphinus</i> (Common dolphin), <i>Balaenoptera</i> (Blue whale), "
                "<i>Panthera tigris</i> (Tiger), <i>Panthera leo</i> (Lion)."))
story.append(figure("fig_4_24abcd.png",
                    "<b>Fig. 4.24</b> - Some mammals : (a) Ornithorhynchus (b) Macropus "
                    "(c) Pteropus (d) Balaenoptera.",
                    max_width_cm=13.08))

# TABLE 4.2 — salient features of all phyla.
# Force a page break so this section opens a fresh page (the second-to-last
# page), beginning with the "salient distinguishing features" sentence.
story.append(PageBreak())
story.append(body("The salient distinguishing features of all phyla under the animal kingdom "
                  "are comprehensively given in Table 4.2."))
story.append(body("<b>TABLE 4.2</b> Salient Features of Different Phyla in the Animal Kingdom"))
story.append(data_table([
    ["Phylum", "Level of Organisation", "Symmetry", "Coelom", "Segmen-tation",
     "Digestive System", "Circula-tory", "Respira-tory", "Distinctive Features"],
    ["Porifera", "Cellular", "Various", "Absent", "Absent", "Absent", "Absent", "Absent",
     "Body with pores and canals in walls."],
    ["Coelenterata (Cnidaria)", "Tissue", "Radial", "Absent", "Absent", "Incomplete", "Absent",
     "Absent", "Cnidoblasts present."],
    ["Ctenophora", "Tissue", "Radial", "Absent", "Absent", "Incomplete", "Absent", "Absent",
     "Comb plates for locomotion."],
    ["Platyhelminthes", "Organ &amp; Organ-system", "Bilateral", "Absent", "Absent", "Incomplete",
     "Absent", "Absent", "Flat body, suckers."],
    ["Aschelminthes", "Organ-system", "Bilateral", "Pseudo-coelomate", "Absent", "Complete",
     "Absent", "Absent", "Often worm-shaped, elongated."],
    ["Annelida", "Organ-system", "Bilateral", "Coelomate", "Present", "Complete", "Present",
     "Absent", "Body segmentation like rings."],
    ["Arthropoda", "Organ-system", "Bilateral", "Coelomate", "Present", "Complete", "Present",
     "Present", "Exoskeleton of cuticle, jointed appendages."],
    ["Mollusca", "Organ-system", "Bilateral", "Coelomate", "Absent", "Complete", "Present",
     "Present", "External skeleton of shell usually present."],
    ["Echinodermata", "Organ-system", "Radial", "Coelomate", "Absent", "Complete", "Present",
     "Present", "Water vascular system, radial symmetry."],
    ["Hemichordata", "Organ-system", "Bilateral", "Coelomate", "Absent", "Complete", "Present",
     "Present", "Worm-like with proboscis, collar and trunk."],
    ["Chordata", "Organ-system", "Bilateral", "Coelomate", "Present", "Complete", "Present",
     "Present", "Notochord, dorsal hollow nerve cord, gill slits with limbs or fins."],
], col_widths=[1.15, 1.2, 0.85, 1.05, 0.95, 1.05, 0.9, 0.9, 1.95]))

# ---- SUMMARY ----
story.append(heading("Summary", "Summary", level=1))
story.append(body("The basic fundamental features such as level of organisation, symmetry, cell "
                  "organisation, coelom, segmentation, notochord, etc., have enabled us to "
                  "broadly classify the animal kingdom. Besides the fundamental features, there "
                  "are many other distinctive characters which are specific for each phyla or "
                  "class."))
story.append(body("Porifera includes multicellular animals which exhibit cellular level of "
                  "organisation and have characteristic flagellated choanocytes. The "
                  "coelenterates have tentacles and bear cnidoblasts; they are mostly aquatic, "
                  "sessile or free-floating. The ctenophores are marine animals with comb "
                  "plates. The platyhelminths have flat body and exhibit bilateral symmetry; the "
                  "parasitic forms show distinct suckers and hooks. Aschelminthes are "
                  "pseudocoelomates and include parasitic as well as non-parasitic roundworms."))
story.append(body("Annelids are metamerically segmented animals with a true coelom. The "
                  "arthropods are the most abundant group of animals characterised by the "
                  "presence of jointed appendages; the body is covered with external skeleton "
                  "made of chitin. The molluscs have a soft body surrounded by an external "
                  "calcareous shell. The echinoderms possess a spiny skin and their most "
                  "distinctive feature is the presence of water vascular system. The "
                  "hemichordates are a small group of worm-like marine animals with a "
                  "cylindrical body of proboscis, collar and trunk."))
story.append(body("Phylum Chordata includes animals which possess a notochord either throughout "
                  "or during early embryonic life; other common features are the dorsal hollow "
                  "nerve cord and paired pharyngeal gill slits. Some of the vertebrates do not "
                  "possess jaws (Agnatha) whereas most of them possess jaws (Gnathostomata). "
                  "Agnatha is represented by the class Cyclostomata; they are the most primitive "
                  "chordates and are ectoparasites on fishes."))
story.append(body("Gnathostomata has two super classes, Pisces and Tetrapoda. Classes "
                  "Chondrichthyes and Osteichthyes bear fins for locomotion and are grouped "
                  "under Pisces; the Chondrichthyes are fishes with cartilaginous endoskeleton "
                  "and are marine. Classes Amphibia, Reptilia, Aves and Mammalia have two pairs "
                  "of limbs and are thus grouped under Tetrapoda. The amphibians have adapted to "
                  "live both on land and water. Reptiles are characterised by the presence of "
                  "dry and cornified skin; limbs are absent in snakes. Fishes, amphibians and "
                  "reptiles are poikilothermous (cold-blooded)."))
story.append(body("Aves are warm-blooded animals with feathers on their bodies and forelimbs "
                  "modified into wings for flying; hind limbs are adapted for walking, swimming, "
                  "perching or clasping. The unique features of mammals are the presence of "
                  "mammary glands and hairs on the skin, and they commonly exhibit viviparity."))

# ---- EXERCISES (gap support) ----
story.append(heading("Exercises", "Exercises", level=1))
story.append(body("The exercises assume two term-pairs that the running text uses but never "
                  "formally defines. They are stated here so the exercise set is self-contained."))
story.append(keyterm("<b>Intracellular vs extracellular digestion (Q4):</b> in intracellular "
                     "digestion food is broken down <i>inside</i> the cell (as in Porifera); in "
                     "extracellular digestion food is broken down <i>outside</i> the cells in a "
                     "gut cavity (coelenterates and ctenophores use both intracellular and "
                     "extracellular digestion)."))
story.append(keyterm("<b>Oviparous vs viviparous (Q12):</b> oviparous animals lay eggs that "
                     "develop and hatch outside the mother's body; viviparous animals give birth "
                     "to young ones that have completed development inside the mother's body. "
                     "The eggs of an oviparous mother and the young of a viviparous mother need "
                     "not be equal in number."))
story.append(memory_aid("Vertebrata ladder - <b>A</b>gnatha then <b>G</b>nathostomata; within "
                        "Gnathostomata, Pisces (Chondrichthyes, Osteichthyes) then Tetrapoda "
                        "(Amphibia, Reptilia, Aves, Mammalia). Chamber count climbs 2 -> 3 -> "
                        "(3/4) -> 4 -> 4 across fishes, amphibia, reptilia, aves and mammals."))


def main():
    return build_pdf(OUT_PDF, story,
                     title="Class 11 Chapter 4 - Animal Kingdom (NEET notes)",
                     subject="NEET Biology")


if __name__ == "__main__":
    sys.exit(main())
