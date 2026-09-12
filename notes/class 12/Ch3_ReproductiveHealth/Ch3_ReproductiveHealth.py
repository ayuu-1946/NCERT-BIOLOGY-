"""
NCERT Biology -> NEET replacement notes
Class 12, Chapter 3 : Reproductive Health

Source  : Chapter/class 12/Chapter 3 - Reproductive Health.pdf
Built to: SUPREME COMMAND PROMPT.md v6 (fixed-pass gated edition, shared canon module)

Run from the repository root:
    python3 "notes/class 12/Ch3_ReproductiveHealth/Ch3_ReproductiveHealth.py"

Figures: every asset in assets/ has already been clip-extracted at 300 dpi and pushed
through PIL convert("L") + autocontrast. figure() re-asserts mode == "L" at build time,
so a raw or colour asset cannot silently reach the PDF (SUPREME COMMAND PROMPT.md v6 §4.4).

Structure of this file:
  1. Imports from neet_template.py -- the frozen canon (page geometry, colours, Times New
     Roman styles, and every sanctioned helper: heading, keyterm, process_flow, note,
     memory_aid, data_table, figure, title_block). Nothing here redeclares the canon (§0.6).
  2. One linear sequence of story.append(...) calls in Content Order (§5),
     each block commented with its NCERT section number for fast auditing.
"""

import os
import sys

from reportlab.lib.units import cm
from reportlab.platypus import Paragraph, Spacer, KeepTogether, Table, TableStyle, Image

# neet_template.py lives at the repository root; chapter scripts live several
# directories deep, so walk upward from this file until the module is found and
# put that directory on sys.path. Standard bootstrap for every chapter (§0.6).
_here = os.path.dirname(os.path.abspath(__file__))
_root = _here
while not os.path.exists(os.path.join(_root, "neet_template.py")):
    _parent = os.path.dirname(_root)
    if _parent == _root:
        raise RuntimeError("neet_template.py not found in any parent directory of this script")
    _root = _parent
if _root not in sys.path:
    sys.path.insert(0, _root)

from neet_template import (
    STYLES, FRAME_WIDTH, DARK_GREY, GRID_LINE,
    heading, keyterm, process_flow, note, memory_aid, data_table, title_block,
    build_pdf,
)
from neet_template import figure as _shared_figure

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "assets")
OUT_PDF = os.path.join(HERE, "Ch3_ReproductiveHealth.pdf")


def figure(asset_name: str, caption_text: str, max_width_cm: float = 15.9):
    """Chapter-local wrapper: binds the shared figure() helper to this chapter's own
    assets/ folder so every call below stays unchanged (asset_name, caption_text,
    max_width_cm=...)."""
    return _shared_figure(asset_name, caption_text, ASSETS, max_width_cm=max_width_cm)


# --------------------------------------------------------------------------------------
# STORY -- Content Order (§5)
# --------------------------------------------------------------------------------------

story = []

# ---- Title block (page 1, no separate title page) ----
story.extend(title_block("Reproductive Health"))

# ---- 3.0 Chapter introduction: what reproductive health means (F003-F010) ----
# F005 and F010 are Rule 3 filler (transitional + rhetorical framing) -- accounted for by
# Rule 3 and not printed as standalone lines; the tutor paragraph below carries the question once.
# [USER REQUEST] 3.0 intro heading + "You have learnt..." paragraph removed as bs
# (F003 heading + F004 opener not printed as standalone; facts remain covered by following WHO definition block)
story.append(Paragraph(
    "The term <b>simply refers to healthy reproductive organs with normal functions</b>, but it has "
    "a broader perspective and <b>includes the emotional and social aspects of reproduction also</b>.",
    STYLES["Body"]))
story.append(keyterm(
    "According to the <b>World Health Organisation (WHO)</b>, <b>reproductive health means a total "
    "well-being in all aspects of reproduction, i.e., physical, emotional, behavioural and social</b>. "
    "Therefore, a society with people having <b>physically and functionally normal reproductive organs</b> "
    "and <b>normal emotional and behavioural interactions among them in all sex-related aspects</b> "
    "might be called <b>reproductively healthy</b>."))
story.append(Spacer(1, 4))

# =============================== 3.1 PROBLEMS AND STRATEGIES ==========================
# ---- 3.1 Reproductive Health -- Problems and Strategies (F011-F030) ----
story.append(heading("3.1", "REPRODUCTIVE HEALTH -- PROBLEMS AND STRATEGIES", 1))
story.append(Paragraph("India moved early on reproductive health -- timeline as NCERT states:", STYLES["Body"]))
story.append(Paragraph("&bull; <b>Programme launch -- 1951:</b> <b>India was amongst the first countries in the world</b> (Summary: <b>the first nation</b>) to launch action plans at national level for total reproductive health as <b>family planning</b>; <b>periodically assessed over past decades</b>.", STYLES["Bullet1"]))
story.append(Paragraph("&bull; <b>Current name:</b> improved programmes covering <b>wider reproduction-related areas</b> now run as <b>Reproductive and Child Health Care (RCH) programmes</b>.", STYLES["Bullet1"]))
story.append(Paragraph("&bull; <b>Major tasks under RCH:</b> <b>creating awareness</b> about reproduction-related aspects and <b>providing facilities and support</b> for a reproductively healthy society.", STYLES["Bullet1"]))
story.append(Spacer(1, 3))

# ---- 3.1 Creating awareness (F016-F021) ----
story.append(heading("3.1", "Creating awareness", 2))
story.append(Paragraph(
    "Under RCH, <b>creating awareness</b> is a major task. Different actors play distinct roles:", STYLES["Body"]))
story.append(Paragraph("&bull; <b>Governmental and non-governmental agencies</b> -- steps through <b>audio-visual and print-media</b>.", STYLES["Bullet1"]))
story.append(Paragraph("&bull; <b>Parents, close relatives, teachers, friends</b> -- major role in <b>dissemination</b> of reproduction-related information.", STYLES["Bullet1"]))
story.append(Paragraph("&bull; <b>Schools</b> -- <b>sex education</b> encouraged, gives right information and discourages <b>myths and misconceptions</b> about sex.", STYLES["Bullet1"]))
story.append(Paragraph("What information is given depends on the audience:", STYLES["Body"]))
story.append(Paragraph("&bull; <b>Adolescent age group especially --</b> <b>reproductive organs, adolescence and related changes, safe and hygienic sexual practices, STDs, AIDS</b> -- to lead a <b>reproductively healthy life</b>.", STYLES["Bullet1"]))
story.append(Paragraph("&bull; <b>Fertile couples and those in marriageable age --</b> <b>birth control options, care of pregnant mothers, post-natal care of mother and child, importance of breast feeding, equal opportunities for male and female child</b> -- to bring up <b>socially conscious healthy families of desired size</b>.", STYLES["Bullet1"]))
story.append(Paragraph("&bull; <b>General society --</b> problems of <b>uncontrolled population growth</b> and social evils like <b>sex-abuse and sex-related crimes</b> -- to enable people to prevent them and build a <b>socially responsible and healthy society</b>.", STYLES["Bullet1"]))
story.append(Spacer(1, 3))

