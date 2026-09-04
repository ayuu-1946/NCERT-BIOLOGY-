#!/usr/bin/env python3
"""
build_question_prompt.py — assemble a ready-to-paste NEET question-generation
prompt for one chapter, with zero manual copy-pasting of source text.

It does what the user should NOT have to do by hand:
  1. Locates the chapter's frozen Facts inventory (the verified NCERT source
     text ledger — not the raw PDF, not model memory).
  2. Locates the registry-listed "bridge" chapters for cross-chapter items
     and pulls their Facts tables too.
  3. Loads NEET_QUESTION_GENERATION_PROMPT.md, fills in {{CLASS}}/{{CHAPTER}}/
     {{COUNT}}, and appends a SUPPLIED NCERT SOURCE TEXT section built from
     the Facts tables above.
  4. Writes the assembled, ready-to-paste prompt to
     scratch/question_prompts/<chapter>_prompt.md.

Usage:
    python3 scripts/build_question_prompt.py --class 11 --chapter Ch4 --count 45
    python3 scripts/build_question_prompt.py --class 11 --chapter AnimalKingdom
    python3 scripts/build_question_prompt.py --class 12 --chapter Ecosystem --count 60

The --chapter argument matches by substring (case-insensitive) against the
chapter directory name, e.g. "Ch4", "Ch4_AnimalKingdom", "AnimalKingdom",
"animal kingdom" (spaces are ignored) all resolve to the same chapter.
"""

import argparse
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PROMPT_TEMPLATE = REPO_ROOT / "NEET_QUESTION_GENERATION_PROMPT.md"
OUTPUT_DIR = REPO_ROOT / "scratch" / "question_prompts"

# ---------------------------------------------------------------------------
# Cross-chapter bridge registry — mirrors the APPENDIX in
# NEET_QUESTION_GENERATION_PROMPT.md. Each group is a set of chapter-name
# substrings that are legitimate NCERT bridges for each other. Only chapters
# that actually exist in notes/ are ever resolved, so partially-built groups
# degrade gracefully.
# ---------------------------------------------------------------------------
BRIDGE_GROUPS = [
    # Class 11 diversity/physiology core
    {"AnimalKingdom", "BodyFluidsAndCirculation", "BreathingAndExchangeOfGases",
     "ExcretoryProductsAndTheirElimination", "Evolution"},
    {"StructuralOrganisationInAnimals", "BreathingAndExchangeOfGases"},
    {"Biomolecules", "CellTheUnitOfLife", "RespirationInPlants",
     "PhotosynthesisInHigherPlants"},
    {"PlantKingdom", "MorphologyOfFloweringPlants", "AnatomyOfFloweringPlants",
     "SexualReproductionInFloweringPlants"},
    {"CellCycleAndCellDivision", "HumanReproduction", "MolecularBasisOfInheritance"},
    {"ChemicalCoordinationAndIntegration", "NeuralControlAndCoordination",
     "ExcretoryProductsAndTheirElimination", "BodyFluidsAndCirculation"},
    # Class 12 genetics/reproduction/ecology/biotech core
    {"MolecularBasisOfInheritance", "BiotechnologyPrinciplesAndProcesses", "Evolution"},
    {"HumanReproduction", "ChemicalCoordinationAndIntegration"},
    {"SexualReproductionInFloweringPlants", "CellCycleAndCellDivision"},
    {"Ecosystem", "OrganismsAndPopulations", "BiodiversityAndConservation"},
    {"MicrobesInHumanWelfare", "BiotechnologyAndItsApplications",
     "HumanHealthAndDisease"},
    {"Evolution", "MolecularBasisOfInheritance", "AnimalKingdom", "PlantKingdom"},
]

FACTS_TABLE_RE = re.compile(
    r"^\|\s*(F\d+[a-z]?)\s*\|\s*([^|]*)\|\s*([^|]*)\|\s*(.*?)\s*\|\s*([^|]*)\|\s*$"
)


def find_chapter_dirs():
    """Return list of (class_label, chapter_dir_path) for every chapter dir."""
    dirs = []
    for class_dir in sorted((REPO_ROOT / "notes").glob("class *")):
        class_label = class_dir.name.replace("class ", "").strip()
        for ch_dir in sorted(class_dir.glob("Ch*_*")):
            if ch_dir.is_dir():
                dirs.append((class_label, ch_dir))
    return dirs


def resolve_chapter(class_arg, chapter_arg):
    """Find the single best-matching chapter dir for the given class + query."""
    query = re.sub(r"[\s_-]+", "", chapter_arg).lower()
    candidates = []
    for class_label, ch_dir in find_chapter_dirs():
        if class_arg and class_label != str(class_arg):
            continue
        name = re.sub(r"[\s_-]+", "", ch_dir.name).lower()
        if query in name:
            candidates.append((class_label, ch_dir))
    if not candidates:
        return None, None, []
    if len(candidates) > 1:
        return "AMBIGUOUS", None, candidates
    class_label, ch_dir = candidates[0]
    return class_label, ch_dir, []


def chapter_topic_name(ch_dir: Path) -> str:
    """Human-readable chapter name, e.g. Ch4_AnimalKingdom -> Animal Kingdom."""
    stem = ch_dir.name.split("_", 1)[-1] if "_" in ch_dir.name else ch_dir.name
    # Insert spaces before capitals that follow lowercase letters
    spaced = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", " ", stem)
    spaced = re.sub(r"(?<=[A-Z])(?=[A-Z][a-z])", " ", spaced)
    return spaced


def find_inventory_file(ch_dir: Path):
    matches = list(ch_dir.glob("*_inventory.md"))
    return matches[0] if matches else None


