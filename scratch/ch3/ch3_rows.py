"""
Ch3 Reproductive Health - Pass 1 working row set.

One tuple per inventory row: (session, section, type, wording)
  session : which Pass 1 session first produced the row (1-S, 1-H, 1-O, 1-F, 1-Z)
  section : NCERT section the row belongs to (Title / Intro / 3.1 ... / SUMMARY / EXERCISES / 3.1a ... for figure rows)
  type    : controlled vocabulary, lower-case only
  wording : the exact original wording (Rule 4: qualifiers preserved verbatim)

Rows are held in DOCUMENT ORDER. Final IDs (F001..FNNN) are assigned by
freeze_inventory.py in list order, so contiguity is structural, not hand-typed.
"""

ROWS = [
    # =====================================================================
    # TITLE  (session 1-H)
    # =====================================================================
    ("1-H", "Title", "title", '"CHAPTER 3 - REPRODUCTIVE HEALTH"'),
    ("1-H", "Title", "contents", 'Contents box lists five sections: "3.1 Reproductive Health - Problems and Strategies"; "3.2 Population Explosion and Birth Control"; "3.3 Medical Termination of Pregnancy"; "3.4 Sexually Transmitted Diseases"; "3.5 Infertility".'),

    # =====================================================================
    # INTRO  (chapter opener)
    # =====================================================================
    ("1-H", "Intro", "heading", 'The chapter opening has no printed section heading in NCERT; represented as "3.0 Reproductive Health" so its opener has a home (traceability: unnumbered chapter introduction, page 41).'),
    ("1-O", "Intro", "opener", '"You have learnt about human reproductive system and its functions in Chapter 2."'),
    ("1-S", "Intro", "fact", '"Now, let\'s discuss a closely related topic - reproductive health."'),
    ("1-S", "Intro", "term", '"The term simply refers to healthy reproductive organs with normal functions."'),
    ("1-S", "Intro", "fact", '"However, it has a broader perspective and includes the emotional and social aspects of reproduction also."'),
    ("1-S", "Intro", "definition", 'According to the "World Health Organisation (WHO)", reproductive health means "a total well-being in all aspects of reproduction, i.e., physical, emotional, behavioural and social".'),
    ("1-S", "Intro", "definition", '"Therefore, a society with people having physically and functionally normal reproductive organs and normal emotional and behavioural interactions among them in all sex-related aspects might be called reproductively healthy." (qualifier: "might be called")'),
    ("1-S", "Intro", "fact", 'Framing questions that set up the chapter: "What do we understand by this term?" and "Why is it significant to maintain reproductive health and what are the methods taken up to achieve it? Let us examine them."'),

    # =====================================================================
    # 3.1 REPRODUCTIVE HEALTH - PROBLEMS AND STRATEGIES
    # =====================================================================
    ("1-H", "3.1", "heading", '"3.1 REPRODUCTIVE HEALTH - PROBLEMS AND STRATEGIES"'),
    ("1-O", "3.1", "opener", '"India was amongst the first countries in the world to initiate action plans and programmes at a national level to attain total reproductive health as a social goal." (qualifier: "amongst the first" - not "the first") [SUMMARY-UNIQUE fold: the summary states it more strongly as "the first nation in the world" - carry both wordings here]'),
    ("1-S", "3.1", "number", 'These programmes called "family planning" were "initiated in 1951" and were periodically assessed over the past decades.'),
    ("1-S", "3.1", "fact", 'Improved programmes covering wider reproduction-related areas are currently in operation under the popular name "Reproductive and Child Health Care (RCH) programmes".'),
    ("1-S", "3.1", "fact", '"Creating awareness among people about various reproduction related aspects and providing facilities and support for building up a reproductively healthy society are the major tasks under these programmes."'),
    ("1-S", "3.1", "fact", '"With the help of audio-visual and the print-media governmental and non-governmental agencies have taken various steps to create awareness among the people about reproduction-related aspects."'),
    ("1-S", "3.1", "fact", '"Parents, other close relatives, teachers and friends, also have a major role in the dissemination of the above information."'),
    ("1-S", "3.1", "fact", '"Introduction of sex education in schools should also be encouraged to provide right information to the young so as to discourage children from believing in myths and having misconceptions about sex-related aspects."'),
    ("1-S", "3.1", "fact", '"Proper information about reproductive organs, adolescence and related changes, safe and hygienic sexual practices, sexually transmitted diseases (STD), AIDS, etc., would help people, especially those in the adolescent age group to lead a reproductively healthy life."'),
    ("1-S", "3.1", "fact", '"Educating people, especially fertile couples and those in marriageable age group, about available birth control options, care of pregnant mothers, post-natal care of the mother and child, importance of breast feeding, equal opportunities for the male and the female child, etc., would address the importance of bringing up socially conscious healthy families of desired size."'),
    ("1-S", "3.1", "fact", '"Awareness of problems due to uncontrolled population growth, social evils like sex-abuse and sex-related crimes, etc., need to be created to enable people to think and take up necessary steps to prevent them and thereby build up a socially responsible and healthy society."'),
    ("1-S", "3.1", "fact", '"Successful implementation of various action plans to attain reproductive health requires strong infrastructural facilities, professional expertise and material support."'),
    ("1-S", "3.1", "fact", '"These are essential to provide medical assistance and care to people in reproduction-related problems like pregnancy, delivery, STDs, abortions, contraception, menstrual problems, infertility, etc."'),
    ("1-S", "3.1", "fact", '"Implementation of better techniques and new strategies from time to time are also required to provide more efficient care and assistance to people."'),
    ("1-S", "3.1", "fact", '"Statutory ban on amniocentesis for sex-determination to legally check increasing menace of female foeticides, massive child immunisation, etc., are some programmes that merit mention in this connection."'),
    ("1-S", "3.1", "term", 'What amniocentesis is (source spelling "aminocentesis"): "some of the amniotic fluid of the developing foetus is taken to analyse the fetal cells and dissolved substances".'),
    ("1-S", "3.1", "fact", '"This procedure is used to test for the presence of certain genetic disorders such as, down syndrome, haemophilia, sickle-cell anemia, etc., determine the survivability of the foetus." (source prints "haemoplilia"; the source sentence is garbled - recorded as a Source problem in the Coverage note)'),
    ("1-S", "3.1", "fact", '"Research on various reproduction-related areas are encouraged and supported by governmental and non-governmental agencies to find out new methods and/or to improve upon the existing ones."'),
    ("1-S", "3.1", "fact", 'Do You Know box: "\'Saheli\' - a new oral contraceptive for the females - was developed by scientists at Central Drug Research Institute (CDRI) in Lucknow, India."'),
    ("1-S", "3.1", "fact", '"Better awareness about sex related matters, increased number of medically assisted deliveries and better post-natal care leading to decreased maternal and infant mortality rates, increased number of couples with small families, better detection and cure of STDs and overall increased medical facilities for all sex-related problems, etc. all indicate improved reproductive health of the society." [SUMMARY-UNIQUE fold: add "assistance to infertile couples" to this list of indicators]'),

    # =====================================================================
    # 3.2 POPULATION STABILISATION AND BIRTH CONTROL
    # (contents box calls this section "Population Explosion and Birth Control")
    # =====================================================================
    ("1-H", "3.2", "heading", '"3.2 POPULATION STABILISATION AND BIRTH CONTROL" (the page-1 contents box lists the same section as "Population Explosion and Birth Control")'),
    ("1-O", "3.2", "opener", '"In the last century an all-round development in various fields significantly improved the quality of life of the people."'),
    ("1-S", "3.2", "fact", '"However, increased health facilities along with better living conditions had an explosive impact on the growth of population." (this explosive growth is the "population explosion" of Exercise Q5 and the summary)'),
    ("1-S", "3.2", "number", '"The world population which was around 2 billion (2000 million) in 1900 rocketed to about 6 billion by 2000 and 7.2 billion in 2011."'),
    ("1-S", "3.2", "fact", '"A similar trend was observed in India too."'),
    ("1-S", "3.2", "number", '"Our population which was approximately 350 million at the time of our independence reached close to the billion mark by 2000 and crossed 1.2 billion in May 2011."'),
    ("1-S", "3.2", "fact", '"A rapid decline in death rate, maternal mortality rate (MMR) and infant mortality rate (IMR) as well as an increase in number of people in reproducible age are probable reasons for this."'),
    ("1-S", "3.2", "fact", '"Through our Reproductive Child Health (RCH) programme, though we could bring down the population growth rate, it was only marginal."'),
    ("1-S", "3.2", "number", '"According to the 2011 census report, the population growth rate was less than 2 per cent, i.e., 20/1000/year, a rate at which our population could increase rapidly."'),
    ("1-S", "3.2", "fact", '"Such an alarming growth rate could lead to an absolute scarcity of even the basic requirements, i.e., food, shelter and clothing, in spite of significant progress made in those areas."'),
    ("1-S", "3.2", "fact", '"Therefore, the government was forced to take up serious measures to check this population growth rate."'),
    ("1-S", "3.2", "fact", '"The most important step to overcome this problem is to motivate smaller families by using various contraceptive methods."'),
    ("1-S", "3.2", "fact", '"advertisements in the media as well as posters/bills, etc., showing a happy couple with two children with a slogan Hum Do Hamare Do (we two, our two)".'),
    ("1-S", "3.2", "fact", '"Many couples, mostly the young, urban, working ones have even adopted an \'one child norm\'." (qualifiers: "mostly the young, urban, working ones")'),
    ("1-S", "3.2", "number", '"Statutory raising of marriageable age of the female to 18 years and that of males to 21 years, and incentives given to couples with small families are two of the other measures taken to tackle this problem."'),
    ("1-S", "3.2", "fact", '"Let us describe some of the commonly used contraceptive methods, which help prevent unwanted pregnancies."'),
    ("1-S", "3.2", "term", '"An ideal contraceptive should be user-friendly, easily available, effective and reversible with no or least side-effects."'),
    ("1-S", "3.2", "fact", '"It also should in no way interfere with the sexual drive, desire and/or the sexual act of the user."'),
    ("1-S", "3.2", "fact", '"A wide range of contraceptive methods are presently available which could be broadly grouped into the following categories, namely Natural/Traditional, Barrier, IUDs, Oral contraceptives, Injectables, Implants and Surgical methods."'),
    ("1-S", "3.2", "fact", '"Natural methods work on the principle of avoiding chances of ovum and sperms meeting."'),
    ("1-S", "3.2", "number", '"Periodic abstinence is one such method in which the couples avoid or abstain from coitus from day 10 to 17 of the menstrual cycle when ovulation could be expected."'),
    ("1-S", "3.2", "term", '"As chances of fertilisation are very high during this period, it is called the fertile period."'),
    ("1-S", "3.2", "fact", '"Therefore, by abstaining from coitus during this period, conception could be prevented."'),
    ("1-S", "3.2", "term", '"Withdrawal or coitus interruptus is another method in which the male partner withdraws his penis from the vagina just before ejaculation so as to avoid insemination."'),
    ("1-S", "3.2", "term", '"Lactational amenorrhea (absence of menstruation) method is based on the fact that ovulation and therefore the cycle do not occur during the period of intense lactation following parturition."'),
    ("1-S", "3.2", "fact", '"Therefore, as long as the mother breast-feeds the child fully, chances of conception are almost nil." (qualifier: "almost nil")'),
    ("1-S", "3.2", "number", '"However, this method has been reported to be effective only upto a maximum period of six months following parturition." (qualifiers: "only", "maximum")'),
    ("1-S", "3.2", "fact", '"As no medicines or devices are used in these methods, side effects are almost nil."'),
    ("1-S", "3.2", "fact", '"Chances of failure, though, of this method are also high."'),
    ("1-S", "3.2", "fact", '"In barrier methods, ovum and sperms are prevented from physically meeting with the help of barriers."'),
    ("1-S", "3.2", "fact", '"Such methods are available for both males and females."'),
    ("1-S", "3.2", "term", '"Condoms (Figure 3.1 a, b) are barriers made of thin rubber/latex sheath that are used to cover the penis in the male or vagina and cervix in the female, just before coitus so that the ejaculated semen would not enter into the female reproductive tract."'),
    ("1-S", "3.2", "fact", '"This can prevent conception."'),
    ("1-S", "3.2", "fact", '"\'Nirodh\' is a popular brand of condom for the male."'),
    ("1-S", "3.2", "fact", '"Use of condoms has increased in recent years due to its additional benefit of protecting the user from contracting STIs and AIDS."'),
    ("1-S", "3.2", "fact", '"Both the male and the female condoms are disposable, can be self-inserted and thereby gives privacy to the user."'),
    ("1-S", "3.2", "term", '"Diaphragms, cervical caps and vaults are also barriers made of rubber that are inserted into the female reproductive tract to cover the cervix during coitus."'),
    ("1-S", "3.2", "fact", '"They prevent conception by blocking the entry of sperms through the cervix." "They are reusable."'),
    ("1-S", "3.2", "fact", '"Spermicidal creams, jellies and foams are usually used alongwith these barriers to increase their contraceptive efficiency." (qualifier: "usually")'),
    ("1-S", "3.2", "fact", '"Another effective and popular method is the use of Intra Uterine Devices (IUDs)."'),
    ("1-S", "3.2", "fact", '"These devices are inserted by doctors or expert nurses in the uterus through vagina."'),
    ("1-S", "3.2", "fact", '"These Intra Uterine Devices are presently available as the non-medicated IUDs (e.g., Lippes loop), copper releasing IUDs (CuT, Cu7, Multiload 375) and the hormone releasing IUDs (Progestasert, LNG-20) (Figure 3.2)."'),
    ("1-S", "3.2", "fact", '"IUDs increase phagocytosis of sperms within the uterus and the Cu ions released suppress sperm motility and the fertilising capacity of sperms."'),
    ("1-S", "3.2", "fact", '"The hormone releasing IUDs, in addition, make the uterus unsuitable for implantation and the cervix hostile to the sperms."'),
    ("1-S", "3.2", "fact", '"IUDs are ideal contraceptives for the females who want to delay pregnancy and/or space children."'),
    ("1-S", "3.2", "fact", '"It is one of most widely accepted methods of contraception in India."'),
    ("1-S", "3.2", "fact", '"Oral administration of small doses of either progestogens or progestogen-estrogen combinations is another contraceptive method used by the females."'),
    ("1-S", "3.2", "term", '"They are used in the form of tablets and hence are popularly called the pills."'),
    ("1-S", "3.2", "number", '"Pills have to be taken daily for a period of 21 days starting preferably within the first five days of menstrual cycle." (qualifier: "preferably")'),
    ("1-S", "3.2", "number", '"After a gap of 7 days (during which menstruation occurs) it has to be repeated in the same pattern till the female desires to prevent conception."'),
    ("1-S", "3.2", "fact", '"They inhibit ovulation and implantation as well as alter the quality of cervical mucus to prevent/retard entry of sperms."'),
    ("1-S", "3.2", "fact", '"Pills are very effective with lesser side effects and are well accepted by the females."'),
    ("1-S", "3.2", "fact", '"Saheli - the new oral contraceptive for the females contains a non-steroidal preparation."'),
    ("1-S", "3.2", "fact", '"It is a \'once a week\' pill with very few side effects and high contraceptive value."'),
    ("1-S", "3.2", "fact", '"Progestogens alone or in combination with estrogen can also be used by females as injections or implants under the skin (Figure 3.3)."'),
    ("1-S", "3.2", "fact", '"Their mode of action is similar to that of pills and their effective periods are much longer."'),
    ("1-S", "3.2", "number", '"Administration of progestogens or progestogen-estrogen combinations or IUDs within 72 hours of coitus have been found to be very effective as emergency contraceptives as they could be used to avoid possible pregnancy due to rape or casual unprotected intercourse."'),
    ("1-S", "3.2", "term", '"Surgical methods, also called sterilisation, are generally advised for the male/female partner as a terminal method to prevent any more pregnancies." (qualifier: "generally advised")'),
    ("1-S", "3.2", "fact", '"Surgical intervention blocks gamete transport and thereby prevent conception."'),
    ("1-S", "3.2", "term", '"Sterilisation procedure in the male is called \'vasectomy\' and that in the female, \'tubectomy\'."'),
    ("1-S", "3.2", "process", 'Vasectomy: "a small part of the vas deferens is removed or tied up through a small incision on the scrotum (Figure 3.4a)".'),
    ("1-S", "3.2", "process", 'Tubectomy: "a small part of the fallopian tube is removed (Figure 3.4b) or tied up through a small incision in the abdomen or through vagina".'),
    ("1-S", "3.2", "fact", '"These techniques are highly effective but their reversibility is very poor."'),
    ("1-S", "3.2", "fact", '"It needs to be emphasised that the selection of a suitable contraceptive method and its use should always be undertaken in consultation with qualified medical professionals." (qualifier: "should always")'),
    ("1-S", "3.2", "fact", '"One must also remember that contraceptives are not regular requirements for the maintenance of reproductive health."'),
    ("1-S", "3.2", "fact", '"In fact, they are practiced against a natural reproductive event, i.e., conception/pregnancy."'),
    ("1-S", "3.2", "fact", '"One is forced to use these methods either to prevent pregnancy or to delay or space pregnancy due to personal reasons."'),
    ("1-S", "3.2", "fact", '"No doubt, the widespread use of these methods have a significant role in checking uncontrolled growth of population."'),
    ("1-S", "3.2", "fact", '"However, their possible ill-effects like nausea, abdominal pain, breakthrough bleeding, irregular menstrual bleeding or even breast cancer, though not very significant, should not be totally ignored." (qualifier: "though not very significant")'),

    # =====================================================================
    # 3.3 MEDICAL TERMINATION OF PREGNANCY (MTP)
    # =====================================================================
    ("1-H", "3.3", "heading", '"3.3 MEDICAL TERMINATION OF PREGNANCY (MTP)"'),
    ("1-O", "3.3", "opener", '"Intentional or voluntary termination of pregnancy before full term is called medical termination of pregnancy (MTP) or induced abortion." (the opener defines the term used in its own section heading)'),
    ("1-S", "3.3", "number", '"Nearly 45 to 50 million MTPs are performed in a year all over the world which accounts to 1/5th of the total number of conceived pregnancies in a year."'),
    ("1-S", "3.3", "fact", '"Whether to accept / legalise MTP or not is being debated upon in many countries due to emotional, ethical, religious and social issues involved in it."'),
    ("1-S", "3.3", "number", '"Government of India legalised MTP in 1971 with some strict conditions to avoid its misuse."'),
    ("1-S", "3.3", "fact", '"Such restrictions are all the more important to check indiscriminate and illegal female foeticides which are reported to be high in India."'),
    ("1-S", "3.3", "fact", 'Question-and-answer pair: "Why MTP? Obviously the answer is - to get rid of unwanted pregnancies either due to casual unprotected intercourse or failure of the contraceptive used during coitus or rapes."'),
    ("1-S", "3.3", "fact", '"MTPs are also essential in certain cases where continuation of the pregnancy could be harmful or even fatal either to the mother or to the foetus or both."'),
    ("1-S", "3.3", "number", '"MTPs are considered relatively safe during the first trimester, i.e., upto 12 weeks of pregnancy." (qualifier: "relatively safe")'),
    ("1-S", "3.3", "fact", '"Second trimester abortions are much more riskier."'),
    ("1-S", "3.3", "fact", '"One disturbing trend observed is that a majority of the MTPs are performed illegally by unqualified quacks which are not only unsafe but could be fatal too." (qualifier: "a majority")'),
    ("1-S", "3.3", "fact", '"Another dangerous trend is the misuse of amniocentesis to determine the sex of the unborn child."'),
    ("1-S", "3.3", "fact", '"Frequently, if the foetus is found to be female, it is followed by MTP - this is totally against what is legal."'),
    ("1-S", "3.3", "fact", '"Such practices should be avoided because these are dangerous both for the young mother and the foetus."'),
    ("1-S", "3.3", "fact", '"Effective counselling on the need to avoid unprotected coitus and the risk factors involved in illegal abortions as well as providing more health care facilities could reverse the mentioned unhealthy trend."'),
    ("1-S", "3.3", "fact", 'Box: "The Medical Termination of Pregnancy (Amendment) Act, 2017 was enacted by the government of India with the intension of reducing the incidence of illegal abortion and consequent maternal mortality and morbidity."'),
    ("1-S", "3.3", "number", '"According to this Act, a pregnancy may be terminated on certain considered grounds within the first 12 weeks of pregnancy on the opinion of one registered medical practitioner." (qualifier: "may be terminated")'),
    ("1-S", "3.3", "number", '"If the pregnancy has lasted more than 12 weeks, but fewer than 24 weeks, two registered medical practitioners must be of the opinion, formed in good faith, that the required ground exist."'),
    ("1-S", "3.3", "fact", 'Grounds for termination under the Act: "(i) The continuation of the pregnancy would involve a risk to the life of the pregnant woman or of grave injury physical or mental health; or (ii) There is a substantial risk that of the child were born, it would suffer from such physical or mental abnormalities as to be seriously handicapped."'),

    # =====================================================================
    # 3.4 SEXUALLY TRANSMITTED INFECTIONS (STIS)
    # (contents box calls this section "Sexually Transmitted Diseases")
    # =====================================================================
    ("1-H", "3.4", "heading", '"3.4 SEXUALLY TRANSMITTED INFECTIONS (STIS)" (the page-1 contents box lists the same section as "Sexually Transmitted Diseases"; the summary calls them "Sexually Transmitted Diseases (STIs)")'),
    ("1-O", "3.4", "opener", '"Infections or diseases which are transmitted through sexual intercourse are collectively called sexually transmitted infections (STI) or venereal diseases (VD) or reproductive tract infections (RTI)." (the opener defines the term used in its own section heading)'),
    ("1-S", "3.4", "fact", '"Gonorrhoea, syphilis, genital herpes, chlamydiasis, genital warts, trichomoniasis, hepatitis-B and of course, the most discussed infection in the recent years, HIV leading to AIDS are some of the common STIs."'),
    ("1-S", "3.4", "fact", '"Among these, HIV infection is most dangerous and is discussed in detail in Chapter 7."'),
    ("1-S", "3.4", "fact", '"Some of these infections like hepatitis-B and HIV can also be transmitted by sharing of injection needles, surgical instruments, etc., with infected persons, transfusion of blood, or from an infected mother to the foetus too."'),
    ("1-S", "3.4", "exception", '"Except for hepatitis-B, genital herpes and HIV infections, other diseases are completely curable if detected early and treated properly."'),
    ("1-S", "3.4", "fact", '"Early symptoms of most of these are minor and include itching, fluid discharge, slight pain, swellings, etc., in the genital region."'),
    ("1-S", "3.4", "fact", '"Infected females may often be asymptomatic and hence, may remain undetected for long." (qualifiers: "may often", "may")'),
    ("1-S", "3.4", "fact", '"Absence or less significant symptoms in the early stages of infection and the social stigma attached to the STIs, deter the infected persons from going for timely detection and proper treatment."'),
    ("1-S", "3.4", "fact", '"This could lead to complications later, which include pelvic inflammatory diseases (PID), abortions, still births, ectopic pregnancies, infertility or even cancer of the reproductive tract."'),
    ("1-S", "3.4", "fact", '"STIs are a major threat to a healthy society."'),
    ("1-S", "3.4", "fact", '"Therefore, prevention or early detection and cure of these diseases are given prime consideration under the reproductive health-care programmes."'),
    ("1-S", "3.4", "number", '"Though all persons are vulnerable to these infections, their incidences are reported to be very high among persons in the age group of 15-24 years - the age group to which you also belong."'),
    ("1-S", "3.4", "fact", '"There is no reason to panic because prevention is possible."'),
    ("1-S", "3.4", "process", 'Three simple principles to be free of these infections: "(i) Avoid sex with unknown partners/multiple partners. (ii) Always try to use condoms during coitus. (iii) In case of doubt, one should go to a qualified doctor for early detection and get complete treatment if diagnosed with infection."'),

    # =====================================================================
    # 3.5 INFERTILITY
    # =====================================================================
    ("1-H", "3.5", "heading", '"3.5 INFERTILITY"'),
    ("1-O", "3.5", "opener", '"A discussion on reproductive health is incomplete without a mention of infertility."'),
    ("1-S", "3.5", "fact", '"A large number of couples all over the world including India are infertile, i.e., they are unable to produce children inspite of unprotected sexual co-habitation." [SUMMARY-UNIQUE fold: the summary adds the "even after 2 years of unprotected sexual cohabitation" criterion - carry it in this definition]'),
    ("1-S", "3.5", "fact", '"The reasons for this could be many - physical, congenital, diseases, drugs, immunological or even psychological."'),
    ("1-S", "3.5", "fact", '"In India, often the female is blamed for the couple being childless, but more often than not, the problem lies in the male partner."'),
    ("1-S", "3.5", "fact", '"Specialised health care units (infertility clinics, etc.) could help in diagnosis and corrective treatment of some of these disorders and enable these couples to have children."'),
    ("1-S", "3.5", "fact", '"However, where such corrections are not possible, the couples could be assisted to have children through certain special techniques commonly known as assisted reproductive technologies (ART)."'),
    ("1-S", "3.5", "term", '"In vitro fertilisation (IVF - fertilisation outside the body in almost similar conditions as that in the body) followed by embryo transfer (ET) is one of such methods."'),
    ("1-S", "3.5", "fact", '"In this method, popularly known as test tube baby programme, ova from the wife/donor (female) and sperms from the husband/donor (male) are collected and are induced to form zygote under simulated conditions in the laboratory."'),
    ("1-S", "3.5", "number", '"The zygote or early embryos (with upto 8 blastomeres) could then be transferred into the fallopian tube (ZIFT - zygote intra fallopian transfer) and embryos with more than 8 blastomeres, into the uterus (IUT - intra uterine transfer), to complete its further development."'),
    ("1-S", "3.5", "fact", '"Embryos formed by in-vivo fertilisation (fusion of gametes within the female) also could be used for such transfer to assist those females who cannot conceive."'),
    ("1-S", "3.5", "term", '"Transfer of an ovum collected from a donor into the fallopian tube (GIFT - gamete intra fallopian transfer) of another female who cannot produce one, but can provide suitable environment for fertilisation and further development is another method attempted."'),
    ("1-S", "3.5", "term", '"Intra cytoplasmic sperm injection (ICSI) is another specialised procedure to form an embryo in the laboratory in which a sperm is directly injected into the ovum."'),
    ("1-S", "3.5", "fact", '"Infertility cases either due to inability of the male partner to inseminate the female or due to very low sperm counts in the ejaculates, could be corrected by artificial insemination (AI) technique."'),
    ("1-S", "3.5", "fact", '"In this technique, the semen collected either from the husband or a healthy donor is artificially introduced either into the vagina or into the uterus (IUI - intra-uterine insemination) of the female."'),
    ("1-S", "3.5", "fact", '"Though options are many, all these techniques require extremely high precision handling by specialised professionals and expensive instrumentation."'),
    ("1-S", "3.5", "fact", '"Therefore, these facilities are presently available only in very few centres in the country." (qualifiers: "only", "very few")'),
    ("1-S", "3.5", "fact", '"Obviously their benefits is affordable to only a limited number of people."'),
    ("1-S", "3.5", "fact", '"Emotional, religious and social factors are also deterrents in the adoption of these methods."'),
    ("1-S", "3.5", "fact", '"Since the ultimate aim of all these procedures is to have children, in India we have so many orphaned and destitute children, who would probably not survive till maturity, unless taken care of."'),
    ("1-S", "3.5", "fact", '"Our laws permit legal adoption and it is as yet, one of the best methods for couples looking for parenthood."'),

    # =====================================================================
    # SUMMARY + EXERCISES headings (session 1-H)
    # =====================================================================
    ("1-H", "SUMMARY", "heading", '"SUMMARY"'),
    ("1-H", "EXERCISES", "heading", '"EXERCISES"'),

    # =====================================================================
    # FIGURE-LABEL MATRIX ROWS (session 1-F) - filled in after the assets are
    # rendered and every in-figure label is harvested by OPENING the asset.
    # =====================================================================
]

