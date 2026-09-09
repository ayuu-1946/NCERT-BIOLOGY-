"""Emit the Ch5 frozen inventory from structured row data (Pass 1 build evidence).

Rows are held as data so `F001..FNNN` is contiguous by construction rather than
by hand-numbering, and so every header count in the emitted file is derived by
re-parsing the table it describes (GATE_1 step 10).

Run from the repository root:
    /vercel/share/neetenv/bin/python scratch/ch5morph_gate1/build_inventory.py
"""
import collections
import importlib.util
import re

OUT = "notes/class 11/Ch5_MorphologyOfFloweringPlants/Ch5_MorphologyOfFloweringPlants_inventory.md"
EXTRACT = "notes/class 11/Ch5_MorphologyOfFloweringPlants/extract_figures.py"
FROZEN = "2026-09-09"
SRC = "Chapter/class 11/Chapter 05 - Morphology of Flowering Plants.pdf"

# (section, type, exact original wording)
ROWS: list[tuple[str, str, str]] = []
R = ROWS.append

# ---------------- UNIT 2 opener (source page 1) ----------------
R(("unit2", "heading", 'Unit banner heading: "UNIT 2 — STRUCTURAL ORGANISATION IN PLANTS AND ANIMALS"'))
R(("unit2", "fact", '"The description of the diverse forms of life on earth was made only by observation – through naked eyes or later through magnifying lenses and microscopes."'))
R(("unit2", "fact", '"This description is mainly of gross structural features, both external and internal."'))
R(("unit2", "fact", '"In addition, observable and perceivable living phenomena were also recorded as part of this description."'))
R(("unit2", "fact", '"Before experimental biology or more specifically, physiology, was established as a part of biology, naturalists described only biology."'))
R(("unit2", "fact", '"Hence, biology remained as a natural history for a long time."'))
R(("unit2", "fact", '"The description, by itself, was amazing in terms of detail."'))
R(("unit2", "fact", '"While the initial reaction of a student could be boredom, one should keep in mind that the detailed description, was utilised in the later day reductionist biology where living processes drew more attention from scientists than the description of life forms and their structure."'))
R(("unit2", "fact", '"Hence, this description became meaningful and helpful in framing research questions in physiology or evolutionary biology."'))
R(("unit2", "fact", '"In the following chapters of this unit, the structural organisation of plants and animals, including the structural basis of physiologial or behavioural phenomena, is described." (NCERT spelling "physiologial" preserved)'))
R(("unit2", "fact", '"For convenience, this description of morphological and anatomical features is presented separately for plants and animals."'))
R(("unit2", "term", 'Unit 2 contents listed as "Chapter 5 Morphology of Flowering Plants", "Chapter 6 Anatomy of Flowering Plants", "Chapter 7 Structural Organisation in Animals"'))

# ---------------- Katherine Esau profile (source page 2) ----------------
R(("esau", "heading", 'Unnumbered scientist-profile heading: "Katherine Esau"'))
R(("esau", "number", '"KATHERINE ESAU was born in Ukraine in 1898." (date: 1898)'))
R(("esau", "number", '"She studied agriculture in Russia and Germany and received her doctorate in 1931 in United States." (date: 1931)'))
R(("esau", "fact", '"She reported in her early publications that the curly top virus spreads through a plant via the food-conducting or phloem tissue."'))
R(("esau", "number", '"Dr Esau\u2019s Plant Anatomy published in 1954 took a dynamic, developmental approach designed to enhance one\u2019s understanding of plant structure and an enormous impact worldwide, literally bringing about a revival of the discipline." (date: 1954)'))
R(("esau", "number", '"The Anatomy of Seed Plants by Katherine Esau was published in 1960." (date: 1960)'))
R(("esau", "fact", '"It was referred to as Webster\u2019s of plant biology – it is encyclopediac." (NCERT spelling "encyclopediac" preserved)'))
R(("esau", "number", '"In 1957 she was elected to the National Academy of Sciences, becoming the sixth woman to receive that honour." (date: 1957; count: sixth)'))
R(("esau", "number", '"In addition to this prestigious award, she received the National Medal of Science from President George Bush in 1989." (date: 1989)'))
R(("esau", "number", '"When Katherine Esau died in the year 1997, Peter Raven, director of Anatomy and Morphology, Missouri Botanical Garden, remembered that she \u2018absolutely dominated\u2019 the field of plant biology even at the age of 99." (dates: 1997; age 99)'))
R(("esau", "caption", 'Profile caption (verbatim): "Katherine Esau (1898 – 1997)" — human-subject photograph; NEVER embedded, text-only per section 4.4 hard-no'))

# ---------------- Chapter title + intro (source page 3) ----------------
R(("Ch5", "heading", 'Chapter 5 title: "MORPHOLOGY OF FLOWERING PLANTS" / "CHAPTER 5"'))
R(("intro", "opener", '"The wide range in the structure of higher plants will never fail to fascinate us."'))
R(("intro", "qualifier", '"Even though the angiosperms show such a large diversity in external structure or morphology, they are all characterised by presence of roots, stems, leaves, flowers and fruits." (qualifier: even though, all)'))
R(("intro", "fact", '"In chapters 2 and 3, we talked about classification of plants based on morphological and other characteristics."'))
R(("intro", "fact", '"For any successful attempt at classification and at understanding any higher plant (or for that matter any living organism) we need to know standard technical terms and standard definitions."'))
R(("intro", "example", '"We also need to know about the possible variations in different parts, found as adaptations of the plants to their environment, e.g., adaptions to various habitats, for protection, climbing, storage, etc." (NCERT spelling "adaptions" preserved)'))
R(("intro", "qualifier", '"If you pull out any weed you will see that all of them have roots, stems and leaves. They may be bearing flowers and fruits." (qualifiers: all, may)'))
R(("intro", "definition", '"The underground part of the flowering plant is the root system while the portion above the ground forms the shoot system (Figure 5.1)."'))
R(("intro", "term", 'Chapter contents box lists: "5.1 The Root", "5.2 The Stem", "5.3 The Leaf", "5.4 The Inflorescence", "5.5 The Flower", "5.6 The Fruit", "5.7 The Seed", "5.8 Semi-technical Description of a Typical Flowering Plant", "5.9 Description of Some Important Families"'))
R(("Fig 5.1", "caption", 'Figure caption (verbatim): "Figure 5.1  Parts of a flowering plant"'))
R(("Fig 5.1", "figure-labels", 'Figure labels: "Flower"; "Fruit"; "Stem"; "Leaf"; "Node"; "Internode"; "Bud"; "Primary root"; "Secondary root"; "Shoot system"; "Root system"'))

# ---------------- 5.1 The Root ----------------
R(("5.1", "heading", 'Numbered section heading: "5.1 THE ROOT"'))
R(("5.1", "opener", '"In majority of the dicotyledonous plants, the direct elongation of the radicle leads to the formation of primary root which grows inside the soil." (qualifier: majority)'))
R(("5.1", "term", '"It bears lateral roots of several orders that are referred to as secondary, tertiary, etc. roots."'))
R(("5.1", "example", '"The primary roots and its branches constitute the tap root system, as seen in the mustard plant (Figure 5.2a)."'))
R(("5.1", "comparison", '"In monocotyledonous plants, the primary root is short lived and is replaced by a large number of roots."'))
R(("5.1", "example", '"These roots originate from the base of the stem and constitute the fibrous root system, as seen in the wheat plant (Figure 5.2b)."'))
R(("5.1", "example", '"In some plants, like grass, Monstera and the banyan tree, roots arise from parts of the plant other than the radicle and are called adventitious roots (Figure 5.2c)." (qualifier: some)'))
R(("5.1", "number", '"The main functions of the root system are absorption of water and minerals from the soil, providing a proper anchorage to the plant parts, storing reserve food material and synthesis of plant growth regulators." (four functions)'))
R(("Fig 5.2", "caption", 'Figure caption (verbatim): "Figure 5.2 Different types of roots : (a) Tap  (b) Fibrous  (c) Adventitious"'))
R(("Fig 5.2", "figure-labels", 'Figure labels: "Main root"; "Laterals"; "Fibrous roots"; "Adventitious roots"'))

# ---------------- 5.1.1 Regions of the Root ----------------
R(("5.1.1", "heading", 'Numbered section heading: "5.1.1 Regions of the Root"'))
R(("5.1.1", "opener", '"The root is covered at the apex by a thimble-like structure called the root cap (Figure 5.3)."'))
R(("5.1.1", "fact", '"It protects the tender apex of the root as it makes its way through the soil."'))
R(("5.1.1", "number", '"A few millimetres above the root cap is the region of meristematic activity." (distance: a few millimetres)'))
R(("5.1.1", "fact", '"The cells of this region are very small, thin-walled and with dense protoplasm."'))
R(("5.1.1", "fact", '"They divide repeatedly."'))
R(("5.1.1", "process", '"The cells proximal to this region undergo rapid elongation and enlargement and are responsible for the growth of the root in length."'))
R(("5.1.1", "term", '"This region is called the region of elongation."'))
R(("5.1.1", "process", '"The cells of the elongation zone gradually differentiate and mature."'))
R(("5.1.1", "term", '"Hence, this zone, proximal to region of elongation, is called the region of maturation."'))
R(("5.1.1", "qualifier", '"From this region some of the epidermal cells form very fine and delicate, thread-like structures called root hairs." (qualifier: some)'))
R(("5.1.1", "fact", '"These root hairs absorb water and minerals from the soil."'))
R(("Fig 5.3", "caption", 'Figure caption (verbatim): "Figure 5.3  The regions of the root-tip"'))
R(("Fig 5.3", "figure-labels", 'Figure labels: "Region of maturation"; "Root hair"; "Region of elongation"; "Region of meristematic activity"; "Root cap"'))

