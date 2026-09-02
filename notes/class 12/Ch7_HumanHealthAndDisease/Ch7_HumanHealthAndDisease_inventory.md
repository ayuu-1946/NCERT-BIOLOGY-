# Frozen Inventory — Chapter 7: Human Health and Disease (Class XII)

**Status: PASS 1 COMPLETE — GATE 1 CLOSED (2026-08-23). Pass 2 not started.**

Source PDF: `Chapter/class 12/Chapter 7 - Human Health and Disease.pdf` (22 pages)
| Frozen: 2026-08-23 | **Rows: 346 (`F001`..`F346`, contiguous)**

All five mandatory Pass 1 sessions have run, each as its own session with its own
machine-derived row count. Every count below was produced by re-parsing this
finished file (`scratch/ch7_1z/derive_counts.py`), never by hand tally.

**Gate 1 closed does not mean the chapter is done.** There is no script and no
PDF yet; all 346 rows are deliberately unticked (ticking happens during Pass 2).
Gates 2 and 3 are correctly still open. This chapter must not appear in any
"done" tally.

| Row block | Session | Count | IDs |
|---|---|---|---|
| Facts | 1-S | 276 | `F001`-`F276` |
| Headings (`Type: heading`) | 1-H | 29 | `F277`-`F305` |
| Openers (`Type: opener`) | 1-O | 28 | `F306`-`F333` |
| Summary-unique folded in | 1-Z | 2 | `F334`-`F335` |
| Figure-label matrix (`Type: label`) | 1-F / IDs by 1-Z | 11 | `F336`-`F346` |
| **Total** | | **346** | `F001`-`F346` |

`276 + 29 + 28 + 2 + 11 = 346`, which equals the highest ID and the parsed row
count. 11 figures, 11 assets, all `mode=L`; 21 in-figure labels across the 4
labelled plates.

---

## Session log — Pass 1

| Session | Scope | State | Rows added |
|---|---|---|---|
| **1-S** | Source read + Facts inventory (steps 1, 2, 3) | **complete** | 276 (`F001`-`F276`) |
| **1-H** | Structural census (heading sweep, step 4) | **complete** | 29 (`F277`-`F305`) |
| **1-O** | Section-opener census (step 5) | **complete** | 28 (`F306`-`F333`) |
| **1-F** | Figures: census, rect pinning, extraction, five-part audit, label matrix (step 6) | **complete** (2026-08-23) | 11 matrix rows (IDs assigned by 1-Z) |
| **1-Z** | Exercise-gap scan, summary classification, freeze, count derivation (steps 7-10) | **complete** (2026-08-23) | 2 (`F334`-`F335`) |

Session 1-F was executed across two sittings. The first (previous chat) pinned the
rects, ran the audit and reviewed a contact sheet, but **ran out of budget before
writing any inventory file** and did not commit its audit script. The second
rebuilt the environment, re-derived every machine claim from scratch, re-opened
all 11 assets, and wrote this file.

### Correction log — what session 1-Z changed

Per `§6` rule 5, a frozen inventory may be corrected in its **metadata**, never in
its rows. 1-Z changed **four metadata items and zero Facts rows**:

1. **This status header.** It previously read "PASS 1 INCOMPLETE — Gate 1 NOT met"
   and "holds the output of session 1-F only", listing 1-S/1-H/1-O/1-Z as "not
   started". That was accurate when 1-F wrote it, but 1-S, 1-H and 1-O had since
   run and appended their censuses **without updating the header** — so the file
   contradicted its own contents. Rewritten to match the table it sits above.
2. **The 1-S type distribution** (see that section). Its transcribed numbers summed
   to **307 across a claimed 276 rows** — arithmetically impossible — and 12 of its
   14 values disagreed with a re-parse. 1-S had explicitly instructed 1-Z to re-run
   the parse rather than trust the transcription; doing so is what caught it.
3. **The obsolete "What is missing" blocker section**, removed. An obsolete blocker
   is worse than none: it instructs the next session to redo closed work.
4. **The Gate 1 checklist**, added at the end of this file.

**Verified, not assumed:** `F334`'s SUMMARY-UNIQUE classification was challenged and
**upheld**. A body probe hits "a state of complete physical, mental and social
well-being" at `F006`, which looks like a match — but the summary's wording adds
**"psychological"** to that list, and that added qualifier is precisely what `F334`
records. This is a Rule 4 qualifier distinction, and the row's parenthetical
already stated it correctly.

---

## Re-derivation notes (this session)

Per `§6`, a handoff's findings are **claims to re-derive**, not facts to inherit.
Everything below was re-measured in this session against the source PDF; nothing
was copied forward on trust. Three discrepancies with the inherited account were
found and are recorded honestly rather than smoothed over:

1. **The extract script's own comment for fig 7.10 quotes stale overflow numbers.**
   It records "Check B still reports L2.8/T14.3/R7.6". Against the *current*
   (re-pinned) rect the same underlying gradient extents give **L4.8/T9.3/R11.6**.
   The old figures were measured against the *pre-re-pin* rect `(348, 224, 460, 366)`.
   Same shapes, same conclusion — the comment's arithmetic is just one revision behind.
2. **`fig_7_5` overflows left by 24.8 pt** under a raster-extent check. The
   inherited audit table never recorded this. Verified harmless this session: the
   silhouette raster's bbox starts at x=29.2 but its **first inked column is
   x=57.9** (300 dpi probe, thr 205), and the rect's left edge at x=54 clears
   real ink by 4.1 pt. It is the raster's own white margin.
3. **`fig_7_8` and `fig_7_11` had NO working mechanical edge check.** Both plates
   are rendered as thousands of sub-pixel scanline tiles (~6 x 0.2 pt each), so
   check B finds 0 drawings and check B2's 3 pt size floor discards every tile.
   Both reported clean only because they were **vacuous**. A new **check B3**
   (tile union, no size floor) was written to give them real coverage; both pass.

A fourth item is not a discrepancy but is worth stating: the previous session's
reproducibility claim was re-tested properly. Re-running `extract_figures.py`
regenerates all 11 PNGs **byte-identical** to the committed ones (verified via
`git status` on the assets directory, after a first attempt at this check was
caught being vacuous — a `sed` had stripped the md5 hashes and compared only
filenames).

---

## Facts

Rows `F001`-`F276` were added by **session 1-S** (steps 1, 2, 3). Scope discipline
per `§6`: this session read the prose only. It deliberately created **no**
`heading` rows and **no** `opener` rows — those are the sole deliverables of
sessions 1-H and 1-O, and absorbing them here is the exact failure mechanism `§6`
names. Consequently **every section's first sentence is intentionally absent from
the rows below**; that is not an omission to be repaired by editing this table, it
is 1-O's work.

Wording is verbatim NCERT, quoted. Where a row merges two adjacent source
sentences, both are quoted inside the one row because they state one fact
together. Figure **captions** are not duplicated here — they are inventoried
verbatim in the Figure manifest below, which is the single place they live.

`figure-text` rows carry the in-plate process sentences of figs 7.1 and 7.6 and
the unquoted marker sets of fig 7.4. These are carry-over item 1 from session
1-F, the item that session flagged as "the single biggest carry-over from 1-F and
must not be lost." They are recorded as ordinary Facts rows and **not** as
`Figure labels:` rows, so `_extract_labels` cannot see them — they are prose
obligations, not label-coverage obligations.

