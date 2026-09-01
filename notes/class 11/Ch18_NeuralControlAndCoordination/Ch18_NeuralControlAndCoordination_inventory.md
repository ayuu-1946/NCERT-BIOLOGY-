# Frozen Inventory — Neural Control and Coordination (Chapter 18, Class 11)

**Source PDF:** `Chapter/class 11/Chapter 18 - Neural Control and Coordination.pdf` (9 extracted pages; textbook pp. 230-238)
**Class:** 11 · **Chapter:** 18
**Figure assets:** 4 (`assets/fig_18_1.png` .. `assets/fig_18_4.png`)
**Gate 1 frozen:** 2026-09-01
**Facts rows:** 131 (F001-F131) · **Figure-label matrix rows:** 4 (F132-F135) · **Total:** 135

This is the **full Pass 1 inventory** and the Gate 1 deliverable. It supersedes the earlier figures-only freeze that lived in this same file (session `1-F`, frozen 2026-08-30), whose figure-label matrix, captions, manifest and audit trail are preserved **verbatim** below — only their row IDs were shifted to the end of the ID space (was `F001`-`F004`, now `F132`-`F135`) so the Facts table can occupy a contiguous `F001`-`F131` in source order, matching the Ch15/Ch16/Ch17 house format. No asset, label string, or manifest entry was re-extracted or reworded by this session; figure extraction was already complete and verified. The earlier freeze explicitly declared itself extraction-only and declared Pass 1 running-text work out of scope, so this file is the first Pass 1 freeze of the chapter's Facts table.

## Session log (Pass 1)

| Session | Sweep | Outcome |
|---|---|---|
| `1-F` | Figure extraction, monochrome conversion, per-asset label harvest | done earlier (2026-08-30) — 4 assets, 4 captions, label matrix (preserved as F132-F135) |
| `1-S` | Full source read, start to finish, before any Facts row was written | done this session — all 9 extracted pages read (textbook pp. 230-238); pp. 1, 2, 7, 8, 9 additionally opened as rendered images to reconcile the figure census against the artwork |
| `1-H` | Heading sweep | done — 12 heading rows (1 title plate + 4 numbered + 5 sub-numbered + 2 unnumbered) |
| `1-O` | Opener sweep | done — 10 opener rows (chapter intro + 9 headed sections that carry an opening sentence) |
| `1-Z` | Summary + exercise-gap sweep | done — 18 summary sentences classified; 10 exercises scanned |

## Figure census reconciliation (why 4 is the whole census)

The chapter draws **4 numbered figures**, on extracted pp. 3-6 (textbook pp. 232-235). To rule out unnumbered plates, every page that carries no numbered figure was rendered and opened: p.1 (title page — the only graphic is the NCERT **QR code**, page furniture), p.2, p.7 (all-prose), p.8 (SUMMARY + first three EXERCISES) and p.9 (rest of EXERCISES). None carries artwork. The `get_images()` counts on those pages are page-template raster furniture (header/footer bands, QR code), not figures. So: 4 figures = 4 assets = 4 caption rows = 4 label rows, with no unnumbered plate anywhere in the chapter.

## Source-typo / transcription policy (recorded so frozen rows are never silently "corrected")

Each deviation is transcribed **exactly as the source draws it** in the Facts row and flagged here; the downstream rewrite prose may legitimately spell them correctly.

- **`passess`** — p.7 (textbook p.236), carried by `F116`. The source misspells "passes" ("A canal called the cerebral aqueduct passess through the midbrain"). Row stands verbatim.
- **`sagital`** — p.6 (textbook p.235), the Figure 18.4 caption, carried by `F131`. The source draws "sagital"; the conventional spelling is "sagittal". `F131` transcribes the source. See the caption-discrepancy section below — the frozen `1-F` manifest row records the normalised "sagittal" and is **not** reworded.
- **`Schwan cell`** — artwork label inside Figure 18.1, carried by `F132`. The plate draws "Schwan cell" while the body prose (F042, F045) says "Schwann cell(s)". The label row preserves the artwork spelling exactly as the `1-F` session harvested it from the opened PNG.
- **`spiral cord`** — p.8 (textbook p.237), SUMMARY box: "The CNS consists of the brain and spiral cord." The source means "spinal". This lives in the summary-classification table, not in a Facts row, and is quoted there verbatim.
- **Exercise 10 lettering skips `(c)`-`(e)`** — p.9 (textbook p.238). Exercise 10 is lettered `(a)`, `(b)`, then `(f)`. A source numbering defect, recorded in the exercise-gap section; not a missing fact.
- **Figure 18.2 charge-mark scatter** — p.4's text layer emits long runs of bare `-` and `+` glyphs plus the tokens `A`, `Na`, `B` between the prose and the caption. These are the polarity marks and markers drawn **inside** the plate, harvested as label vocabulary in `F133`, not sentence facts. No row is created from them.
- **Stray `Forebrain` token after the Figure 18.4 caption** — p.6's text layer emits `Forebrain` on its own line below the caption. It is the plate's bracket label (`F135`), not a heading and not a sentence.
- **Chapter-opening contents rail** — the p.1 rail (`18.1 Neural System` … `18.4  Central Neural System`, the last one printed with a double space) and the vertical title `NEURAL CONTROL AND COORDINATION` interleave with the intro prose in the p.1 text layer. Deduplicated by reading, not by string-splitting; the rail is captured once as the chapter's section list, not as four separate heading rows — the ALLCAPS body headings are the authoritative heading rows.
- **Superscript charges** — the source sets `K`/`Na` charges as superscripts, which the extractor emits inconsistently (`K\n+`, `(K+)`, `Na+`). All rows transcribe them as ASCII `K+` / `Na+` per the encoding rule (no Unicode super/subscripts anywhere in this file).

