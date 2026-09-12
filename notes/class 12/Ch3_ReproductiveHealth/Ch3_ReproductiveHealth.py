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
# F012 summary-unique folded: body says amongst the first countries, summary says the first nation
story.append(Paragraph(
    "<b>India was amongst the first countries in the world</b> to initiate action plans and programmes "
    "at a national level to attain total reproductive health as a social goal -- the summary puts the "
    "same fact even more strongly as <b>the first nation in the world</b> to do so. These programmes, "
    "called <b>family planning</b>, were <b>initiated in 1951</b> and were <b>periodically assessed over the "
    "past decades</b>.", STYLES["Body"]))
story.append(Paragraph(
    "Improved programmes covering wider reproduction-related areas are currently in operation under the "
    "popular name <b>Reproductive and Child Health Care (RCH) programmes</b>.", STYLES["Body"]))
story.append(Paragraph(
    "<b>Creating awareness</b> among people about various reproduction related aspects and <b>providing "
    "facilities and support</b> for building up a reproductively healthy society are the <b>major tasks</b> "
    "under these programmes.", STYLES["Body"]))
story.append(Spacer(1, 3))

# ---- 3.1 Creating awareness (F016-F021) ----
story.append(heading("3.1", "Creating awareness", 2))
story.append(Paragraph(
    "With the help of <b>audio-visual and the print-media</b>, <b>governmental and non-governmental agencies</b> "
    "have taken various steps to create awareness about reproduction-related aspects. <b>Parents, other close "
    "relatives, teachers and friends</b> also have a major role in the dissemination of this information. "
    "<b>Introduction of sex education in schools</b> should also be encouraged to provide right information to "
    "the young so as to discourage children from believing in myths and having misconceptions about "
    "sex-related aspects.", STYLES["Body"]))
story.append(Paragraph(
    "<b>Proper information</b> about <b>reproductive organs, adolescence and related changes, safe and hygienic "
    "sexual practices, sexually transmitted diseases (STD), AIDS</b>, etc., would help people, especially those "
    "in the <b>adolescent age group</b> to lead a reproductively healthy life. Educating people, especially "
    "<b>fertile couples and those in marriageable age group</b>, about available <b>birth control options, care of "
    "pregnant mothers, post-natal care of the mother and child, importance of breast feeding, equal opportunities "
    "for the male and the female child</b>, etc., would address the importance of bringing up <b>socially conscious "
    "healthy families of desired size</b>.", STYLES["Body"]))
story.append(Paragraph(
    "Awareness of problems due to <b>uncontrolled population growth, social evils like sex-abuse and sex-related "
    "crimes</b>, etc., need to be created to enable people to think and take up necessary steps to prevent them "
    "and thereby build up a <b>socially responsible and healthy society</b>.", STYLES["Body"]))
story.append(Spacer(1, 3))

# ---- 3.1 Infrastructure, programmes and research (F022-F030) ----
story.append(heading("3.1", "Infrastructure, programmes and research", 2))
story.append(Paragraph(
    "Successful implementation of various action plans requires <b>strong infrastructural facilities, professional "
    "expertise and material support</b>. These are essential to provide <b>medical assistance and care</b> for "
    "reproduction-related problems like <b>pregnancy, delivery, STDs, abortions, contraception, menstrual problems, "
    "infertility</b>, etc. <b>Implementation of better techniques and new strategies from time to time</b> are also "
    "required to provide more efficient care and assistance.", STYLES["Body"]))
story.append(Paragraph(
    "<b>Statutory ban on amniocentesis for sex-determination</b> to legally check the increasing menace of "
    "<b>female foeticides</b>, <b>massive child immunisation</b>, etc., are some programmes that merit mention in "
    "this connection. NCERT prints the term as <i>aminocentesis</i>; the correct spelling is amniocentesis.",
    STYLES["Body"]))