# ---------------- 5.2 The Stem ----------------
R(("5.2", "heading", 'Numbered section heading: "5.2 THE STEM"'))
R(("5.2", "opener", '"What are the features that distinguish a stem from a root?" (in-text question that opens 5.2; answered by the rows below and by summary row S7)'))
R(("5.2", "definition", '"The stem is the ascending part of the axis bearing branches, leaves, flowers and fruits."'))
R(("5.2", "fact", '"It develops from the plumule of the embryo of a germinating seed."'))
R(("5.2", "term", '"The stem bears nodes and internodes."'))
R(("5.2", "definition", '"The region of the stem where leaves are born are called nodes while internodes are the portions between two nodes."'))
R(("5.2", "qualifier", '"The stem bears buds, which may be terminal or axillary." (qualifier: may)'))
R(("5.2", "qualifier", '"Stem is generally green when young and later often become woody and dark brown." (qualifiers: generally, often)'))
R(("5.2", "fact", '"The main function of the stem is spreading out branches bearing leaves, flowers and fruits."'))
R(("5.2", "fact", '"It conducts water, minerals and photosynthates."'))
R(("5.2", "qualifier", '"Some stems perform the function of storage of food, support, protection and of vegetative propagation." (qualifier: some)'))

# ---------------- 5.3 The Leaf ----------------
R(("5.3", "heading", 'Numbered section heading: "5.3 THE LEAF"'))
R(("5.3", "opener", '"The leaf is a lateral, generally flattened structure borne on the stem." (qualifier: generally)'))
R(("5.3", "fact", '"It develops at the node and bears a bud in its axil."'))
R(("5.3", "fact", '"The axillary bud later develops into a branch."'))
R(("5.3", "fact", '"Leaves originate from shoot apical meristems and are arranged in an acropetal order."'))
R(("5.3", "fact", '"They are the most important vegetative organs for photosynthesis."'))
R(("5.3", "number", '"A typical leaf consists of three main parts:  leaf base, petiole and lamina (Figure 5.4 a)." (count: three)'))
R(("5.3", "number", '"The leaf is attached to the stem by the leaf base and may bear two lateral small leaf like structures called stipules." (qualifier: may; count: two)'))
R(("5.3", "comparison", '"In monocotyledons, the leaf base expands into a sheath covering the stem partially or wholly."'))
R(("5.3", "qualifier", '"In some leguminous plants the leafbase may become swollen, which is called the pulvinus." (qualifiers: some, may; NCERT spelling "leafbase" preserved)'))
R(("5.3", "fact", '"The petiole help hold the blade to light."'))
R(("5.3", "fact", '"Long thin flexible petioles allow leaf blades to flutter in wind, thereby cooling the leaf and bringing fresh air to leaf surface."'))
R(("5.3", "definition", '"The lamina or the leaf blade is the green expanded part of the leaf with veins and veinlets."'))
R(("5.3", "qualifier", '"There is, usually, a middle prominent vein, which is known as the midrib." (qualifier: usually)'))
R(("5.3", "fact", '"Veins provide rigidity to the leaf blade and act as channels of transport for water, minerals and food materials."'))
R(("5.3", "fact", '"The shape, margin, apex, surface and extent of incision of lamina varies in different leaves."'))
R(("Fig 5.4", "caption", 'Figure caption (verbatim): "Figure 5.4 Structure of a leaf : (a) Parts of a leaf (b) Reticulate venation (c) Parallel venation"'))
R(("Fig 5.4", "figure-labels", 'Figure labels: "Lamina"; "Stipule"; "Petiole"; "Leaf base"; "Axillary bud"'))

# ---------------- 5.3.1 Venation ----------------
R(("5.3.1", "heading", 'Numbered section heading: "5.3.1 Venation"'))
R(("5.3.1", "opener", '"The arrangement of veins and the veinlets in the lamina of leaf is termed as venation."'))
R(("5.3.1", "definition", '"When the veinlets form a network, the venation is termed as reticulate (Figure 5.4 b)."'))
R(("5.3.1", "definition", '"When the veins run parallel to each other within a lamina, the venation is termed as parallel (Figure 5.4 c)."'))
R(("5.3.1", "qualifier", '"Leaves of dicotyledonous plants generally possess reticulate venation, while parallel venation is the characteristic of most monocotyledons." (qualifiers: generally, most)'))

# ---------------- 5.3.2 Types of Leaves ----------------
R(("5.3.2", "heading", 'Numbered section heading: "5.3.2 Types of Leaves"'))
R(("5.3.2", "opener", '"A leaf is said to be simple, when its lamina is entire or when incised, the incisions do not touch the midrib."'))
R(("5.3.2", "definition", '"When the incisions of the lamina reach up to the midrib breaking it into a number of leaflets, the leaf is called compound."'))
R(("5.3.2", "exception", '"A bud is present in the axil of petiole in both simple and compound leaves, but not in the axil of leaflets of the compound leaf." (exception: but not)'))
R(("5.3.2", "number", '"The compound leaves may be of two types (Figure 5.5)." (count: two)'))
R(("5.3.2", "example", '"In a pinnately compound leaf a number of leaflets are present on a common axis, the rachis, which represents the midrib of the leaf as in neem."'))
R(("5.3.2", "example", '"In palmately compound leaves, the leaflets are attached at a common point, i.e., at the tip of petiole, as in silk cotton."'))
R(("Fig 5.5", "caption", 'Figure caption (verbatim): "Figure 5.5 Compound leaves : (a) pinnately compound leaf (b) palmately compound leaf"'))
R(("Fig 5.5", "figure-labels", 'Figure labels: "Rachis"; "Neem"; "Silk Cotton"'))

# ---------------- 5.3.3 Phyllotaxy ----------------
R(("5.3.3", "heading", 'Numbered section heading: "5.3.3 Phyllotaxy"'))
R(("5.3.3", "opener", '"Phyllotaxy is the pattern of arrangement of leaves on the stem or branch."'))
R(("5.3.3", "number", '"This is usually of three types – alternate, opposite and whorled (Figure 5.6)." (qualifier: usually; count: three)'))
R(("5.3.3", "example", '"In alternate type of phyllotaxy,  a single leaf arises at each node in alternate manner, as in china rose, mustard and sun flower plants."'))
R(("5.3.3", "example", '"In opposite type, a pair of leaves arise at each node and lie opposite to each other as in Calotropis and guava plants."'))
R(("5.3.3", "example", '"If more than two leaves arise at a node and form a whorl, it is called whorled, as in Alstonia."'))
R(("Fig 5.6", "caption", 'Figure caption (verbatim): "Figure 5.6 Different types of phyllotaxy : (a) Alternate (b) Opposite (c) Whorled"'))
R(("Fig 5.6", "figure-labels", 'Figure labels: "China rose"; "Guava"; "Alstonia"'))

# ---------------- 5.4 The Inflorescence ----------------
R(("5.4", "heading", 'Numbered section heading: "5.4 THE INFLORESCENCE"'))
R(("5.4", "opener", '"A flower is a modified shoot wherein the shoot apical meristem changes to floral meristem."'))
R(("5.4", "fact", '"Internodes do not elongate and the axis gets condensed."'))
R(("5.4", "fact", '"The apex produces different kinds of floral appendages laterally at successive nodes instead of leaves."'))
R(("5.4", "qualifier", '"When a shoot tip transforms into a flower, it is always solitary." (qualifier: always)'))
R(("5.4", "definition", '"The arrangement of flowers on the floral axis is termed as inflorescence."'))
R(("5.4", "number", '"Depending on whether the apex gets developed into a flower or continues to grow, two major types of inflorescences are defined – racemose and cymose." (count: two)'))
R(("5.4", "definition", '"In racemose type of inflorescences the main axis continues to grow, the flowers are borne laterally in an acropetal succession (Figure 5.7)."'))
R(("5.4", "definition", '"In cymose type of  inflorescence the main axis terminates in a flower, hence is limited in growth."'))
R(("5.4", "fact", '"The flowers are borne in a basipetal order (Figure 5.8)."'))
R(("Fig 5.7", "caption", 'Figure caption (verbatim): "Figure 5.7  Racemose inflorescence"'))
R(("Fig 5.8", "caption", 'Figure caption (verbatim): "Figure 5.8  Cymose inflorescence"'))

# ---------------- 5.5 The Flower ----------------
R(("5.5", "heading", 'Numbered section heading: "5.5 THE FLOWER"'))
R(("5.5", "opener", '"The flower is the reproductive unit in the angiosperms."'))
R(("5.5", "fact", '"It is meant for sexual reproduction."'))
R(("5.5", "number", '"A typical flower has four different kinds of whorls arranged successively on the swollen end of the stalk or pedicel, called thalamus or receptacle." (count: four)'))
R(("5.5", "term", '"These are calyx, corolla, androecium and gynoecium."'))
R(("5.5", "comparison", '"Calyx and corolla are accessory organs, while androecium and gynoecium are reproductive organs."'))
R(("5.5", "qualifier", '"In some flowers like lily, the calyx and corolla are not distinct and are termed as perianth." (qualifier: some)'))
R(("5.5", "definition", '"When a flower has both androecium and gynoecium, it is bisexual."'))
R(("5.5", "qualifier", '"A flower having either only stamens or only carpels is unisexual." (qualifier: only)'))
R(("5.5", "qualifier", '"In symmetry, the flower may be actinomorphic (radial symmetry) or zygomorphic (bilateral symmetry)." (qualifier: may)'))
R(("5.5", "definition", '"When a flower can be divided into two equal radial halves in any radial plane passing through the centre, it is said to be actinomorphic, e.g., mustard, datura, chilli."'))
R(("5.5", "definition", '"When it can be divided into two similar halves only in one particular vertical plane, it is zygomorphic, e.g., pea, gulmohur, bean, Cassia." (qualifier: only)'))
R(("5.5", "definition", '"A flower is asymmetric (irregular) if it cannot be divided into two similar halves by any vertical plane passing through the centre, as in canna."'))
R(("5.5", "number", '"A flower may be trimerous, tetramerous or pentamerous when the floral appendages are in multiple of 3, 4 or 5, respectively." (counts: 3, 4, 5)'))
R(("5.5", "definition", '"Flowers with bracts-reduced leaf found at the base of the pedicel-are called bracteate and those without bracts, ebracteate."'))
R(("5.5", "term", '"Based on the position of calyx, corolla and androecium in respect of the ovary on thalamus, the flowers are described as hypogynous, perigynous and epigynous (Figure 5.9)."'))
R(("5.5", "definition", '"In the hypogynous flower the gynoecium occupies the highest position while the other parts are situated below it."'))
R(("5.5", "example", '"The ovary in such flowers is said to be superior, e.g., mustard, china rose and brinjal."'))
R(("5.5", "definition", '"If gynoecium is situated in the centre and other parts of the flower are located on the rim of the thalamus almost at the same level, it is called perigynous."'))
R(("5.5", "example", '"The ovary here is said to be half inferior, e.g., plum, rose, peach."'))
R(("5.5", "definition", '"In epigynous flowers, the margin of thalamus grows upward enclosing the ovary completely and getting fused with it, the other parts of flower arise above the ovary."'))
R(("5.5", "example", '"Hence, the ovary is said to be inferior as in flowers of guava and cucumber, and the ray florets of sunflower."'))
R(("Fig 5.9", "caption", 'Figure caption (verbatim): "Figure 5.9 Position of floral parts on thalamus : (a) Hypogynous (b)  and (c) Perigynous  (d) Epigynous"'))