SUMMARY_CLASSIFICATION = [
    # (summary sentence, classification, search key into the Facts table, note)
    # The search key is resolved to the final row ID by freeze_inventory.py, so no
    # ID is ever hand-typed here (Gate 1 step 10: derive, never hand-tally).
    ("Reproductive health refers to a total well-being in all aspects of reproduction, i.e., physical, emotional, behavioural and social.", "BODY-PRESENT", "reproductive health means", ""),
    ("Our nation was the first nation in the world to initiate various action plans at national level towards attaining a reproductively healthy society.", "SUMMARY-UNIQUE", "amongst the first countries", 'body says "amongst the first countries in the world"; the summary states it more strongly as "the first nation in the world" - both wordings are carried side by side'),
    ("Counselling and creating awareness among people about reproductive organs, adolescence and associated changes, safe and hygienic sexual practices, sexually transmitted infections (STIs) including AIDS, etc., is the primary step towards reproductive health.", "BODY-PRESENT", "Creating awareness among people about various reproduction", "also F019/F020"),
    ("Providing medical facilities and care to the problems like menstrual irregularities, pregnancy related aspects, delivery, medical termination of pregnancy, STIs, birth control, infertility, post natal child and maternal management is another important aspect of the Reproductive and Child Health Care programmes.", "BODY-PRESENT", "These are essential to provide medical assistance and care", "also F030"),
    ("An overall improvement in reproductive health has taken place in our country as indicated by reduced maternal and infant mortality rates, early detection and cure of STIs, assistance to infertile couples, etc.", "SUMMARY-UNIQUE", "all indicate improved reproductive health of the society", '"assistance to infertile couples" is added to the body list of indicators'),
    ("Improved health facilities and better living conditions promoted an explosive growth of population.", "BODY-PRESENT", "explosive impact on the growth of population", ""),
    ("Such a growth necessitated intense propagation of contraceptive methods.", "BODY-PRESENT", "The most important step to overcome this problem", ""),
    ("Various contraceptive options are available now such as natural, traditional, barrier, IUDs, pills, injectables, implants and surgical methods.", "BODY-PRESENT", "could be broadly grouped into the following categories", ""),
    ("Though contraceptives are not regular requirements for reproductive health, one is forced to use them to avoid pregnancy or to delay or space pregnancy.", "BODY-PRESENT", "contraceptives are not regular requirements", "also F097"),
    ("Medical termination of pregnancy is legalised in our country.", "BODY-PRESENT", "legalised MTP in 1971", ""),
    ("MTP is generally performed to get rid of unwanted pregnancy due to rapes, casual relationship, etc., as also in cases when the continuation of pregnancy could be harmful or even fatal to either the mother, or the foetus or both.", "BODY-PRESENT", "to get rid of unwanted pregnancies", "also F107"),
    ("Infections or diseases transmitted through sexual intercourse are called Sexually Transmitted Diseases (STIs).", "BODY-PRESENT", "collectively called sexually transmitted infections", "the summary resumes the NCERT contents-box variant \"Sexually Transmitted Diseases\"; carried by the 3.4 heading row and the STI opener"),
    ("Pelvic Inflammatory Diseases (PIDs), still birth, infertility are some of the complications of them.", "BODY-PRESENT", "This could lead to complications later", ""),
    ("Early detection facilitate better cure of these diseases.", "BODY-PRESENT", "other diseases are completely curable if detected early", "also F130"),
    ("Avoiding sexual intercourse with unknown/multiple partners, use of condoms during coitus are some of the simple precautions to avoid contracting STIs.", "BODY-PRESENT", "Avoid sex with unknown partners/multiple partners", ""),
    ("Inability to conceive or produce children even after 2 years of unprotected sexual cohabitation is called infertility.", "SUMMARY-UNIQUE", "they are unable to produce children inspite of unprotected", 'the "even after 2 years" criterion appears nowhere in the body; folded into the infertility definition'),
    ("Various methods are now available to help such couples.", "BODY-PRESENT", "could be assisted to have children through certain special techniques", ""),
    ("In Vitro fertilisation followed by transfer of embryo into the female genital tract is one such method and is commonly known as the 'Test Tube Baby' Programme.", "BODY-PRESENT", "popularly known as test tube baby programme", "also F141"),
]

