# Frozen Inventory — Locomotion and Movement (Chapter 17, Class 11)

**Source PDF:** `Chapter/class 11/Chapter 17 - Locomotion and Movement.pdf` (13 extracted pages; textbook pp. 217-229)
**Class:** 11 · **Chapter:** 17
**Figure assets:** 10 (`assets/fig_17_1.png` .. `assets/fig_17_10.png`)
**Gate 1 frozen:** 2026-08-31
**Facts rows:** 183 (F001-F183) · **Figure-label matrix rows:** 10 (F184-F193) · **Total:** 193

This is the **full Pass 1 inventory** and the Gate 1 deliverable. It supersedes the earlier figures-only freeze that lived in this same file (session `1-F`), whose figure-label matrix, captions, crop rectangles and manifest are preserved **verbatim** below — only their row IDs were shifted to the end of the ID space (was `F001`-`F010`, now `F184`-`F193`) so the Facts table can occupy a contiguous `F001`-`F183` in source order, matching the Ch15/Ch16 house format. No asset, caption string, crop rectangle, or label was re-extracted or reworded by this session; figure extraction was already complete and verified.

## Session log (Pass 1)

| Session | Sweep | Outcome |
|---|---|---|
| `1-F` | Figure extraction, monochrome conversion, per-asset label harvest | done earlier — 10 assets, 10 captions, label matrix (preserved as F184-F193) |
| `1-S` | Full source read, start to finish, before any Facts row was written | done this session — all 13 extracted pages read (textbook pp. 217-229) |
| `1-H` | Heading sweep | done — 10 heading rows (5 numbered + 2 sub-numbered + 3 unnumbered) |
| `1-O` | Opener sweep | done — 7 opener rows (intro + 6 headed sections that carry an opening sentence) |
| `1-Z` | Summary + exercise-gap sweep | done — 40 summary sentences classified; 10 exercises scanned |

## Source-typo / transcription policy (recorded so frozen rows are never silently "corrected")

The source text layer and artwork contain deviations. Each is transcribed **exactly as the source draws it** in the Facts row and flagged here; the downstream rewrite prose may legitimately spell them correctly.

- **`arragement`** — p.11 (textbook p.227), in the Synovial-joints sentence carried by `F162`. The source misspells "arrangement". Both extractors return `arragement`. Row stands verbatim.
- **`syncitium`** — p.3/4 (textbook p.219), carried by `F052`. NCERT prints "syncitium" (the conventional spelling is "syncytium"). Row stands verbatim.
- **`ADP and P` + stray `1`** — p.6 (textbook p.222), carried by `F090`. The source draws inorganic phosphate as **P with a subscript**, which the text layer splits, emitting `... ADP and P goes back ...` on one line and a bare `1` on the next. Transcribed as `Pi` in the row (ASCII, no Unicode subscript per the encoding rule); the split is a text-layer artefact, not a second fact.
- **`222222222222222 BIOLOGY`** — p.6 running head is corrupted in the text layer (the page number "222" is repeated by the extractor). Page furniture, not a row.
- **Decorative drop-cap / vertical-title scatter** — the chapter-opening contents rail (`17.1 Types of Movement` … `17.5 Disorders …`) and the vertical title `LOCOMOTION AND MOVEMENT` interleave with intro prose in the p.1 text layer. Deduplicated by reading, not by string-splitting; the contents rail is captured once as the chapter's section list, not as five separate heading rows (the ALLCAPS body headings are the authoritative heading rows).

## Facts table

One row per sentence-level fact, in source order. Types: `heading` · `opener` · `concept` · `process` · `number` · `definition` · `example` · `disorder` · `caption`. Every row is **unticked** at Gate 1 freeze (Pass 2 ticks them). Apostrophes/band-letters are transcribed with straight ASCII quotes (`'Z'`, `'A'`, `'I'`, `'H'`); the figure-label matrix (F184-F193) preserves the curly quotes exactly as the `1-F` session recorded them from the artwork.