# ---------------- 5.5.1 Parts of a Flower ----------------
R(("5.5.1", "heading", 'Numbered section heading: "5.5.1 Parts of a Flower"'))
R(("5.5.1", "opener", '"Each flower normally has four floral whorls, viz., calyx, corolla, androecium and gynoecium (Figure 5.10)." (qualifier: normally; count: four)'))
R(("Fig 5.10", "caption", 'Figure caption (verbatim): "Figure 5.10  Parts of a flower"'))
R(("Fig 5.10", "figure-labels", 'Figure labels: "Androecium"; "Gynoecium"; "Corolla"; "Calyx"; "Pedicel"'))

# ---------------- 5.5.1.1 Calyx ----------------
R(("5.5.1.1", "heading", 'Numbered section heading: "5.5.1.1 Calyx"'))
R(("5.5.1.1", "opener", '"The calyx is the outermost whorl of the flower and the members are called sepals."'))
R(("5.5.1.1", "qualifier", '"Generally, sepals are green, leaf like and protect the flower in the bud stage." (qualifier: generally)'))
R(("5.5.1.1", "definition", '"The calyx may be gamosepalous (sepals united) or polysepalous (sepals free)." (qualifier: may)'))

# ---------------- 5.5.1.2 Corolla ----------------
R(("5.5.1.2", "heading", 'Numbered section heading: "5.5.1.2 Corolla"'))
R(("5.5.1.2", "opener", '"Corolla is composed of petals."'))
R(("5.5.1.2", "qualifier", '"Petals are usually brightly coloured to attract insects for pollination." (qualifier: usually)'))
R(("5.5.1.2", "definition", '"Like calyx, corolla may also be gamopetalous (petals united) or polypetalous (petals free)."'))
R(("5.5.1.2", "fact", '"The shape and colour of corolla vary greatly in plants."'))
R(("5.5.1.2", "qualifier", '"Corolla may be tubular, bell-shaped, funnel-shaped or wheel-shaped." (qualifier: may)'))
R(("5.5.1.2", "heading", 'Unnumbered run-in sub-heading: "Aestivation:"'))
R(("5.5.1.2", "definition", '"Aestivation: The mode of arrangement of sepals or petals in floral bud with respect to the other members of the same whorl is known as aestivation."'))
R(("5.5.1.2", "number", '"The main types of aestivation are valvate, twisted, imbricate and vexillary (Figure 5.11)." (count: four)'))
R(("5.5.1.2", "definition", '"When sepals or petals in a whorl just touch one another at the margin, without overlapping, as in Calotropis, it is said to be valvate."'))
R(("5.5.1.2", "definition", '"If one margin of  the appendage overlaps that of the next one and so on as in china rose, lady\u2019s finger and cotton, it is called twisted."'))
R(("5.5.1.2", "definition", '"If the margins of sepals or petals overlap one another but not in any particular direction as in Cassia and gulmohur, the aestivation is called imbricate."'))
R(("5.5.1.2", "number", '"In pea and bean flowers, there are five petals, the largest (standard) overlaps the two lateral petals (wings) which in turn overlap the two smallest anterior petals (keel);  this type of aestivation is known as vexillary or papilionaceous." (counts: five, two, two)'))
R(("Fig 5.11", "caption", 'Figure caption (verbatim): "Figure 5.11 Types of aestivation in corolla : (a) Valvate (b) Twisted (c) Imbricate (d) Vexillary"'))

# ---------------- 5.5.1.3 Androecium ----------------
R(("5.5.1.3", "heading", 'Numbered section heading: "5.5.1.3 Androecium"'))
R(("5.5.1.3", "opener", '"Androecium is composed of stamens."'))
R(("5.5.1.3", "definition", '"Each stamen which represents the male reproductive organ consists of a stalk or a filament and an anther."'))
R(("5.5.1.3", "number", '"Each anther is usually bilobed and each lobe has two chambers, the pollen-sacs." (qualifier: usually; count: two)'))
R(("5.5.1.3", "fact", '"The pollen grains are produced in pollen-sacs."'))
R(("5.5.1.3", "definition", '"A sterile stamen is called staminode."'))
R(("5.5.1.3", "qualifier", '"Stamens of flower may be united with other members such as petals or among themselves." (qualifier: may)'))
R(("5.5.1.3", "example", '"When stamens are attached to the petals, they are epipetalous as in brinjal, or epiphyllous when attached to the perianth as in the flowers of lily."'))
R(("5.5.1.3", "qualifier", '"The stamens in a flower may either remain free (polyandrous) or may be united in varying degrees." (qualifier: may)'))
R(("5.5.1.3", "example", '"The stamens may be united into one bunch or one bundle (monoadelphous) as in china rose, or two bundles (diadelphous) as in pea, or into more than two  bundles (polyadelphous) as in citrus." (NCERT spelling "monoadelphous" preserved)'))
R(("5.5.1.3", "example", '"There may be a variation in the length of filaments within a flower, as in Salvia and mustard."'))

# ---------------- 5.5.1.4 Gynoecium ----------------
R(("5.5.1.4", "heading", 'Numbered section heading: "5.5.1.4 Gynoecium"'))
R(("5.5.1.4", "opener", '"Gynoecium is the female reproductive part of the flower and is made up of one or more carpels."'))
R(("5.5.1.4", "number", '"A carpel consists of three parts namely stigma, style and ovary." (count: three)'))
R(("5.5.1.4", "definition", '"Ovary is the enlarged basal part, on which lies the elongated tube, the style."'))
R(("5.5.1.4", "fact", '"The style connects the ovary to the stigma."'))
R(("5.5.1.4", "qualifier", '"The stigma is usually at the tip of the style and is the receptive surface for pollen grains." (qualifier: usually)'))
R(("5.5.1.4", "definition", '"Each ovary bears one or more ovules attached to a flattened, cushion-like placenta."'))
R(("5.5.1.4", "example", '"When more than one carpel is present, they may be free (as in lotus and rose) and are called apocarpous."'))
R(("5.5.1.4", "example", '"They are termed syncarpous when carpels are fused, as in mustard and tomato."'))
R(("5.5.1.4", "process", '"After fertilisation, the ovules develop into seeds and the ovary matures into a fruit."'))
R(("5.5.1.4", "heading", 'Unnumbered run-in sub-heading: "Placentation:"'))
R(("5.5.1.4", "definition", '"Placentation: The arrangement of ovules within the ovary is known as placentation."'))
R(("5.5.1.4", "number", '"The placentation are of different types namely, marginal, axile, parietal, basal, central and free central (Figure 5.12)." (six names listed; the chapter describes and figures five — see source note SRC-1)'))
R(("5.5.1.4", "definition", '"In marginal  placentation the placenta forms a ridge along the ventral suture of the ovary and the ovules are borne on this ridge forming two rows, as in pea."'))
R(("5.5.1.4", "definition", '"When the  placenta is axial and the ovules are attached to it in a multilocular ovary, the placentaion is said to be axile, as in china rose, tomato and lemon." (NCERT spelling "placentaion" preserved)'))
R(("5.5.1.4", "definition", '"In parietal placentation, the ovules develop on the inner wall of the ovary or on peripheral part."'))
R(("5.5.1.4", "example", '"Ovary is one-chambered but it becomes two-chambered due to the formation of the false septum, e.g., mustard and Argemone."'))
R(("5.5.1.4", "definition", '"When the ovules are borne on central axis and septa are absent, as in Dianthus and Primrose the placentation is called free central."'))
R(("5.5.1.4", "definition", '"In basal placentation, the placenta develops at the base of ovary and a single ovule is attached to it, as in sunflower, marigold."'))
R(("Fig 5.12", "caption", 'Figure caption (verbatim): "Figure 5.12 Types of placentation : (a) Marginal (b) Axile (c) Parietal (d) Free central (e) Basal"'))