## Facts table

One row per sentence-level fact, in source order. Types: `heading` · `opener` · `concept` · `process` · `number` · `definition` · `example` · `prompt` · `caption`. `prompt` is used for the source's three second-person rhetorical set-ups (F048, F058, F082); they are not disposable page furniture — each one announces the mechanism that follows and is retained so Pass 2 cannot silently drop the source's framing. Every Facts row is **unticked** at Gate 1 freeze (Pass 2 ticks them); the preserved figure-label rows (F132-F135) keep the `x` the `1-F` session earned by opening each rendered PNG. Apostrophes are transcribed with straight ASCII quotes in the Facts rows (`Nissl's`, `'command and control system'`); the figure-label matrix preserves the curly apostrophe exactly as `1-F` recorded it from the artwork.

| ID | Section | Type | Exact original wording | Ticked |
|---|---|---|---|---|
| F001 | Title plate | heading | CHAPTER 18 — NEURAL CONTROL AND COORDINATION |  |
| F002 | Intro | opener | As you know, the functions of the organs/organ systems in our body must be coordinated to maintain homeostasis. |  |
| F003 | Intro | definition | Coordination is the process through which two or more organs interact and complement the functions of one another. |  |
| F004 | Intro | example | For example, when we do physical exercises, the energy demand is increased for maintaining an increased muscular activity. |  |
| F005 | Intro | example | The supply of oxygen is also increased. |  |
| F006 | Intro | process | The increased supply of oxygen necessitates an increase in the rate of respiration, heart beat and increased blood flow via blood vessels. |  |
| F007 | Intro | process | When physical exercise is stopped, the activities of nerves, lungs, heart and kidney gradually return to their normal conditions. |  |
| F008 | Intro | concept | Thus, the functions of muscles, lungs, heart, blood vessels, kidney and other organs are coordinated while performing physical exercises. |  |
| F009 | Intro | concept | In our body the neural system and the endocrine system jointly coordinate and integrate all the activities of the organs so that they function in a synchronised fashion. |  |
| F010 | Intro | concept | The neural system provides an organised network of point-to-point connections for a quick coordination. |  |
| F011 | Intro | concept | The endocrine system provides chemical integration through hormones. |  |
| F012 | Intro | concept | In this chapter, you will learn about the neural system of human, mechanisms of neural coordination like transmission of nerve impulse and impulse conduction across a synapse. |  |
| F013 | 18.1 | heading | 18.1 NEURAL SYSTEM |  |
| F014 | 18.1 | opener | The neural system of all animals is composed of highly specialised cells called neurons which can detect, receive and transmit different kinds of stimuli. |  |
| F015 | 18.1 | concept | The neural organisation is very simple in lower invertebrates. |  |
| F016 | 18.1 | example | For example, in Hydra it is composed of a network of neurons. |  |
| F017 | 18.1 | example | The neural system is better organised in insects, where a brain is present along with a number of ganglia and neural tissues. |  |
| F018 | 18.1 | concept | The vertebrates have a more developed neural system. |  |
| F019 | 18.2 | heading | 18.2 HUMAN NEURAL SYSTEM |  |
| F020 | 18.2 | opener | The human neural system is divided into two parts : (i) the central neural system (CNS) (ii) the peripheral neural system (PNS) |  |
| F021 | 18.2 | concept | The CNS includes the brain and the spinal cord and is the site of information processing and control. |  |
| F022 | 18.2 | definition | The PNS comprises of all the nerves of the body associated with the CNS (brain and spinal cord). |  |
| F023 | 18.2 | concept | The nerve fibres of the PNS are of two types : (a) afferent fibres (b) efferent fibres |  |
| F024 | 18.2 | definition | The afferent nerve fibres transmit impulses from tissues/organs to the CNS and the efferent fibres transmit regulatory impulses from the CNS to the concerned peripheral tissues/organs. |  |
| F025 | 18.2 | concept | The PNS is divided into two divisions called somatic neural system and autonomic neural system. |  |
| F026 | 18.2 | definition | The somatic neural system relays impulses from the CNS to skeletal muscles while the autonomic neural system transmits impulses from the CNS to the involuntary organs and smooth muscles of the body. |  |
| F027 | 18.2 | concept | The autonomic neural system is further classified into sympathetic neural system and parasympathetic neural system. |  |
| F028 | 18.2 | definition | Visceral nervous system is the part of the peripheral nervous system that comprises the whole complex of nerves, fibres, ganglia, and plexuses by which impulses travel from the central nervous system to the viscera and from the viscera to the central nervous system. |  |
| F029 | 18.3 | heading | 18.3 NEURON AS STRUCTURAL AND FUNCTIONAL UNIT OF NEURAL SYSTEM |  |
| F030 | 18.3 | opener | A neuron is a microscopic structure composed of three major parts, namely, cell body, dendrites and axon (Figure 18.1). |  |
| F031 | 18.3 | concept | The cell body contains cytoplasm with typical cell organelles and certain granular bodies called Nissl's granules. |  |
| F032 | 18.3 | definition | Short fibres which branch repeatedly and project out of the cell body also contain Nissl's granules and are called dendrites. |  |
| F033 | 18.3 | process | These fibres transmit impulses towards the cell body. |  |
| F034 | 18.3 | concept | The axon is a long fibre, the distal end of which is branched. |  |
| F035 | 18.3 | definition | Each branch terminates as a bulb-like structure called synaptic knob which possess synaptic vesicles containing chemicals called neurotransmitters. |  |
| F036 | 18.3 | process | The axons transmit nerve impulses away from the cell body to a synapse or to a neuro-muscular junction. |  |
| F037 | 18.3 | concept | Based on the number of axon and dendrites, the neurons are divided into three types, i.e., multipolar, bipolar and unipolar. |  |
| F038 | 18.3 | definition | multipolar (with one axon and two or more dendrites; found in the cerebral cortex) |  |
| F039 | 18.3 | definition | bipolar (with one axon and one dendrite, found in the retina of eye) |  |
| F040 | 18.3 | definition | unipolar (cell body with one axon only; found usually in the embryonic stage) |  |
| F041 | 18.3 | concept | There are two types of axons, namely, myelinated and non-myelinated. |  |
| F042 | 18.3 | concept | The myelinated nerve fibres are enveloped with Schwann cells, which form a myelin sheath around the axon. |  |
| F043 | 18.3 | definition | The gaps between two adjacent myelin sheaths are called nodes of Ranvier. |  |
| F044 | 18.3 | concept | Myelinated nerve fibres are found in spinal and cranial nerves. |  |
| F045 | 18.3 | concept | Unmyelinated nerve fibre is enclosed by a Schwann cell that does not form a myelin sheath around the axon, and is commonly found in autonomous and the somatic neural systems. |  |
| F046 | 18.3.1 | heading | 18.3.1 Generation and Conduction of Nerve Impulse |  |
| F047 | 18.3.1 | opener | Neurons are excitable cells because their membranes are in a polarised state. |  |
| F048 | 18.3.1 | prompt | Do you know why the membrane of a neuron is polarised? |  |
| F049 | 18.3.1 | concept | Different types of ion channels are present on the neural membrane. |  |
| F050 | 18.3.1 | concept | These ion channels are selectively permeable to different ions. |  |
| F051 | 18.3.1 | process | When a neuron is not conducting any impulse, i.e., resting, the axonal membrane is comparatively more permeable to potassium ions (K+) and nearly impermeable to sodium ions (Na+). |  |
| F052 | 18.3.1 | concept | Similarly, the membrane is impermeable to negatively charged proteins present in the axoplasm. |  |
| F053 | 18.3.1 | concept | Consequently, the axoplasm inside the axon contains high concentration of K+ and negatively charged proteins and low concentration of Na+. |  |
| F054 | 18.3.1 | concept | In contrast, the fluid outside the axon contains a low concentration of K+, a high concentration of Na+ and thus form a concentration gradient. |  |
| F055 | 18.3.1 | number | These ionic gradients across the resting membrane are maintained by the active transport of ions by the sodium-potassium pump which transports 3 Na+ outwards for 2 K+ into the cell. |  |
| F056 | 18.3.1 | process | As a result, the outer surface of the axonal membrane possesses a positive charge while its inner surface becomes negatively charged and, therefore is, polarised. |  |
| F057 | 18.3.1 | definition | The electrical potential difference across the resting plasma membrane is called as the resting potential. |  |
| F058 | 18.3.1 | prompt | You might be curious to know about the mechanisms of generation of nerve impulse and its conduction along an axon. |  |
| F059 | 18.3.1 | process | When a stimulus is applied at a site (Figure 18.2 e.g., point A) on the polarised membrane, the membrane at the site A becomes freely permeable to Na+. |  |
| F060 | 18.3.1 | process | This leads to a rapid influx of Na+ followed by the reversal of the polarity at that site, i.e., the outer surface of the membrane becomes negatively charged and the inner side becomes positively charged. |  |
| F061 | 18.3.1 | process | The polarity of the membrane at the site A is thus reversed and hence depolarised. |  |
| F062 | 18.3.1 | definition | The electrical potential difference across the plasma membrane at the site A is called the action potential, which is in fact termed as a nerve impulse. |  |
| F063 | 18.3.1 | concept | At sites immediately ahead, the axon (e.g., site B) membrane has a positive charge on the outer surface and a negative charge on its inner surface. |  |
| F064 | 18.3.1 | process | As a result, a current flows on the inner surface from site A to site B. |  |
| F065 | 18.3.1 | process | On the outer surface current flows from site B to site A (Figure 18.2) to complete the circuit of current flow. |  |
| F066 | 18.3.1 | process | Hence, the polarity at the site is reversed, and an action potential is generated at site B. |  |
| F067 | 18.3.1 | process | Thus, the impulse (action potential) generated at site A arrives at site B. |  |
| F068 | 18.3.1 | process | The sequence is repeated along the length of the axon and consequently the impulse is conducted. |  |
| F069 | 18.3.1 | concept | The rise in the stimulus-induced permeability to Na+ is extremely short-lived. |  |
| F070 | 18.3.1 | process | It is quickly followed by a rise in permeability to K+. |  |
| F071 | 18.3.1 | process | Within a fraction of a second, K+ diffuses outside the membrane and restores the resting potential of the membrane at the site of excitation and the fibre becomes once more responsive to further stimulation. |  |
| F072 | 18.3.2 | heading | 18.3.2 Transmission of Impulses |  |
| F073 | 18.3.2 | opener | A nerve impulse is transmitted from one neuron to another through junctions called synapses. |  |
| F074 | 18.3.2 | definition | A synapse is formed by the membranes of a pre-synaptic neuron and a post-synaptic neuron, which may or may not be separated by a gap called synaptic cleft. |  |
| F075 | 18.3.2 | concept | There are two types of synapses, namely, electrical synapses and chemical synapses. |  |
| F076 | 18.3.2 | concept | At electrical synapses, the membranes of pre- and post-synaptic neurons are in very close proximity. |  |
| F077 | 18.3.2 | process | Electrical current can flow directly from one neuron into the other across these synapses. |  |
| F078 | 18.3.2 | concept | Transmission of an impulse across electrical synapses is very similar to impulse conduction along a single axon. |  |
| F079 | 18.3.2 | concept | Impulse transmission across an electrical synapse is always faster than that across a chemical synapse. |  |
| F080 | 18.3.2 | concept | Electrical synapses are rare in our system. |  |
| F081 | 18.3.2 | definition | At a chemical synapse, the membranes of the pre- and post-synaptic neurons are separated by a fluid-filled space called synaptic cleft (Figure 18.3). |  |
| F082 | 18.3.2 | prompt | Do you know how the pre-synaptic neuron transmits an impulse (action potential) across the synaptic cleft to the post-synaptic neuron? |  |
| F083 | 18.3.2 | concept | Chemicals called neurotransmitters are involved in the transmission of impulses at these synapses. |  |
| F084 | 18.3.2 | concept | The axon terminals contain vesicles filled with these neurotransmitters. |  |
| F085 | 18.3.2 | process | When an impulse (action potential) arrives at the axon terminal, it stimulates the movement of the synaptic vesicles towards the membrane where they fuse with the plasma membrane and release their neurotransmitters in the synaptic cleft. |  |
| F086 | 18.3.2 | process | The released neurotransmitters bind to their specific receptors, present on the post-synaptic membrane. |  |
| F087 | 18.3.2 | process | This binding opens ion channels allowing the entry of ions which can generate a new potential in the post-synaptic neuron. |  |
| F088 | 18.3.2 | concept | The new potential developed may be either excitatory or inhibitory. |  |
| F089 | 18.4 | heading | 18.4 CENTRAL NEURAL SYSTEM |  |
| F090 | 18.4 | opener | The brain is the central information processing organ of our body, and acts as the 'command and control system'. |  |
| F091 | 18.4 | concept | It controls the voluntary movements, balance of the body, functioning of vital involuntary organs (e.g., lungs, heart, kidneys, etc.), thermoregulation, hunger and thirst, circadian (24-hour) rhythms of our body, activities of several endocrine glands and human behaviour. |  |
| F092 | 18.4 | concept | It is also the site for processing of vision, hearing, speech, memory, intelligence, emotions and thoughts. |  |
| F093 | 18.4 | concept | The human brain is well protected by the skull. |  |
| F094 | 18.4 | concept | Inside the skull, the brain is covered by cranial meninges consisting of an outer layer called dura mater, a very thin middle layer called arachnoid and an inner layer (which is in contact with the brain tissue) called pia mater. |  |
| F095 | 18.4 | concept | The brain can be divided into three major parts: (i) forebrain, (ii) midbrain, and (iii) hindbrain (Figure 18.4). |  |
| F096 | 18.4.1 | heading | 18.4.1 Forebrain |  |
| F097 | 18.4.1 | opener | The forebrain consists of cerebrum, thalamus and hypothalamus (Figure 18.4). |  |
| F098 | 18.4.1 | concept | Cerebrum forms the major part of the human brain. |  |
| F099 | 18.4.1 | concept | A deep cleft divides the cerebrum longitudinally into two halves, which are termed as the left and right cerebral hemispheres. |  |
| F100 | 18.4.1 | definition | The hemispheres are connected by a tract of nerve fibres called corpus callosum. |  |
| F101 | 18.4.1 | definition | The layer of cells which covers the cerebral hemisphere is called cerebral cortex and is thrown into prominent folds. |  |
| F102 | 18.4.1 | definition | The cerebral cortex is referred to as the grey matter due to its greyish appearance. |  |
| F103 | 18.4.1 | concept | The neuron cell bodies are concentrated here giving the colour. |  |
| F104 | 18.4.1 | concept | The cerebral cortex contains motor areas, sensory areas and large regions that are neither clearly sensory nor motor in function. |  |
| F105 | 18.4.1 | definition | These regions called as the association areas are responsible for complex functions like intersensory associations, memory and communication. |  |
| F106 | 18.4.1 | concept | Fibres of the tracts are covered with the myelin sheath, which constitute the inner part of cerebral hemisphere. |  |
| F107 | 18.4.1 | definition | They give an opaque white appearance to the layer and, hence, is called the white matter. |  |
| F108 | 18.4.1 | concept | The cerebrum wraps around a structure called thalamus, which is a major coordinating centre for sensory and motor signaling. |  |
| F109 | 18.4.1 | concept | Another very important part of the brain called hypothalamus lies at the base of the thalamus. |  |
| F110 | 18.4.1 | concept | The hypothalamus contains a number of centres which control body temperature, urge for eating and drinking. |  |
| F111 | 18.4.1 | concept | It also contains several groups of neurosecretory cells, which secrete hormones called hypothalamic hormones. |  |
| F112 | 18.4.1 | definition | The inner parts of cerebral hemispheres and a group of associated deep structures like amygdala, hippocampus, etc., form a complex structure called the limbic lobe or limbic system. |  |
| F113 | 18.4.1 | concept | Along with the hypothalamus, it is involved in the regulation of sexual behaviour, expression of emotional reactions (e.g., excitement, pleasure, rage and fear), and motivation. |  |
| F114 | 18.4.2 | heading | 18.4.2 Midbrain |  |
| F115 | 18.4.2 | opener | The midbrain is located between the thalamus/hypothalamus of the forebrain and pons of the hindbrain. |  |
| F116 | 18.4.2 | concept | A canal called the cerebral aqueduct passess through the midbrain. |  |
| F117 | 18.4.2 | number | The dorsal portion of the midbrain consists mainly of four round swellings (lobes) called corpora quadrigemina. |  |
| F118 | 18.4.3 | heading | 18.4.3 Hindbrain |  |
| F119 | 18.4.3 | opener | The hindbrain comprises pons, cerebellum and medulla (also called the medulla oblongata). |  |
| F120 | 18.4.3 | concept | Pons consists of fibre tracts that interconnect different regions of the brain. |  |
| F121 | 18.4.3 | concept | Cerebellum has very convoluted surface in order to provide the additional space for many more neurons. |  |
| F122 | 18.4.3 | concept | The medulla of the brain is connected to the spinal cord. |  |
| F123 | 18.4.3 | concept | The medulla contains centres which control respiration, cardiovascular reflexes and gastric secretions. |  |
| F124 | 18.4.3 | concept | Three major regions make up the brain stem; mid brain, pons and medulla oblongata. |  |
| F125 | 18.4.3 | concept | Brain stem forms the connections between the brain and spinal cord. |  |
| F126 | SUMMARY | heading | SUMMARY |  |
| F127 | EXERCISES | heading | EXERCISES |  |
| F128 | Fig 18.1 | caption | Figure 18.1 Structure of a neuron |  |
| F129 | Fig 18.2 | caption | Figure 18.2 Diagrammatic representation of impulse conduction through an axon (at points A and B) |  |
| F130 | Fig 18.3 | caption | Figure 18.3 Diagram showing axon terminal and synapse |  |
| F131 | Fig 18.4 | caption | Figure 18.4 Diagram showing sagital section of the human brain |  |