# ---- 3.1 Infrastructure, programmes and research (F022-F030) ----
story.append(heading("3.1", "Infrastructure, programmes and research", 2))
story.append(Paragraph("Execution needs more than awareness -- it needs systems and science on the ground:", STYLES["Body"]))
story.append(Paragraph("&bull; <b>Strong infrastructural facilities, professional expertise and material support</b> -- to provide <b>medical assistance and care for pregnancy, delivery, STDs, abortions, contraception, menstrual problems, infertility</b>.", STYLES["Bullet1"]))
story.append(Paragraph("&bull; <b>Better techniques and new strategies from time to time</b> -- for <b>more efficient care</b>; research on reproduction-related areas is <b>encouraged and supported by governmental and non-governmental agencies</b>.", STYLES["Bullet1"]))
story.append(Paragraph("Two programmes NCERT singles out as examples of that infrastructure in action:", STYLES["Body"]))
story.append(Paragraph("&bull; <b>Statutory ban on amniocentesis for sex-determination</b> (source prints <i>aminocentesis</i>) -- legally checks the menace of <b>female foeticides</b>.", STYLES["Bullet1"]))
story.append(Paragraph("&bull; <b>Massive child immunisation</b> -- merits mention as a successful public-health programme.", STYLES["Bullet1"]))
story.append(keyterm(
    "<b>Amniocentesis:</b> <b>some of the amniotic fluid of the developing foetus is taken to analyse the fetal "
    "cells and dissolved substances</b>. This procedure is used to test for the presence of certain genetic disorders "
    "such as <b>down syndrome, haemophilia, sickle-cell anemia</b>, etc., and to determine the survivability of the "
    "foetus -- the source sentence prints <i>haemoplilia</i> for haemophilia and is garbled, reproduced here with the "
    "correct term."))
story.append(note(
    "<b>Saheli -- a new oral contraceptive for the females -- was developed by scientists at Central Drug Research "
    "Institute (CDRI) in Lucknow, India.</b>"))
story.append(Paragraph("That the system works is visible in outcome indicators:", STYLES["Body"]))
story.append(Paragraph("&bull; <b>Better awareness</b> about sex-related matters -- up.", STYLES["Bullet1"]))
story.append(Paragraph("&bull; <b>Medically assisted deliveries</b> -- increased in number.", STYLES["Bullet1"]))
story.append(Paragraph("&bull; <b>Better post-natal care</b> -- <b>decreased MMR and IMR</b>.", STYLES["Bullet1"]))
story.append(Paragraph("&bull; <b>Couples with small families</b> -- increased in number.", STYLES["Bullet1"]))
story.append(Paragraph("&bull; <b>Better detection and cure of STDs</b> -- better.", STYLES["Bullet1"]))
story.append(Paragraph("&bull; <b>Overall medical facilities</b> for all sex-related problems -- increased.", STYLES["Bullet1"]))
story.append(Paragraph("&bull; <b>Assistance to infertile couples</b> -- added in Summary as an extra indicator.", STYLES["Bullet1"]))
story.append(Spacer(1, 4))

# =============================== 3.2 POPULATION AND BIRTH CONTROL =====================
# ---- 3.2 Population Stabilisation and Birth Control (F031-F049) ----
# NCERT's page-1 contents box calls this section "Population Explosion and Birth Control" while the
# section heading on page 43 reads "POPULATION STABILISATION AND BIRTH CONTROL" -- both wordings point
# to the same section; the explosive growth of F033 is the population explosion of Exercise Q5 and the summary.
story.append(heading("3.2", "POPULATION STABILISATION AND BIRTH CONTROL", 1, has_table=True))
story.append(Paragraph(
    "In the last century an <b>all-round development in various fields significantly improved the quality of life</b> "
    "of the people.", STYLES["Body"]))

# ---- 3.2 A century of population growth (F033-F040) ----
story.append(heading("3.2", "A century of population growth", 2))
story.append(Paragraph(
    "The last century's <b>all-round development</b> plus <b>increased health facilities and better living conditions</b> "
    "had an <b>explosive impact on population growth</b>.", STYLES["Body"]))
story.append(KeepTogether(data_table([
    ["Population (millions)", "1900 / independence", "2000", "2011"],
    ["<b>World</b>", "about <b>2 billion (2000 million)</b>", "about <b>6 billion</b>", "<b>7.2 billion</b>"],
    ["<b>India</b>", "about <b>350 million</b> at independence (1947)", "close to the <b>billion mark</b>", "crossed <b>1.2 billion</b> in May 2011"],
], col_widths=[1.6, 1.6, 1.6, 1.6])))
story.append(Paragraph("Why it exploded -- probable reasons NCERT lists:", STYLES["Body"]))
story.append(Paragraph("&bull; <b>Rapid decline in death rate</b>, <b>MMR</b> and <b>IMR</b>.", STYLES["Bullet1"]))
story.append(Paragraph("&bull; <b>Increase in number of people in reproducible age</b>.", STYLES["Bullet1"]))
story.append(Paragraph(
    "Through the <b>RCH programme</b> the growth rate was brought down, but only marginally -- <b>2011 census: less than 2 per cent (20/1000/year)</b> -- still a <b>rapid increase</b> that could lead to <b>absolute scarcity of food, shelter and clothing</b> despite progress.", STYLES["Body"]))
story.append(Spacer(1, 3))

# ---- 3.2 Steps to stabilise the population (F041-F045) ----
story.append(heading("3.2", "Steps to stabilise the population", 2))
story.append(Paragraph("Faced with explosive growth, the government was forced to act:", STYLES["Body"]))
story.append(process_flow([
    "<b>Most important step -- motivate smaller families by using various contraceptive methods</b>.",
    "Carry the message via <b>advertisements in media, posters/bills showing a happy couple with two children -- <i>Hum Do Hamare Do</i> (we two, our two)</b>; many <b>young, urban, working couples have even adopted an 'one child norm'</b>.",
    "<b>Statutory raising of marriageable age: female to 18 years, male to 21 years</b>.",
    "<b>Incentives given to couples with small families</b>.",
]))
story.append(Spacer(1, 3))

