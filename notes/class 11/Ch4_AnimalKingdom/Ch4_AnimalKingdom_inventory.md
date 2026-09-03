# Frozen Inventory — Class 11 Chapter 4: Animal Kingdom
Source: `Chapter/class 11/Chapter 04 - Animal Kingdom.pdf` (18 source pages) | Frozen: NOT YET FROZEN (Pass 1a in progress) | Rows: 154

Tick legend: `x` = written into the script and verified present in the generated PDF. All rows are unticked — Pass 2 has not started.

## Status of this file

This inventory was **started from zero on 2026-09-03**. The previous file at this path was not a Gate 1 inventory at all — it was a figure-extraction write-up with no Facts table, no heading/opener rows, no summary classification and no exercise-gap table. It has been moved to `Ch4_prior_figure_notes_UNTRUSTED.md` and **nothing in it is treated as a finding**. Per operator instruction, only the **extracted figure assets** in `assets/` are trusted; every claim about them (page numbers, label sets, mono/verified status) is re-derived in session 1-F.

Chapter 4 is run as a **big chapter** (§8): Pass 1a inventories the first half, Pass 1b the second half, into this same file. Gate 1 is evaluated over the whole chapter only after 1b.

### Half seam (fixed here so nothing is double-covered or dropped)

| Half | Scope | Source pages |
|---|---|---|
| **1a** | Chapter intro, §4.1 and all of §4.1.1–§4.1.6, §4.2 opener, and §4.2.1–§4.2.10 (Porifera through Hemichordata — the non-chordates), incl. the Figure 4.4 footnote | 1–9 |
| **1b** | §4.2.11 Chordata and all of §4.2.11.1–§4.2.11.7, TABLE 4.1, TABLE 4.2 (**all 11 phylum rows, including the non-chordate rows**), SUMMARY, EXERCISES | 10–18 |

Seam rule: TABLE 4.2 is assigned to **1b by physical location** even though its first ten rows describe 1a phyla. 1a must not pre-empt it.

### Session log (each session states its own machine-derived row count)

| Session | Scope | Status | Rows added |
|---|---|---|---|
| 1a-S | Steps 1–3, prose facts, first half | **DONE** | 154 (F001–F154) |
| 1a-H | Step 4, heading sweep, first half | not started | — |
| 1a-O | Step 5, opener sweep, first half | not started | — |
| 1b-S / 1b-H / 1b-O | second half | not started | — |
| 1-F | Step 6, figures, whole chapter | not started | — |
| 1-Z | Steps 7–10, gaps + summary + freeze | not started | — |

### 1a-S census — re-parsed from the Facts table itself (step 10), never hand-tallied

Re-parsing the finished table with `check_pdf.py`'s own row logic gives **154 Facts rows, IDs `F001`–`F154`, contiguous with no gaps and no duplicates**, all unticked. The total is derivable from this per-section list, which sums to 154:

`4.0`=2, `4.1`=2, `4.1.1`=11, `4.1.2`=4, `4.1.3`=3, `4.1.4`=5, `4.1.5`=2, `4.1.6`=2, `4.2`=3, `4.2.1`=13, `4.2.2`=12, `4.2.3`=9, `4.2.4`=10, `4.2.5`=10, `4.2.6`=12, `4.2.7`=19, `4.2.8`=11, `4.2.9`=12, `4.2.10`=12 — 19 sections, 154 rows.

`Type` histogram (machine-grouped, all lowercase, no casing split): feature 86, definition 24, example 17, term 10, number 4, etymology 4, comparison 4, process 3, list 1, exception 1 = 154.

`check_pdf.py._extract_labels` run against this file returns **0 label rows, 0 figures, no phantom `Fig #` row** — correct for a file whose 1-F session has not run. It must return a non-zero, non-doubled count after 1-F.

### `Type` controlled vocabulary (normalised lowercase, asserted at 1-Z)

`definition`, `feature`, `number`, `example`, `process`, `comparison`, `exception`, `etymology`, `list`, `term`, `heading`, `opener`, `caption`