### Caption discrepancy against the frozen `1-F` figure manifest (recorded, not silently reconciled)

The `1-F` manifest row for Figure 18.4 records the caption as **"Diagram showing sagittal section of the human brain"**. The source draws **"sagital"** (one `t`). Both extractors return `sagital`. The manifest row is a frozen `1-F` deliverable and is **not** reworded here; the Pass 1 caption row `F131` carries the source-verbatim `sagital`, and any built PDF must print the source-verbatim string, which the caption check in `verify_inventory.py` enforces. The three other captions match the manifest character-for-character.

## Figure-label matrix

Preserved **verbatim** from the `1-F` freeze (was `F001`-`F004`). The matrix exists in exactly one place — this table — and each row's wording column begins with `Figure labels:`, matching the `_extract_labels` parser in `check_pdf.py`. Labels were harvested by opening each final rendered PNG, not from PDF text extraction. The repeated `Na` marking in Figure 18.2 is one label wording occurring at two positions in the plate; it is represented once because the matrix audits label vocabulary, not repeated spatial occurrences. There is no second pipe-delimited label table anywhere in this file, so no label is double-counted and no phantom separator row is created.

| ID | Section | Type | Exact original wording | Ticked |
|---|---|---|---|---|
| F132 | Fig 18.1 | figure-label | Figure labels: "Dendrites"; "Nissl’s granules"; "Cell body"; "Nucleus"; "Schwan cell"; "Axon"; "Myelin sheath"; "Node of Ranvier"; "Axon terminal"; "Synaptic knob" | x |
| F133 | Fig 18.2 | figure-label | Figure labels: "A"; "Na"; "B" | x |
| F134 | Fig 18.3 | figure-label | Figure labels: "Axon"; "Axon terminal"; "Synaptic vesicles"; "Pre-synaptic membrane"; "Synaptic cleft"; "Post-synaptic membrane"; "Receptors"; "Neurotransmitters"; "Synapse" | x |
| F135 | Fig 18.4 | figure-label | Figure labels: "Forebrain"; "Cerebrum"; "Cerebral hemisphere"; "Corpus callosum"; "Thalamus"; "Hypothalamus"; "Midbrain"; "Hindbrain"; "Pons"; "Cerebellum"; "Medulla"; "Spinal cord"; "Cerebral aqueduct" | x |