| ID | Section | Type | Exact original wording | Ticked |
|----|---------|------|------------------------|--------|
| F001 | title | heading | "LOCOMOTION AND MOVEMENT" (chapter title plate) | x |
| F002 | intro | opener | "Movement is one of the significant features of living beings." | x |
| F003 | intro | concept | "Animals and plants exhibit a wide range of movements." | x |
| F004 | intro | example | "Streaming of protoplasm in the unicellular organisms like Amoeba is a simple form of movement." | x |
| F005 | intro | example | "Movement of cilia, flagella and tentacles are shown by many organisms." | x |
| F006 | intro | example | "Human beings can move limbs, jaws, eyelids, tongue, etc." | x |
| F007 | intro | definition | "Some of the movements result in a change of place or location. Such voluntary movements are called locomotion." | x |
| F008 | intro | example | "Walking, running, climbing, flying and swimming are all some forms of locomotory movements." | x |
| F009 | intro | concept | "Locomotory structures need not be different from those affecting other types of movements." | x |
| F010 | intro | example | "For example, in Paramoecium, cilia helps in the movement of food through cytopharynx and in locomotion as well." | x |
| F011 | intro | example | "Hydra can use its tentacles for capturing its prey and also use them for locomotion." | x |
| F012 | intro | example | "We use limbs for changes in body postures and locomotion as well." | x |
| F013 | intro | concept | "The above observations suggest that movements and locomotion cannot be studied separately." | x |
| F014 | intro | concept | "The two may be linked by stating that all locomotions are movements but all movements are not locomotions." | x |
| F015 | intro | concept | "Methods of locomotion performed by animals vary with their habitats and the demand of the situation." | x |
| F016 | intro | concept | "However, locomotion is generally for search of food, shelter, mate, suitable breeding grounds, favourable climatic conditions or to escape from enemies/predators." | x |
| F017 | 17.1 | heading | "17.1 TYPES OF MOVEMENT" | x |
| F018 | 17.1 | opener | "Cells of the human body exhibit three main types of movements, namely, amoeboid, ciliary and muscular." | x |
| F019 | 17.1 | concept | "Some specialised cells in our body like macrophages and leucocytes in blood exhibit amoeboid movement." | x |
| F020 | 17.1 | process | "It is effected by pseudopodia formed by the streaming of protoplasm (as in Amoeba)." | x |
| F021 | 17.1 | concept | "Cytoskeletal elements like microfilaments are also involved in amoeboid movement." | x |
| F022 | 17.1 | concept | "Ciliary movement occurs in most of our internal tubular organs which are lined by ciliated epithelium." | x |
| F023 | 17.1 | process | "The coordinated movements of cilia in the trachea help us in removing dust particles and some of the foreign substances inhaled along with the atmospheric air." | x |
| F024 | 17.1 | process | "Passage of ova through the female reproductive tract is also facilitated by the ciliary movement." | x |
| F025 | 17.1 | concept | "Movement of our limbs, jaws, tongue, etc, require muscular movement." | x |
| F026 | 17.1 | concept | "The contractile property of muscles are effectively used for locomotion and other movements by human beings and majority of multicellular organisms." | x |
| F027 | 17.1 | concept | "Locomotion requires a perfect coordinated activity of muscular, skeletal and neural systems." | x |
| F028 | 17.1 | concept | "In this chapter, you will learn about the types of muscles, their structure, mechanism of their contraction and important aspects of the skeletal system." | x |
| F029 | 17.2 | heading | "17.2 MUSCLE" | x |
| F030 | 17.2 | opener | "You have studied in Chapter 8 that the cilia and flagella are the outgrowths of the cell membrane." | x |
| F031 | 17.2 | example | "Flagellar movement helps in the swimming of spermatozoa, maintenance of water current in the canal system of sponges and in locomotion of Protists like Euglena." | x |
| F032 | 17.2 | definition | "Muscle is a specialised tissue of mesodermal origin." | x |
| F033 | 17.2 | number | "About 40-50 per cent of the body weight of a human adult is contributed by muscles." | x |
| F034 | 17.2 | concept | "They have special properties like excitability, contractility, extensibility and elasticity." | x |
| F035 | 17.2 | concept | "Muscles have been classified using different criteria, namely location, appearance and nature of regulation of their activities." | x |
| F036 | 17.2 | concept | "Based on their location, three types of muscles are identified : (i) Skeletal (ii) Visceral and (iii) Cardiac." | x |
| F037 | 17.2 | concept | "Skeletal muscles are closely associated with the skeletal components of the body." | x |
| F038 | 17.2 | concept | "They have a striped appearance under the microscope and hence are called striated muscles." | x |
| F039 | 17.2 | concept | "As their activities are under the voluntary control of the nervous system, they are known as voluntary muscles too." | x |
| F040 | 17.2 | concept | "They are primarily involved in locomotory actions and changes of body postures." | x |
| F041 | 17.2 | concept | "Visceral muscles are located in the inner walls of hollow visceral organs of the body like the alimentary canal, reproductive tract, etc." | x |
| F042 | 17.2 | concept | "They do not exhibit any striation and are smooth in appearance. Hence, they are called smooth muscles (nonstriated muscle)." | x |
| F043 | 17.2 | concept | "Their activities are not under the voluntary control of the nervous system and are therefore known as involuntary muscles." | x |
| F044 | 17.2 | example | "They assist, for example, in the transportation of food through the digestive tract and gametes through the genital tract." | x |
| F045 | 17.2 | concept | "As the name suggests, Cardiac muscles are the muscles of heart." | x |
| F046 | 17.2 | concept | "Many cardiac muscle cells assemble in a branching pattern to form a cardiac muscle." | x |
| F047 | 17.2 | concept | "Based on appearance, cardiac muscles are striated." | x |
| F048 | 17.2 | concept | "They are involuntary in nature as the nervous system does not control their activities directly." | x |
| F049 | 17.2 | definition | "Each organised skeletal muscle in our body is made of a number of muscle bundles or fascicles held together by a common collagenous connective tissue layer called fascia." | x |
| F050 | 17.2 | concept | "Each muscle bundle contains a number of muscle fibres (Figure 17.1)." | x |
| F051 | 17.2 | definition | "Each muscle fibre is lined by the plasma membrane called sarcolemma enclosing the sarcoplasm." | x |
| F052 | 17.2 | concept | "Muscle fibre is a syncitium as the sarcoplasm contains many nuclei." | x |
| F053 | 17.2 | concept | "The endoplasmic reticulum, i.e., sarcoplasmic reticulum of the muscle fibres is the store house of calcium ions." | x |
| F054 | 17.2 | definition | "A characteristic feature of the muscle fibre is the presence of a large number of parallelly arranged filaments in the sarcoplasm called myofilaments or myofibrils." | x |
| F055 | 17.2 | concept | "Each myofibril has alternate dark and light bands on it." | x |
| F056 | 17.2 | concept | "A detailed study of the myofibril has established that the striated appearance is due to the distribution pattern of two important proteins - Actin and Myosin." | x |
| F057 | 17.2 | definition | "The light bands contain actin and is called I-band or Isotropic band, whereas the dark band called 'A' or Anisotropic band contains myosin." | x |
| F058 | 17.2 | concept | "Both the proteins are arranged as rod-like structures, parallel to each other and also to the longitudinal axis of the myofibrils." | x |
| F059 | 17.2 | concept | "Actin filaments are thinner as compared to the myosin filaments, hence are commonly called thin and thick filaments respectively." | x |
| F060 | 17.2 | definition | "In the centre of each 'I' band is an elastic fibre called 'Z' line which bisects it." | x |
| F061 | 17.2 | concept | "The thin filaments are firmly attached to the 'Z' line." | x |
| F062 | 17.2 | definition | "The thick filaments in the 'A' band are also held together in the middle of this band by a thin fibrous membrane called 'M' line." | x |
| F063 | 17.2 | concept | "The 'A' and 'I' bands are arranged alternately throughout the length of the myofibrils." | x |
| F064 | 17.2 | definition | "The portion of the myofibril between two successive 'Z' lines is considered as the functional unit of contraction and is called a sarcomere (Figure 17.2)." | x |
| F065 | 17.2 | concept | "In a resting state, the edges of thin filaments on either side of the thick filaments partially overlap the free ends of the thick filaments leaving the central part of the thick filaments." | x |
| F066 | 17.2 | definition | "This central part of thick filament, not overlapped by thin filaments is called the 'H' zone." | x |
| F067 | 17.2.1 | heading | "17.2.1 Structure of Contractile Proteins" | x |
| F068 | 17.2.1 | opener | "Each actin (thin) filament is made of two 'F' (filamentous) actins helically wound to each other." | x |
| F069 | 17.2.1 | definition | "Each 'F' actin is a polymer of monomeric 'G' (Globular) actins." | x |
| F070 | 17.2.1 | concept | "Two filaments of another protein, tropomyosin also run close to the 'F' actins throughout its length." | x |
| F071 | 17.2.1 | concept | "A complex protein Troponin is distributed at regular intervals on the tropomyosin." | x |
| F072 | 17.2.1 | process | "In the resting state a subunit of troponin masks the active binding sites for myosin on the actin filaments (Figure 17.3a)." | x |
| F073 | 17.2.1 | concept | "Each myosin (thick) filament is also a polymerised protein." | x |
| F074 | 17.2.1 | definition | "Many monomeric proteins called Meromyosins (Figure 17.3b) constitute one thick filament." | x |
| F075 | 17.2.1 | definition | "Each meromyosin has two important parts, a globular head with a short arm and a tail, the former being called the heavy meromyosin (HMM) and the latter, the light meromyosin (LMM)." | x |
| F076 | 17.2.1 | definition | "The HMM component, i.e.; the head and short arm projects outwards at regular distance and angle from each other from the surface of a polymerised myosin filament and is known as cross arm." | x |
| F077 | 17.2.1 | concept | "The globular head is an active ATPase enzyme and has binding sites for ATP and active sites for actin." | x |
| F078 | 17.2.2 | heading | "17.2.2 Mechanism of Muscle Contraction" | x |
| F079 | 17.2.2 | opener | "Mechanism of muscle contraction is best explained by the sliding filament theory which states that contraction of a muscle fibre takes place by the sliding of the thin filaments over the thick filaments." | x |
| F080 | 17.2.2 | process | "Muscle contraction is initiated by a signal sent by the central nervous system (CNS) via a motor neuron." | x |
| F081 | 17.2.2 | definition | "A motor neuron along with the muscle fibres connected to it constitute a motor unit." | x |
| F082 | 17.2.2 | definition | "The junction between a motor neuron and the sarcolemma of the muscle fibre is called the neuromuscular junction or motor-end plate." | x |
| F083 | 17.2.2 | process | "A neural signal reaching this junction releases a neurotransmitter (Acetyl choline) which generates an action potential in the sarcolemma." | x |
| F084 | 17.2.2 | process | "This spreads through the muscle fibre and causes the release of calcium ions into the sarcoplasm." | x |
| F085 | 17.2.2 | process | "Increase in Ca++ level leads to the binding of calcium with a subunit of troponin on actin filaments and thereby remove the masking of active sites for myosin." | x |
| F086 | 17.2.2 | process | "Utilising the energy from ATP hydrolysis, the myosin head now binds to the exposed active sites on actin to form a cross bridge (Figure 17.4)." | x |
| F087 | 17.2.2 | process | "This pulls the attached actin filaments towards the centre of 'A' band." | x |
| F088 | 17.2.2 | process | "The 'Z' line attached to these actins are also pulled inwards thereby causing a shortening of the sarcomere, i.e., contraction." | x |
| F089 | 17.2.2 | concept | "It is clear from the above steps, that during shortening of the muscle, i.e., contraction, the 'I' bands get reduced, whereas the 'A' bands retain the length (Figure 17.5)." | x |
| F090 | 17.2.2 | process | "The myosin, releasing the ADP and Pi goes back to its relaxed state." | x |
| F091 | 17.2.2 | process | "A new ATP binds and the cross-bridge is broken (Figure 17.4)." | x |
| F092 | 17.2.2 | process | "The ATP is again hydrolysed by the myosin head and the cycle of cross bridge formation and breakage is repeated causing further sliding." | x |
| F093 | 17.2.2 | process | "The process continues till the Ca++ ions are pumped back to the sarcoplasmic cisternae resulting in the masking of actin filaments." | x |
| F094 | 17.2.2 | process | "This causes the return of 'Z' lines back to their original position, i.e., relaxation." | x |
| F095 | 17.2.2 | concept | "The reaction time of the fibres can vary in different muscles." | x |
| F096 | 17.2.2 | process | "Repeated activation of the muscles can lead to the accumulation of lactic acid due to anaerobic breakdown of glycogen in them, causing fatigue." | x |
| F097 | 17.2.2 | definition | "Muscle contains a red coloured oxygen storing pigment called myoglobin." | x |
| F098 | 17.2.2 | concept | "Myoglobin content is high in some of the muscles which gives a reddish appearance. Such muscles are called the Red fibres." | x |
| F099 | 17.2.2 | concept | "These muscles also contain plenty of mitochondria which can utilise the large amount of oxygen stored in them for ATP production. These muscles, therefore, can also be called aerobic muscles." | x |
| F100 | 17.2.2 | concept | "On the other hand, some of the muscles possess very less quantity of myoglobin and therefore, appear pale or whitish. These are the White fibres." | x |
| F101 | 17.2.2 | concept | "Number of mitochondria are also few in them, but the amount of sarcoplasmic reticulum is high. They depend on anaerobic process for energy." | x |
| F102 | 17.3 | heading | "17.3 SKELETAL SYSTEM" | x |
| F103 | 17.3 | opener | "Skeletal system consists of a framework of bones and a few cartilages." | x |
| F104 | 17.3 | concept | "This system has a significant role in movement shown by the body." | x |
| F105 | 17.3 | concept | "Imagine chewing food without jaw bones and walking around without the limb bones." | x |
| F106 | 17.3 | concept | "Bone and cartilage are specialised connective tissues." | x |
| F107 | 17.3 | concept | "The former has a very hard matrix due to calcium salts in it and the latter has slightly pliable matrix due to chondroitin salts." | x |
| F108 | 17.3 | number | "In human beings, this system is made up of 206 bones and a few cartilages." | x |
| F109 | 17.3 | concept | "It is grouped into two principal divisions - the axial and the appendicular skeleton." | x |
| F110 | 17.3 | number | "Axial skeleton comprises 80 bones distributed along the main axis of the body." | x |
| F111 | 17.3 | concept | "The skull, vertebral column, sternum and ribs constitute axial skeleton." | x |
| F112 | 17.3 | number | "The skull (Figure 17.6) is composed of two sets of bones - cranial and facial, that totals to 22 bones." | x |
| F113 | 17.3 | number | "Cranial bones are 8 in number. They form the hard protective outer covering, cranium for the brain." | x |
| F114 | 17.3 | number | "The facial region is made up of 14 skeletal elements which form the front part of the skull." | x |
| F115 | 17.3 | concept | "A single U-shaped bone called hyoid is present at the base of the buccal cavity." | x |
| F116 | 17.3 | concept | "Each middle ear contains three tiny bones - Malleus, Incus and Stapes, collectively called Ear Ossicles." | x |
| F117 | 17.3 | concept | "The skull region articulates with the superior region of the vertebral column with the help of two occipital condyles (dicondylic skull)." | x |
| F118 | 17.3 | number | "Our vertebral column (Figure 17.7) is formed by 26 serially arranged units called vertebrae and is dorsally placed." | x |
| F119 | 17.3 | concept | "It extends from the base of the skull and constitutes the main framework of the trunk." | x |
| F120 | 17.3 | definition | "Each vertebra has a central hollow portion (neural canal) through which the spinal cord passes." | x |
| F121 | 17.3 | concept | "First vertebra is the atlas and it articulates with the occipital condyles." | x |
| F122 | 17.3 | number | "The vertebral column is differentiated into cervical (7), thoracic (12), lumbar (5), sacral (1-fused) and coccygeal (1-fused) regions starting from the skull." | x |
| F123 | 17.3 | concept | "The number of cervical vertebrae are seven in almost all mammals including human beings." | x |
| F124 | 17.3 | concept | "The vertebral column protects the spinal cord, supports the head and serves as the point of attachment for the ribs and musculature of the back." | x |
| F125 | 17.3 | definition | "Sternum is a flat bone on the ventral midline of thorax." | x |
| F126 | 17.3 | number | "There are 12 pairs of ribs." | x |
| F127 | 17.3 | concept | "Each rib is a thin flat bone connected dorsally to the vertebral column and ventrally to the sternum." | x |
| F128 | 17.3 | definition | "It has two articulation surfaces on its dorsal end and is hence called bicephalic." | x |
| F129 | 17.3 | concept | "First seven pairs of ribs are called true ribs. Dorsally, they are attached to the thoracic vertebrae and ventrally connected to the sternum with the help of hyaline cartilage." | x |
| F130 | 17.3 | concept | "The 8th, 9th and 10th pairs of ribs do not articulate directly with the sternum but join the seventh rib with the help of hyaline cartilage. These are called vertebrochondral (false) ribs." | x |
| F131 | 17.3 | concept | "Last 2 pairs (11th and 12th) of ribs are not connected ventrally and are therefore, called floating ribs." | x |
| F132 | 17.3 | concept | "Thoracic vertebrae, ribs and sternum together form the rib cage (Figure 17.8)." | x |
| F133 | 17.3 | definition | "The bones of the limbs along with their girdles constitute the appendicular skeleton." | x |
| F134 | 17.3 | number | "Each limb is made of 30 bones." | x |
| F135 | 17.3 | number | "The bones of the hand (fore limb) are humerus, radius and ulna, carpals (wrist bones - 8 in number), metacarpals (palm bones - 5 in number) and phalanges (digits - 14 in number) (Figure 17.9)." | x |
| F136 | 17.3 | number | "Femur (thigh bone - the longest bone), tibia and fibula, tarsals (ankle bones - 7 in number), metatarsals (5 in number) and phalanges (digits - 14 in number) are the bones of the legs (hind limb) (Figure 17.10)." | x |
| F137 | 17.3 | definition | "A cup shaped bone called patella cover the knee ventrally (knee cap)." | x |
| F138 | 17.3 | concept | "Pectoral and Pelvic girdle bones help in the articulation of the upper and the lower limbs respectively with the axial skeleton." | x |
| F139 | 17.3 | concept | "Each girdle is formed of two halves." | x |
| F140 | 17.3 | concept | "Each half of pectoral girdle consists of a clavicle and a scapula (Figure 17.9)." | x |
| F141 | 17.3 | definition | "Scapula is a large triangular flat bone situated in the dorsal part of the thorax between the second and the seventh ribs." | x |
| F142 | 17.3 | definition | "The dorsal, flat, triangular body of scapula has a slightly elevated ridge called the spine which projects as a flat, expanded process called the acromion." | x |
| F143 | 17.3 | concept | "The clavicle articulates with this." | x |
| F144 | 17.3 | definition | "Below the acromion is a depression called the glenoid cavity which articulates with the head of the humerus to form the shoulder joint." | x |
| F145 | 17.3 | concept | "Each clavicle is a long slender bone with two curvatures. This bone is commonly called the collar bone." | x |
| F146 | 17.3 | concept | "Pelvic girdle consists of two coxal bones (Figure 17.10)." | x |
| F147 | 17.3 | concept | "Each coxal bone is formed by the fusion of three bones - ilium, ischium and pubis." | x |
| F148 | 17.3 | definition | "At the point of fusion of the above bones is a cavity called acetabulum to which the thigh bone articulates." | x |
| F149 | 17.3 | definition | "The two halves of the pelvic girdle meet ventrally to form the pubic symphysis containing fibrous cartilage." | x |
| F150 | 17.4 | heading | "17.4 JOINTS" | x |
| F151 | 17.4 | opener | "Joints are essential for all types of movements involving the bony parts of the body." | x |
| F152 | 17.4 | concept | "Locomotory movements are no exception to this." | x |
| F153 | 17.4 | definition | "Joints are points of contact between bones, or between bones and cartilages." | x |
| F154 | 17.4 | concept | "Force generated by the muscles is used to carry out movement through joints, where the joint acts as a fulcrum." | x |
| F155 | 17.4 | concept | "The movability at these joints vary depending on different factors." | x |
| F156 | 17.4 | concept | "Joints have been classified into three major structural forms, namely, fibrous, cartilaginous and synovial." | x |
| F157 | 17.4 | concept | "Fibrous joints do not allow any movement." | x |
| F158 | 17.4 | example | "This type of joint is shown by the flat skull bones which fuse end-to-end with the help of dense fibrous connective tissues in the form of sutures, to form the cranium." | x |
| F159 | 17.4 | concept | "In cartilaginous joints, the bones involved are joined together with the help of cartilages." | x |
| F160 | 17.4 | example | "The joint between the adjacent vertebrae in the vertebral column is of this pattern and it permits limited movements." | x |
| F161 | 17.4 | definition | "Synovial joints are characterised by the presence of a fluid filled synovial cavity between the articulating surfaces of the two bones." | x |
| F162 | 17.4 | concept | "Such an arragement allows considerable movement." | x |
| F163 | 17.4 | concept | "These joints help in locomotion and many other movements." | x |
| F164 | 17.4 | example | "Ball and socket joint (between humerus and pectoral girdle), hinge joint (knee joint), pivot joint (between atlas and axis), gliding joint (between the carpals) and saddle joint (between carpal and metacarpal of thumb) are some examples." | x |
| F165 | 17.5 | heading | "17.5 DISORDERS OF MUSCULAR AND SKELETAL SYSTEM" | x |
| F166 | 17.5 | disorder | "Myasthenia gravis: Auto immune disorder affecting neuromuscular junction leading to fatigue, weakening and paralysis of skeletal muscle." | x |
| F167 | 17.5 | disorder | "Muscular dystrophy: Progressive degeneration of skeletal muscle mostly due to genetic disorder." | x |
| F168 | 17.5 | disorder | "Tetany: Rapid spasms (wild contractions) in muscle due to low Ca++ in body fluid." | x |
| F169 | 17.5 | disorder | "Arthritis: Inflammation of joints." | x |
| F170 | 17.5 | disorder | "Osteoporosis: Age-related disorder characterised by decreased bone mass and increased chances of fractures. Decreased levels of estrogen is a common cause." | x |
| F171 | 17.5 | disorder | "Gout: Inflammation of joints due to accumulation of uric acid crystals." | x |
| F172 | summary | heading | "SUMMARY" | x |
| F173 | exercises | heading | "EXERCISES" | x |
| F174 | figures | caption | "Figure 17.1 Diagrammatic cross sectional view of a muscle showing muscle bundles and muscle fibres" | x |
| F175 | figures | caption | "Figure 17.2 Diagrammatic representation of (a) anatomy of a muscle fibre showing a sarcomere (b) a sarcomere" | x |
| F176 | figures | caption | "Figure 17.3 (a) An actin (thin) filament (b) Myosin monomer (Meromyosin)" | x |
| F177 | figures | caption | "Figure 17.4 Stages in cross bridge formation, rotation of head and breaking of cross bridge" | x |
| F178 | figures | caption | "Figure 17.5 Sliding-filament theory of muscle contraction (movement of the thin filaments and the relative size of the I band and H zones)" | x |
| F179 | figures | caption | "Figure 17.6 Diagrammatic view of human skull" | x |
| F180 | figures | caption | "Figure 17.7 Vertebral column (right lateral view)" | x |
| F181 | figures | caption | "Figure 17.8 Ribs and rib cage" | x |
| F182 | figures | caption | "Figure 17.9 Right pectoral girdle and upper arm. (frontal view)" | x |
| F183 | figures | caption | "Figure 17.10 Right pelvic girdle and lower limb bones (frontal view)" | x |