# ---------------- 5.6 The Fruit ----------------
R(("5.6", "heading", 'Numbered section heading: "5.6 THE FRUIT"'))
R(("5.6", "opener", '"The fruit is a characteristic feature of the flowering plants."'))
R(("5.6", "definition", '"It is a mature or ripened ovary, developed after fertilisation."'))
R(("5.6", "definition", '"If a fruit is formed without fertilisation of the ovary, it is called a parthenocarpic fruit."'))
R(("5.6", "qualifier", '"Generally, the fruit consists of a wall or pericarp and seeds." (qualifier: generally)'))
R(("5.6", "qualifier", '"The pericarp may be dry or fleshy." (qualifier: may)'))
R(("5.6", "term", '"When pericarp is thick and fleshy, it is differentiated into the outer epicarp, the middle mesocarp and the inner endocarp."'))
R(("5.6", "example", '"In mango and coconut, the fruit is known as a drupe (Figure 5.13)."'))
R(("5.6", "number", '"They develop from monocarpellary superior ovaries and are one seeded." (count: one)'))
R(("5.6", "example", '"In mango the pericarp is well differentiated into an outer thin epicarp, a middle fleshy edible mesocarp and an inner stony hard endocarp."'))
R(("5.6", "comparison", '"In coconut which is also a drupe, the mesocarp is fibrous."'))
R(("Fig 5.13", "caption", 'Figure caption (verbatim): "Figure 5.13  Parts of a fruit : (a) Mango  (b) Coconut"'))
R(("Fig 5.13", "figure-labels", 'Figure labels: "Epicarp"; "Mesocarp"; "Seed"; "Endocarp"'))

# ---------------- 5.7 The Seed ----------------
R(("5.7", "heading", 'Numbered section heading: "5.7 THE SEED"'))
R(("5.7", "opener", '"The ovules after fertilisation, develop into seeds."'))
R(("5.7", "definition", '"A seed is made up of a seed coat and an embryo."'))
R(("5.7", "number", '"The embryo is made up of a radicle, an embryonal axis and one (as in wheat, maize) or two cotyledons (as in gram and pea)." (counts: one, two)'))

# ---------------- 5.7.1 Structure of a Dicotyledonous Seed ----------------
R(("5.7.1", "heading", 'Numbered section heading: "5.7.1 Structure of a Dicotyledonous Seed"'))
R(("5.7.1", "opener", '"The outermost covering of a seed is the seed coat."'))
R(("5.7.1", "number", '"The seed coat has two layers, the outer testa and the inner tegmen." (count: two)'))
R(("5.7.1", "definition", '"The hilum is a scar on the seed coat through which the developing seeds were attached to the fruit."'))
R(("5.7.1", "definition", '"Above the hilum is a small pore called the micropyle."'))
R(("5.7.1", "number", '"Within the seed coat is the embryo, consisting of an embryonal axis and two cotyledons." (count: two)'))
R(("5.7.1", "qualifier", '"The cotyledons are often fleshy and full of reserve food materials." (qualifier: often)'))
R(("5.7.1", "number", '"At the two ends of the embryonal axis are present the radicle and the plumule (Figure 5.14)." (count: two)'))
R(("5.7.1", "example", '"In some seeds such as castor the endosperm formed as a result of double fertilisation, is a food storing tissue and called endospermic seeds." (qualifier: some)'))
R(("5.7.1", "example", '"In plants such as bean, gram and pea, the endosperm is not present in mature seeds and such seeds are called non-endospermous."'))
R(("Fig 5.14", "caption", 'Figure caption (verbatim): "Figure 5.14 Structure of dicotyledonous seed"'))
R(("Fig 5.14", "figure-labels", 'Figure labels: "Seed coat"; "Cotyledon"; "Plumule"; "Hilum"; "Micropyle"; "Radicle"'))

# ---------------- 5.7.2 Structure of Monocotyledonous Seed ----------------
R(("5.7.2", "heading", 'Numbered section heading: "5.7.2 Structure of Monocotyledonous Seed"'))
R(("5.7.2", "opener", '"Generally, monocotyledonous seeds are endospermic but some as in orchids are non-endospermic." (qualifiers: generally, but some)'))
R(("5.7.2", "qualifier", '"In the seeds of cereals such as maize the seed coat is membranous and generally fused with the fruit wall." (qualifier: generally)'))
R(("5.7.2", "fact", '"The endosperm is bulky and stores food."'))
R(("5.7.2", "definition", '"The outer covering of endosperm separates the embryo by a proteinous layer called aleurone layer."'))
R(("5.7.2", "fact", '"The embryo is   small and situated in a groove at one end of the endosperm."'))
R(("5.7.2", "definition", '"It consists of one large and shield shaped cotyledon known as scutellum and a short axis with a plumule and a radicle."'))
R(("5.7.2", "definition", '"The plumule and radicle are enclosed in sheaths which are called coleoptile and coleorhiza  respectively (Figure 5.15)."'))
R(("Fig 5.15", "caption", 'Figure caption (verbatim): "Figure 5.15 Structure of a monocotyledonous seed"'))
R(("Fig 5.15", "figure-labels", 'Figure labels: "Seed coat & fruit-wall"; "Aleurone layer"; "Endosperm"; "Scutellum"; "Coleoptile"; "Plumule"; "Radicle"; "Coleorhiza"; "Embryo"'))

# ---------------- 5.8 Semi-technical description ----------------
R(("5.8", "heading", 'Numbered section heading: "5.8 SEMI-TECHNICAL DESCRIPTION OF A TYPICAL FLOWERING PLANT"'))
R(("5.8", "opener", '"Various morphological features are used to describe a flowering plant."'))
R(("5.8", "fact", '"The description has to be brief, in a simple and scientific language and presented in a proper sequence."'))
R(("5.8", "process", '"The plant is described beginning with its habit, vegetative characters – roots, stem and leaves and then floral characters inflorescence and flower parts."'))
R(("5.8", "process", '"After describing various parts of plant, a floral diagram and a floral formula are presented."'))
R(("5.8", "fact", '"The floral formula is represented by some symbols."'))
R(("5.8", "term", 'Floral-formula symbol key (verbatim, read from the page image because the text layer drops the glyphs): "Br stands for bracteate", "K stands for calyx", "C for corolla", "P for perianth", "A for androecium", "G for Gynoecium", G underlined "for superior ovary", G overlined "for inferior ovary", male symbol "for male", female symbol "for female", combined male-female symbol "for bisexual plants", circled-plus "for actinomorphic", per-cent symbol "for zygomorphic nature of flower"'))
R(("5.8", "term", '"Fusion is indicated by enclosing the figure within bracket and adhesion by a line drawn above the symbols of the floral parts."'))
R(("5.8", "fact", '"A floral diagram provides information about the number of parts of a flower, their arrangement and the relation they have with one another (Figure 5.16)."'))
R(("5.8", "fact", '"The position of the mother axis with respect to the flower is represented by a dot on the top of the floral diagram."'))
R(("5.8", "process", '"Calyx, corolla, androecium and gynoecium are drawn in successive whorls, calyx being the outermost and the gynoecium being in the centre."'))
R(("5.8", "fact", '"Floral formula also shows cohesion and adhesion within parts of whorls and between whorls."'))
R(("5.8", "example", '"The floral diagram and floral formula in Figure 5.16 represents the mustard plant (Family: Brassicaceae)."'))
R(("Fig 5.16", "caption", 'Figure caption (verbatim): "Figure 5.16 Floral diagram with floral formula"'))
R(("Fig 5.16", "figure-labels", 'Figure labels: "K2+2 C4 A2+4 G(2)"'))

# ---------------- 5.9 Solanaceae ----------------
R(("5.9", "heading", 'Numbered section heading: "5.9 SOLANACEAE" (the chapter contents box titles this section "5.9 Description of Some Important Families" — see source note SRC-2)'))
R(("5.9", "opener", '"It is a large family, commonly called as the \u2018potato family\u2019." ("It" = Solanaceae, named only in the section heading)'))
R(("5.9", "fact", '"It is widely distributed in tropics, subtropics and even temperate zones (Figure 5.17)."'))
R(("5.9", "heading", 'Unnumbered sub-heading: "Vegetative Characters"'))
R(("5.9", "qualifier", '"Plants mostly herbs, shrubs and rarely small trees" (qualifiers: mostly, rarely)'))
R(("5.9", "example", '"Stem: herbaceous rarely woody, aerial; erect, cylindrical, branched, solid or hollow, hairy or glabrous, underground stem in potato (Solanum tuberosum)" (qualifier: rarely)'))
R(("5.9", "qualifier", '"Leaves: alternate, simple, rarely pinnately compound, exstipulate; venation reticulate" (qualifier: rarely)'))
R(("5.9", "heading", 'Unnumbered sub-heading: "Floral Characters"'))
R(("5.9", "example", '"Inflorescence : Solitary, axillary or cymose as in Solanum"'))
R(("5.9", "term", '"Flower: bisexual, actinomorphic"'))
R(("5.9", "number", '"Calyx: sepals five, united, persistent, valvate aestivation" (count: five)'))
R(("5.9", "number", '"Corolla: petals five, united; valvate aestivation" (count: five)'))
R(("5.9", "number", '"Androecium: stamens five, epipetalous" (count: five)'))
R(("5.9", "term", '"Gynoecium: bicarpellary obligately placed, syncarpous; ovary superior, bilocular, placenta swollen with many ovules, axile" (NCERT wording "obligately" preserved — see source note SRC-3)'))
R(("5.9", "term", '"Fruits: berry or capsule"'))
R(("5.9", "qualifier", '"Seeds: many, endospermous" (qualifier: many)'))
R(("5.9", "term", 'Solanaceae floral formula (verbatim, read from the page image): "Floral Formula:" circled-plus, bisexual symbol, "K(5) C(5) A5 G(2)" with an adhesion arc over C and A and G underlined for superior ovary'))
R(("5.9", "heading", 'Unnumbered sub-heading: "Economic Importance"'))
R(("5.9", "example", '"Many plants belonging to this family are source of food (tomato, brinjal, potato), spice (chilli); medicine (belladonna, ashwagandha);  fumigatory (tobacco); ornamentals (petunia)." (qualifier: many)'))
R(("Fig 5.17", "caption", 'Figure caption (verbatim): "Figure 5.17 Solanum nigrum (makoi) plant :  (a) Flowering twig  (b) Flower (c) L.S. of flower  (d) Stamens  (e) Carpel  (f) Floral diagram"'))