**Label total: 35** (10 + 3 + 9 + 13).

### Figure-only content (labels with no prose anchor) — Pass 2 obligations

These label strings are drawn in the artwork but never appear as running text in the chapter, so Pass 2 must anchor each one in prose (or the label-coverage gate will legitimately fail):

- **`Nucleus`** (Fig 18.1) — the body names cell body, Nissl's granules, dendrites, axon, myelin sheath, nodes of Ranvier, synaptic knob and axon terminal, but never the neuron's nucleus.
- **`Cerebral hemisphere`** (Fig 18.4, singular) — the body uses the plural "cerebral hemispheres" only.
- **`Receptors`** (Fig 18.3) — the body says "their specific receptors" (F086), so the bare plural is anchored; listed here as the borderline case to confirm during Pass 2.
- **`Schwan cell`** (Fig 18.1) — artwork misspelling; the prose spells "Schwann cell", so the exact label string will not match running text. Pass 2 must decide the anchor and the typo policy note above governs it: the label row is not reworded.

## Summary classification

**18** summary sentences classified (isolated from the SUMMARY box on textbook p. 237). **14 BODY-PRESENT** (restate a body row) · **4 SUMMARY-UNIQUE** (add a fact the body never states). All 4 SUMMARY-UNIQUE are folded into named sections, so no summary-only fact is dropped.