story.append(keyterm(
    "<b>Amniocentesis:</b> <b>some of the amniotic fluid of the developing foetus is taken to analyse the fetal "
    "cells and dissolved substances</b>. This procedure is used to test for the presence of certain genetic disorders "
    "such as <b>down syndrome, haemophilia, sickle-cell anemia</b>, etc., and to determine the survivability of the "
    "foetus -- the source sentence prints <i>haemoplilia</i> for haemophilia and is garbled, reproduced here with the "
    "correct term."))
story.append(Paragraph(
    "Research on various reproduction-related areas are <b>encouraged and supported by governmental and "
    "non-governmental agencies</b> to find out new methods and/or to improve upon the existing ones.", STYLES["Body"]))
story.append(note(
    "<b>Saheli -- a new oral contraceptive for the females -- was developed by scientists at Central Drug Research "
    "Institute (CDRI) in Lucknow, India.</b>"))
story.append(Paragraph(
    "<b>Better awareness</b> about sex related matters, <b>increased number of medically assisted deliveries</b> and "
    "<b>better post-natal care</b> leading to <b>decreased maternal and infant mortality rates</b>, <b>increased number "
    "of couples with small families</b>, <b>better detection and cure of STDs</b> and <b>overall increased medical "
    "facilities for all sex-related problems</b>, etc. all indicate <b>improved reproductive health of the society</b>. "
    "The summary adds one more indicator to this list -- <b>assistance to infertile couples</b>.", STYLES["Body"]))
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
    "However, <b>increased health facilities along with better living conditions had an explosive impact on the growth "
    "of population</b>.", STYLES["Body"]))
story.append(Paragraph(
    "The <b>world population</b> which was around <b>2 billion (2000 million) in 1900 rocketed to about 6 billion by 2000 "
    "and 7.2 billion in 2011</b>. A similar trend was observed in India too -- <b>our population which was approximately "
    "350 million at the time of our independence reached close to the billion mark by 2000 and crossed 1.2 billion in "
    "May 2011</b>.", STYLES["Body"]))
story.append(Paragraph(
    "A <b>rapid decline in death rate, maternal mortality rate (MMR) and infant mortality rate (IMR)</b> as well as an "
    "<b>increase in number of people in reproducible age</b> are probable reasons for this.", STYLES["Body"]))
story.append(Paragraph(
    "Through our <b>Reproductive Child Health (RCH) programme</b>, though we could <b>bring down the population growth rate, "
    "it was only marginal</b>. According to the <b>2011 census report</b>, the population growth rate was <b>less than "
    "2 per cent, i.e., 20/1000/year</b>, a rate at which our population could increase rapidly. Such an alarming growth "
    "rate could lead to an <b>absolute scarcity of even the basic requirements, i.e., food, shelter and clothing</b>, in "
    "spite of significant progress made in those areas.", STYLES["Body"]))
story.append(Spacer(1, 3))

# ---- 3.2 Steps to stabilise the population (F041-F045) ----
story.append(heading("3.2", "Steps to stabilise the population", 2))
story.append(Paragraph(
    "Therefore, the government was forced to take up serious measures to check this population growth rate. <b>The most "
    "important step to overcome this problem is to motivate smaller families by using various contraceptive methods.</b>",
    STYLES["Body"]))
story.append(Paragraph(
    "The message is carried by <b>advertisements in the media as well as posters/bills, etc., showing a happy couple with "
    "two children with a slogan <i>Hum Do Hamare Do</i> (we two, our two)</b>. <b>Many couples, mostly the young, urban, "
    "working ones have even adopted an 'one child norm'</b>.", STYLES["Body"]))
story.append(Paragraph(
    "<b>Statutory raising of marriageable age of the female to 18 years and that of males to 21 years</b>, and <b>incentives "
    "given to couples with small families</b> are two of the other measures taken to tackle this problem.", STYLES["Body"]))
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
story.append(Paragraph(
    "<b>Natural methods work on the principle of avoiding chances of ovum and sperms meeting.</b> "
    "<b>Periodic abstinence</b> is one such method in which the couples avoid coitus <b>from day 10 to 17 of the menstrual cycle</b> "
    "when ovulation could be expected. As chances of fertilisation are very high during this period, it is called the <b>fertile "
    "period</b>.", STYLES["Body"]))
