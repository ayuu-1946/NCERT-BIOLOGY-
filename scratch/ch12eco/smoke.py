"""SS0.4 smoke test for the Ecosystem session.

Builds a throwaway 1-page PDF *by importing neet_template.py* (never re-declaring
styles), exercising: H1/H2/H3 banners + section badges, a canonical data_table,
every icon badge, a process_flow with >=3 steps, NOTE + MEMORY AID boxes, and one
REAL NCERT figure (Fig 12.4 a - pyramid of numbers) pushed through the full SS4.4
pipeline: clip-render at 300 dpi -> convert("L") -> autocontrast -> bordered box.

Fig 12.4(a) is deliberately chosen because it uses COLOUR to carry meaning: each
trophic level's bar is a different hue (olive P / blue PC / pink SC / orange TC).
A figure that was never coloured would prove nothing about the conversion.
"""
import os
import sys

import pymupdf
from PIL import Image as PILImage, ImageOps, ImageChops
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle
from reportlab.lib.units import cm

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = HERE
while not os.path.exists(os.path.join(ROOT, "neet_template.py")):
    ROOT = os.path.dirname(ROOT)
sys.path.insert(0, ROOT)

from neet_template import (  # noqa: E402
    STYLES,
    heading, keyterm, process_flow, note, memory_aid, data_table,
    title_block, build_pdf,
)
from neet_template import figure as _shared_figure  # noqa: E402
from neet_template import (  # noqa: E402
    _badge_section, _icon_definition, _icon_table, _icon_star, _icon_note, _step_badge,
)

SRC = os.path.join(ROOT, "Chapter", "class 12", "Chapter 12 - Ecosystem.pdf")
ASSETS = os.path.join(HERE, "smoke_assets")
OUT_PDF = os.path.join(HERE, "smoke.pdf")
os.makedirs(ASSETS, exist_ok=True)


# ---------------------------------------------------------------- SS4.4 pipeline
def extract_mono(page_index, clip, out_name, dpi=300):
    """Clip-render a figure region, convert to TRUE monochrome, autocontrast, save."""
    doc = pymupdf.open(SRC)
    page = doc[page_index]
    pix = page.get_pixmap(dpi=dpi, clip=pymupdf.Rect(*clip))
    raw = os.path.join(ASSETS, "_raw_" + out_name)
    pix.save(raw)
    doc.close()

    colour = PILImage.open(raw).convert("RGB")
    # Prove the SOURCE clip really carries colour (else the test is vacuous).
    r, g, b = colour.split()
    chroma = max(
        ImageChops.difference(r, g).getextrema()[1],
        ImageChops.difference(g, b).getextrema()[1],
    )
    mono = ImageOps.autocontrast(colour.convert("L"))
    out_path = os.path.join(ASSETS, out_name)
    mono.save(out_path)
    print("[smoke] source clip max chroma delta =", chroma, "(must be > 0 to be a fair test)")
    assert chroma > 0, "chosen smoke figure carries no colour - pick another"
    return out_path


CLIP_124A = (95, 176, 505, 348)   # Fig 12.4 (a), page 8 (0-indexed 7)
fig_path = extract_mono(7, CLIP_124A, "fig_12_4a.png")

check = PILImage.open(fig_path)
print("[smoke] embedded figure mode =", check.mode, "size =", check.size)
assert check.mode == "L", "figure is not single-channel greyscale"


def figure(asset_name, caption_text, max_width_cm=15.9):
    return _shared_figure(asset_name, caption_text, ASSETS, max_width_cm=max_width_cm)


# ---------------------------------------------------------------- story
story = []
story += title_block("Smoke Test - Ecosystem Session")
story.append(Spacer(1, 6))

story.append(heading("12.1", "ECOSYSTEM - STRUCTURE AND FUNCTION", 1))
story.append(Paragraph(
    "Body text at 10.8pt. Species composition and <b>stratification</b> are the two main "
    "structural features. Expressed as gm<super>-2</super> yr<super>-1</super> for "
    "<i>Homo sapiens</i>. GPP - R = NPP.", STYLES["Body"]))

story.append(heading("12.2", "Productivity", 2))
story.append(keyterm(
    "<b>Gross primary productivity (GPP)</b> - rate of production of organic matter "
    "during photosynthesis."))
story.append(heading("12.2.1", "Net primary productivity", 3))
story.append(Paragraph("Sub-sub-section body line.", STYLES["Body"]))

story.append(Spacer(1, 4))
story.append(data_table([
    ["Type", "Definition", "Value"],
    ["GPP", "Rate of organic matter production", "N/A"],
    ["NPP", "GPP minus respiration losses", "170 billion tons"],
    ["Ocean NPP", "Productivity of the oceans", "55 billion tons"],
    ["Land NPP", "Remainder, on land", "115 billion tons"],
]))

story.append(Spacer(1, 6))
story.append(process_flow([
    "<b>Fragmentation</b> - detritivores break detritus into smaller particles.",
    "<b>Leaching</b> - water-soluble inorganic nutrients go down into the soil horizon.",
    "<b>Catabolism</b> - bacterial and fungal enzymes degrade detritus.",
    "<b>Humification</b> - accumulation of humus.",
    "<b>Mineralisation</b> - humus degraded, inorganic nutrients released.",
], cyclic=True))

story.append(Spacer(1, 6))
story.append(note("All the steps in decomposition operate simultaneously on the detritus."))
story.append(Spacer(1, 5))
story.append(memory_aid("SMOKE ONLY - Fragment, Leach, Catabolise, Humify, Mineralise."))

story.append(Spacer(1, 8))
story.append(Paragraph("Icon row (each must be distinct at print size):", STYLES["Body"]))
icons = Table(
    [[_badge_section("12.1", 13.5), _badge_section("12.4.2", 11.5), _icon_definition(),
      _step_badge(1), _step_badge(9), _icon_table(), _icon_star(), _icon_note()]],
    colWidths=[1.6 * cm, 1.9 * cm] + [1.1 * cm] * 6,
)
icons.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "MIDDLE")]))
story.append(icons)

story.append(Spacer(1, 8))
story.append(figure(
    "fig_12_4a.png",
    "Figure 12.4 (a) Pyramid of numbers in a grassland ecosystem. Only three "
    "top-carnivores are supported in an ecosystem based on production of nearly "
    "6 millions plants",
    max_width_cm=13.0))

build_pdf(OUT_PDF, story, title="Smoke Test - Ecosystem Session")

# ---------------------------------------------------------------- render + B&W check
doc = pymupdf.open(OUT_PDF)
print("[smoke] pages:", doc.page_count)
for i, page in enumerate(doc):
    page.get_pixmap(dpi=200).save(os.path.join(HERE, "smoke_p%d.png" % (i + 1)))
    page.get_pixmap(dpi=300).save(os.path.join(HERE, "smoke_p%d_300.png" % (i + 1)))
    PILImage.open(os.path.join(HERE, "smoke_p%d_300.png" % (i + 1))).convert("L").point(
        lambda p: 255 if p > 190 else 0
    ).save(os.path.join(HERE, "smoke_p%d_bw.png" % (i + 1)))

for pno in range(doc.page_count):
    for img in doc[pno].get_images(full=True):
        pix = pymupdf.Pixmap(doc, img[0])
        print("[smoke] embedded image xref=%s n=%s colorspace=%s" % (img[0], pix.n, pix.colorspace))
doc.close()
print("[smoke] done")
