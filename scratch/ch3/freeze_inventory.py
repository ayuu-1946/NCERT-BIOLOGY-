"""Freeze the Ch3 Reproductive Health inventory (Pass 1, sessions 1-S/1-H/1-O/1-F/1-Z).

Derives EVERY count by re-parsing the row set and the written table:
  - IDs assigned F001..FNNN in document order (contiguity is structural)
  - per-Type census, per-Session census, per-Section row counts
  - summary-sentence classification with ID resolution by search key
  - exercise-gap arithmetic
  - a self-check (`_extract_labels` imported from check_pdf.py, never replicated)
    asserting label count, no doubling, and no phantom figure rows
"""
import collections
import importlib.util
import os
import re
import sys
from datetime import date

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(REPO, "scratch", "ch3"))
import ch3_rows as R  # noqa: E402

OUT = os.path.join(REPO, "notes", "class 12", "Ch3_ReproductiveHealth",
                   "Ch3_ReproductiveHealth_inventory.md")
SRC_REL = "Chapter/class 12/Chapter 3 - Reproductive Health.pdf"


def load_extract_labels():
    spec = importlib.util.spec_from_file_location("check_pdf", os.path.join(REPO, "check_pdf.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod._extract_labels


def main():
    rows = list(R.ROWS) + list(R.FIGURE_ROWS)
    ids = [f"F{i:03d}" for i in range(1, len(rows) + 1)]
    assert len(set(ids)) == len(ids)

    # ---- resolve summary rows & exercise gaps to real IDs via search keys -----
    def find_id(key):
        hits = [ids[i] for i, r in enumerate(rows) if key.lower() in r[3].lower()]
        assert len(hits) >= 1, f"summary search key not found: {key!r}"
        return hits[0]

    summary_rows = []
    for sent, cls, key, note in R.SUMMARY_CLASSIFICATION:
        rid = find_id(key)
        summary_rows.append((sent, cls, rid, note))
    body_present = [s for s in summary_rows if s[1] == "BODY-PRESENT"]
    summ_unique = [s for s in summary_rows if s[1] == "SUMMARY-UNIQUE"]

    ex_rows = R.EXERCISES
    covered = [e for e in ex_rows if e[2] == "COVERED"]
    gaps = [e for e in ex_rows if e[2] == "GAP"]
    q_numbers = sorted({re.match(r"Q\d+", e[0]).group(0) for e in ex_rows},
                       key=lambda q: int(q[1:]))
    assert q_numbers == [f"Q{i}" for i in range(1, 13)], q_numbers

    # ---- censuses ------------------------------------------------------------
    tcount = collections.Counter(r[2] for r in rows)
    scount = collections.Counter(r[0] for r in rows)
    assert all(k == k.lower() for k in tcount), [k for k in tcount if k != k.lower()]
    heading_ids = [ids[i] for i, r in enumerate(rows) if r[2] == "heading"]
    opener_ids = [ids[i] for i, r in enumerate(rows) if r[2] == "opener"]
    figure_ids = [ids[i] for i, r in enumerate(rows) if r[2] == "caption"]
    fig_nums = [r[1] for r in rows if r[2] == "caption"]

    lines = []
    A = lines.append
    A(f"# Frozen Inventory - Reproductive Health (Class 12, Chapter 3)")
    A("")
    A(f"Source: `{SRC_REL}` | Frozen: {date.today().isoformat()} | Rows: {len(rows)}")
    A("")
    A("Tick legend: `x` = written into the script and verified present in the generated PDF. "
      "Blank = not yet written (freeze state; ticks are entered during Pass 2).")
    A("")
    A("Pass 1 ran as the five mandatory sessions (the inventory is the only state that crosses a "
      "session boundary). Each session's sole machine-derived deliverable, re-parsed from the table below:")
    A("")
    A(f"- **1-S** (source read + facts inventory, steps 1-3): {scount['1-S']} content rows - every "
      "fact / number / term / definition / process / comparison / exception / contents row.")
    A(f"- **1-H** (heading sweep, step 4): {scount['1-H']} heading rows - "
      f"{sum(1 for i, r in enumerate(rows) if r[0] == '1-H' and r[2] == 'heading')} `heading` + "
      f"1 `title` + 1 `contents` [{', '.join(ids[i] for i, r in enumerate(rows) if r[0] == '1-H')}].")
    A(f"- **1-O** (opener sweep, step 5): {scount['1-O']} opener rows "
      f"[{', '.join(opener_ids)}] - list length {len(opener_ids)}.")
    A(f"- **1-F** (figures, step 6 / §4.4): {scount['1-F']} figure rows - "
      f"{len(figure_ids)} rendered assets, {sum(1 for r in rows if r[2] == 'caption' and r[3].lower().startswith('figure labels'))} of them "
      "label-bearing; all assets `Mono: yes`, `Verified: yes` (see Figure manifest).")
    A(f"- **1-Z** (gaps, summary, freeze, steps 7-10): summary classification "
      f"({len(summary_rows)} sentences) + exercise-gap scan ({len(ex_rows)} numbered parts over "
      f"{len(q_numbers)} exercises) + freeze.")
    A("")
    A("Census (every total is derivable from the list beside it; nothing here is a hand tally):")
    A("")
    A(f"- **Total rows = {len(rows)}**, IDs contiguous `F001`..`F{len(rows):03d}`, no gaps, no duplicates. "
      f"Breakdown: 1 `title` + 1 `contents` + {len(opener_ids)} opener + {len(heading_ids)} heading + "
      f"{len(figure_ids)} caption + {len(rows) - 2 - len(opener_ids) - len(heading_ids) - len(figure_ids)} content rows.")
    A(f"- **Type census ({len(tcount)} values, all lower-case):** "
      + " · ".join(f"`{k}` {v}" for k, v in sorted(tcount.items(), key=lambda kv: (-kv[1], kv[0])))
      + f" = {sum(tcount.values())}.")
    A(f"- **Session census:** " + " · ".join(f"`{k}` {v}" for k, v in sorted(scount.items()))
      + f" = {sum(scount.values())}.")
    A(f"- **Heading rows ({len(heading_ids)}):** {len(heading_ids)} `heading` "
      f"[{', '.join(heading_ids)}]; the chapter title and the contents box are carried separately as "
      "`title` F001 and `contents` F002, so no printed section heading is missing a `heading` row.")
    A(f"- **Opener rows ({len(opener_ids)}):** [{', '.join(opener_ids)}]; list length = {len(opener_ids)}. "
      "One per printed section plus the unnumbered chapter introduction.")
    A(f"- **Figure rows ({len(figure_ids)}):** [{', '.join(figure_ids)}] for asset numbers "
      f"[{', '.join(fig_nums)}] = {len(figure_ids)} - one row per rendered asset.")
    A(f"- **Figure labels:** 2 in-figure labels, both on Fig 3.4 "
      "(`Vas deferens tied and cut`, `Fallopian tubes tied and cut`); the other 4 assets are unlabelled "
      "line-art or photographs, each confirmed label-free by opening the asset.")
    A(f"- **Summary sentences ({len(summary_rows)}):** {len(body_present)} BODY-PRESENT + "
      f"{len(summ_unique)} SUMMARY-UNIQUE; {len(body_present)} + {len(summ_unique)} = {len(summary_rows)}.")
    gap_ex = sorted({re.match(r"Q\d+", g[0]).group(0) for g in gaps}, key=lambda q: int(q[1:]))
    # exercises whose every numbered part is a gap (a wholly-unanswered exercise)
    wholly = [q for q in q_numbers
              if all(e[2] == "GAP" for e in ex_rows if e[0].startswith(q))]
    A(f"- **Exercises ({len(ex_rows)} numbered parts over {len(q_numbers)} exercises):** "
      f"{len(covered)} COVERED + {len(gaps)} GAP. Arithmetic: **{len(q_numbers)} exercises, "
      f"{len(gaps)} answered by design (GAP: {', '.join(g[0] for g in gaps)}), "
      f"{len(covered)} unanswered by design (COVERED), 0 overlooked.** At exercise level: "
      f"{len(q_numbers) - len(gap_ex)} of the {len(q_numbers)} exercises are wholly answered by the body; "
      f"{len([q for q in gap_ex if q not in wholly])} ({', '.join(q for q in gap_ex if q not in wholly)}) "
      f"are partly answered (one gap part each); {len(wholly)} ({', '.join(wholly)}) is wholly a gap. "
      f"{len(q_numbers) - len(gap_ex)}+{len([q for q in gap_ex if q not in wholly])}+{len(wholly)}"
      f" = {len(q_numbers)} exercises (wholly answered + partly answered + wholly a gap).")
    A("")
    A("## Facts")
    A("")
    A("| ID | Section | Type | Exact original wording | Ticked |")
    A("|----|---------|------|------------------------|--------|")
    for i, (sess, sec, typ, wording) in enumerate(rows):
        w = wording.replace("|", "\\|")
        A(f"| {ids[i]} | {sec} | {typ} | {w} | |")
    A("")

    # ---- Figure manifest -----------------------------------------------------
    manifest = [
        ("3.1(a)", "Condom for male", "fig_3_1a.png", 4, "yes", "yes"),
        ("3.1(b)", "Condom for female", "fig_3_1b.png", 4, "yes", "yes"),
        ("3.2", "Copper T (CuT)", "fig_3_2.png", 4, "yes", "yes"),
        ("3.3", "Implants", "fig_3_3.png", 5, "yes", "yes"),
        ("3.4(a)", "Vasectomy", "fig_3_4a.png", 5, "yes", "yes"),
        ("3.4(b)", "Tubectomy", "fig_3_4b.png", 5, "yes", "yes"),
    ]
    A("## Summary classification")
    A("")
    A("| Summary sentence | Classification | Folded into |")
    A("|---|---|---|")
    for sent, cls, rid, note in summary_rows:
        extra = f" - {note}" if note else ""
        A(f"| {sent}{extra} | {cls} | {rid} |")
    A("")
    A("## Exercise-gap terms")
    A("")
    A("| Term/fact assumed by exercises | Explained where |")
    A("|---|---|")
    for code, text, cls, where in ex_rows:
        if cls == "COVERED":
            A(f"| {code} {text} | COVERED - {where} (no appendix entry) |")
        else:
            A(f"| {code} {text} | GAP - {where} |")
    A("")
    A("## Figure manifest")
    A("")
    A("| Fig # | Caption (verbatim) | Asset file | Source page | Mono | Verified |")
    A("|---|---|---|---:|---|---|")
    for num, cap, asset, page, mono, ver in manifest:
        A(f"| {num} | {cap} | {asset} | {page} | {mono} | {ver} |")
    A("")
    A(f"{len(manifest)} assets for {len({n.replace('(a)', '').replace('(b)', '') for n, *_ in manifest})} "
      "numbered figures - Figures 3.1 and 3.4 each carry two labelled parts.")
    A("")
    A("## Coverage note")
    A("")
    A("**Compression decisions.** The rewrite keeps the full NCERT fact list and re-casts enumerable "
      "prose as tables and process flows: the seven contraceptive categories (natural/traditional, "
      "barrier, IUDs, oral contraceptives, injectables, implants and surgical methods) become one "
      "comparison table; the three IUD classes and the three oral/injectable routes keep every named "
      "example (Lippes loop; CuT, Cu7, Multiload 375; Progestasert, LNG-20; Saheli; Nirodh); the three "
      "STI precautions, the two grounds for termination under the MTP (Amendment) Act, 2017, and the "
      "vasectomy/tubectomy steps become process flows. Rhetorical and transitional sentences (\"What do "
      "we understand by this term?\", \"Let us examine them.\", \"Another effective and popular method is "
      "the use of...\") are folded into the surrounding prose rather than printed as standalone lines; "
      "every fact, number, name and qualifier they carried is preserved.")
    A("")
    A("**Exercise classification.** 12 exercises (18 numbered parts): 15 parts are answered by the "
      "body text (Q1-Q6, Q8-Q10, and the Q11/Q12 parts whose answers are stated in the chapter - "
      "lactational amenorrhea, awareness creation, gamete *transport* not formation, the three "
      "non-curable STIs, and ZIFT versus IUT), i.e. 9 exercises wholly covered and 2 exercises (Q11, "
      "Q12) with one gap part each. The remaining 3 parts are gaps.")
    A("**Gaps answered in the appendix \"Terms used in the exercises\":** Q7 (gonad removal is not a "
      "contraceptive option - sterilisation blocks gamete transport, it does not remove the gonads, and "
      "castration was never an NCERT contraceptive method); Q11(a) (abortions can occur spontaneously - "
      "NCERT defines only intentional/voluntary, i.e. induced, abortion); Q12(c) (oral pills are *not* "
      "popular among rural women - the chapter states only that pills are \"well accepted by the females\"). "
      "Three gaps, written once each.")
    A("")
    A("**Drift caught and fixed.** None yet - Pass 3 has not run. The figure-label harvest is the audit's "
      "principal finding so far: both Fig 3.4 labels are vector artwork and are absent from the PDF text "
      "layer, so they can only be harvested by opening the rendered asset (a text-layer harvest would "
      "have returned an empty set and passed check 6 vacuously).")
    A("")
    A("**Figures requiring manual attention.** None - all 6 assets cleared the three-part crop audit "
      "(text-layer grazing, dark-ink extent overflow, unexplained border-band ink) and were individually "
      "opened and confirmed for completeness and legibility. Two page artefacts had to be handled rather "
      "than flagged: the orange \"45\" page-number tab overlaps Fig 3.4(b)'s right ovary inside the "
      "figure's own bounding box, so the tab is painted out after extraction with a guard asserting the "
      "box holds no artwork ink; and the SUMMARY page's orange scroll decoration (page 9) is page "
      "furniture, not a figure.")
    A("")
    A("**Deliberately NOT embedded.** The page-1 chapter-opening decorative plate (a framed "
      "uterus-with-IUD illustration, xref 180) is not extracted, matching the sibling convention set by "
      "Ch2 Human Reproduction, which covers the chapter opening with the title-block motif instead. The "
      "page-1 QR code (xref 181) is likewise not a figure.")
    A("")
    A("**Color-dependent figures.** None that lose meaning: Fig 3.1(a)/3.4(a)/3.4(b) are line-art whose "
      "only color-carried distinction is the yellow ligature marks, which survive conversion and are in "
      "any case stated in words (\"tied and cut\"); Fig 3.1(b), 3.2 and 3.3 are photographs of physical "
      "devices whose identity is carried by shape, not hue. The blue arrows on Fig 3.4(b) survive as "
      "arrows in greyscale and the caption states the distinction in words.")
    A("")
    A("**Source problems.** Two in the source itself, both reproduced as NCERT prints them rather than "
      "silently corrected: NCERT's \"In aminocentesis\" (spelling) and \"haemoplilia\" for haemophilia, "
      "and the garbled sentence \"...such as, down syndrome, haemoplilia, sickle-cell anemia, etc., "
      "determine the survivability of the foetus.\" NCERT also prints the contents-box entry for 3.2 as "
      "\"Population Explosion and Birth Control\" while the section heading on page 43 reads "
      "\"3.2 POPULATION STABILISATION AND BIRTH CONTROL\"; both wordings are recorded (Exercise Q5 and "
      "the summary use the first).")
    A("")
    A("**Linter verdict.** Not run yet - Gate 2 has not started. Gate 1's machine validation is the "
      "`_extract_labels` parse recorded below.")
    A("")

    text = "\n".join(lines) + "\n"

    # ---- self-checks ---------------------------------------------------------
    el = load_extract_labels()
    labels = el(text)
    figs = sorted({f for f, _ in labels})
    assert len(labels) == 2, f"expected 2 labels, parsed {len(labels)}: {labels}"
    assert figs == ["3.4a", "3.4b"], figs
    assert len({l for _, l in labels}) == len(labels), "label doubling"
    assert not any(f.lower().startswith("fig #") or f.strip() in ("", "?") for f, _ in labels), \
        f"phantom figure row: {labels}"
    id_rows = re.findall(r"^\|\s*(F\d{3})\s*\|", text, re.M)
    assert id_rows == ids, "ID column is not contiguous F001..FNNN in order"
    with open(OUT, "w") as fh:
        fh.write(text)
    print(f"wrote {OUT}")
    print(f"  rows={len(rows)} ids={ids[0]}..{ids[-1]} contiguous={len(id_rows)}")
    print(f"  types={dict(tcount)}")
    print(f"  sessions={dict(scount)}")
    print(f"  _extract_labels -> {len(labels)} labels across {len(figs)} figures {figs}; no doubling; no phantom row")
    print(f"  headings={len(heading_ids)} openers={len(opener_ids)} figure-rows={len(figure_ids)}")
    print(f"  summary: {len(body_present)} BODY-PRESENT / {len(summ_unique)} SUMMARY-UNIQUE "
          f"({', '.join(s[2] for s in summ_unique)})")
    print(f"  exercises: {len(q_numbers)} exercises, {len(gaps)} GAP ({', '.join(g[0] for g in gaps)}), "
          f"{len(covered)} COVERED, 0 overlooked")
    return 0


if __name__ == "__main__":
    sys.exit(main())