| # | Summary sentence (verbatim) | Classification | Body row / folded into |
|---:|---|---|---|
| 1 | The neural system coordinates and integrates functions as well as metabolic and homeostatic activities of all the organs. | BODY-PRESENT | F002, F008, F009 |
| 2 | Neurons, the functional units of neural system are excitable cells due to a differential concentration gradient of ions across the membrane. | BODY-PRESENT | F047, F053, F054 |
| 3 | The electrical potential difference across the resting neural membrane is called the 'resting potential'. | BODY-PRESENT | F057 |
| 4 | The nerve impulse is conducted along the axon membrane in the form of a wave of depolarisation and repolarisation. | SUMMARY-UNIQUE | fold into 18.3.1 — the body narrates depolarisation and the K+ restoration (F060-F071) but never names the travelling **wave of depolarisation and repolarisation** |
| 5 | A synapse is formed by the membranes of a pre-synaptic neuron and a post-synaptic neuron which may or may not be separated by a gap called synaptic cleft. | BODY-PRESENT | F074 |
| 6 | Chemicals involved in the transmission of impulses at chemical synapses are called neurotransmitters. | BODY-PRESENT | F083 |
| 7 | Human neural system consists of two parts : (i) central neural system (CNS) and (ii) the peripheral neural system. | BODY-PRESENT | F020 |
| 8 | The CNS consists of the brain and spiral cord. | BODY-PRESENT | F021 (source prints "spiral cord" for "spinal cord" — see typo policy) |
| 9 | The brain can be divided into three major parts : (i) forebrain, (ii) midbrain and (iii) hindbrain. | BODY-PRESENT | F095 |
| 10 | The forebrain consists of cerebrum, thalamus and hypothalamus. | BODY-PRESENT | F097 |
| 11 | The cerebrum is longitudinally divided into two halves that are connected by the corpus callosum. | BODY-PRESENT | F099, F100 |
| 12 | A very important part of the forebrain called hypothalamus controls the body temperature, eating and drinking. | BODY-PRESENT | F109, F110 |
| 13 | Inner parts of cerebral hemispheres and a group of associated deep structures form a complex structure called limbic system which is concerned with olfaction, autonomic responses, regulation of sexual behaviour, expression of emotional reactions, and motivation. | SUMMARY-UNIQUE | fold into 18.4.1 — **olfaction** and **autonomic responses** are limbic functions the body (F112, F113) never lists |
| 14 | The midbrain receives and integrates visual, tactile and auditory inputs. | SUMMARY-UNIQUE | fold into 18.4.2 — the body (F115-F117) gives the midbrain's position and anatomy but **no function at all** |
| 15 | The hindbrain comprises pons, cerebellum and medulla. | BODY-PRESENT | F119 |
| 16 | The cerebellum integrates information received from the semicircular canals of the ear and the auditory system. | SUMMARY-UNIQUE | fold into 18.4.3 — the body (F121) gives only the convoluted surface, never the cerebellum's **function** |
| 17 | The medulla contains centres, which control respiration, cardiovascular reflexes, and gastric secretions. | BODY-PRESENT | F123 |
| 18 | Pons consist of fibre tracts that interconnect different regions of the brain. | BODY-PRESENT | F120 |

