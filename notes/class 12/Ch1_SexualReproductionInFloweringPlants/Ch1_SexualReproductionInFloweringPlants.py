"""
NCERT Class 12 Biology, Chapter 1 - Sexual Reproduction in Flowering Plants
NEET replacement notes -> A4 print-ready PDF.

Built under SUPREME COMMAND PROMPT.md v6, Pass 2: written linearly from the
frozen 255-row inventory (Ch1_SexualReproductionInFloweringPlants_inventory.md),
importing the repo-level frozen style module `neet_template.py` (v6 §0.6). No
style, geometry, colour or font is re-declared here.

Block markers `# ---- N.N ----` mark every NCERT section so a Pass 3 flag can be
found and fixed in one contiguous block. Inventory row IDs are named in the
comments so any fact can be traced back to its frozen row.

Pass 1 items actioned in this pass:
  1. SUMMARY-UNIQUE F252 ("tetrasporangiate") folded into 1.2.1 anther description.
  2. SUMMARY-UNIQUE F253 ("archesporium") folded into 1.2.2 nucellus description.
  3. Placentation (exercise-gap, referenced only in the source) carried as a
     one-line Class XI recall NOTE in 1.2.2.
  4. Every in-figure label of all 12 labelled figures is written into running
     text as an explicit "labelled in the figure" walk-through sentence, so the
     text stands alone even if a print of the figure is illegible (§4.4 Step 4).
  5. Fig 1.4, 1.6 and 1.10 are photographic/product plates with no in-figure
     labels; they carry a caption row only (no label row) - this is deliberate,
     not a failed harvest.
  6. The p2 Panchanan Maheshwari portrait is NOT embedded (§4.4 hard no); the
     chapter carries no scientist-profile block because the source page 2 plate
     is a photograph only.
  7. Fig 1.9 is embedded as its three cleanly separable sub-panels (a, b, c) so
     each sits inline at its own topic (autogamy / xenogamy / cleistogamy);
     every panel keeps the verbatim NCERT figure number in its caption.

Source: Chapter/class 12/Chapter 1 - Sexual Reproduction in Flowering Plants.pdf
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

# sys.path bootstrap: walk up until we find the repo-level neet_template.py (§0.6)
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
OUT_PDF = os.path.join(HERE, "Ch1_SexualReproductionInFloweringPlants.pdf")


def figure(asset_name, caption_text, max_width_cm=15.9):
    """Chapter-local binding of the shared figure() helper (§0.6)."""
    return _shared_figure(asset_name, caption_text, ASSETS, max_width_cm=max_width_cm)


def body(text):
    return Paragraph(text, STYLES["Body"])


def b1(text):
    return Paragraph("<bullet>&bull;</bullet>" + text, STYLES["Bullet1"])


def b2(text):
    return Paragraph("<bullet>-</bullet>" + text, STYLES["Bullet2"])


def gap(h=4):
    return Spacer(1, h)


story = []

# ======================================================================================
# ---- Title block (§5 item 1) ----
# ======================================================================================
story += title_block("Sexual Reproduction in Flowering Plants")

# ======================================================================================
# ---- Unit 6 opener (F001-F003) ----
# ======================================================================================
story.append(body(
    "<b>Reproduction becomes a vital process without which species cannot survive for "
    "long.</b> Each individual leaves its progeny by asexual or sexual means. The sexual "
    "mode of reproduction enables creation of new variants, so that survival advantage "
    "is enhanced."))
story.append(gap())

# ======================================================================================
# ---- 1.1 FLOWER - A FASCINATING ORGAN OF ANGIOSPERMS (F004-F011) ----
# ======================================================================================
story.append(heading("1.1", "FLOWER &mdash; A FASCINATING ORGAN OF ANGIOSPERMS", level=1))
story.append(body(
    "Human beings have had an intimate relationship with flowers since time immemorial. "
    "<b>All flowering plants show sexual reproduction</b>, and the fruits and seeds we use "
    "are <b>the end products of sexual reproduction</b>. To a biologist, flowers "
    "<b>are morphological and embryological marvels and the sites of sexual "
    "reproduction</b>."))
story.append(body(
    "The two units of sexual reproduction do not develop in the same place: the male unit "
    "develops in the <b>anther</b> and the female unit in the <b>ovary</b>."))
# Fig 1.1 - caption F010, label walk-through F011
story.append(body(
    "In a longitudinal section (L.S.) of a typical flower, the parts labelled in the figure "
    "are, from outside inwards, the <b>sepal</b> and the <b>petal</b> of the outer "
    "protective and attractive whorls, then the male part made of the <b>anther</b> "
    "borne on its <b>filament</b>, and the female part made of the <b>stigma</b> at the "
    "top, the <b>style</b> beneath it and the swollen <b>ovary</b> at the base."))
story.append(figure(
    "fig_1_1.png",
    "Fig. 1.1 &mdash; A diagrammatic representation of L.S. of a flower. Labelled: stigma, "
    "style, anther, petal, filament, sepal, ovary.",
    max_width_cm=11.0))

# ======================================================================================
# ---- 1.2 PRE-FERTILISATION : STRUCTURES AND EVENTS (F012-F017) ----
# ======================================================================================
story.append(heading("1.2", "PRE-FERTILISATION : STRUCTURES AND EVENTS", level=1))
story.append(body(
    "Much before the actual flower is seen on a plant, the decision that the plant is going "
    "to flower has taken place. Several hormonal and structural changes are initiated which "
    "lead to the differentiation and further development of the <b>floral primordium</b>. "
    "<b>Inflorescences</b> are formed which bear the floral buds and then the flowers."))
story.append(keyterm(
    "The <b>androecium</b> consists of a whorl of <b>stamens</b> representing the male "
    "reproductive organ; the <b>gynoecium</b> represents the female reproductive organ."))
story.append(gap())

# ======================================================================================
# ---- 1.2.1 Stamen, Microsporangium and Pollen Grain (F018-F028) ----
# ======================================================================================
story.append(heading("1.2.1", "Stamen, Microsporangium and Pollen Grain", level=2))
story.append(body(
    "A typical stamen has two parts &mdash; the <b>filament</b>, the long and slender stalk, "
    "and the <b>anther</b>, the terminal generally bilobed structure. The <b>proximal end of "
    "the filament is attached to the thalamus or the petal</b> of the flower. The number and "
    "length of stamens are variable in flowers of different species."))
story.append(b1(
    " A typical angiosperm anther is <b>bilobed</b>, with each lobe having two <b>theca</b> "
    "&mdash; that is, they are <b>dithecous</b>. Often a longitudinal groove runs lengthwise "
    "separating the theca."))
story.append(b1(
    " The anther is a <b>four-sided (tetragonal)</b> structure consisting of <b>four "
    "microsporangia</b> located at the corners, <b>two in each lobe</b>. Because it carries "
    "four microsporangia, a typical anther is also described as "
    "<b>tetrasporangiate</b>."))  # F252 (SUMMARY-UNIQUE folded here)
story.append(b1(
    " The microsporangia develop further and become <b>pollen sacs</b>. They extend "
    "longitudinally all through the length of an anther and are packed with pollen grains."))
# Fig 1.2 - caption F027, label walk-through F028
story.append(body(
    "The figure below labels the <b>filament (stalk)</b> and the <b>anther</b> of the stamen, "
    "and in the cut anther the four <b>pollen sacs</b> full of <b>pollen grains</b>, together "
    "with the <b>line of dehiscence</b> along which the anther will later split open."))
story.append(figure(
    "fig_1_2.png",
    "Fig. 1.2 &mdash; (a) A typical stamen; (b) three-dimensional cut section of an anther. "
    "Labelled: anther, pollen grains, pollen sacs, line of dehiscence, filament (stalk).",
    max_width_cm=7.4))

# ---- 1.2.1 Structure of microsporangium (F029-F037) ----
story.append(heading("1.2.1", "Structure of microsporangium", level=3))
story.append(body(
    "In a transverse section, a typical microsporangium appears <b>near circular in "
    "outline</b>. It is <b>generally surrounded by four wall layers</b> &mdash; the "
    "epidermis, endothecium, middle layers and the tapetum."))
story.append(data_table([
    ["Wall layer (outside to inside)", "Function"],
    ["Epidermis", "One of the outer three layers: protection, and helps in dehiscence of "
                  "the anther to release the pollen"],
    ["Endothecium", "As above &mdash; protection and dehiscence"],
    ["Middle layers", "As above &mdash; protection and dehiscence"],
    ["Tapetum (innermost)", "Nourishes the developing pollen grains. Its cells possess dense "
                            "cytoplasm and generally have more than one nucleus"],
], col_widths=[1.0, 2.4]))
story.append(gap())
story.append(body(
    "A group of compactly arranged homogenous cells called the <b>sporogenous tissue</b> "
    "occupies the centre of each microsporangium."))
# Fig 1.3 - caption F036, label walk-through F037
story.append(body(
    "In the figure below, the young anther shows the <b>epidermis</b>, the "
    "<b>endothecium</b>, the <b>middle layers</b> and the <b>tapetum</b> enclosing the "
    "<b>sporogenous tissue</b> and its <b>microspore mother cells</b>; the sterile tissue "
    "joining the two lobes is the <b>connective</b>, and the dehisced anther has shed its "
    "<b>pollen grains</b>."))
story.append(figure(
    "fig_1_3.png",
    "Fig. 1.3 &mdash; (a) Transverse section of a young anther; (b) Enlarged view of one "
    "microsporangium showing wall layers; (c) A mature dehisced anther. Labelled: connective, "
    "epidermis, endothecium, sporogenous tissue, tapetum, middle layers, microspore mother "
    "cells, pollen grains.",
    max_width_cm=15.0))

# ---- 1.2.1 Microsporogenesis (F038-F044) ----
story.append(heading("1.2.1", "Microsporogenesis", level=3))
story.append(body(
    "As the anther develops, the cells of the <b>sporogenous tissue</b> undergo "
    "<b>meiotic divisions</b> to form <b>microspore tetrads</b>. Each such cell is "
    "<b>a potential pollen or microspore mother cell</b>."))
story.append(keyterm(
    "<b>Microsporogenesis</b> &mdash; the process of formation of microspores from a "
    "<b>pollen mother cell (PMC)</b> through meiosis."))
story.append(process_flow([
    "<b>Sporogenous tissue</b> in the centre of the microsporangium: compact, homogenous "
    "cells, each a potential <b>pollen mother cell (PMC)</b> or microspore mother cell.",
    "<b>Meiosis</b> in the PMC.",
    "<b>Microspore tetrad</b> &mdash; the microspores, as they are formed, are arranged in a "
    "cluster of four cells.",
    "As the anthers mature and dehydrate, the microspores <b>dissociate</b> from each other "
    "and develop into <b>pollen grains</b>.",
    "Inside each microsporangium <b>several thousands</b> of microspores or pollen grains are "
    "formed, and they are released with the <b>dehiscence of the anther</b>.",
]))
story.append(gap())

# ---- 1.2.1 Pollen grain (F045-F072) ----
story.append(heading("1.2.1", "Pollen grain", level=3))
story.append(body(
    "The pollen grains represent the <b>male gametophytes</b>. Pollen grains are generally "
    "<b>spherical</b>, measuring about <b>25-50 micrometers in diameter</b>. It has a "
    "prominent <b>two-layered wall</b>."))
story.append(b1(
    " <b>Exine</b> &mdash; the hard outer layer, made up of <b>sporopollenin</b>, which is "
    "<b>one of the most resistant organic material known</b>. It can withstand high "
    "temperatures and strong acids and alkali, and <b>no enzyme that degrades sporopollenin "
    "is so far known</b>."))
story.append(b1(
    " The exine has prominent apertures called <b>germ pores</b> where sporopollenin is "
    "absent. Because of the presence of sporopollenin, pollen grains are <b>well-preserved "
    "as fossils</b>."))
story.append(b1(
    " <b>Intine</b> &mdash; the inner wall of the pollen grain, a <b>thin and continuous</b> "
    "layer made up of <b>cellulose and pectin</b>."))
story.append(b1(
    " The cytoplasm of the pollen grain is surrounded by a <b>plasma membrane</b>."))
story.append(gap())
story.append(body(
    "<b>Contents of a mature pollen grain.</b> When the pollen grain is mature it contains "
    "<b>two cells</b>, the vegetative cell and the generative cell."))
story.append(data_table([
    ["Cell", "Size and contents"],
    ["Vegetative cell", "Bigger; has abundant food reserve and a large irregularly shaped "
                        "<b>nucleus</b>"],
    ["Generative cell", "Small, and floats in the cytoplasm of the vegetative cell; spindle "
                        "shaped with dense cytoplasm and a nucleus"],
], col_widths=[1.0, 2.6]))
story.append(gap())
story.append(b1(
    " In <b>over 60 per cent</b> of angiosperms, pollen grains are shed at this "
    "<b>2-celled stage</b>."))
story.append(b1(
    " In the remaining species, the generative cell divides mitotically to give rise to the "
    "<b>two male gametes before pollen grains are shed</b> (<b>3-celled stage</b>)."))
# Fig 1.4 (F062) and Fig 1.5 (F063) with label walk-through F064
story.append(figure(
    "fig_1_4.png",
    "Fig. 1.4 &mdash; Scanning electron micrographs of a few pollen grains. The micrographs "
    "show the sculptured exine of pollen of different species; this plate carries no "
    "in-figure labels.",
    max_width_cm=13.0))
story.append(body(
    "The maturation series in the figure below labels the <b>vacuoles</b> of the young "
    "microspore and its <b>nucleus</b>, the <b>asymmetric spindle</b> of the unequal division "
    "that follows, and the resulting <b>vegetative cell</b> and <b>generative cell</b> of the "
    "mature 2-celled pollen grain."))
story.append(figure(
    "fig_1_5.png",
    "Fig. 1.5 &mdash; (a) Enlarged view of a pollen grain tetrad; (b) stages of a microspore "
    "maturing into a pollen grain. Labelled: vacuoles, nucleus, asymmetric spindle, vegetative "
    "cell, generative cell.",
    max_width_cm=5.0))
story.append(note(
    "Pollen grains of many species <b>cause severe allergies and bronchial afflictions</b>, "
    "leading to chronic respiratory disorders &mdash; asthma, bronchitis, etc. "
    "<b>Parthenium</b> or <b>carrot grass</b>, which came into India as a contaminant with "
    "imported wheat, has become ubiquitous and causes pollen allergy."))
story.append(gap())
story.append(body(
    "<b>Pollen grains are rich in nutrients.</b> Pollen tablets are used as food supplements, "
    "and such consumption is claimed to increase the performance of athletes and race "
    "horses."))
story.append(figure(
    "fig_1_6.png",
    "Fig. 1.6 &mdash; Pollen products. The plate shows commercial pollen tablets and syrups "
    "sold as food supplements; it carries no in-figure labels.",
    max_width_cm=14.0))
story.append(gap())
story.append(body(
    "<b>Viability of pollen grains.</b> Pollen grains have to land on the stigma "
    "<b>before they lose viability</b> if they have to bring about fertilisation. The period "
    "for which pollen grains remain viable is <b>highly variable</b> and depends on the "
    "prevailing temperature and humidity."))
story.append(data_table([
    ["Group", "Viability of shed pollen"],
    ["Some cereals &mdash; rice, wheat", "Lose viability within <b>30 minutes</b> of release"],
    ["Some members of Rosaceae, Leguminoseae and Solanaceae",
     "Maintain viability for <b>months</b>"],
    ["Stored pollen (a large number of species)",
     "Can be stored for <b>years in liquid nitrogen</b> (minus 196 degrees C); such stored "
     "pollen is used as <b>pollen banks</b>, similar to seed banks, in crop breeding "
     "programmes"],
], col_widths=[1.3, 2.4]))
story.append(gap())

# ======================================================================================
# ---- 1.2.2 The Pistil, Megasporangium (ovule) and Embryo sac (F073-F085) ----
# ======================================================================================
story.append(heading("1.2.2", "The Pistil, Megasporangium (ovule) and Embryo sac", level=2))
story.append(body(
    "The <b>gynoecium</b> represents the female reproductive part of the flower. The "
    "gynoecium may consist of a <b>single pistil (monocarpellary)</b> or may have "
    "<b>more than one pistil (multicarpellary)</b>. When there is more than one, the pistils "
    "may be <b>fused together (syncarpous)</b> or may be <b>free (apocarpous)</b>."))
story.append(body(
    "<b>Each pistil has three parts</b> &mdash; the stigma, style and ovary."))
story.append(b1(" <b>Stigma</b> &mdash; serves as a <b>landing platform for pollen grains</b>."))
story.append(b1(" <b>Style</b> &mdash; the elongated slender part beneath the stigma."))
story.append(b1(
    " <b>Ovary</b> &mdash; the basal bulged part of the pistil. Inside the ovary is the "
    "<b>ovarian cavity (locule)</b>, and the <b>placenta</b> is located inside the ovarian "
    "cavity."))
story.append(b1(
    " Arising from the placenta are the <b>megasporangia</b>, commonly called <b>ovules</b>. "
    "The number of ovules in an ovary may be <b>one</b> (wheat, paddy, mango) to "
    "<b>many</b> (papaya, water melon, orchids)."))
story.append(note(
    "<b>Class XI recall &mdash; placentation.</b> The arrangement of ovules on the placenta "
    "inside the ovary is called placentation, and its types (marginal, axile, parietal, basal, "
    "free central) were studied with flower morphology in Class XI; this chapter assumes that "
    "recall and does not redefine them."))
# Fig 1.7 - caption F084, label walk-through F085
story.append(body(
    "The figure below labels the <b>stigma</b>, <b>style</b> and <b>ovary</b> of the pistil "
    "standing on the <b>thalamus</b>, the <b>syncarpous ovary</b> whose fused <b>carpels</b> "
    "are visible in section, and, in the ovule, the <b>funicle</b>, the <b>hilum</b>, the "
    "<b>micropyle</b> at the <b>micropylar pole</b>, the <b>outer integument</b> and "
    "<b>inner integument</b>, the <b>nucellus</b>, the <b>embryo sac</b> and the "
    "<b>chalazal pole</b> at the opposite end."))
story.append(figure(
    "fig_1_7.png",
    "Fig. 1.7 &mdash; (a) A dissected flower of Hibiscus showing pistil (other floral parts "
    "have been removed); (b) Multicarpellary, syncarpous pistil of <i>Papaver</i>; "
    "(c) A multicarpellary, apocarpous gynoecium of <i>Michelia</i>; (d) A diagrammatic view "
    "of a typical anatropous ovule. Labelled: stigma, style, ovary, thalamus, syncarpous "
    "ovary, carpels, hilum, funicle, micropyle, micropylar pole, outer integument, inner "
    "integument, nucellus, embryo sac, chalazal pole.",
    max_width_cm=15.5))

# ---- 1.2.2 The Megasporangium (Ovule) (F086-F095) ----
story.append(heading("1.2.2", "The Megasporangium (Ovule)", level=3))
story.append(body(
    "Let us familiarise ourselves with the structure of a typical angiosperm ovule."))
story.append(b1(
    " The ovule is a <b>small structure attached to the placenta</b> by means of a stalk "
    "called <b>funicle</b>."))
story.append(b1(
    " The body of the ovule fuses with the funicle in the region called <b>hilum</b>; thus, "
    "hilum represents the <b>junction between ovule and funicle</b>."))
story.append(b1(
    " Each ovule has <b>one or two protective envelopes</b> called <b>integuments</b>. "
    "Integuments encircle the nucellus <b>except at the tip</b>, where a small opening called "
    "the <b>micropyle</b> is organised."))
story.append(b1(
    " Opposite the micropylar end is the <b>chalaza</b>, representing the <b>basal part</b> "
    "of the ovule."))
story.append(b1(
    " Enclosed within the integuments is a mass of cells called the <b>nucellus</b>. Cells of "
    "the nucellus have <b>abundant reserve food materials</b>. It is within this central "
    "nucellar tissue that the <b>archesporium</b> differentiates, and a cell of the "
    "archesporium becomes the megaspore mother cell."))  # F253 (SUMMARY-UNIQUE folded here)
story.append(b1(
    " Located in the nucellus is the <b>embryo sac</b> or <b>female gametophyte</b>. An ovule "
    "<b>generally</b> has a <b>single embryo sac formed from a megaspore</b>."))
story.append(gap())

# ---- 1.2.2 Megasporogenesis (F096-F102) ----
story.append(heading("1.2.2", "Megasporogenesis", level=3))
story.append(keyterm(
    "<b>Megasporogenesis</b> &mdash; the process of formation of megaspores from the "
    "megaspore mother cell."))
story.append(b1(
    " Ovules <b>generally differentiate a single megaspore mother cell (MMC)</b> in the "
    "<b>micropylar region of the nucellus</b>. It is a large cell containing dense cytoplasm "
    "and a prominent nucleus."))
story.append(b1(
    " The MMC undergoes <b>meiotic division</b>. Meiosis results in the production of "
    "<b>four megaspores</b>."))
# Fig 1.8 - caption F101, label walk-through F102
story.append(body(
    "The figure below labels the <b>micropylar end</b> and the <b>chalazal end</b> of the "
    "ovule, the <b>nucellus</b> carrying the large <b>megaspore mother cell</b>, then the "
    "<b>megaspore dyad</b> and the <b>megaspore tetrad</b>; in the mature embryo sac it "
    "labels the two <b>synergids</b> with their <b>filiform apparatus</b>, the <b>egg</b>, "
    "the <b>central cell</b> with its <b>2 polar nuclei</b> (also labelled simply as "
    "<b>polar nuclei</b>), and the three <b>antipodals</b>."))
story.append(figure(
    "fig_1_8.png",
    "Fig. 1.8 &mdash; (a) Parts of the ovule showing a large megaspore mother cell, a dyad "
    "and a tetrad of megaspores; (b) 2, 4, and 8-nucleate stages of embryo sac and a mature "
    "embryo sac; (c) A diagrammatic representation of the mature embryo sac. Labelled: "
    "micropylar end, nucellus, megaspore mother cell, megaspore dyad, megaspore tetrad, "
    "synergids, egg, central cell, 2 polar nuclei, antipodals, chalazal end, polar nuclei, "
    "filiform apparatus.",
    max_width_cm=15.0))

# ---- 1.2.2 Female gametophyte (F103-F115) ----
story.append(heading("1.2.2", "Female gametophyte", level=3))
story.append(body(
    "In a <b>majority</b> of flowering plants, <b>one of the megaspores is functional</b> "
    "while the <b>other three degenerate</b>. Only the functional megaspore develops into the "
    "female gametophyte (embryo sac); this method of development of the embryo sac from a "
    "single megaspore is termed <b>monosporic development</b>."))
story.append(process_flow([
    "<b>Functional megaspore</b> &mdash; its nucleus divides mitotically to form two nuclei "
    "which move to the opposite poles, forming the <b>2-nucleate embryo sac</b>.",
    "<b>Two more sequential mitotic nuclear divisions</b> result in the formation of the "
    "<b>4-nucleate</b> and later the <b>8-nucleate</b> stages of the embryo sac. These "
    "mitotic divisions are <b>strictly free nuclear</b> &mdash; that is, nuclear divisions "
    "are not followed immediately by cell wall formation.",
    "After the 8-nucleate stage, <b>cell walls are laid down</b>, leading to the organisation "
    "of the typical female gametophyte or embryo sac.",
    "<b>Six of the eight nuclei</b> are surrounded by cell walls and organised into cells; "
    "the remaining <b>two nuclei, called polar nuclei</b>, are situated below the egg "
    "apparatus in the large central cell.",
]))
story.append(gap())
story.append(data_table([
    ["Position in the embryo sac", "Cells", "Notes"],
    ["Micropylar end", "<b>Egg apparatus</b> &mdash; three cells grouped together: "
                       "<b>two synergids and one egg cell</b>",
     "The synergids have special cellular thickenings at the micropylar tip called the "
     "<b>filiform apparatus</b>, which play an important role in <b>guiding the pollen tubes "
     "into the synergid</b>"],
    ["Chalazal end", "Three cells called the <b>antipodals</b>", "&mdash;"],
    ["Centre", "The <b>large central cell</b>", "Has <b>two polar nuclei</b>"],
], col_widths=[0.9, 1.6, 1.6]))
story.append(gap())
story.append(note(
    "A typical angiosperm embryo sac, at maturity, though <b>8-nucleate</b> is "
    "<b>7-celled</b> &mdash; six organised cells (2 synergids + 1 egg + 3 antipodals) plus "
    "the one large central cell that still holds two free polar nuclei."))
story.append(memory_aid(
    "Embryo sac census &mdash; <b>&quot;2 + 1 + 3 + 1 = 7 cells, 8 nuclei&quot;</b>: 2 "
    "synergids, 1 egg, 3 antipodals, 1 central cell; the central cell alone carries 2 nuclei, "
    "which is where the extra nucleus comes from."))
story.append(gap())

# ======================================================================================
# ---- 1.2.3 Pollination (F116-F119) ----
# ======================================================================================
story.append(heading("1.2.3", "Pollination", level=2))
story.append(body(
    "In the preceding sections you have learnt that the male and female gametes in flowering "
    "plants are produced in the <b>pollen grain</b> and <b>embryo sac</b>, respectively. As "
    "<b>both types of gametes are non-motile</b>, they have to be brought together for "
    "fertilisation to occur."))
story.append(keyterm(
    "<b>Pollination</b> &mdash; transfer of pollen grains (shed from the anther) to the "
    "stigma of a pistil."))

# ---- 1.2.3 Kinds of Pollination (F120-F137) ----
story.append(heading("1.2.3", "Kinds of Pollination", level=3))
story.append(body(
    "Depending on the <b>source of pollen</b>, pollination can be divided into "
    "<b>three types</b>."))
story.append(data_table([
    ["Type", "Pollen travels from ... to ...", "Genetic consequence"],
    ["<b>Autogamy</b>", "Anther to the stigma of the <b>same flower</b>",
     "Self-pollination"],
    ["<b>Geitonogamy</b>", "Anther to the stigma of <b>another flower of the same plant</b>",
     "Functionally cross-pollination (needs a pollinating agent), but <b>genetically similar "
     "to autogamy</b>, since the pollen grains come from the same plant"],
    ["<b>Xenogamy</b>", "Anther to the stigma of a <b>different plant</b>",
     "The <b>only</b> type of pollination which during pollination brings <b>genetically "
     "different</b> types of pollen grains to the stigma"],
], col_widths=[0.8, 1.8, 2.2]))
story.append(gap())

story.append(heading("1.2.3", "Autogamy", level=3))
story.append(body(
    "In this type, <b>pollination is achieved within the same flower</b> &mdash; pollen is "
    "transferred from the anther to the stigma of the same flower. In a normal flower which "
    "opens and exposes the anthers and the stigma, <b>complete autogamy is rather rare</b>. "
    "Autogamy in such flowers requires <b>synchrony in pollen release and stigma "
    "receptivity</b>, and also, the anthers and the stigma should <b>lie close to each "
    "other</b>."))
story.append(figure(
    "fig_1_9a.png",
    "Fig. 1.9 (a) &mdash; Self-pollinated flowers.",
    max_width_cm=4.2))
story.append(body(
    "Some plants produce <b>two kinds of flowers</b>:"))
story.append(b1(
    " <b>Chasmogamous flowers</b> &mdash; similar to flowers of other species, with "
    "<b>exposed anthers and stigma</b> (for example <i>Viola</i>, <i>Oxalis</i> and "
    "<i>Commelina</i>). The chasmogamous flower is the one labelled in the figure below "
    "alongside the closed buds."))
story.append(b1(
    " <b>Cleistogamous flowers</b> &mdash; which <b>do not open at all</b>. Cleistogamous "
    "flowers are <b>invariably autogamous</b>, as there is <b>no chance of cross-pollen "
    "landing on the stigma</b>, and they produce <b>assured seed-set even in the absence of "
    "pollinators</b>."))
story.append(figure(
    "fig_1_9c.png",
    "Fig. 1.9 (c) &mdash; Cleistogamous flowers. Labelled: chasmogamous flower, cleistogamous "
    "flowers &mdash; the same plant bears both kinds.",
    max_width_cm=7.0))

story.append(heading("1.2.3", "Geitonogamy", level=3))
story.append(body(
    "<b>Transfer of pollen grains from the anther to the stigma of another flower of the same "
    "plant.</b> Although geitonogamy is <b>functionally cross-pollination</b> involving a "
    "pollinating agent, <b>genetically it is similar to autogamy</b> since the pollen grains "
    "come from the same plant."))

story.append(heading("1.2.3", "Xenogamy", level=3))
story.append(body(
    "<b>Transfer of pollen grains from anther to the stigma of a different plant.</b> This is "
    "the <b>only</b> type of pollination which during pollination brings <b>genetically "
    "different types of pollen grains</b> to the stigma."))
story.append(figure(
    "fig_1_9b.png",
    "Fig. 1.9 (b) &mdash; Cross pollinated flowers.",
    max_width_cm=5.1))

# ---- 1.2.3 Agents of Pollination (F138-F165) ----
story.append(heading("1.2.3", "Agents of Pollination", level=3))
story.append(body(
    "Plants use <b>two abiotic (wind and water)</b> and <b>one biotic (animals)</b> agents to "
    "achieve pollination. <b>Majority of plants use biotic agents</b> for pollination; only a "
    "<b>small proportion</b> of plants use abiotic agents."))
story.append(body(
    "Because pollen transfer by abiotic agents is not directed towards the target, the flowers "
    "produce <b>enormous amount of pollen</b> when compared to the number of ovules available "
    "for pollination."))
story.append(data_table([
    ["Abiotic agent", "Facts to remember"],
    ["<b>Wind</b>",
     "Pollination by wind is <b>more common amongst abiotic pollinations</b>. It requires "
     "pollen grains that are <b>light and non-sticky</b>. Such flowers often possess "
     "<b>well-exposed stamens</b> so that the pollen is easily dispersed, and a "
     "<b>large often-feathery stigma</b> to easily trap air-borne pollen grains. "
     "Wind-pollinated flowers often have a <b>single ovule in each ovary</b> and "
     "<b>numerous flowers packed into an inflorescence</b>; a familiar example is the "
     "<b>corn cob</b>. Wind-pollination is <b>quite common in grasses</b>."],
    ["<b>Water</b>",
     "Pollination by water is <b>quite rare</b> in flowering plants and is limited to "
     "<b>about 30 genera, mostly monocotyledons</b>. (Water is, however, a regular mode of "
     "transport for the male gametes among the <b>lower plant groups such as algae, "
     "bryophytes and pteridophytes</b>.) Examples: <i>Vallisneria</i> and <i>Hydrilla</i>, "
     "and several marine sea-grasses such as <i>Zostera</i>. In <i>Vallisneria</i>, the "
     "<b>female flower</b> reaches the surface of water by its long stalk and the <b>male "
     "flowers</b> or pollen grains are released on to the surface of water. In another group, "
     "such as seagrasses, female flowers <b>remain submerged</b> in water and the pollen "
     "grains are released <b>inside the water</b>; in these the pollen is <b>long, ribbon "
     "like</b>. In most of the water-pollinated species, pollen grains are protected from "
     "wetting by a <b>mucilaginous covering</b>."],
], col_widths=[0.7, 3.4]))
story.append(gap())
story.append(note(
    "<b>Both wind and water pollinated flowers are not very colourful and do not produce "
    "nectar.</b> Colour and nectar are advertisements aimed at animals, and an abiotic agent "
    "cannot be advertised to."))
story.append(figure(
    "fig_1_10.png",
    "Fig. 1.10 &mdash; A wind-pollinated plant showing compact inflorecence and well-exposed "
    "stamens. This photographic plate carries no in-figure labels.",
    max_width_cm=7.6))
story.append(body(
    "In the water-pollination panel of the figure below, the <b>female flower</b> of "
    "<i>Vallisneria</i> is labelled at the water surface with its <b>stigma</b> exposed, and "
    "the released <b>male flower</b> is labelled floating towards it."))
story.append(figure(
    "fig_1_11.png",
    "Fig. 1.11 &mdash; (a) Pollination by water in <i>Vallisneria</i>; (b) Insect pollination. "
    "Labelled: female flower, stigma, male flower.",
    max_width_cm=8.0))
story.append(gap())
story.append(body(
    "<b>Biotic agents (animals).</b> <b>Bees, butterflies, flies, beetles, wasps, ants, "
    "moths, birds (sunbirds and humming birds) and bats</b> are the common pollinating agents. "
    "Among the animals, <b>insects, particularly bees are the dominant biotic pollinating "
    "agents</b>. Even <b>larger animals</b> such as some <b>primates (lemurs)</b>, "
    "<b>arboreal (tree-dwelling) rodents</b>, or even <b>reptiles (gecko lizard and garden "
    "lizard)</b> have also been reported as pollinators."))
story.append(b1(
    " <b>Majority of insect-pollinated flowers are large, colourful, fragrant and rich in "
    "nectar.</b> When the flowers are small, a number of flowers are clustered into an "
    "inflorescence to make them conspicuous."))
story.append(b1(
    " The flowers pollinated by <b>flies and beetles</b> secrete <b>foul odours</b> to "
    "attract these animals."))
story.append(b1(
    " <b>Nectar and pollen grains are the usual floral rewards.</b> Pollen of "
    "animal-pollinated flowers is <b>generally sticky</b>, so the visiting animal gets a "
    "coating of pollen on its body and brings about pollination on contact with the stigma of "
    "the next flower."))
story.append(b1(
    " In some species floral rewards are in providing <b>safe places to lay eggs</b>; an "
    "example is that of the tallest flower of <i>Amorphophallus</i> (the flower itself is "
    "about <b>6 feet in height</b>)."))
story.append(b1(
    " A similar relationship exists between a <b>species of moth</b> and the plant "
    "<i>Yucca</i>, where <b>both species &mdash; moth and the plant &mdash; cannot complete "
    "their life cycles without each other</b>."))
story.append(b1(
    " Many floral visitors consume pollen or nectar <b>without bringing about pollination</b>. "
    "Such floral visitors are referred to as <b>pollen/nectar robbers</b>."))
story.append(gap())

# ---- 1.2.3 Outbreeding Devices (F166-F173) ----
story.append(heading("1.2.3", "Outbreeding Devices", level=3))
story.append(body(
    "<b>Majority of flowering plants produce hermaphrodite flowers</b> and pollen grains are "
    "likely to come in contact with the stigma of the same flower. <b>Continued "
    "self-pollination result in inbreeding depression.</b> Flowering plants have therefore "
    "developed many devices to <b>discourage self-pollination and to encourage "
    "cross-pollination</b>."))
story.append(data_table([
    ["Device", "How it prevents selfing"],
    ["1. Non-synchrony", "<b>Pollen release and stigma receptivity are not "
                         "synchronised</b> &mdash; either the pollen is released before the "
                         "stigma becomes receptive, or the stigma becomes receptive much "
                         "before the release of pollen"],
    ["2. Different positions", "<b>The anther and stigma are placed at different positions</b> "
                              "so that the pollen cannot come in contact with the stigma of "
                              "the same flower"],
    ["3. <b>Self-incompatibility</b>",
     "A <b>genetic mechanism</b>; it prevents self-pollen (from the same flower or other "
     "flowers of the same plant) from fertilising the ovules by <b>inhibiting pollen "
     "germination or pollen tube growth in the pistil</b>"],
    ["4. Unisexual flowers",
     "Production of <b>unisexual flowers</b>. If both male and female flowers are present on "
     "the same plant (<b>monoecious</b>, as in castor and maize), autogamy is prevented but "
     "<b>not geitonogamy</b>. If male and female flowers are on different plants "
     "(<b>dioecious</b>, as in papaya), <b>both autogamy and geitonogamy are prevented</b>"],
], col_widths=[1.0, 2.8]))
story.append(gap())

# ---- 1.2.3 Pollen-pistil Interaction (F174-F191) ----
story.append(heading("1.2.3", "Pollen-pistil Interaction", level=3))
story.append(body(
    "<b>Pollination does not guarantee the transfer of the right type of pollen</b> "
    "(compatible pollen of the same species as the stigma). The pistil has the ability to "
    "<b>recognise the pollen</b>, whether it is of the <b>right type (compatible)</b> or of "
    "the <b>wrong type (incompatible)</b>."))
story.append(b1(
    " If it is of the <b>right type</b>, the pistil <b>accepts</b> the pollen and promotes "
    "post-pollination events that leads to fertilisation."))
story.append(b1(
    " If the pollen is of the <b>wrong type</b>, the pistil <b>rejects</b> the pollen by "
    "preventing pollen germination on the stigma or the pollen tube growth in the style."))
story.append(b1(
    " This <b>dialogue</b> is mediated by <b>chemical components of the pollen interacting "
    "with those of the pistil</b>."))
story.append(process_flow([
    "The pollen grain <b>germinates on the stigma</b> to produce a <b>pollen tube</b> through "
    "one of the <b>germ pores</b>.",
    "The <b>pollen tube grows through the tissues of the stigma and style</b> and reaches the "
    "<b>ovary</b>.",
    "Male gametes: in plants that shed pollen in the <b>two-celled</b> condition, the "
    "<b>generative cell divides and forms the two male gametes during the growth of pollen "
    "tube</b> in the stigma; in plants which shed pollen in the <b>three-celled</b> condition, "
    "pollen tubes carry the <b>two male gametes from the beginning</b>.",
    "The pollen tube, after reaching the ovary, <b>enters the ovule through the "
    "micropyle</b> and then <b>enters one of the synergids through the filiform "
    "apparatus</b>.",
]))
story.append(gap())
story.append(keyterm(
    "<b>Pollen-pistil interaction</b> &mdash; all these events, from pollen deposition on the "
    "stigma until pollen tubes enter the ovule."))
# Fig 1.12 - caption F190, label walk-through F191
story.append(body(
    "The figure below labels the growing <b>pollen tube</b> with its <b>vegetative "
    "nucleus</b> and the <b>male gametes</b> it carries, and, in the enlarged egg apparatus, "
    "the <b>synergid</b> with its <b>filiform apparatus</b>, the <b>egg cell</b> and its "
    "<b>egg nucleus</b> bounded by the <b>plasma membrane</b>, the <b>central cell</b> with "
    "the <b>polar nuclei</b>, and an <b>antipodal</b> cell at the far end."))
story.append(figure(
    "fig_1_12.png",
    "Fig. 1.12 &mdash; (a) Pollen grains germinating on the stigma; (b) Pollen tubes growing "
    "through the style; (c) L.S. of pistil showing path of pollen tube growth; (d) enlarged "
    "view of an egg apparatus showing entry of pollen tube into a synergid; (e) Discharge of "
    "male gametes into a synergid and the movements of the sperms, one into the egg and the "
    "other into the central cell. Labelled: pollen tube, antipodal, polar nuclei, egg cell, "
    "synergid, central cell, egg nucleus, plasma membrane, filiform apparatus, male gametes, "
    "vegetative nucleus.",
    max_width_cm=15.5))
story.append(note(
    "<b>Artificial hybridisation</b> is one of the <b>major approaches of crop improvement "
    "programme</b>. Two techniques make sure that only the desired pollen reaches the stigma. "
    "<b>Emasculation</b> &mdash; removal of anthers from the flower bud <b>before the anther "
    "dehisces</b>, using a pair of forceps. <b>Bagging</b> &mdash; emasculated flowers have to "
    "be covered with a bag of suitable size, generally made up of <b>butter paper</b>, to "
    "prevent contamination of its stigma with unwanted pollen. If the <b>female parent "
    "produces unisexual flowers, there is no need for emasculation</b> &mdash; the female "
    "flower buds are simply bagged before they open."))
story.append(gap())

# ======================================================================================
# ---- 1.3 DOUBLE FERTILISATION (F192-F198) ----
# ======================================================================================
story.append(heading("1.3", "DOUBLE FERTILISATION", level=1))
story.append(body(
    "After entering one of the synergids, the pollen tube <b>releases the two male gametes "
    "into the cytoplasm of the synergid</b>. Two fusions then follow."))
story.append(process_flow([
    "<b>Syngamy.</b> One of the male gametes moves towards the <b>egg cell</b> and fuses with "
    "its nucleus, thus completing syngamy. This results in the formation of a <b>diploid "
    "cell, the zygote</b>.",
    "<b>Triple fusion.</b> The other male gamete moves towards the <b>two polar nuclei</b> "
    "located in the <b>central cell</b> and fuses with them to produce a <b>triploid primary "
    "endosperm nucleus (PEN)</b>. As this involves the fusion of <b>three haploid nuclei</b> "
    "it is termed triple fusion.",
    "The central cell after triple fusion becomes the <b>primary endosperm cell (PEC)</b> and "
    "develops into the <b>endosperm</b>, while the <b>zygote develops into an embryo</b>.",
]))
story.append(gap())
story.append(keyterm(
    "<b>Double fertilisation</b> &mdash; since two types of fusions, <b>syngamy</b> and "
    "<b>triple fusion</b>, take place in an embryo sac, the phenomenon is termed double "
    "fertilisation, <b>an event unique to flowering plants</b>."))
story.append(gap())

# ======================================================================================
# ---- 1.4 POST-FERTILISATION : STRUCTURES AND EVENTS (F199-F200) ----
# ======================================================================================
story.append(heading("1.4", "POST-FERTILISATION : STRUCTURES AND EVENTS", level=1))
story.append(body(
    "Following double fertilisation, events of <b>endosperm and embryo development</b>, "
    "<b>maturation of ovule(s) into seed(s)</b> and <b>ovary into fruit</b>, are collectively "
    "termed <b>post-fertilisation events</b>."))

# ---- 1.4.1 Endosperm (F201-F207) ----
story.append(heading("1.4.1", "Endosperm", level=2))
story.append(body(
    "<b>Endosperm development precedes embryo development.</b> The primary endosperm cell "
    "divides repeatedly and forms a <b>triploid endosperm tissue</b>. The cells of this tissue "
    "are filled with reserve food materials and are used for the nutrition of the developing "
    "embryo."))
story.append(process_flow([
    "In the <b>most common type of endosperm development</b>, the <b>PEN</b> undergoes "
    "<b>successive nuclear divisions</b> to give rise to <b>free nuclei</b>. This stage of "
    "endosperm development is called <b>free-nuclear endosperm</b>.",
    "Subsequently <b>cell wall formation occurs</b> and the endosperm becomes "
    "<b>cellular</b>.",
]))
story.append(gap())
story.append(note(
    "The <b>coconut water</b> from tender coconut is nothing but <b>free-nuclear "
    "endosperm</b> (made up of thousands of nuclei), and the surrounding white kernel is the "
    "<b>cellular endosperm</b>."))
story.append(body(
    "Endosperm <b>may</b> either be <b>completely consumed by the developing embryo</b> "
    "(e.g., pea, groundnut, beans) before seed maturation, or it <b>may persist in the mature "
    "seed</b> (e.g. castor and coconut) and be used up during germination."))

# ---- 1.4.2 Embryo (F208-F221) ----
story.append(heading("1.4.2", "Embryo", level=2))
story.append(body(
    "Embryo develops at the <b>micropylar end of the embryo sac</b> where the zygote is "
    "situated. <b>Most zygotes divide only after certain amount of endosperm is formed.</b> "
    "This is an <b>adaptation to provide assured nutrition</b> to the developing embryo."))
story.append(body(
    "The <b>early stages of embryo development (embryogeny) are similar in both "
    "monocotyledons and dicotyledons</b>: the zygote gives rise to the <b>proembryo</b> and "
    "subsequently to the <b>globular</b> and <b>heart-shaped</b> embryos, and finally to the "
    "<b>mature embryo</b>."))
# Fig 1.13 - caption F218, label walk-through F219
story.append(body(
    "In the figure below the fertilised embryo sac labels the <b>zygote</b>, the "
    "<b>primary endosperm nucleus</b> inside the <b>primary endosperm cell</b>, the "
    "<b>degenerating synergids</b> at the micropylar end and the <b>degenerating antipodal "
    "cells</b> at the chalazal end. The embryo series labels the <b>globular embryo</b>, the "
    "<b>heart-shaped embryo</b> and the mature embryo, in which the <b>suspensor</b> anchors "
    "the embryo and the <b>radicle</b>, the <b>cotyledon</b> and the <b>plumule</b> are "
    "already distinct."))
story.append(figure(
    "fig_1_13.png",
    "Fig. 1.13 &mdash; (a) Fertilised embryo sac showing zygote and Primary Endosperm Nucleus "
    "(PEN); (b) Stages in embryo development in a dicot [shown in reduced size as compared to "
    "(a)]. Labelled: degenerating synergids, zygote, primary endosperm cell, primary endosperm "
    "nucleus, degenerating antipodal cells, suspensor, radicle, cotyledon, plumule, globular "
    "embryo, heart-shaped embryo.",
    max_width_cm=15.5))
story.append(data_table([
    ["Part", "Dicotyledonous embryo", "Monocotyledonous embryo (grass family)"],
    ["Cotyledons", "<b>Two cotyledons</b>, borne on an <b>embryonal axis</b>",
     "<b>Only one cotyledon</b>; in the grass family the cotyledon is called "
     "<b>scutellum</b>, situated towards one side (<b>lateral</b>) of the embryonal axis"],
    ["Above the cotyledons", "The portion of embryonal axis above the level of cotyledons is "
                             "the <b>epicotyl</b>, which terminates with the <b>plumule</b> "
                             "or stem tip",
     "Epicotyl has a <b>shoot apex</b> and a few <b>leaf primordia</b> enclosed in a hollow "
     "foliar structure, the <b>coleoptile</b>"],
    ["Below the cotyledons", "The cylindrical portion below the level of cotyledons is the "
                             "<b>hypocotyl</b>, that terminates at its lower end in the "
                             "<b>radicle</b> or root tip; the root tip is covered with a "
                             "<b>root cap</b>",
     "The embryonal axis has the <b>radicle</b> and <b>root cap</b> enclosed in an "
     "undifferentiated sheath called <b>coleorrhiza</b> (also spelt coleorhiza)"],
], col_widths=[0.8, 1.9, 2.0]))
story.append(gap())
# Fig 1.14 - caption F220, label walk-through F221
story.append(body(
    "The figure below labels, in the dicot embryo, the <b>plumule</b>, the two "
    "<b>cotyledons</b>, the <b>hypocotyl</b>, the <b>radicle</b> and its <b>root cap</b>; and "
    "in the grass embryo the <b>scutellum</b>, the <b>coleoptile</b> enclosing the "
    "<b>shoot apex</b>, the <b>epiblast</b> lying opposite the scutellum, and the "
    "<b>coleorhiza</b> sheathing the radicle."))
story.append(figure(
    "fig_1_14.png",
    "Fig. 1.14 &mdash; (a) A typical dicot embryo; (b) L.S. of an embryo of grass. Labelled: "
    "plumule, cotyledons, hypocotyl, radicle, root cap, scutellum, coleoptile, shoot apex, "
    "epiblast, coleorhiza.",
    max_width_cm=4.9))

# ---- 1.4.3 Seed (F222-F243) ----
story.append(heading("1.4.3", "Seed", level=2))
story.append(body(
    "In angiosperms, the <b>seed is the final product of sexual reproduction</b>. It is often "
    "described as a <b>fertilised ovule</b>. Seeds are formed inside fruits."))
story.append(body(
    "A seed typically consists of <b>seed coat(s), cotyledon(s) and an embryo axis</b>."))
story.append(data_table([
    ["Seed type", "Endosperm at maturity", "Examples"],
    ["<b>Non-albuminous</b>", "<b>No residual endosperm</b>, as it is completely consumed "
                              "during embryo development", "Pea, groundnut"],
    ["<b>Albuminous</b>", "<b>Retain a part of endosperm</b>, as it is not completely used up "
                          "during embryo development", "Wheat, maize, barley, castor"],
], col_widths=[0.9, 2.4, 1.1]))
story.append(gap())
story.append(keyterm(
    "<b>Perisperm</b> &mdash; in some seeds such as <b>black pepper and beet</b>, remnants of "
    "nucellus are also persistent; this residual, persistent nucellus is the perisperm."))
story.append(b1(
    " <b>Integuments of ovules harden as tough protective seed coats.</b> The "
    "<b>micropyle</b> remains as a <b>small pore in the seed coat</b>, which facilitates "
    "entry of oxygen and water into the seed during germination."))
story.append(b1(
    " As the seed matures, its <b>water content is reduced</b> and seeds become relatively "
    "dry (<b>10-15 per cent moisture by mass</b>). The general metabolic activity of the "
    "embryo slows down."))
story.append(b1(
    " The embryo <b>may</b> enter a state of inactivity called <b>dormancy</b>, or, if "
    "favourable conditions are available (adequate moisture, oxygen and suitable "
    "temperature), they <b>germinate</b>."))
story.append(gap())
story.append(body("<b>From ovary to fruit.</b>"))
story.append(b1(
    " The wall of the ovary develops into the <b>wall of fruit</b> called <b>pericarp</b>. "
    "The fruits <b>may</b> be <b>fleshy</b> as in guava, orange, mango, etc., or <b>may</b> "
    "be <b>dry</b>, as in groundnut, and mustard, etc."))
story.append(b1(
    " In a few species such as <b>apple, strawberry, cashew</b>, etc., the <b>thalamus</b> "
    "also contributes to fruit formation. Such fruits are called <b>false fruits</b>. "
    "<b>Most fruits however develop only from the ovary and are called true fruits.</b>"))
story.append(b1(
    " In a few species, fruits develop <b>without fertilisation</b>. Such fruits are called "
    "<b>parthenocarpic fruits</b>; <b>banana</b> is one such example. Parthenocarpy can be "
    "<b>induced through the application of growth hormones</b>, and such fruits are "
    "<b>seedless</b>."))
# Fig 1.15 - caption F242, label walk-through F243
story.append(body(
    "The figure below labels, in the seeds, the <b>seed coat</b>, the <b>micropyle</b>, the "
    "<b>cotyledons</b> and the <b>hypocotyl root axis</b> of the dicot seed, and the "
    "<b>endosperm</b>, <b>scutellum</b>, <b>coleoptile</b>, <b>plumule</b>, <b>radicle</b>, "
    "<b>coleorhiza</b>, <b>shoot apical meristem</b> and <b>root tip</b> of the grain. In the "
    "false fruits it labels the <b>thalamus</b> that has grown into the fleshy part, the "
    "<b>pericarp</b> with its <b>mesocarp</b> and <b>endocarp</b>, the <b>seed</b> inside, and "
    "the tiny one-seeded <b>achene</b> fruits sitting on the surface of the strawberry."))
story.append(figure(
    "fig_1_15.png",
    "Fig. 1.15 &mdash; (a) Structure of some seeds. (b) False fruits of apple and strawberry. "
    "Labelled: cotyledons, micropyle, seed coat, endosperm, hypocotyl root axis, shoot apical "
    "meristem, root tip, scutellum, coleoptile, plumule, radicle, coleorhiza, pericarp, "
    "thalamus, seed, endocarp, mesocarp, achene.",
    max_width_cm=15.5))
story.append(body("<b>Why seed formation is an advantage.</b>"))
story.append(b1(
    " <b>Seed formation is more dependable</b>, because pollination and fertilisation are no "
    "longer dependent on water."))
story.append(b1(
    " Seeds have <b>better adaptive strategies for dispersal to new habitats</b> and help the "
    "species to colonise other areas."))
story.append(b1(
    " They have <b>sufficient food reserves</b>, and the <b>hard seed coat protects the young "
    "embryo</b>."))
story.append(b1(
    " Being products of <b>sexual reproduction</b>, they <b>generate new genetic "
    "combinations</b> leading to variations."))
story.append(gap())
story.append(body(
    "<b>Dehydration and dormancy of mature seeds are crucial for storage of seeds</b>, which "
    "can be used as food throughout the year and to raise crops in the next season. Some "
    "records of seed viability:"))
story.append(data_table([
    ["Record", "Species", "Age"],
    ["Oldest germinated seed", "A lupine, <i>Lupinus arcticus</i>, excavated from Arctic "
                               "Tundra &mdash; the seed germinated and flowered",
     "After an estimated record of <b>10,000 years</b> of dormancy"],
    ["A recent record of a viable seed", "Date palm, <i>Phoenix dactylifera</i>, found during "
                                        "the excavation at King Herod's palace near the Dead "
                                        "Sea", "<b>2000 years</b> old"],
], col_widths=[1.1, 2.3, 1.2]))
story.append(gap())
story.append(note(
    "<b>Orchid fruits</b> each contain <b>thousands of tiny seeds</b>. Similar is the case in "
    "fruits of some parasitic species such as <i>Orobanche</i> and <i>Striga</i>."))
story.append(gap())

# ======================================================================================
# ---- 1.5 APOMIXIS AND POLYEMBRYONY (F244-F250) ----
# ======================================================================================
story.append(heading("1.5", "APOMIXIS AND POLYEMBRYONY", level=1))
story.append(body(
    "Although seeds, in general, are the products of fertilisation, a few flowering plants "
    "such as <b>some species of Asteraceae and grasses</b> have evolved a special mechanism "
    "to <b>produce seeds without fertilisation</b>, called <b>apomixis</b>. Thus, apomixis is "
    "a form of <b>asexual reproduction that mimics sexual reproduction</b>."))
story.append(body("There are <b>several ways</b> of development of apomictic seeds."))
story.append(b1(
    " In some species, the <b>diploid egg cell is formed without reduction division</b> and "
    "develops into the embryo <b>without fertilisation</b>."))
story.append(b1(
    " In many <i>Citrus</i> and <i>Mango</i> varieties, some of the <b>nucellar cells</b> "
    "surrounding the embryo sac start dividing, <b>protrude into the embryo sac</b> and "
    "develop into the embryos."))
story.append(keyterm(
    "<b>Polyembryony</b> &mdash; occurrence of <b>more than one embryo in a seed</b>."))
story.append(note(
    "<b>Why apomixis matters to plant breeders.</b> Hybrid seeds are costly, and the farmer "
    "cannot use the hybrid seeds of the produce for sowing, because the characters of the "
    "hybrid progeny <b>segregate</b> in the next generation. <b>If these hybrids are made "
    "into apomicts, there is no segregation of characters in the hybrid progeny</b>, so the "
    "farmer can keep on using the hybrid seeds to raise new crop year after year, and does not "
    "have to buy hybrid seed every year."))
story.append(gap())

# ======================================================================================
# ---- Quick Recap (rewritten summary, §5 item 8; F251-F253) ----
# ======================================================================================
story.append(heading("Recap", "QUICK RECAP", level=1))
story.append(b1(
    " <b>Flowers are the seat of sexual reproduction in angiosperms.</b> The "
    "<b>androecium</b> consisting of stamens represents the male reproductive organs and the "
    "<b>gynoecium</b> consisting of pistils represents the female reproductive organs."))
story.append(b1(
    " A typical anther is <b>bilobed, dithecous and tetrasporangiate</b>. <b>Four wall "
    "layers</b> &mdash; the epidermis, endothecium, middle layers and the tapetum &mdash; "
    "surround the microsporangium. Cells of the sporogenous tissue undergo meiosis "
    "(<b>microsporogenesis</b>) to form microspore tetrads."))
story.append(b1(
    " <b>Pollen grains represent the male gametophytic generation.</b> The pollen grains have "
    "a <b>two-layered wall, the outer exine and inner intine</b>; the exine is of "
    "sporopollenin and is interrupted by germ pores. Pollen is shed at the 2-celled stage in "
    "over 60 per cent of angiosperms, otherwise at the 3-celled stage."))
story.append(b1(
    " The pistil has stigma, style and ovary; ovules arise from the placenta. The ovule's "
    "central tissue is the <b>nucellus</b>, in which the <b>archesporium</b> differentiates. A "
    "cell of the archesporium, the <b>megaspore mother cell</b>, divides meiotically "
    "(<b>megasporogenesis</b>) to give four megaspores, of which usually one is functional "
    "(<b>monosporic development</b>). The <b>mature embryo sac is 7-celled and "
    "8-nucleate</b>."))
story.append(b1(
    " <b>Pollination is the mechanism to transfer pollen grains from the anther to the "
    "stigma</b> &mdash; autogamy, geitonogamy or xenogamy. <b>Pollinating agents are either "
    "abiotic (wind and water) or biotic (animals).</b> Outbreeding devices &mdash; "
    "non-synchrony, spatial separation, self-incompatibility and unisexuality &mdash; "
    "discourage inbreeding depression."))
story.append(b1(
    " <b>Angiosperms exhibit double fertilisation</b> because two fusion events occur in each "
    "embryo sac, namely <b>syngamy</b> (male gamete + egg, giving the diploid zygote) and "
    "<b>triple fusion</b> (male gamete + two polar nuclei, giving the triploid PEN)."))
story.append(b1(
    " <b>Formation of endosperm always precedes development of the embryo.</b> The "
    "<b>mature dicotyledonous embryo has two cotyledons and an embryonal axis with epicotyl "
    "and hypocotyl</b>; monocot (grass) embryos have one cotyledon, the scutellum, with "
    "coleoptile and coleorrhiza. The ovule becomes the seed and the ovary the fruit "
    "(pericarp)."))
story.append(b1(
    " <b>A phenomenon called apomixis</b> is found in some angiosperms and results in the "
    "<b>formation of seeds without fertilisation</b>. Some angiosperms produce more than one "
    "embryo in their seed; this phenomenon is called <b>polyembryony</b>."))
story.append(gap())

# ======================================================================================
# ---- Terms used in the exercises (Rule 2 appendix; F254-F255) ----
# ======================================================================================
story.append(heading("Terms", "TERMS USED IN THE EXERCISES", level=1))
story.append(body(
    "The end-of-chapter EXERCISES lean on the following terms and sequences; each is stated "
    "here in one place so that a reader of these notes alone can answer them."))
story.append(data_table([
    ["Term / item assumed by an exercise", "What it means here"],
    ["<b>Developmental sequence of the male gametophyte</b>",
     "<b>Sporogenous tissue, pollen mother cell, microspore tetrad, pollen grain, male "
     "gametes</b> &mdash; in that order"],
    ["<b>Tetrasporangiate</b> anther", "Carrying four microsporangia &mdash; one at each "
                                       "corner of the tetragonal anther, two per lobe"],
    ["<b>Archesporium</b>", "The tissue differentiating within the nucellus, a cell of which "
                            "becomes the megaspore mother cell"],
    ["<b>Monosporic development</b>", "Development of the embryo sac from a single "
                                      "(functional) megaspore"],
    ["<b>Epicotyl vs hypocotyl</b>", "Epicotyl is the embryonal axis <b>above</b> the "
                                     "cotyledons, ending in the plumule; hypocotyl is the "
                                     "part <b>below</b> the cotyledons, ending in the radicle"],
    ["<b>Coleoptile vs coleorrhiza</b>", "Coleoptile is the hollow foliar sheath over the "
                                         "shoot apex and leaf primordia; coleorrhiza is the "
                                         "undifferentiated sheath enclosing the radicle and "
                                         "root cap"],
    ["<b>Integument vs testa</b>", "Integument is the protective envelope of the "
                                   "<b>ovule</b>; after fertilisation it hardens into the "
                                   "tough seed coat (testa) of the <b>seed</b>"],
    ["<b>Perisperm vs pericarp</b>", "Perisperm is persistent residual <b>nucellus</b> in the "
                                     "seed (black pepper, beet); pericarp is the wall of the "
                                     "<b>fruit</b>, developed from the ovary wall"],
    ["<b>Self-incompatibility</b>", "A genetic mechanism preventing self-pollen from "
                                    "fertilising the ovules, by inhibiting pollen germination "
                                    "or pollen tube growth in the pistil"],
    ["<b>Bagging technique</b>", "Covering an emasculated flower with a butter-paper bag to "
                                 "prevent contamination of its stigma with unwanted pollen"],
    ["<b>Triple fusion</b>", "Fusion of one male gamete with the <b>two polar nuclei</b> of "
                             "the central cell &mdash; three haploid nuclei in all &mdash; "
                             "giving the triploid primary endosperm nucleus"],
    ["<b>Importance of apomixis</b>", "It mimics sexual reproduction but needs no "
                                      "fertilisation, so hybrid characters do not segregate "
                                      "and hybrid seed can be reused year after year"],
], col_widths=[1.2, 2.8]))


if __name__ == "__main__":
    sys.exit(build_pdf(
        OUT_PDF, story,
        title="Class 12 Chapter 1 - Sexual Reproduction in Flowering Plants (NEET notes)",
        subject="NEET Biology"))
