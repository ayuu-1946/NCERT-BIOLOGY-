# Ch5 Gate 3a — per-asset visual audit (all 18 assets, opened by eye)

Session: resumed Gate 3a. Environment rebuilt per §0.2 (venv absent at start,
as expected). Gate 2 independently re-derived: `check_pdf.py --strict` = **PASS,
0 fail / 0 warn**, 31 pages, 646/646 rows ticked, 136/136 labels, 18/18 mono.

**Method** — every asset was OPENED and looked at (§4.4 Step 3). Two automated
detectors were written first and both proved unreliable; they are kept only as
recorded negative results, not as evidence:

- `audit_watermark.py` (v1) hunted the watermark in the **source text layer**.
  It found only the `Reprint 2026-27` footer at y 754.8–765.7, which no crop
  rect reaches (lowest rect bottom = y712), and therefore concluded "no
  watermark anywhere." **Direct inspection of fig_5_5 immediately disproved
  this.** The real watermark is a vector/graphic overlay with no text span —
  invisible to text extraction. This is exactly the silent-failure class §4.4
  warns about; it is why the label harvest must open images too.
- `audit_watermark2.py` (v2) ranked assets by mid-grey mass. It ranks
  **fig_5_5 LOW (0.003)** — the single most severely watermarked asset — and
  fig_5_4b HIGHEST purely because it is a greyscale micrograph. The metric
  tracks shading, not watermarks. **Rejected as evidence.**

Conclusion carried forward as a rule: **watermark presence is decidable only by
looking at the image.** Do not re-derive it statistically.

---

## Watermark census — 17 of 18 assets affected

| Asset | Page | Watermark | Severity (legibility impact) | Baked border |
|---|---|---|---|---|
| fig_5_1 | p2 | YES — "not" upper-left | light | no |
| fig_5_2 | p4 | YES — faint, lower-right | light | no |
| fig_5_3 | p4 | YES — "© NCERT / not to be re…" across full plate | **severe** | no |
| fig_5_central_dogma | p4 | **NO — clean** | — | no |
| fig_5_4a | p5 | YES — "…ed" right side, over H1 histone | moderate | no |
| fig_5_4b | p5 | YES — top + left edges | light | **YES** (frame) |
| fig_5_5 | p8 | YES — "© NCERT / not to be republished" diagonal, full plate | **severe** | no |
| fig_5_6 | p10 | YES — right side, over helix | moderate | **YES** (frame) |
| fig_5_7 | p11 | YES — "© NCERT / not to be repu…" across centre | **severe** | **YES** (frame) |
| fig_5_8 | p13 | YES — lower-right, over "3'" label region | moderate | no |
| fig_5_9 | p14 | YES — "NCERT / republish" across plate | **severe** | **YES** (frame) |
| fig_5_10 | p15 | YES — "not to be" left/centre | moderate | no |
| fig_5_11 | p16 | YES — "© NCERT / not to be rep" left side | **severe** | no |
| fig_5_12 | p20 | YES — "NCERT / publish" right side | moderate | no |
| fig_5_13 | p21 | YES — faint, lower-right | light | no |
| fig_5_14 | p23 | YES — "RT / lished" right side | moderate | no |
| fig_5_15 | p25 | YES — upper-left corner | light | no |
| fig_5_16 | p29 | YES — "© NCERT / to be republished" across gel | **severe** | no |

**Totals: 17/18 watermarked (94%); 1 clean (fig_5_central_dogma).**
Severity: 6 severe, 6 moderate, 5 light.
**Baked borders: 4** — fig_5_4b, fig_5_6, fig_5_7, fig_5_9.

### Correction to the inherited handoff (§5)

The handoff reported the double-border defect on **p10, p11, p14** =
fig_5_6, fig_5_7, fig_5_9. Re-derivation confirms those three **and adds a
fourth it missed: fig_5_4b (p5)**. The handoff's watermark claim is otherwise
confirmed and extends further than it had verified: it had checked
fig_5_1..fig_5_10 and *assumed* 5.11–5.16 likely carried it. All six are now
confirmed affected, and the one genuinely clean asset (central dogma) was not
in its list at all.

---

## New findings this session (not in any prior handoff)

### N1 — fig_5_15 embeds a drawn human figure (needs a ruling, NOT auto-fixed)
`fig_5_15` (Human Genome Project montage, p25) includes a **drawn/illustrated
portrait of a girl's face and torso** as the first element of the montage.

- §4.4 hard no and §5 item 3 ban **photographs** of a person, and `check_pdf.py`
  check 4 gates manifest *portrait/photo* rows. This is a **line illustration,
  not a photograph**, and it is an integral part of an NCERT figure the chapter
  is required to reproduce (Rule 1: every figure).
- Check 4 legitimately did **not** fire here — recording that explicitly per
  §Pass 3 ("note where a check legitimately does not fire so a true negative is
  never later mistaken for a suppressed finding").
- **Not resolved unilaterally.** Reading the ban as covering drawn people would
  require dropping or altering a required NCERT figure, which Rule 5 forbids.
  Escalated as an open question rather than actioned either way.

### N2 — raw Greek beta inside fig_5_14 artwork
`fig_5_14` shows "β-galactosidase" as pixels **inside the plate**. Same class as
the σ/ρ glyphs inside fig_5_10 that the prior session cleared: artwork content,
not the PDF text stream, so `check_pdf.py` check 5 correctly does not fire and
this is **not** a defect. Logged so a later session does not "discover" it as a
check-5 violation and try to fix a picture.

---

## Root cause of the watermark defect

Not a cropping error — the watermark is printed **across the artwork itself** on
every source page, so no bounding box can exclude it. Tightening rects (the
handoff's speculated fix) **cannot** work: the overlay sits under and across the
diagram, not beside it. Any real fix is a pixel-level removal/attenuation step
added after the clip render, and it must not damage artwork strokes or labels.
Deciding and implementing that is a **fix pass**, not this audit pass.