## Exercise-gap terms

10 exercises scanned (textbook pp. 237-238). Terms/facts the exercises demand that the body does **not** supply must be taught somewhere in the rewrite; each is assigned a home below.

| Exercise | Term/fact assumed | Status | Explained where |
|---|---|---|---|
| 9(b) | central neural system part that acts as a **master clock** | GAP — the body mentions "circadian (24-hour) rhythms" (F091) but never names the timekeeping structure | 18.4.1 (hypothalamus / suprachiasmatic pacemaker) |
| 10(b) | **impulse conduction in a myelinated vs unmyelinated fibre** | GAP — the body defines both fibre types (F041-F045) but never contrasts how conduction differs (saltatory vs continuous, speed) | 18.3.1 |
| 10(f) | **cranial nerves vs spinal nerves** | GAP — "spinal and cranial nerves" appears once in passing (F044); neither is defined or counted | 18.2 |
| 8(d) | **cerebellum** (as one half of the cerebrum/cerebellum contrast) | GAP in the body, covered by SUMMARY-UNIQUE #16 | 18.4.3 (folded from summary sentence 16) |
| 5(c) | short note on the **midbrain** (needs a function, not just a location) | GAP in the body, covered by SUMMARY-UNIQUE #14 | 18.4.2 (folded from summary sentence 14) |
| 9(a) | which brain part is **most developed** | present | F098 (cerebrum forms the major part) |
| 10(a) | afferent vs efferent neurons | present | F023, F024 |
| 1, 4(b) | structure of the brain / labelled brain diagram | present | F089-F125, Fig 18.4 (F131, F135) |
| 2(a) | CNS vs PNS | present | F020-F022 |
| 2(b), 3(a), 3(b), 7 | resting potential, polarisation, depolarisation, role of Na+ | present | F047-F062 |
| 3(c), 6 | transmission across a chemical synapse / mechanism of synaptic transmission | present | F081-F088, Fig 18.3 |
| 5(a) | neural coordination | present | F002-F012 |
| 5(b), 5(d), 5(e) | forebrain, hindbrain, synapse | present | F096-F113, F118-F125, F073-F074 |
| 8(a), 8(b), 8(c) | myelinated vs non-myelinated axons, dendrites vs axons, thalamus vs hypothalamus | present | F041-F045, F032-F036, F108-F111 |
| 4(a) | labelled neuron diagram | present | Fig 18.1 (F128, F132) |