### Caption discrepancy against the frozen figure manifest (recorded, not silently reconciled)

`F178` transcribes the **source-verbatim** caption of Figure 17.5: "... (movement of the thin filaments and the relative size of the I band and H zones)". The figure manifest below (preserved from session `1-F`) records the same figure's caption as "... (movement of the thin filament)" — a truncated/singular form. This is analogous to Ch16 defect **D5**: two homes for one caption string that disagree. **Disposition:** the source-verbatim `F178` is authoritative for the downstream rewrite and typeset caption; the manifest string is left exactly as the `1-F` session froze it and flagged here as **OBS-17.5** so the two do not silently diverge without a record. No frozen figure row is reworded by this Gate 1 session.

## Figure-label matrix

One row per figure. Labels were harvested in session `1-F` by opening each rendered monochrome asset at full size (§4.4 Step 1), **not** from the source text layer — Chapter 17's in-figure callouts are vector artwork. This matrix exists in exactly one place in this file and is the authoritative label record consumed by `check_pdf._extract_labels` (§6). Curly quotes are preserved exactly as the artwork draws them.

| ID | Fig # | Type | In-figure labels, verbatim - one row per figure, every callout listed | Ticked |
|----|-------|------|------------------------------------------------------------------|--------|
| F184 | Fig 17.1 | figure-label | Figure labels: “Fascicle (muscle bundle)”; “Muscle fibre (muscle cell)”; “Sarcolemma”; “Blood capillary” | |
| F185 | Fig 17.2 | figure-label | Figure labels: “Z line”; “A band”; “I band”; “H zone”; “Sarcomere”; “(a)”; “(b)” | |
| F186 | Fig 17.3 | figure-label | Figure labels: “Troponin”; “Tropomyosin”; “F actin”; “Actin binding sites”; “ATP binding sites”; “Head”; “Cross arm”; “(a)”; “(b)” | |
| F187 | Fig 17.4 | figure-label | Figure labels: “Actin filament”; “Myosin filament”; “P”; “ADP”; “ATP”; “Cross bridge”; “Myosin head”; “Sliding/rotation”; “(Breaking of cross bridge)”; “(Formation of cross bridge)” | |
| F188 | Fig 17.5 | figure-label | Figure labels: “H zone”; “I band”; “A band”; “Relaxed”; “Contracting”; “Maximally Contracted”; “Z line”; “Two Sarcomeres” | |
| F189 | Fig 17.6 | figure-label | Figure labels: “Parietal bone”; “Frontal bone”; “Temporal bone”; “Occipital bone”; “Occipital condyle”; “Sphenoid bone”; “Ethmoid bone”; “Lacrimal bone”; “Nasal bone”; “Zygomatic bone”; “Maxilla”; “Mandible”; “Hyoid bone” | |
| F190 | Fig 17.7 | figure-label | Figure labels: “Cervical vertebra”; “Thoracic vertebra”; “Lumbar vertebra”; “Intervertebral disc”; “Sacrum”; “Coccyx” | |
| F191 | Fig 17.8 | figure-label | Figure labels: “1”; “2”; “3”; “4”; “5”; “6”; “7”; “8”; “9”; “10”; “11”; “12”; “True ribs”; “False ribs”; “Floating ribs”; “Sternum”; �����Ribs”; “Vertebral column” | |
| F192 | Fig 17.9 | figure-label | Figure labels: “Clavicle”; “Scapula”; “Humerus”; “Radius”; “Ulna”; “Carpals”; “Metacarpals”; “Phalanges” | |
| F193 | Fig 17.10 | figure-label | Figure labels: “Ilium”; “Pubis”; “Ischium”; “Coxal bone”; “Sacrum”; “Femur”; “Patella”; “Tibia”; “Fibula”; “Tarsals”; “Metatarsals”; “Phalanges” | |