# ---------------- SUMMARY ----------------
R(("SUMMARY", "heading", 'Structural heading: "SUMMARY"'))
R(("summary", "summary-unique", '"Flowering plants exhibit enormous variation in shape, size, structure, mode of nutrition, life span, habit and habitat." (SUMMARY-UNIQUE — mode of nutrition, life span, habit and habitat are named nowhere in the body; fold into the chapter intro)'))
R(("summary", "summary-unique", '"The roots in some plants get modified for storage of food, mechanical support and respiration." (SUMMARY-UNIQUE — root modification for mechanical support and respiration is absent from the rationalised body; fold into 5.1; qualifier: some)'))
R(("summary", "summary-unique", '"The shoot system is differentiated into stem, leaves, flowers and fruits." (SUMMARY-UNIQUE — the body defines the shoot system only as the portion above ground; fold into the chapter intro)'))
R(("summary", "summary-unique", '"The morphological features of stems like the presence of nodes and internodes, multicellular hair and positively phototropic nature help to differentiate the stems from roots." (SUMMARY-UNIQUE — multicellular hair and positively phototropic nature are absent from the body; fold into 5.2, where it answers the section\u2019s opening question)'))
R(("summary", "summary-unique", '"Leaf is a lateral outgrowth of stem developed exogeneously at the node." (SUMMARY-UNIQUE — exogenous development is absent from the body; fold into 5.3; NCERT spelling "exogeneously" preserved)'))
R(("summary", "summary-unique", '"They vary in shape, size and period of viability." (SUMMARY-UNIQUE — seed shape, size and period of viability are absent from the body; fold into 5.7)'))
R(("summary", "summary-unique", '"The floral characteristics form the basis of classification and identification of flowering plants." (SUMMARY-UNIQUE — the body never states that floral characters are the basis of classification/identification; fold into 5.8)'))

# ---------------- EXERCISES ----------------
R(("EXERCISES", "heading", 'Structural heading: "EXERCISES"'))


SUMMARY_TABLE = [
    ("S1", "Flowering plants exhibit enormous variation in shape, size, structure, mode of nutrition, life span, habit and habitat.", "SUMMARY-UNIQUE", "{U1} \u2192 chapter intro"),
    ("S2", "They have well developed root and shoot systems.", "BODY-PRESENT", "intro (root system / shoot system)"),
    ("S3", "Root system is either tap root or fibrous.", "BODY-PRESENT", "\u00a75.1"),
    ("S4", "Generally, dicotyledonous plants have tap roots while monocotyledonous plants have fibrous roots.", "BODY-PRESENT", "\u00a75.1 (\u201cmajority of the dicotyledonous plants\u201d / \u201cIn monocotyledonous plants\u201d)"),
    ("S5", "The roots in some plants get modified for storage of food, mechanical support and respiration.", "SUMMARY-UNIQUE", "{U2} \u2192 \u00a75.1"),
    ("S6", "The shoot system is differentiated into stem, leaves, flowers and fruits.", "SUMMARY-UNIQUE", "{U3} \u2192 chapter intro"),
    ("S7", "The morphological features of stems like the presence of nodes and internodes, multicellular hair and positively phototropic nature help to differentiate the stems from roots.", "SUMMARY-UNIQUE", "{U4} \u2192 \u00a75.2"),
    ("S8", "Leaf is a lateral outgrowth of stem developed exogeneously at the node.", "SUMMARY-UNIQUE", "{U5} \u2192 \u00a75.3"),
    ("S9", "These are green in colour to perform the function of photosynthesis.", "BODY-PRESENT", "\u00a75.3 (\u201cmost important vegetative organs for photosynthesis\u201d; lamina \u201cgreen expanded part\u201d)"),
    ("S10", "Leaves exhibit marked variations in their shape, size, margin, apex and extent of incisions of leaf blade (lamina).", "BODY-PRESENT", "\u00a75.3 (\u201cshape, margin, apex, surface and extent of incision of lamina varies\u201d); \u201csize\u201d is carried by the S1 fold"),
    ("S11", "The flower is a modified shoot, meant for sexual reproduction.", "BODY-PRESENT", "\u00a75.4 + \u00a75.5"),
    ("S12", "The flowers are arranged in different types of inflorescences.", "BODY-PRESENT", "\u00a75.4"),
    ("S13", "They exhibit enormous variation in structure, symmetry, position of ovary in relation to other parts, arrangement of petals, sepals, ovules etc.", "BODY-PRESENT", "\u00a75.5 (symmetry, hypogynous/perigynous/epigynous), \u00a75.5.1.2 (aestivation), \u00a75.5.1.4 (placentation)"),
    ("S14", "After fertilisation, the ovary is modified into fruits and ovules into seeds.", "BODY-PRESENT", "\u00a75.5.1.4, \u00a75.6, \u00a75.7"),
    ("S15", "Seeds either may be monocotyledonous or dicotyledonous.", "BODY-PRESENT", "\u00a75.7.1, \u00a75.7.2"),
    ("S16", "They vary in shape, size and period of viability.", "SUMMARY-UNIQUE", "{U6} \u2192 \u00a75.7"),
    ("S17", "The floral characteristics form the basis of classification and identification of flowering plants.", "SUMMARY-UNIQUE", "{U7} \u2192 \u00a75.8"),
    ("S18", "This can be illustrated through semi-technical descriptions of families.", "BODY-PRESENT", "\u00a75.8 heading + \u00a75.9"),
    ("S19", "Hence, a flowering plant is described in a definite sequence by using scientific terms.", "BODY-PRESENT", "\u00a75.8 (\u201cproper sequence\u201d, \u201csimple and scientific language\u201d)"),
    ("S20", "The floral features are represented in the summarised form as floral diagrams and floral formula.", "BODY-PRESENT", "\u00a75.8"),
]

EXERCISES = [
    ("1", "How is a pinnately compound leaf different from a palmately compound leaf?", "COVERED", "\u00a75.3.2 + Fig 5.5"),
    ("2", "Explain with suitable examples the different types of phyllotaxy.", "COVERED", "\u00a75.3.3 + Fig 5.6"),
    ("3", "Define the following terms: (a) aestivation (b) placentation (c) actinomorphic (d) zygomorphic (e) superior ovary (f) perigynous flower (g) epipetalous stamen", "COVERED", "(a) \u00a75.5.1.2 \u00b7 (b) \u00a75.5.1.4 \u00b7 (c),(d) \u00a75.5 \u00b7 (e),(f) \u00a75.5 \u00b7 (g) \u00a75.5.1.3"),
    ("4", "Differentiate between (a) Racemose and cymose inflorescence (b) Apocarpous and syncarpous ovary", "COVERED", "(a) \u00a75.4 \u00b7 (b) \u00a75.5.1.4"),
    ("5", "Draw the labelled diagram of the following: (i) gram seed (ii) V.S. of maize seed", "COVERED", "(i) \u00a75.7.1 + Fig 5.14 (gram named in \u00a75.7 / \u00a75.7.1) \u00b7 (ii) \u00a75.7.2 + Fig 5.15 (maize named in \u00a75.7.2)"),
    ("6", "Take one flower of the family Solanaceae and write its semi-technical description. Also draw their floral diagram.", "COVERED", "\u00a75.9 + Fig 5.17(f)"),
    ("7", "Describe the various types of placentations found in flowering plants.", "COVERED", "\u00a75.5.1.4 + Fig 5.12 \u2014 five types described and figured; see source note SRC-1"),
    ("8", "What is a flower? Describe the parts of a typical angiosperm flower.", "COVERED", "\u00a75.5, \u00a75.5.1\u2013\u00a75.5.1.4 + Figs 5.10, 5.11"),
    ("9", "Define the term inflorescence. Explain the basis for the different types inflorescence in flowering plants.", "COVERED", "\u00a75.4 + Figs 5.7, 5.8"),
    ("10", "Describe the arrangement of floral members in relation to their insertion on thalamus.", "COVERED", "\u00a75.5 (hypogynous / perigynous / epigynous) + Fig 5.9"),
]

# (fig, caption, source page, in-figure label count) -- the crop rect is NOT restated
# here. It is imported from `extract_figures.py`, which is the single source of truth:
# a rect written in two places is a count written in two places, and the first draft of
# this file duplicated Fig 5.1's rect and immediately went stale after a re-pin.
MANIFEST = [
    ("5.1", "Parts of a flowering plant", 4, 11),
    ("5.2", "Different types of roots : (a) Tap  (b) Fibrous  (c) Adventitious", 4, 4),
    ("5.3", "The regions of the root-tip", 5, 5),
    ("5.4", "Structure of a leaf : (a) Parts of a leaf (b) Reticulate venation (c) Parallel venation", 6, 5),
    ("5.5", "Compound leaves : (a) pinnately compound leaf (b) palmately compound leaf", 6, 3),
    ("5.6", "Different types of phyllotaxy : (a) Alternate (b) Opposite (c) Whorled", 7, 3),
    ("5.7", "Racemose inflorescence", 7, 0),
    ("5.8", "Cymose inflorescence", 8, 0),
    ("5.9", "Position of floral parts on thalamus : (a) Hypogynous (b)  and (c) Perigynous  (d) Epigynous", 8, 0),
    ("5.10", "Parts of a flower", 9, 5),
    ("5.11", "Types of aestivation in corolla : (a) Valvate (b) Twisted (c) Imbricate (d) Vexillary", 10, 0),
    ("5.12", "Types of placentation : (a) Marginal (b) Axile (c) Parietal (d) Free central (e) Basal", 11, 0),
    ("5.13", "Parts of a fruit : (a) Mango  (b) Coconut", 12, 4),
    ("5.14", "Structure of dicotyledonous seed", 12, 6),
    ("5.15", "Structure of a monocotyledonous seed", 13, 9),
    ("5.16", "Floral diagram with floral formula", 13, 1),
    ("5.17", "Solanum nigrum (makoi) plant :  (a) Flowering twig  (b) Flower (c) L.S. of flower  (d) Stamens  (e) Carpel  (f) Floral diagram", 14, 0),
]


