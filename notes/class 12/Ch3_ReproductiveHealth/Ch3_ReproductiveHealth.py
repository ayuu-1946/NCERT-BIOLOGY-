"""
NCERT Class 12 Biology, Chapter 3 - Reproductive Health
NEET replacement notes -> A4 print-ready PDF.

Built under SUPREME COMMAND PROMPT.md v6, Pass 2: written linearly from the
frozen 162-row inventory (Ch3_ReproductiveHealth_inventory.md), importing the
repo-level frozen style module `neet_template.py` (v6 SS0.6). No style,
geometry, colour or font is re-declared here.

Block markers `# ---- N.N ----` mark every NCERT section so a Pass 3 flag can be
found and fixed in one contiguous block. Inventory row IDs are named in the
comments so any fact can be traced back to its frozen row.

Filler filtering (Rule 3) is active: 5 class-C filler rows (F005, F010, F046,
F053, F063) are deliberately not printed as standalone sentences because they
restate what neighbours already say; 7 class-B rows are folded into neighbours
rather than printed alone (F035, F041, F070, F113, F132, F135, F151). The four
figure-metadata rows F157-F160 are not printed as text - the asset plus its
caption carries them. Every one is still ticked as "accounted for by Rule 3"
per the inventory tick legend. See end of file for complete removal list.

Source: Chapter/class 12/Chapter 3 - Reproductive Health.pdf
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
    STYLES, FRAME_WIDTH, DARK_GREY, GRID_LINE,
    heading, keyterm, process_flow, note, memory_aid, data_table, title_block, build_pdf,
)
from neet_template import figure as _shared_figure  # noqa: E402
from reportlab.platypus import Paragraph, Spacer  # noqa: E402

ASSETS = os.path.join(HERE, "assets")
OUT_PDF = os.path.join(HERE, "Ch3_ReproductiveHealth.pdf")


def figure(asset_name, caption_text, max_width_cm=15.9):
    """Chapter-local binding of the shared figure() helper (SS0.6)."""
    return _shared_figure(asset_name, caption_text, ASSETS, max_width_cm=max_width_cm)


def body(text):
    return Paragraph(text, STYLES["Body"])


def b1(text):
    return Paragraph("&bull; " + text, STYLES["Bullet1"])


def b2(text):
    return Paragraph("- " + text, STYLES["Bullet2"])


story = []

# ======================================================================================
# ---- Title block (SS5 item 1) ---- F001, F002 (contents box is covered by the five headings below)
# ======================================================================================
story += title_block("Reproductive Health")

# ======================================================================================
# ---- 3.0 Reproductive Health (unnumbered chapter introduction) ---- F003-F010 (opener F004, heading F003)
# ======================================================================================
# F005 and F010 are class-C filler: "Now, let's discuss..." and the two framing
# questions are not printed as standalone lines - the tutor paragraph below asks the
# question once in its own words, and F004/F008 already open the chapter.
story.append(heading("3.0", "Reproductive Health", 1))
story.append(body(
    "You have learnt about the <b>human reproductive system and its functions in "
    "Chapter 2</b>. <b>Reproductive health</b> is the closely related next idea - "
    "what it means, why it matters, and how it is achieved."))
story.append(body(
    "The term <b>simply refers to healthy reproductive organs with normal functions</b> "
    "(F006), but it <b>has a broader perspective and includes the emotional and social "
    "aspects of reproduction also</b> (F007)."))
story.append(keyterm(
    "According to the <b>World Health Organisation (WHO)</b>, <b>reproductive health "
    "means a total well-being in all aspects of reproduction, i.e., physical, emotional, "
    "behavioural and social</b> (F008). <b>Therefore, a society with people having "
    "physically and functionally normal reproductive organs and normal emotional and "
    "behavioural interactions among them in all sex-related aspects might be called "
    "reproductively healthy</b> (F009)."))
# F010 accounted for by Rule 3: the paragraph above already poses the significance
# question, so the verbatim NCERT framing sentence is filtered.

# ======================================================================================
# ---- 3.1 REPRODUCTIVE HEALTH - PROBLEMS AND STRATEGIES ---- F011-F030 (heading F011, opener F012)
# ======================================================================================
story.append(heading("3.1", "Reproductive Health - Problems and Strategies", 1))
# F012 carries both wordings: body "amongst the first countries" + summary-unique "the first nation in the world"
story.append(body(
    "<b>India was amongst the first countries in the world</b> to <b>initiate action plans "
    "and programmes at a national level to attain total reproductive health as a social goal</b> "
    "(F012). The summary states the same fact more strongly as <b>the first nation in the world</b> "
    "to do so - both wordings are carried here (F012 SUMMARY-UNIQUE fold). These programmes called "
    "<b>family planning were initiated in 1951</b> and were <b>periodically assessed over the past "
    "decades</b> (F013)."))
story.append(body(
    "<b>Improved programmes covering wider reproduction-related areas are currently in operation "
    "under the popular name Reproductive and Child Health Care (RCH) programmes</b> (F014). "
    "<b>Creating awareness among people about various reproduction related aspects and providing "
    "facilities and support for building up a reproductively healthy society are the major tasks "
    "under these programmes</b> (F015)."))
story.append(body(
    "<b>With the help of audio-visual and the print-media, governmental and non-governmental agencies "
    "have taken various steps to create awareness among the people about reproduction-related aspects</b> "
    "(F016). <b>Parents, other close relatives, teachers and friends, also have a major role in the "
    "dissemination of the above information</b> (F017). <b>Introduction of sex education in schools "
    "should also be encouraged to provide right information to the young so as to discourage children "
    "from believing in myths and having misconceptions about sex-related aspects</b> (F018)."))
story.append(body(
    "<b>Proper information about reproductive organs, adolescence and related changes, safe and hygienic "
    "sexual practices, sexually transmitted diseases (STD), AIDS, etc., would help people, especially "
    "those in the adolescent age group to lead a reproductively healthy life</b> (F019)."))
story.append(body(
    "<b>Educating people, especially fertile couples and those in marriageable age group, about available "
    "birth control options, care of pregnant mothers, post-natal care of the mother and child, importance "
    "of breast feeding, equal opportunities for the male and the female child, etc., would address the "
    "importance of bringing up socially conscious healthy families of desired size</b> (F020)."))
story.append(body(
    "<b>Awareness of problems due to uncontrolled population growth, social evils like sex-abuse and "
    "sex-related crimes, etc., need to be created to enable people to think and take up necessary steps "
    "to prevent them and thereby build up a socially responsible and healthy society</b> (F021)."))
story.append(body(
    "<b>Successful implementation of various action plans to attain reproductive health requires strong "
    "infrastructural facilities, professional expertise and material support</b> (F022). <b>These are "
    "essential to provide medical assistance and care to people in reproduction-related problems like "
    "pregnancy, delivery, STDs, abortions, contraception, menstrual problems, infertility, etc.</b> "
    "(F023). <b>Implementation of better techniques and new strategies from time to time are also required "
    "to provide more efficient care and assistance to people</b> (F024)."))
story.append(body(
    "<b>Statutory ban on amniocentesis for sex-determination to legally check increasing menace of female "
    "foeticides, massive child immunisation, etc., are some programmes that merit mention in this connection</b> "
    "(F025). NCERT prints the word as <b>aminocentesis</b>; the correct spelling is amniocentesis."))
story.append(keyterm(
    "<b>Amniocentesis:</b> <b>some of the amniotic fluid of the developing foetus is taken to analyse the "
    "fetal cells and dissolved substances</b> (F026). <b>This procedure is used to test for the presence of "
    "certain genetic disorders such as, down syndrome, haemophilia, sickle-cell anemia, etc., determine the "
    "survivability of the foetus</b> (F027) - the source sentence is garbled and prints haemoplilia for "
    "haemophilia, reproduced here with the correct term."))
story.append(body(
    "<b>Research on various reproduction-related areas are encouraged and supported by governmental and "
    "non-governmental agencies to find out new methods and/or to improve upon the existing ones</b> (F028)."))
story.append(note(
    "<b>Saheli - a new oral contraceptive for the females - was developed by scientists at Central Drug "
    "Research Institute (CDRI) in Lucknow, India</b> (F029)."))
story.append(body(
    "<b>Better awareness about sex related matters, increased number of medically assisted deliveries and better "
    "post-natal care leading to decreased maternal and infant mortality rates, increased number of couples with "
    "small families, better detection and cure of STDs and overall increased medical facilities for all sex-related "
    "problems, etc. all indicate improved reproductive health of the society</b> (F030). The summary adds one more "
    "indicator to this list - <b>assistance to infertile couples</b> (F030 SUMMARY-UNIQUE fold)."))

# ======================================================================================
# ---- 3.2 POPULATION STABILISATION AND BIRTH CONTROL ---- F031-F099 (heading F031, opener F032)
# ======================================================================================
story.append(heading("3.2", "Population Stabilisation and Birth Control", 1, has_table=True))
# Note heading mismatch: contents box says "Population Explosion and Birth Control" (F002/F031); the
# section heading on page 43 reads "POPULATION STABILISATION AND BIRTH CONTROL" (F031) - both recorded.
story.append(body(
    "<b>In the last century an all-round development in various fields significantly improved the quality of life "
    "of the people</b> (F032). <b>However, increased health facilities along with better living conditions had an "
    "explosive impact on the growth of population</b> (F033) - this explosive growth is the population explosion "
    "of Exercise Q5 and the summary."))
story.append(body(
    "<b>The world population which was around 2 billion (2000 million) in 1900 rocketed to about 6 billion by 2000 "
    "and 7.2 billion in 2011</b> (F034). <b>A similar trend was observed in India too</b> (F035, folded) - <b>our "
    "population which was approximately 350 million at the time of our independence reached close to the billion "
    "mark by 2000 and crossed 1.2 billion in May 2011</b> (F036)."))
story.append(body(
    "<b>A rapid decline in death rate, maternal mortality rate (MMR) and infant mortality rate (IMR) as well as an "
    "increase in number of people in reproducible age are probable reasons for this</b> (F037). <b>Through our "
    "Reproductive Child Health (RCH) programme, though we could bring down the population growth rate, it was only "
    "marginal</b> (F038). <b>According to the 2011 census report, the population growth rate was less than 2 per cent, "
    "i.e., 20/1000/year, a rate at which our population could increase rapidly</b> (F039). <b>Such an alarming growth "
    "rate could lead to an absolute scarcity of even the basic requirements, i.e., food, shelter and clothing, in spite "
    "of significant progress made in those areas</b> (F040). <b>Therefore, the government was forced to take up serious "
    "measures to check this population growth rate</b> (F041, folded) - <b>the most important step to overcome this "
    "problem is to motivate smaller families by using various contraceptive methods</b> (F042)."))
story.append(body(
    "<b>Advertisements in the media as well as posters/bills, etc., showing a happy couple with two children with a "
    "slogan Hum Do Hamare Do (we two, our two)</b> (F043) illustrate the message. <b>Many couples, mostly the young, "
    "urban, working ones have even adopted an one child norm</b> (F044). <b>Statutory raising of marriageable age of the "
    "female to 18 years and that of males to 21 years, and incentives given to couples with small families are two of the "
    "other measures taken to tackle this problem</b> (F045)."))
# F046 class-C filler "Let us describe..." is not printed as a standalone line - F042 already states the purpose.
story.append(keyterm(
    "<b>An ideal contraceptive should be user-friendly, easily available, effective and reversible with no or least "
    "side-effects</b> (F047). <b>It also should in no way interfere with the sexual drive, desire and/or the sexual act "
    "of the user</b> (F048)."))
story.append(body(
    "<b>A wide range of contraceptive methods are presently available which could be broadly grouped into the following "
    "categories, namely Natural/Traditional, Barrier, IUDs, Oral contraceptives, Injectables, Implants and Surgical "
    "methods</b> (F049). The table below compares them; the following paragraphs give the details named in it."))
# --- Contraceptive comparison table (covers F050-F093 categories) ---
story.append(data_table([
    ["Category", "Principle / How it works", "Key examples / Notes"],
    ["<b>Natural / Traditional</b> (F050)",
     "<b>Avoid chances of ovum and sperms meeting; no medicines or devices</b>; side effects <b>almost nil</b> (F058) but <b>chances of failure are also high</b> (F059)",
     "<b>Periodic abstinence:</b> avoid coitus <b>day 10 to 17</b> of cycle (F051); this is the <b>fertile period</b> (F052). "
     "<b>Withdrawal / coitus interruptus:</b> male withdraws penis before ejaculation to avoid insemination (F054). "
     "<b>Lactational amenorrhea:</b> absence of menstruation; ovulation does not occur during intense lactation after parturition (F055); "
     "as long as mother breast-feeds fully, <b>chances of conception are almost nil</b> (F056), but effective <b>only upto six months</b> after parturition (F057)"],
    ["<b>Barrier</b> (F060)",
     "<b>Ovum and sperms prevented from physically meeting with help of barriers</b>; available <b>for both males and females</b> (F061)",
     "<b>Condoms (Fig. 3.1a, b): barriers made of thin rubber/latex sheath</b> covering penis or vagina and cervix before coitus so ejaculated semen does not enter female tract (F062); "
     "<b>Nirodh</b> is a popular male brand (F064); <b>protects also from STIs and AIDS</b> (F065); <b>disposable, self-inserted, gives privacy</b> (F066). "
     "<b>Diaphragms, cervical caps and vaults:</b> rubber barriers inserted to cover cervix (F067); <b>block entry of sperms</b> through cervix and <b>are reusable</b> (F068). "
     "<b>Spermicidal creams, jellies and foams usually used alongwith barriers</b> increase efficiency (F069)"],
    ["<b>IUDs</b> (F070-F076)",
     "Inserted by <b>doctors or expert nurses in uterus through vagina</b> (F071); increase <b>phagocytosis of sperms</b> and <b>Cu ions suppress sperm motility and fertilising capacity</b> (F073); "
     "hormone-releasing IUDs in addition <b>make uterus unsuitable for implantation and cervix hostile to sperms</b> (F074); "
     "<b>ideal for females who want to delay pregnancy and/or space children</b> (F075); <b>one of most widely accepted methods in India</b> (F076)",
     "<b>Non-medicated:</b> Lippes loop; <b>Copper-releasing:</b> CuT, Cu7, Multiload 375; <b>Hormone-releasing:</b> Progestasert, LNG-20 (Fig. 3.2) (F072)"],
    ["<b>Oral contraceptives (pills)</b> (F077-F084)",
     "<b>Inhibit ovulation and implantation and alter quality of cervical mucus to prevent / retard entry of sperms</b> (F081); "
     "<b>very effective with lesser side effects and well accepted by females</b> (F082)",
     "<b>Progestogens or progestogen-estrogen combinations</b> taken as tablets, popularly called <b>pills</b> (F077-F078); "
     "<b>taken daily for 21 days starting preferably within first 5 days of menstrual cycle; after a gap of 7 days (menstruation occurs) repeat same pattern</b> till desire to prevent conception (F079-F080). "
     "<b>Saheli:</b> contains non-steroidal preparation; <b>once a week pill with very few side effects and high contraceptive value</b> (F083-F084)"],
    ["<b>Injectables / Implants</b> (F085-F086)",
     "Mode of action <b>similar to pills; effective periods much longer</b> (F086)",
     "<b>Progestogens alone or in combination with estrogen can also be used as injections or implants under skin (Fig. 3.3)</b> (F085)"],
    ["<b>Emergency contraception</b> (F087)",
     "Within <b>72 hours of coitus</b>, very effective to avoid possible pregnancy due to rape or casual unprotected intercourse",
     "<b>Progestogens or progestogen-estrogen combinations or IUDs within 72 hours of coitus</b> (F087)"],
    ["<b>Surgical (sterilisation)</b> (F088-F093)",
     "<b>Blocks gamete transport and thereby prevents conception</b> (F089); <b>highly effective but reversibility very poor</b> (F093)",
     "<b>Generally advised as terminal method to prevent any more pregnancies</b> (F088). "
     "<b>Male - vasectomy</b> and <b>female - tubectomy</b> (F090). "
     "<b>Vasectomy:</b> small part of <b>vas deferens is removed or tied up through small incision on scrotum (Fig. 3.4a) - Vas deferens tied and cut</b> (F091). "
     "<b>Tubectomy:</b> small part of <b>fallopian tube is removed (Fig. 3.4b) or tied up through incision in abdomen or through vagina - Fallopian tubes tied and cut</b> (F092)"],
], col_widths=[2.0, 3.4, 5.2]))
# F053 and F063 are class-C filler: "Therefore by abstaining..." and "This can prevent conception" are already inside the table cells above, so not printed standalone.
# Figures for barrier and IUD and implant and sterilisation - placed inline at topic (S5 inline rule)
story.append(figure(
    "fig_3_1a.png",
    "Fig. 3.1a - Condom for the male. A barrier made of thin rubber/latex sheath used to cover the penis so that ejaculated semen does not enter the female reproductive tract.",
    max_width_cm=9.5))
story.append(figure(
    "fig_3_1b.png",
    "Fig. 3.1b - Condom for the female. A barrier made of thin rubber/latex sheath used to cover the vagina and cervix so that ejaculated semen does not enter the female reproductive tract.",
    max_width_cm=9.5))
story.append(figure(
    "fig_3_2.png",
    "Fig. 3.2 - Copper T (CuT). An example of a copper-releasing IUD inserted in the uterus through the vagina.",
    max_width_cm=9.0))
story.append(figure(
    "fig_3_3.png",
    "Fig. 3.3 - Implants. Progestogen or progestogen-estrogen implants placed under the skin; mode similar to pills but effective for much longer.",
    max_width_cm=9.0))
story.append(figure(
    "fig_3_4a.png",
    "Fig. 3.4a - Vasectomy. A small part of the vas deferens is removed or tied up through a small incision on the scrotum. Label: Vas deferens tied and cut.",
    max_width_cm=9.5))
story.append(figure(
    "fig_3_4b.png",
    "Fig. 3.4b - Tubectomy. A small part of the fallopian tube is removed or tied up through an incision in the abdomen or through the vagina. Label: Fallopian tubes tied and cut.",
    max_width_cm=9.5))
# Post-method facts - F094-F099
story.append(body(
    "<b>Selection of a suitable contraceptive method and its use should always be undertaken in consultation with "
    "qualified medical professionals</b> (F094)."))
story.append(body(
    "<b>Contraceptives are not regular requirements for the maintenance of reproductive health</b> (F095). <b>In fact, they "
    "are practiced against a natural reproductive event, i.e., conception/pregnancy</b> (F096). <b>One is forced to use these "
    "methods either to prevent pregnancy or to delay or space pregnancy due to personal reasons</b> (F097)."))
story.append(body(
    "<b>No doubt, the widespread use of these methods have a significant role in checking uncontrolled growth of population</b> "
    "(F098). <b>However, their possible ill-effects like nausea, abdominal pain, breakthrough bleeding, irregular menstrual "
    "bleeding or even breast cancer, though not very significant, should not be totally ignored</b> (F099)."))
story.append(memory_aid(
    "To recall the seven contraceptive categories in NCERT order, remember <b>N-B-I-O-I-I-S</b>: "
    "<b>N</b>atural, <b>B</b>arrier, <b>I</b>UDs, <b>O</b>ral (pills), <b>I</b>njectables, <b>I</b>mplants, "
    "<b>S</b>urgical. Pills need <b>21 + 7</b> days; emergency is <b>72 hours</b>; lactational cover is <b>6 months</b> only."))

# ======================================================================================
# ---- 3.3 MEDICAL TERMINATION OF PREGNANCY (MTP) ---- F100-F118 (heading F100, opener F101)
# ======================================================================================
story.append(heading("3.3", "Medical Termination of Pregnancy (MTP)", 1))
story.append(keyterm(
    "<b>Intentional or voluntary termination of pregnancy before full term is called medical termination of pregnancy "
    "(MTP) or induced abortion</b> (F101) - the opener defines the term used in its own section heading."))
story.append(body(
    "<b>Nearly 45 to 50 million MTPs are performed in a year all over the world which accounts to 1/5th of the total "
    "number of conceived pregnancies in a year</b> (F102). <b>Whether to accept / legalise MTP or not is being debated upon "
    "in many countries due to emotional, ethical, religious and social issues involved in it</b> (F103)."))
story.append(body(
    "<b>Government of India legalised MTP in 1971 with some strict conditions to avoid its misuse</b> (F104). "
    "<b>Such restrictions are all the more important to check indiscriminate and illegal female foeticides which are "
    "reported to be high in India</b> (F105)."))
story.append(body(
    "<b>Why MTP? Obviously the answer is - to get rid of unwanted pregnancies either due to casual unprotected intercourse "
    "or failure of the contraceptive used during coitus or rapes</b> (F106, as a question-and-answer pair). "
    "<b>MTPs are also essential in certain cases where continuation of the pregnancy could be harmful or even fatal either "
    "to the mother or to the foetus or both</b> (F107)."))
story.append(body(
    "<b>MTPs are considered relatively safe during the first trimester, i.e., upto 12 weeks of pregnancy</b> (F108). "
    "<b>Second trimester abortions are much more riskier</b> (F109)."))
story.append(body(
    "<b>One disturbing trend observed is that a majority of the MTPs are performed illegally by unqualified quacks which "
    "are not only unsafe but could be fatal too</b> (F110). <b>Another dangerous trend is the misuse of amniocentesis to "
    "determine the sex of the unborn child</b> (F111). <b>Frequently, if the foetus is found to be female, it is followed "
    "by MTP - this is totally against what is legal</b> (F112) <b>and such practices should be avoided because these are "
    "dangerous both for the young mother and the foetus</b> (F113, folded onto F112)."))
story.append(body(
    "<b>Effective counselling on the need to avoid unprotected coitus and the risk factors involved in illegal abortions "
    "as well as providing more health care facilities could reverse the mentioned unhealthy trend</b> (F114)."))
story.append(note(
    "<b>The Medical Termination of Pregnancy (Amendment) Act, 2017 was enacted by the government of India with the "
    "intension of reducing the incidence of illegal abortion and consequent maternal mortality and morbidity</b> (F115) - "
    "source prints intension for intention."))
# MTP Act grounds as process_flow (two grounds) and time limits
story.append(body(
    "Under the Act, a pregnancy may be terminated on certain considered grounds and within strict time limits:"))
story.append(process_flow([
    "<b>Within the first 12 weeks</b> of pregnancy, on the opinion of <b>one registered medical practitioner</b> (F116).",
    "<b>More than 12 weeks but fewer than 24 weeks</b>, on the opinion of <b>two registered medical practitioners</b>, "
    "formed in good faith, that the required grounds exist (F117).",
    "Ground <b>(i): continuation of the pregnancy would involve a risk to the life of the pregnant woman or of grave "
    "injury to her physical or mental health</b> (F118).",
    "Ground <b>(ii): there is a substantial risk that if the child were born, it would suffer from such physical or "
    "mental abnormalities as to be seriously handicapped</b> (F118).",
]))

# ======================================================================================
# ---- 3.4 SEXUALLY TRANSMITTED INFECTIONS (STIs) ---- F119-F133 (heading F119, opener F120)
# ======================================================================================
story.append(heading("3.4", "Sexually Transmitted Infections (STIs)", 1))
# Heading variant: contents box lists "Sexually Transmitted Diseases" (F119 parenthetical); summary calls them STIs - both carried.
story.append(keyterm(
    "<b>Infections or diseases which are transmitted through sexual intercourse are collectively called sexually transmitted "
    "infections (STI) or venereal diseases (VD) or reproductive tract infections (RTI)</b> (F120) - the opener defines the "
    "term used in its own heading."))
story.append(body(
    "<b>Gonorrhoea, syphilis, genital herpes, chlamydiasis, genital warts, trichomoniasis, hepatitis-B and of course, the "
    "most discussed infection in the recent years, HIV leading to AIDS are some of the common STIs</b> (F121). "
    "<b>Among these, HIV infection is most dangerous and is discussed in detail in Chapter 7</b> (F122)."))
story.append(body(
    "<b>Some of these infections like hepatitis-B and HIV can also be transmitted by sharing of injection needles, surgical "
    "instruments, etc., with infected persons, transfusion of blood, or from an infected mother to the foetus too</b> (F123)."))
story.append(body(
    "<b>Except for hepatitis-B, genital herpes and HIV infections, other diseases are completely curable if detected early "
    "and treated properly</b> (F124)."))
story.append(body(
    "<b>Early symptoms of most of these are minor and include itching, fluid discharge, slight pain, swellings, etc., in the "
    "genital region</b> (F125). <b>Infected females may often be asymptomatic and hence, may remain undetected for long</b> "
    "(F126). <b>Absence or less significant symptoms in the early stages of infection and the social stigma attached to the "
    "STIs, deter the infected persons from going for timely detection and proper treatment</b> (F127)."))
story.append(body(
    "<b>This could lead to complications later, which include pelvic inflammatory diseases (PID), abortions, still births, "
    "ectopic pregnancies, infertility or even cancer of the reproductive tract</b> (F128). <b>STIs are a major threat to a "
    "healthy society</b> (F129). <b>Therefore, prevention or early detection and cure of these diseases are given prime "
    "consideration under the reproductive health-care programmes</b> (F130)."))
story.append(body(
    "<b>Though all persons are vulnerable to these infections, their incidences are reported to be very high among persons "
    "in the age group of 15-24 years - the age group to which you also belong</b> (F131)."))
# F132 folded as clause leading into three principles
story.append(body(
    "There is no reason to panic because prevention is possible (F132, folded) - three simple principles keep one free of "
    "these infections:"))
story.append(process_flow([
    "<b>Avoid sex with unknown partners/multiple partners</b> (F133 i).",
    "<b>Always try to use condoms during coitus</b> (F133 ii).",
    "<b>In case of doubt, go to a qualified doctor for early detection and get complete treatment if diagnosed with infection</b> (F133 iii).",
]))

# ======================================================================================
# ---- 3.5 INFERTILITY ---- F134-F154 (heading F134, opener F135 class-B)
# ======================================================================================
story.append(heading("3.5", "Infertility", 1))
# F135 is class-B opener folded into lead sentence
story.append(body(
    "A discussion on reproductive health is incomplete without a mention of infertility (F135, folded). "
    "<b>A large number of couples all over the world including India are infertile, i.e., they are unable to produce "
    "children inspite of unprotected sexual co-habitation</b> (F136) - the summary adds the diagnostic criterion "
    "<b>even after 2 years of unprotected sexual cohabitation</b>, which is carried here (F136 SUMMARY-UNIQUE fold)."))
story.append(body(
    "<b>The reasons for this could be many - physical, congenital, diseases, drugs, immunological or even psychological</b> "
    "(F137). <b>In India, often the female is blamed for the couple being childless, but more often than not, the problem "
    "lies in the male partner</b> (F138)."))
story.append(body(
    "<b>Specialised health care units (infertility clinics, etc.) could help in diagnosis and corrective treatment of some "
    "of these disorders and enable these couples to have children</b> (F139). <b>However, where such corrections are not "
    "possible, the couples could be assisted to have children through certain special techniques commonly known as assisted "
    "reproductive technologies (ART)</b> (F140)."))
story.append(keyterm(
    "<b>In vitro fertilisation (IVF - fertilisation outside the body in almost similar conditions as that in the body) "
    "followed by embryo transfer (ET) is one of such methods</b> (F141)."))
story.append(body(
    "<b>In this method, popularly known as test tube baby programme, ova from the wife/donor (female) and sperms from the "
    "husband/donor (male) are collected and are induced to form zygote under simulated conditions in the laboratory</b> (F142)."))
story.append(body(
    "<b>The zygote or early embryos (with upto 8 blastomeres) could then be transferred into the fallopian tube "
    "(ZIFT - zygote intra fallopian transfer) and embryos with more than 8 blastomeres, into the uterus (IUT - intra "
    "uterine transfer), to complete its further development</b> (F143). "
    "<b>Embryos formed by in-vivo fertilisation (fusion of gametes within the female) also could be used for such transfer "
    "to assist those females who cannot conceive</b> (F144)."))
story.append(b1(
    "<b>Transfer of an ovum collected from a donor into the fallopian tube (GIFT - gamete intra fallopian transfer) of "
    "another female who cannot produce one, but can provide suitable environment for fertilisation and further development "
    "is another method attempted</b> (F145)."))
story.append(b1(
    "<b>Intra cytoplasmic sperm injection (ICSI) is another specialised procedure to form an embryo in the laboratory in "
    "which a sperm is directly injected into the ovum</b> (F146)."))
story.append(body(
    "<b>Infertility cases either due to inability of the male partner to inseminate the female or due to very low sperm "
    "counts in the ejaculates, could be corrected by artificial insemination (AI) technique</b> (F147). <b>In this "
    "technique, the semen collected either from the husband or a healthy donor is artificially introduced either into the "
    "vagina or into the uterus (IUI - intra-uterine insemination) of the female</b> (F148)."))
story.append(body(
    "<b>Though options are many, all these techniques require extremely high precision handling by specialised professionals "
    "and expensive instrumentation</b> (F149). <b>Therefore, these facilities are presently available only in very few centres "
    "in the country</b> (F150) and <b>obviously their benefits is affordable to only a limited number of people</b> "
    "(F151, folded with F150)."))
story.append(body(
    "<b>Emotional, religious and social factors are also deterrents in the adoption of these methods</b> (F152)."))
story.append(body(
    "<b>Since the ultimate aim of all these procedures is to have children, in India we have so many orphaned and destitute "
    "children, who would probably not survive till maturity, unless taken care of</b> (F153). <b>Our laws permit legal adoption "
    "and it is as yet, one of the best methods for couples looking for parenthood</b> (F154)."))
story.append(note(
    "ART, GIFT and IUI are not interchangeable - <b>IVF-ET/ZIFT/IUT use fertilisation outside the body followed by embryo transfer; "
    "GIFT transfers the unfertilised ovum; ICSI injects one sperm into one ovum; AI/IUI introduces semen into the uterus/vagina</b> - "
    "and the blastomere rule decides ZIFT (upto 8) versus IUT (more than 8)."))

# ======================================================================================
# ---- Quick Recap (§5 item 8; rewritten summary) ---- F155 heading, summary 18 sentences
# ======================================================================================
story.append(heading("QR", "Quick Recap", 1))
story.append(b1(
    "<b>Reproductive health</b> is <b>total well-being in all aspects - physical, emotional, behavioural and social</b> (WHO, F008); "
    "it needs <b>counselling, awareness about organs, adolescence, safe hygiene, STIs including AIDS</b>, plus <b>medical care for "
    "menstrual problems, pregnancy, delivery, MTP, STIs, birth control, infertility and post-natal management</b> (F015/F023); "
    "India was <b>amongst the first / the first nation to launch RCH programmes (1951 family planning)</b> (F012-F014), now judged by "
    "<b>reduced MMR/IMR, more small families, better STD cure, more medical facilities and assistance to infertile couples</b> (F030)."))
story.append(b1(
    "<b>Population explosion:</b> better health and living conditions drove <b>world 2B (1900) to 6B (2000) to 7.2B (2011)</b> (F034) and "
    "<b>India 350M at independence to near 1B by 2000 to over 1.2B in May 2011</b> (F035-F036); reasons <b>fall in death/MMR/IMR and more people in "
    "reproducible age</b> (F037); RCH cut growth only marginally to <b>less than 2% = 20/1000/year (2011)</b> (F038-F039), threatening "
    "<b>food, shelter, clothing scarcity</b> (F040) and prompting <b>smaller-family motivation, Hum Do Hamare Do, one-child norm, marriage age "
    "18F/21M and incentives</b> (F042-F045)."))
story.append(b1(
    "<b>Contraception - seven NCERT groups:</b> an <b>ideal contraceptive is user-friendly, easily available, effective, reversible, with least "
    "side effects and no interference with drive/act</b> (F047-F048); <b>Natural</b> methods avoid ovum-sperm meeting without devices - "
    "<b>periodic abstinence day 10-17 fertile period, withdrawal, lactational amenorrhea (intense lactation, 6 months only, almost nil side effects but high failure)</b> (F050-F059); "
    "<b>Barrier</b> methods physically block meeting - <b>condoms (Nirodh, protects also from STIs/AIDS, disposable, private), diaphragms/caps/vaults (reusable), plus spermicidal creams/jellies/foams</b> (F060-F069); "
    "<b>IUDs</b> inserted by doctors/nurses through vagina - <b>Lippes loop, CuT/Cu7/Multiload 375, Progestasert/LNG-20</b> via <b>phagocytosis, Cu suppression, hormone hostile uterus/cervix; ideal for spacing, most widely accepted</b> (F070-F076); "
    "<b>Pills</b> (progestogen or progestogen-estrogen) <b>21 days within first 5 days + 7-day gap, inhibit ovulation/implantation and alter cervical mucus, well accepted</b> and <b>Saheli weekly non-steroidal</b> (F077-F084); "
    "<b>Injectables/implants</b> under skin, similar mode but <b>much longer action</b> (F085-F086); <b>emergency within 72 hours</b> (F087); "
    "<b>Surgical sterilisation blocks gamete transport, vasectomy (Vas deferens tied and cut) and tubectomy (Fallopian tubes tied and cut), highly effective, poorly reversible</b> (F088-F093); "
    "always choose with a <b>qualified doctor</b> (F094); contraception is <b>against natural conception, used only to prevent/delay/space pregnancy, with possible but not very significant ill-effects (nausea, bleeding, breast cancer ignored at peril)</b> (F095-F099)."))
story.append(b1(
    "<b>MTP:</b> <b>intentional/voluntary termination before full term, induced abortion</b> (F101); <b>45-50 million per year = 1/5th of conceived pregnancies</b> (F102); "
    "debated for <b>emotional/ethical/religious/social reasons</b> (F103); <b>legal in India since 1971 with strict conditions to avoid misuse and illegal female foeticide</b> (F104-F105); "
    "needed for <b>unwanted pregnancies (casual/failed contraception/rape) or harm to mother/foetus</b> (F106-F107); <b>relatively safe upto 12 weeks, riskier in second trimester</b> (F108-F109); "
    "<b>majority illegal by quacks, unsafe/fatal; misuse of amniocentesis for sex determination leading to female foeticide, dangerous for mother and foetus, reversible only by counselling, avoiding unprotected coitus and more health facilities</b> (F110-F114); "
    "<b>Amendment Act 2017</b> aims to cut illegal abortion/mortality (F115); <b>within 12 weeks - one doctor's opinion; 12-24 weeks - two doctors; grounds: risk to life/grave injury to physical/mental health, or substantial risk of serious physical/mental handicap in child</b> (F116-F118)."))
story.append(b1(
    "<b>STIs:</b> <b>infections transmitted by sexual intercourse - STI/VD/RTI</b> (F120): <b>gonorrhoea, syphilis, genital herpes, chlamydiasis, genital warts, trichomoniasis, hepatitis-B, HIV-AIDS (most dangerous, Chapter 7)</b> (F121-F122); "
    "<b>hepatitis-B/HIV also spread by needles, surgical instruments, blood transfusion, mother-to-foetus</b> (F123); <b>all except hepatitis-B, genital herpes and HIV are completely curable if early and properly treated</b> (F124); "
    "<b>minor early symptoms - itching, discharge, pain, swelling; females often asymptomatic</b> (F125-F126); <b>absent/less symptoms plus stigma deter timely treatment</b> (F127) leading to <b>PID, abortions, still births, ectopic pregnancies, infertility, reproductive tract cancer</b> (F128); "
    "<b>major threat, prevention/early cure is prime under RCH</b> (F129-F130); <b>highest incidence 15-24 years (your age)</b> (F131); "
    "prevention is possible - <b>avoid unknown/multiple partners, use condoms, see a qualified doctor if in doubt and complete treatment</b> (F132-F133)."))
story.append(b1(
    "<b>Infertility:</b> <b>inability to produce children inspite of unprotected co-habitation even after 2 years (summary criterion)</b> (F136); <b>many causes - physical, congenital, diseases, drugs, immunological, psychological</b> (F137); "
    "<b>female often blamed but more often male partner is responsible</b> (F138); <b>infertility clinics help diagnosis/corrective treatment, but where not possible, assisted reproductive technologies (ART) assist</b> (F139-F140); "
    "<b>IVF-ET (test tube baby): ova and sperms collected, zygote formed in lab under simulated conditions; ZIFT (upto 8 blastomeres) to fallopian tube, IUT (more than 8) to uterus; in-vivo fertilised embryos also usable</b> (F141-F144); "
    "<b>GIFT transfers donor ovum to another female's fallopian tube who provides environment</b> (F145); <b>ICSI injects one sperm directly into ovum</b> (F146); "
    "<b>AI corrects inability to inseminate or very low sperm counts - semen (husband or donor) artificially introduced into vagina or uterus (IUI)</b> (F147-F148); "
    "<b>all require high precision, expensive instrumentation, available in very few centres, affordable to limited people, deterred by emotional/religious/social factors</b> (F149-F152); "
    "<b>India has many orphaned/destitute children unlikely to survive without care - legal adoption is as yet one of the best methods for parenthood</b> (F153-F154)."))

# ======================================================================================
# ---- Terms used in the exercises (§5 item 9; GAP questions only) ---- F156 heading
# ======================================================================================
story.append(heading("EX", "Terms Used in the Exercises", 1))
story.append(body(
    "Only three exercise parts rely on ideas the chapter never states. Each is answered below using only chapter-based reasoning; "
    "every other exercise (Q1-Q6, Q8-Q10, Q11b-d, Q12a-b,d) is answered by the body text above."))
story.append(b1(
    "<b>Q7 - Why removal of gonads cannot be a contraceptive option.</b> The chapter's surgical methods are <b>sterilisation by "
    "blocking gamete transport - Vas deferens tied and cut (vasectomy) and Fallopian tubes tied and cut (tubectomy)</b> (F089-F092); "
    "they <b>do not remove the gonads (testes/ovaries)</b>, and <b>reversibility is already very poor</b> (F093). "
    "Removing the testes or ovaries would <b>remove the source of gametes and of androgens/estrogens</b> (the hormones that maintain "
    "secondary sexual characters and reproductive function) - a permanent, non-contraceptive castration that the chapter never lists "
    "among its seven contraceptive categories (F049) and that violates the <b>ideal contraceptive criterion of reversibility and no "
    "interference with normal physiology</b> (F047). Hence gonad removal is not a contraceptive option."))
story.append(b1(
    "<b>Q11(a) - True: abortions can occur spontaneously.</b> The chapter defines only <b>intentional/voluntary termination (MTP/induced "
    "abortion)</b> (F101), but <b>spontaneous abortion (miscarriage) is a different fact</b> - the chapter itself lists <b>abortion as a complication "
    "of STIs/PID</b> (F128) that occurs without any MTP procedure, which shows that pregnancy loss can happen on its own."))
story.append(b1(
    "<b>Q12(c) - False to correct: Oral pills are not particularly popular among rural women.</b> The chapter states only that "
    "<b>pills are very effective with lesser side effects and are well accepted by the females</b> (F082) and that <b>Saheli is a once-a-week pill</b> (F084), "
    "but <b>never distinguishes rural from urban users</b>. In fact, <b>IUDs are described as one of the most widely accepted methods in India</b> (F076), "
    "often promoted for spacing in the public programme, so singling out pills as rural-popular is not supported by the text."))

story.append(Spacer(1, 6))
story.append(Paragraph(
    "<i>Every fact, number, name, qualifier, table row, figure and figure label in NCERT Class 12 "
    "Chapter 3 is carried above. Nothing outside the source chapter has been added, except the "
    "clearly marked NOTE/MEMORY AID material and the exercise-gap explanations, which are derived "
    "only from chapter content.</i>", STYLES["Caption"]))


def main():
    return build_pdf(
        OUT_PDF, story,
        title="Class 12 Chapter 3 - Reproductive Health (NEET notes)",
        subject="NEET Biology",
    )


if __name__ == "__main__":
    import sys
    sys.exit(main())

# ---- Filler filtered in this Pass (Rule 3 active) ----
# Class-C (zero fact beyond neighbours) - NOT printed as standalone sentences, accounted for by Rule 3:
#   F005 "Now, let's discuss a closely related topic - reproductive health." - covered by F004+F008 intro.
#   F010 "What do we understand by this term? Why is it significant... Let us examine them." - rhetorical framing, tutor sentence carries it once.
#   F046 "Let us describe some of the commonly used contraceptive methods..." - transitional, F042 already motivates the description.
#   F053 "Therefore, by abstaining from coitus during this period, conception could be prevented." - pure restatement of F051+F052 fertile-period logic, already in table.
#   F063 "This can prevent conception." - one-line restatement of condom mechanism already in F062, already in table cell.
# Class-B (fold, never standalone) - fact still appears, merged into neighbour sentence/table:
#   F035 "A similar trend was observed in India too." -> merged into India population sentence with F036.
#   F041 "Therefore, the government was forced to take up serious measures..." -> merged as lead-in to F042's "most important step".
#   F070 "Another effective and popular method is the use of IUDs." -> transitional heading folded into IUD table row and paragraph.
#   F113 "Such practices should be avoided because these are dangerous..." -> folded as clause onto end of F112 sentence.
#   F132 "There is no reason to panic because prevention is possible." -> folded as opening clause before three STI principles (F133).
#   F135 "A discussion on reproductive health is incomplete without a mention of infertility." -> folded into 3.5 opening sentence.
#   F151 "Obviously their benefits is affordable to only a limited number of people." -> folded with F150's "very few centres".
#   F157-F160 "No in-figure text labels - unlabelled ..." -> figure-metadata, not printed as text; the asset plus its caption carries the fact that the figure exists and has no labels (verified by opening).
# Total filtered as standalone sentences: 5 (class-C) + 7 (class-B textual) + 4 (figure-metadata) = 16 flagged rows; 146 class-A rows printed normally. No fact was dropped - each flagged row's wording is still carried inside the neighbour noted above.