story.append(Paragraph(
    "<b>Withdrawal or coitus interruptus</b> is another method in which the <b>male partner withdraws his penis from the vagina just "
    "before ejaculation</b> so as to avoid insemination.", STYLES["Body"]))
story.append(Paragraph(
    "<b>Lactational amenorrhea</b> (absence of menstruation) method is based on the fact that <b>ovulation and therefore the cycle do "
    "not occur during the period of intense lactation following parturition</b>. Therefore, as long as the <b>mother breast-feeds the "
    "child fully, chances of conception are almost nil</b>. However, this method has been reported to be <b>effective only upto a maximum "
    "period of six months following parturition</b>.", STYLES["Body"]))
story.append(Paragraph(
    "As <b>no medicines or devices</b> are used in these methods, <b>side effects are almost nil</b>. <b>Chances of failure, though, of "
    "this method are also high.</b>", STYLES["Body"]))
story.append(Spacer(1, 3))

# ---- 3.2 Barrier methods -- detail ----
story.append(heading("3.2", "Barrier methods", 3))
story.append(Paragraph(
    "In barrier methods, <b>ovum and sperms are prevented from physically meeting with the help of barriers</b>. Such methods are "
    "<b>available for both males and females</b>.", STYLES["Body"]))
story.append(Paragraph(
    "<b>Condoms (Figure 3.1 a, b) are barriers made of thin rubber/latex sheath</b> that are used to <b>cover the penis in the male or "
    "vagina and cervix in the female, just before coitus</b> so that the <b>ejaculated semen would not enter into the female "
    "reproductive tract</b>.", STYLES["Body"]))
story.append(Paragraph(
    "<b>Nirodh</b> is a popular brand of condom for the male. <b>Use of condoms has increased in recent years due to its additional "
    "benefit of protecting the user from contracting STIs and AIDS.</b> Both the <b>male and the female condoms are disposable, can be "
    "self-inserted and thereby gives privacy</b> to the user.", STYLES["Body"]))
story.append(Paragraph(
    "<b>Diaphragms, cervical caps and vaults</b> are also barriers made of <b>rubber that are inserted into the female reproductive "
    "tract to cover the cervix</b> during coitus. They <b>prevent conception by blocking the entry of sperms through the cervix</b>. "
    "They are <b>reusable</b>.", STYLES["Body"]))
story.append(Paragraph(
    "<b>Spermicidal creams, jellies and foams are usually used alongwith these barriers to increase their contraceptive efficiency.</b>",
    STYLES["Body"]))
story.append(Spacer(1, 3))

# ---- 3.2 IUDs -- detail ----
story.append(heading("3.2", "Intra-uterine devices (IUDs)", 3))
story.append(Paragraph(
    "Another effective and popular method is the use of <b>Intra Uterine Devices (IUDs)</b>. <b>These devices are inserted by doctors "
    "or expert nurses in the uterus through vagina.</b>", STYLES["Body"]))
story.append(Paragraph(
    "These Intra Uterine Devices are presently available as the <b>non-medicated IUDs (e.g., Lippes loop), copper releasing IUDs "
    "(CuT, Cu7, Multiload 375) and the hormone releasing IUDs (Progestasert, LNG-20)</b> (Figure 3.2).", STYLES["Body"]))
story.append(Paragraph(
    "<b>IUDs increase phagocytosis of sperms within the uterus and the Cu ions released suppress sperm motility and the fertilising "
    "capacity of sperms.</b> The <b>hormone releasing IUDs, in addition, make the uterus unsuitable for implantation and the cervix "
    "hostile to the sperms.</b>", STYLES["Body"]))