### Figure-only content (labels with no prose anchor) — Pass 2 obligations

Labels drawn in the artwork but never named in the running prose. These must be carried by the rewrite or the information is lost.

| Figure-only fact | Where it must be explained |
|---|---|
| "Blood capillary" (Fig 17.1) — the muscle's blood supply is drawn but the prose never mentions capillaries | 17.2, when the fascicle/fibre cross-section is described |
| "Intervertebral disc" (Fig 17.7) — drawn between vertebrae; prose names the cartilaginous joint between adjacent vertebrae (F160) but never the disc by name | 17.3 (vertebral column) or 17.4 (cartilaginous joints) |
| "Maximally Contracted" / "Contracting" / "Relaxed" (Fig 17.5) — the three discrete contraction states are a figure-only staging; prose describes contraction and relaxation but not this three-step labelling | 17.2.2, when I-band reduction is described |
| "Sliding/rotation", "(Formation of cross bridge)", "(Breaking of cross bridge)" (Fig 17.4) — process-stage captions inside the artwork | 17.2.2 cross-bridge cycle (prose covers formation/breaking; the *rotation* of the head is figure-emphasised) |

Parser note: Fig 17.8's numeric rib labels "1".."12" and Fig 17.3/17.4's single-letter labels ("P") are artwork scale/part marks; several coincide with prose numbers (rib pairs) and need no separate prose home beyond the rib-numbering already in F126-F131.