## Facts
| ID | Section | Type | Exact original wording | Ticked |
|----|---------|------|------------------------|--------|
| F001 | 4.0 | number | "As over a million species of animals have been described till now, the need for classification becomes all the more important." | |
| F002 | 4.0 | feature | "The classification also helps in assigning a systematic position to newly described species." | |
| F003 | 4.1 | list | "there are fundamental features common to various individuals in relation to the arrangement of cells, body symmetry, nature of coelom, patterns of digestive, circulatory or reproductive systems" | |
| F004 | 4.1 | feature | "These features are used as the basis of animal classification and some of them are discussed here." | |
| F005 | 4.1.1 | feature | "Though all members of Animalia are multicellular, all of them do not exhibit the same pattern of organisation of cells." | |
| F006 | 4.1.1 | definition | "in sponges, the cells are arranged as loose cell aggregates, i.e., they exhibit cellular level of organisation" | |
| F007 | 4.1.1 | feature | "Some division of labour (activities) occur among the cells." | |
| F008 | 4.1.1 | definition | "In coelenterates, the arrangement of cells is more complex. Here the cells performing the same function are arranged into tissues, hence is called tissue level of organisation." | |
| F009 | 4.1.1 | definition | "A still higher level of organisation, i.e., organ level is exhibited by members of Platyhelminthes and other higher phyla where tissues are grouped together to form organs, each specialised for a particular function." | |
| F010 | 4.1.1 | definition | "In animals like Annelids, Arthropods, Molluscs, Echinoderms and Chordates, organs have associated to form functional systems, each system concerned with a specific physiological function. This pattern is called organ system level of organisation." | |
| F011 | 4.1.1 | feature | "Organ systems in different groups of animals exhibit various patterns of complexities." | |
| F012 | 4.1.1 | definition | "the digestive system in Platyhelminthes has only a single opening to the outside of the body that serves as both mouth and anus, and is hence called incomplete" | |
| F013 | 4.1.1 | definition | "A complete digestive system has two openings, mouth and anus." | |
| F014 | 4.1.1 | definition | "(i) open type in which the blood is pumped out of the heart and the cells and tissues are directly bathed in it" | |
| F015 | 4.1.1 | definition | "(ii) closed type in which the blood is circulated through a series of vessels of varying diameters (arteries, veins and capillaries)" | |
| F016 | 4.1.2 | definition | "Sponges are mostly asymmetrical, i.e., any plane that passes through the centre does not divide them into equal halves." | |
| F017 | 4.1.2 | definition | "When any plane passing through the central axis of the body divides the organism into two identical halves, it is called radial symmetry." | |
| F018 | 4.1.2 | example | "Coelenterates, ctenophores and echinoderms have this kind of body plan (Figure 4.1a)." | |
| F019 | 4.1.2 | definition | "Animals like annelids, arthropods, etc., where the body can be divided into identical left and right halves in only one plane, exhibit bilateral symmetry (Figure 4.1b)." | |
| F020 | 4.1.3 | definition | "Animals in which the cells are arranged in two embryonic layers, an external ectoderm and an internal endoderm, are called diploblastic animals, e.g., coelenterates." | |
| F021 | 4.1.3 | feature | "An undifferentiated layer, mesoglea, is present in between the ectoderm and the endoderm (Figure 4.2a)." | |
| F022 | 4.1.3 | definition | "Those animals in which the developing embryo has a third germinal layer, mesoderm, in between the ectoderm and endoderm, are called triploblastic animals (platyhelminthes to chordates, Figure 4.2b)." | |
| F023 | 4.1.4 | feature | "Presence or absence of a cavity between the body wall and the gut wall is very important in classification." | |
| F024 | 4.1.4 | definition | "The body cavity, which is lined by mesoderm is called coelom." | |
| F025 | 4.1.4 | example | "Animals possessing coelom are called coelomates, e.g., annelids, molluscs, arthropods, echinoderms, hemichordates and chordates (Figure 4.3a)." | |
| F026 | 4.1.4 | definition | "In some animals, the body cavity is not lined by mesoderm, instead, the mesoderm is present as scattered pouches in between the ectoderm and endoderm. Such a body cavity is called pseudocoelom and the animals possessing them are called pseudocoelomates, e.g., aschelminthes (Figure 4.3b)." | |
| F027 | 4.1.4 | definition | "The animals in which the body cavity is absent are called acoelomates, e.g., platyhelminthes (Figure 4.3c)." | |
| F028 | 4.1.5 | definition | "In some animals, the body is externally and internally divided into segments with a serial repetition of at least some organs." | |
| F029 | 4.1.5 | definition | "For example, in earthworm, the body shows this pattern called metameric segmentation and the phenomenon is known as metamerism." | |
| F030 | 4.1.6 | definition | "Notochord is a mesodermally derived rod-like structure formed on the dorsal side during embryonic development in some animals." | |
| F031 | 4.1.6 | definition | "Animals with notochord are called chordates and those animals which do not form this structure are called non-chordates, e.g., porifera to echinoderms." | |
| F032 | 4.2 | feature | "The broad classification of Animalia, based on common fundamental features as mentioned in the preceding sections, is given in Figure 4.4." | |
| F033 | 4.2 | feature | "The important characteristic features of the different phyla are described." | |
| F034 | 4.2 | exception | Figure 4.4 footnote: "*Echinodermata exhibits radial or bilateral symmetry depending on the stage." | |
| F035 | 4.2.1 | term | "Members of this phylum are commonly known as sponges." | |
| F036 | 4.2.1 | feature | "They are generally marine and mostly asymmetrical animals (Figure 4.5)." | |
| F037 | 4.2.1 | feature | "These are primitive multicellular animals and have cellular level of organisation." | |
| F038 | 4.2.1 | feature | "Sponges have a water transport or canal system." | |
| F039 | 4.2.1 | process | "Water enters through minute pores (ostia) in the body wall into a central cavity, spongocoel, from where it goes out through the osculum." | |
| F040 | 4.2.1 | feature | "This pathway of water transport is helpful in food gathering, respiratory exchange and removal of waste." | |
| F041 | 4.2.1 | term | "Choanocytes or collar cells line the spongocoel and the canals." | |
| F042 | 4.2.1 | feature | "Digestion is intracellular." | |
| F043 | 4.2.1 | feature | "The body is supported by a skeleton made up of spicules or spongin fibres." | |
| F044 | 4.2.1 | feature | "Sexes are not separate (hermaphrodite), i.e., eggs and sperms are produced by the same individual." | |
| F045 | 4.2.1 | process | "Sponges reproduce asexually by fragmentation and sexually by formation of gametes." | |
| F046 | 4.2.1 | feature | "Fertilisation is internal and development is indirect having a larval stage which is morphologically distinct from the adult." | |
| F047 | 4.2.1 | example | "Examples: Sycon (Scypha), Spongilla (Fresh water sponge) and Euspongia (Bath sponge)." | |
| F048 | 4.2.2 | feature | "They are aquatic, mostly marine, sessile or free-swimming, radially symmetrical animals (Figure 4.6)." | |
| F049 | 4.2.2 | etymology | "The name cnidaria is derived from the cnidoblasts or cnidocytes (which contain the stinging capsules or nematocysts) present on the tentacles and the body." | |
| F050 | 4.2.2 | feature | "Cnidoblasts are used for anchorage, defense and for the capture of prey (Figure 4.7)." | |
| F051 | 4.2.2 | feature | "Cnidarians exhibit tissue level of organisation and are diploblastic." | |
| F052 | 4.2.2 | feature | "They have a central gastro-vascular cavity with a single opening, mouth on hypostome." | |
| F053 | 4.2.2 | feature | "Digestion is extracellular and intracellular." | |
| F054 | 4.2.2 | example | "Some of the cnidarians, e.g., corals have a skeleton composed of calcium carbonate." | |
| F055 | 4.2.2 | feature | "Cnidarians exhibit two basic body forms called polyp and medusa (Figure 4.6)." | |
| F056 | 4.2.2 | definition | "The former is a sessile and cylindrical form like Hydra, Adamsia, etc." | |
| F057 | 4.2.2 | definition | "whereas, the latter is umbrella-shaped and free-swimming like Aurelia or jelly fish" | |
| F058 | 4.2.2 | process | "Those cnidarians which exist in both forms exhibit alternation of generations (Metagenesis), i.e., polyps produce medusae asexually and medusae form the polyps sexually (e.g., Obelia)." | |
| F059 | 4.2.2 | example | "Examples: Physalia (Portuguese man-of-war), Adamsia (Sea anemone), Pennatula (Sea-pen), Gorgonia (Sea-fan) and Meandrina (Brain coral)." | |
| F060 | 4.2.3 | term | "Ctenophores, commonly known as sea walnuts or comb jellies" | |
| F061 | 4.2.3 | feature | "are exclusively marine, radially symmetrical, diploblastic organisms with tissue level of organisation" | |
| F062 | 4.2.3 | number | "The body bears eight external rows of ciliated comb plates, which help in locomotion (Figure 4.8)." | |
| F063 | 4.2.3 | feature | "Digestion is both extracellular and intracellular." | |
| F064 | 4.2.3 | definition | "Bioluminescence (the property of a living organism to emit light) is well-marked in ctenophores." | |
| F065 | 4.2.3 | feature | "Sexes are not separate." | |
| F066 | 4.2.3 | feature | "Reproduction takes place only by sexual means." | |
| F067 | 4.2.3 | feature | "Fertilisation is external with indirect development." | |
| F068 | 4.2.3 | example | "Examples: Pleurobrachia and Ctenoplana." | |
| F069 | 4.2.4 | term | "They have dorso-ventrally flattened body, hence are called flatworms (Figure 4.9)." | |
| F070 | 4.2.4 | feature | "These are mostly endoparasites found in animals including human beings." | |
| F071 | 4.2.4 | feature | "Flatworms are bilaterally symmetrical, triploblastic and acoelomate animals with organ level of organisation." | |
| F072 | 4.2.4 | feature | "Hooks and suckers are present in the parasitic forms." | |
| F073 | 4.2.4 | feature | "Some of them absorb nutrients from the host directly through their body surface." | |
| F074 | 4.2.4 | term | "Specialised cells called flame cells help in osmoregulation and excretion." | |
| F075 | 4.2.4 | feature | "Sexes are not separate." | |
| F076 | 4.2.4 | feature | "Fertilisation is internal and development is through many larval stages." | |
| F077 | 4.2.4 | example | "Some members like Planaria possess high regeneration capacity." | |
| F078 | 4.2.4 | example | "Examples: Taenia (Tapeworm), Fasciola (Liver fluke)." | |
| F079 | 4.2.5 | term | "The body of the aschelminthes is circular in cross-section, hence, the name roundworms (Figure 4.10)." | |
| F080 | 4.2.5 | feature | "They may be freeliving, aquatic and terrestrial or parasitic in plants and animals." | |
| F081 | 4.2.5 | feature | "Roundworms have organ-system level of body organisation." | |
| F082 | 4.2.5 | feature | "They are bilaterally symmetrical, triploblastic and pseudocoelomate animals." | |
| F083 | 4.2.5 | feature | "Alimentary canal is complete with a well-developed muscular pharynx." | |
| F084 | 4.2.5 | feature | "An excretory tube removes body wastes from the body cavity through the excretory pore." | |
| F085 | 4.2.5 | feature | "Sexes are separate (dioecious), i.e., males and females are distinct." | |
| F086 | 4.2.5 | comparison | "Often females are longer than males." | |
| F087 | 4.2.5 | feature | "Fertilisation is internal and development may be direct (the young ones resemble the adult) or indirect." | |
| F088 | 4.2.5 | example | "Examples : Ascaris (Roundworm), Wuchereria (Filaria worm), Ancylostoma (Hookworm)." | |
| F089 | 4.2.6 | feature | "They may be aquatic (marine and fresh water) or terrestrial; free-living, and sometimes parasitic." | |
| F090 | 4.2.6 | feature | "They exhibit organ-system level of body organisation and bilateral symmetry." | |
| F091 | 4.2.6 | feature | "They are triploblastic, metamerically segmented and coelomate animals." | |
| F092 | 4.2.6 | etymology | "Their body surface is distinctly marked out into segments or metameres and, hence, the phylum name Annelida (Latin, annulus : little ring) (Figure 4.11)." | |
| F093 | 4.2.6 | feature | "They possess longitudinal and circular muscles which help in locomotion." | |
| F094 | 4.2.6 | feature | "Aquatic annelids like Nereis possess lateral appendages, parapodia, which help in swimming." | |
| F095 | 4.2.6 | feature | "A closed circulatory system is present." | |
| F096 | 4.2.6 | term | "Nephridia (sing. nephridium) help in osmoregulation and excretion." | |
| F097 | 4.2.6 | feature | "Neural system consists of paired ganglia (sing. ganglion) connected by lateral nerves to a double ventral nerve cord." | |
| F098 | 4.2.6 | comparison | "Nereis, an aquatic form, is dioecious, but earthworms and leeches are monoecious." | |
| F099 | 4.2.6 | feature | "Reproduction is sexual." | |
| F100 | 4.2.6 | example | "Examples : Nereis, Pheretima (Earthworm) and Hirudinaria (Blood sucking leech)." | |
| F101 | 4.2.7 | feature | "This is the largest phylum of Animalia which includes insects." | |
| F102 | 4.2.7 | number | "Over two-thirds of all named species on earth are arthropods (Figure 4.12)." | |
| F103 | 4.2.7 | feature | "They have organ-system level of organisation." | |
| F104 | 4.2.7 | feature | "They are bilaterally symmetrical, triploblastic, segmented and coelomate animals." | |
| F105 | 4.2.7 | feature | "The body of arthropods is covered by chitinous exoskeleton." | |
| F106 | 4.2.7 | feature | "The body consists of head, thorax and abdomen." | |
| F107 | 4.2.7 | etymology | "They have jointed appendages (arthros-joint, poda-appendages)." | |
| F108 | 4.2.7 | feature | "Respiratory organs are gills, book gills, book lungs or tracheal system." | |
| F109 | 4.2.7 | feature | "Circulatory system is of open type." | |
| F110 | 4.2.7 | feature | "Sensory organs like antennae, eyes (compound and simple), statocysts or balancing organs are present." | |
| F111 | 4.2.7 | feature | "Excretion takes place through malpighian tubules." | |
| F112 | 4.2.7 | feature | "They are mostly dioecious." | |
| F113 | 4.2.7 | feature | "Fertilisation is usually internal." | |
| F114 | 4.2.7 | feature | "They are mostly oviparous." | |
| F115 | 4.2.7 | feature | "Development may be direct or indirect." | |
| F116 | 4.2.7 | example | "Examples: Economically important insects – Apis (Honey bee), Bombyx (Silkworm), Laccifer (Lac insect)" | |
| F117 | 4.2.7 | example | "Vectors – Anopheles, Culex and Aedes (Mosquitoes)" | |
| F118 | 4.2.7 | example | "Gregarious pest – Locusta (Locust)" | |
| F119 | 4.2.7 | example | "Living fossil – Limulus (King crab)." | |
| F120 | 4.2.8 | number | "This is the second largest animal phylum (Figure 4.13)." | |
| F121 | 4.2.8 | feature | "Molluscs are terrestrial or aquatic (marine or fresh water) having an organ-system level of organisation." | |
| F122 | 4.2.8 | feature | "They are bilaterally symmetrical, triploblastic and coelomate animals." | |
| F123 | 4.2.8 | feature | "Body is covered by a calcareous shell and is unsegmented with a distinct head, muscular foot and visceral hump." | |
| F124 | 4.2.8 | feature | "A soft and spongy layer of skin forms a mantle over the visceral hump." | |
| F125 | 4.2.8 | definition | "The space between the hump and the mantle is called the mantle cavity in which feather like gills are present." | |
| F126 | 4.2.8 | feature | "They have respiratory and excretory functions." | |
| F127 | 4.2.8 | feature | "The anterior head region has sensory tentacles." | |
| F128 | 4.2.8 | term | "The mouth contains a file-like rasping organ for feeding, called radula." | |
| F129 | 4.2.8 | feature | "They are usually dioecious and oviparous with indirect development." | |
| F130 | 4.2.8 | example | "Examples: Pila (Apple snail), Pinctada (Pearl oyster), Sepia (Cuttlefish), Loligo (Squid), Octopus (Devil fish), Aplysia (Sea-hare), Dentalium (Tusk shell) and Chaetopleura (Chiton)." | |
| F131 | 4.2.9 | etymology | "These animals have an endoskeleton of calcareous ossicles and, hence, the name Echinodermata (Spiny bodied, Figure 4.14)." | |
| F132 | 4.2.9 | feature | "All are marine with organ-system level of organisation." | |
| F133 | 4.2.9 | comparison | "The adult echinoderms are radially symmetrical but larvae are bilaterally symmetrical." | |
| F134 | 4.2.9 | feature | "They are triploblastic and coelomate animals." | |
| F135 | 4.2.9 | feature | "Digestive system is complete with mouth on the lower (ventral) side and anus on the upper (dorsal) side." | |
| F136 | 4.2.9 | feature | "The most distinctive feature of echinoderms is the presence of water vascular system which helps in locomotion, capture and transport of food and respiration." | |
| F137 | 4.2.9 | feature | "An excretory system is absent." | |
| F138 | 4.2.9 | feature | "Sexes are separate." | |
| F139 | 4.2.9 | feature | "Reproduction is sexual." | |
| F140 | 4.2.9 | feature | "Fertilisation is usually external." | |
| F141 | 4.2.9 | feature | "Development is indirect with free-swimming larva." | |
| F142 | 4.2.9 | example | "Examples: Asterias (Star fish), Echinus (Sea urchin), Antedon (Sea lily), Cucumaria (Sea cucumber) and Ophiura (Brittle star)." | |
| F143 | 4.2.10 | comparison | "Hemichordata was earlier considered as a sub-phylum under phylum Chordata. But now it is placed as a separate phylum under non-chordata." | |
| F144 | 4.2.10 | term | "Hemichordates have a rudimentary structure in the collar region called stomochord, a structure similar to notochord." | |
| F145 | 4.2.10 | feature | "This phylum consists of a small group of worm-like marine animals with organ-system level of organisation." | |
| F146 | 4.2.10 | feature | "They are bilaterally symmetrical, triploblastic and coelomate animals." | |
| F147 | 4.2.10 | feature | "The body is cylindrical and is composed of an anterior proboscis, a collar and a long trunk (Figure 4.15)." | |
| F148 | 4.2.10 | feature | "Circulatory system is of open type." | |
| F149 | 4.2.10 | feature | "Respiration takes place through gills." | |
| F150 | 4.2.10 | term | "Excretory organ is proboscis gland." | |
| F151 | 4.2.10 | feature | "Sexes are separate." | |
| F152 | 4.2.10 | feature | "Fertilisation is external." | |
| F153 | 4.2.10 | feature | "Development is indirect." | |
| F154 | 4.2.10 | example | "Examples: Balanoglossus and Saccoglossus." | |