story.append(Paragraph(
    "<b>IUDs are ideal contraceptives for the females who want to delay pregnancy and/or space children.</b> <b>It is one of most "
    "widely accepted methods of contraception in India.</b>", STYLES["Body"]))
story.append(Spacer(1, 3))

# ---- 3.2 Oral, injectable, implant and emergency ----
story.append(heading("3.2", "Oral contraceptives, injectables, implants and emergency contraception", 3))
story.append(Paragraph(
    "<b>Oral administration of small doses of either progestogens or progestogen-estrogen combinations</b> is another contraceptive "
    "method used by the females. They are used in the form of <b>tablets and hence are popularly called the pills</b>.", STYLES["Body"]))
story.append(Paragraph(
    "<b>Pills have to be taken daily for a period of 21 days starting preferably within the first five days of menstrual cycle.</b> "
    "<b>After a gap of 7 days</b> (during which menstruation occurs) <b>it has to be repeated in the same pattern till the female "
    "desires to prevent conception.</b> They <b>inhibit ovulation and implantation as well as alter the quality of cervical mucus to "
    "prevent/retard entry of sperms</b>.", STYLES["Body"]))
story.append(Paragraph(
    "<b>Pills are very effective with lesser side effects and are well accepted by the females.</b> <b>Saheli -- the new oral "
    "contraceptive for the females contains a non-steroidal preparation.</b> It is a <b>once a week pill with very few side effects "
    "and high contraceptive value</b>.", STYLES["Body"]))
story.append(Paragraph(
    "<b>Progestogens alone or in combination with estrogen can also be used by females as injections or implants under the skin</b> "
    "(Figure 3.3). Their <b>mode of action is similar to that of pills and their effective periods are much longer</b>.",
    STYLES["Body"]))
story.append(Paragraph(
    "<b>Administration of progestogens or progestogen-estrogen combinations or IUDs within 72 hours of coitus</b> have been found to be "
    "<b>very effective as emergency contraceptives</b> as they could be used to avoid possible pregnancy due to <b>rape or casual "
    "unprotected intercourse</b>.", STYLES["Body"]))
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
story.append(Paragraph(
    "<b>Selection of a suitable contraceptive method and its use should always be undertaken in consultation with qualified medical "
    "professionals.</b>", STYLES["Body"]))
story.append(Paragraph(
    "<b>Contraceptives are not regular requirements for the maintenance of reproductive health.</b> In fact, they are <b>practiced "
    "against a natural reproductive event, i.e., conception/pregnancy</b>. One is <b>forced to use these methods either to prevent "
    "pregnancy or to delay or space pregnancy due to personal reasons</b>.", STYLES["Body"]))
story.append(Paragraph(
    "<b>No doubt, the widespread use of these methods have a significant role in checking uncontrolled growth of population.</b> "
    "However, their <b>possible ill-effects like nausea, abdominal pain, breakthrough bleeding, irregular menstrual bleeding or even "
    "breast cancer, though not very significant, should not be totally ignored</b>.", STYLES["Body"]))
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
story.append(Paragraph(
    "<b>Nearly 45 to 50 million MTPs are performed in a year all over the world which accounts to 1/5th of the total number "
    "of conceived pregnancies in a year.</b> Whether to accept / legalise MTP or not is being debated upon in many "
    "countries due to <b>emotional, ethical, religious and social issues</b> involved in it.", STYLES["Body"]))
story.append(Paragraph(
    "<b>Government of India legalised MTP in 1971 with some strict conditions to avoid its misuse.</b> Such restrictions are "
    "all the more important to <b>check indiscriminate and illegal female foeticides which are reported to be high in India</b>.",
    STYLES["Body"]))
story.append(Spacer(1, 2))