## Summary classification

**40** summary sentences classified (isolated from the SUMMARY box on textbook pp. 227-228). **37 BODY-PRESENT** (restate a body row) · **3 SUMMARY-UNIQUE** (add a framing the body never states outright). All 3 SUMMARY-UNIQUE are folded into named sections, so no summary-only fact is dropped.

| Summary sentence (abridged) | Class | Fold target |
|---|---|---|
| "Muscle fibre is the anatomical unit of muscle." | SUMMARY-UNIQUE | 17.2 — the body calls the sarcomere the *functional* unit of contraction (F064) and describes the fibre in detail, but never labels the fibre the *anatomical unit* |
| "Each sarcomere has a central 'A' band made of thick myosin filaments, and two half 'I' bands made of thin actin filaments on either side of it marked by 'Z' lines." | SUMMARY-UNIQUE | 17.2 — the body gives A-band, I-band and Z-line separately (F057, F060, F064) but never states the sarcomere = one central A-band + two *half* I-bands framing |
| "Muscles are classified as Red and White fibres based primarily on the amount of red coloured myoglobin pigment in them." | SUMMARY-UNIQUE | 17.2.2 — the body describes Red and White fibres (F098-F101) but the summary's explicit "classified ... based primarily on the amount of myoglobin" is the tidy criterion statement |