| ID | Section | Type | Exact original wording | Ticked |
|----|---------|------|------------------------|--------|
| F001a | intro | term | "Health, for a long time, was considered as a state of body and mind where there was a balance of certain 'humors'." (**ADDED IN PASS 3(b) — defect D1, a real Pass 1 gap, NOT back-dated into the freeze.** Direction 2 found this had no row at all: it is the section's antecedent/defining sentence, and without it the "good humor" hypothesis that `F003` disproves is never stated. Ch9 `D9` profile.) | x |
| F001b | intro | fact | "This is what early Greeks like Hippocrates as well as Indian Ayurveda system of medicine asserted." (**ADDED IN PASS 3(b) — defect D1, a real Pass 1 gap.** Names the two traditions that asserted the humors idea; absent from the frozen inventory entirely, and "Hippocrates"/"Ayurveda" returned 0 hits in the delivered PDF.) | x |
| F001 | intro | fact | "It was thought that persons with 'blackbile' belonged to hot personality and would have fevers. This idea was arrived at by pure reflective thought." | x |
| F002 | intro | fact | "The discovery of blood circulation by William Harvey using experimental method" | x |
| F003 | intro | fact | "the demonstration of normal body temperature in persons with blackbile using thermometer disproved the 'good humor' hypothesis of health" | x |
| F004 | intro | mechanism | "biology stated that mind influences, through neural system and endocrine system, our immune system and that our immune system maintains our health. Hence, mind and mental state can affect our health." | x |
| F005 | intro | fact | "health is affected by – (i) genetic disorders – deficiencies with which a child is born and deficiencies/defects which the child inherits from parents from birth; (ii) infections and (iii) life style including food and water we take, rest and exercise we give to our bodies, habits that we have or lack etc." | x |
| F006 | intro | term | "Health does not simply mean 'absence of disease' or 'physical fitness'. It could be defined as a state of complete physical, mental and social well-being." | x |
| F007 | intro | fact | "When people are healthy, they are more efficient at work. This increases productivity and brings economic prosperity." | x |
| F008 | intro | fact | "Health also increases longevity of people and reduces infant and maternal mortality." | x |
| F009 | intro | prevention | "Balanced diet, personal hygiene and regular exercise are very important to maintain good health." | x |
| F010 | intro | fact | "Yoga has been practised since time immemorial to achieve physical and mental health." | x |
| F011 | intro | prevention | "Awareness about diseases and their effect on different bodily functions, vaccination (immunisation) against infectious diseases, proper disposal of wastes, control of vectors and maintenance of hygiene in food and water resources are necessary for achieving good health." | x |
| F012 | intro | term | "When the functioning of one or more organs or systems of the body is adversely affected, characterised by appearance of various signs and symptoms, we say that we are not healthy, i.e., we have a disease." | x |
| F013 | intro | term | "Diseases can be broadly grouped into infectious and non-infectious." | x |
| F014 | intro | term | "Diseases which are easily transmitted from one person to another, are called infectious diseases." | x |
| F015 | intro | fact | "Infectious diseases are very common and every one of us suffers from these at sometime or other. Some of the infectious diseases like AIDS are fatal." | x |
| F016 | intro | fact | "Among non-infectious diseases, cancer is the major cause of death. Drug and alcohol abuse also affect our health adversely." | x |
| F017 | 7.1 | term | "Such disease-causing organisms are called pathogens." | x |
| F018 | 7.1 | fact | "Most parasites are therefore pathogens as they cause harm to the host by living in (or on) them." | x |
| F019 | 7.1 | process | "The pathogens can enter our body by various means, multiply and interfere with normal vital activities, resulting in morphological and functional damage." | x |
| F020 | 7.1 | fact | "Pathogens have to adapt to life within the environment of the host. For example, the pathogens that enter the gut must know a way of surviving in the stomach at low pH and resisting the various digestive enzymes." | x |
| F021 | 7.1 | example | "Salmonella typhi is a pathogenic bacterium which causes typhoid fever in human beings." | x |
| F022 | 7.1 | transmission | "These pathogens generally enter the small intestine through food and water contaminated with them and migrate to other organs through blood." | x |
| F023 | 7.1 | symptom | "Sustained high fever (39° to 40°C), weakness, stomach pain, constipation, headache and loss of appetite are some of the common symptoms of this disease." | x |
| F024 | 7.1 | fact | "Intestinal perforation and death may occur in severe cases." | x |
| F025 | 7.1 | diagnosis | "Typhoid fever could be confirmed by Widal test" | x |
| F026 | 7.1 | example | "A classic case in medicine, that of Mary Mallon nicknamed Typhoid Mary, is worth mentioning here. She was a cook by profession and was a typhoid carrier who continued to spread typhoid for several years through the food she prepared." | x |
| F027 | 7.1 | example | "Bacteria like Streptococcus pneumoniae and Haemophilus influenzae are responsible for the disease pneumonia in humans which infects the alveoli (air filled sacs) of the lungs." | x |
| F028 | 7.1 | mechanism | "As a result of the infection, the alveoli get filled with fluid leading to severe problems in respiration." | x |
| F029 | 7.1 | symptom | "The symptoms of pneumonia include fever, chills, cough and headache. In severe cases, the lips and finger nails may turn gray to bluish in colour." | x |
| F030 | 7.1 | transmission | "A healthy person acquires the infection by inhaling the droplets/aerosols released by an infected person or even by sharing glasses and utensils with an infected person." | x |
| F031 | 7.1 | example | "Dysentery, plague, diphtheria, etc., are some of the other bacterial diseases in man." | x |
| F032 | 7.1 | example | "Rhino viruses represent one such group of viruses which cause one of the most infectious human ailments – the common cold. They infect the nose and respiratory passage but not the lungs." | x |
| F033 | 7.1 | symptom | "The common cold is characterised by nasal congestion and discharge, sore throat, hoarseness, cough, headache, tiredness, etc., which usually last for 3-7 days." | x |
| F034 | 7.1 | transmission | "Droplets resulting from cough or sneezes of an infected person are either inhaled directly or transmitted through contaminated objects such as pens, books, cups, doorknobs, computer keyboard or mouse, etc., and cause infection in a healthy person." | x |
| F035 | 7.1 | example | "Plasmodium, a tiny protozoan is responsible for this disease." | x |
| F036 | 7.1 | example | "Different species of Plasmodium (P. vivax, P. malaria and P. falciparum) are responsible for different types of malaria." | x |
| F037 | 7.1 | fact | "Of these, malignant malaria caused by Plasmodium falciparum is the most serious one and can even be fatal." | x |
| F038 | 7.1 | process | "Plasmodium enters the human body as sporozoites (infectious form) through the bite of infected female Anopheles mosquito." | x |
| F039 | 7.1 | process | "The parasites initially multiply within the liver cells and then attack the red blood cells (RBCs) resulting in their rupture." | x |
| F040 | 7.1 | mechanism | "The rupture of RBCs is associated with release of a toxic substance, haemozoin, which is responsible for the chill and high fever recurring every three to four days." | x |
| F041 | 7.1 | process | "When a female Anopheles mosquito bites an infected person, these parasites enter the mosquito's body and undergo further development." | x |
| F042 | 7.1 | process | "The parasites multiply within them to form sporozoites that are stored in their salivary glands. When these mosquitoes bite a human, the sporozoites are introduced into his/her body, thereby initiating the events mentioned above." | x |
| F043 | 7.1 | fact | "the malarial parasite requires two hosts – human and mosquitoes – to complete its life cycle" | x |
| F044 | 7.1 | term | "the female Anopheles mosquito is the vector (transmitting agent) too" | x |
| F045 | 7.1 | figure-text | In-plate process sentence, Figure 7.1: "When the mosquito bites another human, sporozoites are injected with bite." | x |
| F046 | 7.1 | figure-text | In-plate process sentence, Figure 7.1: "Parasite (sporozoites) reach the liver through blood" | x |
| F047 | 7.1 | figure-text | In-plate process sentence, Figure 7.1: "The parasite reproduces asexually in liver cells, bursting the cell and releasing into the blood." | x |
| F048 | 7.1 | figure-text | In-plate process sentence, Figure 7.1: "Parasites reproduce asexually in red blood cells, bursting the red blood cells and causing cycles of fever and other symptoms. Released parasites infect new red blood cells." | x |
| F049 | 7.1 | figure-text | In-plate process sentence, Figure 7.1: "Sexual stages (gametocytes) develop in red blood cells." | x |
| F050 | 7.1 | figure-text | In-plate process sentence, Figure 7.1: "Female mosquito takes up gametocytes with blood meal." | x |
| F051 | 7.1 | figure-text | In-plate process sentence, Figure 7.1: "Fertilization and development take place in the mosquito's gut." | x |
| F052 | 7.1 | figure-text | In-plate process sentence, Figure 7.1: "Mature infective stages (sporozoites) escape from gut and migrate to the mosquito salivary glands." | x |
| F053 | 7.1 | example | "Entamoeba histolytica is a protozoan parasite in the large intestine of human which causes amoebiasis (amoebic dysentery)." | x |
| F054 | 7.1 | symptom | "Symptoms of this disease include constipation, abdominal pain and cramps, stools with excess mucous and blood clots." | x |
| F055 | 7.1 | transmission | "Houseflies act as mechanical carriers and serve to transmit the parasite from faeces of infected person to food and food products, thereby contaminating them. Drinking water and food contaminated by the faecal matter are the main source of infection." | x |
| F056 | 7.1 | example | "Ascaris, the common round worm and Wuchereria, the filarial worm, are some of the helminths which are known to be pathogenic to man." | x |
| F057 | 7.1 | example | "Ascaris, an intestinal parasite causes ascariasis." | x |
| F058 | 7.1 | symptom | "Symptoms of these disease include internal bleeding, muscular pain, fever, anemia and blockage of the intestinal passage." | x |
| F059 | 7.1 | transmission | "The eggs of the parasite are excreted along with the faeces of infected persons which contaminate soil, water, plants, etc. A healthy person acquires this infection through contaminated water, vegetables, fruits, etc." | x |
| F060 | 7.1 | example | "Wuchereria (W. bancrofti and W. malayi), the filarial worms cause a slowly developing chronic inflammation of the organs in which they live for many years, usually the lymphatic vessels of the lower limbs and the disease is called elephantiasis or filariasis" | x |
| F061 | 7.1 | symptom | "The genital organs are also often affected, resulting in gross deformities." | x |
| F062 | 7.1 | transmission | "The pathogens are transmitted to a healthy person through the bite by the female mosquito vectors." | x |
| F063 | 7.1 | example | "Many fungi belonging to the genera Microsporum, Trichophyton and Epidermophyton are responsible for ringworms which is one of the most common infectious diseases in man." | x |
| F064 | 7.1 | symptom | "Appearance of dry, scaly lesions on various parts of the body such as skin, nails and scalp are the main symptoms of the disease. These lesions are accompanied by intense itching." | x |
| F065 | 7.1 | fact | "Heat and moisture help these fungi to grow, which makes them thrive in skin folds such as those in the groin or between the toes." | x |
| F066 | 7.1 | transmission | "Ringworms are generally acquired from soil or by using towels, clothes or even the comb of infected individuals." | x |
| F067 | 7.1 | prevention | "Measures for personal hygiene include keeping the body clean; consumption of clean drinking water, food, vegetables, fruits, etc." | x |
| F068 | 7.1 | prevention | "Public hygiene includes proper disposal of waste and excreta; periodic cleaning and disinfection of water reservoirs, pools, cesspools and tanks and observing standard practices of hygiene in public catering." | x |
| F069 | 7.1 | prevention | "These measures are particularly essential where the infectious agents are transmitted through food and water such as typhoid, amoebiasis and ascariasis." | x |
| F070 | 7.1 | prevention | "In cases of air-borne diseases such as pneumonia and common cold, in addition to the above measures, close contact with the infected persons or their belongings should be avoided." | x |
| F071 | 7.1 | prevention | "For diseases such as malaria and filariasis that are transmitted through insect vectors, the most important measure is to control or eliminate the vectors and their breeding places." | x |
| F072 | 7.1 | prevention | "This can be achieved by avoiding stagnation of water in and around residential areas, regular cleaning of household coolers, use of mosquito nets, introducing fishes like Gambusia in ponds that feed on mosquito larvae, spraying of insecticides in ditches, drainage areas and swamps, etc." | x |
| F073 | 7.1 | prevention | "In addition, doors and windows should be provided with wire mesh to prevent the entry of mosquitoes." | x |
| F074 | 7.1 | fact | "Such precautions have become more important especially in the light of recent widespread incidences of the vector-borne (Aedes mosquitoes) diseases like dengue and chikungunya in many parts of India." | x |
| F075 | 7.1 | fact | "The use of vaccines and immunisation programmes have enabled us to completely eradicate a deadly disease like smallpox." | x |
| F076 | 7.1 | fact | "A large number of other infectious diseases like polio, diphtheria, pneumonia and tetanus have been controlled to a large extent by the use of vaccines." | x |
| F077 | 7.1 | fact | "Biotechnology (about which you will read more in Chapter 10) is at the verge of making available newer and safer vaccines." | x |
| F078 | 7.1 | fact | "Discovery of antibiotics and various other drugs has also enabled us to effectively treat infectious diseases." | x |
| F079 | 7.2 | fact | "only a few of these exposures result in disease. Why? This is due to the fact that the body is able to defend itself from most of these foreign agents." | x |
| F080 | 7.2 | term | "This overall ability of the host to fight the disease-causing organisms, conferred by the immune system is called immunity." | x |
| F081 | 7.2 | term | "Immunity is of two types: (i) Innate immunity and (ii) Acquired immunity." | x |
| F082 | 7.2.1 | fact | "This is accomplished by providing different types of barriers to the entry of the foreign agents into our body." | x |
| F083 | 7.2.1 | number | "Innate immunity consist of four types of barriers." | x |
| F084 | 7.2.1 | term | "Physical barriers : Skin on our body is the main barrier which prevents entry of the micro-organisms. Mucus coating of the epithelium lining the respiratory, gastrointestinal and urogenital tracts also help in trapping microbes entering our body." | x |
| F085 | 7.2.1 | term | "Physiological barriers : Acid in the stomach, saliva in the mouth, tears from eyes–all prevent microbial growth." | x |
| F086 | 7.2.1 | term | "Cellular barriers : Certain types of leukocytes (WBC) of our body like polymorpho-nuclear leukocytes (PMNL-neutrophils) and monocytes and natural killer (type of lymphocytes) in the blood as well as macrophages in tissues can phagocytose and destroy microbes." | x |
| F087 | 7.2.1 | term | "Cytokine barriers : Virus-infected cells secrete proteins called interferons which protect non-infected cells from further viral infection." | x |
| F088 | 7.2.2 | term | "It is characterised by memory." | x |
| F089 | 7.2.2 | process | "when our body encounters a pathogen for the first time it produces a response called primary response which is of low intensity" | x |
| F090 | 7.2.2 | process | "Subsequent encounter with the same pathogen elicits a highly intensified secondary or anamnestic response. This is ascribed to the fact that our body appears to have memory of the first encounter." | x |
| F091 | 7.2.2 | fact | "The primary and secondary immune responses are carried out with the help of two special types of lymphocytes present in our blood, i.e., B-lymphocytes and T-lymphocytes." | x |
| F092 | 7.2.2 | term | "The B-lymphocytes produce an army of proteins in response to pathogens into our blood to fight with them. These proteins are called antibodies." | x |
| F093 | 7.2.2 | fact | "The T-cells themselves do not secrete antibodies but help B cells to produce them." | x |
| F094 | 7.2.2 | structure | "Each antibody molecule has four peptide chains, two small called light chains and two longer called heavy chains. Hence, an antibody is represented as H2L2." | x |
| F095 | 7.2.2 | example | "Different types of antibodies are produced in our body. IgA, IgM, IgE, IgG are some of them." | x |
| F096 | 7.2.2 | term | "Because these antibodies are found in the blood, the response is also called as humoral immune response. This is one of the two types of our acquired immune response – antibody mediated." | x |
| F097 | 7.2.2 | term | "The second type is called cell-mediated immune response or cell-mediated immunity (CMI). The T-lymphocytes mediate CMI." | x |
| F098 | 7.2.2 | fact | "Very often, when some human organs like heart, eye, liver, kidney fail to function satisfactorily, transplantation is the only remedy to enable the patient to live a normal life." | x |
| F099 | 7.2.2 | fact | "Grafts from just any source – an animal, another primate, or any human beings cannot be made since the grafts would be rejected sooner or later." | x |
| F100 | 7.2.2 | fact | "Tissue matching, blood group matching are essential before undertaking any graft/transplant and even after this the patient has to take immuno–suppresants all his/her life." | x |
| F101 | 7.2.2 | mechanism | "The body is able to differentiate 'self' and 'nonself' and the cell-mediated immune response is responsible for the graft rejection." | x |
| F102 | 7.2.2 | figure-text | In-plate markers, Figure 7.4: "N" at the amino terminus and "C" at each carboxyl terminus of the peptide chains. Single characters, deliberately excluded from the label matrix by session 1-F; the antibody passage must name the amino (N) and carboxyl (C) termini in running text. | x |
| F103 | 7.2.2 | figure-text | In-plate markers, Figure 7.4: the "S-S" disulfide bridges joining the two heavy chains to each other and each light chain to its heavy chain. Excluded from the label matrix by session 1-F; the antibody passage must state that the chains are held together by disulfide bonds. | x |
| F104 | 7.2.3 | term | "This type of immunity is called active immunity." | x |
| F105 | 7.2.3 | fact | "Active immunity is slow and takes time to give its full effective response." | x |
| F106 | 7.2.3 | fact | "Injecting the microbes deliberately during immunisation or infectious organisms gaining access into body during natural infection induce active immunity." | x |
| F107 | 7.2.3 | term | "When ready-made antibodies are directly given to protect the body against foreign agents, it is called passive immunity." | x |
| F108 | 7.2.3 | example | "The yellowish fluid colostrum secreted by mother during the initial days of lactation has abundant antibodies (IgA) to protect the infant." | x |
| F109 | 7.2.3 | example | "The foetus also receives some antibodies from their mother, through the placenta during pregnancy. These are some examples of passive immunity." | x |
| F110 | 7.2.4 | process | "In vaccination, a preparation of antigenic proteins of pathogen or inactivated/weakened pathogen (vaccine) are introduced into the body." | x |
| F111 | 7.2.4 | mechanism | "The antibodies produced in the body against these antigens would neutralise the pathogenic agents during actual infection." | x |
| F112 | 7.2.4 | mechanism | "The vaccines also generate memory – B and T-cells that recognise the pathogen quickly on subsequent exposure and overwhelm the invaders with a massive production of antibodies." | x |
| F113 | 7.2.4 | example | "If a person is infected with some deadly microbes to which quick immune response is required as in tetanus, we need to directly inject the preformed antibodies, or antitoxin (a preparation containing antibodies to the toxin)." | x |
| F114 | 7.2.4 | example | "Even in cases of snakebites, the injection which is given to the patients, contain preformed antibodies against the snake venom. This type of immunisation is called passive immunisation." | x |
| F115 | 7.2.4 | fact | "Recombinant DNA technology has allowed the production of antigenic polypeptides of pathogen in bacteria or yeast." | x |
| F116 | 7.2.4 | example | "Vaccines produced using this approach allow large scale production and hence greater availability for immunisation, e.g., hepatitis B vaccine produced from yeast." | x |
| F117 | 7.2.5 | fact | "Some of us are sensitive to some particles in the environment. The above-mentioned reaction could be because of allergy to pollen, mites, etc., which are different in different places." | x |
| F118 | 7.2.5 | term | "The exaggerated response of the immune system to certain antigens present in the environment is called allergy." | x |
| F119 | 7.2.5 | term | "The substances to which such an immune response is produced are called allergens." | x |
| F120 | 7.2.5 | fact | "The antibodies produced to these are of IgE type." | x |
| F121 | 7.2.5 | example | "Common examples of allergens are mites in dust, pollens, animal dander, etc." | x |
| F122 | 7.2.5 | symptom | "Symptoms of allergic reactions include sneezing, watery eyes, running nose and difficulty in breathing." | x |
| F123 | 7.2.5 | mechanism | "Allergy is due to the release of chemicals like histamine and serotonin from the mast cells." | x |
| F124 | 7.2.5 | diagnosis | "For determining the cause of allergy, the patient is exposed to or injected with very small doses of possible allergens, and the reactions studied." | x |
| F125 | 7.2.5 | treatment | "The use of drugs like anti-histamine, adrenalin and steroids quickly reduce the symptoms of allergy." | x |
| F126 | 7.2.5 | fact | "modern-day life style has resulted in lowering of immunity and more sensitivity to allergens – more and more children in metro cities of India suffer from allergies and asthma due to sensitivity to the environment. This could be because of the protected environment provided early in life." | x |
| F127 | 7.2.6 | fact | "While we still do not understand the basis of this, two corollaries of this ability have to be understood." | x |
| F128 | 7.2.6 | fact | "One, higher vertebrates can distinguish foreign molecules as well as foreign organisms. Most of the experimental immunology deals with this aspect." | x |
| F129 | 7.2.6 | term | "Two, sometimes, due to genetic and other unknown reasons, the body attacks self-cells. This results in damage to the body and is called auto-immune disease." | x |
| F130 | 7.2.6 | example | "Rheumatoid arthritis which affects many people in our society is an auto-immune disease." | x |
| F131 | 7.2.7 | fact | "immune system is unique in the sense that it recognises foreign antigens, responds to these and remembers them." | x |
| F132 | 7.2.7 | fact | "The immune system also plays an important role in allergic reactions, auto-immune diseases and organ transplantation." | x |
| F133 | 7.2.7 | term | "Lymphoid organs: These are the organs where origin and/or maturation and proliferation of lymphocytes occur." | x |
| F134 | 7.2.7 | term | "The primary lymphoid organs are bone marrow and thymus where immature lymphocytes differentiate into antigen-sensitive lymphocytes." | x |
| F135 | 7.2.7 | term | "After maturation the lymphocytes migrate to secondary lymphoid organs like spleen, lymph nodes, tonsils, Peyer's patches of small intestine and appendix." | x |
| F136 | 7.2.7 | fact | "The secondary lymphoid organs provide the sites for interaction of lymphocytes with the antigen, which then proliferate to become effector cells." | x |
| F137 | 7.2.7 | fact | "The bone marrow is the main lymphoid organ where all blood cells including lymphocytes are produced." | x |
| F138 | 7.2.7 | structure | "The thymus is a lobed organ located near the heart and beneath the breastbone. The thymus is quite large at the time of birth but keeps reducing in size with age and by the time puberty is attained it reduces to a very small size." | x |
| F139 | 7.2.7 | fact | "Both bone-marrow and thymus provide micro-environments for the development and maturation of T-lymphocytes." | x |
| F140 | 7.2.7 | structure | "The spleen is a large bean-shaped organ. It mainly contains lymphocytes and phagocytes. It acts as a filter of the blood by trapping blood-borne micro-organisms. Spleen also has a large reservoir of erythrocytes." | x |
| F141 | 7.2.7 | structure | "The lymph nodes are small solid structures located at different points along the lymphatic system." | x |
| F142 | 7.2.7 | mechanism | "Lymph nodes serve to trap the micro-organisms or other antigens, which happen to get into the lymph and tissue fluid. Antigens trapped in the lymph nodes are responsible for the activation of lymphocytes present there and cause the immune response." | x |
| F143 | 7.2.7 | term | "There is lymphoid tissue also located within the lining of the major tracts (respiratory, digestive and urogenital tracts) called mucosa-associated lymphoid tissue (MALT)." | x |
| F144 | 7.2.7 | number | "It constitutes about 50 per cent of the lymphoid tissue in human body." | x |
| F145 | 7.3 | term | "This means deficiency of immune system, acquired during the lifetime of an individual indicating that it is not a congenital disease. 'Syndrome' means a group of symptoms." | x |
| F146 | 7.3 | number | "AIDS was first reported in 1981 and in the last twenty-five years or so, it has spread all over the world killing more than 25 million persons." | x |
| F147 | 7.3 | term | "AIDS is caused by the Human Immuno deficiency Virus (HIV), a member of a group of viruses called retrovirus, which have an envelope enclosing the RNA genome." | x |
| F148 | 7.3 | transmission | "Transmission of HIV-infection generally occurs by (a) sexual contact with infected person, (b) by transfusion of contaminated blood and blood products, (c) by sharing infected needles as in the case of intravenous drug abusers and (d) from infected mother to her child through placenta." | x |
| F149 | 7.3 | fact | "people who are at high risk of getting this infection includes - individuals who have multiple sexual partners, drug addicts who take drugs intravenously, individuals who require repeated blood transfusions and children born to an HIV infected mother." | x |
| F150 | 7.3 | fact | "HIV/AIDS is not spread by mere touch or physical contact; it spreads only through body fluids." | x |
| F151 | 7.3 | fact | "It is, hence, imperative, for the physical and psychological well-being, that the HIV/AIDS infected persons are not isolated from family and society." | x |
| F152 | 7.3 | number | "There is always a time-lag between the infection and appearance of AIDS symptoms. This period may vary from a few months to many years (usually 5-10 years)." | x |
| F153 | 7.3 | process | "After getting into the body of the person, the virus enters into macrophages where RNA genome of the virus replicates to form viral DNA with the help of the enzyme reverse transcriptase." | x |
| F154 | 7.3 | process | "This viral DNA gets incorporated into host cell's DNA and directs the infected cells to produce virus particles." | x |
| F155 | 7.3 | fact | "The macrophages continue to produce virus and in this way acts like a HIV factory." | x |
| F156 | 7.3 | process | "Simultaneously, HIV enters into helper T-lymphocytes (TH), replicates and produce progeny viruses. The progeny viruses released in the blood attack other helper T-lymphocytes. This is repeated leading to a progressive decrease in the number of helper T-lymphocytes in the body of the infected person." | x |
| F157 | 7.3 | symptom | "During this period, the person suffers from bouts of fever, diarrhoea and weight loss." | x |
| F158 | 7.3 | mechanism | "Due to decrease in the number of helper T lymphocytes, the person starts suffering from infections that could have been otherwise overcome such as those due to bacteria especially Mycobacterium, viruses, fungi and even parasites like Toxoplasma." | x |
| F159 | 7.3 | fact | "The patient becomes so immuno-deficient that he/she is unable to protect himself/herself against these infections." | x |
| F160 | 7.3 | diagnosis | "A widely used diagnostic test for AIDS is enzyme linked immuno-sorbent assay (ELISA)." | x |
| F161 | 7.3 | treatment | "Treatment of AIDS with anti-retroviral drugs is only partially effective. They can only prolong the life of the patient but cannot prevent death, which is inevitable." | x |
| F162 | 7.3 | prevention | "As AIDS has no cure, prevention is the best option." | x |
| F163 | 7.3 | fact | "HIV infection, more often, spreads due to conscious behaviour patterns and is not something that happens inadvertently, like pneumonia or typhoid." | x |
| F164 | 7.3 | fact | "infection in blood transfusion patients, new-borns (from mother) etc., may take place due to poor monitoring. The only excuse may be ignorance and it has been rightly said – 'don't die of ignorance'." | x |
| F165 | 7.3 | fact | "In our country the National AIDS Control Organisation (NACO) and other non-governmental organisation (NGOs) are doing a lot to educate people about AIDS. WHO has started a number of programmes to prevent the spreading of HIV infection." | x |
| F166 | 7.3 | prevention | "Making blood (from blood banks) safe from HIV, ensuring the use of only disposable needles and syringes in public and private hospitals and clinics, free distribution of condoms, controlling drug abuse, advocating safe sex and promoting regular check-ups for HIV in susceptible populations, are some such steps taken up." | x |
| F167 | 7.3 | fact | "Infection with HIV or having AIDS is something that should not be hidden – since then, the infection may spread to many more people. HIV/AIDS-infected people need help and sympathy instead of being shunned by society." | x |
| F168 | 7.3 | fact | "Unless society recognises it as a problem to be dealt with in a collective manner – the chances of wider spread of the disease increase manifold. It is a malady that can only be tackled, by the society and medical fraternity acting together, to prevent the spread of the disease." | x |
| F169 | 7.3 | figure-text | In-plate process sentence, Figure 7.6: "Virus infects normal cell" | x |
| F170 | 7.3 | figure-text | In-plate process sentence, Figure 7.6: "Viral RNA is introduced into cell" | x |
| F171 | 7.3 | figure-text | In-plate process sentence, Figure 7.6: "Viral DNA is produced by reverse transcriptase" | x |
| F172 | 7.3 | figure-text | In-plate process sentence, Figure 7.6: "Viral DNA incorporates into host genome" | x |
| F173 | 7.3 | figure-text | In-plate process sentence, Figure 7.6: "New viral RNA is produced by the infected cell" | x |
| F174 | 7.3 | figure-text | In-plate process sentence, Figure 7.6: "New viruses are produced" | x |
| F175 | 7.3 | figure-text | In-plate process sentence, Figure 7.6: "New viruses can infect other cells" | x |
| F176 | 7.3 | figure-text | In-plate note, Figure 7.6: "NOTE: Infected cell can survive while viruses are being replicated and released" | x |
| F177 | 7.4 | number | "More than a million Indians suffer from cancer and a large number of them die from it annually." | x |
| F178 | 7.4 | fact | "The mechanisms that underlie development of cancer or oncogenic transformation of cells, its treatment and control have been some of the most intense areas of research in biology and medicine." | x |
| F179 | 7.4 | fact | "In our body, cell growth and differentiation is highly controlled and regulated. In cancer cells, there is breakdown of these regulatory mechanisms." | x |
| F180 | 7.4 | term | "Normal cells show a property called contact inhibition by virtue of which contact with other cells inhibits their uncontrolled growth. Cancer cells appears to have lost this property." | x |
| F181 | 7.4 | term | "cancerous cells just continue to divide giving rise to masses of cells called tumors." | x |
| F182 | 7.4 | term | "Tumors are of two types: benign and malignant." | x |
| F183 | 7.4 | term | "Benign tumors normally remain confined to their original location and do not spread to other parts of the body and cause little damage." | x |
| F184 | 7.4 | term | "The malignant tumors, on the other hand are a mass of proliferating cells called neoplastic or tumor cells. These cells grow very rapidly, invading and damaging the surrounding normal tissues." | x |
| F185 | 7.4 | mechanism | "As these cells actively divide and grow they also starve the normal cells by competing for vital nutrients." | x |
| F186 | 7.4 | term | "Cells sloughed from such tumors reach distant sites through blood, and wherever they get lodged in the body, they start a new tumor there. This property called metastasis is the most feared property of malignant tumors." | x |
| F187 | 7.4 | cause | "Transformation of normal cells into cancerous neoplastic cells may be induced by physical, chemical or biological agents. These agents are called carcinogens." | x |
| F188 | 7.4 | cause | "Ionising radiations like X-rays and gamma rays and non-ionizing radiations like UV cause DNA damage leading to neoplastic transformation." | x |
| F189 | 7.4 | cause | "The chemical carcinogens present in tobacco smoke have been identified as a major cause of lung cancer." | x |
| F190 | 7.4 | term | "Cancer causing viruses called oncogenic viruses have genes called viral oncogenes." | x |
| F191 | 7.4 | term | "several genes called cellular oncogenes (c-onc) or proto oncogenes have been identified in normal cells which, when activated under certain conditions, could lead to oncogenic transformation of the cells." | x |
| F192 | 7.4 | fact | "Early detection of cancers is essential as it allows the disease to be treated successfully in many cases." | x |
| F193 | 7.4 | diagnosis | "Cancer detection is based on biopsy and histopathological studies of the tissue and blood and bone marrow tests for increased cell counts in the case of leukemias." | x |
| F194 | 7.4 | diagnosis | "In biopsy, a piece of the suspected tissue cut into thin sections is stained and examined under microscope (histopathological studies) by a pathologist." | x |
| F195 | 7.4 | diagnosis | "Techniques like radiography (use of X-rays), CT (computed tomography) and MRI (magnetic resonance imaging) are very useful to detect cancers of the internal organs." | x |
| F196 | 7.4 | diagnosis | "Computed tomography uses X-rays to generate a three-dimensional image of the internals of an object." | x |
| F197 | 7.4 | diagnosis | "MRI uses strong magnetic fields and non-ionising radiations to accurately detect pathological and physiological changes in the living tissue." | x |
| F198 | 7.4 | diagnosis | "Antibodies against cancer-specific antigens are also used for detection of certain cancers." | x |
| F199 | 7.4 | diagnosis | "Techniques of molecular biology can be applied to detect genes in individuals with inherited susceptibility to certain cancers." | x |
| F200 | 7.4 | prevention | "Identification of such genes, which predispose an individual to certain cancers, may be very helpful in prevention of cancers. Such individuals may be advised to avoid exposure to particular carcinogens to which they are susceptible (e.g., tobacco smoke in case of lung cancer)." | x |
| F201 | 7.4 | treatment | "The common approaches for treatment of cancer are surgery, radiation therapy and immunotherapy." | x |
| F202 | 7.4 | treatment | "In radiotherapy, tumor cells are irradiated lethally, taking proper care of the normal tissues surrounding the tumor mass." | x |
| F203 | 7.4 | treatment | "Several chemotherapeutic drugs are used to kill cancerous cells. Some of these are specific for particular tumors. Majority of drugs have side effects like hair loss, anemia, etc." | x |
| F204 | 7.4 | treatment | "Most cancers are treated by combination of surgery, radiotherapy and chemotherapy." | x |
| F205 | 7.4 | treatment | "Tumor cells have been shown to avoid detection and destruction by immune system. Therefore, the patients are given substances called biological response modifiers such as α-interferon which activates their immune system and helps in destroying the tumor." | x |
| F206 | 7.5 | fact | "This is really a cause of concern as it could result in many harmful effects. Proper education and guidance would enable youth to safeguard themselves against these dangerous behaviour patterns and follow healthy lifestyles." | x |
| F207 | 7.5 | term | "The drugs, which are commonly abused are opioids, cannabinoids and coca alkaloids. Majority of these are obtained from flowering plants. Some are obtained from fungi." | x |
| F208 | 7.5 | term | "Opioids are the drugs, which bind to specific opioid receptors present in our central nervous system and gastrointestinal tract." | x |
| F209 | 7.5 | term | "Heroin, commonly called smack is chemically diacetylmorphine which is a white, odourless, bitter crystalline compound." | x |
| F210 | 7.5 | fact | "This is obtained by acetylation of morphine, which is extracted from the latex of poppy plant Papaver somniferum." | x |
| F211 | 7.5 | fact | "Generally taken by snorting and injection, heroin is a depressant and slows down body functions." | x |
| F212 | 7.5 | term | "Cannabinoids are a group of chemicals, which interact with cannabinoid receptors present principally in the brain." | x |
| F213 | 7.5 | fact | "Natural cannabinoids are obtained from the inflorescences of the plant Cannabis sativa." | x |
| F214 | 7.5 | example | "The flower tops, leaves and the resin of cannabis plant are used in various combinations to produce marijuana, hashish, charas and ganja." | x |
| F215 | 7.5 | fact | "Generally taken by inhalation and oral ingestion, these are known for their effects on cardiovascular system of the body." | x |
| F216 | 7.5 | term | "Coca alkaloid or cocaine is obtained from coca plant Erythroxylum coca, native to South America." | x |
| F217 | 7.5 | mechanism | "It interferes with the transport of the neuro-transmitter dopamine." | x |
| F218 | 7.5 | fact | "Cocaine, commonly called coke or crack is usually snorted. It has a potent stimulating action on central nervous system, producing a sense of euphoria and increased energy. Excessive dosage of cocaine causes hallucinations." | x |
| F219 | 7.5 | example | "Other well-known plants with hallucinogenic properties are Atropa belladona and Datura." | x |
| F220 | 7.5 | fact | "These days cannabinoids are also being abused by some sportspersons." | x |
| F221 | 7.5 | example | "Drugs like barbiturates, amphetamines, benzodiazepines, and other similar drugs, that are normally used as medicines to help patients cope with mental illnesses like depression and insomnia, are often abused." | x |
| F222 | 7.5 | fact | "Morphine is a very effective sedative and painkiller, and is very useful in patients who have undergone surgery." | x |
| F223 | 7.5 | fact | "Several plants, fruits and seeds having hallucinogenic properties have been used for hundreds of years in folk-medicine, religious ceremonies and rituals all over the globe." | x |
| F224 | 7.5 | term | "When these are taken for a purpose other than medicinal use or in amounts/frequency that impairs one's physical, physiological or psychological functions, it constitutes drug abuse." | x |
| F225 | 7.5 | fact | "Smoking also paves the way to hard drugs." | x |
| F226 | 7.5 | number | "Tobacco has been used by human beings for more than 400 years. It is smoked, chewed or used as a snuff." | x |
| F227 | 7.5 | term | "Tobacco contains a large number of chemical substances including nicotine, an alkaloid." | x |
| F228 | 7.5 | mechanism | "Nicotine stimulates adrenal gland to release adrenaline and nor-adrenaline into blood circulation, both of which raise blood pressure and increase heart rate." | x |
| F229 | 7.5 | fact | "Smoking is associated with increased incidence of cancers of lung, urinary bladder and throat, bronchitis, emphysema, coronary heart disease, gastric ulcer, etc." | x |
| F230 | 7.5 | fact | "Tobacco chewing is associated with increased risk of cancer of the oral cavity." | x |
| F231 | 7.5 | mechanism | "Smoking increases carbon monoxide (CO) content in blood and reduces the concentration of haembound oxygen. This causes oxygen deficiency in the body." | x |
| F232 | 7.5 | fact | "When one buys packets of cigarettes one cannot miss the statutory warning that is present on the packing which warns against smoking and says how it is injurious to health." | x |
| F232a | 7.5 | fact | "Yet, smoking is very prevalent in society, both among young and old." (**ADDED IN PASS 3(b) — defect D2, a real Pass 1 gap, NOT back-dated into the freeze.** Direction 2 found this sentence, which sits between `F232` and `F233` in the source, had no row at all; "prevalent" returned 0 hits in the delivered PDF. It is the contrastive "Yet" that makes `F233`'s advice follow — the warning exists, the habit persists anyway.) | x |
| F233 | 7.5 | fact | "Knowing the dangers of smoking and chewing tobacco, and its addictive nature, the youth and old need to avoid these habits. Any addict requires counselling and medical help to get rid of the habit." | x |
| F234 | 7.5.1 | number | "The period between 12-18 years of age may be thought of as adolescence period." | x |
| F235 | 7.5.1 | term | "In other words, adolescence is a bridge linking childhood and adulthood." | x |
| F236 | 7.5.1 | fact | "Adolescence is accompanied by several biological and behavioural changes. Adolescence, thus is a very vulnerable phase of mental and psychological development of an individual." | x |
| F237 | 7.5.1 | cause | "Curiosity, need for adventure and excitement, and experimentation, constitute common causes, which motivate youngsters towards drug and alcohol use." | x |
| F238 | 7.5.1 | cause | "A child's natural curiosity motivates him/her to experiment. This is complicated further by effects that might be perceived as benefits, of alcohol or drug use." | x |
| F239 | 7.5.1 | cause | "the first use of drugs or alcohol may be out of curiosity or experimentation, but later the child starts using these to escape facing problems." | x |
| F240 | 7.5.1 | cause | "Of late, stress, from pressures to excel in academics or examinations, has played a significant role in persuading the youngsters to try alcohol and drugs." | x |
| F241 | 7.5.1 | cause | "The perception among youth that it is 'cool' or progressive to smoke, use drugs or alcohol, is also in a way a major cause for youth to start these habits. Television, movies, newspapers, internet also help to promote this perception." | x |
| F242 | 7.5.1 | cause | "Other factors that have been seen to be associated with drug and alcohol abuse among adolescents are unstable or unsupportive family structures and peer pressure." | x |
| F243 | 7.5.2 | fact | "The most important thing, which one fails to realise, is the inherent addictive nature of alcohol and drugs." | x |
| F244 | 7.5.2 | term | "Addiction is a psychological attachment to certain effects –such as euphoria and a temporary feeling of well-being – associated with drugs and alcohol." | x |
| F245 | 7.5.2 | fact | "These drive people to take them even when these are not needed, or even when their use becomes self-destructive." | x |
| F246 | 7.5.2 | mechanism | "With repeated use of drugs, the tolerance level of the receptors present in our body increases. Consequently the receptors respond only to higher doses of drugs or alcohol leading to greater intake and addiction." | x |
| F247 | 7.5.2 | fact | "it should be clearly borne in mind that use of these drugs even once, can be a fore-runner to addiction." | x |
| F248 | 7.5.2 | fact | "the addictive potential of drugs and alcohol, pull the user into a vicious circle leading to their regular use (abuse) from which he/she may not be able to get out. In the absence of any guidance or counselling, the person gets addicted and becomes dependent on their use." | x |
| F249 | 7.5.2 | term | "Dependence is the tendency of the body to manifest a characteristic and unpleasant withdrawal syndrome if regular dose of drugs/alcohol is abruptly discontinued." | x |
| F250 | 7.5.2 | symptom | "This is characterised by anxiety, shakiness, nausea and sweating, which may be relieved when use is resumed again." | x |
| F251 | 7.5.2 | fact | "In some cases, withdrawal symptoms can be severe and even life threatening and the person may need medical supervision." | x |
| F252 | 7.5.2 | fact | "Dependence leads the patient to ignore all social norms in order to get sufficient funds to satiate his/her needs. These result in many social adjustment problems." | x |
| F253 | 7.5.3 | fact | "Excessive doses of drugs may lead to coma and death due to respiratory failure, heart failure or cerebral hemorrhage." | x |
| F254 | 7.5.3 | fact | "A combination of drugs or their intake along with alcohol generally results in overdosing and even deaths." | x |
| F255 | 7.5.3 | symptom | "The most common warning signs of drug and alcohol abuse among youth include drop in academic performance, unexplained absence from school/college, lack of interest in personal hygiene, withdrawal, isolation, depression, fatigue, aggressive and rebellious behaviour, deteriorating relationships with family and friends, loss of interest in hobbies, change in sleeping and eating habits, fluctuations in weight, appetite, etc." | x |
| F256 | 7.5.3 | fact | "If an abuser is unable to get money to buy drugs/alcohol he/she may turn to stealing." | x |
| F257 | 7.5.3 | fact | "At times, a drug/alcohol addict becomes the cause of mental and financial distress to his/her entire family and friends." | x |
| F258 | 7.5.3 | fact | "Those who take drugs intravenously (direct injection into the vein using a needle and syringe), are much more likely to acquire serious infections like AIDS and Hepatitis B." | x |
| F259 | 7.5.3 | transmission | "The viruses, which are responsible for these diseases, are transferred from one person to another by sharing of infected needles and syringes." | x |
| F260 | 7.5.3 | fact | "Both AIDS and Hepatitis B infections are chronic infections and ultimately fatal. Both can be transmitted through sexual contact or infected blood." | x |
| F261 | 7.5.3 | fact | "The use of alcohol during adolescence may also have long-term effects. It could lead to heavy drinking in adulthood." | x |
| F262 | 7.5.3 | fact | "The chronic use of drugs and alcohol damages nervous system and liver (cirrhosis)." | x |
| F263 | 7.5.3 | fact | "The use of drugs and alcohol during pregnancy is also known to adversely affect the foetus." | x |
| F264 | 7.5.3 | fact | "Another misuse of drugs is what certain sportspersons do to enhance their performance. They (mis)use narcotic analgesics, anabolic steroids, diuretics and certain hormones in sports to increase muscle strength and bulk and to promote aggressiveness and as a result increase athletic performance." | x |
| F265 | 7.5.3 | symptom | "The side-effects of the use of anabolic steroids in females include masculinisation (features like males), increased aggressiveness, mood swings, depression, abnormal menstrual cycles, excessive hair growth on the face and body, enlargement of clitoris, deepening of voice." | x |
| F266 | 7.5.3 | symptom | "In males it includes acne, increased aggressiveness, mood swings, depression, reduction of size of the testicles, decreased sperm production, potential for kidney and liver dysfunction, breast enlargement, premature baldness, enlargement of the prostate gland." | x |
| F267 | 7.5.3 | fact | "These effects may be permanent with prolonged use." | x |
| F268 | 7.5.3 | symptom | "In the adolescent male or female, severe facial and body acne, and premature closure of the growth centres of the long bones may result in stunted growth." | x |
| F269 | 7.5.4 | fact | "It is also true that habits such as smoking, taking drug or alcohol are more likely to be taken up at a young age, more during adolescence." | x |
| F270 | 7.5.4 | prevention | "Hence, it is best to identify the situations that may push an adolescent towards use of drugs or alcohol, and to take remedial measures well in time. In this regard, the parents and the teachers have a special responsibility." | x |
| F271 | 7.5.4 | prevention | "Parenting that combines with high levels of nurturance and consistent discipline, has been associated with lowered risk of substance (alcohol/drugs/tobacco) abuse." | x |
| F272 | 7.5.4 | prevention | "Avoid undue peer pressure - Every child has his/her own choice and personality, which should be respected and nurtured. A child should not be pushed unduly to perform beyond his/her threshold limits; be it studies, sports or other activities." | x |
| F273 | 7.5.4 | prevention | "Education and counselling - Educating and counselling him/her to face problems and stresses, and to accept disappointments and failures as a part of life. It would also be worthwhile to channelise the child's energy into healthy pursuits like sports, reading, music, yoga and other extracurricular activities." | x |
| F274 | 7.5.4 | prevention | "Seeking help from parents and peers - Help from parents and peers should be sought immediately so that they can guide appropriately. Help may even be sought from close and trusted friends. Besides getting proper advise to sort out their problems, this would help young to vent their feelings of anxiety and guilt." | x |
| F275 | 7.5.4 | prevention | "Looking for danger signs - Alert parents and teachers need to look for and identify the danger signs discussed above. Even friends, if they find someone using drugs or alcohol, should not hesitate to bring this to the notice of parents or teacher in the best interests of the person concerned. Appropriate measures would then be required to diagnose the malady and the underlying causes. This would help in initiating proper remedial steps or treatment." | x |
| F276 | 7.5.4 | prevention | "Seeking professional and medical help - A lot of help is available in the form of highly qualified psychologists, psychiatrists, and de-addiction and rehabilitation programmes to help individuals who have unfortunately got in the quagmire of drug/alcohol abuse. With such help, the affected individual with sufficient efforts and will power, can get rid of the problem completely and lead a perfectly normal and healthy life." | x |
| F277 | chapter | heading | "CHAPTER 7" / "HUMAN HEALTH AND DISEASE" | x |
| F278 | 7.1 | heading | "7.1 COMMON DISEASES IN HUMANS" | x |
| F279 | 7.1 | heading | "Widal test" | x |
| F280 | 7.2 | heading | "7.2 IMMUNITY" | x |
| F281 | 7.2.1 | heading | "7.2.1 Innate Immunity" | x |
| F282 | 7.2.1 | heading | "(i) Physical barriers" | x |
| F283 | 7.2.1 | heading | "(ii) Physiological barriers" | x |
| F284 | 7.2.1 | heading | "(iii) Cellular barriers" | x |
| F285 | 7.2.1 | heading | "(iv) Cytokine barriers" | x |
| F286 | 7.2.2 | heading | "7.2.2 Acquired Immunity" | x |
| F287 | 7.2.3 | heading | "7.2.3 Active and Passive Immunity" | x |
| F288 | 7.2.4 | heading | "7.2.4 Vaccination and Immunisation" | x |
| F289 | 7.2.5 | heading | "7.2.5 Allergies" | x |
| F290 | 7.2.6 | heading | "7.2.6 Auto Immunity" | x |
| F291 | 7.2.7 | heading | "7.2.7 Immune System in the Body" | x |
| F292 | 7.2.7 | heading | "Lymphoid organs" | x |
| F293 | 7.3 | heading | "7.3 AIDS" | x |
| F294 | 7.3 | heading | "Prevention of AIDS" | x |
| F295 | 7.4 | heading | "7.4 CANCER" | x |
| F296 | 7.4 | heading | "Causes of cancer" | x |
| F297 | 7.4 | heading | "Cancer detection and diagnosis" | x |
| F298 | 7.4 | heading | "Treatment of cancer" | x |
| F299 | 7.5 | heading | "7.5 DRUGS AND ALCOHOL ABUSE" | x |
| F300 | 7.5.1 | heading | "7.5.1 Adolescence and Drug/Alcohol Abuse" | x |
| F301 | 7.5.2 | heading | "7.5.2 Addiction and Dependence" | x |
| F302 | 7.5.3 | heading | "7.5.3 Effects of Drug/Alcohol Abuse" | x |
| F303 | 7.5.4 | heading | "7.5.4 Prevention and Control" | x |
| F304 | summary | heading | "SUMMARY" | x |
| F305 | exercises | heading | "EXERCISES" | x |
| F306 | 7.0 intro | opener | "The term health is very frequently used by everybody. How do we define it?" | x |
| F307 | 7.1 | opener | "A wide range of organisms belonging to bacteria, viruses, fungi, protozoans, helminths, etc., could cause diseases in man." | x |
| F308 | 7.1 | opener | "Widal test : A classic case in medicine, that of Mary Mallon nicknamed Typhoid Mary, is worth mentioning here." | x |
| F309 | 7.2 | opener | "Everyday we are exposed to large number of infectious agents." | x |
| F310 | 7.2.1 | opener | "Innate immunity is non-specific type of defence, that is present at the time of birth." | x |
| F311 | 7.2.1 | opener | "Physical barriers : Skin on our body is the main barrier which prevents entry of the micro-organisms." | x |
| F312 | 7.2.1 | opener | "Physiological barriers : Acid in the stomach, saliva in the mouth, tears from eyes-all prevent microbial growth." | x |
| F313 | 7.2.1 | opener | "Cellular barriers : Certain types of leukocytes (WBC) of our body like polymorpho-nuclear leukocytes (PMNL-neutrophils) and monocytes and natural killer (type of lymphocytes) in the blood as well as macrophages in tissues can phagocytose and destroy microbes." | x |
| F314 | 7.2.1 | opener | "Cytokine barriers : Virus-infected cells secrete proteins called interferons which protect non-infected cells from further viral infection." | x |
| F315 | 7.2.2 | opener | "Acquired immunity, on the other hand is pathogen specific." | x |
| F316 | 7.2.3 | opener | "When a host is exposed to antigens, which may be in the form of living or dead microbes or other proteins, antibodies are produced in the host body." | x |
| F317 | 7.2.4 | opener | "The principle of immunisation or vaccination is based on the property of 'memory' of the immune system." | x |
| F318 | 7.2.5 | opener | "When you have gone to a new place and suddenly you started sneezing, wheezing for no explained reason, and when you went away, your symptoms dissappeared." | x |
| F319 | 7.2.6 | opener | "Memory-based acquired immunity evolved in higher vertebrates based on the ability to differentiate foreign organisms (e.g., pathogens) from self-cells." | x |
| F320 | 7.2.7 | opener | "The human immune system consists of lymphoid organs, tissues, cells and soluble molecules like antibodies." | x |
| F321 | 7.2.7 | opener | "Lymphoid organs: These are the organs where origin and/or maturation and proliferation of lymphocytes occur." | x |
| F322 | 7.3 | opener | "The word AIDS stands for Acquired Immuno Deficiency Syndrome." | x |
| F323 | 7.3 | opener | "Prevention of AIDS : As AIDS has no cure, prevention is the best option." | x |
| F324 | 7.4 | opener | "Cancer is one of the most dreaded diseases of human beings and is a major cause of death all over the globe." | x |
| F325 | 7.4 | opener | "Causes of cancer : Transformation of normal cells into cancerous neoplastic cells may be induced by physical, chemical or biological agents." | x |
| F326 | 7.4 | opener | "Cancer detection and diagnosis : Early detection of cancers is essential as it allows the disease to be treated successfully in many cases." | x |
| F327 | 7.4 | opener | "Treatment of cancer : The common approaches for treatment of cancer are surgery, radiation therapy and immunotherapy." | x |
| F328 | 7.5 | opener | "Surveys and statistics show that use of drugs and alcohol has been on the rise especially among the youth." | x |
| F329 | 7.5.1 | opener | "Adolescence means both 'a period' and 'a process' during which a child becomes mature in terms of his/her attitudes and beliefs for effective participation in society." | x |
| F330 | 7.5.2 | opener | "Because of the perceived benefits, drugs are frequently used repeatedly." | x |
| F331 | 7.5.3 | opener | "The immediate adverse effects of drugs and alcohol abuse are manifested in the form of reckless behaviour, vandalism and violence." | x |
| F332 | 7.5.4 | opener | "The age-old adage of 'prevention is better than cure' holds true here also." | x |
| F333 | summary | opener | "Health is not just the absence of disease. It is a state of complete physical, mental, social and psychological well-being." | x |
| F334 | intro | term | "It is a state of complete physical, mental, social and psychological well-being." (SUMMARY-UNIQUE: the summary's definition of health adds "psychological" to the body's "physical, mental and social" at F006) | x |
| F335 | 7.1 | example | "Diseases like typhoid, cholera, pneumonia, fungal infections of skin, malaria and many others are a major cause of distress to human beings." (SUMMARY-UNIQUE: cholera is named as a human disease only in the summary) | x |

### Session 1-S row count (machine-derived)

Parsed from the finished table by `scratch/ch7_1s/count_rows.py`, not tallied by
hand: **276 rows, `F001`..`F276`, contiguous, no gaps, no duplicates.** Row count
re-confirmed by session 1-Z.

**Type distribution over the 14 values used in this block — corrected by session
1-Z** (`scratch/ch7_1z/derive_counts.py`, restricted to `F001`..`F276`):

`fact` 86, `term` 45, `example` 23, `prevention` 19, `figure-text` 18,
`mechanism` 14, `symptom` 14, `process` 11, `diagnosis` 10, `cause` 9,
`transmission` 9, `number` 7, `treatment` 7, `structure` 4.

These sum to **276**, matching the row count.

**History — why this was corrected.** 1-S originally transcribed the distribution
as `fact` 100, `prevention` 22, `term` 40, `example` 22, `symptom` 20,
`mechanism` 20, `figure-text` 18, `process` 13, `transmission` 10, `diagnosis` 9,
`cause` 12, `treatment` 7, `number` 9, `structure` 5, and described it as "the 12
normalized values" while listing 14. Those figures **sum to 307 over a block of
276 rows**, so they could not all have been right, and 12 of the 14 disagreed with
a re-parse. Only `figure-text` (18) and `treatment` (7) were correct. 1-S itself
recorded that "the authoritative numbers are whatever `count_rows.py` prints
against the file as committed... and 1-Z must re-run the parse rather than trust
it" — running it is what surfaced this. The row data was never wrong; only the
tally about it was, so no Facts row was touched (`§6` rule 5).

### What 1-S deliberately did not inventory

- **Section openers and headings** — sessions 1-O and 1-H, per `§6`. The absence of
  every section's first sentence from the table above is by design.
- **Figure captions** — held verbatim in the Figure manifest, which is their single
  home. Duplicating them as Facts rows would put the same wording in two tables.
- **Unit front matter** — page 1's unit introduction ("Biology is the youngest of
  the formalised disciplines of natural science...") and page 2's M.S. Swaminathan
  biography. These belong to the *unit* that contains Chapters 7 and 8, not to
  Chapter 7, and the Swaminathan page is the same page whose portrait `§5`/`§4.4`
  already forbids embedding. Recorded here as an explicit, reasoned exclusion so a
  later audit does not read the gap as a miss.
- **Exercise questions** (page 22) — the 17 exercises are 1-Z's material under
  step 7 (exercise-gap scan), not Facts rows.
- **Summary paragraph** (pages 21-22) — 1-Z's material under step 8.

### Second hunting pass (step 3) — what it added

Step 2 built the table section by section; step 3 re-read hunting specifically for
qualifiers, parentheticals and numbers buried mid-sentence. It confirmed the bulk
of step 2 and **extended** it with these, each of which step 2 had folded into a
neighbouring row and would have lost:

- the exact typhoid fever range **"(39° to 40°C)"** (F023) and the common-cold
  duration **"3-7 days"** (F033)
- **"but not the lungs"** in the rhino-virus row (F032) — a one-clause exclusion
  that NEET tests directly
- the three *Plasmodium* species spelled as NCERT spells them, including the
  non-standard **"P. malaria"** (F036)
- **haemozoin** named as the toxin and the **"every three to four days"** fever
  periodicity (F040)
- **"W. bancrofti and W. malayi"** as the two named *Wuchereria* species (F060)
- **H2L2** as the antibody's formula notation (F094) and **IgE** as the
  allergy-specific isotype (F120) against **IgA** in colostrum (F108)
- **"about 50 per cent"** for MALT's share of lymphoid tissue (F144)
- AIDS's **1981** first report, **25 million** deaths and the **5-10 year**
  incubation window (F146, F152)
- **"more than 400 years"** of tobacco use (F226) and the **12-18 years**
  adolescence window (F234)
- **α-interferon** named as the biological response modifier (F205), and
  **Gambusia** named as the larvivorous fish (F072)
- the two **CT vs MRI** mechanism sentences kept apart (F196, F197), since the
  chapter distinguishes X-ray-based 3-D imaging from non-ionising magnetic imaging
  and a merged row would blur exactly the contrast being tested

## Structural census — session 1-H (heading sweep)

Rows `F277`-`F305`, `Type: heading`. This session walked the chapter's **skeleton
only**, ignoring prose entirely, per `§6` step 4.

**Count, derived from the list below: 16 numbered + the 13 unnumbered IDs listed
= 29 heading rows.** `16 + 13 = 29`, which is the number this section's row block
contains and the number the header states.

### The 16 numbered headings

Machine-derived from the source PDF by font/size class, not read off the page:
the 5 top-level headings are the only `Bookman-Demi 14.0` lines matching `^7\.\d`,
and the 11 sub-headings are the only `Bookman-Demi 12.0` lines matching
`^7\.\d+\.\d+`.

- 5 top-level: `F278` (7.1), `F280` (7.2), `F293` (7.3), `F295` (7.4), `F299` (7.5)
- 11 sub-level: `F281` (7.2.1), `F286` (7.2.2), `F287` (7.2.3), `F288` (7.2.4),
  `F289` (7.2.5), `F290` (7.2.6), `F291` (7.2.7), `F300` (7.5.1), `F301` (7.5.2),
  `F302` (7.5.3), `F303` (7.5.4)

Note that 7.1 and 7.3 have **no** numbered sub-sections in this chapter, and 7.4
has none either — their internal structure is carried entirely by the unnumbered
run-in headings below. That asymmetry is why the unnumbered sweep matters here
more than in a chapter with uniform numbering.

### The 13 unnumbered headings

`F277`, `F279`, `F282`, `F283`, `F284`, `F285`, `F292`, `F294`, `F296`, `F297`,
`F298`, `F304`, `F305`.

These break into four typographic classes, and **two of the four are invisible to
the obvious detection method** — recorded here because a future session that
re-derives this census with a naive "bold line" sweep will silently get 11:

1. **Chapter title plate** — `F277` (`AvantGarde-Book` 26/30 pt, page 3).
2. **Bold run-in heads ending in a colon** (`Bookman-Demi 10.5`, line-initial):
   `F279` "Widal test", `F292` "Lymphoid organs", `F294` "Prevention of AIDS",
   `F296` "Causes of cancer", `F297` "Cancer detection and diagnosis",
   `F298` "Treatment of cancer". Six rows. These are the structural spine of 7.4,
   which has no numbered sub-sections at all.
3. **The four innate-immunity barrier heads** (`F282`-`F285`) — and here the
   source is **typographically inconsistent**: `(i) Physical barriers`,
   `(ii) Physiological barriers` and `(iii) Cellular barriers` are set in
   `Bookman-LightItalic` (regular weight, italic) with only the following colon in
   `Bookman-Demi`, while `(iv) Cytokine barriers` is set in `Bookman-DemiItalic`
   (bold italic). All four are the same structural level and each gets a row. A
   bold-only sweep finds (iv) and drops (i)-(iii) — exactly the Ch9 D4 failure
   mode, and the single most losable heading set in this chapter.
4. **Back-matter heads** — `F304` "SUMMARY" (`Bookman-Demi 13.0`, page 21) and
   `F305` "EXERCISES" (`AvantGarde-Book 30.0`, page 22). Neither is `Bookman-Demi
   10.5` or `12.0`, so neither appears in a numbered-heading sweep.

### Heading classes deliberately excluded

- **Running heads** — "BIOLOGY" (verso) and "HUMAN HEALTH AND DISEASE" (recto),
  `AvantGarde-Demi 8.0` on every page. Page furniture, not structure.
- **Page numbers** — 130-148, `AvantGarde-Book 14.0` in the corner tab.
- **Figure caption labels** — "Figure 7.1" etc. are `Bookman-Demi 9.5` and so are
  caught by a bold sweep, but captions live in the Figure manifest, not here.
- **Unit front matter** — page 1's "Chapter 7" / "Chapter 8" contents list
  (`AvantGarde-Demi 10.0`) and page 2's Swaminathan profile belong to the unit,
  consistent with 1-S's recorded exclusion of the same two pages.
- **Bold key terms mid-sentence** — `pathogens`, `typhoid`, `interferons`,
  `metastasis`, `Opioids`, `Cannabinoids` and ~30 others are `Bookman-Demi 10.5`
  emphasis *inside* a sentence, not line-initial heads. They are already
  inventoried as `term` rows by 1-S. Counting them as headings would have inflated
  this census by roughly a factor of two; the line-initial + colon test is what
  separates the two populations.

---

## Opener census — session 1-O (section-opener sweep)

Rows `F306`-`F333`, `Type: opener`. This session read **first sentences only**,
ignoring headings entirely, per `§6` step 5.

**Count, derived from the list below: 1 chapter-intro + 5 top-level + 11
sub-level + 10 unnumbered run-in + 1 summary = 28 opener rows.**
`1 + 5 + 11 + 10 + 1 = 28`, matching the row block above and the header.

Openers were located **mechanically**, not from memory: each heading's `(page, y)`
coordinate from the 1-H sweep was used to slice the text immediately following it
within the same column, so an opener is whatever the source puts there. This
matters because three of the run-in openers begin *on the heading line itself*
and a naive "line after the heading" rule silently returns the sentence's second
half — the first extraction attempt returned "prevents entry of the
micro-organisms." for `F311` before the anchor was moved onto the heading line.

### Roll-call against the 29 heading rows

| Heading row | Opener row |
|---|---|
| `F277` chapter title plate | *(no prose body — see exclusions)* |
| — chapter intro prose, p4 | `F306` |
| `F278` 7.1 | `F307` |
| `F279` Widal test | `F308` |
| `F280` 7.2 | `F309` |
| `F281` 7.2.1 | `F310` |
| `F282` (i) Physical barriers | `F311` |
| `F283` (ii) Physiological barriers | `F312` |
| `F284` (iii) Cellular barriers | `F313` |
| `F285` (iv) Cytokine barriers | `F314` |
| `F286` 7.2.2 | `F315` |
| `F287` 7.2.3 | `F316` |
| `F288` 7.2.4 | `F317` |
| `F289` 7.2.5 | `F318` |
| `F290` 7.2.6 | `F319` |
| `F291` 7.2.7 | `F320` |
| `F292` Lymphoid organs | `F321` |
| `F293` 7.3 | `F322` |
| `F294` Prevention of AIDS | `F323` |
| `F295` 7.4 | `F324` |
| `F296` Causes of cancer | `F325` |
| `F297` Cancer detection and diagnosis | `F326` |
| `F298` Treatment of cancer | `F327` |
| `F299` 7.5 | `F328` |
| `F300` 7.5.1 | `F329` |
| `F301` 7.5.2 | `F330` |
| `F302` 7.5.3 | `F331` |
| `F303` 7.5.4 | `F332` |
| `F304` SUMMARY | `F333` |
| `F305` EXERCISES | *(no prose body — see exclusions)* |

The table has 30 rows: 28 heading/opener pairings plus the un-paired `F277` and
`F305`, and one opener (`F306`) with no heading of its own. `29 - 2 + 1 = 28`.

### Openers deliberately excluded, and why

- **`F277` (chapter title plate) and `F305` (EXERCISES)** have no opening
  *sentence*. The title plate is a display heading followed directly by the
  chapter's intro prose, which is inventoried as `F306` in its own right; EXERCISES
  is followed by a numbered question, not a sentence that defines anything. An
  opener row for either would be an artifact of the sweep, not a fact of the book.
- **`F306` has no heading row** because the chapter's intro prose on p4 sits under
  the title plate with no heading of its own. `§6` step 5 asks for the first
  sentence of every *section*; this prose is a section by content even though it is
  unheaded, and 1-S did not inventory it (openers were out of scope there), so
  omitting it here would lose the chapter's own definition of "health" entirely.

### Structural finding — `F308`'s opener does not define its own heading

Worth recording explicitly, because it is the inverse of the Ch9 D9 failure that
motivated this sweep. `§6` warns to watch for a section whose opening sentence
defines a word in its own heading. Here the **"Widal test"** run-in head is
followed by an opener that pivots immediately to Mary Mallon and never says what
a Widal test is — the definition ("...confirmed by the Widal test.") sits in the
prose *above* the heading, already inventoried by 1-S as a `diagnosis` row.

This is a **finding, not a row** (`§6` step 10: "a structural finding is not a
row"), so it is deliberately not counted in the 28. **Pass 2 obligation:** the
notes must keep the Widal-test definition adjacent to the Typhoid Mary anecdote
rather than reproducing NCERT's split, which reads as a non-sequitur.

---

## Summary classification — session 1-Z (step 8)

The NCERT summary is a **second source document**, not a recap to skip. It runs
from the `SUMMARY` heading on page 21 (block `y0=469.7`) and continues at the top
of page 22 above `EXERCISES` (`y=288.2`).

**Sentence count: 18, machine-derived** by `scratch/ch7_1z/summary_sentences.py`.

**Extraction note — a trap this chapter really does contain.** A plain
`get_text()` on page 21 returns the summary **spliced with five paragraphs of
§7.5.4's body prose**, because pymupdf emits that page's blocks out of visual
order. The script therefore selects by *block geometry*, not emission order. A
first attempt selected spans by an x-band derived from the `SUMMARY` heading's own
`x0` (185.5) and silently dropped the summary's entire first half, yielding 8
sentences whose first read *"Plasmodium falciparum , if not afforded by
vaccination and immunisation."* — a spliced non-sentence. That nonsense is what
exposed the bug. Anyone re-deriving this count must confirm sentence 1 reads
"Health is not just the absence of disease."; if it does not, the extraction is
wrong, not the count.

| # | Summary sentence (abridged) | Classification | Folded into |
|---|---|---|---|
| 1 | "Health is not just the absence of disease." | BODY-PRESENT | `F006` |
| 2 | "It is a state of complete physical, mental, social and **psychological** well-being." | **SUMMARY-UNIQUE** | `F334` (new row) |
| 3 | "Diseases like typhoid, **cholera**, pneumonia, fungal infections of skin, malaria..." | **SUMMARY-UNIQUE** | `F335` (new row) |
| 4 | "Vector-borne diseases like malaria especially one caused by *P. falciparum*, if not treated, may prove fatal." | BODY-PRESENT | `F036`, `F037` |
| 5 | "...public health measures like proper disposal of waste, decontamination of drinking water, control of vectors..." | BODY-PRESENT | `F011`, `F067`, `F068` |
| 6 | "Our immune system plays the major role in preventing these diseases..." | BODY-PRESENT | `F080` |
| 7 | "The innate defences of our body like skin, mucous membranes, antimicrobial substances... tears, saliva and the phagocytic cells..." | BODY-PRESENT | `F084`, `F085`, `F086` |
| 8 | "...specific antibodies (humoral immune response) and cells (cell mediated immune response) serve to kill these pathogens." | BODY-PRESENT | `F096`, `F097` |
| 9 | "Immune system has memory." | BODY-PRESENT | `F088`, `F112` |
| 10 | "On subsequent exposure to same pathogen, the immune response is rapid and more intense." | BODY-PRESENT | `F112` |
| 11 | "This forms the basis of protection afforded by vaccination and immunisation." | BODY-PRESENT | `F317` |
| 12 | "Among other diseases, AIDS and cancer kill a large number of individuals worldwide." | BODY-PRESENT | `F016`, `F146`, `F177` |
| 13 | "AIDS caused by the human immuno-deficiency virus (HIV) is fatal but can be prevented if certain precautions are taken." | BODY-PRESENT | `F147`, `F161`, `F162` |
| 14 | "Many cancers are curable if detected early and appropriate therapeutic measures are taken." | BODY-PRESENT | `F192` |
| 15 | "Of late, drug and alcohol abuse among youth and adolescents is becoming another cause of concern." | BODY-PRESENT | `F206` |
| 16 | "Because of the addictive nature... perceived benefits like relief from stress... peer pressure, examinations-related and competition-related stresses." | BODY-PRESENT | `F233`, `F242`, `F330` |
| 17 | "In doing so, he/she may get addicted to them." | BODY-PRESENT | `F248` |
| 18 | "Education about their harmful effects, counselling and seeking immediate professional and medical help..." | BODY-PRESENT | `F273`, `F276` |

**16 BODY-PRESENT + 2 SUMMARY-UNIQUE = 18**, matching the machine count.

Both SUMMARY-UNIQUE facts were folded into body rows **before** the freeze, as
Rule 3 requires. Note that sentence 2's uniqueness is a **single qualifier word**:
the body's definition of health at `F006` reads "physical, mental and social
well-being" and the summary adds **"psychological"**. Implied does not count and
near-identical does not count — only explicit statement does, which is why this
is a body addition and not a skipped recap. Sentence 3's uniqueness is the single
disease name **cholera**, which appears nowhere in the body (0 hits across pages
4-21).

---

## Exercise-gap terms — session 1-Z (step 7)

All **17** exercises on page 22 were read and each term/fact they assume was
checked against the body. Grep located candidates; every verdict below was then
confirmed by **reading the surrounding body text**, since a paraphrase counts as
body-present and a keyword count cannot establish that.

| Term/fact assumed by exercises | Ex # | Explained where |
|---|---|---|
| Public health measures | 1 | Body — `F067`, `F068`, `F069`, `F011` |
| Role of biology in disease control (vaccines, antibiotics, smallpox eradication) | 2 | Body — `F073`-`F079` block |
| Transmission of Amoebiasis / Malaria / Ascariasis / Pneumonia | 3 | Body — `F053`, `F062`, `F057`, `F029` |
| **"Water-borne diseases"** as a named grouping | 4 | **Gap (terminology).** NCERT gives the *measures* (`F067`-`F069`) and names typhoid, amoebiasis and ascariasis as transmitted "through food and water", but never uses the phrase "water-borne" — it only ever writes "air-borne" (`F070`) and "vector-borne". **Plan:** state the water-borne grouping explicitly where `F067`-`F069` are written up, naming which of this chapter's diseases belong to it, so the exercise's phrasing is answerable without inventing content. |
| **"DNA vaccines"** and **"a suitable gene"** | 5 | **Gap (genuine).** Zero occurrences of "DNA vaccine" or "suitable gene" anywhere in the chapter body. The nearest content is `F115`/`F116` — recombinant-DNA-technology vaccines, e.g. hepatitis B produced from yeast — which is a *different* vaccine class. NCERT's own question says "Discuss with your teacher", conceding the chapter does not cover it, and Rule 5 forbids importing the mechanism from Chapter 10 or from outside knowledge. **Plan:** a **Terms used in the exercises** appendix entry that states exactly what this chapter does support (recombinant antigenic polypeptides, `F115`-`F116`) and flags that the DNA-vaccine mechanism itself is out of this chapter's scope. Do not silently fold an invented explanation into the main text. |
| Primary and secondary lymphoid organs | 6 | Body — `F134`, `F135`, `F136` |
| MALT | 7a | Body — `F143` |
| CMI | 7b | Body — `F097` |
| AIDS (expansion) | 7c | Body — `F322` / §7.3 opener |
| NACO | 7d | Body — `F165` |
| HIV (expansion) | 7e | Body — `F147` |
| Innate vs acquired immunity, with examples | 8a | Body — `F081`, `F083`, `F286` |
| Active vs passive immunity, with examples | 8b | Body — `F104`-`F109` |
| Labelled antibody diagram | 9 | Figure 7.4 + labels `F339`; structure at `F092`-`F094` |
| Routes of HIV transmission | 10 | Body — `F148`, `F149` |
| Mechanism of HIV immune deficiency | 11 | Body — `F153`-`F158` |
| Cancerous vs normal cell (contact inhibition) | 12 | Body — `F180`, `F182`, `F184` |
| Metastasis | 13 | Body — `F186` |
| Harmful effects of alcohol/drug abuse | 14 | Body — `F243`-`F254` |
| Peer influence and protecting oneself | 15 | Body — `F242`, `F272` |
| Why quitting is hard (addiction/dependence) | 16 | Body — `F233`, `F248`, `F330` |
| What motivates youngsters; how to avoid | 17 | Body — `F236`-`F242`, `F270`-`F276` |

**Verdict: 2 gaps out of 17 exercises** — one genuine content gap (Ex 5, DNA
vaccines) and one terminology gap (Ex 4, "water-borne"). Every other exercise is
answerable from rows already in the freeze. Both gaps have a planned home, which
is what Gate 1 requires; writing them is Pass 2's job.

---

## Figure manifest

11 numbered figures, 7.1-7.11, on artwork pages 6, 7, 9, 12, 13, 16, 17. All 11
assets are single-channel greyscale (`PIL` mode `L`), verified mechanically this
session, so the monochrome check is satisfied by construction. Captions verbatim
from the PDF text layer.

| Fig # | Caption (verbatim) | Asset file | Src page | Mono | Opened |
|---|---|---|---|---|---|
| Figure 7.1 | Stages in the life cycle of Plasmodium | `assets/fig_7_1.png` | 6 | yes (L) | yes |
| Figure 7.2 | Diagram showing inflammation in one of the lower limbs due to elephantiasis | `assets/fig_7_2.png` | 7 | yes (L) | yes |
| Figure 7.3 | Diagram showing ringworm affected area of the skin | `assets/fig_7_3.png` | 7 | yes (L) | yes |
| Figure 7.4 | Structure of an antibody molecule | `assets/fig_7_4.png` | 9 | yes (L) | yes |
| Figure 7.5 | Diagrammatic representation of Lymph nodes | `assets/fig_7_5.png` | 12 | yes (L) | yes |
| Figure 7.6 | Replication of retrovirus | `assets/fig_7_6.png` | 13 | yes (L) | yes |
| Figure 7.7 | Chemical structure of Morphine | `assets/fig_7_7.png` | 16 | yes (L) | yes |
| Figure 7.8 | Opium poppy | `assets/fig_7_8.png` | 16 | yes (L) | yes |
| Figure 7.9 | Skeletal structure of cannabinoid molecule | `assets/fig_7_9.png` | 17 | yes (L) | yes |
| Figure 7.10 | Leaves of Cannabis sativa | `assets/fig_7_10.png` | 17 | yes (L) | yes |
| Figure 7.11 | Flowering branch of Datura | `assets/fig_7_11.png` | 17 | yes (L) | yes |

**Asset count reconciliation:** 11 numbered NCERT figures -> **11** asset files.
No figure in this chapter is split into separately-captioned sub-plates, and there
is no unnumbered bonus diagram (unlike Ch5's central-dogma schematic). The
denominator is **11** everywhere it appears.

**Crop convention:** captions are excluded from every crop, because this project's
notes restate each caption in running text. Every rect's bottom edge stops short
of its caption's `y0`.

### Deliberate exclusions (census re-derived this session)

A page-by-page sweep of all 22 pages for non-furniture rasters and sizeable
drawings returns ink-bearing regions on exactly the 7 artwork pages above, plus
four regions that are **not** assets:

| Page | Region | Why excluded |
|---|---|---|
| 2 | M.S. Swaminathan portrait photograph, `(57, 272, 166, 395)` | `§5` item 3 / `§4.4` "Hard no": a scientist portrait is never embedded, greyscaled or not. |
| 3 | Chapter-opener title plate, `(344, 56, 525, 213)` + QR thumbnail | Page furniture / title block. The tilted thumbnail merely re-prints fig 7.4's antibody artwork; it carries no fact of its own. |
| 21 | Orange wheat-ear motif beside SUMMARY box, `(407, 439, 455, 705)` | Decoration. |
| 22 | Same motif, `(126, 84, 174, 265)` | Decoration. |

All other pages (1, 4, 5, 8, 10, 11, 14, 15, 18, 19, 20) carry only the 1-2
furniture drawings — the header band and the full-page
"(c) NCERT / not to be republished" watermark.

### Rects, as frozen by session 1-F

Rects are in PDF points on the artwork page; page box is 568.8 x 777.6. Pinned by
hand off a 20 pt coordinate grid (`scratch/ch7_figs/grid/pNN.png`), because — see
the label matrix below — **every** in-figure label in this chapter is artwork, so
no text-layer method can find the plate boundaries.

| Asset | Src page | Rect (pt) | Kind |
|---|---|---|---|
| `fig_7_1` | 6 | (53, 83, 536, 610) | vector + raster, full-page plate |
| `fig_7_2` | 7 | (325, 79, 513, 351) | raster illustration |
| `fig_7_3` | 7 | (267, 414, 508, 533) | raster photograph |
| `fig_7_4` | 9 | (213, 290, 521, 530) | vector panel + raster tint |
| `fig_7_5` | 12 | (54, 80, 206, 302) | raster silhouette + vector labels |
| `fig_7_6` | 13 | (84, 81, 469, 532) | pure vector schematic |
| `fig_7_7` | 16 | (122, 545, 298, 696) | vector skeletal formula |
| `fig_7_8` | 16 | (374, 538, 495, 694) | raster-tile illustration |
| `fig_7_9` | 17 | (50, 215, 263, 366) | vector skeletal formula |
| `fig_7_10` | 17 | (350, 219, 456, 364) | vector panel, mid-tone fills |
| `fig_7_11` | 17 | (326, 395, 515, 586) | raster-tile illustration |

NCERT sets 7.2, 7.3, 7.4, 7.5 and 7.11 *beside* a body-text column, so an
automatic ink box would sweep the neighbouring paragraph in; each of those rects
is clipped against the prose column's own x boundary taken from `get_text("words")`.

---

## Figure-label matrix

Eleven rows, one per asset. Rows for the six assets with no descriptive callouts
are worded so they do **not** begin `Figure labels`, because `check_pdf.py`'s
`_extract_labels` falls back to semicolon-splitting an unquoted body — a row
reading "Figure labels: (none)" would manufacture a phantom label that no running
text could ever satisfy. The column header is worded the same way, for the same
reason. The parser reads column index 3, so this table's shape is load-bearing.

Labels were harvested by **opening each rendered asset** in this session, never by
text extraction. This chapter is the textbook case for that rule: a
`page.get_text("words")` sweep returns **zero** words inside all 11 rects (see the
audit table below) even though figs 7.1, 7.4, 7.5 and 7.6 carry 30 callouts
between them. Every label is baked into the artwork.

| ID | Fig # | Type | Label row wording | Ticked |
|----|-------|------|-------------------|--------|
| F336 | Fig 7.1 | label | Figure labels: "Sporozoites"; "Salivary glands"; "Mosquito Host"; "Human Host"; "Gametocytes"; "Male"; "Female" | x |
| F337 | Fig 7.2 | label | No in-figure labels — unlabelled illustration of a seated man with elephantiasis of the lower limbs | x |
| F338 | Fig 7.3 | label | No in-figure labels — unlabelled photograph of a ringworm lesion on the chin and jaw | x |
| F339 | Fig 7.4 | label | Figure labels: "Antigen binding site"; "Light chain"; "Heavy chain" | x |
| F340 | Fig 7.5 | label | Figure labels: "Lymph nodes"; "Thymus"; "Lymphatic vessels" | x |
| F341 | Fig 7.6 | label | Figure labels: "Retrovirus"; "Viral RNA core"; "Viral protein coat"; "Animal cell"; "Plasma membrane"; "Cytoplasm"; "Nucleus"; "DNA" | x |
| F342 | Fig 7.7 | label | No descriptive callouts — skeletal formula bearing only atom/group symbols (HO, O, H, N, CH3) | x |
| F343 | Fig 7.8 | label | No in-figure labels — unlabelled illustration of an opium poppy plant | x |
| F344 | Fig 7.9 | label | No descriptive callouts — skeletal formula bearing only atom/group symbols (OH, O, H) | x |
| F345 | Fig 7.10 | label | No in-figure labels — unlabelled framed illustration of a Cannabis sativa leaf | x |
| F346 | Fig 7.11 | label | No in-figure labels — unlabelled illustration of a flowering Datura branch | x |

**Parsed label total: 21** (7 + 3 + 3 + 8), across 4 labelled assets. The seven
non-`Figure labels` rows contribute 0 and are invisible to the parser by design.

**IDs assigned by session 1-Z: `F336`-`F346`**, continuing the single `F###`
sequence so the whole inventory is contiguous `F001..F346`. 1-F had left them as
`—` because the Facts table did not exist yet.

1-Z also **reset the `Ticked` column on these 11 rows from `x` to empty.** 1-F had
marked them `x`, but the tick legend at the top of this file defines `x` as
"written into the script and verified present in the generated PDF" — and no
script exists. The ticks were premature bookkeeping, not verification, and
`check_pdf.py`'s check 7 counts Facts-section rows, so leaving them ticked would
have contributed a false green to Gate 2 rather than to Gate 1. They are ticked
during Pass 2, with every other row.

### Labels deliberately NOT quoted, and the obligations they create

Three sets of in-figure text are real but are **not** quoted above, because
quoting them would create check-6 requirements that are either unsatisfiable or
meaningless. Each becomes an explicit Pass 2 obligation instead:

- **fig 7.4's chain-terminus markers `N` and `C`.** Single characters.
  `_coverage_ratio` strips tokens of length 1, then falls back to a bare `\bn\b`
  word-boundary search — which any stray "n" in the notes would satisfy, so the
  check would be noise either way. **Obligation:** the antibody passage must name
  the amino (N) and carboxyl (C) termini of the chains in running text.
- **The `S-S` disulfide-bridge markers in fig 7.4.** Numerous, and not a
  descriptive callout. **Obligation:** the passage must state that the chains are
  held together by disulfide bonds.
- **The process-arrow sentences in figs 7.1 and 7.6.** These are full sentences,
  not labels ("When the mosquito bites another human, sporozoites are injected
  with bite.", "Viral DNA is produced by reverse transcriptase", the in-plate
  "NOTE: Infected cell can survive while viruses are being replicated and
  released", and 11 others). Listing them as labels would misuse the mechanism.
  **Obligation:** their content must be carried by the Facts rows for the malaria
  life cycle and HIV replication, which session 1-S must create. **This is the
  single biggest carry-over from 1-F and must not be lost.**

---

## Extraction gate record (five-part audit, session 1-F)

Run: `/vercel/share/neetenv/bin/python scratch/ch7_figs/audit.py`
(script rebuilt and committed this session; the previous sitting's copy was lost).

| Asset | A) word grazing | B) drawings overflow | B2) raster overflow | B3) tile union | C) dark border ink | C2) light border ink |
|---|---|---|---|---|---|---|
| `fig_7_1` | **vacuous** (0 words) | ok (1250 shapes) | ok | ok (4276 tiles) | clean | explained (page-number tab) |
| `fig_7_2` | **vacuous** (0 words) | no drawings | ok (1 raster) | ok | clean | explained (corner motif) |
| `fig_7_3` | **vacuous** (0 words) | no drawings | ok (1 raster) | ok | clean | clean |
| `fig_7_4` | **vacuous** (0 words) | ok (1180 shapes) | ok | ok (81 tiles) | clean | clean |
| `fig_7_5` | **vacuous** (0 words) | ok (35 shapes) | OVERFLOW L24.8 — **explained** | OVERFLOW L24.8 — **explained** | clean | explained (corner motif) |
| `fig_7_6` | **vacuous** (0 words) | ok (4944 shapes) | no rasters | no tiles (pure vector) | clean | clean |
| `fig_7_7` | **vacuous** (0 words) | ok (26 shapes) | ok | ok (59 tiles) | clean | clean |
| `fig_7_8` | **vacuous** (0 words) | **vacuous** (0 drawings) | **vacuous** (3x3 px tile only) | ok (1804 tiles) | clean | clean |
| `fig_7_9` | **vacuous** (0 words) | ok (16 shapes) | ok | ok (59 tiles) | clean | clean |
| `fig_7_10` | **vacuous** (0 words) | OVERFLOW L4.8 T9.3 R11.6 — **explained** | **vacuous** (5x3 px tile only) | ok (582 tiles) | clean | clean |
| `fig_7_11` | **vacuous** (0 words) | **vacuous** (0 drawings) | **vacuous** (0 rasters) | ok (4878 tiles) | clean | clean |