# ---- 3.3 Why MTP, and its safety window ----
story.append(heading("3.3", "Why MTP, and when it is safest", 2))
story.append(Paragraph(
    "Why MTP? Obviously the answer is -- <b>to get rid of unwanted pregnancies either due to casual unprotected intercourse or "
    "failure of the contraceptive used during coitus or rapes</b>. <b>MTPs are also essential in certain cases where continuation "
    "of the pregnancy could be harmful or even fatal either to the mother or to the foetus or both.</b>", STYLES["Body"]))
story.append(Paragraph(
    "<b>MTPs are considered relatively safe during the first trimester, i.e., upto 12 weeks of pregnancy.</b> <b>Second trimester "
    "abortions are much more riskier.</b>", STYLES["Body"]))
story.append(Paragraph(
    "<b>One disturbing trend observed is that a majority of the MTPs are performed illegally by unqualified quacks which are not "
    "only unsafe but could be fatal too.</b> <b>Another dangerous trend is the misuse of amniocentesis to determine the sex of "
    "the unborn child.</b> <b>Frequently, if the foetus is found to be female, it is followed by MTP -- this is totally against "
    "what is legal</b> and such practices should be avoided because these are dangerous both for the young mother and the foetus.",
    STYLES["Body"]))
story.append(Paragraph(
    "<b>Effective counselling on the need to avoid unprotected coitus and the risk factors involved in illegal abortions as well as "
    "providing more health care facilities could reverse the mentioned unhealthy trend.</b>", STYLES["Body"]))
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
story.append(Spacer(1, 54))

# =============================== 3.4 STIs ===========================================
# ---- 3.4 Sexually Transmitted Infections (F119-F133) ----
story.append(heading("3.4", "SEXUALLY TRANSMITTED INFECTIONS (STIs)", 1))
# Contents box lists "Sexually Transmitted Diseases" while the section heading and summary use STIs -- both are the same group.
story.append(keyterm(
    "<b>Infections or diseases which are transmitted through sexual intercourse are collectively called sexually transmitted "
    "infections (STI) or venereal diseases (VD) or reproductive tract infections (RTI)</b> -- the opener defines the term used in "
    "its own heading."))
story.append(Paragraph(
    "<b>Gonorrhoea, syphilis, genital herpes, chlamydiasis, genital warts, trichomoniasis, hepatitis-B and of course, the most "
    "discussed infection in the recent years, HIV leading to AIDS are some of the common STIs.</b> Among these, <b>HIV infection "
    "is most dangerous and is discussed in detail in Chapter 7</b>.", STYLES["Body"]))
story.append(Paragraph(
    "<b>Some of these infections like hepatitis-B and HIV can also be transmitted by sharing of injection needles, surgical "
    "instruments, etc., with infected persons, transfusion of blood, or from an infected mother to the foetus too.</b>",
    STYLES["Body"]))
story.append(Paragraph(
    "<b>Except for hepatitis-B, genital herpes and HIV infections, other diseases are completely curable if detected early and "
    "treated properly.</b>", STYLES["Body"]))
story.append(Spacer(1, 2))

# ---- 3.4 Symptoms, stigma and complications ----
story.append(heading("3.4", "Symptoms, stigma and complications", 2))
story.append(Paragraph(
    "<b>Early symptoms of most of these are minor and include itching, fluid discharge, slight pain, swellings, etc., in the "
    "genital region.</b> <b>Infected females may often be asymptomatic and hence, may remain undetected for long.</b> <b>Absence or "
    "less significant symptoms in the early stages of infection and the social stigma attached to the STIs, deter the infected "
    "persons from going for timely detection and proper treatment.</b>", STYLES["Body"]))
story.append(Paragraph(
    "This could lead to complications later, which include <b>pelvic inflammatory diseases (PID), abortions, still births, ectopic "
    "pregnancies, infertility or even cancer of the reproductive tract</b>. <b>STIs are a major threat to a healthy society.</b> "
    "Therefore, <b>prevention or early detection and cure of these diseases are given prime consideration under the reproductive "
    "health-care programmes</b>.", STYLES["Body"]))