def crop_rects() -> dict[str, tuple[int, int, int, int]]:
    """Crop rects, imported from the extraction script rather than restated."""
    spec = importlib.util.spec_from_file_location("ef", EXTRACT)
    ef = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ef)
    rects = {fid.replace("_", "."): rect for fid, _, rect in ef.FIGS}
    pages = {fid.replace("_", "."): pno for fid, pno, _ in ef.FIGS}
    assert {f for f, _, _, _ in MANIFEST} == set(rects), "manifest and extraction script disagree on the figure set"
    for fig, _, page, _ in MANIFEST:
        assert pages[fig] == page, f"{fig}: manifest page {page} != extraction script page {pages[fig]}"
    return rects

# (fig, class, finding, change). "class" is one of:
#   ART  -- the inherited rect clipped artwork, an in-figure label or a panel marker
#   CAP  -- the inherited rect cut the printed caption through its glyph row
#   ---  -- the inherited rect was clean; re-pinned only for the artwork-only standard
#   +NEW -- a defect introduced by *this* session's first re-pin and caught before the freeze
# Every ART / CAP classification is machine-adjudicated by
# `scratch/ch5morph_gate1/adjudicate_inherited.py`, which measures each inherited rect
# against the plate's ink-and-image extent. The first draft of this log was asserted
# rather than derived and was wrong: it claimed "15 defects" while listing 16 IDs, and it
# recorded a Fig 5.14 clip (D11) inferred from the same watermark-polluted
# `get_drawings()` union that this session went on to reject. Fig 5.14's inherited rect
# was in fact clean.
REPIN_LOG = [
    ("5.1", "ART", "Right edge at x=315 clipped the last letter of the bracket label `Root system`; the plate\u2019s ink extends to x=315.6. Small, but it is a label.", "(78,95,315,405) \u2192 (88,98,325,404)"),
    ("5.2", "ART", "Left edge at x=78 cut the in-figure label `Laterals` clean off (ink starts at x=63.4), so the asset rendered it as \u201cerals\u201d. **The inherited tracker recorded this label as \u201cintentionally retained\u201d.** Clipped by 14.6 pt \u2014 the largest label defect in the set.", "(78,420,555,665) \u2192 (55,445,543,663)"),
    ("5.3", "CAP", "Bottom edge at y=345 cut the printed caption through its glyph row \u2014 only 84% of the caption line was inside the rect, so the descenders of \u201cFigure\u201d and \u201cregions\u201d were sliced. Artwork itself was intact.", "caption excluded; (285,112,520,345) \u2192 (283,128,525,334)"),
    ("5.4", "ART", "Bottom edge at y=435 fell **above** the panel markers `(b)` and `(c)` (they occupy y 441.4\u2013450.9), so both were absent from the asset entirely. Clipped by 14.9 pt.", "(45,95,278,435) \u2192 (50,97,267,456)"),
    ("5.5", "ART / +NEW", "Right edge at x=265 clipped the silk-cotton photograph, whose image bbox ends at x=271.0 \u2014 6.0 pt lost. This session\u2019s **first re-pin then introduced a new defect**: y0=499 sat above Fig 5.4\u2019s caption tail `(c) Parallel venation` (which ends at y=504.2) and bled it into the top of the plate. Caught by re-opening the asset; y0 moved to 506.", "(45,505,265,750) \u2192 (54,506,279,676)"),
    ("5.6", "ART", "Right edge at x=505 clipped the Guava photograph, whose image bbox ends at x=512.0 \u2014 7.0 pt lost. (Its ink bbox stops at 501.7 because the photo\u2019s background is light, which is why the raster bbox has to be unioned in for photographic plates.)", "(275,85,505,335) \u2192 (294,85,520,332)"),
    ("5.7", "---", "Clean. Re-pinned only to drop dead space and adopt the artwork-only standard. Confirmed by opening: a plain photograph with zero in-figure labels.", "(275,405,515,675) \u2192 (280,421,495,678)"),
    ("5.8", "CAP", "Bottom edge at y=245 cut the printed caption almost exactly in half \u2014 only 42% of the caption line was inside the rect. Artwork itself was intact.", "caption excluded; (50,95,278,245) \u2192 (54,97,280,237)"),
    ("5.9", "ART", "Bottom edge at y=660 cut the panel markers `(a)`\u2013`(d)` mid-glyph; they extend to y=666.2. Clipped by 6.2 pt.", "(62,480,515,660) \u2192 (72,480,522,674)"),
    ("5.10", "ART", "Right edge at x=510 clipped the label `Gynoecium`, which is **baked into the raster artwork** (image bbox ends at x=514.0) rather than present in the text layer \u2014 so no text-layer check could have seen it. The top edge at y=565 also grazed the prose line above, which ends at y=565.9, printing a sliver of body text along the top of the plate.", "(42,565,510,685) \u2192 (38,569,522,690)"),
    ("5.11", "---", "Clean. Re-pinned only to tighten margins.", "(125,95,475,305) \u2192 (129,97,466,300)"),
    ("5.12", "CAP", "Left edge at x=378 cut the leading `F` off the printed caption (its line starts at x=373.9). Artwork was intact \u2014 and note the inherited rect was 40 pt wider than the plate needs, because it had been pinned from a watermark-polluted drawings union.", "caption excluded; (378,85,520,735) \u2192 (394,95,497,630)"),
    ("5.13", "--- / +NEW", "Inherited rect was clean. This session\u2019s **first re-pin introduced a defect**: y1=229 clipped the panel markers `(a)`/`(b)`, which are baked into the artwork and reach y=235.5. Caught by the ink measurement before the freeze; y1 moved to 241.", "(188,90,505,265) \u2192 (204,96,490,241)"),
    ("5.14", "--- / +NEW", "Inherited rect was **clean** \u2014 this is the entry the first draft of this log got wrong, asserting a right-edge clip on the strength of a drawings union that reported x=299.9 when the plate\u2019s real ink ends at x=276.5. That 23 pt was watermark. Acting on it, this session\u2019s **first re-pin set x1=309 and bled the neighbouring prose column**, which starts at x=303.1. Caught by re-opening the asset.", "(48,465,285,605) \u2192 (54,478,286,608)"),
    ("5.15", "---", "Clean. Re-pinned only to exclude the printed caption and tighten margins.", "(72,90,485,345) \u2192 (84,97,471,303)"),
    ("5.16", "ART", "Right edge at x=515 clipped the floral diagram\u2019s hatched outer ring, whose ink reaches x=515.9. Small, but it is the figure\u2019s outermost whorl.", "caption excluded; (335,445,515,710) \u2192 (333,452,525,681)"),
    ("5.17", "CAP", "Bottom edge at y=690 cut the printed caption through its first glyph row \u2014 only 11% of that line was inside the rect, the worst caption cut in the set. Artwork itself was intact.", "caption excluded; (102,455,475,690) \u2192 (112,466,468,680)"),
]