**Source numbering defect:** Exercise 10 is lettered `(a)`, `(b)`, `(f)` — the source skips `(c)`-`(e)`. Recorded, not renumbered; there are no missing sub-questions to recover.

## Figure manifest

Preserved verbatim from the `1-F` freeze.

| Fig # | Caption (verbatim) | Asset file | Source page | Mono | Verified |
|---|---|---|---:|---|---|
| Fig 18.1 | Structure of a neuron | `assets/fig_18_1.png` | 3 | yes | yes |
| Fig 18.2 | Diagrammatic representation of impulse conduction through an axon (at points A and B) | `assets/fig_18_2.png` | 4 | yes | yes |
| Fig 18.3 | Diagram showing axon terminal and synapse | `assets/fig_18_3.png` | 5 | yes | yes |
| Fig 18.4 | Diagram showing sagittal section of the human brain | `assets/fig_18_4.png` | 6 | yes | yes |

All four emitted assets are high-resolution grayscale PNGs (`mode=L`) generated with autocontrast: `fig_18_1.png` 1284x2250, `fig_18_2.png` 2201x1272, `fig_18_3.png` 2054x1498, `fig_18_4.png` 2751x1663.

### Extraction record and audit trail (preserved from `1-F`)

The reproducible extractor is `extract_figures.py`. The canonical 4x grid renderer is `scratch/ch18_render_quad_grids.py`, and its page overlays are stored in `scratch/ch18_figs/grid_4x/`. The mechanical audit is `scratch/audit_ch18.py`, and the final visual review is recorded in `scratch/ch18_figs/grid_findings.md`. The opened-image label harvest is preserved in `scratch/ch18_figs/doc_label_harvest.md`.