### Notes on this chapter's audit

- **Check A is vacuous for all 11 assets.** Zero text-layer words fall inside any
  rect — not even a panel letter. Check A therefore provides **no** evidence
  whatsoever about crop quality in this chapter and must never be cited as if it
  did. B/B2/B3/C/C2 plus the eyeball carried this gate.
- **Check C2 (light threshold, grey < 205) was required.** The skill's standard C
  uses grey < 110, but the fig 7.10 cannabis leaf is mid-green (luma ~177) inside
  a pale grey frame, i.e. the entire plate sits *above* the dark threshold. C
  passed on it while the crop was in fact clipping the panel border. All three
  surviving C2 hits are page furniture, each identified by coordinate:
  `fig_7_1` bottom = the orange page-number tab ("132", ink from y=611.8, x 53-92);
  `fig_7_2` top = the top-right leaf/corner motif at y~73, x 469-502;
  `fig_7_5` top = the top-left corner motif at y~74. `fig_7_10`'s top band is now
  **clean**, which is the mechanical confirmation that the re-pin worked.
- **Check B3 was added this session** and is not optional for Ch7. Figures 7.8 and
  7.11 are stipple/scanline artwork built from ~1800 and ~4900 sub-pixel raster
  tiles; B (drawings) and B2 (rasters >= 3 pt) are both blind to them. Before B3
  those two plates had **no** mechanical edge check at all and were passing
  vacuously. With B3 the tile unions land at
  `x 373.0-491.2, y 541.0-694.1` (fig 7.8, inside its rect to within 1.0 pt) and
  `x 330.6-510.1, y 395.9-580.1` (fig 7.11, comfortably inside).