EXERCISES = [
    ("Q1", "What do you think is the significance of reproductive health in a society?", "COVERED", "3.1 (reproductively healthy society; improved reproductive health of the society)"),
    ("Q2", "Suggest the aspects of reproductive health which need to be given special attention in the present scenario.", "COVERED", "3.1 (awareness list, medical care list, statutory ban on amniocentesis, child immunisation)"),
    ("Q3", "Is sex education necessary in schools? Why?", "COVERED", "3.1 (introduction of sex education in schools)"),
    ("Q4", "Do you think that reproductive health in our country has improved in the past 50 years? If yes, mention some such areas of improvement.", "COVERED", "3.1 (indicators of improved reproductive health)"),
    ("Q5", "What are the suggested reasons for population explosion?", "COVERED", "3.2 (decline in death rate, MMR, IMR; increase in number of people in reproducible age)"),
    ("Q6", "Is the use of contraceptives justified? Give reasons.", "COVERED", "3.2 (contraceptives are not regular requirements; forced use; role in checking uncontrolled growth of population)"),
    ("Q7", "Removal of gonads cannot be considered as a contraceptive option. Why?", "GAP", 'chapter never discusses removal of gonads; answer added in the "Terms used in the exercises" appendix'),
    ("Q8", "Amniocentesis for sex determination is banned in our country. Is this ban necessary? Comment.", "COVERED", "3.1 (statutory ban to check female foeticides) + 3.3 (misuse of amniocentesis)"),
    ("Q9", "Suggest some methods to assist infertile couples to have children.", "COVERED", "3.5 (IVF-ET, ZIFT, IUT, GIFT, ICSI, AI/IUI)"),
    ("Q10", "What are the measures one has to take to prevent from contracting STDs?", "COVERED", "3.4 (three simple principles)"),
    ("Q11a", "State True/False with explanation: Abortions could happen spontaneously too.", "GAP", "the chapter defines only intentional/voluntary (induced) abortion; spontaneous abortion is never stated - answer added in the appendix"),
    ("Q11b", "Infertility is defined as the inability to produce a viable offspring and is always due to abnormalities/defects in the female partner.", "COVERED", "3.5 (2-year definition folded from the summary; problem lies in the male partner more often than not; reasons list)"),
    ("Q11c", "Complete lactation could help as a natural method of contraception.", "COVERED", "3.2 (lactational amenorrhea)"),
    ("Q11d", "Creating awareness about sex related aspects is an effective method to improve reproductive health of the people.", "COVERED", "3.1 (awareness creation as a major task; sex education)"),
    ("Q12a", "Correct the statement: Surgical methods of contraception prevent gamete formation.", "COVERED", "3.2 (surgical intervention blocks gamete transport)"),
    ("Q12b", "Correct the statement: All sexually transmitted diseases are completely curable.", "COVERED", "3.4 (except hepatitis-B, genital herpes and HIV)"),
    ("Q12c", "Correct the statement: Oral pills are very popular contraceptives among the rural women.", "GAP", 'the chapter states pills are "well accepted by the females" but never distinguishes rural from urban users - answer added in the appendix'),
    ("Q12d", "Correct the statement: In E. T. techniques, embryos are always transferred into the uterus.", "COVERED", "3.5 (ZIFT transfers the zygote/early embryo into the fallopian tube; IUT into the uterus)"),
]