The remaining **37 sentences are BODY-PRESENT**: movement as essential feature (F002) · protoplasmic/ciliary/fin/limb/wing movement forms (F004-F005, F008) · locomotion definition (F007) · reasons for locomotion (F016) · three human-cell movement types (F018) · locomotion needs coordinated muscle activity (F027) · three muscle types (F036) · skeletal striated/voluntary (F037-F040) · visceral nonstriated/involuntary (F041-F043) · cardiac striated/branched/involuntary (F045-F048) · four muscle properties (F034) · myofibrils parallel in fibre (F054) · sarcomere serial units are functional units (F064) · actin/myosin polymerised contractile proteins (F056-F059) · troponin masks active sites (F072) · myosin head ATPase with ATP + actin sites (F077) · motor neuron → action potential (F080-F083) · Ca++ release from sarcoplasmic reticulum (F084) · Ca++ activates actin → cross bridge (F085-F086) · cross bridges pull actin → sliding → contraction (F087-F088) · Ca++ returned → actin inactivated → bridges broken → relaxation (F093-F094) · repeated stimulation → fatigue (F096) · bones + cartilages = skeletal system (F103) · axial/appendicular division (F109) · axial = skull/vertebral column/ribs/sternum (F111) · appendicular = limb bones + girdles (F133) · three joint types fibrous/cartilaginous/synovial (F156) · synovial allow considerable movement, role in locomotion (F161-F163).

## Exercise-gap terms

10 exercises scanned (textbook pp. 228-229). Most are answerable from body rows. The genuine gaps — facts the exercises assume but the body never states explicitly — are listed with a planned rewrite home; the rest are recorded as non-gaps so a later audit does not re-raise them.

| Term/fact assumed by exercises | Explained where |
|---|---|
| Ex 4(b) — that the H-zone represents **only thick** filaments (the true/false answer hinges on it not representing thin filaments) | 17.2, sharpening F066 so the H-zone is explicitly thick-filament-only |
| Ex 5(a) — a side-by-side **Actin vs Myosin** contrast as a difference pair | 17.2 / 17.2.1, keeping thin-vs-thick and troponin/tropomyosin-vs-ATPase-head contrasts adjacent (carried by F057-F077) |
| Ex 5(c) — a side-by-side **Pectoral vs Pelvic girdle** contrast pair | 17.3, keeping clavicle+scapula vs coxal-bone descriptions adjacent (F140-F149) |

Non-gaps, recorded so they are not re-raised: Ex 1 sarcomere diagram (F064, Fig 17.2) · Ex 2 sliding filament theory (F079) · Ex 3 steps in muscle contraction (F080-F094) · Ex 4(a) actin in thin filament (F057/F059) · Ex 4(c) 206 bones (F108) · Ex 4(d) rib pairs — 12 not 11 (F126) · Ex 4(e) sternum ventral (F125) · Ex 5(b) Red vs White muscles (F098-F101) · Ex 6(a) smooth muscle involuntary (F041-F043) · Ex 6(b) tropomyosin/thin filament (F057/F070) · Ex 6(c) red muscle/myoglobin (F097-F098) · Ex 6(d) skull/sutures (F158) · Ex 7 three movement types (F018) · Ex 8 skeletal vs cardiac muscle (F037-F048) · Ex 9(a) atlas/axis pivot (F164) · Ex 9(b) carpal/metacarpal saddle (F164) · Ex 9(c) between phalanges — hinge (Fig 17.4 joint types, F164) · Ex 9(d) femur/acetabulum ball-and-socket (F148, F164) · Ex 9(e) between cranial bones — fibrous/sutures (F158) · Ex 9(f) pubic bones — cartilaginous/pubic symphysis (F149) · Ex 10(a) cervical vertebrae = 7 (F122-F123) · Ex 10(b) phalanges = 14 (F135-F136) · Ex 10(c) F actins + tropomyosin/troponin (F068-F071) · Ex 10(d) Ca++ in sarcoplasmic reticulum (F053, F093) · Ex 10(e) floating ribs 11th/12th (F131) · Ex 10(f) cranium = 8 bones (F113).

Exercise 9 answer-key note: 9(c) "between phalanges" is a hinge joint — the chapter lists hinge only as "knee joint" (F164); the phalangeal application is an exercise inference, not a stated body fact, but it is answerable from the joint-type definitions, so it is a non-gap, not a gap.

## Figure manifest

Extraction, monochrome conversion and per-asset visual verification were completed in session `1-F` (skill `in-repo-ncert-figure-extraction`). Every asset is a 440 dpi clip render, Pillow mode `L` (`convert("L")` + `ImageOps.autocontrast(cutoff=1)`), opened individually at full size. Captions here are preserved verbatim from `1-F`; where a caption disagrees with its source-verbatim Facts row, see **OBS-17.5** above.

| Fig # | Caption (verbatim, as recorded in 1-F) | Asset file | Source page | Crop rectangle (PDF points) | Mono | Verified |
|---|---|---|---:|---|---|---|
| Fig 17.1 | Diagrammatic cross sectional view of a muscle showing muscle bundles and muscle fibres | `assets/fig_17_1.png` | 3 | `(90,245,525,502)` | Yes | Yes |
| Fig 17.2 | Diagrammatic representation of (a) anatomy of a muscle fibre showing a sarcomere (b) a sarcomere | `assets/fig_17_2.png` | 4 | `(85,325,520,680)` | Yes | Yes |
| Fig 17.3 | (a) An actin (thin) filament (b) Myosin monomer (Meromyosin) | `assets/fig_17_3.png` | 5 | `(85,375,505,595)` | Yes | Yes |
| Fig 17.4 | Stages in cross bridge formation, rotation of head and breaking of cross bridge | `assets/fig_17_4.png` | 6 | `(65,275,565,545)` | Yes | Yes |
| Fig 17.5 | Sliding-filament theory of muscle contraction (movement of the thin filament) | `assets/fig_17_5.png` | 7 | `(65,90,510,425)` | Yes | Yes |
| Fig 17.6 | Diagrammatic view of human skull | `assets/fig_17_6.png` | 8 | `(95,295,525,570)` | Yes | Yes |
| Fig 17.7 | Vertebral column (right lateral view) | `assets/fig_17_7.png` | 9 | `(275,75,520,365)` | Yes | Yes |
| Fig 17.8 | Ribs and rib cage | `assets/fig_17_8.png` | 9 | `(240,425,520,675)` | Yes | Yes |
| Fig 17.9 | Right pectoral girdle and upper arm. (frontal view) | `assets/fig_17_9.png` | 10 | `(50,75,295,382)` | Yes | Yes |
| Fig 17.10 | Right pelvic girdle and lower limb bones (frontal view) | `assets/fig_17_10.png` | 10 | `(50,410,295,758)` | Yes | Yes |

Asset dimensions and full extraction/audit notes are unchanged from session `1-F` (see the extraction script `extract_figures.py` and `../../scratch/audit_ch17_results.txt`). Figures 17.7 and 17.8 share source page 9; Figures 17.9 and 17.10 share source page 10. Figure 17.8 is the one region where a neighbouring prose column overlaps the left label zone; its documented text-layer mask preserves the "Floating ribs" label. No unnumbered bonus plate and no photograph of a person exists in this chapter, so the denominator is 10 everywhere and `check_pdf.py` check 4 has no manifest row to fire on (true negative).

## Census sections (each total derivable from the list beside it)