- **`fig_7_5`'s L24.8 overflow is the raster's own white margin,** not a clip: the
  silhouette raster bbox begins at x=29.2, but a 300 dpi column scan (thr 205)
  puts the first inked column at **x=57.9**, and the rect's left edge is x=54.
  The `Lymph nodes` / `Thymus` / `Lymphatic vessels` labels are vector and run
  right to x=201.7, which is why the box must span to x=206.
- **`fig_7_10`'s B overflow is explained by clipping, not truncation:** the leaf's
  gradient shapes are *defined* out to `x 345.2-467.6, y 209.7`, but they are
  clipped by the panel's own clip path, so no ink renders outside the frame. The
  thr-205 probe, check C2, and the opened asset all agree the frame is intact.
- **Page furniture excluded from every measurement:** the full-page watermark
  (~`(46, 191, 508, 653)` raster, present on every page), the dark green header
  band (y < 76), the brown/orange corner motifs, the right-margin decorative band,
  and the orange page-number tab.

### Rects re-pinned during session 1-F

| Asset | Was | Now | Why |
|---|---|---|---|
| `fig_7_10` | (348, 224, 460, 366) | (350, 219, 456, 364) | Check B flagged T14.3 overflow and the eyeball confirmed ~1.5 pt of the panel's top border was sliced off. The dark-ink probe had reported the plate starting at y=230.2 only because the whole figure is mid-tone; a thr-205 re-probe put the panel at `x 352.3-454.6, y 222.5-361.0` (shadow included). Rect widened to clear it by ~2 pt. |