def main() -> None:
    ids = [f"F{i:03d}" for i in range(1, len(ROWS) + 1)]
    types = collections.Counter(t for _, t, _ in ROWS)
    assert all(t == t.lower() for t in types), "Type vocabulary must be single-cased"
    assert sum(types.values()) == len(ROWS)

    def ids_of(kind):
        return [i for i, (_, t, _) in zip(ids, ROWS) if t == kind]

    headings, openers = ids_of("heading"), ids_of("opener")
    captions, uniques = ids_of("caption"), ids_of("summary-unique")
    labelrows = [(i, s, w) for i, (s, t, w) in zip(ids, ROWS) if t == "figure-labels"]
    per_fig = {s: len(re.findall(r'"([^"]+)"', w)) for _, s, w in labelrows}
    n_labels = sum(per_fig.values())

    numbered = [i for i, (_, t, w) in zip(ids, ROWS) if t == "heading" and w.startswith("Numbered")]
    unnumbered = [i for i, (_, t, w) in zip(ids, ROWS) if t == "heading" and w.startswith("Unnumbered")]
    structural = [i for i in headings if i not in numbered and i not in unnumbered]

    census = " \u00b7 ".join(f"`{t}` {n}" for t, n in sorted(types.items(), key=lambda kv: (-kv[1], kv[0])))
    fold_map = {f"U{n}": fid for n, fid in enumerate(uniques, start=1)}

    body_present = [s for s in SUMMARY_TABLE if s[2] == "BODY-PRESENT"]
    covered = [e for e in EXERCISES if e[2] == "COVERED"]
    gaps = [e for e in EXERCISES if e[2] != "COVERED"]

    out = []
    W = out.append

    W(f"# Frozen Inventory \u2014 Morphology of Flowering Plants (Class 11, Chapter 5)\n")
    W(f"Source: `{SRC}` | Frozen: {FROZEN} | Rows: {len(ROWS)}\n")
    W("**Counts (machine-derived from the Facts table by re-parsing it \u2014 never a hand tally). "
      "Regenerate with `scratch/ch5morph_gate1/build_inventory.py`.**\n")
    W(f"- Total Facts rows: **{len(ROWS)}** (IDs `{ids[0]}..{ids[-1]}`, contiguous, monotonic, no gaps, no duplicates, 0 ticked \u2014 Pass 2 does the ticking)")
    W(f"- Heading rows (`Type: heading`): **{len(headings)}** = {len(numbered)} numbered section headings + "
      f"{len(structural)} structural ({', '.join(structural)} \u2014 unit banner, chapter title, `SUMMARY`, `EXERCISES`) + "
      f"{len(unnumbered)} unnumbered sub-headings ({', '.join(unnumbered)})")
    W(f"- Opener rows (`Type: opener`): **{len(openers)}** = 1 chapter intro + {len(numbered)} numbered sections, one each")
    W(f"- Figure-label rows (`Type: figure-labels`): **{len(labelrows)}** label-bearing figures / **{n_labels}** in-figure labels "
      f"({' \u00b7 '.join(f'{k.replace(chr(70) + 'ig ', '')}={v}' for k, v in per_fig.items())})")
    W(f"- Caption rows (`Type: caption`): **{len(captions)}** = {len(MANIFEST)} figure captions + 1 scientist-profile caption")
    W(f"- Summary sentences classified: **{len(SUMMARY_TABLE)}** = {len(body_present)} BODY-PRESENT + {len(uniques)} SUMMARY-UNIQUE "
      f"(folds `{uniques[0]}`\u2013`{uniques[-1]}`)")
    W(f"- Exercises: **{len(EXERCISES)} exercises, {len(gaps)} answered by design (GAP), {len(covered)} unanswered by design (COVERED), 0 overlooked**")
    W(f"- Figures: **{len(MANIFEST)}/{len(MANIFEST)}** `Mono: yes` + `Verified: yes`; "
      f"{len(labelrows)} carry in-figure labels and {len(MANIFEST) - len(labelrows)} carry none "
      f"({', '.join('Fig ' + f for f, _, _, n in MANIFEST if n == 0)}) \u2014 each confirmed by opening the asset\n")
    W(f"Type vocabulary (normalized, one spelling and casing per value, {len(types)} values): {census} = **{len(ROWS)}**\n")
    W("Tick legend: `x` = written into the script and verified present in the generated PDF. "
      "**0 rows ticked \u2014 Gate 1 closed, Pass 2 not started.**\n")
    W("Session log (Pass 1, five mandatory sessions, each reporting its own machine-derived row count):\n")
    W(f"- **1-S** source read + two independent prose sweeps \u2014 done. Contributed the "
      f"{len(ROWS) - len(headings) - len(openers) - len(labelrows) - len(uniques)} content rows "
      f"(`fact`/`definition`/`number`/`example`/`qualifier`/`term`/`process`/`comparison`/`exception`/`caption`).")
    W(f"- **1-H** heading sweep \u2014 done. Contributed **{len(headings)}** `heading` rows "
      f"({len(numbered)} numbered + {len(structural)} structural + {len(unnumbered)} unnumbered).")
    W(f"- **1-O** opener sweep \u2014 done. Contributed **{len(openers)}** `opener` rows.")
    W(f"- **1-F** figures \u2014 re-run at this gate. **{len(MANIFEST)}** assets re-pinned and regenerated, all `mode=L` at 300 dpi, "
      f"all re-verified by opening; **{len(labelrows)}** `figure-labels` rows carrying **{n_labels}** labels harvested visually.")
    W(f"- **1-Z** gaps, summary and freeze \u2014 done. Contributed **{len(uniques)}** `summary-unique` fold rows; "
      f"exercise-gap scan and freeze; every count above derived by re-parse. \u2192 **Gate 1**\n")

    W("## Facts\n")
    W("| ID | Section | Type | Exact original wording | Ticked |")
    W("|----|---------|------|------------------------|--------|")
    for i, (s, t, w) in zip(ids, ROWS):
        W(f"| {i} | {s} | {t} | {w} |  |")
    W("")

    W("## Summary classification\n")
    W("Every sentence of the NCERT `SUMMARY`, classified BODY-PRESENT (the fact is explicitly in a body row, so it "
      "belongs only in the rewritten Quick Recap) or SUMMARY-UNIQUE (stated only in the summary, so it must be folded "
      "into a body section *before* the Quick Recap). The test applied is the strict one: implied does not count, only "
      "explicit statement counts.\n")
    W("| # | Summary sentence | Classification | Folded into |")
    W("|---|---|---|---|")
    for sid, sentence, cls, home in SUMMARY_TABLE:
        W(f"| {sid} | \u201c{sentence}\u201d | {cls} | {home.format(**fold_map)} |")
    W("")
    W(f"Totals: **{len(SUMMARY_TABLE)} sentences = {len(body_present)} BODY-PRESENT + {len(uniques)} SUMMARY-UNIQUE.** "
      f"All {len(uniques)} SUMMARY-UNIQUE facts have a Facts row (`{uniques[0]}`\u2013`{uniques[-1]}`) and a named body home.\n")

    W("## Exercise-gap terms (Rule 2)\n")
    W(f"Classification of all {len(EXERCISES)} end-of-chapter exercises (10 numbered questions carrying 11 lettered "
      "sub-parts: 7 in Q3, 2 in Q4, 2 in Q5). Only GAP questions are reproduced and answered in the PDF, in the closing "
      "appendix \u201cTerms used in the exercises\u201d; COVERED questions are answered by the body text and are **not** reproduced.\n")
    W("| # | Exercise | Class | Answered where |")
    W("|---|---|---|---|")
    for qid, q, cls, home in EXERCISES:
        W(f"| {qid} | {q} | {cls} | {home} |")
    W("")
    W(f"Arithmetic, stated in words: **{len(EXERCISES)} exercises, {len(gaps)} answered by design (GAP), "
      f"{len(covered)} unanswered by design (COVERED), 0 overlooked.** Because the gap count is zero, the PDF gets "
      "**no exercise appendix and no exercise section** (Rule 2). The one place the chapter comes close to a gap is "
      "Q7, adjudicated under source note SRC-1 below: the shortfall is the source\u2019s own, and closing it would require "
      "outside content, which Rule 5 forbids.\n")

    W("## Figure manifest\n")
    W(f"All {len(MANIFEST)} numbered NCERT figures. Census taken from the **page images** of every artwork page, not from "
      "caption numbers alone: the caption census (Fig 5.1\u2013Fig 5.17) and the page-image census agree at "
      f"{len(MANIFEST)}, and no additional unnumbered plate exists. Source page numbers are PDF page indices, not "
      "printed textbook page numbers; rects are PDF points in the source mediabox `(0, 0, 576, 784.8)`.\n")
    W("Standard: each asset holds the complete artwork, every in-figure label, every leader line and every panel marker, "
      "and **excludes the printed caption** \u2014 captions are typeset by the Pass-2 script from the `caption` rows above, so "
      "a caption baked into the plate would print twice. Assets are rendered at 300 dpi, converted to true "
      "single-channel greyscale with Pillow `convert(\"L\")` and then `autocontrast(cutoff=1)`.\n")
    W("| Fig # | Caption (verbatim) | Asset file | Source page | Crop rect (x0,y0,x1,y1) | In-figure labels | Mono | Verified |")
    W("|---|---|---|---:|---|---:|---|---|")
    rects = crop_rects()
    for fig, cap, page, nlab in MANIFEST:
        asset = f"`assets/fig_{fig.replace('.', '_')}.png`"
        W(f"| {fig} | {cap} | {asset} | {page} | `{tuple(rects[fig])}` | {nlab} | yes | yes |")
    W("")
    W(f"**The {len(MANIFEST) - len(labelrows)} label-free plates carry no `figure-labels` row on purpose.** "
      "`check_pdf.py`'s `_extract_labels` matches any row whose wording begins \u201cFigure labels\u201d and, finding no quoted "
      "strings, falls back to splitting the remainder on `;` \u2014 so a row reading \u201cFigure labels: none\u201d would be parsed as "
      "a phantom label. Their emptiness is recorded here instead, and each was confirmed by opening the asset: Fig 5.7 "
      "is a plain photograph, Fig 5.8 a bare branching diagram, and Figs 5.9, 5.11, 5.12 and 5.17 are multi-panel "
      "plates whose only text is the panel markers, which the caption maps.\n")
    W("**Panel markers are not counted as labels.** `(a)`\u2026`(f)` carry no biological content of their own \u2014 the caption "
      "supplies their meaning, and it is captured verbatim in the `caption` row. Counting them would put tokens like "
      "\u201c(a)\u201d into check 6, which requires every listed label to appear in running text.\n")

    art = [r[0] for r in REPIN_LOG if "ART" in r[1]]
    cap = [r[0] for r in REPIN_LOG if "CAP" in r[1]]
    introduced = [r[0] for r in REPIN_LOG if "+NEW" in r[1]]
    defective = sorted(set(art) | set(cap), key=float)
    cleanset = [f for f, _, _, _ in MANIFEST if f not in defective]

    W("### Session 1-F re-verification and re-pin log\n")
    W("Every inherited asset was opened and read (section 4.4 Step 3), not spot-checked, and each verdict below is "
      "machine-adjudicated by `scratch/ch5morph_gate1/adjudicate_inherited.py`, which measures every inherited "
      "rectangle against its plate's ink-and-image extent.\n")
    W(f"- **{len(art)} of {len(MANIFEST)} inherited rectangles clipped artwork, an in-figure label or a panel marker** "
      f"(Figs {', '.join(art)}).")
    W(f"- **{len(cap)} of {len(MANIFEST)} cut the printed caption through its glyph row** (Figs {', '.join(cap)}).")
    W(f"- **{len(defective)} of {len(MANIFEST)} therefore carried at least one defect**; "
      f"{len(cleanset)} were clean (Figs {', '.join(cleanset)}).")
    W(f"- **{len(introduced)} further defects were introduced by this session's own first re-pin** and caught before "
      f"the freeze (Figs {', '.join(introduced)}) \u2014 logged here rather than quietly corrected, because two of the "
      "three came from trusting the watermark-polluted drawings union.")
    W("")
    W("All 17 were re-pinned and regenerated, then re-opened and read again. The adjudicator confirms the current "
      "rectangles clip **nothing**. The inherited three-part audit had passed the whole set as clean \u2014 see the blind "
      "spot recorded under the audit record.\n")
    W("| Fig # | Class | Finding | Change |")
    W("|---|---|---|---|")
    for fig, cls, finding, change in REPIN_LOG:
        W(f"| {fig} | {cls} | {finding} | {change} |")
    W("")

    W("### Three-part crop audit + print-asset check\n")
    W("Run by `audit_figures.py`; full output in `Ch5_figure_audit.txt`.\n")
    W("| Audit | Result |")
    W("|---|---|")
    W("| A \u2014 text-layer word grazing | **0 grazing words across all 17 assets.** Rotated spans are excluded: page 11 "
      "carries a rotated, non-rendering duplicate `(a)` belonging to the watermark layer, which the first run reported "
      "against Fig 5.12 as a true negative (the visible `(a)`\u2013`(e)` markers are all fully inside the crop). |")
    W("| B \u2014 drawings-extent overflow | 4 reports (Figs 5.3, 5.8, 5.14, 5.15). **All are watermark artefacts** and are "
      "adjudicated by B2. NCERT\u2019s diagonal \u201cnot to be republished\u201d and (c) marks are vector artwork drawn across the "
      "whole page, so their strokes get attributed to whichever plate sits behind them. This is what mis-pinned the "
      "inherited Fig 5.14 rect, and it is why B is no longer treated as authoritative. |")
    W("| B2 \u2014 ink-extent overflow | **Clean for all 17.** Measures dark ink (< 215) just outside each rect, discounting "
      "the caption\u2019s own words. The watermark renders around grey 230\u2013245, so this separates real clipped artwork from "
      "watermark strokes and proves B\u2019s four reports are not clipping. |")
    W("| C \u2014 border-band ink | **Clean for all 17** (dark ink < 110, unexplained by any text-layer word). |")
    W("| D \u2014 print-asset check | **17/17** `mode=L`, single channel, 300 dpi. |")
    W("")
    W("> **Blind spot, recorded so it is not rediscovered.** Audits A and C both *discount text-layer words* \u2014 A only "
      "reports a word it can see is partly outside, and C deletes any dark pixel that a word explains. Neither can see "
      "a label that has been cropped away entirely, which is exactly the Fig 5.2 `Laterals` defect: the label sat "
      "outside the rect, so no word grazed the boundary and no unexplained ink remained. The inherited audit was "
      "green and the inherited tracker even recorded that label as \u201cintentionally retained\u201d. Only opening every "
      "rendered asset and reading it catches this class, which is why section 4.4 Step 3 makes the visual pass "
      "mandatory and why session 1-F owns its own context budget.\n")
    W("No figure failed extraction, none is deliberately omitted, and none is a photograph of a person \u2014 so the PDF "
      "needs no \u201cFigures requiring manual attention\u201d block. The one human-subject image in the source, the Katherine "
      "Esau portrait on page 2, is **never embedded** (section 4.4 hard no); its caption is preserved as a text-only "
      f"row (`{captions[0]}`) and the profile facts as `F014`\u2013`F022`.\n")

    W("## Source notes (findings about the source, not defects in this inventory)\n")
    W("- **SRC-1 \u2014 \u00a75.5.1.4 names six placentation types but describes five.** The sentence \u201cThe placentation are of "
      "different types namely, marginal, axile, parietal, basal, central and free central\u201d lists **central** *and* "
      "**free central**, but the chapter then defines only marginal, axile, parietal, free central and basal, and "
      "Figure 5.12 figures exactly those five. \u201cCentral placentation\u201d is therefore named and never explained. This "
      "makes exercise Q7 (\u201cDescribe the various types of placentations\u201d) impossible to answer exhaustively from the "
      "chapter. It is logged here rather than opened as a Rule 2 GAP because closing it would require a definition "
      "from outside this chapter, which Rule 5 forbids. Pass 2 must reproduce the six-name list verbatim and must not "
      "silently \u201ccorrect\u201d it to five.")
    W("- **SRC-2 \u2014 \u00a75.9 has two different titles.** The chapter contents box on source page 3 calls it \u201c5.9 Description "
      "of Some Important Families\u201d; the in-body heading on page 14 reads \u201c5.9 SOLANACEAE\u201d, and only one family is "
      "actually described. Both strings are preserved (in the `F032` contents row and the `F252` heading row).")
    W("- **SRC-3 \u2014 \u00a75.9 prints \u201cbicarpellary obligately placed\u201d.** Read off the page image at 230 dpi to be sure. The "
      "standard morphological term is *obliquely*. Rule 4 bans qualifier and term drift, so the NCERT string is "
      "preserved exactly; Pass 3 should not \u201cfix\u201d it. Same treatment for the other preserved source spellings: "
      "\u201cphysiologial\u201d, \u201cadaptions\u201d, \u201cencyclopediac\u201d, \u201cleafbase\u201d, \u201cmonoadelphous\u201d, \u201cplacentaion\u201d, \u201cexogeneously\u201d.")
    W("- **SRC-4 \u2014 the floral-formula symbols are invisible to text extraction.** `get_text()` returns the \u00a75.8 symbol "
      "key with the male, female, bisexual and zygomorphic glyphs simply missing, and the two `G` variants "
      "indistinguishable. The key in `F192` and the Solanaceae formula in `F251` were read from the page images at "
      "250\u2013280 dpi. The printed distinction is **G underlined = superior ovary**, **G overlined = inferior ovary**.\n")

    W("## Carry-over list (for Pass 2 / Pass 3)\n")
    W("1. **Typeset every caption from the `caption` rows.** No asset now contains a baked-in caption, so nothing will "
      "double-print; the corollary is that a figure with no typeset caption will have none at all.")
    W("2. **Fig 5.16\u2019s only label is the printed floral formula** `K2+2 C4 A2+4 G(2)`. Check 6 needs it in running "
      "text, so write it verbatim rather than describing it. The same applies to the Solanaceae formula in `F251`.")
    W("3. **The four \u00a75.5.1.x headings are typographically invisible to a colour-based heading sweep.** Every other "
      "heading in this chapter is cyan (`0x00AEEF`, colour int 44783); `5.5.1.1 Calyx` through `5.5.1.4 Gynoecium` are "
      "10.5 pt `Bookman-LightItalic` in colour int 7171953, each drawn five times to fake a bold weight. A sweep keyed "
      "on the heading colour silently drops all four \u2014 a whole level of the flower section. Do not re-derive the "
      "heading set from styling alone.")
    W("4. **\u00a75.9\u2019s 11 bold field labels are deliberately *not* heading rows** (`Stem:`, `Leaves:`, `Inflorescence :`, "
      "`Flower`, `Calyx:`, `Corolla:`, `Androecium:`, `Gynoecium:`, `Fruits:`, `Seeds:`, `Floral Formula:`). The source "
      "styles them identically to the three real sub-headings (`Vegetative Characters`, `Floral Characters`, "
      "`Economic Importance`) \u2014 all are 10.5 pt `Bookman-Demi` \u2014 so typography cannot separate them. The editorial "
      "rule applied: a run-in label that heads a distinct sub-topic with its own definition and prose treatment is a "
      "heading (`Aestivation:`, `Placentation:` \u2014 both separately examined in Q3), whereas the field names of a single "
      "structured description record are not. Nothing is lost either way: each field\u2019s full line is preserved verbatim "
      "as its own Facts row. If a later pass disagrees, that is a metadata correction to the heading census, not a "
      "reason to rewrite rows.")
    W("5. **\u00a75.2\u2019s opener is a question, not a definition.** `F046` is the genuine first sentence, \u201cWhat are the "
      "features that distinguish a stem from a root?\u201d, and the chapter body never fully answers it \u2014 the distinguishing "
      "features it asks for arrive only in the summary (fold `F276`: multicellular hair, positively phototropic "
      "nature). Place that fold in \u00a75.2 so the question is answered where it is asked.")
    W("6. **\u00a75.9\u2019s opener leans on its own heading.** `F253` begins \u201cIt is a large family\u2026\u201d, where \u201cIt\u201d is Solanaceae, "
      "named only in the heading. If Pass 2 rewrites the heading, the opener\u2019s antecedent disappears.")
    W("7. **`audit_figures.py` check B is not authoritative** on watermarked pages; read B2. Both are kept so the "
      "disagreement stays visible rather than being silently resolved.")
    W("8. **`numpy` is an extra dependency** of this chapter\u2019s `audit_figures.py`, beyond the four packages in the "
      f"section-1 venv recipe: `uv pip install --python /vercel/share/neetenv/bin/python numpy`.\n")

    W("## References\n")
    W(f"[1]: `../../../{SRC}` \u2014 NCERT Class 11 Biology, Chapter 5 source PDF (16 pages).")
    W("[2]: `../../../GATE_1_PASS_1_SOURCE_MASTERY.md` \u2014 Gate 1 criteria and the five-session Pass 1 split.")
    W("[3]: `../../../skills/ncert-figure-extraction/SKILL.md` \u2014 440 dpi / 5-point grid pinning, three-part crop audit, "
      "visual confirmation.")
    W("[4]: `extract_figures.py`, `audit_figures.py`, `Ch5_figure_audit.txt`, `Ch5_TRACKER.md` \u2014 reproducible "
      "extraction, audit, audit output, chapter tracker.")
    W("[5]: `scratch/ch5morph_gate1/` \u2014 Pass 1 build evidence: `build_inventory.py` (emits this file), "
      "`gate1_close.py` (the Gate 1 machine check), `adjudicate_inherited.py` (re-derives the inherited-crop "
      "defect count), `ink_bbox.py` (watermark-robust extent measurement), `probe_geometry.py`, "
      "`source_text.txt`, `GATE1_EXPLAINER.md`, and the page crops behind source notes SRC-3 and SRC-4. "
      "Whole-page renders are not kept here \u2014 `scratch/ch5_figs/pages_150/` already holds them, and the "
      "mandatory 440 dpi / 5-point grids are in `scratch/ch5_figs/grid_4x/`.")

    with open(OUT, "w") as fh:
        fh.write("\n".join(out) + "\n")

    print(f"rows={len(ROWS)}  ids={ids[0]}..{ids[-1]}")
    print(f"headings={len(headings)} ({len(numbered)}+{len(structural)}+{len(unnumbered)})  openers={len(openers)}")
    print(f"captions={len(captions)}  figure-labels rows={len(labelrows)}  labels={n_labels}  summary-unique={len(uniques)}")
    print(f"types={len(types)}  census sums to {sum(types.values())}")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
