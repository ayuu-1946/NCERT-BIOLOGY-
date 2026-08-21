"""Session smoke test (SUPREME COMMAND PROMPT v6 §0.4) - throwaway."""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, ROOT)

from neet_template import (  # noqa: E402
    STYLES, heading, keyterm, process_flow, note, memory_aid, data_table,
    title_block, build_pdf,
)
from neet_template import figure as _shared_figure  # noqa: E402
from reportlab.platypus import Paragraph  # noqa: E402

ASSETS = os.path.join(ROOT, "notes", "class 12", "Ch11_OrganismsAndPopulations", "assets")

story = []
story += title_block("Smoke Test")
story.append(heading("11.1", "Populations", 1))
story.append(heading("11.1.1", "Population Attributes", 2))
story.append(heading("11.1.2", "Population Growth", 3, has_table=True))
story.append(Paragraph("Body text at 10.8pt for the print-legibility check.", STYLES["Body"]))
story.append(keyterm("<b>Population density</b> - designated as N."))
story.append(data_table([["Species A", "Species B", "Interaction"],
                         ["+", "+", "Mutualism"],
                         ["-", "-", "Competition"],
                         ["+", "-", "Predation"]]))
story.append(process_flow(["Lag phase", "Acceleration", "Deceleration", "Asymptote at K"]))
story.append(note("Natality and immigration raise density; mortality and emigration lower it."))
story.append(memory_aid("MICE - Mortality, Immigration, Competition, Emigration."))
story.append(_shared_figure("fig_11_3.png",
                        "Fig. 11.3 - Population growth curve: a exponential, b logistic, K carrying capacity.",
                        ASSETS))
# colour-carrying source figure (originally a full-colour photograph) - proves the
# convert("L") + autocontrast pipeline, per SUPREME COMMAND PROMPT v6 SS0.4 item 4
story.append(_shared_figure("fig_11_5.png",
                        "Fig. 11.5 - Showing bee - a pollinator on orchid flower.",
                        ASSETS))

build_pdf(os.path.join(HERE, "smoke.pdf"), story, title="Smoke Test")
