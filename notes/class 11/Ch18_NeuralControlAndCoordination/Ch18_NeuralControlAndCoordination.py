"""
NCERT Class 11 Biology, Chapter 18 - Neural Control and Coordination
NEET replacement notes -> A4 print-ready PDF.

Built under SUPREME COMMAND PROMPT.md v6, Pass 2: written linearly from the
frozen 135-row inventory (Ch18_NeuralControlAndCoordination_inventory.md) in
Content Order (SS5), importing the repo-level frozen style module
`neet_template.py` (SS0.6). No style, geometry, colour or font is re-declared
here.

Block markers `# ---- N.N ----` mark every NCERT section so a Pass 3 flag can be
found and fixed in one contiguous block. Inventory row IDs are named in the
comments so any fact can be traced back to its frozen row.

FIGURE-LABEL COVERAGE (check 6): all four figures carry their callouts as
artwork, so each figure is followed by a NOTE listing its in-figure labels
verbatim (matrix rows F132-F135, 35 label strings). That is what puts every
in-figure label into the running text for check_pdf.py check 6, and it lets a
print reader name the parts of a diagram whose labels did not survive
photocopying. The four "figure-only" obligations flagged by the inventory are
handled there too: `Nucleus` (Fig 18.1), `Cerebral hemisphere` in the singular
(Fig 18.4), the bare plural `Receptors` (Fig 18.3), and the artwork's
misspelling `Schwan cell` (Fig 18.1), which is quoted as the plate's own
spelling while the prose keeps NCERT's `Schwann cell`.

SOURCE-VERBATIM SPELLINGS (inventory typo policy): the Figure 18.4 caption is
printed with the source's `sagital`; `passess` (F116) is quoted where the
midbrain aqueduct is described; the SUMMARY's `spiral cord` is quoted in the
Quick Recap. Each is flagged in place as the source's spelling so a reader never
mistakes it for an error introduced here.

SUMMARY-UNIQUE FOLDS (Rule 3): four facts stated only in the NCERT summary are
folded into the body sections named by the inventory - the travelling wave of
depolarisation and repolarisation (18.3.1), limbic olfaction + autonomic
responses (18.4.1), the midbrain's visual/tactile/auditory integration (18.4.2),
and the cerebellum's semicircular-canal/auditory integration (18.4.3).

EXERCISE GAPS (Rule 2): the three genuine gaps (master clock; myelinated vs
unmyelinated conduction; cranial vs spinal nerves) are closed in their planned
homes and restated in the closing "Terms used in the exercises" appendix, where
anything that goes beyond this chapter's own sentences is labelled as such.

Superscripts: the inventory stores the ionic charges as plain ASCII K+ / Na+,
but check_pdf.py check 5 bans Unicode sub/superscripts in the PDF text stream,
so every charge is written here with a <super> tag.

Source: Chapter/class 11/Chapter 18 - Neural Control and Coordination.pdf
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

# sys.path bootstrap: walk up until we find the repo-level neet_template.py (SS0.6)
_probe = HERE
while _probe != os.path.dirname(_probe):
    if os.path.exists(os.path.join(_probe, "neet_template.py")):
        sys.path.insert(0, _probe)
        break
    _probe = os.path.dirname(_probe)

from neet_template import (  # noqa: E402
    STYLES,
    heading, keyterm, process_flow, note, memory_aid, data_table, title_block, build_pdf,
)
from neet_template import figure as _shared_figure  # noqa: E402
from reportlab.platypus import Paragraph, Spacer  # noqa: E402

ASSETS = os.path.join(HERE, "assets")
OUT_PDF = os.path.join(HERE, "Ch18_NeuralControlAndCoordination.pdf")

# Inline ion shorthands (check 5: tags, never Unicode sub/superscripts)
NA = "Na<super>+</super>"
K = "K<super>+</super>"


def figure(asset_name, caption_text, max_width_cm=15.9):
    """Chapter-local binding of the shared figure() helper (SS0.6)."""
    return _shared_figure(asset_name, caption_text, ASSETS, max_width_cm=max_width_cm)


def body(text):
    return Paragraph(text, STYLES["Body"])


def b1(text):
    return Paragraph("&bull; " + text, STYLES["Bullet1"])


def b2(text):
    return Paragraph("- " + text, STYLES["Bullet2"])


def gap(h=4):
    return Spacer(1, h)


story = []

# ======================================================================================
# ---- Title block (SS5 item 1) ---- F001
# ======================================================================================
story += title_block("Neural Control and Coordination")

# ======================================================================================
# ---- 18.intro ---- F002-F012 (opener F002)
# ======================================================================================
story.append(body(
    "The functions of the <b>organs/organ systems</b> in our body <b>must be coordinated to "
    "maintain homeostasis</b>."))

story.append(keyterm(
    "<b>Coordination</b> - the process through which <b>two or more organs interact and "
    "complement the functions of one another</b>."))

story.append(body(
    "<b>Worked example - physical exercise.</b> When we do physical exercises the <b>energy "
    "demand is increased</b> for maintaining an increased muscular activity, and the <b>supply "
    "of oxygen is also increased</b>. That increased oxygen supply necessitates an increase in "
    "the <b>rate of respiration, heart beat</b> and <b>increased blood flow via blood "
    "vessels</b>. When physical exercise is stopped, the activities of <b>nerves, lungs, heart "
    "and kidney</b> gradually return to their <b>normal conditions</b>. Thus the functions of "
    "<b>muscles, lungs, heart, blood vessels, kidney</b> and other organs are coordinated while "
    "performing physical exercises."))

story.append(gap())
story.append(data_table([
    ["System", "How it coordinates", "Nature of the link"],
    ["<b>Neural system</b>",
     "Provides an <b>organised network of point-to-point connections</b>",
     "For a <b>quick</b> coordination"],
    ["<b>Endocrine system</b>", "Provides <b>chemical integration</b>",
     "Through <b>hormones</b>"],
], col_widths=[22, 48, 30]))

story.append(gap())
story.append(body(
    "In our body the <b>neural system and the endocrine system jointly</b> coordinate and "
    "integrate <b>all</b> the activities of the organs so that they function in a "
    "<b>synchronised fashion</b>."))

story.append(note(
    "<b>Scope of this chapter.</b> You will learn about the <b>neural system of human</b> and "
    "the <b>mechanisms of neural coordination</b> - the <b>transmission of nerve impulse</b> and "
    "<b>impulse conduction across a synapse</b>."))

story.append(gap())

# ======================================================================================
# ---- 18.1 NEURAL SYSTEM ---- F013-F018 (heading F013, opener F014)
# ======================================================================================
story.append(heading("18.1", "Neural System", level=1))

story.append(keyterm(
    "<b>Neurons</b> - the neural system of <b>all</b> animals is composed of highly specialised "
    "cells called neurons, which can <b>detect, receive and transmit</b> different kinds of "
    "<b>stimuli</b>."))

story.append(gap())
story.append(data_table([
    ["Animal group", "Level of neural organisation"],
    ["<b>Lower invertebrates</b>", "Neural organisation is <b>very simple</b>."],
    ["<i>Hydra</i>", "Composed of a <b>network of neurons</b>."],
    ["<b>Insects</b>",
     "The neural system is <b>better organised</b>: a <b>brain</b> is present along with a "
     "number of <b>ganglia</b> and <b>neural tissues</b>."],
    ["<b>Vertebrates</b>", "Have a <b>more developed</b> neural system."],
], col_widths=[26, 74]))

story.append(gap())

# ======================================================================================
# ---- 18.2 HUMAN NEURAL SYSTEM ---- F019-F028 (heading F019, opener F020)
# ======================================================================================
story.append(heading("18.2", "Human Neural System", level=1, has_table=True))

story.append(body(
    "The human neural system is divided into <b>two parts</b>: <b>(i) the central neural system "
    "(CNS)</b> and <b>(ii) the peripheral neural system (PNS)</b>."))

story.append(b1(
    "<b>CNS</b> - includes the <b>brain</b> and the <b>spinal cord</b>, and is the <b>site of "
    "information processing and control</b>."))
story.append(b1(
    "<b>PNS</b> - comprises <b>all the nerves of the body associated with the CNS</b> (brain and "
    "spinal cord)."))

story.append(gap())
story.append(body(
    "<b>The nerve fibres of the PNS are of two types</b>: <b>(a) afferent fibres</b> and "
    "<b>(b) efferent fibres</b>."))

story.append(data_table([
    ["Fibre type", "Direction of the impulse", "What it carries"],
    ["<b>Afferent</b> nerve fibres", "<b>From tissues/organs to the CNS</b>",
     "Sensory input arriving at the CNS"],
    ["<b>Efferent</b> fibres", "<b>From the CNS to the concerned peripheral tissues/organs</b>",
     "<b>Regulatory</b> impulses"],
], col_widths=[22, 40, 38]))

story.append(gap())
story.append(body(
    "The PNS is divided into two divisions called the <b>somatic neural system</b> and the "
    "<b>autonomic neural system</b>."))

story.append(data_table([
    ["Division of the PNS", "Relays impulses from the CNS to"],
    ["<b>Somatic neural system</b>", "<b>Skeletal muscles</b>"],
    ["<b>Autonomic neural system</b>",
     "The <b>involuntary organs</b> and <b>smooth muscles</b> of the body"],
], col_widths=[32, 68]))

story.append(gap())
story.append(b1(
    "The autonomic neural system is <b>further classified</b> into the <b>sympathetic neural "
    "system</b> and the <b>parasympathetic neural system</b>."))

story.append(gap())
story.append(keyterm(
    "<b>Visceral nervous system</b> - the part of the <b>peripheral</b> nervous system that "
    "comprises the whole complex of <b>nerves, fibres, ganglia and plexuses</b> by which "
    "impulses travel <b>from the central nervous system to the viscera</b> and <b>from the "
    "viscera to the central nervous system</b>."))

story.append(gap())
story.append(note(
    "<b>Exercise gap closed here (Exercise 10f: cranial nerves vs spinal nerves).</b> NCERT's "
    "own text names <b>spinal and cranial nerves</b> only once, as the place where myelinated "
    "nerve fibres are found (18.3), and never defines either. Both are <b>PNS</b> nerves and "
    "they are told apart by <b>where they leave the CNS</b>: <b>cranial nerves arise from the "
    "brain</b>, while <b>spinal nerves arise from the spinal cord</b>. Each carries afferent "
    "fibres, efferent fibres, or both. <i>Beyond this chapter's own sentences - kept because "
    "Exercise 10(f) demands the distinction (Rule 2).</i>"))

story.append(gap())

# ======================================================================================
# ---- 18.3 NEURON AS STRUCTURAL AND FUNCTIONAL UNIT ---- F029-F045 (heading F029, opener F030)
# Figure 18.1 (caption F128, labels F132) sits here, at the neuron structure it illustrates.
# ======================================================================================
story.append(heading("18.3", "Neuron as Structural and Functional Unit of Neural System",
                     level=1))

story.append(body(
    "A <b>neuron</b> is a <b>microscopic</b> structure composed of <b>three major parts</b>, "
    "namely, <b>cell body, dendrites</b> and <b>axon</b> (Figure 18.1)."))

story.append(data_table([
    ["Part of the neuron", "Structure", "Function"],
    ["<b>Cell body</b>",
     "Contains <b>cytoplasm</b> with typical <b>cell organelles</b> and certain <b>granular "
     "bodies called Nissl's granules</b>",
     "The metabolic centre of the neuron; impulses arrive here from the dendrites"],
    ["<b>Dendrites</b>",
     "<b>Short fibres</b> which <b>branch repeatedly</b> and <b>project out of the cell "
     "body</b>; they <b>also contain Nissl's granules</b>",
     "<b>Transmit impulses towards the cell body</b>"],
    ["<b>Axon</b>",
     "A <b>long fibre</b>, the <b>distal end of which is branched</b>; each branch terminates "
     "as a bulb-like structure called a <b>synaptic knob</b>, which possesses <b>synaptic "
     "vesicles containing chemicals called neurotransmitters</b>",
     "<b>Transmits nerve impulses away from the cell body</b> to a <b>synapse</b> or to a "
     "<b>neuro-muscular junction</b>"],
], col_widths=[16, 46, 38]))

story.append(gap())
story.append(figure("fig_18_1.png", "Fig. 18.1 - Structure of a neuron"))

story.append(note(
    "<b>Read the plate (Figure 18.1 labels).</b> The diagram marks the <b>Dendrites</b>, the "
    "<b>Nissl's granules</b> inside the <b>Cell body</b>, the <b>Nucleus</b> within that cell "
    "body, the <b>Schwan cell</b> (the plate's own spelling of the <b>Schwann cell</b>) wrapping "
    "the <b>Axon</b> as a <b>Myelin sheath</b>, a <b>Node of Ranvier</b> between two sheaths, "
    "and at the far end the <b>Axon terminal</b> ending in a <b>Synaptic knob</b>."))

story.append(gap())
story.append(body(
    "<b>Based on the number of axon and dendrites</b>, the neurons are divided into <b>three "
    "types</b>."))

story.append(data_table([
    ["Type", "Axon and dendrites", "Where found"],
    ["<b>Multipolar</b>", "<b>One axon and two or more dendrites</b>",
     "<b>Cerebral cortex</b>"],
    ["<b>Bipolar</b>", "<b>One axon and one dendrite</b>", "<b>Retina of eye</b>"],
    ["<b>Unipolar</b>", "<b>Cell body with one axon only</b>",
     "Found <b>usually</b> in the <b>embryonic stage</b>"],
], col_widths=[18, 44, 38]))

story.append(gap())
story.append(body(
    "There are <b>two types of axons</b>, namely, <b>myelinated</b> and <b>non-myelinated</b>."))

story.append(data_table([
    ["Feature", "Myelinated nerve fibre", "Unmyelinated nerve fibre"],
    ["Schwann cells",
     "<b>Enveloped with Schwann cells</b>, which <b>form a myelin sheath</b> around the axon",
     "<b>Enclosed by a Schwann cell that does not form a myelin sheath</b> around the axon"],
    ["Gaps in the sheath",
     "The gaps between two adjacent myelin sheaths are called <b>nodes of Ranvier</b>",
     "No myelin sheath, hence <b>no nodes of Ranvier</b>"],
    ["Where found", "<b>Spinal and cranial nerves</b>",
     "<b>Commonly</b> found in <b>autonomous</b> and the <b>somatic</b> neural systems"],
], col_widths=[18, 41, 41]))

story.append(gap())
story.append(memory_aid(
    "<b>Neuron traffic direction:</b> <b>D</b>endrites <b>D</b>eliver <b>in</b>, <b>A</b>xons "
    "<b>A</b>way. Both carry Nissl's granules only on the dendrite side of the cell body."))

story.append(gap())

# ======================================================================================
# ---- 18.3.1 Generation and Conduction of Nerve Impulse ---- F046-F071
# (heading F046, opener F047, prompts F048/F058 kept as the source's framing)
# Figure 18.2 (caption F129, labels F133) sits here, on the A-to-B conduction it shows.
# SUMMARY-UNIQUE fold #4 (wave of depolarisation and repolarisation) closes the section.
# Exercise gap 10(b) (myelinated vs unmyelinated conduction) closes it too.
# ======================================================================================
story.append(heading("18.3.1", "Generation and Conduction of Nerve Impulse", level=2))

story.append(body(
    "Neurons are <b>excitable cells</b> because their <b>membranes are in a polarised "
    "state</b>. <i>Why is the membrane of a neuron polarised?</i>"))

story.append(b1(
    "<b>Different types of ion channels</b> are present on the neural membrane, and these ion "
    "channels are <b>selectively permeable to different ions</b>."))
story.append(b1(
    f"<b>At rest</b> (a neuron <b>not conducting any impulse</b>) the axonal membrane is "
    f"<b>comparatively more permeable to potassium ions ({K})</b> and <b>nearly impermeable to "
    f"sodium ions ({NA})</b>."))
story.append(b1(
    "<b>Similarly</b>, the membrane is <b>impermeable to negatively charged proteins</b> present "
    "in the <b>axoplasm</b>."))

story.append(gap())
story.append(data_table([
    ["Compartment", f"{K}", f"{NA}", "Negatively charged proteins"],
    ["<b>Axoplasm</b> (inside the axon)", "<b>High</b> concentration", "<b>Low</b> concentration",
     "<b>High</b> - trapped inside"],
    ["<b>Fluid outside the axon</b>", "<b>Low</b> concentration", "<b>High</b> concentration",
     "Not stated by NCERT"],
], col_widths=[34, 20, 20, 26]))

story.append(gap())
story.append(body(
    "These opposed concentrations <b>form a concentration gradient</b> across the membrane."))

story.append(keyterm(
    f"<b>Sodium-potassium pump</b> - the ionic gradients across the resting membrane are "
    f"maintained by the <b>active transport</b> of ions by this pump, which transports "
    f"<b>3 {NA} outwards for 2 {K} into the cell</b>."))

story.append(gap())
story.append(body(
    "<b>As a result</b>, the <b>outer surface</b> of the axonal membrane possesses a "
    "<b>positive charge</b> while its <b>inner surface becomes negatively charged</b>, and the "
    "membrane is therefore <b>polarised</b>."))

story.append(keyterm(
    "<b>Resting potential</b> - the <b>electrical potential difference across the resting plasma "
    "membrane</b>."))

story.append(gap())
story.append(body(
    "<i>Now the mechanism of generation of a nerve impulse and its conduction along an "
    "axon.</i>"))

story.append(process_flow([
    f"A <b>stimulus is applied at a site</b> (Figure 18.2, e.g., <b>point A</b>) on the "
    f"polarised membrane; the membrane at <b>site A becomes freely permeable to {NA}</b>.",
    f"This leads to a <b>rapid influx of {NA}</b>, followed by the <b>reversal of the polarity "
    f"at that site</b>: the <b>outer surface becomes negatively charged</b> and the <b>inner "
    f"side becomes positively charged</b>. The polarity at site A is thus reversed and hence "
    f"<b>depolarised</b>.",
    "The electrical potential difference across the plasma membrane at site A is called the "
    "<b>action potential</b>, which is <b>in fact termed as a nerve impulse</b>.",
    "At sites <b>immediately ahead</b> - the axon at <b>site B</b> - the membrane still has a "
    "<b>positive charge on the outer surface</b> and a <b>negative charge on its inner "
    "surface</b>.",
    "<b>As a result, a current flows on the inner surface from site A to site B</b>; on the "
    "<b>outer surface current flows from site B to site A</b> (Figure 18.2), <b>completing the "
    "circuit of current flow</b>.",
    "Hence the <b>polarity at the site is reversed</b> and an <b>action potential is generated "
    "at site B</b> - i.e. the impulse (action potential) generated at <b>site A arrives at site "
    "B</b>.",
    "<b>The sequence is repeated along the length of the axon</b> and consequently the "
    "<b>impulse is conducted</b>.",
]))

story.append(gap())
story.append(figure(
    "fig_18_2.png",
    "Fig. 18.2 - Diagrammatic representation of impulse conduction through an axon (at points A "
    "and B)"))

story.append(note(
    f"<b>Read the plate (Figure 18.2 labels).</b> The plate marks the stimulated site <b>A</b> "
    f"and the site immediately ahead, <b>B</b>, with rows of plus and minus charge marks on the "
    f"two membrane surfaces and <b>Na</b> printed at each site where sodium ({NA}) rushes "
    f"inwards. Reading the panels top to bottom shows the reversed polarity travelling from "
    f"<b>A</b> to <b>B</b> along the axon."))

story.append(gap())
story.append(body(
    f"<b>Restoring the resting state.</b> The <b>stimulus-induced rise in permeability to "
    f"{NA} is extremely short-lived</b>. It is <b>quickly followed by a rise in permeability to "
    f"{K}</b>. <b>Within a fraction of a second, {K} diffuses outside the membrane</b> and "
    f"<b>restores the resting potential</b> of the membrane at the site of excitation, and the "
    f"<b>fibre becomes once more responsive to further stimulation</b>."))

story.append(gap())
story.append(note(
    "<b>The impulse travels as a wave.</b> Taken end to end, the nerve impulse is <b>conducted "
    "along the axon membrane in the form of a wave of depolarisation and repolarisation</b>: "
    "depolarisation sweeps forward site by site while the sites just behind it are already being "
    "repolarised. <i>(NCERT states this only in the chapter summary; it is folded in here, at "
    "the mechanism it describes.)</i>"))

story.append(gap())
story.append(note(
    "<b>Exercise gap closed here (Exercise 10b: conduction in a myelinated vs an unmyelinated "
    "nerve fibre).</b> The chapter defines both fibre types (18.3) but never contrasts how they "
    "conduct. In an <b>unmyelinated</b> fibre the bare membrane is depolarised at <b>every "
    "successive point</b>, exactly as the A-to-B sequence above describes, so conduction is "
    "<b>continuous and slower</b>. In a <b>myelinated</b> fibre the <b>myelin sheath insulates "
    "the axon</b> and the membrane is exposed only at the <b>nodes of Ranvier</b>, so the "
    "impulse is regenerated <b>node to node</b> - <b>saltatory (jumping) conduction</b>, which "
    "is <b>faster</b> and uses less energy. <i>Beyond this chapter's own sentences - kept "
    "because Exercise 10(b) demands the contrast (Rule 2).</i>"))

story.append(gap())

# ======================================================================================
# ---- 18.3.2 Transmission of Impulses ---- F072-F088 (heading F072, opener F073, prompt F082)
# Figure 18.3 (caption F130, labels F134) sits here, on the chemical synapse it shows.
# ======================================================================================
story.append(heading("18.3.2", "Transmission of Impulses", level=2, has_table=True))

story.append(body(
    "A nerve impulse is <b>transmitted from one neuron to another through junctions called "
    "synapses</b>."))

story.append(keyterm(
    "<b>Synapse</b> - formed by the membranes of a <b>pre-synaptic neuron</b> and a "
    "<b>post-synaptic neuron</b>, which <b>may or may not be separated by a gap called the "
    "synaptic cleft</b>."))

story.append(gap())
story.append(body(
    "There are <b>two types of synapses</b>, namely, <b>electrical synapses</b> and <b>chemical "
    "synapses</b>."))

story.append(data_table([
    ["Feature", "Electrical synapse", "Chemical synapse"],
    ["Membranes",
     "Membranes of pre- and post-synaptic neurons are in <b>very close proximity</b>",
     "Membranes of the pre- and post-synaptic neurons are <b>separated by a fluid-filled space "
     "called the synaptic cleft</b> (Figure 18.3)"],
    ["How the impulse crosses",
     "<b>Electrical current can flow directly</b> from one neuron into the other across these "
     "synapses",
     "Chemicals called <b>neurotransmitters</b> are involved in the transmission of impulses"],
    ["Resemblance",
     "Transmission is <b>very similar to impulse conduction along a single axon</b>",
     "A fresh potential must be generated in the post-synaptic neuron"],
    ["Speed", "<b>Always faster</b> than that across a chemical synapse", "<b>Slower</b>"],
    ["Occurrence", "<b>Rare in our system</b>", "The usual synapse in our system"],
], col_widths=[18, 41, 41]))

story.append(gap())
story.append(figure("fig_18_3.png", "Fig. 18.3 - Diagram showing axon terminal and synapse"))

story.append(note(
    "<b>Read the plate (Figure 18.3 labels).</b> The plate follows the <b>Axon</b> into its "
    "<b>Axon terminal</b>, which holds the <b>Synaptic vesicles</b>; the enlarged inset of the "
    "<b>Synapse</b> shows the <b>Pre-synaptic membrane</b>, the <b>Synaptic cleft</b> and the "
    "<b>Post-synaptic membrane</b>, with <b>Neurotransmitters</b> crossing the cleft to the "
    "<b>Receptors</b> drawn on the post-synaptic membrane."))

story.append(gap())
story.append(body(
    "<i>How does the pre-synaptic neuron transmit an impulse (action potential) across the "
    "synaptic cleft to the post-synaptic neuron?</i>"))

story.append(process_flow([
    "The <b>axon terminals contain vesicles filled with neurotransmitters</b>.",
    "When an <b>impulse (action potential) arrives at the axon terminal</b>, it <b>stimulates "
    "the movement of the synaptic vesicles towards the membrane</b>.",
    "The vesicles <b>fuse with the plasma membrane</b> and <b>release their neurotransmitters in "
    "the synaptic cleft</b>.",
    "The <b>released neurotransmitters bind to their specific receptors</b>, present on the "
    "<b>post-synaptic membrane</b>.",
    "This <b>binding opens ion channels</b>, allowing the <b>entry of ions</b> which can "
    "<b>generate a new potential in the post-synaptic neuron</b>.",
    "The <b>new potential developed may be either excitatory or inhibitory</b>.",
]))

story.append(gap())

# ======================================================================================
# ---- 18.4 CENTRAL NEURAL SYSTEM ---- F089-F095 (heading F089, opener F090)
# Figure 18.4 (caption F131 - source-verbatim 'sagital'; labels F135) sits here, on the
# three-part division of the brain it shows.
# ======================================================================================
story.append(heading("18.4", "Central Neural System", level=1))

story.append(body(
    "The <b>brain</b> is the <b>central information processing organ</b> of our body, and acts "
    "as the <b>'command and control system'</b>."))

story.append(data_table([
    ["What the brain does", "Items NCERT lists"],
    ["<b>Controls</b>",
     "<b>Voluntary movements</b>; <b>balance of the body</b>; functioning of <b>vital "
     "involuntary organs</b> (e.g., lungs, heart, kidneys, etc.); <b>thermoregulation</b>; "
     "<b>hunger and thirst</b>; <b>circadian (24-hour) rhythms</b> of our body; activities of "
     "<b>several endocrine glands</b>; and <b>human behaviour</b>"],
    ["<b>Site for processing of</b>",
     "<b>Vision, hearing, speech, memory, intelligence, emotions</b> and <b>thoughts</b>"],
], col_widths=[24, 76]))

story.append(gap())
story.append(body(
    "<b>Protection.</b> The human brain is <b>well protected by the skull</b>. Inside the skull "
    "the brain is covered by <b>cranial meninges</b>."))

story.append(data_table([
    ["Layer of the cranial meninges", "Position"],
    ["<b>Dura mater</b>", "The <b>outer</b> layer"],
    ["<b>Arachnoid</b>", "A <b>very thin middle</b> layer"],
    ["<b>Pia mater</b>", "The <b>inner</b> layer, <b>in contact with the brain tissue</b>"],
], col_widths=[34, 66]))

story.append(gap())
story.append(body(
    "The brain can be divided into <b>three major parts</b>: <b>(i) forebrain, (ii) midbrain</b> "
    "and <b>(iii) hindbrain</b> (Figure 18.4)."))

story.append(figure(
    "fig_18_4.png",
    "Fig. 18.4 - Diagram showing sagital section of the human brain "
    "(NCERT prints 'sagital'; the conventional spelling is 'sagittal')"))

story.append(note(
    "<b>Read the plate (Figure 18.4 labels).</b> A bracket marks the <b>Forebrain</b>, inside "
    "which the plate names the <b>Cerebrum</b>, one <b>Cerebral hemisphere</b> of the pair, the "
    "<b>Corpus callosum</b> joining them, the <b>Thalamus</b> and the <b>Hypothalamus</b>. "
    "Below it are the <b>Midbrain</b>, with its <b>Cerebral aqueduct</b>, and the "
    "<b>Hindbrain</b> - <b>Pons</b>, <b>Cerebellum</b> and <b>Medulla</b> - which continues into "
    "the <b>Spinal cord</b>."))

story.append(gap())

# ======================================================================================
# ---- 18.4.1 Forebrain ---- F096-F113 (heading F096, opener F097)
# SUMMARY-UNIQUE fold #13 (limbic olfaction + autonomic responses) and exercise gap 9(b)
# (master clock) close this block.
# ======================================================================================
story.append(heading("18.4.1", "Forebrain", level=2))

story.append(body(
    "The forebrain consists of <b>cerebrum, thalamus</b> and <b>hypothalamus</b> "
    "(Figure 18.4)."))

story.append(b1("<b>Cerebrum forms the major part of the human brain.</b>"))
story.append(b1(
    "A <b>deep cleft divides the cerebrum longitudinally into two halves</b>, which are termed "
    "the <b>left and right cerebral hemispheres</b>."))
story.append(keyterm(
    "<b>Corpus callosum</b> - the <b>tract of nerve fibres</b> that <b>connects the "
    "hemispheres</b>."))
story.append(keyterm(
    "<b>Cerebral cortex</b> - the <b>layer of cells which covers the cerebral hemisphere</b>; it "
    "is <b>thrown into prominent folds</b>."))

story.append(gap())
story.append(data_table([
    ["Matter", "What it is", "Why it looks that way"],
    ["<b>Grey matter</b>",
     "The <b>cerebral cortex</b> is referred to as the grey matter",
     "Due to its <b>greyish appearance</b> - the <b>neuron cell bodies are concentrated "
     "here</b>, giving the colour"],
    ["<b>White matter</b>",
     "<b>Fibres of the tracts</b>, covered with the <b>myelin sheath</b>, which constitute the "
     "<b>inner part of the cerebral hemisphere</b>",
     "They give an <b>opaque white appearance</b> to the layer"],
], col_widths=[16, 42, 42]))

story.append(gap())
story.append(body(
    "The cerebral cortex contains <b>motor areas, sensory areas</b> and <b>large regions that "
    "are neither clearly sensory nor motor in function</b>."))

story.append(keyterm(
    "<b>Association areas</b> - those neither-sensory-nor-motor regions, responsible for "
    "<b>complex functions</b> like <b>intersensory associations, memory</b> and "
    "<b>communication</b>."))

story.append(gap())
story.append(data_table([
    ["Forebrain part", "Position", "Function"],
    ["<b>Thalamus</b>", "The <b>cerebrum wraps around</b> it",
     "A <b>major coordinating centre for sensory and motor signaling</b>"],
    ["<b>Hypothalamus</b>", "Lies at the <b>base of the thalamus</b>",
     "Contains a number of <b>centres which control body temperature, urge for eating and "
     "drinking</b>; also contains several groups of <b>neurosecretory cells</b>, which secrete "
     "hormones called <b>hypothalamic hormones</b>"],
], col_widths=[18, 26, 56]))

story.append(gap())
story.append(keyterm(
    "<b>Limbic lobe or limbic system</b> - the <b>inner parts of cerebral hemispheres</b> and a "
    "group of <b>associated deep structures like amygdala, hippocampus</b>, etc., form this "
    "complex structure."))

story.append(b1(
    "<b>Along with the hypothalamus</b>, the limbic system is involved in the <b>regulation of "
    "sexual behaviour</b>, the <b>expression of emotional reactions</b> (e.g., <b>excitement, "
    "pleasure, rage and fear</b>) and <b>motivation</b>."))
story.append(b1(
    "The limbic system is <b>also concerned with olfaction and autonomic responses</b>. "
    "<i>(Stated only in the NCERT summary; folded in here with the rest of the limbic "
    "functions.)</i>"))

story.append(gap())
story.append(note(
    "<b>Exercise gap closed here (Exercise 9b: which part of our central neural system acts as a "
    "master clock?).</b> The chapter states that the brain controls the <b>circadian (24-hour) "
    "rhythms</b> of our body (18.4) but never names the timekeeper. That role belongs to the "
    "<b>hypothalamus</b>, whose <b>suprachiasmatic nucleus</b> is the body's <b>master "
    "clock</b> - consistent with the hypothalamus already being the centre for body "
    "temperature, eating and drinking. <i>The name of the nucleus is beyond this chapter's own "
    "sentences - kept because Exercise 9(b) demands it (Rule 2).</i>"))

story.append(gap())

# ======================================================================================
# ---- 18.4.2 Midbrain ---- F114-F117 (heading F114, opener F115)
# SUMMARY-UNIQUE fold #14 (visual, tactile and auditory inputs) closes this block; the source
# spelling 'passess' (F116) is quoted in place.
# ======================================================================================
story.append(heading("18.4.2", "Midbrain", level=2))

story.append(b1(
    "The midbrain is <b>located between the thalamus/hypothalamus of the forebrain and the pons "
    "of the hindbrain</b>."))
story.append(b1(
    "A canal called the <b>cerebral aqueduct</b> passes through the midbrain (NCERT prints "
    "<b>'passess'</b>)."))
story.append(b1(
    "The <b>dorsal portion</b> of the midbrain consists <b>mainly of four round swellings "
    "(lobes) called corpora quadrigemina</b>."))
story.append(b1(
    "<b>Function:</b> the midbrain <b>receives and integrates visual, tactile and auditory "
    "inputs</b>. <i>(Stated only in the NCERT summary; the body gives the midbrain no function "
    "at all, so it is folded in here.)</i>"))

story.append(gap())

# ======================================================================================
# ---- 18.4.3 Hindbrain ---- F118-F125 (heading F118, opener F119)
# SUMMARY-UNIQUE fold #16 (cerebellum function) closes this block, which is also the home the
# inventory assigned to exercise gap 8(d) (cerebrum vs cerebellum).
# ======================================================================================
story.append(heading("18.4.3", "Hindbrain", level=2, has_table=True))

story.append(body(
    "The hindbrain comprises <b>pons, cerebellum</b> and <b>medulla</b> (also called the "
    "<b>medulla oblongata</b>)."))

story.append(data_table([
    ["Hindbrain part", "Structure", "Function"],
    ["<b>Pons</b>", "Consists of <b>fibre tracts</b>",
     "They <b>interconnect different regions of the brain</b>"],
    ["<b>Cerebellum</b>",
     "Has a <b>very convoluted surface</b> in order to provide <b>additional space for many "
     "more neurons</b>",
     "<b>Integrates information received from the semicircular canals of the ear and the "
     "auditory system</b> <i>(summary-only fact, folded in here)</i>"],
    ["<b>Medulla</b>", "<b>Connected to the spinal cord</b>",
     "Contains <b>centres which control respiration, cardiovascular reflexes</b> and <b>gastric "
     "secretions</b>"],
], col_widths=[18, 36, 46]))

story.append(gap())
story.append(keyterm(
    "<b>Brain stem</b> - <b>three major regions make up the brain stem: mid brain, pons</b> and "
    "<b>medulla oblongata</b>. The brain stem <b>forms the connections between the brain and "
    "spinal cord</b>."))

story.append(gap())
story.append(memory_aid(
    "<b>Hindbrain trio - 'PCM':</b> <b>P</b>ons (bridges brain regions), <b>C</b>erebellum "
    "(balance-and-hearing integrator, convoluted surface), <b>M</b>edulla (respiration, "
    "cardiovascular reflexes, gastric secretions). Drop the cerebellum and the remaining two, "
    "with the midbrain, are exactly the brain stem."))

story.append(gap())

# ======================================================================================
# ---- SUMMARY (Quick Recap, SS5 item 8) ---- F126 (heading F126)
# A denser rewrite of the NCERT summary (textbook p. 237), not a copy. All 18 summary
# sentences are represented; the 4 SUMMARY-UNIQUE facts were already folded into their body
# sections above and are restated here in their summary form.
# ======================================================================================
story.append(heading("Recap", "Quick Recap (NCERT Summary, rewritten)", level=1))

story.append(body(
    "The <b>neural system coordinates and integrates functions</b> as well as <b>metabolic and "
    "homeostatic activities of all the organs</b>. <b>Neurons</b>, the <b>functional units</b> "
    "of the neural system, are <b>excitable cells</b> due to a <b>differential concentration "
    "gradient of ions across the membrane</b>. The electrical potential difference across the "
    "<b>resting</b> neural membrane is the <b>'resting potential'</b>; the nerve impulse is "
    "conducted along the axon membrane as a <b>wave of depolarisation and repolarisation</b>."))

story.append(gap())
story.append(body(
    "A <b>synapse</b> is formed by the membranes of a <b>pre-synaptic</b> and a "
    "<b>post-synaptic</b> neuron, which <b>may or may not</b> be separated by a gap called the "
    "<b>synaptic cleft</b>. Chemicals involved in the transmission of impulses at <b>chemical "
    "synapses</b> are called <b>neurotransmitters</b>."))

story.append(gap())
story.append(body(
    "The human neural system consists of <b>two parts</b>: <b>(i) the central neural system "
    "(CNS)</b> and <b>(ii) the peripheral neural system</b>. The <b>CNS consists of the brain "
    "and spinal cord</b> (the NCERT summary prints <b>'spiral cord'</b>). The brain divides into "
    "<b>(i) forebrain, (ii) midbrain</b> and <b>(iii) hindbrain</b>."))

story.append(gap())
story.append(body(
    "The <b>forebrain</b> consists of <b>cerebrum, thalamus</b> and <b>hypothalamus</b>. The "
    "<b>cerebrum is longitudinally divided into two halves</b> connected by the <b>corpus "
    "callosum</b>. The <b>hypothalamus</b>, a <b>very important part of the forebrain</b>, "
    "<b>controls body temperature, eating and drinking</b>. The <b>inner parts of the cerebral "
    "hemispheres plus associated deep structures</b> form the <b>limbic system</b>, concerned "
    "with <b>olfaction, autonomic responses, regulation of sexual behaviour, expression of "
    "emotional reactions</b> and <b>motivation</b>."))

story.append(gap())
story.append(body(
    "The <b>midbrain receives and integrates visual, tactile and auditory inputs</b>. The "
    "<b>hindbrain comprises pons, cerebellum</b> and <b>medulla</b>. The <b>cerebellum "
    "integrates information received from the semicircular canals of the ear and the auditory "
    "system</b>. The <b>medulla contains centres which control respiration, cardiovascular "
    "reflexes and gastric secretions</b>, and the <b>pons consists of fibre tracts that "
    "interconnect different regions of the brain</b>."))

story.append(gap())

# ======================================================================================
# ---- EXERCISES ---- F127 (heading F127)
# All ten NCERT exercises (textbook pp. 237-238) reproduced with worked answers drawn from the
# chapter text above. Exercise 10's source lettering skips (c)-(e) and is reproduced as printed.
# ======================================================================================
story.append(heading("Ex", "EXERCISES (with worked answers)", level=1))

story.append(note(
    "All <b>ten</b> NCERT exercises are reproduced below with worked answers. Every answer is "
    "sourced from the chapter text above; the three answers that go beyond NCERT's own "
    "sentences (<b>9b master clock</b>, <b>10b saltatory conduction</b>, <b>10f cranial vs "
    "spinal nerves</b>) are flagged in place and collected in the appendix. <b>Exercise 10 is "
    "lettered (a), (b), (f) in the source</b> - the printed book skips (c)-(e), and that is "
    "reproduced, not renumbered."))

story.append(gap())
story.append(body("<b>1. Briefly describe the structure of the Brain.</b>"))
story.append(b1(
    "The brain is the <b>central information processing organ</b>, the <b>'command and control "
    "system'</b>, <b>protected by the skull</b> and wrapped in <b>cranial meninges</b> - "
    "<b>dura mater</b> (outer), <b>arachnoid</b> (very thin middle) and <b>pia mater</b> (inner, "
    "touching the brain tissue)."))
story.append(b1(
    "<b>Forebrain</b> - <b>cerebrum</b> (major part; a deep cleft divides it into left and right "
    "<b>cerebral hemispheres</b> joined by the <b>corpus callosum</b>; the folded <b>cerebral "
    "cortex</b> is the <b>grey matter</b> with motor, sensory and <b>association areas</b>, over "
    "myelinated tracts forming the <b>white matter</b>), <b>thalamus</b> (coordinating centre "
    "for sensory and motor signaling) and <b>hypothalamus</b> (temperature, eating, drinking, "
    "<b>hypothalamic hormones</b>); the <b>limbic system</b> lies inside."))
story.append(b1(
    "<b>Midbrain</b> - between thalamus/hypothalamus and pons; the <b>cerebral aqueduct</b> runs "
    "through it; the dorsal portion bears the <b>corpora quadrigemina</b> (four round swellings) "
    "and it integrates <b>visual, tactile and auditory</b> inputs."))
story.append(b1(
    "<b>Hindbrain</b> - <b>pons</b> (fibre tracts interconnecting brain regions), "
    "<b>cerebellum</b> (very convoluted surface; integrates semicircular-canal and auditory "
    "information) and <b>medulla oblongata</b> (respiration, cardiovascular reflexes, gastric "
    "secretions), connected to the <b>spinal cord</b>. <b>Mid brain + pons + medulla oblongata = "
    "brain stem</b>, the connection between brain and spinal cord (see Figure 18.4)."))

story.append(gap())
story.append(body("<b>2. Compare the following:</b>"))
story.append(body("<b>(a) Central neural system (CNS) and Peripheral neural system (PNS)</b>"))
story.append(data_table([
    ["Feature", "CNS", "PNS"],
    ["Parts", "<b>Brain</b> and <b>spinal cord</b>",
     "<b>All the nerves of the body associated with the CNS</b>"],
    ["Role", "<b>Site of information processing and control</b>",
     "<b>Carries impulses to and from the CNS</b> through <b>afferent</b> and <b>efferent</b> "
     "fibres"],
    ["Divisions", "Forebrain, midbrain, hindbrain; spinal cord",
     "<b>Somatic</b> neural system and <b>autonomic</b> neural system (the latter "
     "<b>sympathetic</b> + <b>parasympathetic</b>); the <b>visceral nervous system</b> is the "
     "part serving the viscera"],
], col_widths=[16, 34, 50]))

story.append(gap())
story.append(body("<b>(b) Resting potential and action potential</b>"))
story.append(data_table([
    ["Feature", "Resting potential", "Action potential"],
    ["Definition",
     "Electrical potential difference across the <b>resting</b> plasma membrane",
     "Electrical potential difference across the membrane <b>at the stimulated site</b> - <b>in "
     "fact termed a nerve impulse</b>"],
    ["State of the membrane", "<b>Polarised</b>", "<b>Depolarised</b> (polarity reversed)"],
    ["Charges",
     "Outer surface <b>positive</b>, inner surface <b>negative</b>",
     "Outer surface <b>negative</b>, inner side <b>positive</b>"],
    ["Permeability",
     f"More permeable to <b>{K}</b>, nearly impermeable to <b>{NA}</b>; gradients held by the "
     f"<b>sodium-potassium pump</b> (3 {NA} out for 2 {K} in)",
     f"Membrane becomes <b>freely permeable to {NA}</b>, giving a <b>rapid influx</b> of {NA}"],
], col_widths=[16, 42, 42]))

story.append(gap())
story.append(body("<b>3. Explain the following processes:</b>"))
story.append(b1(
    f"<b>(a) Polarisation of the membrane of a nerve fibre.</b> At rest the axonal membrane is "
    f"<b>comparatively more permeable to {K}</b>, <b>nearly impermeable to {NA}</b> and "
    f"<b>impermeable to the negatively charged proteins</b> of the axoplasm, so the axoplasm "
    f"holds <b>high {K}</b> + <b>negative proteins</b> and <b>low {NA}</b> while the fluid "
    f"outside holds <b>low {K}</b> and <b>high {NA}</b> - a <b>concentration gradient</b> "
    f"maintained by the <b>sodium-potassium pump</b> (<b>3 {NA} out for 2 {K} in</b>). Result: "
    f"<b>outer surface positive, inner surface negative</b> - the membrane is <b>polarised</b>, "
    f"and that potential difference is the <b>resting potential</b>."))
story.append(b1(
    f"<b>(b) Depolarisation of the membrane of a nerve fibre.</b> A <b>stimulus</b> at a site "
    f"(point <b>A</b>) makes the membrane there <b>freely permeable to {NA}</b>; the <b>rapid "
    f"{NA} influx reverses the polarity</b> so the <b>outer surface becomes negative</b> and the "
    f"<b>inner side positive</b>. The site is <b>depolarised</b> and the potential difference "
    f"there is the <b>action potential</b>, i.e. the <b>nerve impulse</b>."))
story.append(b1(
    "<b>(c) Transmission of a nerve impulse across a chemical synapse.</b> See Exercise 6 - the "
    "arriving action potential moves <b>synaptic vesicles</b> to the membrane, they <b>fuse</b> "
    "and <b>release neurotransmitters into the synaptic cleft</b>, which <b>bind specific "
    "receptors on the post-synaptic membrane</b>, <b>opening ion channels</b> whose <b>ion "
    "entry generates a new potential</b> that <b>may be excitatory or inhibitory</b>."))

story.append(gap())
story.append(body("<b>4. Draw labelled diagrams of the following:</b>"))
story.append(b1(
    "<b>(a) Neuron</b> - redraw <b>Figure 18.1</b> and label the <b>dendrites</b>, the "
    "<b>Nissl's granules</b> and <b>nucleus</b> in the <b>cell body</b>, the <b>axon</b> with "
    "its <b>Schwann cell</b> and <b>myelin sheath</b>, a <b>node of Ranvier</b>, and the "
    "<b>axon terminal</b> ending in a <b>synaptic knob</b>."))
story.append(b1(
    "<b>(b) Brain</b> - redraw <b>Figure 18.4</b> and label the <b>forebrain</b> "
    "(<b>cerebrum</b>, <b>cerebral hemisphere</b>, <b>corpus callosum</b>, <b>thalamus</b>, "
    "<b>hypothalamus</b>), the <b>midbrain</b> with its <b>cerebral aqueduct</b>, and the "
    "<b>hindbrain</b> (<b>pons</b>, <b>cerebellum</b>, <b>medulla</b>) continuing into the "
    "<b>spinal cord</b>."))

story.append(gap())
story.append(body("<b>5. Write short notes on the following:</b>"))
story.append(b1(
    "<b>(a) Neural coordination</b> - <b>coordination</b> is the process through which two or "
    "more organs <b>interact and complement</b> each other's functions; the <b>neural system</b> "
    "does this with an <b>organised network of point-to-point connections for quick "
    "coordination</b>, while the <b>endocrine system</b> provides <b>chemical integration "
    "through hormones</b>. Example: in exercise, oxygen supply, respiration rate, heart beat and "
    "blood flow rise together and return to normal afterwards."))
story.append(b1(
    "<b>(b) Forebrain</b> - <b>cerebrum + thalamus + hypothalamus</b>; cerebrum is the major "
    "part, split into <b>two cerebral hemispheres</b> joined by the <b>corpus callosum</b>, "
    "covered by the folded <b>cerebral cortex</b> (<b>grey matter</b>: motor, sensory and "
    "<b>association areas</b>) over the myelinated <b>white matter</b>; <b>thalamus</b> "
    "coordinates sensory and motor signaling; <b>hypothalamus</b> controls body temperature and "
    "the urge for eating and drinking and secretes <b>hypothalamic hormones</b>; the "
    "<b>limbic system</b> (with <b>amygdala, hippocampus</b>) handles <b>olfaction, autonomic "
    "responses, sexual behaviour, emotional reactions and motivation</b>."))
story.append(b1(
    "<b>(c) Midbrain</b> - lies <b>between the thalamus/hypothalamus and the pons</b>; the "
    "<b>cerebral aqueduct</b> runs through it; its <b>dorsal portion</b> bears <b>four round "
    "swellings, the corpora quadrigemina</b>; it <b>receives and integrates visual, tactile and "
    "auditory inputs</b> and, with pons and medulla, forms the <b>brain stem</b>."))
story.append(b1(
    "<b>(d) Hindbrain</b> - <b>pons</b> (fibre tracts interconnecting brain regions), "
    "<b>cerebellum</b> (very <b>convoluted surface</b> for more neurons; integrates "
    "<b>semicircular canal</b> and <b>auditory</b> information) and <b>medulla oblongata</b> "
    "(<b>respiration, cardiovascular reflexes, gastric secretions</b>), which is <b>connected to "
    "the spinal cord</b>."))
story.append(b1(
    "<b>(e) Synapse</b> - a <b>junction</b> formed by the membranes of a <b>pre-synaptic</b> and "
    "a <b>post-synaptic</b> neuron, which <b>may or may not</b> be separated by the <b>synaptic "
    "cleft</b>. <b>Electrical synapses</b> (membranes in very close proximity, direct current "
    "flow, <b>always faster</b>, <b>rare in our system</b>) versus <b>chemical synapses</b> "
    "(cleft crossed by <b>neurotransmitters</b>)."))

story.append(gap())
story.append(body("<b>6. Give a brief account of Mechanism of synaptic transmission.</b>"))
story.append(process_flow([
    "An <b>impulse (action potential) arrives at the axon terminal</b> of the <b>pre-synaptic</b> "
    "neuron, whose <b>vesicles are filled with neurotransmitters</b>.",
    "The impulse <b>stimulates the movement of the synaptic vesicles towards the membrane</b>.",
    "The vesicles <b>fuse with the plasma membrane</b> and <b>release their neurotransmitters "
    "into the synaptic cleft</b>.",
    "The neurotransmitters <b>bind their specific receptors on the post-synaptic membrane</b>.",
    "The binding <b>opens ion channels</b>; the <b>entering ions generate a new potential</b> in "
    "the post-synaptic neuron, which <b>may be excitatory or inhibitory</b>.",
]))

story.append(gap())
story.append(body(
    f"<b>7. Explain the role of {NA} in the generation of action potential.</b>"))
story.append(b1(
    f"At rest the membrane is <b>nearly impermeable to {NA}</b>, which is kept <b>high "
    f"outside</b> and <b>low inside</b> by the <b>sodium-potassium pump</b> (<b>3 {NA} out for "
    f"2 {K} in</b>) - this is what <b>polarises</b> the membrane."))
story.append(b1(
    f"On <b>stimulation</b> the membrane at that site becomes <b>freely permeable to {NA}</b>; "
    f"the <b>rapid influx of {NA}</b> <b>reverses the polarity</b> (outer negative, inner "
    f"positive) - <b>depolarisation</b> - and the resulting potential difference <b>is</b> the "
    f"<b>action potential / nerve impulse</b>."))
story.append(b1(
    f"The {NA} influx also drives the <b>local current</b> from the depolarised site to the site "
    f"immediately ahead, so the impulse is <b>conducted</b> along the axon; the rise in {NA} "
    f"permeability is <b>extremely short-lived</b> and is followed by a rise in <b>{K}</b> "
    f"permeability that <b>restores the resting potential</b>."))

story.append(gap())
story.append(body("<b>8. Differentiate between:</b>"))
story.append(data_table([
    ["Pair", "First member", "Second member"],
    ["<b>(a) Myelinated vs non-myelinated axons</b>",
     "<b>Enveloped with Schwann cells forming a myelin sheath</b>; gaps between adjacent sheaths "
     "are <b>nodes of Ranvier</b>; found in <b>spinal and cranial nerves</b>",
     "<b>Enclosed by a Schwann cell that does not form a myelin sheath</b>; <b>commonly</b> "
     "found in <b>autonomous</b> and <b>somatic</b> neural systems"],
    ["<b>(b) Dendrites vs axons</b>",
     "<b>Short</b>, <b>repeatedly branched</b> fibres projecting from the cell body, "
     "<b>containing Nissl's granules</b>; <b>transmit impulses towards the cell body</b>",
     "A <b>long</b> fibre with a <b>branched distal end</b>, each branch ending in a "
     "<b>synaptic knob</b> with <b>neurotransmitter vesicles</b>; <b>transmit impulses away "
     "from the cell body</b> to a synapse or neuro-muscular junction"],
    ["<b>(c) Thalamus vs hypothalamus</b>",
     "The <b>cerebrum wraps around</b> it; a <b>major coordinating centre for sensory and motor "
     "signaling</b>",
     "Lies at the <b>base of the thalamus</b>; centres for <b>body temperature, eating and "
     "drinking</b>; <b>neurosecretory cells</b> secreting <b>hypothalamic hormones</b>; with the "
     "limbic system governs <b>emotion, sexual behaviour, motivation</b>"],
    ["<b>(d) Cerebrum vs cerebellum</b>",
     "<b>Forebrain</b>; <b>major part of the human brain</b>; <b>two hemispheres</b> joined by "
     "the <b>corpus callosum</b>; folded <b>cortex</b> with motor, sensory and association "
     "areas - voluntary action, memory, intelligence, speech",
     "<b>Hindbrain</b>; <b>very convoluted surface</b> giving space for many more neurons; "
     "<b>integrates information from the semicircular canals of the ear and the auditory "
     "system</b>"],
], col_widths=[17, 41, 42]))

story.append(gap())
story.append(body("<b>9. Answer the following:</b>"))
story.append(b1(
    "<b>(a) Which part of the human brain is the most developed?</b> The <b>cerebrum</b> - it "
    "<b>forms the major part of the human brain</b>."))
story.append(b1(
    "<b>(b) Which part of our central neural system acts as a master clock?</b> The "
    "<b>hypothalamus</b> (its <b>suprachiasmatic nucleus</b>), which times the brain-controlled "
    "<b>circadian (24-hour) rhythms</b>. <i>(Answer beyond NCERT's own sentences - see the "
    "appendix.)</i>"))

story.append(gap())
story.append(body(
    "<b>10. Distinguish between:</b> <i>(source lettering: (a), (b), (f) - the book skips "
    "(c)-(e))</i>"))
story.append(b1(
    "<b>(a) Afferent neurons vs efferent neurons.</b> <b>Afferent</b> nerve fibres <b>transmit "
    "impulses from tissues/organs to the CNS</b>; <b>efferent</b> fibres <b>transmit regulatory "
    "impulses from the CNS to the concerned peripheral tissues/organs</b>."))
story.append(b1(
    "<b>(b) Impulse conduction in a myelinated vs an unmyelinated nerve fibre.</b> In an "
    "<b>unmyelinated</b> fibre the membrane is depolarised at <b>every successive point</b>, so "
    "conduction is <b>continuous and slower</b>; in a <b>myelinated</b> fibre the <b>myelin "
    "sheath insulates</b> the axon and the membrane is exposed only at the <b>nodes of "
    "Ranvier</b>, so the impulse leaps <b>node to node</b> - <b>saltatory conduction</b>, "
    "<b>faster</b> and more energy-efficient. <i>(Answer beyond NCERT's own sentences - see the "
    "appendix.)</i>"))
story.append(b1(
    "<b>(f) Cranial nerves vs spinal nerves.</b> Both are <b>PNS</b> nerves, and NCERT notes "
    "that <b>myelinated nerve fibres are found in spinal and cranial nerves</b>. <b>Cranial "
    "nerves arise from the brain</b>; <b>spinal nerves arise from the spinal cord</b>. <i>(Answer "
    "beyond NCERT's own sentences - see the appendix.)</i>"))

story.append(gap())

# ======================================================================================
# ---- APPENDIX: Terms used in the exercises (SS5 item 9, Rule 2) ----
# The three genuine exercise gaps, collected in one place and labelled as additions so no
# reader mistakes them for NCERT body text (Rule 5).
# ======================================================================================
story.append(heading("Appendix", "Terms used in the exercises", level=1, has_table=True))

story.append(body(
    "Three exercises lean on something this chapter never states. Each is answered above at the "
    "point where it belongs, and collected here so the addition is never mistaken for NCERT "
    "body text."))

story.append(data_table([
    ["Exercise", "Term the exercise assumes", "Explanation added (not in the NCERT body)"],
    ["<b>9(b)</b>", "<b>Master clock</b> of the central neural system",
     "NCERT states only that the brain controls <b>circadian (24-hour) rhythms</b>. The "
     "timekeeper is the <b>hypothalamus</b>, specifically its <b>suprachiasmatic nucleus</b>."],
    ["<b>10(b)</b>", "<b>Conduction in a myelinated vs an unmyelinated fibre</b>",
     "NCERT defines both fibre types but not their conduction. <b>Unmyelinated: continuous</b> "
     "depolarisation point by point, <b>slower</b>. <b>Myelinated: saltatory</b> - the impulse "
     "is regenerated only at the <b>nodes of Ranvier</b>, so it is <b>faster</b>."],
    ["<b>10(f)</b>", "<b>Cranial nerves vs spinal nerves</b>",
     "NCERT names them once, as the site of myelinated fibres. <b>Cranial nerves leave the "
     "brain</b>; <b>spinal nerves leave the spinal cord</b>; both belong to the <b>PNS</b> and "
     "may carry afferent fibres, efferent fibres or both."],
], col_widths=[10, 26, 64]))

story.append(gap())
story.append(note(
    "<b>Coverage note.</b> All <b>4 figures</b> of the chapter are embedded as verified "
    "monochrome assets (Figures 18.1-18.4), each followed by its full in-figure label list, so "
    "no figure required manual attention. Source spellings kept verbatim where NCERT prints "
    "them: <b>'sagital'</b> (Figure 18.4 caption), <b>'passess'</b> (18.4.2) and <b>'spiral "
    "cord'</b> (summary). Nothing in the chapter is a photograph of a person, so no such image "
    "was embedded."))


def main():
    return build_pdf(
        OUT_PDF, story,
        title="Class 11 Chapter 18 - Neural Control and Coordination (NEET notes)",
        subject="NEET Biology",
    )


if __name__ == "__main__":
    sys.exit(main())
