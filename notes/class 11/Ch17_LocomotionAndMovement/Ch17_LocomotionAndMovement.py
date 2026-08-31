"""
NCERT Class 11 Biology, Chapter 17 - Locomotion and Movement
NEET replacement notes -> A4 print-ready PDF.

Built under SUPREME COMMAND PROMPT.md v6, Pass 2: written linearly from the
frozen 193-row inventory (Ch17_LocomotionAndMovement_inventory.md) in Content
Order (SS5), importing the repo-level frozen style module `neet_template.py`
(SS0.6). No style, geometry, colour or font is re-declared here.

Block markers `# ---- N.N ----` mark every NCERT section so a Pass 3 flag can be
found and fixed in one contiguous block. Inventory row IDs are named in the
comments so any fact can be traced back to its frozen row.

FIGURE-LABEL COVERAGE (check 6): all ten figures carry their callouts as vector
artwork, so each figure is followed by a NOTE that lists its in-figure labels
verbatim (matrix rows F184-F193, 95 label strings total). That is what puts
every figure-label into the running text for check_pdf.py check 6, and it also
lets a print reader name the parts of a diagram whose labels did not survive
extraction. The four genuine "figure-only" obligations flagged in the inventory
(Blood capillary; Intervertebral disc; the Relaxed/Contracting/Maximally
Contracted staging; the Sliding/rotation and formation/breaking captions) are
carried in the running prose too, not just in the label NOTEs.

Subscripts / superscripts: the inventory stores Ca++, ADP, Pi, ATP in plain
readable form, but check_pdf.py check 5 bans Unicode sub/superscripts in the PDF
text stream, so every one is written here as a <sub> / <super> tag.

Band letters ('Z', 'A', 'I', 'H', 'M') are transcribed with straight ASCII
quotes exactly as the frozen Facts rows record them.

Source: Chapter/class 11/Chapter 17 - Locomotion and Movement.pdf
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
OUT_PDF = os.path.join(HERE, "Ch17_LocomotionAndMovement.pdf")

# Inline chemistry shorthands (check 5: tags, never Unicode sub/superscripts)
CAPP = "Ca<super>++</super>"
PI = "P<sub>i</sub>"


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
story += title_block("Locomotion and Movement")

# ======================================================================================
# ---- 17.intro ---- F002-F016 (opener F002)
# ======================================================================================
story.append(body(
    "<b>Movement is one of the significant features of living beings.</b> Animals and plants "
    "exhibit a wide range of movements. The <b>streaming of protoplasm</b> in unicellular "
    "organisms like <i>Amoeba</i> is a simple form of movement; the movement of <b>cilia, "
    "flagella and tentacles</b> is shown by many organisms; and human beings can move their "
    "<b>limbs, jaws, eyelids, tongue,</b> etc."))

story.append(keyterm(
    "<b>Locomotion</b> - some movements result in a change of place or location. Such "
    "voluntary movements are called locomotion. Walking, running, climbing, flying and "
    "swimming are all forms of locomotory movements."))

story.append(b1(
    "Locomotory structures <b>need not be different</b> from those affecting other types of "
    "movements. For example, in <i>Paramoecium</i>, cilia help in the movement of food "
    "through the cytopharynx <i>and</i> in locomotion as well; <i>Hydra</i> can use its "
    "tentacles for capturing prey <i>and</i> for locomotion; and we use our limbs for "
    "changes in body posture <i>and</i> for locomotion."))

story.append(body(
    "These observations suggest that movements and locomotion <b>cannot be studied "
    "separately</b>. The two may be linked by stating that <b>all locomotions are movements "
    "but all movements are not locomotions</b>."))

story.append(b1(
    "Methods of locomotion vary with the animal's <b>habitat</b> and the demand of the "
    "situation. However, locomotion is <b>generally</b> for the search of food, shelter, "
    "mate, suitable breeding grounds, favourable climatic conditions, or to escape from "
    "enemies/predators."))

story.append(gap())

# ======================================================================================
# ---- 17.1 TYPES OF MOVEMENT ---- F017-F028 (heading F017, opener F018)
# ======================================================================================
story.append(heading("17.1", "Types of Movement", level=1))

story.append(body(
    "Cells of the human body exhibit <b>three main types of movements</b>, namely, "
    "<b>amoeboid, ciliary and muscular</b>."))

story.append(data_table([
    ["Type", "Where it occurs", "How it works"],
    ["<b>Amoeboid</b>",
     "Specialised cells like <b>macrophages</b> and <b>leucocytes</b> in blood",
     "Effected by <b>pseudopodia</b> formed by the streaming of protoplasm (as in "
     "<i>Amoeba</i>); <b>cytoskeletal elements like microfilaments</b> are also involved."],
    ["<b>Ciliary</b>",
     "Most internal tubular organs lined by <b>ciliated epithelium</b>",
     "Coordinated cilia in the <b>trachea</b> help remove dust particles and foreign "
     "substances inhaled with air; the passage of <b>ova</b> through the female reproductive "
     "tract is also facilitated by ciliary movement."],
    ["<b>Muscular</b>",
     "Limbs, jaws, tongue, etc.",
     "Uses the <b>contractile property of muscles</b>; effectively used for locomotion and "
     "other movements by human beings and the <b>majority</b> of multicellular organisms."],
], col_widths=[16, 34, 50]))

story.append(gap())
story.append(note(
    "Locomotion requires a <b>perfect coordinated activity of the muscular, skeletal and "
    "neural systems</b>. This chapter covers the types of muscles, their structure, the "
    "mechanism of their contraction, and the important aspects of the skeletal system."))

story.append(gap())

# ======================================================================================
# ---- 17.2 MUSCLE ---- F029-F066 (heading F029, opener F030)
# ======================================================================================
story.append(heading("17.2", "Muscle", level=1))

story.append(body(
    "You have studied in Chapter 8 that <b>cilia and flagella are outgrowths of the cell "
    "membrane</b>. Flagellar movement helps in the <b>swimming of spermatozoa</b>, the "
    "maintenance of water current in the <b>canal system of sponges</b>, and in the "
    "locomotion of Protists like <i>Euglena</i>."))

story.append(keyterm(
    "<b>Muscle</b> - a specialised tissue of <b>mesodermal origin</b>. About <b>40-50 per "
    "cent</b> of the body weight of a human adult is contributed by muscles."))

story.append(b1(
    "Muscles have special properties: <b>excitability, contractility, extensibility and "
    "elasticity</b>."))

story.append(body(
    "Muscles have been classified using different criteria, namely <b>location, appearance "
    "and nature of regulation</b> of their activities. Based on their <b>location</b>, three "
    "types are identified: <b>(i) Skeletal (ii) Visceral</b> and <b>(iii) Cardiac</b>."))

story.append(data_table([
    ["Muscle type", "Location", "Appearance", "Regulation", "Chief role"],
    ["<b>Skeletal</b>",
     "Closely associated with the <b>skeletal components</b> of the body",
     "<b>Striped / striated</b> under the microscope",
     "Under <b>voluntary</b> control of the nervous system (voluntary muscles)",
     "Primarily <b>locomotory actions</b> and changes of body posture"],
    ["<b>Visceral</b>",
     "Inner walls of hollow visceral organs - alimentary canal, reproductive tract, etc.",
     "<b>No striation, smooth</b> (smooth / nonstriated muscle)",
     "<b>Not</b> under voluntary control (involuntary muscles)",
     "Transport of food through the digestive tract and gametes through the genital tract"],
    ["<b>Cardiac</b>",
     "Muscles of the <b>heart</b>; many cells assemble in a <b>branching pattern</b>",
     "<b>Striated</b>",
     "<b>Involuntary</b> - the nervous system does not control them directly",
     "Contraction of the heart"],
], col_widths=[12, 24, 20, 24, 20]))

story.append(gap())
story.append(body(
    "<b>Structure of a skeletal muscle.</b> Each organised skeletal muscle is made of a "
    "number of <b>muscle bundles</b> or <b>fascicles</b> held together by a common "
    "collagenous connective tissue layer called <b>fascia</b>. Each muscle bundle contains a "
    "number of <b>muscle fibres</b> (Figure 17.1). The bundle is also served by a "
    "<b>blood capillary</b> supply drawn in the cross-section."))

story.append(keyterm(
    "<b>Sarcolemma / sarcoplasm.</b> Each muscle fibre is lined by the plasma membrane "
    "called <b>sarcolemma</b> enclosing the <b>sarcoplasm</b>. A muscle fibre is a "
    "<b>syncitium</b> (source spelling) as the sarcoplasm contains <b>many nuclei</b>."))

story.append(b1(
    "The endoplasmic reticulum, i.e. the <b>sarcoplasmic reticulum</b> of the muscle fibres, "
    f"is the <b>store house of calcium ions</b> ({CAPP})."))
story.append(b1(
    "A characteristic feature of the muscle fibre is a large number of parallelly arranged "
    "<b>filaments</b> in the sarcoplasm called <b>myofilaments</b> or <b>myofibrils</b>."))

story.append(figure(
    "fig_17_1.png",
    "Figure 17.1 Diagrammatic cross sectional view of a muscle showing muscle bundles and "
    "muscle fibres"))
story.append(note(
    "<b>Figure 17.1 labels:</b> Fascicle (muscle bundle); Muscle fibre (muscle cell); "
    "Sarcolemma; Blood capillary."))

story.append(gap())
story.append(body(
    "<b>Banding pattern.</b> Each myofibril has <b>alternate dark and light bands</b> on it. "
    "The striated appearance is due to the distribution pattern of two important proteins - "
    "<b>Actin and Myosin</b>."))

story.append(data_table([
    ["Band / line", "Also called", "Contents"],
    ["<b>'I' band (light)</b>", "Isotropic band", "Contains <b>actin</b> (thin filament)"],
    ["<b>'A' band (dark)</b>", "Anisotropic band", "Contains <b>myosin</b> (thick filament)"],
    ["<b>'Z' line</b>", "Elastic fibre bisecting each 'I' band",
     "Thin filaments are <b>firmly attached</b> to it"],
    ["<b>'M' line</b>", "Thin fibrous membrane",
     "Holds the thick filaments together in the <b>middle of the 'A' band</b>"],
    ["<b>'H' zone</b>", "Central part of the 'A' band",
     "The part of the thick filament <b>not overlapped</b> by thin filaments - i.e. "
     "<b>thick filaments only</b>"],
], col_widths=[16, 30, 54]))

story.append(gap())
story.append(b1(
    "Both proteins are arranged as <b>rod-like structures</b>, parallel to each other and to "
    "the longitudinal axis of the myofibrils. <b>Actin filaments are thinner</b> than the "
    "myosin filaments, hence they are commonly called <b>thin</b> and <b>thick</b> filaments "
    "respectively."))
story.append(b1(
    "The <b>'A' and 'I' bands are arranged alternately</b> throughout the length of the "
    "myofibrils."))

story.append(keyterm(
    "<b>Sarcomere</b> - the portion of the myofibril between <b>two successive 'Z' lines</b>. "
    "It is the <b>functional unit of contraction</b> (Figure 17.2). (The muscle <b>fibre</b> "
    "itself is the <b>anatomical unit</b> of muscle, while the sarcomere is its functional "
    "unit.)"))

story.append(b1(
    "In a <b>resting state</b>, the edges of the thin filaments on either side of the thick "
    "filaments <b>partially overlap</b> the free ends of the thick filaments, leaving the "
    "central part of the thick filaments (the <b>'H' zone</b>) free."))

story.append(memory_aid(
    "Each <b>sarcomere</b> = one central <b>'A' band</b> (thick myosin filaments) flanked by "
    "<b>two half 'I' bands</b> (thin actin filaments), the whole unit marked off by "
    "<b>'Z' lines</b> at both ends. Mnemonic for what shortens: only the <b>'I'</b> band and "
    "the <b>'H'</b> zone shrink on contraction - the <b>'A'</b> band never does."))

story.append(figure(
    "fig_17_2.png",
    "Figure 17.2 Diagrammatic representation of (a) anatomy of a muscle fibre showing a "
    "sarcomere (b) a sarcomere"))
story.append(note(
    "<b>Figure 17.2 labels:</b> Z line; A band; I band; H zone; Sarcomere; panels (a) and "
    "(b)."))

story.append(gap())

# ======================================================================================
# ---- 17.2.1 Structure of Contractile Proteins ---- F067-F077 (heading F067, opener F068)
# ======================================================================================
story.append(heading("17.2.1", "Structure of Contractile Proteins", level=2))

story.append(body(
    "<b>Actin (thin) filament.</b> Each actin filament is made of two <b>'F' (filamentous) "
    "actins</b> helically wound to each other. Each 'F' actin is a polymer of monomeric "
    "<b>'G' (Globular) actins</b>."))

story.append(b1(
    "Two filaments of another protein, <b>tropomyosin</b>, also run close to the 'F' actins "
    "throughout their length."))
story.append(b1(
    "A complex protein <b>Troponin</b> is distributed at regular intervals on the "
    "tropomyosin. In the <b>resting state</b>, a subunit of troponin <b>masks the active "
    "binding sites for myosin</b> on the actin filaments (Figure 17.3a)."))

story.append(gap())
story.append(body(
    "<b>Myosin (thick) filament.</b> Each myosin filament is also a polymerised protein. "
    "Many monomeric proteins called <b>Meromyosins</b> (Figure 17.3b) constitute one thick "
    "filament."))

story.append(data_table([
    ["Part of a meromyosin", "Name", "Feature"],
    ["Globular <b>head</b> + short arm", "<b>Heavy meromyosin (HMM)</b>",
     "Projects outwards at regular distance and angle from the surface of the filament, "
     "forming the <b>cross arm</b>; the head is an <b>active ATPase enzyme</b> with binding "
     "sites for <b>ATP</b> and active sites for <b>actin</b>."],
    ["<b>Tail</b>", "<b>Light meromyosin (LMM)</b>",
     "The rod-like shaft of the monomer."],
], col_widths=[24, 24, 52]))

story.append(figure(
    "fig_17_3.png",
    "Figure 17.3 (a) An actin (thin) filament (b) Myosin monomer (Meromyosin)"))
story.append(note(
    "<b>Figure 17.3 labels:</b> Troponin; Tropomyosin; F actin; Actin binding sites; ATP "
    "binding sites; Head; Cross arm; panels (a) and (b)."))

story.append(gap())

# ======================================================================================
# ---- 17.2.2 Mechanism of Muscle Contraction ---- F078-F101 (heading F078, opener F079)
# ======================================================================================
story.append(heading("17.2.2", "Mechanism of Muscle Contraction", level=2))

story.append(keyterm(
    "<b>Sliding filament theory</b> - the mechanism of muscle contraction is best explained "
    "by this theory, which states that contraction of a muscle fibre takes place by the "
    "<b>sliding of the thin filaments over the thick filaments</b>."))

story.append(keyterm(
    "<b>Motor unit</b> - a motor neuron along with the muscle fibres connected to it. The "
    "junction between a motor neuron and the sarcolemma of the muscle fibre is the "
    "<b>neuromuscular junction</b> or <b>motor-end plate</b>."))

story.append(gap())
story.append(body("<b>The contraction cycle</b>, step by step:"))
story.append(process_flow([
    "Contraction is initiated by a signal sent by the <b>central nervous system (CNS)</b> "
    "via a <b>motor neuron</b>.",
    "The neural signal reaching the neuromuscular junction releases a neurotransmitter "
    "(<b>Acetyl choline</b>), which generates an <b>action potential</b> in the sarcolemma.",
    f"The action potential spreads through the muscle fibre and causes the release of "
    f"<b>calcium ions ({CAPP})</b> into the sarcoplasm.",
    f"The rise in {CAPP} level leads to the binding of calcium with a subunit of "
    "<b>troponin</b> on the actin filaments, which <b>removes the masking</b> of the active "
    "sites for myosin.",
    "Using energy from <b>ATP hydrolysis</b>, the <b>myosin head</b> binds to the exposed "
    "active sites on actin to form a <b>cross bridge</b> (Figure 17.4).",
    "The cross bridge <b>pulls the attached actin filaments towards the centre of the 'A' "
    "band</b>; the 'Z' lines attached to these actins are also pulled inwards, "
    "<b>shortening the sarcomere</b> - i.e. contraction.",
    f"The myosin head, releasing the <b>ADP and {PI}</b>, goes back to its relaxed state. A "
    "<b>new ATP</b> binds and the cross bridge is <b>broken</b> (Figure 17.4).",
    f"The ATP is again hydrolysed by the myosin head and the cycle of cross-bridge formation "
    "and breakage repeats, causing further <b>sliding</b>.",
    f"The process continues till the {CAPP} ions are <b>pumped back</b> into the sarcoplasmic "
    "cisternae, masking the actin filaments again; the 'Z' lines return to their original "
    "position - i.e. <b>relaxation</b>.",
]))

story.append(gap())
story.append(b1(
    "During shortening (contraction), the <b>'I' bands get reduced</b>, whereas the "
    "<b>'A' bands retain their length</b> (Figure 17.5). The figure stages this across three "
    "states of the sarcomere: <b>Relaxed</b>, <b>Contracting</b> and <b>Maximally "
    "Contracted</b>."))
story.append(b1(
    "The <b>reaction time</b> of the fibres can vary in different muscles."))

story.append(figure(
    "fig_17_4.png",
    "Figure 17.4 Stages in cross bridge formation, rotation of head and breaking of cross "
    "bridge"))
story.append(note(
    "<b>Figure 17.4 labels:</b> Actin filament; Myosin filament; P; ADP; ATP; Cross bridge; "
    "Myosin head; Sliding/rotation of the head; (Formation of cross bridge); (Breaking of "
    "cross bridge)."))

story.append(gap())
story.append(figure(
    "fig_17_5.png",
    "Figure 17.5 Sliding-filament theory of muscle contraction (movement of the thin "
    "filaments and the relative size of the I band and H zones)"))
story.append(note(
    "<b>Figure 17.5 labels:</b> H zone; I band; A band; Z line; Two Sarcomeres; and the "
    "three staged states Relaxed, Contracting and Maximally Contracted."))

story.append(gap())
story.append(body(
    "<b>Fatigue.</b> Repeated activation of the muscles can lead to the accumulation of "
    "<b>lactic acid</b> due to the <b>anaerobic breakdown of glycogen</b> in them, causing "
    "<b>fatigue</b>."))

story.append(body(
    "<b>Red vs White fibres.</b> Muscles are classified as Red and White fibres based "
    "primarily on the amount of the red-coloured oxygen-storing pigment <b>myoglobin</b>."))

story.append(data_table([
    ["Feature", "Red fibres", "White fibres"],
    ["Myoglobin", "<b>High</b> - gives a reddish appearance", "<b>Low</b> - appear pale / whitish"],
    ["Mitochondria", "<b>Plenty</b>", "<b>Few</b>"],
    ["Sarcoplasmic reticulum", "Lower", "<b>High</b>"],
    ["Energy source", "Use stored O<sub>2</sub> for ATP - <b>aerobic muscles</b>",
     "Depend on the <b>anaerobic</b> process for energy"],
], col_widths=[24, 38, 38]))

story.append(gap())

# ======================================================================================
# ---- 17.3 SKELETAL SYSTEM ---- F102-F149 (heading F102, opener F103)
# ======================================================================================
story.append(heading("17.3", "Skeletal System", level=1))

story.append(body(
    "The <b>skeletal system</b> consists of a framework of <b>bones and a few "
    "cartilages</b>. This system has a significant role in the movement shown by the body - "
    "imagine chewing food without jaw bones and walking around without limb bones."))

story.append(keyterm(
    "<b>Bone and cartilage</b> are specialised <b>connective tissues</b>. Bone has a very "
    "<b>hard matrix</b> due to <b>calcium salts</b>; cartilage has a slightly <b>pliable "
    "matrix</b> due to <b>chondroitin salts</b>."))

story.append(b1(
    "In human beings, the skeletal system is made up of <b>206 bones</b> and a few "
    "cartilages, grouped into two principal divisions - the <b>axial</b> and the "
    "<b>appendicular</b> skeleton."))

story.append(gap())
story.append(heading("17.3.axial", "Axial Skeleton", level=3))
story.append(body(
    "The <b>axial skeleton</b> comprises <b>80 bones</b> distributed along the main axis of "
    "the body: the <b>skull, vertebral column, sternum and ribs</b>."))

story.append(body(
    "<b>Skull</b> (Figure 17.6). The skull is composed of two sets of bones - <b>cranial and "
    "facial</b> - that total <b>22 bones</b>. Cranial bones are <b>8</b> in number and form "
    "the hard protective outer covering, the <b>cranium</b>, for the brain. The facial "
    "region is made up of <b>14</b> skeletal elements that form the front part of the skull."))
story.append(b1(
    "A single <b>U-shaped bone called hyoid</b> is present at the base of the buccal cavity."))
story.append(b1(
    "Each middle ear contains <b>three tiny bones - Malleus, Incus and Stapes</b>, "
    "collectively called <b>Ear Ossicles</b>."))
story.append(b1(
    "The skull articulates with the superior region of the vertebral column with the help of "
    "<b>two occipital condyles (dicondylic skull)</b>."))

story.append(figure(
    "fig_17_6.png",
    "Figure 17.6 Diagrammatic view of human skull"))
story.append(note(
    "<b>Figure 17.6 labels:</b> Parietal bone; Frontal bone; Temporal bone; Occipital bone; "
    "Occipital condyle; Sphenoid bone; Ethmoid bone; Lacrimal bone; Nasal bone; Zygomatic "
    "bone; Maxilla; Mandible; Hyoid bone."))

story.append(gap())
story.append(body(
    "<b>Vertebral column</b> (Figure 17.7) is formed by <b>26 serially arranged units called "
    "vertebrae</b> and is dorsally placed. It extends from the base of the skull and "
    "constitutes the main framework of the trunk."))
story.append(b1(
    "Each vertebra has a central hollow portion (<b>neural canal</b>) through which the "
    "<b>spinal cord</b> passes. The first vertebra is the <b>atlas</b>, and it articulates "
    "with the occipital condyles."))
story.append(b1(
    "The column is differentiated into <b>cervical (7), thoracic (12), lumbar (5), sacral "
    "(1-fused) and coccygeal (1-fused)</b> regions, starting from the skull. The number of "
    "<b>cervical vertebrae is seven in almost all mammals</b>, including human beings. "
    "(Adjacent vertebrae are separated by an <b>intervertebral disc</b> of cartilage, which "
    "forms the cartilaginous joint discussed in 17.4.)"))
story.append(b1(
    "The vertebral column <b>protects the spinal cord, supports the head</b>, and serves as "
    "the point of attachment for the ribs and the musculature of the back."))

story.append(figure(
    "fig_17_7.png",
    "Figure 17.7 Vertebral column (right lateral view)"))
story.append(note(
    "<b>Figure 17.7 labels:</b> Cervical vertebra; Thoracic vertebra; Lumbar vertebra; "
    "Intervertebral disc; Sacrum; Coccyx."))

story.append(gap())
story.append(body(
    "<b>Sternum and ribs.</b> The <b>sternum</b> is a flat bone on the ventral midline of "
    "the thorax. There are <b>12 pairs of ribs</b>. Each rib is a thin flat bone connected "
    "dorsally to the vertebral column and ventrally to the sternum; it has <b>two "
    "articulation surfaces</b> on its dorsal end and is hence called <b>bicephalic</b>."))

story.append(data_table([
    ["Rib set", "Pairs", "Attachment"],
    ["<b>True ribs</b>", "First <b>7</b> pairs",
     "Dorsally attached to the thoracic vertebrae; ventrally connected to the sternum with "
     "<b>hyaline cartilage</b>"],
    ["<b>Vertebrochondral (false) ribs</b>", "<b>8th, 9th, 10th</b> pairs",
     "Do <b>not</b> articulate directly with the sternum; join the <b>seventh rib</b> with "
     "hyaline cartilage"],
    ["<b>Floating ribs</b>", "Last <b>2</b> pairs (11th, 12th)",
     "<b>Not connected ventrally</b>"],
], col_widths=[30, 22, 48]))

story.append(b1(
    "Thoracic vertebrae, ribs and sternum together form the <b>rib cage</b> (Figure 17.8)."))

story.append(figure(
    "fig_17_8.png",
    "Figure 17.8 Ribs and rib cage"))
story.append(note(
    "<b>Figure 17.8 labels:</b> rib pairs numbered 1 to 12; True ribs; False ribs; Floating "
    "ribs; Sternum; Ribs; Vertebral column."))

story.append(gap())
story.append(heading("17.3.append", "Appendicular Skeleton", level=3))
story.append(keyterm(
    "<b>Appendicular skeleton</b> - the bones of the limbs along with their girdles. Each "
    "limb is made of <b>30 bones</b>."))

story.append(data_table([
    ["Limb", "Bones (with counts)"],
    ["<b>Hand / fore limb</b> (Figure 17.9)",
     "Humerus, radius and ulna, <b>carpals</b> (wrist bones - <b>8</b>), <b>metacarpals</b> "
     "(palm bones - <b>5</b>) and <b>phalanges</b> (digits - <b>14</b>)."],
    ["<b>Leg / hind limb</b> (Figure 17.10)",
     "<b>Femur</b> (thigh bone - the <b>longest bone</b>), tibia and fibula, <b>tarsals</b> "
     "(ankle bones - <b>7</b>), <b>metatarsals</b> (<b>5</b>) and <b>phalanges</b> (digits - "
     "<b>14</b>)."],
], col_widths=[26, 74]))

story.append(b1(
    "A cup-shaped bone called <b>patella</b> covers the knee ventrally (the <b>knee cap</b>)."))
story.append(b1(
    "<b>Pectoral</b> and <b>Pelvic</b> girdle bones help in the articulation of the upper and "
    "lower limbs respectively with the axial skeleton. Each girdle is formed of two halves."))

story.append(gap())
story.append(body("<b>Pectoral girdle</b> (Figure 17.9):"))
story.append(b1(
    "Each half consists of a <b>clavicle</b> and a <b>scapula</b>."))
story.append(b1(
    "<b>Scapula</b> is a large <b>triangular flat bone</b> situated in the dorsal part of the "
    "thorax between the <b>second and the seventh ribs</b>. Its dorsal, flat, triangular body "
    "has a slightly elevated ridge called the <b>spine</b>, which projects as a flat, "
    "expanded process called the <b>acromion</b>; the clavicle articulates with this."))
story.append(b1(
    "Below the acromion is a depression called the <b>glenoid cavity</b>, which articulates "
    "with the <b>head of the humerus</b> to form the <b>shoulder joint</b>."))
story.append(b1(
    "Each <b>clavicle</b> is a long slender bone with two curvatures, commonly called the "
    "<b>collar bone</b>."))

story.append(figure(
    "fig_17_9.png",
    "Figure 17.9 Right pectoral girdle and upper arm. (frontal view)"))
story.append(note(
    "<b>Figure 17.9 labels:</b> Clavicle; Scapula; Humerus; Radius; Ulna; Carpals; "
    "Metacarpals; Phalanges."))

story.append(gap())
story.append(body("<b>Pelvic girdle</b> (Figure 17.10):"))
story.append(b1(
    "Consists of <b>two coxal bones</b>. Each coxal bone is formed by the fusion of "
    "<b>three bones - ilium, ischium and pubis</b>."))
story.append(b1(
    "At the point of fusion is a cavity called the <b>acetabulum</b>, to which the thigh bone "
    "(femur) articulates."))
story.append(b1(
    "The two halves of the pelvic girdle meet ventrally to form the <b>pubic symphysis</b>, "
    "containing fibrous cartilage."))

story.append(figure(
    "fig_17_10.png",
    "Figure 17.10 Right pelvic girdle and lower limb bones (frontal view)"))
story.append(note(
    "<b>Figure 17.10 labels:</b> Ilium; Pubis; Ischium; Coxal bone; Sacrum; Femur; Patella; "
    "Tibia; Fibula; Tarsals; Metatarsals; Phalanges."))

story.append(gap())
story.append(memory_aid(
    "<b>Pectoral vs Pelvic girdle</b> at a glance: pectoral = <b>clavicle + scapula</b> "
    "(articulates the arm at the glenoid cavity/shoulder); pelvic = one <b>coxal bone</b> per "
    "half = <b>ilium + ischium + pubis</b> fused (articulates the thigh at the acetabulum)."))

story.append(gap())

# ======================================================================================
# ---- 17.4 JOINTS ---- F150-F164 (heading F150, opener F151)
# ======================================================================================
story.append(heading("17.4", "Joints", level=1))

story.append(body(
    "<b>Joints</b> are essential for all types of movements involving the bony parts of the "
    "body; locomotory movements are no exception."))

story.append(keyterm(
    "<b>Joints</b> - points of contact between bones, or between bones and cartilages. The "
    "force generated by the muscles is used to carry out movement through joints, where the "
    "joint acts as a <b>fulcrum</b>. The movability at these joints varies depending on "
    "different factors."))

story.append(body(
    "Joints have been classified into <b>three major structural forms</b>, namely, "
    "<b>fibrous, cartilaginous and synovial</b>."))

story.append(data_table([
    ["Joint type", "Movement", "Example"],
    ["<b>Fibrous</b>", "Do <b>not allow any movement</b>",
     "Flat <b>skull bones</b> fusing end-to-end via dense fibrous connective tissue as "
     "<b>sutures</b> to form the cranium"],
    ["<b>Cartilaginous</b>", "Permit <b>limited</b> movements",
     "Joint between <b>adjacent vertebrae</b> in the vertebral column"],
    ["<b>Synovial</b>",
     "Allow <b>considerable</b> movement; help in locomotion and many other movements",
     "Characterised by a fluid-filled <b>synovial cavity</b> between the articulating "
     "surfaces of the two bones"],
], col_widths=[20, 34, 46]))

story.append(gap())
story.append(body(
    "<b>Synovial joints</b> are characterised by the presence of a <b>fluid-filled synovial "
    "cavity</b> between the articulating surfaces of the two bones. Such an <b>arrangement</b> "
    "allows considerable movement. Sub-types with examples:"))
story.append(b1("<b>Ball and socket joint</b> - between humerus and pectoral girdle."))
story.append(b1("<b>Hinge joint</b> - knee joint."))
story.append(b1("<b>Pivot joint</b> - between atlas and axis."))
story.append(b1("<b>Gliding joint</b> - between the carpals."))
story.append(b1("<b>Saddle joint</b> - between carpal and metacarpal of the thumb."))

story.append(gap())

# ======================================================================================
# ---- 17.5 DISORDERS OF MUSCULAR AND SKELETAL SYSTEM ---- F165-F171 (heading F165)
# ======================================================================================
story.append(heading("17.5", "Disorders of Muscular and Skeletal System", level=1))

story.append(data_table([
    ["Disorder", "Description"],
    ["<b>Myasthenia gravis</b>",
     "<b>Auto immune disorder</b> affecting the <b>neuromuscular junction</b>, leading to "
     "fatigue, weakening and paralysis of skeletal muscle."],
    ["<b>Muscular dystrophy</b>",
     "<b>Progressive degeneration</b> of skeletal muscle, mostly due to a <b>genetic "
     "disorder</b>."],
    ["<b>Tetany</b>",
     f"Rapid spasms (wild contractions) in muscle due to <b>low {CAPP}</b> in body fluid."],
    ["<b>Arthritis</b>", "<b>Inflammation of joints</b>."],
    ["<b>Osteoporosis</b>",
     "<b>Age-related</b> disorder characterised by <b>decreased bone mass</b> and increased "
     "chances of fractures. <b>Decreased levels of estrogen</b> is a common cause."],
    ["<b>Gout</b>",
     "Inflammation of joints due to the accumulation of <b>uric acid crystals</b>."],
], col_widths=[22, 78]))

story.append(gap())
story.append(note(
    "Chapter map recap: <b>movement</b> (amoeboid / ciliary / muscular) leads to "
    "<b>muscle</b> (skeletal / visceral / cardiac), whose contractile unit is the "
    "<b>sarcomere</b>; contraction runs by the <b>sliding filament theory</b>; muscles act "
    "on the <b>skeletal system</b> (206 bones: axial + appendicular) through <b>joints</b>. "
    "Disorders can strike either the muscular side (myasthenia gravis, muscular dystrophy, "
    "tetany) or the skeletal/joint side (arthritis, osteoporosis, gout)."))


def main():
    return build_pdf(
        OUT_PDF, story,
        title="Class 11 Chapter 17 - Locomotion and Movement (NEET notes)",
        subject="NEET Biology",
    )


if __name__ == "__main__":
    sys.exit(main())