story.append(Paragraph(
    "Though all persons are vulnerable to these infections, their <b>incidences are reported to be very high among persons in the age "
    "group of 15-24 years -- the age group to which you also belong</b>.", STYLES["Body"]))
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
story.append(Paragraph(
    "A discussion on reproductive health is incomplete without a mention of infertility. <b>A large number of couples all over the "
    "world including India are infertile, i.e., they are unable to produce children inspite of unprotected sexual co-habitation -- "
    "the summary adds the diagnostic criterion of <b>even after 2 years of unprotected sexual cohabitation</b>.</b>", STYLES["Body"]))
story.append(Paragraph(
    "<b>The reasons for this could be many -- physical, congenital, diseases, drugs, immunological or even psychological.</b> "
    "<b>In India, often the female is blamed for the couple being childless, but more often than not, the problem lies in the "
    "male partner.</b>", STYLES["Body"]))
story.append(Paragraph(
    "<b>Specialised health care units (infertility clinics, etc.) could help in diagnosis and corrective treatment of some of these "
    "disorders and enable these couples to have children.</b> However, where such corrections are not possible, the couples could be "
    "<b>assisted to have children through certain special techniques commonly known as assisted reproductive technologies (ART)</b>.",
    STYLES["Body"]))
story.append(Spacer(1, 2))

# ---- 3.5 ART: IVF, ZIFT, IUT, GIFT ----
story.append(heading("3.5", "Assisted reproductive technologies", 2))
story.append(keyterm(
    "<b>In vitro fertilisation (IVF -- fertilisation outside the body in almost similar conditions as that in the body) followed by "
    "embryo transfer (ET) is one of such methods.</b>"))
story.append(Paragraph(
    "In this method, popularly known as <b>test tube baby programme</b>, <b>ova from the wife/donor (female) and sperms from the "
    "husband/donor (male) are collected and are induced to form zygote under simulated conditions in the laboratory</b>. The "
    "<b>zygote or early embryos (with upto 8 blastomeres) could then be transferred into the fallopian tube (ZIFT -- zygote intra "
    "fallopian transfer) and embryos with more than 8 blastomeres, into the uterus (IUT -- intra uterine transfer), to complete "
    "its further development</b>. <b>Embryos formed by in-vivo fertilisation (fusion of gametes within the female) also could be "
    "used for such transfer to assist those females who cannot conceive.</b>", STYLES["Body"]))
story.append(Paragraph(
    "<b>Transfer of an ovum collected from a donor into the fallopian tube (GIFT -- gamete intra fallopian transfer) of another "
    "female who cannot produce one, but can provide suitable environment for fertilisation and further development is another method "
    "attempted.</b>", STYLES["Body"]))
story.append(Paragraph(
    "<b>Intra cytoplasmic sperm injection (ICSI) is another specialised procedure to form an embryo in the laboratory in which a sperm "
    "is directly injected into the ovum.</b>", STYLES["Body"]))

# ---- 3.5 AI / IUI and the limits of ART ----
story.append(heading("3.5", "Artificial insemination and the limits of ART", 2))
story.append(Paragraph(
    "<b>Infertility cases either due to inability of the male partner to inseminate the female or due to very low sperm counts in the "
    "ejaculates, could be corrected by artificial insemination (AI) technique.</b> In this technique, the <b>semen collected either "
    "from the husband or a healthy donor is artificially introduced either into the vagina or into the uterus (IUI -- intra-uterine "
    "insemination)</b> of the female.", STYLES["Body"]))
story.append(Paragraph(
    "Though options are many, <b>all these techniques require extremely high precision handling by specialised professionals and "
    "expensive instrumentation</b>. Therefore, <b>these facilities are presently available only in very few centres in the country</b> "
    "and obviously their benefits is affordable to only a limited number of people. <b>Emotional, religious and social factors are also "
    "deterrents in the adoption of these methods.</b>", STYLES["Body"]))
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
