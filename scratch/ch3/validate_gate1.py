"""GATE 1 machine validation for Ch3 Reproductive Health.

Re-parses the FROZEN INVENTORY FILE (not the generator's in-memory rows) so the
artifact that crosses the handoff is what actually gets checked. Asserts every
Gate 1 criterion in GATE_1_PASS_1_SOURCE_MASTERY.md §7.
"""
import importlib.util
import os
import re
import sys

from PIL import Image

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CH = os.path.join(REPO, "notes", "class 12", "Ch3_ReproductiveHealth")
INV = os.path.join(CH, "Ch3_ReproductiveHealth_inventory.md")
ASSETS = os.path.join(CH, "assets")
FAILS, CHECKS = [], []


def check(name, ok, detail=""):
    CHECKS.append((name, ok, detail))
    if not ok:
        FAILS.append(f"{name}: {detail}")
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f" - {detail}" if detail else ""))


def load_extract_labels():
    spec = importlib.util.spec_from_file_location("check_pdf", os.path.join(REPO, "check_pdf.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod._extract_labels


def main():
    text = open(INV).read()
    print("GATE 1 validation - Ch3 Reproductive Health")
    print("=" * 62)

    # ---- Facts table --------------------------------------------------------
    rows, in_facts = [], False
    for line in text.splitlines():
        if line.startswith("## Facts"):
            in_facts = True
            continue
        if in_facts and line.startswith("## "):
            in_facts = False
        if in_facts and line.strip().startswith("|"):
            c = [x.strip() for x in line.strip().strip("|").split("|")]
            if re.fullmatch(r"F\d{3}", c[0]):
                rows.append(c)
    ids = [r[0] for r in rows]
    expect = [f"F{i:03d}" for i in range(1, len(rows) + 1)]
    check("Facts rows parsed", len(rows) > 0, f"{len(rows)} rows")
    check("IDs contiguous F001..FNNN, no gaps/dupes", ids == expect,
          f"{ids[0]}..{ids[-1]}, {len(set(ids))} unique")
    types = [r[2] for r in rows]
    check("Type column uses one normalized casing (all lower-case)",
          all(t == t.lower() for t in types),
          f"{sorted(set(types))}")
    check("no row has an empty Section or wording", all(r[1] and r[3] for r in rows))
    check("every row unticked at freeze (Gate 1 state)",
          all(len(r) < 5 or r[4] == "" for r in rows),
          f"{sum(1 for r in rows if len(r) > 4 and r[4])} ticked")

    # ---- header counts vs a re-parse of the table ---------------------------
    head = text.split("## Facts")[0]
    n = len(rows)
    m_rows = re.search(r"Rows: (\d+)", head)
    check("header 'Rows:' equals parsed row count",
          f"Rows: {n}" in head, f"header says {m_rows.group(1) if m_rows else '?'}")
    check("header total-rows census equals parsed row count",
          f"**Total rows = {n}**" in head)
    tc = {}
    for t in types:
        tc[t] = tc.get(t, 0) + 1
    for t, v in sorted(tc.items()):
        check(f"type census `{t}` = {v} matches header",
              f"`{t}` {v}" in head)
    for sess in ("1-S", "1-H", "1-O", "1-F"):
        got = sum(1 for l in head.splitlines() if f"**{sess}**" in l)
        check(f"session log has a {sess} entry", got == 1)
    for label, key in (("heading", "Heading rows"), ("opener", "Opener rows"),
                       ("caption", "Figure rows")):
        hid = [r[0] for r in rows if r[2] == label]
        m = re.search(rf"\*\*{key} \((\d+)\)", head)
        check(f"{key} header count == parsed {label} rows",
              m and int(m.group(1)) == len(hid), f"header {m.group(1) if m else '?'} vs rows {len(hid)}")
        line = next((l for l in head.splitlines() if l.startswith(f"- **{key} (")), "")
        br = re.search(r"\[([^\]]+)\]", line)
        listed = re.findall(r"F\d{3}", br.group(1)) if br else []
        check(f"{key} census list length == its total",
              len(set(listed)) == len(hid), f"listed {sorted(set(listed))}")

    # ---- figure-label matrix via check_pdf.py's own parser ------------------
    el = load_extract_labels()
    labels = el(text)
    figs = sorted({f for f, _ in labels})
    check("_extract_labels parses the expected label count (2)",
          len(labels) == 2, f"{len(labels)}: {labels}")
    check("_extract_labels sees no label doubling",
          len({l for _, l in labels}) == len(labels))
    check("_extract_labels sees no phantom figure rows",
          all(not f.lower().startswith("fig") and f not in ("?", "") for f, _ in labels),
          f"figure ids: {figs}")
    check("label-bearing figures match the manifest parts (3.4a, 3.4b)",
          figs == ["3.4a", "3.4b"])

    # ---- figure manifest ----------------------------------------------------
    man, in_man = [], False
    for line in text.splitlines():
        if line.startswith("## Figure manifest"):
            in_man = True
            continue
        if in_man and line.startswith("## "):
            in_man = False
        if in_man and line.strip().startswith("|"):
            c = [x.strip() for x in line.strip().strip("|").split("|")]
            if c and re.match(r"^\d\.\d", c[0]):
                man.append(c)
    check("manifest has one row per rendered asset", len(man) == 6, f"{len(man)} rows")
    check("every manifest row is Mono: yes", all(r[4].lower() == "yes" for r in man))
    check("every manifest row is Verified: yes", all(r[5].lower() == "yes" for r in man))
    missing = []
    for r in man:
        p = os.path.join(ASSETS, r[2])
        if not os.path.exists(p):
            missing.append(r[2])
            continue
        im = Image.open(p)
        if im.mode != "L" or len(im.getbands()) != 1:
            missing.append(f"{r[2]}(mode={im.mode})")
    check("every asset file exists on disk in true greyscale (mode L)", not missing, str(missing))
    figrows = [r for r in rows if r[2] == "caption"]
    check("one Facts caption row per manifest asset",
          sorted(r[1] for r in figrows) == sorted(r[0].replace("(", "").replace(")", "") for r in man),
          f"{[r[1] for r in figrows]}")

    # ---- summary classification --------------------------------------------
    summ = []
    in_s = False
    for line in text.splitlines():
        if line.startswith("## Summary classification"):
            in_s = True
            continue
        if in_s and line.startswith("## "):
            in_s = False
        if in_s and line.strip().startswith("|") and line.count("|") >= 4:
            c = [x.strip() for x in line.strip().strip("|").split("|")]
            if c[1] in ("BODY-PRESENT", "SUMMARY-UNIQUE"):
                summ.append(c)
    bp = [s for s in summ if s[1] == "BODY-PRESENT"]
    su = [s for s in summ if s[1] == "SUMMARY-UNIQUE"]
    check("summary table classifies every sentence", len(summ) == 18, f"{len(summ)} sentences")
    check("summary arithmetic (BODY-PRESENT + SUMMARY-UNIQUE == sentences)",
          len(bp) + len(su) == len(summ), f"{len(bp)} + {len(su)} = {len(summ)}")
    check("header summary census matches the parsed split",
          f"**Summary sentences (18):** {len(bp)} BODY-PRESENT + {len(su)} SUMMARY-UNIQUE" in head)
    bad = [s[2] for s in summ if s[2] not in ids]
    check("every 'Folded into' ID exists in the Facts table", not bad, str(bad))
    su_ids = [s[2] for s in su]
    by_id = {r[0]: r[3] for r in rows}
    folds_ok = all("SUMMARY-UNIQUE fold" in by_id.get(sid, "") for sid in su_ids)
    check("every SUMMARY-UNIQUE target row carries an explicit fold note",
          folds_ok, f"SUMMARY-UNIQUE -> {su_ids}")

    # ---- exercises ----------------------------------------------------------
    ex = []
    in_e = False
    for line in text.splitlines():
        if line.startswith("## Exercise-gap terms"):
            in_e = True
            continue
        if in_e and line.startswith("## "):
            in_e = False
        if in_e and line.strip().startswith("|") and line.count("|") >= 3:
            c = [x.strip() for x in line.strip().strip("|").split("|")]
            if re.match(r"^Q\d+", c[0]):
                ex.append(c)
    cov = [e for e in ex if e[1].startswith("COVERED")]
    gap = [e for e in ex if e[1].startswith("GAP")]
    qs = {re.match(r"Q\d+", e[0]).group(0) for e in ex}
    check("exercise table covers every numbered part", len(ex) == 18 and len(qs) == 12,
          f"{len(ex)} parts over {len(qs)} exercises")
    check("exercise arithmetic in the header matches the table",
          f"{len(cov)} COVERED + {len(gap)} GAP" in head, f"{len(cov)} COVERED + {len(gap)} GAP")
    check("every GAP names where its answer lives",
          all("appendix" in e[1] for e in gap), f"{len(gap)} gaps")
    check("no COVERED row reproduces an answer (classification only)",
          all("(no appendix entry)" in e[1] for e in cov))

    # ---- Pass 2 printing dispositions (Rule 3) -----------------------------
    disp = text.split("**Pass 2 printing dispositions (Rule 3).**")[1].split("**Exercise classification.")[0] \
        if "**Pass 2 printing dispositions (Rule 3).**" in text else ""
    check("dispositions block present in the Coverage note", bool(disp))
    b_ids = re.findall(r"\*\*(F\d{3}(?:-F\d{3})?)\*\*", disp.split("Class C")[0]) if disp else []
    c_ids = re.findall(r"\*\*(F\d{3}(?:-F\d{3})?)\*\*", disp.split("Class C")[1]) if "Class C" in disp else []
    def _expand(tags):
        out = []
        for t in tags:
            if "-" in t:
                a, b2 = t.split("-")
                out += [f"F{i:03d}" for i in range(int(a[1:]), int(b2[1:]) + 1)]
            else:
                out.append(t)
        return out
    B, Cc = _expand(b_ids), _expand(c_ids)
    check("class B lists IDs and class C lists IDs",
          len(B) > 0 and len(Cc) > 0, f"B={len(B)} C={len(Cc)}")
    check("every disposed ID exists in the Facts table", all(i in ids for i in B + Cc),
          str([i for i in B + Cc if i not in ids]))
    check("no ID is in both classes", not (set(B) & set(Cc)), str(sorted(set(B) & set(Cc))))
    check("no `Figure labels:` row is disposed of (it is the only thing check 6 can fail on)",
          not any(by_id_i in Cc for by_id_i in
                  [r[0] for r in rows if r[3].lower().startswith("figure labels")]),
          "class C is clean of label rows")
    m = re.search(r"\*\*Printing dispositions:\*\* (\d+) class B \(fold\) \+ (\d+) class C[^=]*= (\d+) flagged, (\d+) class A", text)
    check("header states the disposition counts", bool(m))
    if m:
        check("disposition counts match the lists",
              (int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4))) ==
              (len(B), len(Cc), len(set(B) | set(Cc)), len(rows) - len(set(B) | set(Cc))),
              f"header {m.groups()} vs lists B={len(B)} C={len(Cc)}")
        check("class A + B + C = total rows",
              int(m.group(4)) + int(m.group(3)) == len(rows))
    check("tick legend documents the class C sense of `x`",
          "accounted for by Rule 3" in text)

    # ---- coverage note headings (Rule 6 / Gate 3 deliverable) ---------------
    for h in ("Compression decisions", "Exercise classification", "Drift caught and fixed",
              "Figures requiring manual attention", "Color-dependent figures",
              "Source problems", "Linter verdict"):
        check(f"Coverage note carries the fixed heading '{h}'", f"**{h}.**" in text or f"**{h}**" in text)

    print("=" * 62)
    print(f"{len(CHECKS) - len(FAILS)}/{len(CHECKS)} checks passed")
    if FAILS:
        print("FAILURES:")
        for f in FAILS:
            print("  -", f)
        return 1
    print("GATE 1 VALIDATION: ALL CHECKS PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
