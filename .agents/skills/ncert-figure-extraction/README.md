# ncert-figure-extraction

An [Agent Skill](https://agentskills.io) for extracting figures from NCERT
chapter PDFs into cropped PNG assets — hand-pinned bounding boxes off a grid
overlay, audited three ways (text-layer grazing, drawings-extent overflow,
border-band ink) so nothing bleeds in and nothing gets clipped.

[![skills.sh](https://skills.sh/b/ayuu-1946/ncert-figure-extraction)](https://skills.sh/ayuu-1946/ncert-figure-extraction)

## Install

```bash
npx skills add ayuu-1946/ncert-figure-extraction
```

## What it does

See [SKILL.md](./SKILL.md) for the full workflow: grid-overlay rendering,
rect pinning, the three-part audit script, and the visual-confirmation step.
