"""
NCERT Class 12 Biology, Chapter 2 - Human Reproduction
NEET replacement notes -> A4 print-ready PDF.

Built under SUPREME COMMAND PROMPT.md v6, Pass 2: written linearly from the
frozen 220-row inventory (Ch2_HumanReproduction_inventory.md), importing the
repo-level frozen style module `neet_template.py` (v6 §0.6). No style,
geometry, colour or font is re-declared here.

Block markers `# ---- N.N ----` mark every NCERT section so a Pass 3 flag can
be found and fixed in one contiguous block. Inventory row IDs are named in the
comments so any fact can be traced back to its frozen row.

Figures: all 14 assets (12 numbered figures; 2.1 and 2.3 split into (a)/(b))
are embedded inline at their topic via neet_template.figure(). Every in-figure
label from the frozen figure-label matrix (F207-F220) is carried in the running
text and/or the figure caption so the text stands alone and check_pdf.py check 6
is satisfied per label.

Source: Chapter/class 12/Chapter 2 - Human Reproduction.pdf
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
    STYLES, FRAME_WIDTH, DARK_GREY, GRID_LINE,
    heading, keyterm, process_flow, note, memory_aid, data_table, title_block, build_pdf,
)
from neet_template import figure as _shared_figure  # noqa: E402
from reportlab.platypus import Paragraph, Spacer  # noqa: E402

ASSETS = os.path.join(HERE, "assets")
OUT_PDF = os.path.join(HERE, "Ch2_HumanReproduction.pdf")


def figure(asset_name, caption_text, max_width_cm=15.9):
    """Chapter-local binding of the shared figure() helper (§0.6)."""
    return _shared_figure(asset_name, caption_text, ASSETS, max_width_cm=max_width_cm)


def body(text):
    return Paragraph(text, STYLES["Body"])


def b1(text):
    return Paragraph("&bull; " + text, STYLES["Bullet1"])


def b2(text):
    return Paragraph("- " + text, STYLES["Bullet2"])


story = []

# ======================================================================================
# ---- Title block (§5 item 1) ---- F001
# ======================================================================================
story += title_block("Human Reproduction")

# ======================================================================================
# ---- 2.intro (chapter opener) ---- F002-F008 (opener F002)
# ======================================================================================
story.append(heading("2.0", "Reproductive Events in Humans", 1))
story.append(body(
    "As you are aware, <b>humans are sexually reproducing and viviparous</b>. Human reproduction "
    "runs through a fixed series of events, each with its own name."))
story.append(process_flow([
    "<b>Gametogenesis</b> - the formation of gametes: <b>sperms</b> in males and <b>ovum</b> in "
    "females.",
    "<b>Insemination</b> - the <b>transfer of sperms into the female genital tract</b>.",
    "<b>Fertilisation</b> - the <b>fusion of male and female gametes</b>, leading to formation of "
    "the <b>zygote</b>.",
    "Formation and development of the <b>blastocyst</b> and its <b>attachment to the uterine "
    "wall (implantation)</b>.",
    "<b>Gestation</b> - the embryonic development inside the uterus.",
    "<b>Parturition</b> - the delivery of the baby.",
]))
story.append(body(
    "All these reproductive events <b>occur only after puberty</b>. There is an important "
    "difference between the sexes in how long gamete formation lasts: <b>sperm formation "
    "continues even in old men</b>, <b>but formation of ovum ceases in women around the age of "
    "fifty years</b>."))

# ======================================================================================
# ---- 2.1 THE MALE REPRODUCTIVE SYSTEM ---- F009-F036 (heading F009, opener F010)
# ======================================================================================
# [VERIFICATION FIX] table icon removed: §2.1 contains no data_table (the stray
# open-square badge that appeared at the banner's right margin on page 1). The icon
# now sits only on the table-bearing sections 2.2 and 2.6.
story.append(heading("2.1", "The Male Reproductive System", 1))
story.append(body(
    "The <b>male reproductive system is located in the pelvis region</b>. It includes a "
    "<b>pair of testes</b> along with <b>accessory ducts</b>, <b>glands</b> and the "
    "<b>external genitalia</b>."))

story.append(heading("2.1a", "The Testes", 2))
story.append(body(
    "The <b>testes are situated outside the abdominal cavity</b> within a pouch called the "
    "<b>scrotum</b>. The scrotum <b>maintains the low temperature of the testes</b> - "
    "<b>2-2.5&#176;C lower than the normal internal body temperature</b> - which is "
    "<b>necessary for spermatogenesis</b>."))
story.append(body(
    "In adults, <b>each testis is oval</b>, with a <b>length of about 4 to 5 cm</b> and a "
    "<b>width of about 2 to 3 cm</b>. The testis is <b>covered by a dense covering</b>. Each "
    "testis has <b>about 250 compartments called testicular lobules</b>, and <b>each lobule "
    "contains one to three highly coiled seminiferous tubules</b> in which sperms are produced."))
story.append(body(
    "Each <b>seminiferous tubule</b> is lined on its inside by <b>two types of cells</b>: the "
    "<b>male germ cells (spermatogonia)</b> and the <b>Sertoli cells</b>. The <b>male germ cells "
    "undergo meiotic divisions</b>, finally leading to <b>sperm formation</b>, while the "
    "<b>Sertoli cells provide nutrition to the germ cells</b>."))
story.append(body(
    "The regions <b>outside the seminiferous tubules</b>, called <b>interstitial spaces</b>, "
    "contain <b>small blood vessels</b> and <b>interstitial cells</b>, also called <b>Leydig "
    "cells</b>. The <b>Leydig cells synthesise and secrete testicular hormones called "
    "androgens</b>. Other <b>immunologically competent cells are also present</b>."))
story.append(figure(
    "fig_2_2.png",
    "Fig. 2.2 - Diagrammatic sectional view of a seminiferous tubule. Labelled parts: "
    "interstitial cells, spermatogonia, spermatozoa and Sertoli cells."))

story.append(heading("2.1b", "Accessory Ducts, Penis and Glands", 2))
story.append(body(
    "The <b>male sex accessory ducts</b> include the <b>rete testis</b>, <b>vasa efferentia</b>, "
    "<b>epididymis</b> and <b>vas deferens</b>. Their connected path carries the sperms outward:"))
story.append(process_flow([
    "The <b>seminiferous tubules</b> of the testis open into the <b>vasa efferentia</b> through "
    "the <b>rete testis</b>.",
    "The <b>vasa efferentia leave the testis</b> and open into the <b>epididymis</b>, located "
    "<b>along the posterior surface of each testis</b>.",
    "The <b>epididymis leads to the vas deferens</b>, which <b>ascends to the abdomen and loops "
    "over the urinary bladder</b>.",
    "The vas deferens <b>receives a duct from the seminal vesicle</b> and opens into the "
    "<b>urethra</b> as the <b>ejaculatory duct</b>.",
    "The <b>urethra originates from the urinary bladder</b> and <b>extends through the penis</b> "
    "to its external opening called the <b>urethral meatus</b>.",
]))
story.append(body(
    "Together, <b>these ducts store and transport the sperms</b> from the testis to the outside "
    "through the urethra."))
story.append(body(
    "The <b>penis is the male external genitalia</b>. It is made up of a <b>special tissue that "
    "helps in erection of the penis to facilitate insemination</b>. The <b>enlarged end of the "
    "penis, called the glans penis, is covered by a loose fold of skin called the foreskin</b>."))
story.append(body(
    "The <b>male accessory glands</b> include the <b>paired seminal vesicles</b>, a <b>prostate</b> "
    "and the <b>paired bulbourethral glands</b>. The <b>secretions of these glands constitute the "
    "seminal plasma</b>, which is <b>rich in fructose, calcium and certain enzymes</b>. The "
    "<b>secretions of the bulbourethral glands also help in the lubrication of the penis</b>."))
story.append(figure(
    "fig_2_1a.png",
    "Fig. 2.1a - Diagrammatic sectional view of the male pelvis showing the reproductive system. "
    "Labelled parts: ureter, urinary bladder, seminal vesicle, ejaculatory duct, prostate, "
    "bulbourethral gland, vas deferens, urethra, penis, glans penis, foreskin, testis, scrotum, "
    "rectum and anus.", max_width_cm=11.5))
story.append(figure(
    "fig_2_1b.png",
    "Fig. 2.1b - Diagrammatic view of the male reproductive system (part of the testis is opened "
    "to show inner details). Labelled parts: ureter, urinary bladder, seminal vesicle, prostate, "
    "bulbourethral gland, vas deferens, epididymis, vasa efferentia, rete testis, testicular "
    "lobules, urethra, glans penis, foreskin and testis.", max_width_cm=11.5))

# ======================================================================================
# ---- 2.2 THE FEMALE REPRODUCTIVE SYSTEM ---- F037-F077 (heading F037, opener F038)
# ======================================================================================
# [VERIFICATION FIX] has_table=True: §2.2 carries a data_table (mammary-gland structure).
story.append(heading("2.2", "The Female Reproductive System", 1, has_table=True))
story.append(body(
    "The <b>female reproductive system</b> consists of a <b>pair of ovaries</b> along with a "
    "<b>pair of oviducts</b>, a <b>uterus</b>, a <b>cervix</b>, a <b>vagina</b> and the "
    "<b>external genitalia</b>, located in the <b>pelvic region</b>. These parts, along with a "
    "<b>pair of mammary glands</b>, are <b>integrated structurally and functionally to support "
    "ovulation, fertilisation, pregnancy, birth and child care</b>."))

story.append(heading("2.2a", "The Ovaries", 2))
story.append(body(
    "The <b>ovaries are the primary female sex organs</b> that <b>produce the female gamete "
    "(ovum)</b> and <b>several steroid hormones (ovarian hormones)</b>. They are <b>located one "
    "on each side of the lower abdomen</b>. <b>Each ovary is about 2 to 4 cm in length</b> and is "
    "<b>connected to the pelvic wall and uterus by ligaments</b>."))
story.append(body(
    "Each ovary is <b>covered by a thin epithelium</b> which <b>encloses the ovarian stroma</b>. "
    "The <b>stroma is divided into two zones</b> - a <b>peripheral cortex</b> and an <b>inner "
    "medulla</b>. <b>Ovarian follicles in different stages of development are embedded in the "
    "stroma</b>."))

story.append(heading("2.2b", "The Accessory Ducts - Oviducts, Uterus, Cervix, Vagina", 2))
story.append(body(
    "The <b>oviducts (fallopian tubes)</b>, <b>uterus</b> and <b>vagina</b> constitute the "
    "<b>female accessory ducts</b>. <b>Each fallopian tube is about 10-12 cm long</b> and "
    "<b>extends from the periphery of each ovary to the uterus</b>. Its parts, from the ovary "
    "towards the uterus, are:"))
story.append(process_flow([
    "<b>Infundibulum</b> - the <b>funnel-shaped part closer to the ovary</b>. Its edges have "
    "<b>finger-like projections called fimbriae</b>, which <b>help in the collection of the ovum "
    "after ovulation</b>.",
    "<b>Ampulla</b> - the <b>wider part of the oviduct</b> that the infundibulum leads into.",
    "<b>Isthmus</b> - the <b>last part of the oviduct</b>, which has a <b>narrow lumen</b> and "
    "<b>joins the uterus</b>.",
]))
story.append(body(
    "The <b>uterus is single</b> and is also called the <b>womb</b>. Its <b>shape is like an "
    "inverted pear</b>, and it is <b>supported by ligaments attached to the pelvic wall</b>. The "
    "<b>uterus opens into the vagina through a narrow cervix</b>. The <b>cavity of the cervix is "
    "called the cervical canal</b>, which <b>along with the vagina forms the birth canal</b>."))
story.append(body(
    "The <b>wall of the uterus has three layers of tissue</b>:"))
story.append(data_table([
    ["Layer", "Position", "Nature / feature"],
    ["<b>Perimetrium</b>", "External", "Thin membranous layer"],
    ["<b>Myometrium</b>", "Middle", "Thick layer of smooth muscle; <b>exhibits strong contraction "
     "during delivery of the baby</b>"],
    ["<b>Endometrium</b>", "Inner", "Glandular layer that <b>lines the uterine cavity</b> and "
     "<b>undergoes cyclical changes during the menstrual cycle</b>"],
], col_widths=[2.2, 1.8, 6.6]))
story.append(figure(
    "fig_2_3a.png",
    "Fig. 2.3a - Diagrammatic sectional view of the female pelvis showing the reproductive system. "
    "Labelled parts: uterus, urinary bladder, pubic symphysis, urethra, clitoris, labium minora, "
    "labium majora, vaginal orifice, cervix, rectum, vagina and anus.", max_width_cm=11.0))
story.append(figure(
    "fig_2_3b.png",
    "Fig. 2.3b - Diagrammatic sectional view of the female reproductive system. Labelled parts: "
    "uterine fundus, uterine cavity, endometrium, myometrium, perimetrium, isthmus, ampulla, "
    "infundibulum, fallopian tube, ovary, fimbriae, cervix, cervical canal and vagina.",
    max_width_cm=12.5))

story.append(heading("2.2c", "The External Genitalia", 2))
story.append(body(
    "The <b>female external genitalia</b> include the <b>mons pubis</b>, <b>labia majora</b>, "
    "<b>labia minora</b>, <b>hymen</b> and <b>clitoris</b>."))
story.append(b1(
    "<b>Mons pubis</b> - a <b>cushion of fatty tissue covered by skin and pubic hair</b>."))
story.append(b1(
    "<b>Labia majora</b> - <b>fleshy folds of tissue</b> which <b>extend down from the mons pubis "
    "and surround the vaginal opening</b>."))
story.append(b1(
    "<b>Labia minora</b> - <b>paired folds of tissue under the labia majora</b>."))
story.append(b1(
    "<b>Hymen</b> - a membrane that <b>often partially covers the opening of the vagina</b>."))
story.append(b1(
    "<b>Clitoris</b> - a <b>tiny finger-like structure</b> which <b>lies at the upper junction of "
    "the two labia minora above the urethral opening</b>."))
story.append(note(
    "The <b>hymen is often torn during the first coitus (intercourse)</b>. It can <b>also be "
    "broken</b> by a <b>sudden fall or jolt</b>, insertion of a <b>vaginal tampon</b>, or "
    "<b>active participation in some sports like horseback riding, cycling, etc.</b> In some women "
    "the <b>hymen persists even after coitus</b>. Therefore the <b>presence or absence of the "
    "hymen is not a reliable indicator of virginity or sexual experience</b>."))

story.append(heading("2.2d", "The Mammary Glands", 3))
story.append(body(
    "A <b>functional mammary gland is characteristic of all female mammals</b>, and the <b>mammary "
    "glands are one of the female secondary sexual characteristics</b>. The <b>mammary glands are "
    "paired structures (breasts)</b> that <b>contain glandular tissue and a variable amount of "
    "fat</b>. Milk drains from the gland along a fixed path:"))
story.append(process_flow([
    "The <b>glandular tissue of each breast is divided into 15-20 mammary lobes</b> containing "
    "<b>clusters of cells called alveoli</b>.",
    "The <b>cells of the alveoli secrete milk</b>, which is <b>stored in the cavities (lumens) of "
    "the alveoli</b>.",
    "The <b>alveoli open into mammary tubules</b>.",
    "The <b>tubules of each lobe join to form a mammary duct</b>.",
    "Several <b>mammary ducts join to form a wider mammary ampulla</b>, which is <b>connected to a "
    "lactiferous duct</b> and <b>opens at the nipple</b>, from where <b>milk is expressed during "
    "breastfeeding</b>.",
]))
story.append(figure(
    "fig_2_4.png",
    "Fig. 2.4 - A diagrammatic sectional view of a mammary gland. Labelled parts: mammary lobe, "
    "mammary alveolus, mammary duct, ampulla, lactiferous duct, nipple, areola, fat, rib, muscles "
    "between ribs and pectoralis major muscle.", max_width_cm=10.5))

# ======================================================================================
# ---- 2.3 GAMETOGENESIS ---- F078-F120 (heading F078, opener F079)
# ======================================================================================
story.append(heading("2.3", "Gametogenesis", 1))
story.append(body(
    "The <b>primary sex organs</b> - the <b>testis in males</b> and the <b>ovaries in females</b> "
    "- <b>produce gametes</b>, i.e. <b>sperms and ovum respectively</b>, by the process called "
    "<b>gametogenesis</b>."))

story.append(heading("2.3a", "Spermatogenesis", 2))
story.append(body(
    "In the testis, <b>immature male germ cells (spermatogonia) produce sperms by "
    "spermatogenesis</b>, a process that <b>begins at puberty</b>. The steps are:"))
story.append(process_flow([
    "<b>Spermatogonia</b> (sing. spermatogonium) on the inside wall of the seminiferous tubules "
    "<b>multiply by mitotic division and increase in number</b>. Each <b>spermatogonium is "
    "diploid and contains 46 chromosomes</b>.",
    "Some spermatogonia, called <b>primary spermatocytes</b>, <b>periodically undergo meiosis</b>.",
    "A <b>primary spermatocyte completes the first meiotic division (reduction division)</b>, "
    "producing <b>two equal, haploid secondary spermatocytes</b>, each with <b>only 23 "
    "chromosomes</b>.",
    "The <b>secondary spermatocytes undergo the second meiotic division</b> to produce <b>four "
    "equal, haploid spermatids</b>.",
    "The <b>spermatids are transformed into spermatozoa (sperms)</b> by the process called "
    "<b>spermiogenesis</b>.",
    "After spermiogenesis, the <b>sperm heads become embedded in the Sertoli cells</b> and are "
    "<b>finally released from the seminiferous tubules</b> by the process called "
    "<b>spermiation</b>.",
]))
story.append(figure(
    "fig_2_5.png",
    "Fig. 2.5 - Diagrammatic sectional view of a seminiferous tubule (enlarged). Labelled cells: "
    "spermatogonium, primary spermatocyte, secondary spermatocyte, spermatid, spermatozoa and "
    "Sertoli cell.", max_width_cm=9.5))

story.append(heading("2.3b", "Hormonal Control of Spermatogenesis", 3))
story.append(body(
    "Spermatogenesis <b>starts at puberty</b> due to a <b>significant increase in the secretion "
    "of gonadotropin releasing hormone (GnRH)</b>, which is a <b>hypothalamic hormone</b>."))
story.append(process_flow([
    "<b>Increased GnRH acts at the anterior pituitary gland</b> and <b>stimulates secretion of "
    "two gonadotropins</b> - <b>luteinising hormone (LH)</b> and <b>follicle stimulating hormone "
    "(FSH)</b>.",
    "<b>LH acts at the Leydig cells</b> and <b>stimulates synthesis and secretion of "
    "androgens</b>. The <b>androgens, in turn, stimulate the process of spermatogenesis</b>.",
    "<b>FSH acts on the Sertoli cells</b> and <b>stimulates secretion of some factors which help "
    "in the process of spermiogenesis</b>.",
]))

story.append(heading("2.3c", "Structure of the Sperm", 3))
story.append(body(
    "A <b>sperm is a microscopic structure</b> composed of a <b>head</b>, a <b>neck</b>, a "
    "<b>middle piece</b> and a <b>tail</b>. A <b>plasma membrane envelops the whole body of the "
    "sperm</b>."))
story.append(b1(
    "<b>Head:</b> contains an <b>elongated haploid nucleus</b>, the <b>anterior portion of which "
    "is covered by a cap-like structure, the acrosome</b>. The <b>acrosome is filled with enzymes "
    "that help fertilisation of the ovum</b>."))
story.append(b1(
    "<b>Middle piece:</b> possesses <b>numerous mitochondria</b>, which <b>produce energy for the "
    "movement of the tail</b> that <b>facilitates sperm motility essential for fertilisation</b>."))
story.append(figure(
    "fig_2_6.png",
    "Fig. 2.6 - Structure of a sperm. Labelled parts: plasma membrane, acrosome, nucleus, head, "
    "neck, middle piece, mitochondria and tail.", max_width_cm=7.0))
story.append(body(
    "The <b>human male ejaculates about 200 to 300 million sperms during a coitus</b>. For "
    "<b>normal fertility</b>, <b>at least 60 per cent of sperms must have normal shape and "
    "size</b> and <b>at least 40 per cent must show vigorous motility</b>."))
story.append(body(
    "Sperms <b>released from the seminiferous tubules are transported by the accessory ducts</b>. "
    "The <b>secretions of the epididymis, vas deferens, seminal vesicle and prostate are "
    "essential for the maturation and motility of sperms</b>. The <b>seminal plasma along with "
    "the sperms constitutes the semen</b>. The <b>functions of the male sex accessory ducts and "
    "glands are maintained by the testicular hormones (androgens)</b>."))

story.append(heading("2.3d", "Oogenesis", 2))
story.append(body(
    "<b>Oogenesis</b> - the <b>formation of a mature female gamete</b> - is <b>markedly different "
    "from spermatogenesis</b>. It is <b>initiated during the embryonic development stage</b>, when "
    "a <b>couple of million gamete mother cells (oogonia) are formed within each fetal ovary</b>. "
    "<b>No more oogonia are formed and added after birth</b>."))
story.append(process_flow([
    "<b>Oogonia start division and enter prophase-I of the meiotic division</b>, then get "
    "<b>temporarily arrested at that stage</b>; they are now called <b>primary oocytes</b>.",
    "Each <b>primary oocyte gets surrounded by a layer of granulosa cells</b> and is called a "
    "<b>primary follicle</b>. A <b>large number of these follicles degenerate during the phase "
    "from birth to puberty</b>, so that <b>at puberty only 60,000-80,000 primary follicles are "
    "left in each ovary</b>.",
    "The <b>primary follicles get surrounded by more layers of granulosa cells and a new "
    "theca</b> and are called <b>secondary follicles</b>.",
    "A secondary follicle <b>transforms into a tertiary follicle</b>, characterised by a "
    "<b>fluid-filled cavity called the antrum</b>. The <b>theca layer is organised into an inner "
    "theca interna and an outer theca externa</b>.",
    "At the <b>tertiary-follicle stage the primary oocyte grows in size and completes its first "
    "meiotic division</b>. This is an <b>unequal division</b>, resulting in a <b>large haploid "
    "secondary oocyte and a tiny first polar body</b>; the <b>secondary oocyte retains the bulk "
    "of the nutrient-rich cytoplasm of the primary oocyte</b>.",
    "The <b>tertiary follicle further changes into the mature follicle or Graafian follicle</b>. "
    "The <b>secondary oocyte forms a new membrane called the zona pellucida</b> surrounding it.",
    "The <b>Graafian follicle ruptures to release the secondary oocyte (ovum) from the ovary</b> "
    "by the process called <b>ovulation</b>.",
]))
story.append(figure(
    "fig_2_7.png",
    "Fig. 2.7 - Diagrammatic sectional view of an ovary. Labelled parts: blood vessels, primary "
    "follicle, tertiary follicle, antrum, Graafian follicle, secondary oocyte and corpus luteum.",
    max_width_cm=11.0))
story.append(figure(
    "fig_2_8.png",
    "Fig. 2.8 - Schematic representation of (a) spermatogenesis and (b) oogenesis. Labelled: "
    "spermatogonia, mitosis, primary spermatocytes, secondary spermatocytes, spermatids and "
    "spermatozoa, with the chromosome number per cell shown as 46 and 23; and oogonia, primary "
    "oocyte, secondary oocyte, first polar body, second polar body and ovum.", max_width_cm=13.0))

# ======================================================================================
# ---- 2.4 MENSTRUAL CYCLE ---- F121-F145 (heading F121, opener F122)
# ======================================================================================
story.append(heading("2.4", "Menstrual Cycle", 1))
story.append(body(
    "The <b>reproductive cycle in the female primates</b> (e.g. <b>monkeys, apes and human "
    "beings</b>) is called the <b>menstrual cycle</b>. The <b>first menstruation begins at "
    "puberty</b> and is called <b>menarche</b>."))
story.append(body(
    "In human females, <b>menstruation is repeated at an average interval of about 28/29 "
    "days</b>. The <b>cycle of events starting from one menstruation till the next is called the "
    "menstrual cycle</b>, and <b>one ovum is released (ovulation) during the middle of each "
    "menstrual cycle</b>."))
story.append(body("The cycle proceeds through the following phases:"))
story.append(process_flow([
    "<b>Menstrual phase:</b> the cycle <b>starts with the menstrual phase</b>, when <b>menstrual "
    "flow occurs</b>; it <b>lasts for 3-5 days</b>. The <b>menstrual flow results due to "
    "breakdown of the endometrial lining of the uterus and its blood vessels</b>, which forms a "
    "<b>liquid that comes out through the vagina</b>.",
    "<b>Follicular phase:</b> the <b>primary follicles grow to become a fully mature Graafian "
    "follicle</b> and, <b>simultaneously, the endometrium regenerates through proliferation</b>.",
    "<b>Ovulatory phase:</b> the <b>LH surge induces rupture of the Graafian follicle and "
    "release of the ovum (ovulation)</b>.",
    "<b>Luteal phase:</b> the <b>remaining parts of the Graafian follicle transform into the "
    "corpus luteum</b>, which <b>secretes large amounts of progesterone</b>.",
]))
story.append(note(
    "<b>Menstruation only occurs if the released ovum is not fertilised.</b> A <b>lack of "
    "menstruation may be indicative of pregnancy</b>; it <b>may also be caused due to some other "
    "underlying causes like stress, poor health, etc.</b>"))
story.append(body(
    "These <b>changes in the ovary and the uterus are induced by changes in the levels of "
    "pituitary and ovarian hormones</b>. The <b>secretion of gonadotropins (LH and FSH) increases "
    "gradually during the follicular phase</b> and <b>stimulates follicular development as well "
    "as the secretion of estrogens by the growing follicles</b>. <b>Both LH and FSH attain a peak "
    "level in the middle of the cycle (about the 14th day)</b>. The <b>rapid secretion of LH "
    "leading to its maximum level during mid-cycle, called the LH surge, induces rupture of the "
    "Graafian follicle and release of the ovum (ovulation)</b>."))
story.append(body(
    "The <b>progesterone secreted by the corpus luteum is essential for maintenance of the "
    "endometrium</b>. Such an <b>endometrium is necessary for implantation of the fertilised ovum "
    "and other events of pregnancy</b>. <b>During pregnancy all events of the menstrual cycle stop "
    "and there is no menstruation</b>. <b>In the absence of fertilisation, the corpus luteum "
    "degenerates</b>, <b>causing disintegration of the endometrium leading to menstruation</b>, "
    "which marks a <b>new cycle</b>."))
story.append(body(
    "In human beings, <b>menstrual cycles cease around 50 years of age</b>; that is termed "
    "<b>menopause</b>. <b>Cyclic menstruation is an indicator of a normal reproductive phase</b> "
    "and <b>extends between menarche and menopause</b>."))
story.append(figure(
    "fig_2_9.png",
    "Fig. 2.9 - Diagrammatic presentation of the various events during a menstrual cycle. "
    "Labelled: FSH, LH, developing follicle, mature follicle, corpus luteum, ovulation, estrogen, "
    "progesterone, menses, the follicular phase and the luteal phase.", max_width_cm=13.0))
# ---- Menstrual Hygiene (boxed margin note) ---- F144 (heading), F145
story.append(note(
    "<b>Menstrual Hygiene.</b> Maintenance of hygiene and sanitation during menstruation is very "
    "important. Take a bath and clean regularly; use <b>sanitary napkins</b> or <b>clean "
    "homemade pads</b>; change them <b>after every 4-5 hrs</b> as per requirement; dispose of "
    "used napkins by wrapping them in used paper; <b>do not throw used napkins in the drainpipe of "
    "toilets or in the open area</b>; and after handling the napkin, <b>wash hands with soap</b>."))

# ======================================================================================
# ---- 2.5 FERTILISATION AND IMPLANTATION ---- F146-F169 (heading F146, opener F147)
# ======================================================================================
story.append(heading("2.5", "Fertilisation and Implantation", 1))
story.append(body(
    "During <b>copulation (coitus)</b>, <b>semen is released by the penis into the vagina "
    "(insemination)</b>. The <b>motile sperms swim rapidly, pass through the cervix, enter the "
    "uterus and finally reach the ampullary region of the fallopian tube</b>. The <b>ovum "
    "released by the ovary is also transported to the ampullary region, where fertilisation takes "
    "place</b>."))
story.append(note(
    "<b>Fertilisation can only occur if the ovum and sperms are transported simultaneously to the "
    "ampullary region.</b> This is <b>why not all copulations lead to fertilisation and "
    "pregnancy</b>."))

story.append(heading("2.5a", "Fertilisation", 2))
story.append(body(
    "The <b>process of fusion of a sperm with an ovum is called fertilisation</b>. During "
    "fertilisation, a <b>sperm comes in contact with the zona pellucida layer of the ovum</b> and "
    "<b>induces changes in the membrane that block the entry of additional sperms</b>. This "
    "<b>ensures that only one sperm can fertilise an ovum</b>. The <b>secretions of the acrosome "
    "help the sperm enter the cytoplasm of the ovum through the zona pellucida and the plasma "
    "membrane</b>."))
story.append(body(
    "This entry <b>induces completion of the meiotic division of the secondary oocyte</b>. The "
    "<b>second meiotic division is also unequal</b> and <b>results in a second polar body and a "
    "haploid ovum (ootid)</b>. The <b>haploid nucleus of the sperm and that of the ovum fuse "
    "together to form a diploid zygote</b>."))
story.append(figure(
    "fig_2_10.png",
    "Fig. 2.10 - Ovum surrounded by a few sperms. Labelled parts: sperm, zona pellucida, corona "
    "radiata, perivitelline space and ovum.", max_width_cm=8.0))

story.append(heading("2.5b", "Sex Determination", 3))
story.append(body(
    "The <b>sex of the baby is decided at the fertilisation stage</b>. The <b>chromosome pattern "
    "in the human female is XX and in the male is XY</b>. <b>All haploid gametes (ova) produced by "
    "the female have the sex chromosome X</b>, whereas in <b>male gametes (sperms) the sex "
    "chromosome could be either X or Y</b> - <b>50 per cent of sperms carry X and the other 50 "
    "per cent carry Y</b>."))
story.append(body(
    "Thus the <b>zygote carries either XX or XY depending on whether the X- or Y-bearing sperm "
    "fertilised the ovum</b>: <b>XX develops into a female baby and XY into a male</b> (more on "
    "chromosomal patterns in Chapter 5). Therefore, <b>scientifically it is correct to say that "
    "the sex of the baby is determined by the father and not by the mother</b>."))

story.append(heading("2.5c", "Cleavage and Implantation", 2))
story.append(process_flow([
    "<b>Mitotic division called cleavage starts as the zygote moves through the isthmus of the "
    "oviduct towards the uterus</b> and <b>forms 2, 4, 8, 16 daughter cells called "
    "blastomeres</b>.",
    "The <b>embryo with 8 to 16 blastomeres is called a morula</b>.",
    "The <b>morula continues to divide and transforms into a blastocyst as it moves further into "
    "the uterus</b>. The <b>blastomeres in the blastocyst are arranged into an outer layer called "
    "the trophoblast and an inner group of cells attached to the trophoblast called the inner cell "
    "mass</b>.",
    "The <b>trophoblast layer gets attached to the endometrium and the inner cell mass gets "
    "differentiated as the embryo</b>.",
    "After attachment, the <b>uterine cells divide rapidly and cover the blastocyst</b>, so the "
    "<b>blastocyst becomes embedded in the endometrium</b> - this is called <b>implantation</b>, "
    "and it <b>leads to pregnancy</b>.",
]))
story.append(figure(
    "fig_2_11.png",
    "Fig. 2.11 - Transport of the ovum, fertilisation, and passage of the growing embryo through "
    "the fallopian tube. Labelled stages: morula, blastocyst and implantation.", max_width_cm=13.0))

# ======================================================================================
# ---- 2.6 PREGNANCY AND EMBRYONIC DEVELOPMENT ---- F170-F189 (heading F170, opener F171)
# ======================================================================================
# [VERIFICATION FIX] has_table=True: §2.6 carries a data_table (foetal-growth timeline).
story.append(heading("2.6", "Pregnancy and Embryonic Development", 1, has_table=True))
story.append(body(
    "After implantation, <b>finger-like projections appear on the trophoblast called chorionic "
    "villi</b>, which are <b>surrounded by the uterine tissue and maternal blood</b>. The "
    "<b>chorionic villi and uterine tissue become interdigitated and jointly form a structural "
    "and functional unit between the developing embryo (foetus) and the maternal body called the "
    "placenta</b>."))
story.append(body(
    "The <b>placenta facilitates the supply of oxygen and nutrients to the embryo</b> and the "
    "<b>removal of carbon dioxide and excretory/waste materials produced by the embryo</b>. It is "
    "<b>connected to the embryo through an umbilical cord</b>, which <b>helps in the transport of "
    "substances to and from the embryo</b>."))
story.append(body(
    "The <b>placenta also acts as an endocrine tissue</b> and <b>produces hormones like human "
    "chorionic gonadotropin (hCG), human placental lactogen (hPL), estrogens, progestogens, "
    "etc.</b> In the <b>later phase of pregnancy, a hormone called relaxin is also secreted by the "
    "ovary</b>."))
story.append(note(
    "<b>hCG, hPL and relaxin are produced in women only during pregnancy.</b> In addition, "
    "<b>during pregnancy the levels of other hormones like estrogens, progestogens, cortisol, "
    "prolactin, thyroxine, etc. are increased several-fold in the maternal blood</b>. The "
    "<b>increased production of these hormones is essential for supporting fetal growth, "
    "metabolic changes in the mother, and maintenance of pregnancy</b>."))
story.append(body(
    "<b>Immediately after implantation, the inner cell mass (embryo) differentiates into an outer "
    "layer, the ectoderm, and an inner layer, the endoderm</b>; a <b>mesoderm soon appears "
    "between them</b>. These <b>three (germ) layers give rise to all tissues (organs) in "
    "adults</b>. The <b>inner cell mass contains certain cells called stem cells</b> which have "
    "the <b>potency to give rise to all the tissues and organs</b>."))
story.append(body(
    "<b>Human pregnancy lasts 9 months.</b> The growth of the foetus follows a recognisable "
    "timeline:"))
story.append(data_table([
    ["Stage of pregnancy", "Development observed"],
    ["After <b>1 month</b>", "The <b>embryo's heart is formed</b>; the <b>first sign of the "
     "growing foetus may be noticed by listening to the heart sound through a stethoscope</b>."],
    ["End of <b>2 months</b>", "The <b>foetus develops limbs and digits</b>."],
    ["End of <b>12 weeks (first trimester)</b>", "<b>Most major organ systems are formed</b>; the "
     "<b>limbs and external genital organs are well-developed</b>."],
    ["<b>Fifth month</b>", "The <b>first movements of the foetus and the appearance of hair on "
     "the head are usually observed</b>."],
    ["End of about <b>24 weeks (end of second trimester)</b>", "The <b>body is covered with fine "
     "hair, the eye-lids separate, and eyelashes are formed</b>."],
    ["End of <b>9 months</b>", "The <b>foetus is fully developed and ready for delivery</b>."],
], col_widths=[3.4, 7.2]))
story.append(figure(
    "fig_2_12.png",
    "Fig. 2.12 - The human foetus within the uterus. Labelled parts: placental villi, umbilical "
    "cord, cavity of uterus, yolk sac, embryo and cervix.", max_width_cm=9.5))

# ======================================================================================
# ---- 2.7 PARTURITION AND LACTATION ---- F190-F204 (heading F190, opener F191)
# ======================================================================================
story.append(heading("2.7", "Parturition and Lactation", 1))
story.append(body(
    "The <b>average duration of human pregnancy is about 9 months</b>, which is called the "
    "<b>gestation period</b>. <b>Vigorous contraction of the uterus at the end of pregnancy "
    "causes expulsion/delivery of the foetus</b>. The <b>process of delivery of the foetus "
    "(childbirth) is called parturition</b>."))
story.append(body(
    "<b>Parturition is induced by a complex neuroendocrine mechanism</b> involving <b>cortisol, "
    "estrogens and oxytocin</b>. It proceeds as a self-reinforcing reflex:"))
story.append(process_flow([
    "<b>Signals for parturition originate from the fully developed foetus and the placenta</b> "
    "and <b>induce mild uterine contractions called the foetal ejection reflex</b>.",
    "The <b>foetal ejection reflex triggers the release of oxytocin from the maternal "
    "pituitary</b>.",
    "<b>Oxytocin acts on the uterine muscle and causes stronger uterine contractions</b>, which "
    "in turn <b>stimulate further secretion of oxytocin</b>.",
    "This <b>stimulatory reflex between uterine contraction and oxytocin secretion continues</b>, "
    "resulting in <b>stronger contractions and expulsion of the baby through the birth canal "
    "(parturition)</b>.",
]))
story.append(body(
    "<b>Soon after the infant is delivered, the placenta is also expelled out of the uterus.</b>"))
story.append(body(
    "The <b>mammary glands undergo differentiation during pregnancy</b> and <b>start producing "
    "milk towards the end of pregnancy by the process called lactation</b>. <b>Lactation helps "
    "the mother in feeding the new-born.</b> The <b>milk produced during the initial few days of "
    "lactation is called colostrum</b>, which <b>contains several antibodies absolutely essential "
    "to develop resistance for the new-born babies</b>. Hence <b>breast-feeding during the "
    "initial period of infant growth is recommended by doctors for bringing up a healthy "
    "baby</b>."))

# ======================================================================================
# ---- Quick Recap (§5 item 8; rewritten summary) ---- F205
# ======================================================================================
story.append(heading("QR", "Quick Recap", 1))
story.append(b1(
    "Humans are <b>sexually reproducing and viviparous</b>. The male reproductive system is a "
    "<b>pair of testes</b>, the <b>male sex accessory ducts, accessory glands and external "
    "genitalia</b>."))
story.append(b1(
    "Each testis has <b>about 250 testicular lobules</b>, each with <b>one to three seminiferous "
    "tubules</b> lined by <b>spermatogonia (which undergo meiosis to form sperms) and Sertoli "
    "cells (which nourish the germ cells)</b>; the <b>Leydig cells outside the tubules secrete "
    "androgens</b>. The male external genitalia is the <b>penis</b>."))
story.append(b1(
    "The female reproductive system is a <b>pair of ovaries, a pair of oviducts, a uterus, a "
    "vagina, external genitalia and a pair of mammary glands</b>. The <b>ovaries produce the ovum "
    "and ovarian (steroid) hormones</b>, with <b>ovarian follicles at different stages embedded "
    "in the stroma</b>. The <b>uterus has three layers - perimetrium, myometrium and "
    "endometrium</b>, and the <b>mammary glands are a female secondary sexual characteristic</b>."))
story.append(b1(
    "<b>Spermatogenesis</b> yields sperms carried by the accessory ducts; a sperm has a "
    "<b>head, neck, middle piece and tail</b>. <b>Oogenesis</b> forms the mature female gamete. "
    "The <b>reproductive cycle of female primates is the menstrual cycle</b>, which starts only "
    "after puberty, releases <b>one ovum per cycle</b>, and is <b>controlled by pituitary and "
    "ovarian hormones</b>."))
story.append(b1(
    "After coitus, <b>sperms reach the ampulla, where a sperm fertilises the ovum to form a "
    "diploid zygote</b>; the <b>X- or Y-bearing sperm determines the sex</b>. The zygote forms a "
    "<b>blastocyst that is implanted in the uterus</b>, the <b>placenta connects foetus and "
    "mother</b>, and <b>gestation lasts about 9 months</b>."))
story.append(b1(
    "<b>Parturition is induced by a complex neuroendocrine mechanism involving cortisol, "
    "estrogens and oxytocin</b>; the <b>mammary glands secrete milk (lactation) after childbirth</b>, "
    "beginning with the antibody-rich <b>colostrum</b>."))

# ======================================================================================
# ---- Terms used in the exercises (§5 item 9; GAP questions only) ---- F206
# ======================================================================================
story.append(heading("EX", "Terms Used in the Exercises", 1))
story.append(body(
    "Two exercise questions rely on ideas the chapter itself does not spell out. Both are "
    "answered here using only chapter-based reasoning."))
story.append(b1(
    "<b>Identical vs fraternal twins.</b> The chapter states that <b>one ovum is normally "
    "released per menstrual cycle</b> and that a <b>single sperm fertilises a single ovum</b> to "
    "form one zygote. <b>Identical twins</b> arise when <b>one fertilised ovum (one zygote) "
    "splits</b> to give two embryos - they share the same genetic make-up. <b>Fraternal "
    "(non-identical) twins</b> arise when <b>two separate ova are released and fertilised by two "
    "separate sperms</b>, giving two genetically different embryos."))
story.append(b1(
    "<b>Eggs released for a litter of six puppies.</b> Because each puppy develops from its own "
    "fertilised ovum (one zygote per offspring), a dog delivering a <b>litter of six puppies "
    "must have released at least six ova</b> in that cycle, each fertilised by a separate sperm."))

story.append(Spacer(1, 6))
story.append(Paragraph(
    "<i>Every fact, number, name, qualifier, table row, figure and figure label in NCERT Class 12 "
    "Chapter 2 is carried above. Nothing outside the source chapter has been added, except the "
    "clearly marked NOTE/MEMORY AID material and the exercise-gap explanations, which are derived "
    "only from chapter content.</i>", STYLES["Caption"]))


def main():
    return build_pdf(
        OUT_PDF, story,
        title="Class 12 Chapter 2 - Human Reproduction (NEET notes)",
        subject="NEET Biology",
    )


if __name__ == "__main__":
    sys.exit(main())