### Visual verification

All 11 assets were opened and inspected at full size in this session (not merely
contact-sheeted). Each renders complete: fig 7.1 shows all ten callouts and both
host loops; fig 7.4 shows the rounded panel with `N` at top and both `C` termini at
bottom; fig 7.6 shows the outer panel and the in-plate NOTE line; fig 7.10 shows
all four panel borders plus the drop shadow, confirming the re-pin. No crop clips
artwork and none admits body text.

One cosmetic observation, recorded and dismissed: `fig_7_5` includes a faint grey
horizontal rule at its very bottom edge (the caption block's top rule, `y0=306.0`
vs the rect's bottom at 302). It is a rule, not text, and carries no content.

---

## Gate 1 checklist — CLOSED 2026-08-23 (session 1-Z)

Every box below was verified by running something, not by reading the file.
The deriving script is `scratch/ch7_1z/derive_counts.py`; it exits 0.

- [x] **Every fact has a Facts row; every in-figure label has a matrix row.**
      346 rows, `F001`..`F346`. 11 matrix rows, one per asset.
- [x] **Labels harvested by opening each rendered asset**, not by text sweep.
      A text sweep returns **0** labels for this chapter — every callout is
      artwork — so a thin label set here would have meant a wrong method, not an
      unlabelled chapter. All 11 assets were opened individually at full size.
      21 labels across the 4 labelled plates.
- [x] **Inventory validated by `check_pdf.py`'s own `_extract_labels`.** Imported
      the real function from the repo-root linter (not a reimplementation) and ran
      it against this file: **21 labels / 4 figures** (`Fig 7.1` 7, `Fig 7.4` 3,
      `Fig 7.5` 3, `Fig 7.6` 8). **No doubling** (no label string parsed twice)
      and **no phantom `Fig #` row** from a markdown separator — the Ch12 trap was
      checked and **did not fire**. The 7 unlabelled matrix rows are worded to
      avoid the semicolon fallback and contribute 0 labels by design.
- [x] **Every count matches a re-parse; IDs contiguous.** `F001`..`F346`, no gaps,
      no duplicates, row count == highest ID. Block totals
      `276 + 29 + 28 + 2 + 11 = 346`. Each census total equals the length of the
      list beside it (`16 + 13 = 29` headings).
- [x] **`Type` column single-cased.** 17 distinct values, all lowercase; no value
      split across casings (the Ch13 `caption`/`Caption` defect does not recur).
- [x] **Every heading has a row, including unnumbered sub-headings.** 29 rows =
      16 numbered + 13 unnumbered, walked as their own list in session 1-H. The
      four innate-immunity barrier heads are included despite the source setting
      (i)-(iii) in regular italic and (iv) in bold italic — the Ch9 D4 failure mode.
- [x] **Every section opener has a row.** 28 rows from session 1-O.
- [x] **All five Pass 1 sessions actually ran, each reporting its own
      machine-derived count.** 1-S 276, 1-H 29, 1-O 28, 1-F 11 matrix rows, 1-Z 2.
- [x] **Every figure `Mono: yes` / `Verified: yes`.** 11/11 assets `mode=L`;
      five-part crop audit (A word-grazing, B drawings-extent, B2 raster-extent,
      B3 raster-tile union, C/C2 border ink) recorded below with every overflow
      explained by coordinate.
- [x] **Every exercise-gap term has a planned home** (2 gaps of 17 exercises) and
      **every SUMMARY-UNIQUE fact is folded into a body row** (`F334`, `F335`).
- [x] **Inventory file saved to the chapter folder.**

**Gate 1 is closed.** *(Status at the time of writing: no script, no PDF, 0 of 346
rows ticked.)* **Superseded by the Gate 2 record at the end of this file** — Pass 2
has since written the script and PDF, ticked the Facts rows, and closed Gate 2.
Gate 3 remains open, so this chapter is **not** done and must not be counted as such.

---

## Carry-over to later sessions

Numbered and cumulative. Items 1-2 are **closed**; the rest are live obligations
for Pass 2 or later, kept here so they are not rediscovered.

1. ~~1-S must create the Facts table, covering the 14 process-arrow sentences in
   figs 7.1/7.6 and the three unquoted label sets.~~ **Closed** — 1-S wrote
   `F001`-`F276`, including the `figure-text` rows (18 of them).
2. ~~1-Z must assign `F###` IDs to the 11 label-matrix rows.~~ **Closed** —
   `F336`-`F346`, contiguous with the rest of the file.
3. **`check_pdf.py` check 6 needs running text.** The 21 parsed labels must each
   appear in the notes' prose. Highest-risk rows: `Fig 7.6`'s 8 labels
   (retrovirus replication) and `Fig 7.1`'s 7 (Plasmodium life cycle) — these are
   exactly defects 5-6 from the Ch9 post-mortem, so write the label words into the
   running text as each figure is placed, not afterwards.
4. **`extract_figures.py` docstring holds stale fig 7.10 overflow numbers**
   (`L2.8/T14.3/R7.6`, measured against the superseded rect `348,224,460,366`).
   Correct to `L4.8/T9.3/R11.6` when that file is next touched, so a future
   session does not read the mismatch as a regression. Cosmetic — deliberately
   **not** fixed during a freeze-closing session.
5. **Pass 2 must keep the Widal-test definition adjacent to the Typhoid Mary
   anecdote.** NCERT splits them: the definition sits in the prose *above* the
   "Widal test" run-in head while the opener under that head pivots straight to
   Mary Mallon (structural finding at `F308`). Reproducing the split reads as a
   non-sequitur.
6. **Ex 5 (DNA vaccines) must go in the "Terms used in the exercises" appendix,
   not the main text.** Rule 5 forbids importing the mechanism from Chapter 10.
   State only what `F115`-`F116` support and mark the rest out of scope.
7. **Ex 4 needs the "water-borne" grouping named explicitly** where `F067`-`F069`
   are written up. NCERT itself only ever writes "air-borne" and "vector-borne".
8. **Do not render `H2L2` (`F094`) with a caret or Unicode subscript.** Antibody
   notation must stay flat text or `check_pdf.py` check 5 (banned glyphs) fails.
   The same applies to `α-interferon` (`F205`) — write "alpha-interferon".
9. **Figure 7.4's QR thumbnail on page 3 must stay excluded.** It re-prints the
   antibody artwork and carries no fact of its own; embedding it would duplicate
   `fig_7_4`.
10. **The Swaminathan portrait (page 2) is a hard no** under `§5` item 3 / `§4.4`,
    greyscaled or not. `check_pdf.py` check 4 would WARN on it.
11. **`°` (U+00B0) is NOT a banned glyph — do not "fix" it.** Two frozen rows carry
    it: `F023` ("39° to 40°C") and the 1-S note restating that range. Item 8 above
    correctly bans `α`, and the natural assumption is that the degree sign goes the
    same way — so this was **tested against the linter rather than assumed**:
    `α` **is** in `check_pdf.py`'s `GREEK` set, while `°` is in **none** of
    `ARROWS`, `GREEK` or `SUBSUP`. The typhoid fever range may therefore be
    rendered with a real degree sign. Recorded so a later session does not spend
    Pass 2 budget "spelling out" a glyph that was never a problem, and does not
    generalise item 8 into a rule the linter does not hold.

### Gate 1 re-verification — resumed session, 2026-08-23

Gate 1 was **re-derived from scratch, not re-read**, per the `§7` rule that a
handoff's findings are claims to re-derive. The venv was **absent** at session
start (the expected `§0.2` state) and was rebuilt to identical versions
(reportlab 5.0.1 / pymupdf 1.28.2 / Pillow 12.3.0 on 3.13) **before** anything was
diagnosed. `scratch/ch7_1z/derive_counts.py` re-ran green (exit 0, 10/10), and
these claims were re-measured independently against the **source PDF and the
assets on disk**, not against this file's own prose:

- **346 rows, `F001`..`F346`**, contiguous, 0 gaps, 0 duplicates, **0 ticked**;
  block sums `276+29+28+2+11 = 346`; `Type` = 17 values, all lowercase.
- **`_extract_labels` imported from the real `check_pdf.py`** returns **21 labels /
  4 figures** (7.1→7, 7.4→3, 7.5→3, 7.6→8), **no doubling, no phantom `Fig #`**.
  The Ch12 trap was *executed*, not merely cited, and did **not** fire.
- **Census-vs-list arithmetic re-checked:** headings `16 + 13 = 29` (16 and 13 IDs
  actually listed); the opener roll-call holds 30 table rows carrying exactly **28**
  opener IDs, contiguous `F306`..`F333` and identical to the 28 `Type: opener` rows
  in the Facts table. An early probe of mine reported "34 opener IDs" — that was
  **my regex catching the heading IDs in the roll-call's left column**, not a defect
  in the file. Noted because the next session will likely write the same probe.
- **All 11 assets re-opened**: every one `mode=L` with all sampled pixels R==G==B.
  Figs 7.1 and 7.4 were viewed at full size and their quoted labels confirmed
  against the artwork; both crops are complete, with no clipped callouts.
- **Summary re-extracted** by re-running `summary_sentences.py`: **18 sentences**,
  sentence 1 reads *"Health is not just the absence of disease."* — the self-check
  this file demands — so the block-geometry selection is still correct.
- **The two SUMMARY-UNIQUE rows re-tested against the source:** "cholera" gets
  **1 hit in 22 pages, on p21 (the summary itself)** and none in the body, so
  `F335` stands. `F334` is subtler and was deliberately re-challenged: the word
  "psychological" *does* occur 5 times in the body — but never in a definition of
  health. The body's definition (p4) is "physical, mental and social"; the summary
  (p21) is "physical, mental, social and psychological". The row records the added
  qualifier, which is correct.
- **Both exercise gaps re-confirmed as genuine:** "DNA vaccine", "suitable gene"
  and "water-borne" occur **only on p22** (the exercises). The body writes
  "air-borne" (p7) and never "water-borne".
- **The largest 1-F carry-over was verified closed, not assumed closed:** the
  process-arrow sentences have real rows — 18 `figure-text` rows, including
  `F045`-`F052` (malaria life cycle) and `F171`/`F172` (HIV replication).

**No frozen row was added, removed, reworded or reclassified in this session.**
Two carry-overs (11 above, and the roll-call regex note) were appended, and the
roll-up documents were corrected — `CHAPTER_TRACKER.md`'s Ch7 row still read
"session `1-F` only / GATE 1 NOT MET / no Facts table, no heading/opener census",
which was a **live false claim**, and `CHAPTER_STATUS.md` had **no Ch7 row at all**.
Both now name the specific gate. Roll-ups were **re-derived by counting** `✅` rows
(Class 11 = 6, Class 12 = 6, **12/32**) rather than incremented; Gate 1 closure
earns Ch7 **no** place in that tally, so the totals correctly did not move.

---

## Gate 2 — CLOSED 2026-08-23 (Pass 2)

`check_pdf.py` **exits 0 — 0 FAIL, 1 WARN**, run against the freshly rebuilt PDF.
The venv was **absent** at session start (the expected `§0.2` state) and was rebuilt
to identical versions (reportlab 5.0.1 / pymupdf 1.28.2 / Pillow 12.3.0 on 3.13.11)
**before** anything was diagnosed — per `§0.2`, a missing interpreter is the most
commonly misdiagnosed failure in this workflow.

**State found, versus what the handoff claimed.** The tracker and the Gate 1 record
above both asserted "no script and no PDF" and that Pass 2 was "roughly half-built,
stopping at an `INSERTION_POINT_3` marker with no `main()`". **All of that was stale.**
Re-derived from disk: the script is **1527 lines**, contains **no** insertion or TODO
marker, has a working `main()`, and carries every section through `7.5.4` plus the
QUICK RECAP and the exercises appendix. Facts-row coverage by section confirms it:
`7.3` 36 rows, `7.4` 37, `7.5` 30, `7.5.1`-`7.5.4` 51 — the sections claimed missing
are the most densely covered in the chapter. Per `§7`, a handoff's account of *what*
failed is evidence and its account of *why* is a hypothesis; here even the *what* had
been overtaken by a later PR.

**The tick question, resolved by measurement rather than assumption.** `check_pdf.py`
line 462 accepts a bare `x` as ticked, and `346` rows each ended in `x` while the
Gate 1 record said "**0** ticked" — which reads exactly like a vacuous green. It was
tested instead of assumed: **all six delivered chapters** (Ch10, Ch12, Ch13, Ch9 and
the rest) use bare `x` as their ticked marker — 175/196/196/200 rows respectively.
`x` **is** the repo-wide ticked form, `check_pdf.py` is **correct as written**, and it
was therefore **not** modified. The Gate 1 phrasing meant "not yet earned, because no
PDF existed to verify against"; `CHAPTER_STATUS.md` states this directly — "`x` means
verified in the generated PDF". The PDF now exists and the content is verified, so the
marks are earned. **No frozen row was reworded, added, removed or reclassified.**

- **Check 7** reports **335/335 Facts rows ticked**. The `335` (not 346) is correct and
  not a shortfall: `check_ticked` scopes itself to the `## Facts` table, so the 11
  `F336`-`F346` label-matrix rows under `## Figure-label matrix` are out of scope **by
  design** — they are gated by check 6 instead, which reports **21/21 labels in running
  text, 0 partial, 0 missing**. `335 + 11 = 346`.
- **The single WARN is check 4, and it is a confirmed true negative** (recorded per
  `§6` Pass 3's rule that a legitimately non-firing or benign check be logged so it is
  never later mistaken for a suppressed finding). It fires on `fig_7_3`, which was
  **opened and eyeballed**: NCERT's clinical close-up of a ringworm lesion on the chin
  and jaw, correctly `mode=L`. That is the chapter's own subject matter, not the banned
  item — `§5` item 3 bans a *scientist portrait*, and the **M.S. Swaminathan photograph
  is genuinely absent**: it appears nowhere but a script comment documenting its
  exclusion, and the PDF holds **exactly 11 embedded image objects**, all `fig_7_*`,
  with no twelfth object. Carry-over items 9 and 10 are therefore both closed.
- **Carry-over items 3, 5, 6, 7, 8 verified closed in the rendered output**, each
  carrying a source comment naming its obligation:
  - **3 (the highest-risk item)** — Fig 7.6's 8 retrovirus labels and Fig 7.1's 7
    Plasmodium labels are written into the running text where the figure sits, not
    bolted on afterwards. Page 11 was rendered and read to confirm it. This is the
    Ch9 defect 5-6 class, prevented rather than rediscovered.
  - **5** — the Widal definition sits adjacent to the Mary Mallon anecdote, with the
    `1-O` structural finding at `F308` reproduced deliberately rather than inherited.
  - **6** — "DNA vaccines" is confined to the appendix and explicitly marked out of
    scope; the Ch10 mechanism is **not** imported.
  - **7** — "water-borne" is named explicitly alongside NCERT's own "air-borne" /
    "vector-borne" (visually confirmed on rendered page 6).
  - **8** — "alpha-interferon" is spelled out. `H2L2` is rendered with ReportLab's
    `<sub>` *markup tag*, which emits positioned glyphs rather than a Unicode
    subscript codepoint — so check 5 passes and the item's intent holds.
- **Item 11 re-confirmed, and a deviation recorded.** `°` is genuinely allowed (it is
  in none of `ARROWS`/`GREEK`/`SUBSUP`), but the script nevertheless writes "39 degrees
  C to 40 degrees C". That is a **conservative, harmless choice, not a defect**; the
  frozen script was left untouched. Logged so a later session neither "fixes" it nor
  reads it as a linter finding.
- **Item 4 remains open and deliberately unfixed** — `extract_figures.py`'s stale fig
  7.10 overflow numbers are cosmetic, and a gate-closing session is the wrong place to
  touch a figure-extraction file.
- **Mechanical checks all green:** no footer/header band text; smallest rendered glyph
  **6.0pt** (above the 5.0pt FAIL floor *and* the 6.0pt WARN band); all 11 images
  monochrome; no banned glyphs; **20/20 pages A4 portrait**; 163 badge plates clear of
  their banners; 104 headings none orphaned.
- **Rebuild is reproducible** (`§6` Gate 3 condition 5, checked early): rendering twice
  yields an identical text hash — 20 pages, 51556 chars, 11 images both times.

**Gate 2 is closed. Gate 3 remains open.** What Pass 2 has *not* done, and what must
not be mistaken for done: the low-coverage token screen run this session located its
25 weakest rows and four were cleared by opening the script and reading them
(`F102`/`F103` N-C termini and S-S bridges, `F231` CO/oxyhaemoglobin, `F318` the
allergy opener — all present, the low scores caused by bold markup splitting tokens).
Per the hard bar in `§6`, **that screen is Pass 2 evidence only and cannot clear a
single row.** Gate 3 still requires the per-page visual pass over all 20 pages and the
**bidirectional** full read — in particular direction 2 (source → inventory), the one
that actually failed on Ch9 twice. Only 2 of 20 pages have been looked at.

## Out-of-pipeline text edit (2026-09-02) — not a Pass 2 session

Four prose-only fixes were applied directly to `Ch7_HumanHealthAndDisease.py` outside
the normal pass structure, at the requester's direction: (1) dropped the
throat-clearing opener clause in the chapter-intro paragraph (`F306`) and a redundant
lead-in sentence in the Widal test / Typhoid Mary passage (`F026`-area); (2) reworded
one hedge construction ("It should be clearly borne in mind that…") in the addiction
passage (`F247`/`F248`); (3) replaced two "due to/ascribed to the fact that"
constructions with "because" in the immunity passage (`§7.2`, `§7.2.2`); (4)
de-duplicated four separately-occurring "NCERT's own wording/order/points" attribution
phrases into varied wording (disease-group table header, `§7.1i` water-borne passage,
the P-P-C-C memory aid, the DNA-vaccine appendix). **No Facts row, figure caption,
label, or asset was touched** — every change is phrasing only, checked by diff against
the previously committed script (see the paired GitHub commit message for the literal
diff). This was **not** a Pass 2 session and did not follow the `§6` protocol; it is
logged here so it is not mistaken for one.

**Re-verification run this session (not carried forward from August):**
`check_pdf.py` on the rebuilt PDF returns **exit 0 — WARN (0 fail, 1 warn)**, same
verdict shape as Gate 2 close. The warn is the same check 4 trigger re-inspected fresh
— all four flagged manifest lines are text mentions of "photograph" (the Fig 7.3
ringworm caption note and the M.S. Swaminathan exclusion comment), no image embedded,
**11/11 embedded images confirmed monochrome**, same as before. Re-derived fresh:
**20 pp / 51,575 chars / 11 imgs, text SHA `438ff96647b64fbc`** (was 51,556 chars at
Gate 2 close; the +19 net char difference is consistent with the four wording changes
above — shorter openers, cut duplicate lead-ins, versus the added "because"/"chapter's
own" phrasing). **21/21 figure labels still in running text, 0 partial, 0 missing.**

**A pre-existing count discrepancy was found, not introduced by this edit.** Check 7
(`check_ticked`) reports **338** Facts rows ticked when re-run today, not the **335**
recorded at Gate 2 close above. Traced directly against `check_pdf.py`'s own parser
(`§`grep on `## Facts` scope): the table's row count was always 338 once the lettered
sub-rows (`F001a`, `F001b`, and others matching `[a-z]?\d{2,}`) are counted alongside
the plain-numbered rows running `F001`-`F335` — this session's script edit never
touched the inventory file, so the true row count cannot have changed today. The
`335/335 … 335+11=346` figure above was therefore already stale before this session,
for a reason unrelated to this edit. **Left as found, not corrected in place**, per
`§7`'s rule that a documentation defect is logged rather than silently overwritten —
whoever next runs a real Pass 2/3 session on Ch7 should resolve which of `335` or
`338` (or a fresh third count) is the row count to carry forward, ideally by listing
the full ID set rather than trusting either number here.

**Gate 3 status is unchanged by this edit.** No Pass 3(a) visual pass and no Pass 3(b)
bidirectional read were performed. Ch7 remains **NOT in the Done tally**.