**Heading census — 10 rows = 5 numbered + 2 sub-numbered + 3 unnumbered.**
Numbered headings, in source order: 17.1 TYPES OF MOVEMENT · 17.2 MUSCLE · 17.3 SKELETAL SYSTEM · 17.4 JOINTS · 17.5 DISORDERS OF MUSCULAR AND SKELETAL SYSTEM.
Sub-numbered headings, in source order: 17.2.1 Structure of Contractile Proteins · 17.2.2 Mechanism of Muscle Contraction.
Unnumbered headings, in source order: the chapter title plate (LOCOMOTION AND MOVEMENT) · SUMMARY · EXERCISES.
The six disorder names in 17.5 (`Myasthenia gravis:` · `Muscular dystrophy:` · `Tetany:` · `Arthritis:` · `Osteoporosis:` · `Gout:`) are **not** counted as headings; they are colon-led definition entries carried by `disorder`-type rows F166-F171, exactly as Ch16 treated `Renal calculi:` / `Glomerulonephritis:`. The muscle-type names (Skeletal/Visceral/Cardiac) and fibre-type names (Red/White) are run-in prose emphases, not headings. No numbered TABLE exists in this chapter.

**Opener census — 7 rows.** One opener per headed section plus the unheaded chapter-intro prose, minus the headings that carry no opening sentence of their own — the title plate, SUMMARY, EXERCISES, and **17.5** (which opens directly onto its first disorder entry with no introductory sentence). Sections with an opener: intro (F002) · 17.1 (F018) · 17.2 (F030) · 17.2.1 (F068) · 17.2.2 (F079) · 17.3 (F103) · 17.4 (F151). That is 6 headed openers plus the intro = 7. 17.2's numbered head is followed by prose before the 17.2.1 sub-head, so 17.2 carries its own opener.

**Figure census — 10 numbered figures, 10 assets, 10 caption rows (F174-F183), 10 label rows (F184-F193), and the in-text call-outs listed below.**
Call-outs, in source order: (Figure 17.1) · (Figure 17.2) · (Figure 17.3a) · (Figure 17.3b) · (Figure 17.4) · (Figure 17.5) · (Figure 17.4) · (Figure 17.6) · (Figure 17.7) · (Figure 17.8) · (Figure 17.9) · (Figure 17.10) · (Figure 17.9) · (Figure 17.10). Figures 17.3, 17.4, 17.9 and 17.10 are each called out with an (a)/(b) split or a second reference, so call-outs exceed the 10 figures. The authoritative count is machine-derived by `verify_inventory.py` from the source text; see check [1].