Figure 18.2 was repinned after visual review so the complete lower panel, arrows, charge marks, `A`/`B` markers, and both `Na` labels are retained. Figure 18.4 was repinned to remove preceding body text while preserving the complete brain plate, bracket, and labels. The final visual gate was completed by opening every final PNG individually and confirming correct figure identity, complete labels and leader lines, no accidental neighbouring prose or figure capture, print-legible detail, and monochrome output. The final audit reports clean border-band checks for all four assets. The vector drawing-extent check is not applicable to the raster artwork in Figure 18.4.

## Census sections (each total derivable from the list beside it)

**Heading census — 12 rows = 1 title plate + 4 numbered + 5 sub-numbered + 2 unnumbered.** Title plate (F001) · 18.1 (F013) · 18.2 (F019) · 18.3 (F029) · 18.3.1 (F046) · 18.3.2 (F072) · 18.4 (F089) · 18.4.1 (F096) · 18.4.2 (F114) · 18.4.3 (F118) · SUMMARY (F126) · EXERCISES (F127). The p.1 contents rail lists only 18.1-18.4 and is not a heading source.

**Opener census — 10 rows.** One opener per headed section plus the unheaded chapter-intro prose, minus the headings that carry no opening sentence of their own — the title plate, SUMMARY and EXERCISES. Sections with an opener: intro (F002) · 18.1 (F014) · 18.2 (F020) · 18.3 (F030) · 18.3.1 (F047) · 18.3.2 (F073) · 18.4 (F090) · 18.4.1 (F097) · 18.4.2 (F115) · 18.4.3 (F119). That is 9 headed openers plus the intro = 10. Both 18.3 and 18.4 run prose before their first sub-head, so each carries its own opener.

**Figure census — 4 numbered figures, 4 assets, 4 caption rows (F128-F131), 4 label rows (F132-F135), 35 labels, and 6 in-text call-outs.** Call-outs: Figure 18.1 x1 (F030) · Figure 18.2 x2 (F059, F065) · Figure 18.4 x2 (F095, F097) · Figure 18.3 x1 (F081). Total mentions of the string `Figure 18.` in the source = 10 (6 call-outs + 4 caption heads). Pages carrying no figure were opened as images to confirm no unnumbered plate exists (see the figure census reconciliation section).

**Type census — 131 Facts rows by type** (machine-derived by `verify_inventory.py` check [4] from the Type column, not hand-tallied): concept 55 · process 22 · definition 22 · heading 12 · opener 10 · caption 4 · prompt 3 · example 3 · number 2. Plus 4 `figure-label` rows in the matrix = 135 total.

**Exercise census — 10 numbered exercises**, sub-lettered `(a)`-`(f)` with the source's `(c)`-`(e)` skip in exercise 10.

## Gate 1 checklist

| # | Gate 1 requirement | Status |
|---|---|---|
| 1 | Whole source read start to finish before any row was written | PASS — session `1-S`; all 9 pages of text plus rendered images of every figure-free page |
| 2 | Every sentence-level fact captured verbatim, in source order, one row each | PASS — 131 contiguous rows F001-F131 |
| 3 | Heading sweep complete and censused | PASS — 12 rows, list above |
| 4 | Opener sweep complete and censused | PASS — 10 rows, list above |
| 5 | Figure census reconciled source-to-asset, no unnumbered plate | PASS — 4 = 4 = 4 = 4; figure-free pages opened as images |
| 6 | Figure-label matrix present, single location, machine-parseable | PASS — F132-F135, 35 labels, parsed by `check_pdf._extract_labels` (asserted by `verify_inventory.py` check [3]) |
| 7 | Captions transcribed verbatim | PASS — F128-F131; the one manifest/source divergence (`sagital`) is recorded, not silently reconciled |
| 8 | Summary sentences classified, SUMMARY-UNIQUE facts each assigned a home | PASS — 18 classified, 4 SUMMARY-UNIQUE all folded |
| 9 | Exercise-gap sweep complete, each gap assigned a home | PASS — 5 gaps, each with a named destination section |
| 10 | Source typos / extraction artefacts recorded, rows not silently corrected | PASS — typo-policy section |
| 11 | Encoding hygiene: no Unicode sub/superscripts, no U+FFFD | PASS — asserted by `verify_inventory.py` check [5] |
| 12 | All Facts rows unticked at freeze | PASS — Pass 2 ticks them; only the `1-F` label rows carry `x`, earned by opened-PNG verification |
| 13 | Every asserted count machine-derivable, not hand-waved | PASS — `verify_inventory.py` re-derives all of them from the PDF, the assets and this file |

**Gate 1 is green.** Pass 2 (rewrite) has not started and no rewrite prose exists for this chapter.

## References

- Source PDF: `Chapter/class 11/Chapter 18 - Neural Control and Coordination.pdf`
- Assets: `assets/fig_18_1.png` .. `assets/fig_18_4.png`
- Extraction script: `extract_figures.py` · grid renderer: `../../../scratch/ch18_render_quad_grids.py` · audit: `../../../scratch/audit_ch18.py`
- Pass 1 verifier: `verify_inventory.py` (run: `/vercel/share/neetenv/bin/python verify_inventory.py`)
- Extracted source text used for the `1-S` read: `../../../scratch/ch18_pass1/source_text.txt`