def parse_facts_table(inventory_path: Path):
    """Extract Facts rows as list of dicts: id, section, type, wording."""
    facts = []
    in_table = False
    for line in inventory_path.read_text(encoding="utf-8", errors="replace").splitlines():
        if line.strip().startswith("## Facts"):
            in_table = True
            continue
        if not in_table:
            continue
        if line.strip().startswith("| ID") or line.strip().startswith("|----"):
            continue
        m = FACTS_TABLE_RE.match(line.strip())
        if m:
            fid, section, ftype, wording, _ticked = m.groups()
            facts.append({
                "id": fid.strip(),
                "section": section.strip(),
                "type": ftype.strip(),
                "wording": wording.strip(),
            })
        elif in_table and line.strip() and not line.strip().startswith("|"):
            # Facts table ended (prose resumed after the table)
            break
    return facts


def bridges_for(ch_dir_name: str):
    """Return set of chapter-name substrings bridged to this chapter."""
    key = ch_dir_name.split("_", 1)[-1] if "_" in ch_dir_name else ch_dir_name
    linked = set()
    for group in BRIDGE_GROUPS:
        if key in group:
            linked |= (group - {key})
    return linked


def find_bridge_chapter_dirs(anchor_ch_dir: Path, all_dirs):
    linked_names = bridges_for(anchor_ch_dir.name)
    found = []
    for class_label, ch_dir in all_dirs:
        if ch_dir == anchor_ch_dir:
            continue
        key = ch_dir.name.split("_", 1)[-1] if "_" in ch_dir.name else ch_dir.name
        if key in linked_names:
            found.append((class_label, ch_dir))
    return found


def format_facts_block(label: str, facts):
    if not facts:
        return f"### {label}\n_No inventory Facts table found — chapter may not have completed Gate 1 yet._\n"
    lines = [f"### {label} — {len(facts)} supplied source facts (verbatim from NCERT, frozen inventory)"]
    for f in facts:
        lines.append(f"- **{f['id']}** [{f['section']}] ({f['type']}): {f['wording']}")
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--class", dest="class_arg", required=True, help='e.g. "11" or "12"')
    parser.add_argument("--chapter", dest="chapter_arg", required=True, help='e.g. "Ch4", "AnimalKingdom"')
    parser.add_argument("--count", dest="count", default="45", help="number of questions (default 45)")
    args = parser.parse_args()

    class_label, ch_dir, ambiguous = resolve_chapter(args.class_arg, args.chapter_arg)

    if class_label == "AMBIGUOUS":
        print("Ambiguous chapter query. Matches:", file=sys.stderr)
        for cl, cd in ambiguous:
            print(f"  class {cl}: {cd.name}", file=sys.stderr)
        sys.exit(1)
    if ch_dir is None:
        print(f"No chapter found matching class={args.class_arg!r} chapter={args.chapter_arg!r}", file=sys.stderr)
        sys.exit(1)

    topic = chapter_topic_name(ch_dir)
    inventory_path = find_inventory_file(ch_dir)
    if inventory_path is None:
        print(f"Warning: no *_inventory.md found in {ch_dir}", file=sys.stderr)
        anchor_facts = []
    else:
        anchor_facts = parse_facts_table(inventory_path)

    all_dirs = find_chapter_dirs()
    bridge_dirs = find_bridge_chapter_dirs(ch_dir, all_dirs)

    source_sections = [format_facts_block(f"ANCHOR CHAPTER — Class {class_label}, {ch_dir.name} ({topic})", anchor_facts)]
    bridge_names = []
    for b_class, b_dir in bridge_dirs:
        b_inv = find_inventory_file(b_dir)
        b_facts = parse_facts_table(b_inv) if b_inv else []
        b_topic = chapter_topic_name(b_dir)
        source_sections.append(format_facts_block(f"BRIDGE CHAPTER — Class {b_class}, {b_dir.name} ({b_topic})", b_facts))
        bridge_names.append(f"Class {b_class} {b_topic}")

    if not PROMPT_TEMPLATE.exists():
        print(f"Missing template: {PROMPT_TEMPLATE}", file=sys.stderr)
        sys.exit(1)

    template = PROMPT_TEMPLATE.read_text(encoding="utf-8")
    filled = (
        template
        .replace("{{CLASS}}", class_label)
        .replace("{{CHAPTER}}", f"{ch_dir.name} ({topic})")
        .replace("{{COUNT}}", str(args.count))
    )

    source_block = (
        "\n\n---\n\n"
        "## SUPPLIED NCERT SOURCE TEXT (auto-assembled — this is the only text you may use as fact ground truth)\n\n"
        f"Anchor chapter: **Class {class_label} — {ch_dir.name} ({topic})**. "
        f"Bridge chapters supplied for cross-chapter items: {', '.join(bridge_names) if bridge_names else 'none found in registry — Tier-2/3 items must stay within the anchor chapter, or flag any link as UNGROUNDED.'}\n\n"
        + "\n".join(source_sections)
    )

    assembled = filled + source_block

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    out_path = OUTPUT_DIR / f"{ch_dir.name}_prompt.md"
    out_path.write_text(assembled, encoding="utf-8")

    print(f"Chapter resolved: Class {class_label} — {ch_dir.name} ({topic})")
    print(f"Anchor facts supplied: {len(anchor_facts)}")
    print(f"Bridge chapters found: {len(bridge_dirs)} -> {', '.join(bridge_names) if bridge_names else '(none)'}")
    print(f"Assembled prompt written to: {out_path.relative_to(REPO_ROOT)}")
    print("Paste that file's contents directly into the model. Nothing else to attach.")


if __name__ == "__main__":
    main()