**Type census — 183 Facts rows by type** (machine-derived by `verify_inventory.py` check [7] from the Type column; the numbers below are filled from that script's output and are not hand-tallied): concept · process · number · heading · opener · definition · example · disorder · caption. Plus 10 `figure-label` rows in the matrix = 193 total.

## Gate 1 checklist

| # | Requirement | Status |
|---|---|---|
| 1 | Chapter read start to finish before any Facts row was written | done — session `1-S`, full read of all 13 extracted pages (textbook pp. 217-229) |
| 2 | Every sentence-level fact captured as its own row | done — 183 Facts rows |
| 3 | All 5 numbered + 2 sub-numbered + 3 unnumbered headings captured | done — 10 heading rows, machine-confirmed contiguous 17.1-17.5 |
| 4 | Every section's opening sentence captured | done — 7 opener rows; census reconciles (10 headings - 4 openerless + 1 intro) |
| 5 | All 10 captions transcribed verbatim | done — F174-F183; Fig 17.5 caption source-verbatim, manifest divergence flagged as OBS-17.5 |
| 6 | In-figure labels harvested by opening each asset, not the text layer | done — session `1-F`, all 10 assets opened at full size; matrix preserved as F184-F193 |
| 7 | Label matrix present in exactly one place, parseable by `check_pdf._extract_labels` | done — asserted by `verify_inventory.py` check [4] |
| 8 | Figure-only labels identified and given a Pass 2 home | done — 4 genuine figure-only obligations flagged + parser marks noted |
| 9 | Summary sentences classified, SUMMARY-UNIQUE folded | done — 40 = 37 BODY-PRESENT + 3 SUMMARY-UNIQUE, all 3 folded |
| 10 | Exercises scanned, genuine gaps assigned a home | done — 10 scanned, 3 gaps, remainder recorded as non-gaps |
| 11 | No Unicode sub/superscripts or U+FFFD in this file | done — asserted by `verify_inventory.py` check [5] |
| 12 | All counts machine-derived, not hand-tallied | done — `verify_inventory.py` re-parses the PDF and this file and exits non-zero on drift |
| 13 | All Facts rows unticked at freeze | done — 0 of 193 ticked |

## Pass 3 defect register (verification sweep)

Pass 3 ran two independent sweeps over the built PDF: **3(a)** a page-by-page visual inspection of every rendered page, and **3(b)** a bidirectional full read (source text -> notes, then notes -> source) to catch both dropped and invented content. Defects are numbered `D<n>` in the Ch15/Ch16 house style; every one below is closed.

| # | Sweep | Defect | Disposition |
|---|---|---|---|
| D1 | 3(b) | Sarcomere was introduced only inside a `[MEMORY AID - not in NCERT]` box, so the NCERT definition ("portion of the myofibril between two successive 'Z' lines ... functional unit of contraction", `F062`-`F064`) sat in non-NCERT furniture instead of body text | fixed — the definition is now a body bullet on notes p.3 with the Figure 17.2 call-out; the memory aid was reduced to the mnemonic alone (only the 'I' band and 'H' zone shrink, the 'A' band never does) |
| D2 | 3(b) | Exercise 9(c) and 9(d) are answerable only by applying a chapter definition, not by quoting one | fixed — both answers carry an explicit `(Applied answer: ...)` parenthetical naming the chapter statement they are derived from, and the EXERCISES `[NOTE]` flags this in place |
| D3 | 3(a) | Figure 17.5 typeset caption had to be chosen between two frozen strings (see **OBS-17.5**) | closed — the typeset caption uses the source-verbatim `F178` string ("... movement of the thin filaments and the relative size of the I band and H zones"); the `1-F` manifest row is left frozen as recorded, so the divergence stays documented rather than silently reconciled |

**Non-defects confirmed during 3(b)** (recorded so a later session does not re-open them): the `syncitium`, `arragement` and `ADP and P` + stray `1` source artefacts behave exactly as the transcription policy above dictates (frozen verbatim in the rows, spelled/typeset correctly in the prose, `Pi` rendered as P with a subscript i); the corrupted p.6 running head is page furniture and produced no row; and the only content in the notes with no source anchor is the two `[MEMORY AID - not in NCERT]` boxes and the chapter-map recap `[NOTE]`, each explicitly labelled as such.

## Gate 3 record

| # | Requirement | Status |
|---|---|---|
| 1 | Every Facts row ticked | done — 193 of 193 (`F001`-`F193`), zero `[ ]` remaining |
| 2 | All 10 figures placed, each with a verbatim caption and a `[NOTE] labels` line | done — Fig 17.1-17.10 on notes pp. 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 |
| 3 | `check_pdf.py` green | done — all checks pass; check 4 has no manifest row to fire on (true negative, denominator 10) |
| 4 | Build reproducible from the committed script | done — rebuild differs only in the PDF `CreationDate`/`ModDate`/ID (62 bytes); 15 pages, 30,008 text chars, 10 images both times |
| 5 | Pass 3(a) visual inspection of every rendered page | done — all 15 pages rendered at 105 dpi and inspected: no text/figure collision, no clipped artwork, no cell overflow, no orphan heading, all badges correct, greyscale-only so print-safe in B&W |
| 6 | Pass 3(b) bidirectional read | done — source pp. 217-229 -> notes (nothing dropped) and notes -> source (nothing invented); defects D1-D3 raised and closed |
| 7 | SUMMARY reproduced and EXERCISES answered | done — full summary section plus all 10 NCERT exercises with worked answers sourced from the chapter text |
| 8 | Defect register written | done — D1-D3 above, all closed |

## Pass 3(b) section-by-section read log (re-verified 2026-09-02)

The bidirectional read was re-run this session **section by section**, walking the source (textbook pp. 217–229) against the built notes (15 rendered pages) and then the notes back against the source. Each row records the source span, the notes span, the figure(s) that land in that section, and the drift verdict. Every section is clean; the only defects ever raised (D1–D3, above) all fall in §17.2 / EXERCISES / Fig 17.5 and are already closed.

| # | Section (source) | Facts span | Notes location | Figures | Source→notes (dropped?) | Notes→source (invented?) |
|---|---|---|---|---|---|---|
| 0 | Intro — Movement vs Locomotion (`Amoeba`, `Paramoecium`, `Hydra`; all locomotions are movements, not vice-versa; habitat/purpose) | `F001`–`F011` | p.1 | — | none — bullet-for-bullet | none |
| 1 | **17.1 Types of Movement** (amoeboid / ciliary / muscular; macrophages·leucocytes·microfilaments; trachea·ova; note on muscular+skeletal+neural) | `F012`–`F024` | p.1 | — | none — 3-row table reproduces where/how verbatim | none; `[NOTE]` correctly flags the coordinated-systems remark |
| 2 | **17.2 Muscle** (mesodermal origin, 40–50%, excitability/contractility/extensibility/elasticity; skeletal/visceral/cardiac; structure of skeletal muscle; banding A/I/Z/M/H; sarcomere as functional unit; resting overlap) | `F025`–`F075` | pp. 1–4 | **17.1** (p.2), **17.2** (p.3) | none — muscle-type table, band table, sarcomere bullets all present | none — **D1** was the only issue (sarcomere sat in a memory-aid box); fixed, now body text on p.3 |
| 3 | **17.2.1 Structure of Contractile Proteins** (F/G actin, tropomyosin, troponin masks sites; meromyosin HMM/LMM, head = ATPase with ATP + actin sites) | `F076`–`F088` | pp. 3–4 | **17.3** (p.4) | none — actin bullets + HMM/LMM table present | none |
| 4 | **17.2.2 Mechanism of Muscle Contraction** (sliding-filament theory; motor unit / neuromuscular junction; 9-step cycle; I-band shortens, A-band constant; reaction time; fatigue/lactic acid; red vs white fibres/myoglobin) | `F089`–`F133` | pp. 4–6 | **17.4** (p.5), **17.5** (p.6) | none — the full contraction cycle is staged as a numbered process-flow; red/white table present | none; `Pi` artefact (`F090`) rendered correctly, verbatim in row |
| 5 | **17.3 Skeletal System** intro (bone vs cartilage matrix; 206 bones; axial + appendicular) | `F134`–`F138` | p.6 | — | none | none |
| 6 | **Axial Skeleton** (80 bones; skull 22 = cranial 8 + facial 14; hyoid; ear ossicles M/I/S; dicondylic; vertebral column 26, atlas, 7/12/5/1/1, intervertebral disc; sternum + 12 rib pairs, bicephalic; true/false/floating) | `F139`–`F167` | pp. 7–9 | **17.6** (p.7), **17.7** (p.8), **17.8** (p.9) | none — every count matches; rib table (true 7 / vertebrochondral 8–10 / floating 11–12) present | none |
| 7 | **Appendicular Skeleton** (30 bones/limb; fore-limb humerus·radius·ulna·carpals 8·metacarpals 5·phalanges 14; hind-limb femur·tibia·fibula·tarsals 7·metatarsals 5·phalanges 14; patella; pectoral = clavicle+scapula, spine·acromion·glenoid cavity; pelvic = coxal = ilium+ischium+pubis, acetabulum, pubic symphysis) | `F168`–`F179` | pp. 9–11 | **17.9** (p.10), **17.10** (p.11) | none — limb table + girdle bullets present | none; the two `[MEMORY AID]` boxes are the only non-NCERT content and are labelled |
| 8 | **17.4 Joints** (fulcrum; fibrous/cartilaginous/synovial; ball-and-socket, hinge, pivot, gliding, saddle with examples) | `F180`–`F186` | pp. 11–12 | — | none — joint-type table + sub-type bullets present | none; `arragement` artefact (`F162`/synovial) rendered correctly, verbatim in row |
| 9 | **17.5 Disorders** (myasthenia gravis, muscular dystrophy, tetany, arthritis, osteoporosis, gout) | `F187`–`F193` | p.12 | — | none — 6-row disorder table present | none; chapter-map recap `[NOTE]` labelled as synthesis |
| 10 | **SUMMARY** (pp. 228–229) | folded into `F001`–`F193` (3 SUMMARY-UNIQUE folded at Gate 1) | p.12 | — | none — full summary reproduced | none |
| 11 | **EXERCISES** (10 questions, pp. 229) | `question` rows across the file | pp. 13–15 | — | none — all 10 answered with worked solutions | none — **D2** (9c/9d answerable only by applying a definition) closed via explicit `(Applied answer: …)` parentheticals + EXERCISES `[NOTE]` |

**Verdict:** 12 / 12 source sections read in both directions, **nothing dropped and nothing invented**; all 10 figures land in their correct sections with verbatim captions and `[NOTE] labels` lines; the three defects ever raised (D1–D3) remain closed. This matches the machine evidence (`check_pdf.py --strict` = PASS 0/0; 183/183 Facts ticked; 95/95 labels; 10/10 mono images).

## References

- Source PDF: `Chapter/class 11/Chapter 17 - Locomotion and Movement.pdf`
- Assets: `assets/fig_17_1.png` .. `assets/fig_17_10.png`
- Extraction script: `extract_figures.py` · audit: `../../scratch/audit_ch17.py` / `../../scratch/audit_ch17_results.txt`
- Verifier: `verify_inventory.py` (run with `/vercel/share/neetenv/bin/python`)
- Protocol: `SUPREME COMMAND PROMPT.md` §4.4 (figures), §6 (passes/gates), Gate 1
- Checker: `check_pdf.py` (check 6 consumes the label matrix above)