# ---- 3.2 What makes an ideal contraceptive (F047-F049) ----
# F046 is Rule 3 transitional filler ("Let us describe...") -- not printed as a standalone line; F042 already motivates the description.
story.append(heading("3.2", "What makes an ideal contraceptive", 2))
story.append(keyterm(
    "An <b>ideal contraceptive</b> should be <b>user-friendly, easily available, effective and reversible with no or least "
    "side-effects</b>. It also should <b>in no way interfere with the sexual drive, desire and/or the sexual act</b> of the "
    "user."))
story.append(Paragraph(
    "A <b>wide range of contraceptive methods</b> are presently available which could be broadly grouped into the following "
    "categories, namely <b>Natural/Traditional, Barrier, IUDs, Oral contraceptives, Injectables, Implants and Surgical methods</b>. "
    "The table below compares them; the sections that follow give the details named in it.", STYLES["Body"]))
story.append(Spacer(1, 2))

# ---- 3.2 Contraceptive methods at a glance -- comparison table ----
story.append(data_table([
    ["Category", "Principle / How it works", "Key examples and notes"],
    ["<b>Natural / Traditional</b>",
     "Avoid chances of <b>ovum and sperms meeting</b>; <b>no medicines or devices</b>; side effects <b>almost nil</b> but "
     "<b>chances of failure are also high</b>",
     "<b>Periodic abstinence:</b> avoid coitus <b>day 10 to 17</b> when ovulation could be expected -- the <b>fertile period</b>. "
     "<b>Withdrawal / coitus interruptus:</b> male withdraws penis before ejaculation to avoid insemination. "
     "<b>Lactational amenorrhea</b> (absence of menstruation): ovulation does not occur during intense lactation after "
     "parturition; as long as mother breast-feeds fully, chances of conception are <b>almost nil</b>, but effective "
     "<b>only upto six months</b> after parturition"],
    ["<b>Barrier</b>",
     "<b>Ovum and sperms prevented from physically meeting</b> with barriers; available <b>for both males and females</b>",
     "<b>Condoms (Fig. 3.1a, b):</b> thin <b>rubber/latex sheath</b> covering penis or vagina and cervix so ejaculated semen "
     "does not enter female tract; <b>Nirodh</b> is a popular male brand; <b>protects also from STIs and AIDS</b>; "
     "<b>disposable, self-inserted, gives privacy</b>. <b>Diaphragms, cervical caps and vaults:</b> rubber barriers covering "
     "cervix, <b>blocking entry of sperms</b> through cervix, <b>reusable</b>. <b>Spermicidal creams, jellies and foams</b> "
     "usually used alongwith barriers increase efficiency"],
    ["<b>IUDs</b>",
     "Inserted by <b>doctors or expert nurses in uterus through vagina</b>; increase <b>phagocytosis of sperms</b> and "
     "<b>Cu ions suppress sperm motility and fertilising capacity</b>; hormone-releasing IUDs also <b>make uterus unsuitable "
     "for implantation and cervix hostile to sperms</b>; <b>ideal for spacing and delaying</b>; <b>most widely accepted in India</b>",
     "<b>Non-medicated:</b> Lippes loop; <b>Copper-releasing:</b> CuT, Cu7, Multiload 375; <b>Hormone-releasing:</b> "
     "Progestasert, LNG-20 (Fig. 3.2)"],
    ["<b>Oral contraceptives (pills)</b>",
     "<b>Inhibit ovulation and implantation</b> and <b>alter quality of cervical mucus</b> to prevent / retard entry of sperms; "
     "<b>very effective with lesser side effects, well accepted</b>",
     "<b>Progestogens or progestogen-estrogen combinations</b> as <b>tablets (pills)</b>: taken <b>daily for 21 days starting "
     "preferably within first five days of menstrual cycle</b>; after a <b>gap of 7 days</b> (menstruation occurs) repeat same "
     "pattern till desire to prevent conception. <b>Saheli:</b> non-steroidal, <b>once a week</b> pill with very few side effects "
     "and high contraceptive value"],
    ["<b>Injectables / Implants</b>",
     "Mode similar to pills; <b>effective periods much longer</b>",
     "<b>Progestogens alone or in combination with estrogen</b> as <b>injections or implants under the skin</b> (Fig. 3.3)"],
    ["<b>Emergency contraception</b>",
     "Within <b>72 hours of coitus</b>, very effective after rape or casual unprotected intercourse",
     "<b>Progestogens or progestogen-estrogen combinations or IUDs within 72 hours</b>"],
    ["<b>Surgical (sterilisation)</b>",
     "<b>Blocks gamete transport</b> and prevents conception; <b>highly effective but reversibility very poor</b>; generally advised "
     "as <b>terminal method to prevent any more pregnancies</b>",
     "<b>Male - vasectomy</b> and <b>female - tubectomy</b>. <b>Vasectomy:</b> small part of <b>vas deferens is removed or tied up "
     "through small incision on scrotum (Fig. 3.4a) -- Vas deferens tied and cut</b>. <b>Tubectomy:</b> small part of "
     "<b>fallopian tube is removed (Fig. 3.4b) or tied up through incision in abdomen or through vagina -- Fallopian tubes tied "
     "and cut</b>"],
], col_widths=[1.9, 3.4, 5.3]))
story.append(Spacer(1, 4))

# ---- 3.2 Natural methods -- detail ----
story.append(heading("3.2", "Natural and traditional methods", 3))
story.append(Paragraph("<b>Principle:</b> <b>avoid chances of ovum and sperms meeting</b> -- no medicines or devices involved.", STYLES["Body"]))
story.append(KeepTogether(data_table([
    ["Method", "How it is practised", "Key timing / limit"],
    ["<b>Periodic abstinence</b>",
     "Couples avoid coitus <b>day 10 to 17 of menstrual cycle</b> when ovulation could be expected -- the <b>fertile period</b> (very high chance of fertilisation)",
     "Fertile window <b>10-17</b>"],
    ["<b>Withdrawal / coitus interruptus</b>",
     "Male withdraws penis <b>just before ejaculation</b> so as to avoid insemination",
     "--"],
    ["<b>Lactational amenorrhea</b> (absence of menstruation)",
     "Based on <b>ovulation not occurring during intense lactation after parturition</b>; as long as mother <b>breast-feeds fully, chances almost nil</b>",
     "Effective <b>only upto 6 months</b> following parturition"],
], col_widths=[1.7, 2.8, 1.7])))
story.append(Paragraph("<b>Trade-off:</b> <b>no medicines or devices so side effects almost nil</b>, but <b>chances of failure are also high</b>.", STYLES["Body"]))
story.append(Spacer(1, 3))

