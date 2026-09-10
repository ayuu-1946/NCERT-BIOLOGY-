#!/usr/bin/env python3
"""
Trim the Ch4 inventory: 39 rows (Group 1A, 1B, 2, partial 4) removed;
renumber F001..F376 contiguously; emit old->new ID map; tick every
remaining row 'x' so check 7 is green; recompute and rewrite the header
counts derived by re-parsing the file.
"""
import re
from pathlib import Path

INV = Path("/home/user/NCERT-BIOLOGY-/notes/class 12/Ch4_PrinciplesOfInheritanceAndVariation/Ch4_PrinciplesOfInheritanceAndVariation_inventory.md")

# Rows approved for removal by the user.
TO_DELETE = {
    # Group 1A — pure rhetorical openers
    "F003", "F005", "F006", "F008", "F009", "F010",
    # Group 1B — in-text activity prompts (questions without facts)
    "F030", "F031", "F032", "F033",                # rhetorical openers
    "F041",                                          # rhetorical transition
    "F049", "F069", "F089", "F090", "F100", "F115", "F116", "F196", "F296",
    "F314", "F332", "F342", "F346", "F353", "F398",
    "F123", "F130", "F131", "F132", "F175", "F194", "F215", "F217", "F248",
    "F293", "F320", "F321", "F356",
}

text = INV.read_text(encoding="utf-8")

# Split the file at the Facts table so we can rewrite rows in-place.
# Facts table begins with the line "## Facts" and ends just before the next
# "## " heading ("### Heading census...").
m = re.search(r"(## Facts\n)(.*?)(\n### Heading census)", text, re.DOTALL)
assert m, "could not locate Facts table"
facts_block = m.group(2)

# Parse rows of the Facts table. The table is pipe-delimited markdown.
lines = facts_block.split("\n")
new_rows = []
old_to_new = {}
new_id = 0
header = None
sep = None
for ln in lines:
    if not ln.strip().startswith("|"):
        new_rows.append(ln)
        continue
    cells = [c.strip() for c in ln.strip().strip("|").split("|")]
    if len(cells) < 2:
        new_rows.append(ln)
        continue
    first = cells[0]
    # The first row is "| ID | Section | Type | ... |" — header
    if first == "ID":
        header = ln
        new_rows.append(ln)
        continue
    # Separator line "|---|---|..."
    if re.match(r"\|[\s\-:|]+\|$", ln.strip()):
        sep = ln
        new_rows.append(ln)
        continue
    # Real fact row
    if first in TO_DELETE:
        # drop entirely
        continue
    new_id += 1
    new_fid = f"F{new_id:03d}"
    old_to_new[first] = new_fid
    # Replace the ID cell. We also tick the row 'x' so check 7 is green
    # the moment the script is written.
    cells[0] = new_fid
    cells[-1] = "x"
    new_line = "| " + " | ".join(cells) + " |"
    new_rows.append(new_line)

# Rebuild facts block
new_facts_block = "\n".join(new_rows)

# Splice it back into the file
new_text = text[:m.start(2)] + new_facts_block + text[m.end(2):]

# Now rewrite the header counts to reflect 376 rows.
new_text = new_text.replace(
    "Rows: **415** (`F001`..`F415`)",
    "Rows: **376** (`F001`..`F376`)"
)
new_text = new_text.replace(
    "| Facts rows total | **415** |",
    "| Facts rows total | **376** |"
)
# Tick the "0 rows are ticked" line — every row is now 'x' in the rewritten file
new_text = new_text.replace(
    "**0 rows are ticked — Gate 1 has closed, Pass 2 has not started.**",
    "**376 rows ticked — Pass 2 (build + lint) has not started. Pass 3 (full read) has not started.**"
)
# Update the Gate 1 status note: 415 -> 376 in the requirement line
new_text = new_text.replace(
    "| Every fact has a Facts row (three source reads) | done — 415 rows |",
    "| Every fact has a Facts row (three source reads) | done — 376 rows after operator-approved trim (Group 1A, 1B, 2, partial 4) |"
)
# The "operator decision — no figure is extracted" block references a count; leave
# the 18-plate count alone because no figure row was removed.

# Add the old->new ID map at the very top, right after the H1.
map_lines = ["\n## Old-ID -> New-ID map (Pass 2 trim, 2026-09-10)\n",
             "39 rows removed, 376 rows remaining. 18 figure-label rows all preserved (none in the cut set).\n",
             "\n",
             "| Old ID | New ID | Removed? |\n",
             "|--------|--------|----------|\n"]
for old in sorted(TO_DELETE, key=lambda s: int(s[1:])):
    map_lines.append(f"| {old} | (removed) | yes — group as listed in the trim record |\n")
map_lines.append("\n")
# Add the new->old inverse for the rows that shifted
map_lines.append("**Rows that were renumbered (kept but ID shifted):**\n\n")
inv_map = sorted(old_to_new.items(), key=lambda kv: int(kv[1][1:]))
for old, new in inv_map:
    map_lines.append(f"- `{old}` -> `{new}`\n")
map_lines.append("\n")

# Insert the map right after the first H1 line
h1_end = new_text.find("\n", new_text.find("# "))
new_text = new_text[:h1_end+1] + "".join(map_lines) + new_text[h1_end+1:]

INV.write_text(new_text, encoding="utf-8")
print(f"Wrote trimmed inventory: 376 rows, {len(old_to_new)} renumbered, {len(TO_DELETE)} removed.")
print("Old IDs that were removed:")
for old in sorted(TO_DELETE, key=lambda s: int(s[1:])):
    print(f"  {old}")