# Figure-label matrix rows (session 1-F) - appended after the assets are rendered
# and every in-figure label has been harvested by OPENING the asset.
FIGURE_ROWS = [
    # Session 1-F. One row per rendered asset. Labels were harvested by OPENING each
    # converted asset (skill §5) - and that mattered: both Fig 3.4 labels are VECTOR
    # artwork, absent from the PDF text layer, so a text-layer harvest would have
    # returned an empty set and passed check 6 vacuously.
    ("1-F", "3.1a", "caption", "No in-figure text labels - unlabelled line-art diagram; harvest confirmed by opening the rendered asset and by a zero text-layer word count inside the pinned rect."),
    ("1-F", "3.1b", "caption", "No in-figure text labels - unlabelled photograph; harvest confirmed by opening the rendered asset and by a zero text-layer word count inside the pinned rect."),
    ("1-F", "3.2", "caption", "No in-figure text labels - unlabelled photograph (Copper T device); harvest confirmed by opening the rendered asset and by a zero text-layer word count inside the pinned rect."),
    ("1-F", "3.3", "caption", "No in-figure text labels - unlabelled photograph (implants held between fingers); harvest confirmed by opening the rendered asset and by a zero text-layer word count inside the pinned rect."),
    ("1-F", "3.4a", "caption", 'Figure labels: "Vas deferens tied and cut"'),
    ("1-F", "3.4b", "caption", 'Figure labels: "Fallopian tubes tied and cut"'),
]