# ---- 3.2 Barrier methods -- detail ----
story.append(heading("3.2", "Barrier methods", 3))
story.append(Paragraph("<b>Principle:</b> <b>ovum and sperms prevented from physically meeting with help of barriers</b> -- available for <b>both males and females</b>.", STYLES["Body"]))
story.append(KeepTogether(data_table([
    ["Barrier", "What it is / how used", "Extra facts"],
    ["<b>Condoms</b> (Fig. 3.1a, b) -- thin <b>rubber/latex sheath</b>",
     "Cover <b>penis in male or vagina and cervix in female just before coitus</b> so <b>ejaculated semen does not enter female tract</b>",
     "<b>Nirodh</b> popular male brand; <b>protects from STIs and AIDS</b>; <b>disposable, self-inserted, gives privacy</b>"],
    ["<b>Diaphragms, cervical caps and vaults</b> -- rubber, cover <b>cervix</b>",
     "Inserted into female tract to <b>cover cervix during coitus</b>; <b>blocks entry of sperms through cervix</b>",
     "<b>Reusable</b>"],
    ["<b>Spermicidal creams, jellies and foams</b>",
     "Usually used <b>alongwith barriers</b>",
     "Increase <b>contraceptive efficiency</b>"],
], col_widths=[1.8, 2.6, 2.0])))
story.append(Spacer(1, 3))

# ---- 3.2 IUDs -- detail ----
story.append(heading("3.2", "Intra-uterine devices (IUDs)", 3))
story.append(Paragraph("<b>Inserted by doctors or expert nurses in uterus through vagina</b> -- one of the most <b>widely accepted methods in India</b>, ideal for <b>delaying and spacing</b>.", STYLES["Body"]))
story.append(KeepTogether(data_table([
    ["IUD type", "Examples (Fig. 3.2)", "How it works"],
    ["<b>Non-medicated</b>", "Lippes loop", "Increase <b>phagocytosis of sperms within uterus</b>"],
    ["<b>Copper-releasing</b>", "CuT, Cu7, Multiload 375", "<b>Cu ions suppress sperm motility and fertilising capacity</b>"],
    ["<b>Hormone-releasing</b>", "Progestasert, LNG-20", "Make <b>uterus unsuitable for implantation and cervix hostile to sperms</b> (in addition to phagocytosis)"],
], col_widths=[1.5, 1.8, 3.1])))
story.append(Spacer(1, 6))

# ---- 3.2 Oral, injectable, implant and emergency ----
story.append(heading("3.2", "Oral contraceptives, injectables, implants and emergency contraception", 3))
story.append(KeepTogether(data_table([
    ["Method", "Composition / delivery", "Schedule and action"],
    ["<b>Oral pills</b> -- progestogens or progestogen-estrogen combinations as <b>tablets</b>",
     "Popularly called <b>pills</b>; <b>Saheli</b> -- non-steroidal, <b>once a week</b>, very few side effects, high contraceptive value",
     "Take <b>daily for 21 days starting preferably within first 5 days of menstrual cycle</b>; <b>gap 7 days</b> (menstruation) then repeat; <b>inhibit ovulation and implantation and alter cervical mucus</b> to prevent/retard sperm entry; <b>very effective, lesser side effects, well accepted</b>"],
    ["<b>Injectables / Implants</b> -- progestogens alone or with estrogen",
     "As <b>injections or implants under the skin</b> (Fig. 3.3)",
     "Mode <b>similar to pills</b> but <b>effective periods much longer</b>"],
    ["<b>Emergency contraception</b>",
     "<b>Progestogens or progestogen-estrogen combinations or IUDs</b>",
     "Within <b>72 hours of coitus</b> -- very effective after <b>rape or casual unprotected intercourse</b>"],
], col_widths=[1.7, 2.0, 2.9])))
story.append(Spacer(1, 3))

# ---- 3.2 Surgical methods ----
story.append(heading("3.2", "Surgical methods -- sterilisation", 3))
story.append(Paragraph(
    "<b>Surgical methods, also called sterilisation, are generally advised for the male/female partner as a terminal method to "
    "prevent any more pregnancies.</b> <b>Surgical intervention blocks gamete transport and thereby prevent conception.</b> "
    "<b>Sterilisation procedure in the male is called vasectomy and that in the female, tubectomy.</b>", STYLES["Body"]))
story.append(process_flow([
    "<b>Vasectomy:</b> a small part of the <b>vas deferens is removed or tied up through a small incision on the scrotum</b> "
    "(Figure 3.4a) -- <b>Vas deferens tied and cut</b>.",
    "<b>Tubectomy:</b> a small part of the <b>fallopian tube is removed (Figure 3.4b) or tied up through a small incision in the "
    "abdomen or through vagina</b> -- <b>Fallopian tubes tied and cut</b>.",
]))
story.append(Paragraph(
    "These techniques are <b>highly effective but their reversibility is very poor</b>.", STYLES["Body"]))
# ---- Figures: stacked horizontally in groups of two, each <=25cm² (user constraint) ----
# Per-figure max widths computed from px dimensions to keep area = w*h <=25:
# fig_3_1a 684x192 natural 5.79cm area 9.4 -> cap 5.8; 3_1b 759x422 natural 6.42 area 22.9 -> cap 6.4
# fig_3_2 759x876 needs 4.65; fig_3_3 768x559 needs 5.86; fig_3_4a 900x809 needs 5.27; fig_3_4b 942x871 needs 5.20
# Horizontal pairing via Table([ [figA, figB] ]) — each cell holds a figure() KeepTogether (border + caption).
# FRAME_WIDTH is 18cm; two figures at ~5-6cm each fit side-by-side with gutters.