## Summary classification
| Summary sentence | Classification | Folded into |
|---|---|---|
| _pending session 1-Z (summary is whole-chapter content on source pages 16–17)_ | — | — |

## Exercise-gap terms
| Term/fact assumed by exercises | Explained where |
|---|---|
| _pending session 1-Z (15 exercises on source pages 17–18)_ | — |

## Figure manifest
| Fig # | Caption (verbatim) | Asset file | Source page | Mono | Verified |
|---|---|---|---|---|---|
| _pending session 1-F — 26 assets exist on disk in `assets/`, none re-verified in this arc_ | — | — | — | no | no |

## Carry-over list

1. **The prior `Ch4_AnimalKingdom_inventory.md` is untrusted and archived** as `Ch4_prior_figure_notes_UNTRUSTED.md`. It contains no Facts/heading/opener/summary/exercise rows. Do not mine it for findings; re-derive at 1-F.
2. **The archived file claims the source PDF has "14 pages"; the machine says 18** (`doc.page_count == 18`, text extracted to `scratch/ch4_gate1/ch4_source.txt`). Every source-page number in that file is therefore suspect and must be re-pinned in 1-F.
3. `Ch4_figure_audit.md` and `extract_figures.py` in this folder are from the same untrusted arc, as was the old tracker — now archived as `Ch4_prior_TRACKER_UNTRUSTED.md` and replaced by a rewritten `Ch4_AnimalKingdom_TRACKER.md` that records Gate 1 as OPEN. `extract_figures.py` may be reused as a *starting point* for 1-F rectangles only after the 440 dpi / 5 pt gridline standard (§3) is applied and each rectangle re-inspected.
4. The archived file records one asset `fig_vertebrata_chart.png` as a "bonus un-numbered" chart. §3 step 1 item 4 says **unnumbered plates are real figures**, not bonuses — 1-F must census from page images and decide its status properly (it is the "The subphylum Vertebrata is further divided as follows:" chart on source page 11, i.e. 1b territory).
5. Source page 5 extracts out of reading order: the §4.2.2 heading and its opening sentence sit at the *bottom* of the text stream while the continuation prose sits at the top. 1a-O must take the opener from the layout, not from the raw text order.
6. Source pages 11–15 render each class heading **five times** in the text layer (e.g. `4.2.11.1` × 5) — a faux-bold overprint, not five headings. 1b-H must not count duplicates.
7. TABLE 4.2 (source page 15) extracts **column-major**: all "Level of Organisation" values, then all "Symmetry" values, etc., with the phylum names last. 1b must reassemble it by column position, and check the alignment against the per-phylum prose in 1a's rows.
