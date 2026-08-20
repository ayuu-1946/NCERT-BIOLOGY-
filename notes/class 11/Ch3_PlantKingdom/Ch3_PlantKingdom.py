"""Class 11 - Chapter 3: Plant Kingdom (NEET replacement notes).

Generated from the frozen 215-row inventory under SUPREME COMMAND PROMPT.md v6.
All styles, geometry, badges, tables, figures and PDF construction come from the
repo-level frozen neet_template.py. Source typos documented in the inventory are
normalised in prose; Table 3.1 preserves the printed NCERT wording.
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

from reportlab.platypus import Paragraph, Spacer, KeepTogether
from reportlab.lib.units import cm
from neet_template import (
    STYLES, heading, keyterm, process_flow, note, memory_aid,
    data_table, title_block, build_pdf,
)
from neet_template import figure as _shared_figure

ASSETS = os.path.join(HERE, "assets")
OUT_PDF = os.path.join(HERE, "Ch3_PlantKingdom.pdf")


def figure(asset_name, caption_text, max_width_cm=15.9):
    return _shared_figure(asset_name, caption_text, ASSETS, max_width_cm=max_width_cm)


def body(text):
    return Paragraph(text, STYLES["Body"])


def b1(text):
    return Paragraph("&bull; " + text, STYLES["Bullet1"])


def b2(text):
    return Paragraph("- " + text, STYLES["Bullet2"])


story = []
story += title_block("Plant Kingdom")

# ---- 3.0 Chapter map and changing systems ----
story.append(heading("3.0", "A Changing View of the Plant Kingdom", level=1))
story.append(body("The chapter map is <b>3.1 Algae; 3.2 Bryophytes; 3.3 Pteridophytes; 3.4 Gymnosperms; 3.5 Angiosperms</b>. In the previous chapter, living organisms were placed under Whittaker's <b>1969 Five Kingdom classification</b>: Monera, Protista, Fungi, Animalia and Plantae. Here the focus narrows to classification within Kingdom Plantae, popularly called the plant kingdom."))
story.append(b1("Our understanding has changed with time. Fungi and cell-walled members of Monera and Protista, once placed with plants, are now excluded. Thus cyanobacteria, also called blue-green algae, are no longer treated as algae. This chapter nevertheless follows the NCERT sequence Algae, Bryophytes, Pteridophytes, Gymnosperms and Angiosperms."))
story.append(b1("The earliest <b>artificial systems</b> used a few gross, superficial morphological characters such as habit, colour, number and shape of leaves. They relied mainly on vegetative characters or on androecium structure, as in <b>Linnaeus'</b> system. Equal weight was given to vegetative and sexual characters even though vegetative characters are more easily altered by the environment; closely related species could therefore be separated."))
story.append(b1("<b>Natural classification systems</b> instead use natural affinities and consider external features together with internal features such as ultrastructure, anatomy, embryology and phytochemistry. <b>George Bentham and Joseph Dalton Hooker</b> gave such a system for flowering plants."))
story.append(b1("Modern <b>phylogenetic systems</b> are based on evolutionary relationships and assume that organisms in the same taxa share a common ancestor. Evidence from other sources becomes especially important when supporting fossils are absent."))
story.append(data_table([
    ["Approach", "Evidence and method"],
    ["Numerical taxonomy", "All observable characters are numbered and coded, then processed by computer; each character receives equal importance and hundreds can be considered."],
    ["Cytotaxonomy", "Uses cytological information such as chromosome number, structure and behaviour."],
    ["Chemotaxonomy", "Uses plant chemical constituents to resolve classification confusion."],
], col_widths=[3.2, 12.0]))

# ---- 3.1 Algae ----
story.append(heading("3.1", "Algae", level=1))
story.append(keyterm("<b>Algae</b> are chlorophyll-bearing, simple, thalloid, autotrophic and largely aquatic organisms, occurring in both fresh water and marine water. They also inhabit moist stones, soil and wood; some associate with fungi as lichens or with animals, for example on a sloth bear."))
story.append(b1("Their form and size vary from colonial <i>Volvox</i> and filamentous <i>Ulothrix</i> and <i>Spirogyra</i> to massive marine kelps. In a <i>Volvox</i> colony, the figure identifies a <b>Daughter colony</b> inside a <b>Parent colony</b>."))
story.append(heading("3.1a", "Three Modes of Reproduction", level=2))
story.append(process_flow([
    "<b>Vegetative:</b> fragmentation; each fragment develops into a thallus.",
    "<b>Asexual:</b> spores, most commonly flagellated, motile zoospores; germination produces new plants.",
    "<b>Sexual:</b> fusion of two gametes; the gametes determine whether reproduction is isogamous, anisogamous or oogamous.",
]))
story.append(data_table([
    ["Sexual pattern", "Diagnostic feature", "Examples"],
    ["Isogamy / isogamous", "Gametes similar in size: both flagellated, or both non-motile.", "<i>Ulothrix</i>; <i>Spirogyra</i>"],
    ["Anisogamy / anisogamous", "Two fusing gametes are dissimilar in size.", "Species of <i>Eudorina</i>"],
    ["Oogamy / oogamous", "Large non-motile female gamete and smaller motile male gamete.", "<i>Volvox</i>, <i>Fucus</i>"],
], col_widths=[2.7, 8.2, 4.2]))
story.append(heading("3.1b", "Ecological and Economic Importance", level=2))
story.append(b1("Algae perform at least <b>half of total carbon dioxide fixation on Earth</b> through photosynthesis, increase dissolved oxygen locally, and are primary producers of energy-rich compounds at the base of aquatic food cycles."))
story.append(b1("Among the <b>70 marine algal species used as food</b> are many species of <i>Porphyra</i>, <i>Laminaria</i> and <i>Sargassum</i>. Brown and red marine algae yield water-holding hydrocolloids: algin from brown algae and carrageen from red algae."))
story.append(b1("Agar from <i>Gelidium</i> and <i>Gracilaria</i> is used to grow microbes and prepare ice-creams and jellies. Protein-rich unicellular <i>Chlorella</i> is a food supplement even for space travellers."))
story.append(note("Algae are classified into <b>Chlorophyceae, Phaeophyceae and Rhodophyceae</b> according to their pigments and stored food. This classification basis is stated explicitly in the NCERT summary."))

# ---- 3.1.1 Chlorophyceae ----
story.append(heading("3.1.1", "Chlorophyceae - Green Algae", level=2))
story.append(b1("The plant body may be unicellular, colonial or filamentous. Its usual grass-green colour comes from dominant chlorophyll <i>a</i> and <i>b</i>, localised in definite chloroplasts that may be discoid, plate-like, reticulate, cup-shaped, spiral or ribbon-shaped."))
story.append(b1("Most members have one or more chloroplastic storage bodies called <b>pyrenoids</b>, containing protein besides starch; some algae instead store oil droplets. The rigid wall usually has inner cellulose and outer pectose layers."))
story.append(b1("Vegetative reproduction is usually by fragmentation; asexual reproduction uses flagellated zoospores formed in zoosporangia; sexual reproduction varies and may be isogamous, anisogamous or oogamous."))
story.append(b1("Common members are <i>Chlamydomonas</i>, <i>Volvox</i>, <i>Ulothrix</i>, <i>Spirogyra</i> and <i>Chara</i>."))
story.append(figure("fig_3_1a.png", "<b>Fig. 3.1(a)</b> - Green algae: part (a-i), <i>Volvox</i>, showing Daughter colony and Parent colony; part (a-ii), <i>Ulothrix</i>."))

# ---- 3.1.2 Phaeophyceae ----
story.append(heading("3.1.2", "Phaeophyceae - Brown Algae", level=2))
story.append(b1("Primarily marine brown algae range from simple branched filamentous <i>Ectocarpus</i> to profusely branched kelps reaching <b>100 metres</b>. They contain chlorophyll <i>a</i>, chlorophyll <i>c</i>, carotenoids and xanthophylls; fucoxanthin abundance produces colours from olive green to brown."))
story.append(b1("Food is stored as laminarin or mannitol. A cellulosic wall is usually covered by a gelatinous algin coat. Besides plastids, the protoplast has a centrally located vacuole and nucleus."))
story.append(keyterm("The body attaches by a <b>Holdfast</b>, continues as the stalk-like <b>Stipe</b>, and expands into the photosynthetic <b>Frond</b>. Figure 3.1(b) also labels an <b>Air bladder</b> and <b>Midrib</b>."))
story.append(b1("Vegetative reproduction is by fragmentation. Most asexual reproduction uses pear-shaped biflagellate zoospores with two unequal lateral flagella. Sexual reproduction may be isogamous, anisogamous or oogamous; gametes unite in water or, in oogamous species, within the oogonium. Gametes are pyriform and bear two lateral flagella."))
story.append(b1("Common forms are <i>Ectocarpus</i>, <i>Dictyota</i>, <i>Laminaria</i>, <i>Sargassum</i> and <i>Fucus</i>."))
story.append(figure("fig_3_1b.png", "<b>Fig. 3.1(b)</b> - Brown algae: part (b-i) <i>Laminaria</i>, part (b-ii) <i>Fucus</i>, and part (b-iii) <i>Dictyota</i>. Labels include Frond, Stipe, Holdfast, Air bladder and Midrib."))

# ---- 3.1.3 Rhodophyceae ----
story.append(heading("3.1.3", "Rhodophyceae - Red Algae", level=2))
story.append(b1("Red algae are named for dominant red r-phycoerythrin. Most are marine, especially in warmer areas, occurring both in well-lit surface water and at great ocean depths where little light penetrates. Most red thalli are multicellular and some show complex organisation."))
story.append(b1("Food is floridean starch, structurally similar to amylopectin and glycogen. Vegetative reproduction is usually fragmentation; asexual spores and sexual gametes are non-motile. Sexual reproduction is oogamous and followed by complex post-fertilisation development."))
story.append(b1("Common members are <i>Polysiphonia</i>, <i>Porphyra</i>, <i>Gracilaria</i> and <i>Gelidium</i>. The illustrated thalli mark the <b>Frond</b>, <b>Main axis</b> and <b>Branches</b>."))
story.append(figure("fig_3_1c.png", "<b>Fig. 3.1(c)</b> - Red algae: part (c-i) <i>Porphyra</i> and part (c-ii) <i>Polysiphonia</i>, with Frond, Main axis and Branches labelled."))

# ---- Table 3.1 ----
story.append(heading("T 3.1", "Divisions of Algae and their Main Characteristics", level=2))
story.append(data_table([
    ["Classes", "Common Name", "Major Pigments", "Stored Food", "Cell Wall", "Flagellar Number and Position of Insertions", "Habitat"],
    ["Chlorophyceae", "Green algae", "Chlorophyll a, b", "Starch", "Cellulose", "2-8, equal, apical", "Fresh water, brackish water, salt water"],
    ["Phaeophyceae", "Brown algae", "Chlorophyll a, c, fucoxanthin", "Mannitol, laminarin", "Cellulose and algin", "2, unequal, lateral", "Fresh water (rare), brackish water, salt water"],
    ["Rhodophyceae", "Red algae", "Chlorophyll a, d, phycoerythrin", "Floridean starch", "Cellulose, pectin and poly sulphate esters", "Absent", "Fresh water (some), brackish water, salt water (most)"],
], col_widths=[1.75, 1.5, 2.15, 1.65, 2.0, 2.7, 2.55], font_size=7.2))

# ---- 3.2 Bryophytes ----
story.append(heading("3.2", "Bryophytes - Amphibians of the Plant Kingdom", level=1))
story.append(keyterm("Bryophytes include mosses and liverworts of moist, shaded hill habitats. They are called <b>amphibians of the plant kingdom</b>: they live on soil but require water for sexual reproduction. They commonly occupy damp, humid, shaded places and aid succession on bare rock or soil."))
story.append(b1("Their body is more differentiated than an algal thallus: it may be thallus-like, prostrate or erect, and anchors by unicellular or multicellular rhizoids. They lack true roots, stem and leaves, but <b>may</b> possess root-like, leaf-like <b>or</b> stem-like structures."))
story.append(b1("The main plant body is a haploid gametophyte that produces gametes. Multicellular antheridia produce biflagellate antherozoids; a flask-shaped archegonium produces one egg."))
story.append(process_flow([
    "Antherozoids released into water reach the archegonium.",
    "One antherozoid fuses with the egg to form a diploid zygote.",
    "The zygote does not immediately undergo reduction division; it forms a multicellular sporophyte attached to and nourished by the photosynthetic gametophyte.",
    "Some sporophyte cells undergo meiosis to make haploid spores, which germinate into gametophytes.",
]))
story.append(b1("Bryophytes have little economic importance overall, but some mosses feed herbaceous mammals, birds and other animals. <i>Sphagnum</i> peat has long served as fuel and as water-retaining packing material for transporting living material."))
story.append(b1("Mosses and lichens first colonise rocks, then decompose them to prepare substrate for higher plants. Dense moss mats reduce rain impact and prevent soil erosion. Bryophytes are divided into liverworts and mosses."))

# ---- 3.2.1 Liverworts ----
story.append(heading("3.2.1", "Liverworts", level=2))
story.append(b1("Liverworts grow on stream banks, marshy ground, damp soil, tree bark and deep woods. In thalloid <i>Marchantia</i>, the body is dorsiventral and closely appressed to the substrate; leafy forms bear two rows of tiny leaf-like appendages on stem-like structures."))
story.append(b1("Asexual reproduction occurs by thallus fragmentation or by <b>gemmae</b> (singular: gemma): green, multicellular asexual buds formed in <b>Gemma cup</b> receptacles. Detached gemmae germinate into new individuals."))
story.append(b1("Male and female organs occur on the same or different thalli. Figure 3.2 identifies the female <b>Archegoniophore</b>, male <b>Antheridiophore</b>, Gemma cup and <b>Rhizoids</b>. The sporophyte differentiates into foot, seta and capsule; meiosis in the capsule forms spores that germinate into free-living gametophytes."))
story.append(figure("fig_3_2ab.png", "<b>Fig. 3.2(a-b)</b> - A liverwort, <i>Marchantia</i>: panel (a), female thallus with Archegoniophore; panel (b), male thallus with Antheridiophore. Gemma cup and Rhizoids are labelled."))

# ---- 3.2.2 Mosses ----
story.append(heading("3.2.2", "Mosses", level=2))
story.append(process_flow([
    "<b>Protonema stage:</b> develops directly from a spore; it is creeping, green, branched and often filamentous.",
    "<b>Leafy stage:</b> develops as a lateral bud from secondary protonema; upright slender axes carry spirally arranged leaves and attach by multicellular branched rhizoids.",
    "The leafy stage bears apical antheridia and archegonia. After fertilisation, the zygote forms a sporophyte of foot, seta and capsule.",
    "The capsule forms spores after meiosis and has an elaborate dispersal mechanism.",
]))
story.append(b1("Vegetative reproduction is by fragmentation and budding in secondary protonema. The moss sporophyte is more elaborate than the liverwort sporophyte. Common examples are <i>Funaria</i>, <i>Polytrichum</i> and <i>Sphagnum</i>."))
story.append(note("Summary contrast: the liverwort body is thalloid and dorsiventral, whereas mosses have upright slender axes with spirally arranged leaves."))
story.append(b1("In the moss figure, <i>Funaria</i> shows <b>Gametophyte</b>, <b>Sporophyte</b>, <b>Capsule</b>, <b>Seta</b> and <b>Rhizoids</b>. <i>Sphagnum</i> shows <b>Leaves</b>, <b>Main axis</b>, <b>Branches</b>, <b>Antheridial branch</b> and <b>Archegonial branch</b>."))
story.append(figure("fig_3_2cd.png", "<b>Fig. 3.2(c-d)</b> - Mosses: panel (c), <i>Funaria</i> gametophyte and sporophyte; panel (d), <i>Sphagnum</i> gametophyte. Labels: Sporophyte, Gametophyte, Capsule, Seta, Leaves, Main axis, Rhizoids, Antheridial branch, Archegonial branch and Branches."))

# ---- 3.3 Pteridophytes ----
story.append(heading("3.3", "Pteridophytes - First Vascular Land Plants", level=1))
story.append(b1("Pteridophytes include horsetails and ferns. They are medicinal, act as soil binders and are commonly grown as ornamentals. Evolutionarily, they are the first terrestrial plants with vascular xylem and phloem, tissues studied further in Chapter 6."))
story.append(b1("They usually grow in cool, damp, shaded places, though some tolerate sandy soil. Unlike bryophytes with dominant gametophytes, their main body is a dominant sporophyte differentiated into true roots, stem and leaves, all with well-developed vascular tissue."))
story.append(b1("Leaves may be small <b>microphylls</b>, as in <i>Selaginella</i>, or large <b>macrophylls</b>, as in ferns. Sporangia are subtended by leaf-like <b>sporophylls</b>; sporophylls may gather into compact <b>strobili</b> or cones in <i>Selaginella</i> and <i>Equisetum</i>. The singular is <b>Strobilus</b>."))
story.append(process_flow([
    "Spore mother cells undergo meiosis in sporangia and produce spores.",
    "Spores germinate into an inconspicuous, small, multicellular, free-living, mostly photosynthetic thalloid gametophyte called the prothallus.",
    "Antheridia release antherozoids; water carries them to the archegonial mouth, where a male gamete fuses with the egg to form a diploid zygote.",
    "The zygote forms a multicellular, differentiated sporophyte, the dominant phase.",
]))
story.append(b1("The prothallus needs cool, damp, shaded conditions. This restricted habitat and water-dependent fertilisation limit living pteridophytes to narrow geographical regions. Gametophytes carry male antheridia and female archegonia."))
story.append(data_table([
    ["Spore condition", "Meaning and significance"],
    ["Homosporous", "Most pteridophytes make one similar kind of spore."],
    ["Heterosporous", "<i>Selaginella</i> and <i>Salvinia</i> make large macrospores and small microspores. These produce female and male gametophytes respectively."],
], col_widths=[3.2, 12.0]))
story.append(b1("In heterosporous plants, female gametophytes remain on the parent sporophyte for variable periods and young embryos develop within them. This is a precursor of the seed habit and an important evolutionary step."))
story.append(b1("Four classes are <b>Psilopsida</b> (<i>Psilotum</i>), <b>Lycopsida</b> (<i>Selaginella</i>, <i>Lycopodium</i>), <b>Sphenopsida</b> (<i>Equisetum</i>) and <b>Pteropsida</b> (<i>Dryopteris</i>, <i>Pteris</i>, <i>Adiantum</i>)."))
story.append(b1("Figure 3.3(a-b) labels <i>Selaginella</i> <b>Leaves</b>, <b>Stem</b> and <b>Roots</b>. In <i>Equisetum</i>, it identifies the Strobilus, <b>Node</b>, <b>Internode</b>, <b>Branch</b> and <b>Rhizome</b>."))
story.append(figure("fig_3_3ab.png", "<b>Fig. 3.3(a-b)</b> - Pteridophytes: panel (a) <i>Selaginella</i>, labelled Leaves, Stem and Roots; panel (b) <i>Equisetum</i>, labelled Strobilus, Node, Internode, Branch and Rhizome."))
story.append(figure("fig_3_3cd.png", "<b>Fig. 3.3(c-d)</b> - Pteridophytes: panel (c), a fern; panel (d), <i>Salvinia</i>."))

# ---- 3.4 Gymnosperms ----
story.append(heading("3.4", "Gymnosperms - Naked Seeds", level=1))
story.append(keyterm("<b>Gymnosperms</b> (gymnos = naked; sperma = seeds) have ovules not enclosed by an ovary wall, exposed before and after fertilisation. Their post-fertilisation seeds remain uncovered, so these are <b>naked-seeded plants</b>. They include shrubs, medium trees and tall trees; giant redwood <i>Sequoia</i> is among the tallest tree species."))
story.append(heading("3.4a", "Vegetative Features", level=2))
story.append(b1("Roots are generally tap roots. <i>Pinus</i> roots form fungal mycorrhiza; <i>Cycas</i> has specialised coralloid roots associated with N<sub>2</sub>-fixing cyanobacteria. Stems are unbranched in <i>Cycas</i> or branched in <i>Pinus</i> and <i>Cedrus</i>. Leaves may be simple or compound; <i>Cycas</i> pinnate leaves persist for years."))
story.append(b1("Gymnosperm leaves withstand extremes of temperature, humidity and wind. Conifer needles reduce surface area; thick cuticle and sunken stomata further reduce water loss."))
story.append(heading("3.4b", "Heterospory, Cones and Fertilisation", level=2))
story.append(b1("Gymnosperms are heterosporous, making haploid microspores and megaspores in sporangia carried on spirally arranged sporophylls. Microsporophylls form male cones; megasporophylls form female cones."))
story.append(b1("A microsporangiate or male strobilus bears microsporophylls and microsporangia. Microspores develop inside microsporangia into highly reduced, few-celled male gametophytes called <b>pollen grains</b>. A macrosporangiate or female strobilus bears ovules or megasporangia on megasporophylls."))
story.append(b1("Male and female cones may occur on one tree, as in <i>Pinus</i>. In <i>Cycas</i>, male cones and megasporophylls occur on different trees."))
story.append(process_flow([
    "A megaspore mother cell differentiates in the nucellus. Envelopes protect the nucellus; together they form an ovule borne on a megasporophyll, sometimes clustered into a female cone.",
    "The mother cell undergoes meiosis to form <b>four megaspores</b>. One retained megaspore forms a multicellular female gametophyte with two or more archegonia.",
    "Neither gametophyte is independently free-living: both remain in sporangia retained on the sporophyte.",
    "Air currents carry released pollen grains to ovule openings. A pollen grain germinates; its tube grows toward the archegonia and releases male gametes near the archegonial mouth.",
    "A male gamete fuses with the egg cell. The zygote becomes an embryo and the exposed ovule becomes an uncovered seed.",
]))
story.append(b1("Figure 3.4(c) identifies the <i>Ginkgo</i> <b>Dwarf Shoot</b>, <b>Long Shoot</b> and <b>Seeds</b>."))
story.append(figure("fig_3_4a.png", "<b>Fig. 3.4(a)</b> - Gymnosperms: panel (a), <i>Cycas</i>."))
story.append(figure("fig_3_4b.png", "<b>Fig. 3.4(b)</b> - Gymnosperms: panel (b), <i>Pinus</i>."))
story.append(figure("fig_3_4c.png", "<b>Fig. 3.4(c)</b> - Gymnosperms: panel (c), <i>Ginkgo</i>, showing Dwarf Shoot, Long Shoot and Seeds."))

# ---- 3.5 Angiosperms ----
story.append(heading("3.5", "Angiosperms - Flowering Plants", level=1))
story.append(b1("Unlike gymnosperms with naked ovules, angiosperms develop pollen grains and ovules in specialised <b>flowers</b>; their seeds are enclosed in <b>fruits</b>. This exceptionally large group occupies a wide range of habitats."))
story.append(b1("Size ranges from tiny <i>Wolffia</i> to <i>Eucalyptus</i> trees over <b>100 metres</b>. Angiosperms supply food, fodder, fuel, medicines and many commercial products. They divide into dicotyledons and monocotyledons."))
story.append(figure("fig_3_5ab.png", "<b>Fig. 3.5</b> - Angiosperms: panel (a), a dicotyledon; panel (b), a monocotyledon."))

# ---- Recap ----
story.append(heading("Recap", "Quick Recap", level=1))
story.append(data_table([
    ["Group", "Dominant/diagnostic idea", "Exam anchor"],
    ["Algae", "Simple thalloid autotrophs; vegetative, asexual and sexual reproduction", "Three classes based on pigments and stored food"],
    ["Bryophytes", "Haploid gametophyte dominant; sporophyte dependent", "Water needed for sex; no true roots, stem or leaves"],
    ["Pteridophytes", "Vascular sporophyte dominant", "Heterospory foreshadows seed habit"],
    ["Gymnosperms", "Ovules and seeds exposed", "Reduced gametophytes retained on sporophyte"],
    ["Angiosperms", "Flowers; seeds enclosed in fruits", "Dicotyledons and monocotyledons"],
], col_widths=[2.7, 7.2, 5.3]))
story.append(memory_aid("Increasing protection of the next generation: bryophyte embryo remains on gametophyte; heterosporous pteridophytes retain the female gametophyte; gymnosperms retain ovules but leave seeds naked; angiosperms enclose seeds in fruits."))

# ---- Exercises ----
story.append(heading("Exercises", "Exercise Structures to Retain", level=1))
story.append(b1("Q8 asks for protonema, antheridium, archegonium, diplontic, sporophyll and isogamy. Q9 compares red versus brown algae, liverworts versus mosses, and homosporous versus heterosporous pteridophytes."))
story.append(b1("Q10's printed columns scramble these pairs: <i>Chlamydomonas</i>-Algae, <i>Cycas</i>-Gymnosperm, <i>Selaginella</i>-Pteridophyte, <i>Sphagnum</i>-Moss."))
story.append(b1("Q4 asks the ploidy of a moss protonemal cell, dicot primary endosperm nucleus, moss leaf cell, fern prothallus cell, <i>Marchantia</i> gemma cell, monocot meristem cell, liverwort ovum and fern zygote."))

# ---- Appendix ----
story.append(heading("Appendix", "Terms Used in the Exercises", level=1))
story.append(note("The following points close genuine exercise gaps; they are background explanations not stated in the chapter body."))
story.append(b1("<b>Angiosperm meiosis:</b> microspore mother cells undergo meiosis to form microspores (pollen precursors), and the megaspore mother cell undergoes meiosis to form megaspores."))
story.append(b1("<b>Primary endosperm nucleus:</b> in a typical angiosperm it is triploid (3n), formed when one male gamete fuses with two polar nuclei."))
story.append(b1("<b>Monocot meristem:</b> it belongs to the diploid sporophyte, so its cells are 2n. Ploidy answers for Q4 are: moss protonema n; primary endosperm nucleus 3n; moss leaf n; fern prothallus n; <i>Marchantia</i> gemma n; monocot meristem 2n; liverwort ovum n; fern zygote 2n."))
story.append(b1("<b>Gymnosperm economic importance:</b> gymnosperms provide timber and softwood, paper pulp, resins and turpentine, edible pine nuts, ornamentals, and medicinal products from plants such as <i>Ephedra</i> and <i>Taxus</i>."))
story.append(b1("<b>Diplontic life cycle:</b> the diploid sporophyte is dominant and the gametophyte is reduced to a few cells, as in gymnosperms and angiosperms. By contrast, haplontic algae have a dominant haploid phase, while bryophytes and pteridophytes show both multicellular generations."))


def main():
    try:
        for asset in (
            "fig_3_1a.png", "fig_3_1b.png", "fig_3_1c.png", "fig_3_2ab.png",
            "fig_3_2cd.png", "fig_3_3ab.png", "fig_3_3cd.png", "fig_3_4a.png",
            "fig_3_4b.png", "fig_3_4c.png", "fig_3_5ab.png",
        ):
            path = os.path.join(ASSETS, asset)
            if not os.path.isfile(path):
                raise FileNotFoundError(f"Required figure asset missing: {path}")
        build_pdf(OUT_PDF, story, title="Plant Kingdom")
    except (OSError, RuntimeError, ValueError) as exc:
        raise RuntimeError(f"Failed to build Plant Kingdom notes: {exc}") from exc


if __name__ == "__main__":
    main()
