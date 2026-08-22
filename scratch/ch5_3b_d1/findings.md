# Gate 3b Direction 1 — figure-label rows traced to source (visual)

Method: crop each figure's pinned rect from the SOURCE pdf (+8pt margin) at 300 dpi,
read every printed label off the artwork, compare against the inventory's rows for
that figure. In-figure labels are vector art, so this is the only possible method.

Inventory is FROZEN: findings are FLAGGED here, rows are not edited.

| Figure | rows | verdict |
|---|---|---|
| Fig 5.1 | F511-F516 (6) | CONFIRMED (previous session) |
| Fig 5.2 | F517-F523 (7) | CONFIRMED — 5', 3', hydrogen bonds, A, T, G, C all printed |
| Fig 5.3 | F524-F533 (10) | **DEFECT — see D1-1** |
| Fig 5.4a | F534-F537 (4) | CONFIRMED — DNA, H1 histone, Histone octamer, Core of histone molecules |
| Fig 5.5 | F538-F547 (10) | CONFIRMED — all 10 printed (source capitalises "No Radioactive"; immaterial) |

## D1-1 — Fig 5.3 rows include four labels that belong to a different figure

Fig 5.3 (p4, DNA double helix) prints exactly **six** labels:
Base pairs, Adenine, Thymine, Guanine, Cytosine, Sugar phosphate backbone
= F524-F529. Those six are CONFIRMED.

F530 "Central dogma", F531 "DNA", F532 "RNA", F533 "Protein" are **not on Fig 5.3's
artwork at all**. They belong to the *unnumbered* central-dogma plate lower on p4
(shipped as `fig_5_central_dogma.png`). The `1-F` session had no figure number to
file them under and parked them on the nearest numbered figure.

Consequence: the inventory's own count "Fig 5.3: 10 labels" is wrong, and the
unnumbered plate appears to have zero label rows when it actually has rows — they
are just mis-sectioned. Not a content loss; a section-attribution defect.

## D1-2 — F532 "RNA" is a wording drift; the plate prints "mRNA"

The central-dogma plate prints, verbatim:
`replication`, `DNA`, `transcription`, `mRNA`, `translation`, `protein`, `Central dogma`.

- F531 "DNA" — ok
- F532 "RNA" — **source prints `mRNA`**, not `RNA`. Real drift, exam-relevant
  (the central dogma's middle term being mRNA specifically is the point).
- F533 "Protein" — source prints lowercase `protein`; immaterial.

## D1-3 — three plate labels have no inventory row (Direction-2 class)

`replication`, `transcription`, `translation` are printed labels on the
central-dogma plate with **no** corresponding `figure-label` row anywhere in
F511-F646. Uninventoried figure content.
