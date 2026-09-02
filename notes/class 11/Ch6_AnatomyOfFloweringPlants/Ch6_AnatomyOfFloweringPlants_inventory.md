# Frozen Inventory — Anatomy of Flowering Plants (Class 11, Chapter 6)

Source: `Chapter/class 11/Chapter 06 - Anatomy of Flowering Plants.pdf` | Frozen: 2026-09-02 | Rows: 132

**Counts (machine-derived from the Facts table — re-parse, never hand-tally):**
- Total Facts rows: **132** (IDs `F001..F132`, contiguous, no gaps/duplicates)
- Heading rows (`Type: heading`): **14** = 11 numbered section headings + chapter title + `SUMMARY` + `EXERCISES`; **0 unnumbered sub-headings** exist in this chapter
- Opener rows (`Type: opener`): **11** (one per numbered section: 6.1, 6.1.1, 6.1.2, 6.1.3, 6.2, 6.2.1, 6.2.2, 6.2.3, 6.2.4, 6.2.5, 6.2.6)
- Figure-label rows (`Type: figure-labels`): **5** figures / **44** labels (6.1=5, 6.2=3, 6.3=9, 6.4=16, 6.5=11)
- Caption rows (`Type: caption`): **5**
- Summary sentences classified: **13** (7 BODY-PRESENT, 6 SUMMARY-UNIQUE)
- Exercises: **7 total, 1 answered by design (GAP: Q6), 6 unanswered by design (COVERED), 0 overlooked**

Tick legend: `x` = written into the script and verified present in the generated PDF. **All 132/132 rows ticked at Pass 2 (2026-09-02).**

Session log (Pass 1, five mandatory sessions):
- **1-S** source read + facts — done (F002–F006 intro; per-section fact rows)
- **1-H** heading sweep — done (14 `heading` rows; 11 numbered + 3 structural, 0 unnumbered)
- **1-O** opener sweep — done (11 `opener` rows)
- **1-F** figures — done previously (manifest + 44-label matrix, all `Mono: yes`/`Verified: yes`)
- **1-Z** gaps, summary, freeze — done (summary classification + exercise-gap; counts machine-derived) → **Gate 1**