# Helper to make a row of two figures (uses Table to place side-by-side, not vertical stacking)
# Does NOT call figure() which returns KeepTogether (KeepTogether inside Table cell explodes to 16777219 pt and crashes layout).
# Instead we replicate figure()'s internals -- mono check (§4.4), scale to min(max_w, natural_w), GRID_LINE box -- but return
# a plain inner Table (framed image + caption stacked vertically) that Table can measure. Outer row Table then sits side-by-side.
def _fig_inner(asset_name: str, caption_text: str, max_width_cm: float):
    path = os.path.join(ASSETS, asset_name)
    if not os.path.exists(path):
        raise FileNotFoundError(f"MISSING FIGURE ASSET: {path} (required by caption: {caption_text})")
    from PIL import Image as PILImage
    with PILImage.open(path) as im:
        px_w, px_h = im.size
        mode = im.mode
    if mode != "L":
        raise RuntimeError(f"FIGURE NOT MONOCHROME: {asset_name} has mode {mode!r}, expected 'L'. Run convert_figures_mono.py (§4.4).")
    max_w = min(max_width_cm * cm, FRAME_WIDTH)
    natural_w = px_w / 300.0 * 2.54 * cm
    width = min(max_w, natural_w)
    height = width * px_h / px_w
    img = Image(path, width=width, height=height)
    framed = Table([[img]], colWidths=[width + 10])
    framed.setStyle(TableStyle([
        ("BOX", (0, 0), (-1, -1), 0.5, GRID_LINE),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    framed.hAlign = "CENTER"
    cap = Paragraph(caption_text, STYLES["Caption"])
    # Inner stack: framed image on row 0, caption on row 1 -- plain Table, not KeepTogether, so outer Table can measure it
    inner = Table([[framed], [cap]], colWidths=[width + 10])
    inner.setStyle(TableStyle([
        ("ALIGN", (0,0), (-1,-1), "CENTER"),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("LEFTPADDING", (0,0), (-1,-1), 0),
        ("RIGHTPADDING", (0,0), (-1,-1), 0),
        ("TOPPADDING", (0,0), (-1,-1), 2),
        ("BOTTOMPADDING", (0,0), (-1,-1), 2),
    ]))
    return inner

def _fig_pair(a_name, a_cap, a_w, b_name, b_cap, b_w):
    fa = _fig_inner(a_name, a_cap, a_w)
    fb = _fig_inner(b_name, b_cap, b_w)
    cw = (FRAME_WIDTH - 0.4*cm) / 2
    t = Table([[fa, fb]], colWidths=[cw, cw])
    t.setStyle(TableStyle([
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("ALIGN", (0,0), (-1,-1), "CENTER"),
        ("LEFTPADDING", (0,0), (-1,-1), 3),
        ("RIGHTPADDING", (0,0), (-1,-1), 3),
        ("TOPPADDING", (0,0), (-1,-1), 2),
        ("BOTTOMPADDING", (0,0), (-1,-1), 2),
    ]))
    # Keep the pair together across page breaks where possible (pair, not individual figure+caption)
    return KeepTogether([t])

# Row 1: condoms (both naturally <25, but capped to meet area precisely)
story.append(_fig_pair(
    "fig_3_1a.png",
    "Fig. 3.1a -- Condom for the male. Thin rubber/latex sheath covering the penis so ejaculated semen does not enter the female tract. Shape carries meaning, monochrome intact.",
    5.8,
    "fig_3_1b.png",
    "Fig. 3.1b -- Condom for the female. Thin rubber/latex sheath covering vagina and cervix. Photograph of device; shape, not hue, carries fact.",
    6.4))

# Row 2: IUD + implants (both capped to <25)
story.append(_fig_pair(
    "fig_3_2.png",
    "Fig. 3.2 -- Copper T (CuT). Copper-releasing IUD inserted in uterus through vagina. Photograph; form not colour carries fact.",
    4.6,
    "fig_3_3.png",
    "Fig. 3.3 -- Implants. Progestogen or progestogen-estrogen implants under the skin. Photograph of rods; meaning in shape/placement, not hue.",
    5.8))

# Row 3: vasectomy + tubectomy (both capped)
story.append(_fig_pair(
    "fig_3_4a.png",
    "Fig. 3.4a -- Vasectomy. Vas deferens removed or tied via small scrotal incision. Label: Vas deferens tied and cut. Yellow marks survive as mid-grey, stated in words.",
    5.2,
    "fig_3_4b.png",
    "Fig. 3.4b -- Tubectomy. Fallopian tube removed or tied via abdomen/vagina. Label: Fallopian tubes tied and cut. Yellow ligatures mid-grey; blue arrows survive as grey line arrows.",
    5.19))
story.append(Spacer(1, 3))

# ---- 3.2 Closing on contraceptive choice ----
story.append(Paragraph("Putting contraception in perspective -- NCERT caveats at the end of 3.2:", STYLES["Body"]))
story.append(Paragraph("&bull; <b>Who decides:</b> selection and use should always be in <b>consultation with qualified medical professionals</b>.", STYLES["Bullet1"]))
story.append(Paragraph("&bull; <b>Nature:</b> <b>not regular requirements for maintenance of reproductive health</b>; practiced <b>against a natural event -- conception/pregnancy</b>; one is <b>forced to use them either to prevent or to delay/space pregnancy due to personal reasons</b>.", STYLES["Bullet1"]))
story.append(Paragraph("&bull; <b>Population role:</b> <b>widespread use has significant role in checking uncontrolled growth of population</b>.", STYLES["Bullet1"]))
story.append(Paragraph("&bull; <b>Caution -- possible ill-effects:</b> <b>nausea, abdominal pain, breakthrough bleeding, irregular menstrual bleeding or even breast cancer -- though not very significant, should not be totally ignored</b>.", STYLES["Bullet1"]))
story.append(memory_aid(
    "Recall the seven NCERT contraceptive groups in order: <b>N-B-I-O-I-I-S</b> -- <b>N</b>atural, <b>B</b>arrier, <b>I</b>UDs, "
    "<b>O</b>ral pills, <b>I</b>njectables, <b>I</b>mplants, <b>S</b>urgical. Timings: pills <b>21 + 7</b> days, emergency "
    "<b>72 hours</b>, lactational cover <b>only 6 months</b>."))
story.append(Spacer(1, 4))

# =============================== 3.3 MTP ============================================
# ---- 3.3 Medical Termination of Pregnancy (F100-F114) ----
story.append(heading("3.3", "MEDICAL TERMINATION OF PREGNANCY (MTP)", 1))
story.append(keyterm(
    "<b>Intentional or voluntary termination of pregnancy before full term is called medical termination of pregnancy "
    "(MTP) or induced abortion</b> -- the opener defines the term used in its own section heading."))
story.append(Paragraph("&bull; <b>Global scale:</b> <b>nearly 45 to 50 million MTPs per year worldwide = 1/5th of total conceived pregnancies</b>; whether to accept/legalise is debated for <b>emotional, ethical, religious and social issues</b>.", STYLES["Bullet1"]))
story.append(Paragraph("&bull; <b>Indian law:</b> <b>Government of India legalised MTP in 1971 with strict conditions to avoid misuse</b>; restrictions important to <b>check indiscriminate and illegal female foeticides reported high in India</b>.", STYLES["Bullet1"]))
story.append(Spacer(1, 2))

# ---- 3.3 Why MTP, and its safety window ----
story.append(heading("3.3", "Why MTP, and when it is safest", 2))
story.append(Paragraph("&bull; <b>Why MTP?</b> <b>To get rid of unwanted pregnancies</b> -- due to <b>casual unprotected intercourse, failure of contraceptive used during coitus, or rapes</b>; also <b>essential where continuation could be harmful or even fatal to mother or foetus or both</b>.", STYLES["Bullet1"]))
story.append(Paragraph("&bull; <b>When is it safest?</b> <b>Relatively safe during first trimester -- upto 12 weeks</b>; <b>second trimester abortions are much more risky</b>.", STYLES["Bullet1"]))
story.append(Paragraph("&bull; <b>Majority of MTPs performed illegally by unqualified quacks</b> -- <b>not only unsafe but could be fatal</b>.", STYLES["Bullet1"]))
story.append(Paragraph("&bull; <b>Misuse of amniocentesis to determine sex of unborn child</b> -- if <b>foetus found female, followed by MTP -- totally against what is legal</b>; dangerous for <b>young mother and foetus</b>.", STYLES["Bullet1"]))
story.append(Paragraph("&bull; <b>Reversal:</b> <b>effective counselling to avoid unprotected coitus and on risk factors of illegal abortions</b>, plus <b>more health care facilities</b>, could reverse these trends.", STYLES["Bullet1"]))
story.append(Spacer(1, 2))

# ---- 3.3 The MTP (Amendment) Act, 2017 ----
story.append(heading("3.3", "The MTP (Amendment) Act, 2017", 2))
story.append(note(
    "The <b>Medical Termination of Pregnancy (Amendment) Act, 2017 was enacted by the government of India with the intension of "
    "reducing the incidence of illegal abortion and consequent maternal mortality and morbidity</b> -- source prints <i>intension</i> "
    "for intention."))
story.append(Paragraph(
    "Under the Act, a pregnancy may be terminated on certain considered grounds and within strict time limits:",
    STYLES["Body"]))
story.append(process_flow([
    "Within the <b>first 12 weeks of pregnancy</b>, on the opinion of <b>one registered medical practitioner</b>.",
    "More than <b>12 weeks but fewer than 24 weeks</b>, on the opinion of <b>two registered medical practitioners</b>, formed in "
    "good faith, that the required grounds exist.",
    "Ground <b>(i): continuation of the pregnancy would involve a risk to the life of the pregnant woman or of grave injury to her "
    "physical or mental health</b>.",
    "Ground <b>(ii): there is a substantial risk that if the child were born, it would suffer from such physical or mental "
    "abnormalities as to be seriously handicapped</b>.",
]))
story.append(Spacer(1, 12))

# =============================== 3.4 STIs ===========================================
# ---- 3.4 Sexually Transmitted Infections (F119-F133) ----
story.append(heading("3.4", "SEXUALLY TRANSMITTED INFECTIONS (STIs)", 1))
# Contents box lists "Sexually Transmitted Diseases" while the section heading and summary use STIs -- both are the same group.
story.append(keyterm(
    "<b>Infections or diseases which are transmitted through sexual intercourse are collectively called sexually transmitted "
    "infections (STI) or venereal diseases (VD) or reproductive tract infections (RTI)</b> -- the opener defines the term used in "
    "its own heading."))
story.append(Paragraph("&bull; <b>Common examples (8 named):</b> <b>gonorrhoea, syphilis, genital herpes, chlamydiasis, genital warts, trichomoniasis, hepatitis-B and HIV leading to AIDS</b> -- among these <b>HIV is most dangerous (Chapter 7)</b>.", STYLES["Bullet1"]))
story.append(Paragraph("&bull; <b>Other routes for hepatitis-B and HIV:</b> also transmitted by <b>sharing injection needles, surgical instruments with infected persons, transfusion of blood, or from infected mother to foetus</b>.", STYLES["Bullet1"]))
story.append(Paragraph("&bull; <b>Curability:</b> <b>all except hepatitis-B, genital herpes and HIV are completely curable if detected early and treated properly</b>.", STYLES["Bullet1"]))
story.append(Spacer(1, 2))

# ---- 3.4 Symptoms, stigma and complications ----
story.append(heading("3.4", "Symptoms, stigma and complications", 2))
story.append(Paragraph("&bull; <b>Early symptoms (minor):</b> <b>itching, fluid discharge, slight pain, swellings, etc., in genital region</b>.", STYLES["Bullet1"]))
story.append(Paragraph("&bull; <b>Asymptomatic cases:</b> <b>infected females may often be asymptomatic</b> and remain undetected for long.", STYLES["Bullet1"]))
story.append(Paragraph("&bull; <b>Why timely treatment is deterred:</b> <b>absence or less significant early symptoms</b> plus <b>social stigma</b> attached to STIs deter infected persons from timely detection and proper treatment.", STYLES["Bullet1"]))
story.append(Paragraph("&bull; <b>Late complications if untreated:</b> <b>PID, abortions, still births, ectopic pregnancies, infertility or even cancer of reproductive tract</b> -- STIs are a <b>major threat to healthy society</b>; <b>prevention / early detection and cure given prime consideration under RCH</b>.", STYLES["Bullet1"]))
story.append(Paragraph("&bull; <b>Most vulnerable age group:</b> all persons vulnerable but <b>incidences very high among 15-24 years -- the age group to which you also belong</b>.", STYLES["Bullet1"]))
story.append(Spacer(1, 2))

# ---- 3.4 Prevention is possible ----

story.append(heading("3.4", "Prevention is possible", 2))
story.append(Paragraph(
    "There is no reason to panic because prevention is possible -- three simple principles keep one free of these infections:",
    STYLES["Body"]))
story.append(process_flow([
    "<b>Avoid sex with unknown partners/multiple partners.</b>",
    "<b>Always try to use condoms during coitus.</b>",
    "<b>In case of doubt, go to a qualified doctor for early detection and get complete treatment if diagnosed with infection.</b>",
]))
story.append(Spacer(1, 4))

# =============================== 3.5 INFERTILITY ====================================
# ---- 3.5 Infertility (F134-F154) ----
story.append(heading("3.5", "INFERTILITY", 1))
story.append(KeepTogether(data_table([
    ["Aspect of infertility", "What NCERT states"],
    ["<b>Why it matters</b>", "Discussion on reproductive health is incomplete without infertility"],
    ["<b>Definition</b>", "<b>A large number of couples all over the world including India are infertile</b> -- unable to produce children inspite of <b>unprotected sexual co-habitation even after 2 years</b> (2-year criterion from Summary)"],
    ["<b>Reasons -- could be many</b>", "<b>Physical, congenital, diseases, drugs, immunological or even psychological</b>"],
    ["<b>Who is blamed vs reality in India</b>", "Often <b>female blamed</b> for childless couple, but <b>more often than not problem lies in male partner</b>"],
    ["<b>Where help comes from</b>", "<b>Specialised health care units (infertility clinics, etc.) could help in diagnosis and corrective treatment</b> and enable children; where not possible, <b>assisted to have children through ART (assisted reproductive technologies)</b>"],
], col_widths=[1.8, 4.6])))
story.append(Spacer(1, 2))

# ---- 3.5 ART: IVF, ZIFT, IUT, GIFT ----
story.append(heading("3.5", "Assisted reproductive technologies", 2))
story.append(keyterm(
    "<b>In vitro fertilisation (IVF -- fertilisation outside the body in almost similar conditions as that in the body) followed by "
    "embryo transfer (ET) is one of such methods.</b>"))
story.append(Paragraph("The lab route is best seen as a menu of cargos and destinations:", STYLES["Body"]))
story.append(KeepTogether(data_table([
    ["ART (what moves)", "Cargo / source", "Where it goes / how"],
    ["<b>IVF-ET: test tube baby programme</b>",
     "<b>Ova from wife/donor (female) and sperms from husband/donor (male)</b> collected and induced to form <b>zygote under simulated lab conditions</b>",
     "<b>ZIFT</b> -- zygote or <b>early embryos upto 8 blastomeres into fallopian tube</b>; <b>IUT</b> -- embryos <b>with more than 8 blastomeres into uterus</b>; <b>in-vivo fertilised embryos also usable</b> to assist females who cannot conceive"],
    ["<b>GIFT -- gamete intra fallopian transfer</b>",
     "<b>Ovum collected from a donor</b>",
     "Transferred into <b>fallopian tube of another female</b> who cannot produce one but can provide suitable environment for fertilisation and further development"],
    ["<b>ICSI -- intra cytoplasmic sperm injection</b>",
     "A <b>single sperm directly injected into an ovum</b>",
     "Embryo formed <b>in laboratory</b>"],
], col_widths=[1.6, 2.0, 2.8])))
story.append(Spacer(1, 2))

# ---- 3.5 AI / IUI and the limits of ART ----
story.append(heading("3.5", "Artificial insemination and the limits of ART", 2))
story.append(Paragraph("&bull; <b>AI -- artificial insemination / IUI -- intra-uterine insemination:</b> for infertility due to <b>inability of male partner to inseminate the female</b> or <b>very low sperm counts</b> -- <b>semen from husband or healthy donor artificially introduced into vagina or uterus (IUI)</b> of female.", STYLES["Bullet1"]))
story.append(Paragraph("Why ART does not reach everyone:", STYLES["Body"]))
story.append(Paragraph("&bull; <b>Technical:</b> <b>extremely high precision handling by specialised professionals and expensive instrumentation required</b>.", STYLES["Bullet1"]))
story.append(Paragraph("&bull; <b>Access:</b> <b>available only in very few centres in the country; affordable to only a limited number of people</b>.", STYLES["Bullet1"]))
story.append(Paragraph("&bull; <b>Acceptance:</b> <b>emotional, religious and social factors are deterrents in adoption</b>.", STYLES["Bullet1"]))
story.append(note(
    "ZIFT vs IUT is a numbers test: <b>ZIFT -- zygote or early embryo upto 8 blastomeres -- into the fallopian tube; IUT -- embryos "
    "with more than 8 blastomeres -- into the uterus</b>. GIFT transfers an <b>unfertilised ovum</b>, IVF transfers an <b>embryo</b>, "
    "ICSI injects a <b>single sperm into a single ovum</b>, and IUI introduces <b>semen into the uterus</b> -- four different cargos, "
    "four different names."))
story.append(Spacer(1, 2))

# ---- 3.5 Adoption ----

story.append(heading("3.5", "Adoption as an alternative", 2))
story.append(Paragraph(
    "Since the ultimate aim of all these procedures is to have children, <b>in India we have so many orphaned and destitute children, "
    "who would probably not survive till maturity, unless taken care of</b>. <b>Our laws permit legal adoption and it is as yet, one of "
    "the best methods for couples looking for parenthood.</b>", STYLES["Body"]))
story.append(Spacer(1, 4))

# =============================== QUICK RECAP ========================================
# ---- Quick Recap (denser rewrite of the chapter summary, Rule 3) ----
story.append(heading("QR", "QUICK RECAP", 1))
story.append(Paragraph(
    "&bull; <b>Reproductive health</b> is <b>total well-being -- physical, emotional, behavioural and social</b> (WHO). India was "
    "<b>amongst the first countries / the first nation to launch RCH programmes (family planning, 1951)</b>. The work is <b>awareness "
    "(audio-visual, print, parents/teachers, sex education)</b> plus <b>medical care for pregnancy, delivery, STDs, contraception, "
    "menstrual problems and infertility</b>, supported by <b>infrastructure, expertise, research and laws such as the ban on "
    "amniocentesis for sex determination</b>. Indicators of improvement are <b>lower MMR/IMR, more small families, better STD cure, "
    "more medical facilities and assistance to infertile couples</b> -- plus <b>Saheli from CDRI, Lucknow</b>.", STYLES["Bullet1"]))
story.append(Paragraph(
    "&bull; <b>Population:</b> better health and living conditions drove an <b>explosion -- world 2 billion (1900) to 6 billion (2000) to "
    "7.2 billion (2011); India about 350 million at independence to near a billion by 2000 to over 1.2 billion in May 2011</b>. "
    "Reasons: <b>fall in death rate, MMR, IMR and more people in reproducible age</b>. RCH cut growth only marginally to <b>less than "
    "2% (20/1000/year, 2011)</b>, threatening <b>food, shelter, clothing scarcity</b>. Response: <b>motivate smaller families -- Hum Do "
    "Hamare Do, one-child norm, marriage age 18 (F) / 21 (M), incentives</b>.", STYLES["Bullet1"]))
story.append(Paragraph(
    "&bull; <b>Contraception -- seven NCERT groups:</b> an <b>ideal contraceptive is user-friendly, easily available, effective, "
    "reversible, least side effects and does not interfere with the sexual act</b>. <b>Natural</b> -- avoid ovum-sperm meeting without "
    "devices: <b>periodic abstinence day 10-17 (fertile period), withdrawal, lactational amenorrhea (intense lactation, 6 months only, "
    "almost nil side effects but high failure)</b>. <b>Barrier</b> -- physically block meeting: <b>condoms (Nirodh, also protects from "
    "STIs/AIDS, disposable, private), diaphragms/caps/vaults (reusable) plus spermicidal creams/jellies/foams</b>. <b>IUDs</b> by doctors / "
    "nurses through vagina: <b>Lippes loop, CuT/Cu7/Multiload 375, Progestasert/LNG-20</b> via <b>phagocytosis, Cu suppression, hormone "
    "making uterus unsuitable and cervix hostile</b>; ideal for <b>spacing, most widely accepted in India</b>. <b>Pills</b> -- progestogen "
    "or progestogen-estrogen <b>21 days within first 5 days, 7-day gap, inhibit ovulation/implantation and alter cervical mucus</b>; "
    "well accepted, plus <b>Saheli weekly, non-steroidal</b>. <b>Injectables/implants</b> under skin, <b>similar mode but much longer "
    "action</b>. <b>Emergency within 72 hours</b> after rape or casual unprotected intercourse. <b>Surgical sterilisation blocks gamete "
    "transport -- vasectomy (Vas deferens tied and cut) and tubectomy (Fallopian tubes tied and cut), highly effective, poorly "
    "reversible</b> -- always chosen with a qualified doctor. Contraception is <b>against natural conception, used only to prevent / "
    "delay / space pregnancy</b>, and <b>possible ill-effects (nausea, bleeding, breast cancer) though not very significant should not "
    "be ignored</b>.", STYLES["Bullet1"]))
story.append(Paragraph(
    "&bull; <b>MTP:</b> <b>intentional / voluntary termination before full term (induced abortion)</b>; <b>45-50 million per year = 1/5th of "
    "conceived pregnancies</b>; debated for <b>emotional, ethical, religious, social reasons</b>; <b>legal in India since 1971 with strict "
    "conditions to check illegal female foeticide</b>; needed for <b>unwanted pregnancies (casual / failed contraception / rape) or harm "
    "to mother / foetus</b>; <b>relatively safe upto 12 weeks, riskier in second trimester</b>; <b>majority illegal by quacks, unsafe / "
    "fatal; amniocentesis misused for sex determination leading to female foeticide, dangerous for mother and foetus</b>; reversible only by "
    "<b>counselling, avoiding unprotected coitus and more health facilities</b>. <b>Amendment Act, 2017</b> aims to cut illegal abortion / "
    "mortality: <b>within 12 weeks -- one doctor; 12-24 weeks -- two doctors; grounds: risk to life / grave injury to physical / mental "
    "health, or substantial risk of serious physical / mental handicap in the child</b>.", STYLES["Bullet1"]))
story.append(Paragraph(
    "&bull; <b>STIs:</b> <b>infections transmitted by sexual intercourse -- STI / VD / RTI</b>: <b>gonorrhoea, syphilis, genital herpes, "
    "chlamydiasis, genital warts, trichomoniasis, hepatitis-B, HIV leading to AIDS (most dangerous, Chapter 7)</b>; <b>hepatitis-B / HIV "
    "also spread by needles, surgical instruments, blood transfusion, mother to foetus</b>; <b>all except hepatitis-B, genital herpes and "
    "HIV are completely curable if early and properly treated</b>; <b>minor early symptoms -- itching, discharge, pain, swelling; females "
    "often asymptomatic</b>; <b>absent/less symptoms plus stigma deter timely treatment</b> leading to <b>PID, abortions, still births, "
    "ectopic pregnancies, infertility, reproductive-tract cancer</b>; <b>major threat, prevention / early cure is prime under RCH</b>; "
    "<b>highest incidence 15-24 years</b>; prevention: <b>avoid unknown / multiple partners, use condoms, see a qualified doctor if in "
    "doubt and complete treatment</b>.", STYLES["Bullet1"]))
story.append(Paragraph(
    "&bull; <b>Infertility -- inability to produce children inspite of unprotected co-habitation even after 2 years</b>; many causes -- "
    "<b>physical, congenital, diseases, drugs, immunological, psychological</b>; <b>female often blamed but more often male partner is "
    "responsible</b>; <b>infertility clinics help diagnosis / corrective treatment, but where not possible, ART assists</b>: "
    "<b>IVF-ET (test tube baby) -- ova and sperms collected, zygote formed in lab under simulated conditions; ZIFT (upto 8 blastomeres) "
    "to fallopian tube, IUT (more than 8) to uterus; in-vivo embryos also usable</b>; <b>GIFT -- donor ovum into another female's "
    "fallopian tube</b>; <b>ICSI -- single sperm directly into ovum</b>; <b>AI -- inability to inseminate or very low counts corrected by "
    "introducing husband / donor semen into vagina or uterus (IUI)</b>; <b>all require high precision, expensive instrumentation, available "
    "in very few centres, affordable to limited people, deterred by emotional / religious / social factors</b>; <b>many orphaned / destitute "
    "children unlikely to survive without care -- legal adoption is as yet one of the best methods for parenthood</b>.",
    STYLES["Bullet1"]))
story.append(Spacer(1, 4))

# =============================== EXERCISE-GAP APPENDIX ==============================
# ---- Terms used in the exercises (Rule 2 gaps; chapter facts only) ----
story.append(heading("EX", "TERMS USED IN THE EXERCISES", 1))
story.append(Paragraph(
    "A few end-of-chapter questions lean on a term or task the body states only indirectly. Each is closed below "
    "<b>using only facts from this chapter</b>.", STYLES["Body"]))
story.append(data_table([
    ["Exercise term / task", "Explanation from this chapter"],
    ["<b>Q7 -- Why removal of gonads is not a contraceptive option</b>",
     "The chapter's surgical methods are <b>sterilisation by blocking gamete transport -- Vas deferens tied and cut (vasectomy) and "
     "Fallopian tubes tied and cut (tubectomy)</b>; they <b>do not remove the gonads (testes / ovaries)</b>, and <b>reversibility is "
     "already very poor</b>. Removing testes or ovaries would eliminate the <b>source of gametes and of reproductive hormones</b> -- a "
     "permanent, non-contraceptive castration the chapter <b>never lists among its seven contraceptive categories</b> and that violates "
     "the <b>ideal-contraceptive criteria of reversibility and no interference with normal physiology</b>. Hence gonad removal is not a "
     "contraceptive option."],
    ["<b>Q11(a) -- Abortions can happen spontaneously -- True</b>",
     "The chapter defines only <b>intentional / voluntary termination (MTP / induced abortion)</b>, but it also lists <b>abortion as a "
     "complication of STIs / PID</b> that occurs without any MTP procedure, which shows pregnancy loss can happen on its own. Spontaneous "
     "abortion (miscarriage) is therefore true."],
    ["<b>Q12(c) -- Oral pills are not especially popular among rural women -- False to correct</b>",
     "The chapter states only that <b>pills are very effective with lesser side effects and are well accepted by the females</b> and that "
     "<b>Saheli is a once-a-week pill</b>, but it <b>never distinguishes rural from urban users</b>. In fact, <b>IUDs are described as one of "
     "the most widely accepted methods in India</b>, often promoted for spacing in the public programme, so singling out pills as "
     "rural-popular is not supported."],
], col_widths=[2.0, 5.6]))
story.append(Spacer(1, 4))
# [USER REQUEST] Footer disclaimer removed as bs

if __name__ == "__main__":
    sys.exit(build_pdf(
        OUT_PDF, story,
        title="Class 12 Chapter 3 - Reproductive Health (NEET notes)",
        subject="NEET Biology"))
