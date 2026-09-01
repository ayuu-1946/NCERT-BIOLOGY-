"""
NCERT Class 11 Biology, Chapter 19 - Chemical Coordination and Integration
NEET replacement notes -> A4 print-ready PDF.

Built under SUPREME COMMAND PROMPT.md v6, Pass 2: written linearly from the
frozen 218-row inventory (Ch19_ChemicalCoordinationAndIntegration_inventory.md)
in Content Order (SS5), importing the repo-level frozen style module
`neet_template.py` (SS0.6). No style, geometry, colour or font is re-declared
here.

Block markers `# ---- N.N ----` mark every NCERT section so a Pass 3 flag can be
found and fixed in one contiguous block. Inventory row IDs are named in the
comments so any fact can be traced back to its frozen row.

The eight Pass-1 carry-forwards are honoured as follows.

1. GREEK (carry-forward 1). Rows F142/F143 hold the source's real Greek glyphs
   `alpha`-cells / `beta`-cells; check_pdf.py check 5 bans Greek from the
   generated PDF, so the running text spells them `alpha-cells` / `beta-cells`.
   Ionic charges are written with <super> tags (Ca<super>2+</super>,
   Na<super>+</super>, K<super>+</super>) for the same reason.

2. SOURCE-VERBATIM SPELLINGS (carry-forward 2). All five are printed as the
   source prints them and flagged in place so no reader takes them for errors
   introduced here: `sella tursica` (F039), `Exopthalmic goitre` (F087),
   `pupilary dilation` (F121/F125), `glucagons` (F153) and `Diagramatic` in the
   Figure 19.5 caption (F208) - while Figures 19.2, 19.3 and 19.4 keep the
   source's correctly spelled `Diagrammatic`.

3. PAGE 6 IS NOT ITALIC (carry-forward 3). The source italicises essentially all
   of page 6 by typesetting accident; SS19.2.7 is set here as ordinary body text.

4. EXERCISE GAP (carry-forward 4). The one gap - Q1(a) `Exocrine gland`, a term
   the body uses (F139, F188) but never defines - is closed in SS19.1 beside
   F013, phrased only from what the source itself supplies (ductless vs
   duct-bearing) and labelled as an addition, per Rules 2 and 5.

5. FIGURE 19.5 STAYS WITH SS19.4 (carry-forward 5). Q8 is answered only by
   SS19.4's prose plus F217's plate labels, so both panels sit inside SS19.4.

6. EXERCISE WORDING (carry-forward 6). The body's `atrial wall` and
   `gastro-intestinal tract` are kept; the exercises' `Atrium` / `G-I Tract` are
   recorded only in the closing appendix as the exercises' own shorter names.

7. FIGURE-LABEL COVERAGE (carry-forward 7, check 6). All seven plates carry
   their callouts as artwork, so each figure is followed by a NOTE naming its
   in-figure labels verbatim - matrix rows F212-F218, 38 label strings. That is
   what puts every in-figure label into the running text, and it lets a print
   reader name the parts of a diagram whose labels did not survive photocopying.

8. FIGURE 19.4 IS ONE ASSET (carry-forward 8). Its two panels interleave
   horizontally, so panels (a) and (b) are delivered as the single combined
   plate `fig_19_4.png` and read together in one note.

SUMMARY-UNIQUE FOLDS (Rule 3): the three facts stated only in the NCERT summary
are folded into the body sections the inventory names - F125 (catecholamine
glycogenolysis / lipolysis / proteolysis, SS19.2.7), F179 (progesterone in
mammary gland development and lactation, SS19.2.10) and F191 (the GI hormones
regulate the secretion of digestive juices, SS19.3).

Source: Chapter/class 11/Chapter 19 - Chemical Coordination and Integration.pdf
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
OUT_PDF = os.path.join(HERE, "Ch19_ChemicalCoordinationAndIntegration.pdf")

# Inline ion shorthands (check 5: tags, never Unicode sub/superscripts)
CA2 = "Ca<super>2+</super>"
NA = "Na<super>+</super>"
K = "K<super>+</super>"
CAPP = "Ca<super>++</super>"


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
# ---- Title block (SS5 item 1) ---- F001, F002
# ======================================================================================
story += title_block("Chemical Coordination and Integration")

# ======================================================================================
# ---- 19.intro ---- F003-F007 (opener F003), chapter map F008-F011
# ======================================================================================
story.append(body(
    "You have already learnt that the <b>neural system provides a point-to-point rapid "
    "coordination</b> among organs. The <b>neural coordination is fast but short-lived</b>."))

story.append(body(
    "As the <b>nerve fibres do not innervate all cells of the body</b> and the <b>cellular "
    "functions need to be continuously regulated</b>, a <b>special kind of coordination and "
    "integration</b> has to be provided. <b>This function is carried out by hormones.</b>"))

story.append(body(
    "The <b>neural system and the endocrine system jointly coordinate and regulate the "
    "physiological functions</b> in the body."))

story.append(gap())
story.append(data_table([
    ["Chapter 19 map", "What it covers"],
    ["<b>19.1 Endocrine Glands and Hormones</b>", "What a ductless gland and a hormone are"],
    ["<b>19.2 Human Endocrine System</b>",
     "The ten glands in fixed order: hypothalamus, pituitary, pineal, thyroid, parathyroid, "
     "thymus, adrenal, pancreas, testis, ovary"],
    ["<b>19.3 Hormones of Heart, Kidney and Gastrointestinal Tract</b>",
     "Hormone sources that are <b>not</b> endocrine glands"],
    ["<b>19.4 Mechanism of Hormone Action</b>", "How a hormone acts once it reaches its target"],
], col_widths=[38, 62]))

story.append(gap())
story.append(memory_aid(
    "<b>Two coordinating systems, two speeds:</b> <b>neural = fast but short-lived</b> and "
    "point-to-point; <b>endocrine = slower but sustained</b> and broadcast in the blood. Every "
    "fact in this chapter hangs on that contrast."))

# ======================================================================================
# ---- 19.1 ENDOCRINE GLANDS AND HORMONES ---- F012-F020 (opener F013)
#      + the one exercise gap (Rule 2, carry-forward 4): Exocrine gland, Q1(a)
# ======================================================================================
story.append(gap(6))
story.append(heading("19.1", "ENDOCRINE GLANDS AND HORMONES", level=1))

story.append(keyterm(
    "<b>Endocrine glands lack ducts</b> and are hence called <b>ductless glands</b>. Their "
    "<b>secretions are called hormones</b>."))

story.append(gap())
story.append(data_table([
    ["Gland type", "Duct", "Where the secretion goes"],
    ["<b>Endocrine</b> (ductless)", "<b>Absent</b>",
     "Released as a <b>hormone</b>, carried in the blood"],
    ["<b>Exocrine</b>", "<b>Present</b>",
     "Poured through the duct on to a surface or into a cavity"],
], col_widths=[26, 20, 54]))

story.append(note(
    "<b>Exocrine gland</b> - the chapter <b>uses</b> the word without defining it "
    "(the <b>pancreas acts as both exocrine and endocrine gland</b>, and <b>secretin acts on the "
    "exocrine pancreas</b>), so the contrast is stated here from the chapter's own words only: "
    "an <b>endocrine gland is ductless</b>, therefore an <b>exocrine gland is the duct-bearing "
    "kind</b>. Nothing beyond that is claimed."))

story.append(gap())
story.append(body(
    "The <b>classical definition</b> of hormone as a chemical produced by endocrine glands and "
    "<b>released into the blood</b> and <b>transported to a distantly located target organ</b> "
    "has a <b>current scientific definition</b> as follows."))

story.append(keyterm(
    "<b>Hormones are non-nutrient chemicals</b> which act as <b>intercellular messengers</b> and "
    "are <b>produced in trace amounts</b>."))

story.append(gap())
story.append(body(
    "The <b>new definition covers a number of new molecules</b> in addition to the hormones "
    "secreted by the <b>organised endocrine glands</b>."))

story.append(b1(
    "<b>Invertebrates</b> possess <b>very simple endocrine systems with few hormones</b>, "
    "whereas a <b>large number of chemicals act as hormones</b> and provide coordination in the "
    "<b>vertebrates</b>."))
story.append(b1("The <b>human endocrine system</b> is described here."))
story.append(b1(
    "These hormones <b>regulate metabolism, growth and development of our organs, the endocrine "
    "glands or certain cells</b>."))

# ======================================================================================
# ---- 19.2 HUMAN ENDOCRINE SYSTEM ---- F021-F027 (opener F022) + Fig 19.1 labels F212
# ======================================================================================
story.append(gap(6))
story.append(heading("19.2", "HUMAN ENDOCRINE SYSTEM", level=1))

story.append(keyterm(
    "The <b>endocrine glands</b> and <b>hormone producing diffused tissues/cells</b> located in "
    "different parts of our body constitute the <b>endocrine system</b>."))

story.append(gap())
story.append(body(
    "<b>Pituitary, pineal, thyroid, adrenal, pancreas, parathyroid, thymus</b> and <b>gonads</b> "
    "(<b>testis</b> in males and <b>ovary</b> in females) are the <b>organised endocrine "
    "bodies</b> in our body (Figure 19.1). Counting the <b>hypothalamus</b>, the endocrine system "
    "is composed of <b>hypothalamus, pituitary and pineal, thyroid, adrenal, pancreas, "
    "parathyroid, thymus and gonads (testis and ovary)</b>."))

story.append(body(
    "In addition to these, some <b>other organs</b>, e.g., <b>gastrointestinal tract, liver, "
    "kidney, heart</b> also produce hormones. A brief account of the <b>structure and functions "
    "of all major endocrine glands and hypothalamus</b> of the human body is given in the "
    "following sections."))

story.append(gap())
story.append(figure("fig_19_1.png", "Figure 19.1 Location of endocrine glands",
                    max_width_cm=10.4))

story.append(note(
    "<b>Read the plate (Figure 19.1 labels).</b> Working down the body the plate marks the "
    "<b>Hypothalamus</b> and, just below it, the <b>Pituitary</b>; the <b>Pineal</b> on the "
    "dorsal side of the forebrain; the <b>Thyroid and Parathyroid</b> in the neck; the "
    "<b>Thymus</b> behind the sternum; the <b>Pancreas</b> and, above the kidney, the "
    "<b>Adrenal</b>; and the gonads - <b>Ovary (in female)</b> and <b>Testis (in male)</b>."))

story.append(gap())
story.append(memory_aid(
    # [VERIFICATION FIX] Pass 3(a) D1: printed "SS19.2" - the docstring's ASCII
    # stand-in for the section sign leaked into reader-facing text. Spelled out.
    "<b>Ten glands, head to gonad, in the order Section 19.2 uses them:</b> "
    "<b>Hy</b>pothalamus, <b>Pi</b>tuitary, <b>Pi</b>neal, <b>Thy</b>roid, <b>Para</b>thyroid, "
    "<b>Thy</b>mus, <b>Ad</b>renal, <b>Pan</b>creas, <b>Tes</b>tis, <b>Ov</b>ary. Learn the order "
    "once and every subsection number becomes predictable."))

# ======================================================================================
# ---- 19.2.1 The Hypothalamus ---- F028-F037 (opener F029)
# ======================================================================================
story.append(gap(6))
story.append(heading("19.2.1", "The Hypothalamus", level=2))

story.append(body(
    "As you know, the hypothalamus is the <b>basal part of diencephalon, forebrain</b> "
    "(Figure 19.1) and it <b>regulates a wide spectrum of body functions</b>."))

story.append(keyterm(
    "It contains several groups of <b>neurosecretory cells called nuclei</b> which produce "
    "hormones. These hormones <b>regulate the synthesis and secretion of pituitary hormones</b>."))

story.append(gap())
story.append(data_table([
    ["Hypothalamic hormone type", "What it does", "Example"],
    ["<b>Releasing hormones</b>", "<b>Stimulate secretion of pituitary hormones</b>",
     "<b>Gonadotrophin releasing hormone (GnRH)</b> stimulates the pituitary synthesis and "
     "release of <b>gonadotrophins</b>"],
    ["<b>Inhibiting hormones</b>", "<b>Inhibit secretions of pituitary hormones</b>",
     "<b>Somatostatin</b> from the hypothalamus <b>inhibits the release of growth hormone</b> "
     "from the pituitary"],
], col_widths=[22, 33, 45]))

story.append(gap())
story.append(process_flow([
    "These hormones <b>originate in the hypothalamic neurons</b>.",
    "They <b>pass through axons</b> and are <b>released from their nerve endings</b>.",
    "They <b>reach the pituitary gland through a portal circulatory system</b>.",
    "There they <b>regulate the functions of the anterior pituitary</b>.",
]))

story.append(gap())
story.append(note(
    "The <b>posterior pituitary</b> is under the <b>direct neural regulation of the "
    "hypothalamus</b> (Figure 19.2) - so the two lobes are reached by two different routes: the "
    "<b>anterior</b> by <b>blood</b> (portal system), the <b>posterior</b> by <b>nerve</b>."))

# ======================================================================================
# ---- 19.2.2 The Pituitary Gland ---- F038-F069 (opener F039) + Fig 19.2 labels F213
# ======================================================================================
story.append(gap(6))
story.append(heading("19.2.2", "The Pituitary Gland", level=2))

story.append(body(
    "The pituitary gland is located in a <b>bony cavity called sella tursica</b> "
    "(the source's own spelling) and is <b>attached to hypothalamus by a stalk</b> "
    "(Figure 19.2). It is divided anatomically into an <b>adenohypophysis</b> and a "
    "<b>neurohypophysis</b>."))

story.append(gap())
story.append(data_table([
    ["Anatomical division", "Part", "Hormones"],
    ["<b>Adenohypophysis</b> - consists of <b>two portions</b>",
     "<b>Pars distalis</b>, commonly called <b>anterior pituitary</b>",
     "<b>Growth hormone (GH), prolactin (PRL), thyroid stimulating hormone (TSH), "
     "adrenocorticotrophic hormone (ACTH), luteinizing hormone (LH)</b> and <b>follicle "
     "stimulating hormone (FSH)</b> - <b>six trophic hormones</b>"],
    ["", "<b>Pars intermedia</b>",
     "Secretes <b>only one hormone</b> called <b>melanocyte stimulating hormone (MSH)</b>; in "
     "humans the pars intermedia is <b>almost merged with pars distalis</b>"],
    ["<b>Neurohypophysis (pars nervosa)</b>", "Also known as <b>posterior pituitary</b>",
     "<b>Stores and releases two hormones</b>, <b>oxytocin</b> and <b>vasopressin</b>, which are "
     "actually <b>synthesised by the hypothalamus</b> and are <b>transported axonally</b> to "
     "neurohypophysis"],
], col_widths=[24, 22, 54]))

story.append(gap())
story.append(note(
    "The pituitary gland is divided into <b>three major parts</b>, which are called as <b>pars "
    "distalis, pars intermedia</b> and <b>pars nervosa</b>. Two of the three (distalis, "
    "intermedia) make the adenohypophysis; the third is the neurohypophysis."))

story.append(gap())
story.append(figure("fig_19_2.png",
                    "Figure 19.2 Diagrammatic representation of pituitary and its relationship "
                    "with hypothalamus", max_width_cm=10.2))

story.append(note(
    "<b>Read the plate (Figure 19.2 labels).</b> The plate marks the <b>Hypothalamus</b> at the "
    "top with its <b>Hypothalamic neurons</b> running down the stalk; the <b>Portal "
    "circulation</b> carrying hypothalamic hormones into the <b>Anterior pituitary</b>; and the "
    "<b>Posterior pituitary</b>, which the neurons reach directly."))

story.append(gap())
story.append(Paragraph("<b>Growth hormone (GH) - the two directions of error</b>", STYLES["Body"]))
story.append(data_table([
    ["Condition", "Secretion", "Effect"],
    ["<b>Gigantism</b>", "<b>Over-secretion of GH</b>",
     "Stimulates <b>abnormal growth of the body</b>"],
    ["<b>Pituitary dwarfism</b>", "<b>Low secretion of GH</b>", "<b>Stunted growth</b>"],
    ["<b>Acromegaly</b>",
     "<b>Excess secretion of growth hormone in adults</b>, especially in <b>middle age</b>",
     "<b>Severe disfigurement (especially of the face)</b>, which may lead to <b>serious "
     "complications and premature death if unchecked</b>"],
], col_widths=[22, 30, 48]))

story.append(note(
    "<b>Acromegaly is hard to diagnose in the early stages</b> and often <b>goes undetected for "
    "many years</b>, until <b>changes in external features become noticeable</b>."))

story.append(gap())
story.append(Paragraph("<b>What each anterior-pituitary hormone does</b>", STYLES["Body"]))
story.append(data_table([
    ["Hormone", "Action"],
    ["<b>Prolactin (PRL)</b>",
     "Regulates the <b>growth of the mammary glands</b> and <b>formation of milk</b> in them"],
    ["<b>TSH</b> - the exercises call it <b>Thyrotrophin (TSH)</b>",
     "Stimulates the <b>synthesis and secretion of thyroid hormones</b> from the thyroid gland"],
    ["<b>ACTH</b> - the exercises call it <b>Corticotrophin (ACTH)</b>",
     "Stimulates the <b>synthesis and secretion of steroid hormones called glucocorticoids</b> "
     "from the <b>adrenal cortex</b>"],
    ["<b>LH</b> and <b>FSH</b>",
     "<b>Stimulate gonadal activity</b> and hence are called <b>gonadotrophins</b>"],
    ["<b>LH in males</b>",
     "Stimulates the <b>synthesis and secretion of hormones called androgens from testis</b>"],
    ["<b>FSH in males</b>", "<b>FSH and androgens regulate spermatogenesis</b>"],
    ["<b>LH in females</b>",
     "<b>Induces ovulation of fully mature follicles (graafian follicles)</b> and <b>maintains "
     "the corpus luteum</b>, formed from the <b>remnants of the graafian follicles after "
     "ovulation</b>"],
    ["<b>FSH in females</b>",
     "Stimulates <b>growth and development of the ovarian follicles</b>"],
    ["<b>MSH</b> - the exercises call it <b>Melanotrophin (MSH)</b>",
     "Acts on the <b>melanocytes (melanin containing cells)</b> and <b>regulates pigmentation of "
     "the skin</b>"],
], col_widths=[26, 74]))

story.append(gap())
story.append(Paragraph("<b>The two posterior-pituitary hormones</b>", STYLES["Body"]))
story.append(data_table([
    ["Hormone", "Action"],
    ["<b>Oxytocin</b>",
     "Acts on the <b>smooth muscles</b> of our body and <b>stimulates their contraction</b>. In "
     "females it stimulates a <b>vigorous contraction of uterus at the time of child birth</b>, "
     "and <b>milk ejection from the mammary gland</b>"],
    ["<b>Vasopressin</b>",
     "Acts <b>mainly at the kidney</b> and stimulates <b>resorption of water and electrolytes by "
     "the distal tubules</b>, thereby <b>reducing loss of water through urine (diuresis)</b>; "
     "hence it is also called <b>anti-diuretic hormone (ADH)</b>"],
], col_widths=[20, 80]))

story.append(note(
    "An <b>impairment affecting synthesis or release of ADH</b> results in a <b>diminished ability "
    "of the kidney to conserve water</b>, leading to <b>water loss and dehydration</b>. This "
    "condition is known as <b>Diabetes Insipidus</b> - a water disorder, not a sugar disorder."))

story.append(gap())
story.append(body(
    "Taken together, the <b>pituitary hormones regulate the growth and development of somatic "
    "tissues</b> and the <b>activities of peripheral endocrine glands</b>."))

story.append(gap())
story.append(memory_aid(
    "<b>Six from pars distalis:</b> <b>G</b>H, <b>P</b>RL, <b>T</b>SH, <b>A</b>CTH, <b>L</b>H, "
    "<b>F</b>SH - \"<b>G</b>ood <b>P</b>eople <b>T</b>ake <b>A</b>ll <b>L</b>ife's "
    "<b>F</b>avours\". <b>One from pars intermedia:</b> MSH. <b>Two stored in pars nervosa:</b> "
    "oxytocin, vasopressin. <b>6 + 1 + 2</b>."))

# ======================================================================================
# ---- 19.2.3 The Pineal Gland ---- F070-F075 (opener F071)
# ======================================================================================
story.append(gap(6))
story.append(heading("19.2.3", "The Pineal Gland", level=2))

story.append(body(
    "The pineal gland is located on the <b>dorsal side of forebrain</b>. Pineal secretes a "
    "hormone called <b>melatonin</b>."))

story.append(b1(
    "Melatonin plays a <b>very important role in the regulation of a 24-hour (diurnal) rhythm</b> "
    "of our body."))
story.append(b2(
    "For example, it helps in <b>maintaining the normal rhythms of sleep-wake cycle, body "
    "temperature</b>."))
story.append(b1(
    "In addition, melatonin also influences <b>metabolism, pigmentation, the menstrual cycle</b> "
    "as well as our <b>defense capability</b>."))

# ======================================================================================
# ---- 19.2.4 Thyroid Gland ---- F076-F095 (opener F077) + Fig 19.3 labels F214, F215
# ======================================================================================
story.append(gap(6))
story.append(heading("19.2.4", "Thyroid Gland", level=2))

story.append(body(
    "The thyroid gland is composed of <b>two lobes</b> which are located on <b>either side of the "
    "trachea</b> (Figure 19.3 a). Both the lobes are <b>interconnected with a thin flap of "
    "connective tissue called isthmus</b>."))

story.append(keyterm(
    "The thyroid gland is composed of <b>follicles and stromal tissues</b>. Each <b>thyroid "
    "follicle</b> is composed of <b>follicular cells, enclosing a cavity</b>."))

story.append(gap())
story.append(body(
    "These <b>follicular cells synthesise two hormones</b>, <b>tetraiodothyronine or thyroxine "
    "(T<sub>4</sub>)</b> and <b>triiodothyronine (T<sub>3</sub>)</b>. <b>Iodine is essential for "
    "the normal rate of hormone synthesis</b> in the thyroid."))

story.append(gap())
story.append(figure("fig_19_3a.png",
                    "Figure 19.3 Diagrammatic view of the position of Thyroid and Parathyroid "
                    "(a) Ventral side", max_width_cm=7.6))

story.append(note(
    "<b>Read the plate (Figure 19.3 (a) labels).</b> On the ventral side the plate marks the "
    "<b>Vocal cord</b> above, the two lobes of the <b>Thyroid</b> astride the <b>Trachea</b>."))

story.append(gap())
story.append(figure("fig_19_3b.png",
                    "Figure 19.3 Diagrammatic view of the position of Thyroid and Parathyroid "
                    "(b) Dorsal side", max_width_cm=7.6))

story.append(note(
    "<b>Read the plate (Figure 19.3 (b) labels).</b> The dorsal view marks the four "
    "<b>Parathyroid glands</b> on the back of the thyroid lobes - the same organ seen from "
    # [VERIFICATION FIX] Pass 3(a) D1: printed "SS19.2.5" - same leak as above.
    "behind, which is why Section 19.2.5 refers to this panel."))

story.append(gap())
story.append(Paragraph("<b>Too little iodine, too much hormone</b>", STYLES["Body"]))
story.append(data_table([
    ["Disorder", "Cause", "Consequences"],
    ["<b>Goitre</b> with <b>hypothyroidism</b>", "<b>Deficiency of iodine in our diet</b>",
     "Hypothyroidism and <b>enlargement of the thyroid gland</b>, commonly called <b>goitre</b>"],
    ["<b>Cretinism</b>", "<b>Hypothyroidism during pregnancy</b>",
     "<b>Defective development and maturation of the growing baby</b> leading to <b>stunted "
     "growth (cretinism), mental retardation, low intelligence quotient, abnormal skin, "
     "deaf-mutism</b>, etc."],
    ["<b>Irregular cycle</b>", "<b>Hypothyroidism in adult women</b>",
     "The <b>menstrual cycle may become irregular</b>"],
    ["<b>Hyperthyroidism</b>",
     "<b>Cancer of the thyroid gland</b> or <b>development of nodules</b> of the thyroid glands",
     "Rate of <b>synthesis and secretion of the thyroid hormones is increased to abnormal high "
     "levels</b>, which <b>adversely affects the body physiology</b>"],
    ["<b>Exopthalmic goitre</b> (the source's own spelling), also called <b>Graves' disease</b>",
     "A <b>form of hyperthyroidism</b>",
     "<b>Enlargement of the thyroid gland, protrusion of the eyeballs, increased basal metabolic "
     "rate</b> and <b>weight loss</b>"],
], col_widths=[22, 26, 52]))

story.append(gap())
story.append(Paragraph("<b>What the thyroid hormones do</b>", STYLES["Body"]))
story.append(b1(
    "Thyroid hormones play an important role in the <b>regulation of the basal metabolic "
    "rate</b>."))
story.append(b1("These hormones also <b>support the process of red blood cell formation</b>."))
story.append(b1(
    "Thyroid hormones <b>control the metabolism of carbohydrates, proteins and fats</b>."))
story.append(b1(
    "<b>Maintenance of water and electrolyte balance</b> is also influenced by thyroid "
    "hormones."))
story.append(b1(
    "Collected in one line: the thyroid gland hormones play an important role in the regulation "
    "of the <b>basal metabolic rate, development and maturation of the central neural system, "
    "erythropoiesis, metabolism of carbohydrates, proteins and fats, menstrual cycle</b>."))

story.append(gap())
story.append(keyterm(
    "Thyroid gland <b>also secretes a protein hormone called thyrocalcitonin (TCT)</b> which "
    "<b>regulates the blood calcium levels</b> - thyrocalcitonin regulates calcium levels in our "
    "blood <b>by decreasing it</b>."))

# ======================================================================================
# ---- 19.2.5 Parathyroid Gland ---- F096-F104 (opener F097)
# ======================================================================================
story.append(gap(6))
story.append(heading("19.2.5", "Parathyroid Gland", level=2))

story.append(body(
    "In humans, <b>four parathyroid glands</b> are present on the <b>back side of the thyroid "
    "gland</b>, <b>one pair each in the two lobes</b> of the thyroid gland (Figure 19.3 b)."))

story.append(keyterm(
    "The parathyroid glands secrete a <b>peptide hormone called parathyroid hormone (PTH)</b>. "
    "The <b>secretion of PTH is regulated by the circulating levels of calcium ions</b>."))

story.append(gap())
story.append(process_flow([
    f"<b>Parathyroid hormone (PTH) increases the {CA2} levels in the blood.</b>",
    "PTH <b>acts on bones</b> and stimulates the process of <b>bone resorption "
    "(dissolution/demineralisation)</b>.",
    f"PTH also stimulates <b>reabsorption of {CA2} by the renal tubules</b>.",
    f"PTH <b>increases {CA2} absorption from the digested food</b>.",
]))

story.append(gap())
story.append(keyterm(
    f"It is, thus, clear that <b>PTH is a hypercalcemic hormone</b>, i.e., it <b>increases the "
    f"blood {CA2} levels</b>. Along with <b>TCT</b>, it plays a <b>significant role in calcium "
    f"balance</b> in the body."))

story.append(gap())
story.append(memory_aid(
    "<b>Calcium see-saw:</b> <b>PTH pushes calcium UP</b> (hyper<b>calcemic</b>: bone, kidney, "
    "gut all deliver calcium to the blood); <b>TCT pulls it DOWN</b>. Same ion, opposite glands - "
    "thyroid down, parathyroid up."))

# ======================================================================================
# ---- 19.2.6 Thymus ---- F105-F112 (opener F106)
# ======================================================================================
story.append(gap(6))
story.append(heading("19.2.6", "Thymus", level=2))

story.append(body(
    "The thymus gland is a <b>lobular structure located between lungs behind sternum on the "
    "ventral side of aorta</b>. The <b>thymus plays a major role in the development of the immune "
    "system</b>."))

story.append(keyterm(
    "This gland secretes the <b>peptide hormones called thymosins</b>."))

story.append(gap())
story.append(b1(
    "Thymosins play a <b>major role in the differentiation of T-lymphocytes</b>, which provide "
    "<b>cell-mediated immunity</b>."))
story.append(b1(
    "In addition, thymosins also <b>promote production of antibodies</b> to provide <b>humoral "
    "immunity</b>."))
story.append(b1(
    "<b>Thymus is degenerated in old individuals</b> resulting in a <b>decreased production of "
    "thymosins</b>. As a result, the <b>immune responses of old persons become weak</b>."))

# ======================================================================================
# ---- 19.2.7 Adrenal Gland ---- F113-F137 (opener F114) + Fig 19.4 labels F216
#      Carry-forward 3: NOT set in italic, though the source italicises page 6.
#      Fold: F125 (SUMMARY-UNIQUE glycogenolysis / lipolysis / proteolysis).
# ======================================================================================
story.append(gap(6))
story.append(heading("19.2.7", "Adrenal Gland", level=2))

story.append(body(
    "Our body has <b>one pair of adrenal glands, one above of each kidney</b> (Figure 19.4 a). "
    "The gland is <b>composed of two types of tissues</b>: the <b>centrally located tissue is "
    "called the adrenal medulla</b>, and <b>outside this lies the adrenal cortex</b> "
    "(Figure 19.4 b)."))

story.append(gap())
story.append(figure("fig_19_4.png",
                    "Figure 19.4  Diagrammatic representation of : (a) Adrenal gland above kidney "
                    "(b) Section showing two parts of adrenal gland"))

story.append(note(
    "<b>Read the plate (Figure 19.4 labels).</b> Panel (a) marks the <b>Adrenal gland</b> sitting "
    "on top of the <b>Kidney</b>; panel (b) cuts the same gland open to show the outer <b>Adrenal "
    "cortex</b> enclosing the central <b>Adrenal medulla</b>. Both panels are delivered as one "
    "plate because their parts interleave horizontally."))

story.append(note(
    "<b>Underproduction of hormones by the adrenal cortex alters carbohydrate metabolism</b>, "
    "causing <b>acute weakness and fatigue</b>, leading to a disease called <b>Addison's "
    "disease</b>."))

story.append(gap())
story.append(heading("Medulla", "Adrenal medulla - the catecholamines", level=3))

story.append(keyterm(
    "The adrenal medulla secretes two hormones called <b>adrenaline or epinephrine</b> and "
    "<b>noradrenaline or norepinephrine</b>. These are commonly called as <b>catecholamines</b>."))

story.append(gap())
story.append(body(
    "Adrenaline and noradrenaline are <b>rapidly secreted in response to stress of any kind and "
    "during emergency situations</b> and are called <b>emergency hormones</b> or <b>hormones of "
    "Fight or Flight</b>."))

story.append(gap())
story.append(data_table([
    ["Catecholamine effect", "What happens"],
    ["<b>Alertness and skin</b>",
     "These hormones increase <b>alertness</b>, <b>pupilary dilation</b> (the source's own "
     "spelling), <b>piloerection (raising of hairs)</b>, <b>sweating</b> etc."],
    ["<b>Heart and lungs</b>",
     "Both the hormones <b>increase the heart beat, the strength of heart contraction</b> and the "
     "<b>rate of respiration</b>"],
    ["<b>Carbohydrate</b>",
     "Catecholamines <b>stimulate the breakdown of glycogen</b> resulting in an <b>increased "
     "concentration of glucose in blood</b>"],
    ["<b>Fat and protein</b>",
     "In addition, they also <b>stimulate the breakdown of lipids and proteins</b>"],
], col_widths=[22, 78]))

story.append(note(
    "<b>The one-line list to reproduce in an exam:</b> these hormones increase <b>alertness, "
    "pupilary dilation, piloerection, sweating, heart beat, strength of heart contraction, rate "
    "of respiration, glycogenolysis, lipolysis, proteolysis</b>. The last three are the "
    "<b>metabolic names</b> for the breakdown of glycogen, lipids and proteins above."))

story.append(gap())
story.append(heading("Cortex", "Adrenal cortex - the corticoids", level=3))

story.append(body(
    "The adrenal cortex can be divided into <b>three layers</b>, called <b>zona reticularis "
    "(inner layer)</b>, <b>zona fasciculata (middle layer)</b> and <b>zona glomerulosa (outer "
    "layer)</b>. The adrenal cortex secretes many hormones, commonly called as <b>corticoids</b>."))

story.append(gap())
story.append(data_table([
    ["Corticoid class", "Definition", "Main one in our body"],
    ["<b>Glucocorticoids</b>", "The corticoids <b>involved in carbohydrate metabolism</b>",
     "<b>Cortisol</b> is the main glucocorticoid"],
    ["<b>Mineralocorticoids</b>",
     "Corticoids which <b>regulate the balance of water and electrolytes</b> in our body",
     "<b>Aldosterone</b> is the main mineralocorticoid in our body"],
], col_widths=[22, 48, 30]))

story.append(gap())
story.append(b1(
    "<b>Glucocorticoids stimulate gluconeogenesis, lipolysis and proteolysis</b>; and "
    "<b>inhibit cellular uptake and utilisation of amino acids</b>."))
story.append(b1(
    "<b>Cortisol</b> is also involved in <b>maintaining the cardio-vascular system</b> as well as "
    "the <b>kidney functions</b>."))
story.append(b1(
    "<b>Glucocorticoids, particularly cortisol, produce anti-inflammatory reactions</b> and "
    "<b>suppress the immune response</b>."))
story.append(b1("<b>Cortisol stimulates the RBC production.</b>"))
story.append(b1(
    "Collected in one line: <b>glucocorticoids stimulate gluconeogenesis, lipolysis, proteolysis, "
    "erythropoiesis, cardio-vascular system, blood pressure</b>, and <b>glomerular filtration "
    "rate</b>, and <b>inhibit inflammatory reactions by suppressing the immune response</b>."))

story.append(gap())
story.append(process_flow([
    f"<b>Aldosterone acts mainly at the renal tubules.</b>",
    f"It <b>stimulates the reabsorption of {NA} and water</b>.",
    f"It <b>stimulates the excretion of {K} and phosphate ions</b>.",
    "Thus aldosterone helps in the <b>maintenance of electrolytes, body fluid volume, osmotic "
    "pressure and blood pressure</b>.",
]))

story.append(gap())
story.append(note(
    "<b>Small amounts of androgenic steroids</b> are also secreted by the adrenal cortex, which "
    "play a role in the <b>growth of axial hair, pubic hair and facial hair during puberty</b>."))

story.append(gap())
story.append(memory_aid(
    "<b>Cortex from outside in - \"salt, sugar, sex\":</b> <b>zona glomerulosa</b> (outer) is the "
    "salt layer, <b>zona fasciculata</b> (middle) the sugar layer, <b>zona reticularis</b> (inner) "
    "the sex-steroid layer. NCERT lists them inner-first, so read the list backwards."))

# ======================================================================================
# ---- 19.2.8 Pancreas ---- F138-F156 (opener F139)
#      Carry-forward 1: alpha-cells / beta-cells spelled out (rows F142/F143 are Greek).
# ======================================================================================
story.append(gap(6))
story.append(heading("19.2.8", "Pancreas", level=2))

story.append(body(
    "Pancreas is a <b>composite gland</b> (Figure 19.1) which acts as <b>both exocrine and "
    "endocrine gland</b>."))

story.append(keyterm(
    "The <b>endocrine pancreas consists of 'Islets of Langerhans'</b>. There are about <b>1 to 2 "
    "million Islets of Langerhans in a normal human pancreas</b>, representing <b>only 1 to 2 per "
    "cent of the pancreatic tissue</b>."))

story.append(gap())
story.append(data_table([
    ["Islet cell", "Hormone", "Chemical nature"],
    ["<b>alpha-cells</b>", "<b>Glucagon</b>",
     "<b>Peptide hormone</b>; plays an important role in <b>maintaining the normal blood glucose "
     "levels</b>"],
    ["<b>beta-cells</b>", "<b>Insulin</b>",
     "<b>Peptide hormone</b>; plays a major role in the <b>regulation of glucose homeostasis</b>"],
], col_widths=[18, 20, 62]))

story.append(note(
    "The source prints these two cell names with the Greek letters <b>alpha</b> and <b>beta</b> "
    "before the word <b>cells</b>; they are spelled out here so the page stays a plain-ASCII "
    "print file. The <b>two main types of cells in the Islet of Langerhans</b> are exactly these "
    "two."))

story.append(gap())
story.append(Paragraph("<b>Glucagon - the hyperglycemic hormone</b>", STYLES["Body"]))
story.append(process_flow([
    "Glucagon acts <b>mainly on the liver cells (hepatocytes)</b>.",
    "It <b>stimulates glycogenolysis</b>, resulting in an <b>increased blood sugar "
    "(hyperglycemia)</b>.",
    "In addition, this hormone <b>stimulates the process of gluconeogenesis</b>, which also "
    "<b>contributes to hyperglycemia</b>.",
    "Glucagon <b>reduces the cellular glucose uptake and utilisation</b>.",
    "Thus, <b>glucagon is a hyperglycemic hormone</b>.",
]))

story.append(gap())
story.append(Paragraph("<b>Insulin - the hypoglycemic hormone</b>", STYLES["Body"]))
story.append(process_flow([
    "Insulin acts <b>mainly on hepatocytes and adipocytes (cells of adipose tissue)</b>.",
    "It <b>enhances cellular glucose uptake and utilisation</b>.",
    "As a result, there is a <b>rapid movement of glucose from blood to hepatocytes and "
    "adipocytes</b>, resulting in <b>decreased blood glucose levels (hypoglycemia)</b>.",
    "Insulin also <b>stimulates conversion of glucose to glycogen (glycogenesis)</b> in the "
    "target cells.",
]))

story.append(gap())
story.append(keyterm(
    "The <b>glucose homeostasis in blood</b> is thus <b>maintained jointly by the two - insulin "
    "and glucagons</b> (the source's own plural spelling of glucagon)."))

story.append(gap())
story.append(note(
    "<b>Prolonged hyperglycemia</b> leads to a complex disorder called <b>diabetes mellitus</b>, "
    "which is associated with <b>loss of glucose through urine</b> and <b>formation of harmful "
    "compounds known as ketone bodies</b>. <b>Insulin deficiency and/or insulin resistance</b> "
    "result in this disease, and <b>diabetic patients are successfully treated with insulin "
    "therapy</b>."))

story.append(gap())
story.append(memory_aid(
    "<b>Alphabet trick:</b> <b>A</b>lpha comes first and gives glucAgon, which raises sugar; "
    "<b>B</b>eta gives insulin, which <b>B</b>rings sugar down. Hyper- and hypo-glycemia are "
    "therefore alpha and beta respectively."))

# ======================================================================================
# ---- 19.2.9 Testis ---- F157-F167 (opener F158)
# ======================================================================================
story.append(gap(6))
story.append(heading("19.2.9", "Testis", level=2))

story.append(body(
    "A <b>pair of testis</b> is present in the <b>scrotal sac (outside abdomen)</b> of male "
    "individuals (Figure 19.1). <b>Testis performs dual functions as a primary sex organ as well "
    "as an endocrine gland.</b>"))

story.append(keyterm(
    "Testis is composed of <b>seminiferous tubules and stromal or interstitial tissue</b>. The "
    "<b>Leydig cells or interstitial cells</b>, which are present in the <b>intertubular "
    "spaces</b>, produce a group of hormones called <b>androgens</b>, mainly "
    "<b>testosterone</b>."))

story.append(gap())
story.append(b1(
    "Androgens <b>regulate the development, maturation and functions of the male accessory sex "
    "organs</b> like <b>epididymis, vas deferens, seminal vesicles, prostate gland, urethra</b> "
    "etc."))
story.append(b1(
    "These hormones <b>stimulate muscular growth, growth of facial and axillary hair, "
    "aggressiveness, low pitch of voice</b> etc."))
story.append(b1(
    "Androgens play a <b>major stimulatory role in the process of spermatogenesis (formation of "
    "spermatozoa)</b>."))
story.append(b1(
    "Androgens <b>act on the central neural system</b> and <b>influence the male sexual behaviour "
    "(libido)</b>."))
story.append(b1(
    "These hormones produce <b>anabolic (synthetic) effects on protein and carbohydrate "
    "metabolism</b>."))
story.append(b1(
    "Collected in one line: the testis secretes androgens, which stimulate the <b>development, "
    "maturation and functions of the male accessory sex organs, appearance of the male secondary "
    "sex characters, spermatogenesis, male sexual behaviour, anabolic pathways</b> and "
    "<b>erythropoiesis</b>."))

# ======================================================================================
# ---- 19.2.10 Ovary ---- F168-F180 (opener F169). Fold: F179 (SUMMARY-UNIQUE).
# ======================================================================================
story.append(gap(6))
story.append(heading("19.2.10", "Ovary", level=2))

story.append(body(
    "Females have a <b>pair of ovaries located in the abdomen</b> (Figure 19.1). <b>Ovary is the "
    "primary female sex organ which produces one ovum during each menstrual cycle.</b> In "
    "addition, ovary also produces <b>two groups of steroid hormones called estrogen and "
    "progesterone</b>."))

story.append(keyterm(
    "Ovary is composed of <b>ovarian follicles and stromal tissues</b>. The <b>estrogen is "
    "synthesised and secreted mainly by the growing ovarian follicles</b>."))

story.append(gap())
story.append(process_flow([
    "A <b>follicle grows</b> and secretes <b>estrogen</b>.",
    "<b>Ovulation</b> occurs.",
    "After ovulation, the <b>ruptured follicle is converted to a structure called corpus "
    "luteum</b>.",
    "The corpus luteum <b>secretes mainly progesterone</b>.",
], cyclic=True))

story.append(gap())
story.append(data_table([
    ["Hormone", "Actions"],
    ["<b>Estrogens</b>",
     "Produce <b>wide ranging actions</b> such as <b>stimulation of growth and activities of "
     "female secondary sex organs, development of growing ovarian follicles, appearance of female "
     "secondary sex characters</b> (e.g., <b>high pitch of voice</b>, etc.) and <b>mammary gland "
     "development</b>. Estrogens also <b>regulate female sexual behaviour</b>"],
    ["<b>Progesterone</b> - the exercises call it the <b>Progestational hormone</b>",
     "<b>Progesterone supports pregnancy.</b> It also <b>acts on the mammary glands</b> and "
     "<b>stimulates the formation of alveoli (sac-like structures which store milk)</b> and "
     "<b>milk secretion</b>. Progesterone thus plays a major role in the <b>maintenance of "
     "pregnancy</b> as well as in <b>mammary gland development and lactation</b>"],
], col_widths=[24, 76]))

# ======================================================================================
# ---- 19.3 HORMONES OF HEART, KIDNEY AND GASTROINTESTINAL TRACT ----
#      F181-F192 (opener F182). Fold: F191 (SUMMARY-UNIQUE).
# ======================================================================================
story.append(gap(6))
story.append(heading("19.3", "HORMONES OF HEART, KIDNEY AND GASTROINTESTINAL TRACT", level=1))

story.append(body(
    "Now you know about the <b>endocrine glands and their hormones</b>. However, as mentioned "
    "earlier, <b>hormones are also secreted by some tissues which are not endocrine glands</b>."))

story.append(gap())
story.append(data_table([
    ["Non-gland source", "Hormone", "Action"],
    ["<b>Heart</b> - the <b>atrial wall</b>",
     "<b>Atrial natriuretic factor (ANF)</b>, a very important <b>peptide hormone</b>",
     "<b>Decreases blood pressure</b>"],
    ["<b>Kidney</b> - the <b>juxtaglomerular cells</b>",
     "<b>Erythropoietin</b>, a <b>peptide hormone</b>",
     "<b>Stimulates erythropoiesis (formation of RBC)</b>"],
], col_widths=[26, 30, 44]))

story.append(gap())
story.append(process_flow([
    "<b>Blood pressure is increased.</b>",
    "<b>ANF is secreted.</b>",
    "This causes <b>dilation of the blood vessels</b>.",
    "<b>This reduces the blood pressure.</b>",
]))

story.append(gap())
story.append(keyterm(
    "<b>Endocrine cells present in different parts of the gastro-intestinal tract</b> secrete "
    "<b>four major peptide hormones</b>, namely <b>gastrin, secretin, cholecystokinin (CCK)</b> "
    "and <b>gastric inhibitory peptide (GIP)</b>."))

story.append(gap())
story.append(data_table([
    ["GI hormone", "Acts on", "Action"],
    ["<b>Gastrin</b>", "The <b>gastric glands</b>",
     "<b>Stimulates the secretion of hydrochloric acid and pepsinogen</b>"],
    ["<b>Secretin</b>", "The <b>exocrine pancreas</b>",
     "<b>Stimulates secretion of water and bicarbonate ions</b>"],
    ["<b>CCK</b>", "<b>Both pancreas and gall bladder</b>",
     "<b>Stimulates the secretion of pancreatic enzymes and bile juice</b>, respectively"],
    ["<b>GIP</b>", "The <b>stomach</b>", "<b>Inhibits gastric secretion and motility</b>"],
], col_widths=[16, 26, 58]))

story.append(note(
    "Taken together, <b>these hormones regulate the secretion of digestive juices and help in "
    "digestion</b> - three stimulate a secretion and the fourth, GIP, shuts one down."))

story.append(gap())
story.append(body(
    "<b>Several other non-endocrine tissues secrete hormones called growth factors.</b> These "
    "factors are <b>essential for the normal growth of tissues and their "
    "repairing/regeneration</b>."))

story.append(gap())
story.append(memory_aid(
    "<b>Four GI hormones, three organs, one inhibitor:</b> <b>G</b>astrin -&gt; stomach acid, "
    "<b>S</b>ecretin -&gt; pancreatic bicarbonate, <b>C</b>CK -&gt; pancreatic enzymes + bile, "
    "<b>GIP</b> -&gt; the only one that <b>inhibits</b>. \"GIP is the Grumpy Inhibitory "
    "Peptide.\""))

# ======================================================================================
# ---- 19.4 MECHANISM OF HORMONE ACTION ---- F193-F208 (opener F194)
#      Carry-forward 5: Figure 19.5 (a) and (b) stay inside this section.
# ======================================================================================
story.append(gap(6))
story.append(heading("19.4", "MECHANISM OF HORMONE ACTION", level=1))

story.append(body(
    "Hormones produce their effects on target tissues by <b>binding to specific proteins called "
    "hormone receptors</b> located in the <b>target tissues only</b>."))

story.append(gap())
story.append(data_table([
    ["Receptor class", "Where it sits"],
    ["<b>Membrane-bound receptors</b>",
     "Hormone receptors present on the <b>cell membrane of the target cells</b>"],
    ["<b>Intracellular receptors</b>",
     "Receptors present <b>inside the target cell</b>, <b>mostly nuclear receptors (present in "
     "the nucleus)</b>"],
], col_widths=[28, 72]))

story.append(gap())
story.append(process_flow([
    "<b>Binding of a hormone to its receptor</b> leads to the <b>formation of a hormone-receptor "
    "complex</b> (Figure 19.5 a, b).",
    "<b>Each receptor is specific to one hormone only</b> and hence <b>receptors are "
    "specific</b>.",
    "<b>Hormone-Receptor complex formation leads to certain biochemical changes in the target "
    "tissue.</b>",
    "<b>Target tissue metabolism</b> and hence <b>physiological functions are regulated by "
    "hormones</b>.",
]))

story.append(gap())
story.append(body(
    "On the basis of their <b>chemical nature</b>, hormones can be divided into groups :"))

story.append(data_table([
    ["Group", "Examples"],
    ["<b>(i) peptide, polypeptide, protein hormones</b>",
     "e.g., <b>insulin, glucagon, pituitary hormones, hypothalamic hormones</b>, etc."],
    ["<b>(ii) steroids</b>",
     "e.g., <b>cortisol, testosterone, estradiol</b> and <b>progesterone</b>"],
    ["<b>(iii) iodothyronines</b>", "<b>thyroid hormones</b>"],
    ["<b>(iv) amino-acid derivatives</b>", "e.g., <b>epinephrine</b>"],
], col_widths=[38, 62]))

story.append(gap())
story.append(data_table([
    ["Receptor used", "Does the hormone enter the cell?", "What it regulates"],
    ["<b>Membrane-bound</b>",
     "<b>Normally do not enter the target cell</b>, but <b>generate second messengers</b> "
     f"(e.g., <b>cyclic AMP, IP<sub>3</sub>, {CAPP}</b> etc)",
     "The second messengers in turn <b>regulate cellular metabolism</b> (Figure 19.5a)"],
    ["<b>Intracellular</b> (e.g., <b>steroid hormones, iodothyronines</b>, etc.)",
     "<b>Enter and bind inside the cell</b>",
     "<b>Mostly regulate gene expression or chromosome function</b> by the <b>interaction of "
     "hormone-receptor complex with the genome</b>"],
], col_widths=[26, 34, 40]))

story.append(note(
    "<b>Cumulative biochemical actions result in physiological and developmental effects</b> "
    "(Figure 19.5b) - which is why a single hormone-receptor binding event can end in tissue "
    "growth."))

story.append(gap())
story.append(figure("fig_19_5a.png",
                    "Figure 19.5 Diagramatic representation of the mechanism of hormone action : "
                    "(a) Protein hormone"))

story.append(note(
    "<b>Read the plate (Figure 19.5 (a) labels).</b> A <b>Hormone (e.g., FSH)</b> reaches a "
    "<b>Receptor</b> held in the <b>Ovarian cell membrane</b>; that binding is <b>Response 1</b>, "
    "the <b>(Generation of second messenger)</b> step <b>(Cyclic AMP or " + CAPP + ")</b>; the "
    "messenger drives <b>Biochemical responses</b>, which end in <b>Physiological responses "
    "(e.g., ovarian growth)</b>."))

story.append(gap())
story.append(figure("fig_19_5b.png",
                    "Figure 19.5 Diagramatic representation of the mechanism of hormone action : "
                    "(b) Steroid hormone"))

story.append(note(
    "<b>Read the plate (Figure 19.5 (b) labels).</b> A <b>Hormone (e.g., estrogen)</b> crosses the "
    "<b>Uterine cell membrane</b>, and inside the <b>Nucleus</b> the <b>Hormone-receptor "
    "complex</b> acts on the <b>Genome</b>; <b>mRNA</b> is transcribed, <b>Proteins</b> are made, "
    "and the outcome is <b>Physiological responses (Tissue growth and differentiation)</b>."))

story.append(note(
    "Both Figure 19.5 captions are printed here with the source's own <b>Diagramatic</b>, which is "
    "how page 11 spells it - Figures 19.2, 19.3 and 19.4 use the correct <b>Diagrammatic</b> in "
    "the same book."))

story.append(gap())
story.append(memory_aid(
    "<b>Two mechanisms, one question:</b> does the hormone <b>get in</b>? Protein/peptide "
    "hormones <b>stay outside</b> and shout through a <b>second messenger</b>; steroids and "
    "iodothyronines <b>walk in</b> and talk to the <b>genome</b>. Water-soluble stays out, "
    "lipid-soluble goes in."))

# ======================================================================================
# ---- Recap (source SUMMARY, F209) ---- the 32 summary sentences, all already placed
#      in their body sections above; gathered here as a revision sweep.
# ======================================================================================
story.append(gap(6))
story.append(heading("Recap", "Quick recap of the whole chapter", level=1))

story.append(b1(
    "There are <b>special chemicals which act as hormones</b> and provide <b>chemical "
    "coordination, integration and regulation</b> in the human body; they <b>regulate metabolism, "
    "growth and development of our organs</b>."))
story.append(b1(
    "The <b>endocrine system</b> is composed of <b>hypothalamus, pituitary and pineal, thyroid, "
    "adrenal, pancreas, parathyroid, thymus and gonads</b>; <b>gastrointestinal tract, kidney and "
    "heart</b> also produce hormones."))
story.append(b1(
    "<b>Pituitary:</b> <b>pars distalis</b> produces <b>six trophic hormones</b>; <b>pars "
    "intermedia</b> secretes <b>only one</b>; <b>pars nervosa</b> secretes <b>two</b>. The "
    "pituitary hormones regulate <b>somatic tissue growth</b> and <b>peripheral endocrine "
    "glands</b>."))
story.append(b1(
    "<b>Pineal:</b> <b>melatonin</b> governs the <b>24-hour (diurnal) rhythm</b> - sleep and "
    "waking, body temperature."))
story.append(b1(
    "<b>Thyroid:</b> <b>BMR</b>, <b>central neural system maturation</b>, <b>erythropoiesis</b>, "
    "<b>carbohydrate/protein/fat metabolism</b>, <b>menstrual cycle</b>; <b>thyrocalcitonin</b> "
    "<b>lowers</b> blood calcium. <b>Parathyroid: PTH raises</b> it."))
story.append(b1(
    "<b>Thymus:</b> <b>thymosins</b> differentiate <b>T-lymphocytes</b> (cell-mediated immunity) "
    "and raise <b>antibody</b> production (humoral immunity)."))
story.append(b1(
    "<b>Adrenal:</b> <b>medulla</b> secretes <b>epinephrine and norepinephrine</b>; <b>cortex</b> "
    "secretes <b>glucocorticoids</b> and <b>mineralocorticoids</b>."))
story.append(b1(
    "<b>Pancreas:</b> <b>glucagon</b> raises blood glucose (glycogenolysis, gluconeogenesis); "
    "<b>insulin</b> lowers it (uptake, utilisation, glycogenesis). Failure of insulin gives "
    "<b>diabetes mellitus</b>."))
story.append(b1(
    "<b>Gonads:</b> <b>testis</b> secretes <b>androgens</b>; <b>ovary</b> secretes <b>estrogen "
    "and progesterone</b>."))
story.append(b1(
    "<b>Non-glands:</b> <b>ANF</b> from the heart lowers blood pressure, <b>erythropoietin</b> "
    "from the kidney drives RBC formation, and the <b>gastrointestinal tract</b> secretes "
    "<b>gastrin, secretin, cholecystokinin</b> and <b>gastric inhibitory peptide</b>."))

# ======================================================================================
# ---- Appendix (source EXERCISES F210 and the trailing NOTE page F211) ----
#      Rule 5: anything here that goes beyond this chapter's own sentences is labelled.
# ======================================================================================
story.append(gap(6))
story.append(heading("Appendix", "Terms the exercises use, and where they are answered", level=1))

story.append(data_table([
    ["Term as the exercises print it", "This chapter's own wording", "Section"],
    ["<b>Exocrine gland</b>",
     "The chapter defines the <b>endocrine gland as ductless</b>; the exocrine gland is therefore "
     "the <b>duct-bearing</b> kind. <b>Stated as an addition</b> - the chapter never defines it",
     "19.1"],
    ["<b>Atrium</b>", "The body says <b>atrial wall</b> of the heart (ANF)", "19.3"],
    ["<b>G-I Tract</b>", "The body says <b>gastro-intestinal tract</b>", "19.3"],
    ["<b>Hypoglycemic / hyperglycemic hormone</b>",
     "The body uses the nouns <b>hypoglycemia</b> (insulin) and <b>hyperglycemia</b> (glucagon)",
     "19.2.8"],
    ["<b>Gonadotrophic hormones</b>",
     "<b>LH and FSH stimulate gonadal activity</b> and hence are called <b>gonadotrophins</b>",
     "19.2.2"],
    ["<b>Blood pressure lowering hormone</b>", "<b>ANF decreases blood pressure</b>", "19.3"],
    ["<b>Thyrotrophin, Corticotrophin, Melanotrophin, Progestational hormone</b>",
     "<b>TSH, ACTH, MSH</b> and <b>progesterone</b> - the only place the book prints these four "
     "names is the exercise list",
     "19.2.2, 19.2.10"],
    ["<b>Mechanism of action of FSH</b>",
     "The <b>membrane-bound receptor plus second messenger</b> route, drawn with <b>Hormone "
     "(e.g., FSH)</b> in Figure 19.5a",
     "19.4"],
], col_widths=[26, 60, 14]))

story.append(note(
    "The textbook's <b>final page carries only the word NOTE</b> above a blank panel and the "
    "reprint line - it holds <b>no biology</b>, so nothing from it is reproduced here."))

if __name__ == "__main__":
    sys.exit(build_pdf(
        OUT_PDF, story,
        title="Class 11 Chapter 19 - Chemical Coordination and Integration (NEET notes)",
        subject="NEET Biology"))