Pass 2 / Gate 2 (2026-09-02):
- Script `Ch6_AnatomyOfFloweringPlants.py` written linearly from this freeze in Content Order (§5), importing the repo-level `neet_template.py`; no style/geometry/colour/font re-declared. All 6 SUMMARY-UNIQUE facts (`F125`–`F130`) folded into their body homes and restated in the Quick Recap.
- PDF built: **6 A4 portrait pages, 4.6 MB, 5 embedded monochrome images** (Fig 6.1–6.5).
- `check_pdf.py` → **exit 0, VERDICT WARN (0 fail / 1 benign warn)**: check 6 = **44/44 labels in running text**; check 7 = **132/132 Facts rows ticked**; checks 1–3, 5, 8–10 all PASS. The single WARN is **check 4** keyword-firing on "photo" inside *photosynthesis*/*photosynthates* rows (`F106`, `F126`, `S3`) — true-negative (check 3 confirms all 5 assets are monochrome T.S. diagrams; no person photograph exists in Ch6).
- Ticking: chapter-local `tick_rows.py` (token screen, Pass-2 evidence only, never a Gate-3 clear) auto-ticked 121 rows; the remaining 11 (`F008`/`F057` paraphrased openers, `F071`/`F098`/`F115` figure captions, `F124` recap heading, `F125`/`F127`/`F128`/`F129`/`F130` summary-unique folds) were flagged as scorer artefacts (annotation words in the wording column), hand-verified present in the extracted PDF text, and ticked. → **Gate 2 CLOSED** (Gate 3 full-read defect hunt still open).

Type vocabulary (normalized, single casing): `heading`, `opener`, `definition`, `term`, `number`, `qualifier`, `comparison`, `exception`, `example`, `fact`, `caption`, `figure-labels`, `exercise-gap`, `summary-unique`.

## Facts

| ID | Section | Type | Exact original wording | Ticked |
|----|---------|------|------------------------|--------|
| F001 | Ch6 | heading | Chapter 6 title: "ANATOMY OF FLOWERING PLANTS" | x |
| F002 | intro | definition | "Study of internal structure of plants is called anatomy." | x |
| F003 | intro | term | "Plants have cells as the basic unit, cells are organised into tissues and in turn the tissues are organised into organs." | x |
| F004 | intro | comparison | "Different organs in a plant show differences in their internal structure." | x |
| F005 | intro | comparison | "Within angiosperms, the monocots and dicots are also seen to be anatomically different." | x |
| F006 | intro | fact | "Internal structures also show adaptations to diverse environments." | x |
| F007 | 6.1 | heading | "6.1 The Tissue System" | x |
| F008 | 6.1 | opener | "We were discussing types of tissues based on the types of cells present. Let us now consider how tissues vary depending on their location in the plant body." | x |
| F009 | 6.1 | fact | "Their structure and function would also be dependent on location." | x |
| F010 | 6.1 | number | "On the basis of their structure and location, there are three types of tissue systems." (count: three) | x |
| F011 | 6.1 | term | "These are the epidermal tissue system, the ground or fundamental tissue system and the vascular or conducting tissue system." | x |
| F012 | 6.1.1 | heading | "6.1.1 Epidermal Tissue System" | x |
| F013 | 6.1.1 | opener | "The epidermal tissue system forms the outer-most covering of the whole plant body and comprises epidermal cells, stomata and the epidermal appendages – the trichomes and hairs." | x |
| F014 | 6.1.1 | fact | "The epidermis is the outermost layer of the primary plant body." | x |
| F015 | 6.1.1 | fact | "It is made up of elongated, compactly arranged cells, which form a continuous layer." | x |
| F016 | 6.1.1 | qualifier | "Epidermis is usually single-layered." (qualifier: usually) | x |
| F017 | 6.1.1 | fact | "Epidermal cells are parenchymatous with a small amount of cytoplasm lining the cell wall and a large vacuole." | x |
| F018 | 6.1.1 | term | "The outside of the epidermis is often covered with a waxy thick layer called the cuticle which prevents the loss of water." | x |
| F019 | 6.1.1 | exception | "Cuticle is absent in roots." | x |
| F020 | 6.1.1 | fact | "The cells of epidermis bear a number of hairs." | x |
| F021 | 6.1.1 | term | "The root hairs are unicellular elongations of the epidermal cells and help absorb water and minerals from the soil." | x |
| F022 | 6.1.1 | term | "On the stem the epidermal hairs are called trichomes." | x |
| F023 | 6.1.1 | qualifier | "The trichomes in the shoot system are usually multicellular." (qualifier: usually) | x |
| F024 | 6.1.1 | qualifier | "They may be branched or unbranched and soft or stiff." (qualifier: may) | x |
| F025 | 6.1.1 | fact | "They may even be secretory." | x |
| F026 | 6.1.1 | fact | "The trichomes help in preventing water loss due to transpiration." | x |
| F027 | 6.1.1 | term | "Stomata are structures present in the epidermis of leaves." | x |
| F028 | 6.1.1 | fact | "Stomata regulate the process of transpiration and gaseous exchange." | x |
| F029 | 6.1.1 | number | "Each stoma is composed of two bean-shaped cells known as guard cells which enclose stomatal pore." (count: two) | x |
| F030 | 6.1.1 | exception | "In grasses, the guard cells are dumb-bell shaped." | x |
| F031 | 6.1.1 | fact | "The outer walls of guard cells (away from the stomatal pore) are thin and the inner walls (towards the stomatal pore) are highly thickened." | x |
| F032 | 6.1.1 | fact | "The guard cells possess chloroplasts and regulate the opening and closing of stomata." | x |
| F033 | 6.1.1 | qualifier | "Sometimes, a few epidermal cells, in the vicinity of the guard cells become specialised in their shape and size and are known as subsidiary cells." (qualifier: sometimes) | x |
| F034 | 6.1.1 | term | "The stomatal aperture, guard cells and the surrounding subsidiary cells are together called stomatal apparatus." | x |
| F035 | Fig 6.1 | caption | Fig. 6.1 caption: "Diagrammatic representation: (a) stomata with bean-shaped guard cells (b) stomata with dumb-bell shaped guard cell" | x |
| F036 | Fig 6.1 | figure-labels | Figure labels: "Epidermal cells"; "Subsidiary cells"; "Chloroplast"; "Guard cells"; "Stomatal pore" | x |
| F037 | 6.1.2 | heading | "6.1.2 The Ground Tissue System" | x |
| F038 | 6.1.2 | opener | "All tissues except epidermis and vascular bundles constitute the ground tissue." | x |
| F039 | 6.1.2 | term | "It consists of simple tissues such as parenchyma, collenchyma and sclerenchyma." | x |
| F040 | 6.1.2 | qualifier | "Parenchymatous cells are usually present in cortex, pericycle, pith and medullary rays, in the primary stems and roots." (qualifier: usually) | x |
| F041 | 6.1.2 | term | "In leaves, the ground tissue consists of thin-walled chloroplast containing cells and is called mesophyll." | x |
| F042 | 6.1.3 | heading | "6.1.3 The Vascular Tissue System" | x |
| F043 | 6.1.3 | opener | "The vascular system consists of complex tissues, the phloem and the xylem." | x |
| F044 | 6.1.3 | term | "The xylem and phloem together constitute vascular bundles." | x |
| F045 | 6.1.3 | fact | "In dicotyledonous stems, cambium is present between phloem and xylem." | x |
| F046 | 6.1.3 | term | "Such vascular bundles because of the presence of cambium possess the ability to form secondary xylem and phloem tissues, and hence are called open vascular bundles." | x |
| F047 | 6.1.3 | comparison | "In the monocotyledons, the vascular bundles have no cambium present in them. Hence, since they do not form secondary tissues they are referred to as closed." | x |
| F048 | 6.1.3 | term | "When xylem and phloem within a vascular bundle are arranged in an alternate manner along the different radii, the arrangement is called radial such as in roots." | x |
| F049 | 6.1.3 | term | "In conjoint type of vascular bundles, the xylem and phloem are jointly situated along the same radius of vascular bundles." | x |
| F050 | 6.1.3 | fact | "Such vascular bundles are common in stems and leaves." | x |
| F051 | 6.1.3 | qualifier | "The conjoint vascular bundles usually have the phloem located only on the outer side of xylem." (qualifiers: usually, only) | x |
| F052 | Fig 6.2 | caption | Fig. 6.2 caption: "Various types of vascular bundles: (a) radial (b) conjoint closed (c) conjoint open" | x |
| F053 | Fig 6.2 | figure-labels | Figure labels: "Xylem"; "Phloem"; "Cambium" | x |
| F054 | 6.2 | heading | "6.2 Anatomy of Dicotyledonous and Monocotyledonous Plants" | x |
| F055 | 6.2 | opener | "For a better understanding of tissue organisation of roots, stems and leaves, it is convenient to study the transverse sections of the mature zones of these organs." | x |
| F056 | 6.2.1 | heading | "6.2.1 Dicotyledonous Root" | x |
| F057 | 6.2.1 | opener | "Look at Figure 6.3 (a), it shows the transverse section of the sunflower root." (also carries example organism: sunflower) | x |
| F058 | 6.2.1 | term | "The outermost layer is epiblema." | x |
| F059 | 6.2.1 | fact | "Many of the cells of epiblema protrude in the form of unicellular root hairs." | x |
| F060 | 6.2.1 | fact | "The cortex consists of several layers of thin-walled parenchyma cells with intercellular spaces." | x |
| F061 | 6.2.1 | term | "The innermost layer of the cortex is called endodermis." | x |
| F062 | 6.2.1 | fact | "It comprises a single layer of barrel-shaped cells without any intercellular spaces." | x |
| F063 | 6.2.1 | term | "The tangential as well as radial walls of the endodermal cells have a deposition of water-impermeable, waxy material suberin in the form of casparian strips." | x |
| F064 | 6.2.1 | term | "Next to endodermis lies a few layers of thick-walled parenchyomatous cells referred to as pericycle." | x |
| F065 | 6.2.1 | fact | "Initiation of lateral roots and vascular cambium during the secondary growth takes place in these cells." | x |
| F066 | 6.2.1 | fact | "The pith is small or inconspicuous." (dicot root) | x |
| F067 | 6.2.1 | term | "The parenchymatous cells which lie between the xylem and the phloem are called conjuctive tissue." | x |
| F068 | 6.2.1 | number | "There are usually two to four xylem and phloem patches." (count: 2–4; qualifier: usually) | x |
| F069 | 6.2.1 | fact | "Later, a cambium ring develops between the xylem and phloem." | x |
| F070 | 6.2.1 | term | "All tissues on the innerside of the endodermis such as pericycle, vascular bundles and pith constitute the stele." | x |
| F071 | Fig 6.3 | caption | Fig. 6.3 caption: "T.S.: (a) Dicot root (Primary) (b) Monocot root" | x |
| F072 | Fig 6.3 | figure-labels | Figure labels: "Root hair"; "Epidermis"; "Cortex"; "Endodermis"; "Pericycle"; "Protoxylem"; "Metaxylem"; "Pith"; "Phloem" | x |
| F073 | 6.2.2 | heading | "6.2.2 Monocotyledonous Root" | x |
| F074 | 6.2.2 | opener | "The anatomy of the monocot root is similar to the dicot root in many respects." | x |
| F075 | 6.2.2 | fact | "It has epidermis, cortex, endodermis, pericycle, vascular bundles and pith." | x |
| F076 | 6.2.2 | number | "As compared to the dicot root which have fewer xylem bundles, there are usually more than six (polyarch) xylem bundles in the monocot root." (count: more than six / polyarch; qualifier: usually; comparison) | x |
| F077 | 6.2.2 | fact | "Pith is large and well developed." (monocot root) | x |
| F078 | 6.2.2 | exception | "Monocotyledonous roots do not undergo any secondary growth." | x |
| F079 | 6.2.3 | heading | "6.2.3 Dicotyledonous Stem" | x |
| F080 | 6.2.3 | opener | "The transverse section of a typical young dicotyledonous stem shows that the epidermis is the outermost protective layer of the stem." | x |
| F081 | 6.2.3 | fact | "Covered with a thin layer of cuticle, it may bear trichomes and a few stomata." | x |
| F082 | 6.2.3 | fact | "The cells arranged in multiple layers between epidermis and pericycle constitute the cortex." | x |
| F083 | 6.2.3 | number | "It consists of three sub-zones." (count: three) | x |
| F084 | 6.2.3 | term | "The outer hypodermis, consists of a few layers of collenchymatous cells just below the epidermis, which provide mechanical strength to the young stem." | x |
| F085 | 6.2.3 | fact | "Cortical layers below hypodermis consist of rounded thin walled parenchymatous cells with conspicuous intercellular spaces." | x |
| F086 | 6.2.3 | term | "The innermost layer of the cortex is called the endodermis." | x |
| F087 | 6.2.3 | term | "The cells of the endodermis are rich in starch grains and the layer is also referred to as the starch sheath." | x |
| F088 | 6.2.3 | term | "Pericycle is present on the inner side of the endodermis and above the phloem in the form of semi-lunar patches of sclerenchyma." | x |
| F089 | 6.2.3 | term | "In between the vascular bundles there are a few layers of radially placed parenchymatous cells, which constitute medullary rays." | x |
| F090 | 6.2.3 | fact | "A large number of vascular bundles are arranged in a ring; the 'ring' arrangement of vascular bundles is a characteristic of dicot stem." | x |
| F091 | 6.2.3 | term | "Each vascular bundle is conjoint, open, and with endarch protoxylem." | x |
| F092 | 6.2.3 | fact | "A large number of rounded, parenchymatous cells with large intercellular spaces which occupy the central portion of the stem constitute the pith." | x |
| F093 | 6.2.4 | heading | "6.2.4 Monocotyledonous Stem" | x |
| F094 | 6.2.4 | opener | "The monocot stem has a sclerenchymatous hypodermis, a large number of scattered vascular bundles, each surrounded by a sclerenchymatous bundle sheath, and a large, conspicuous parenchymatous ground tissue." | x |
| F095 | 6.2.4 | term | "Vascular bundles are conjoint and closed." | x |
| F096 | 6.2.4 | qualifier | "Peripheral vascular bundles are generally smaller than the centrally located ones." (qualifier: generally) | x |
| F097 | 6.2.4 | fact | "The phloem parenchyma is absent, and water-containing cavities are present within the vascular bundles." | x |
| F098 | Fig 6.4 | caption | Fig. 6.4 caption: "T.S. of stem: (a) Dicot (b) Monocot" | x |
| F099 | Fig 6.4 | figure-labels | Figure labels: "Epidermal hair"; "Epidermis"; "Hypodermis"; "Parenchyma"; "Endodermis"; "Pericycle"; "Vascular bundle"; "Medullary rays"; "Pith"; "Collenchyma"; "Phloem"; "Cambium"; "Metaxylem"; "Protoxylem"; "Vascular bundles"; "Ground tissue" | x |
| F100 | 6.2.5 | heading | "6.2.5 Dorsiventral (Dicotyledonous) Leaf" | x |
| F101 | 6.2.5 | opener | "The vertical section of a dorsiventral leaf through the lamina shows three main parts, namely, epidermis, mesophyll and vascular system." (count: three) | x |
| F102 | 6.2.5 | term | "The epidermis which covers both the upper surface (adaxial epidermis) and lower surface (abaxial epidermis) of the leaf has a conspicuous cuticle." | x |
| F103 | 6.2.5 | comparison | "The abaxial epidermis generally bears more stomata than the adaxial epidermis." (qualifier: generally) | x |
| F104 | 6.2.5 | qualifier | "The latter may even lack stomata." (qualifier: may; the adaxial epidermis) | x |
| F105 | 6.2.5 | term | "The tissue between the upper and the lower epidermis is called the mesophyll." | x |
| F106 | 6.2.5 | fact | "Mesophyll, which possesses chloroplasts and carry out photosynthesis, is made up of parenchyma." | x |
| F107 | 6.2.5 | number | "It has two types of cells – the palisade parenchyma and the spongy parenchyma." (count: two) | x |
| F108 | 6.2.5 | fact | "The adaxially placed palisade parenchyma is made up of elongated cells, which are arranged vertically and parallel to each other." | x |
| F109 | 6.2.5 | fact | "The oval or round and loosely arranged spongy parenchyma is situated below the palisade cells and extends to the lower epidermis." | x |
| F110 | 6.2.5 | fact | "There are numerous large spaces and air cavities between these cells." | x |
| F111 | 6.2.5 | fact | "Vascular system includes vascular bundles, which can be seen in the veins and the midrib." | x |
| F112 | 6.2.5 | fact | "The size of the vascular bundles are dependent on the size of the veins." | x |
| F113 | 6.2.5 | fact | "The veins vary in thickness in the reticulate venation of the dicot leaves." | x |
| F114 | 6.2.5 | term | "The vascular bundles are surrounded by a layer of thick walled bundle sheath cells." | x |
| F115 | Fig 6.5 | caption | Fig. 6.5 caption: "T.S. of leaf: (a) Dicot (b) Monocot" | x |
| F116 | Fig 6.5 | figure-labels | Figure labels: "Bundle sheath"; "Xylem"; "Phloem"; "Adaxial epidermis"; "Palisade mesophyll"; "Air cavity"; "Spongy mesophyll"; "Sub-stomatal cavity"; "Stoma"; "Abaxial epidermis"; "Mesophyll" | x |
| F117 | 6.2.6 | heading | "6.2.6 Isobilateral (Monocotyledonous) Leaf" | x |
| F118 | 6.2.6 | opener | "The anatomy of isobilateral leaf is similar to that of the dorsiventral leaf in many ways." | x |
| F119 | 6.2.6 | comparison | "In an isobilateral leaf, the stomata are present on both the surfaces of the epidermis; and the mesophyll is not differentiated into palisade and spongy parenchyma." | x |
| F120 | 6.2.6 | term | "In grasses, certain adaxial epidermal cells along the veins modify themselves into large, empty, colourless cells. These are called bulliform cells." (example: grasses) | x |
| F121 | 6.2.6 | fact | "When the bulliform cells in the leaves have absorbed water and are turgid, the leaf surface is exposed." | x |
| F122 | 6.2.6 | fact | "When they are flaccid due to water stress, they make the leaves curl inwards to minimise water loss." | x |
| F123 | 6.2.6 | qualifier | "The parallel venation in monocot leaves is reflected in the near similar sizes of vascular bundles (except in main veins) as seen in vertical sections of the leaves." (qualifier: except) | x |
| F124 | SUMMARY | heading | "SUMMARY" | x |
| F125 | summary | summary-unique | "The plant tissues are broadly classified into meristematic (apical, lateral and intercalary) and permanent (simple and complex)." (SUMMARY-UNIQUE — fold into body intro/tissue-system opener) | x |
| F126 | summary | summary-unique | "Assimilation of food and its storage, transportation of water, minerals and photosynthates, and mechanical support are the main functions of tissues." (SUMMARY-UNIQUE — fold into §6.1) | x |
| F127 | summary | summary-unique | "The ground tissue system forms the main bulk of the plant." (SUMMARY-UNIQUE — fold into §6.1.2) | x |
| F128 | summary | summary-unique | "The ground tissue is divided into three zones – cortex, pericycle and pith." (SUMMARY-UNIQUE — fold into §6.1.2; count: three) | x |
| F129 | summary | summary-unique | "The vascular bundles form the conducting tissue and translocate water, minerals and food material." (SUMMARY-UNIQUE — fold into §6.1.3) | x |
| F130 | summary | summary-unique | "The secondary growth occurs in most of the dicotyledonous roots and stems." (SUMMARY-UNIQUE — fold into §6.2; qualifier: most) | x |
| F131 | EXERCISES | heading | "EXERCISES" | x |
| F132 | Q6 | exercise-gap | "How is the study of plant anatomy useful to us?" (GAP — answered from intro facts only: anatomy = study of internal structure & functional organisation; lets us distinguish monocots from dicots anatomically; reveals adaptations of internal structures to diverse environments) | x |

## Summary classification

Every sentence of the NCERT SUMMARY, classified BODY-PRESENT (already in a body row → goes only in Quick Recap) or SUMMARY-UNIQUE (stated only in the summary → folded into a body section before writing Quick Recap).

| # | Summary sentence | Classification | Folded into |
|---|---|---|---|
| S1 | "Anatomically, a plant is made of different kinds of tissues." | BODY-PRESENT | intro (F002–F003) |
| S2 | "The plant tissues are broadly classified into meristematic (apical, lateral and intercalary) and permanent (simple and complex)." | SUMMARY-UNIQUE | F125 → §6.1 opener context |
| S3 | "Assimilation of food and its storage, transportation of water, minerals and photosynthates, and mechanical support are the main functions of tissues." | SUMMARY-UNIQUE | F126 → §6.1 |
| S4 | "There are three types of tissue systems – epidermal, ground and vascular." | BODY-PRESENT | F010–F011 |
| S5 | "The epidermal tissue systems are made of epidermal cells, stomata and the epidermal appendages." | BODY-PRESENT | F013 |
| S6 | "The ground tissue system forms the main bulk of the plant." | SUMMARY-UNIQUE | F127 → §6.1.2 |
| S7 | "It is divided into three zones – cortex, pericycle and pith." | SUMMARY-UNIQUE | F128 → §6.1.2 |
| S8 | "The vascular tissue system is formed by the xylem and phloem." | BODY-PRESENT | F043–F044 |
| S9 | "On the basis of presence of cambium, location of xylem and phloem, the vascular bundles are of different types." | BODY-PRESENT | F045–F049 |
| S10 | "The vascular bundles form the conducting tissue and translocate water, minerals and food material." | SUMMARY-UNIQUE | F129 → §6.1.3 |
| S11 | "Monocotyledonous and dicotyledonous plants show marked variation in their internal structures." | BODY-PRESENT | F005, §6.2 |
| S12 | "They differ in type, number and location of vascular bundles." | BODY-PRESENT | F047, F076, F090, F095 |
| S13 | "The secondary growth occurs in most of the dicotyledonous roots and stems." | SUMMARY-UNIQUE | F130 → §6.2 |

Totals: 13 sentences = 7 BODY-PRESENT + 6 SUMMARY-UNIQUE. All 6 SUMMARY-UNIQUE facts have a Facts row (F125–F130) and a planned body home.

## Exercise-gap terms (Rule 2)

Classification of all 7 end-of-chapter exercises. Only GAP questions are reproduced+answered in the PDF (appendix "Terms used in the exercises"); COVERED questions are answered by the body and are NOT reproduced.

| # | Exercise (abbreviated) | Class | Answered where |
|---|---|---|---|
| 1 | Draw anatomical differences: monocot vs dicot root; monocot vs dicot stem | COVERED | §6.2.1–6.2.4 + Figs 6.3, 6.4 |
| 2 | TS of young stem — monocot or dicot? give reasons | COVERED | §6.2.3 (ring of conjoint open bundles) vs §6.2.4 (scattered conjoint closed bundles) |
| 3 | Identify: conjoint scattered bundles, sclerenchymatous bundle sheath, phloem parenchyma absent | COVERED | §6.2.4 (monocot stem) |
| 4 | What is stomatal apparatus? Structure of stomata + labelled diagram | COVERED | §6.1.1 (F029–F034) + Fig 6.1 |
| 5 | Name three tissue systems; tissues under each | COVERED | §6.1 (F010–F011), §6.1.1–6.1.3 |
| 6 | How is the study of plant anatomy useful to us? | **GAP** | Appendix — answered from intro facts (F002, F005, F006) only |
| 7 | Internal structure of dorsiventral leaf + labelled diagrams | COVERED | §6.2.5 (F101–F114) + Fig 6.5 |

Arithmetic: **7 exercises, 1 answered by design (GAP: Q6), 6 unanswered by design (COVERED), 0 overlooked.**

## Figure manifest

Extraction standard: hand-pinned rectangles from mandatory 440 dpi grids (5 PDF-point spacing); final assets rendered at 300 dpi, converted to true grayscale with Pillow `convert("L")` + `autocontrast(cutoff=1)`. Page-image inspection of artwork pages 2–7 identified five numbered NCERT figure plates and no additional unnumbered plate (page 7 carries only prose + summary + exercises).

| Fig # | Caption (verbatim) | Asset file | Source page | Crop rect (x0,y0,x1,y1) | Mono | Verified |
|---|---|---|---:|---|---|---|
| 6.1 | Diagrammatic representation: (a) stomata with bean-shaped guard cells (b) stomata with dumb-bell shaped guard cell | `assets/fig_6_1.png` | 2 | (60, 337, 530, 448) | yes | yes |
| 6.2 | Various types of vascular bundles: (a) radial (b) conjoint closed (c) conjoint open | `assets/fig_6_2.png` | 3 | (320, 80, 520, 482) | yes | yes |
| 6.3 | T.S.: (a) Dicot root (Primary) (b) Monocot root | `assets/fig_6_3.png` (a/b composite; also `fig_6_3a.png`, `fig_6_3b.png`) | 4 | (75, 78, 320, 558) | yes | yes |
| 6.4 | T.S. of stem: (a) Dicot (b) Monocot | `assets/fig_6_4.png` | 5 | (55, 235, 550, 700) | yes | yes |
| 6.5 | T.S. of leaf: (a) Dicot (b) Monocot | `assets/fig_6_5.png` (a/b composite; also `fig_6_5a.png`, `fig_6_5b.png`) | 6 | (55, 285, 320, 690) | yes | yes |

Audit (from `Ch6_figure_audit.txt`): text-layer grazing = no grazing words for all five; drawings-extent = ok for 6.1/6.2/6.3/6.5 and correctly "raster figure" for 6.4; border-band ink = clean for all five. All emitted PNGs exist, `mode=L`, single channel. Figure 6.2 has zero text-layer words inside the plate, confirming its labels are vector/raster artwork verified visually. Multi-part plates (6.3, 6.5) recombined horizontally from standalone (a)/(b) assets. No figure failed extraction; none deliberately omitted; none is a photograph of a person.

## References

[1] `Chapter/class 11/Chapter 06 - Anatomy of Flowering Plants.pdf` — NCERT Biology source chapter.
[2] `SUPREME COMMAND PROMPT.md` — replacement-chapter, inventory, and figure requirements (v6).
[3] `skills/ncert-figure-extraction/SKILL.md` — hand-pinned crop, three-part audit, visual-verification procedure.
