"""Labels harvested by OPENING each asset in notes/class 11/Ch16.../assets/ and reading it.

Not from the PDF text layer: Ch16 is a two-column layout whose figure labels are vector
artwork, and pdfplumber interleaves Fig 16.4's labels into page 4's prose (verified).
Apostrophes are recorded exactly as drawn -- the source mixes curly and straight within
the same chapter, and even within Fig 16.3.
"""

LABELS = {
    "Fig 16.1": [
        "Inferior vena cava", "Adrenal gland", "Renal artery", "Renal vein",
        "Pelvis", "Kidney", "Medulla", "Cortex", "Dorsal aorta", "Ureter",
        "Urinary bladder", "Urethra",
    ],
    "Fig 16.2": [
        "Medullary pyramid", "Renal column", "Calyx", "Renal artery",
        "Renal vein", "Renal pelvis", "Ureter", "Cortex", "Renal capsule",
    ],
    # Fig 16.3 draws "Henle's loop" with a STRAIGHT apostrophe but
    # "Bowman's capsule" with a curly one. Both recorded as drawn.
    "Fig 16.3": [
        "Afferent arteriole", "Efferent arteriole", "Glomerulus",
        "Bowman\u2019s capsule", "Proximal convoluted tubule",
        "Distal convoluted tubule", "Descending limb of loop of Henle",
        "Ascending limb of loop of Henle", "Henle's loop", "Vasa recta",
        "Collecting duct",
    ],
    "Fig 16.4": [
        "Afferent arteriole", "Efferent arteriole", "Bowman\u2019s capsule",
        "Proximal convoluted tubule",
    ],
    "Fig 16.5": [
        "Proximal convoluted tubule", "Distal convoluted tubule", "Cortex",
        "Medulla", "HCO3-", "NaCl", "Nutrients", "H2O", "K+", "H+", "NH3",
        "Descending limb of loop of Henle", "Thick segment of ascending limb",
        "Thin segment of ascending limb", "Collecting duct", "Urea",
    ],
    # Fig 16.6 draws "Bowman's capsule" with a STRAIGHT apostrophe.
    "Fig 16.6": [
        "Afferent arteriole", "Efferent arteriole", "Bowman's capsule",
        "Glomerulus", "Cortex", "Outer medulla", "Inner medulla", "H2O",
        "NaCl", "Urea", "Vasa recta", "Nephron",
        "300 mOsmolL-1", "600 mOsmolL-1", "900 mOsmolL-1", "1200 mOsmolL-1",
        "200", "300", "400", "600", "800", "900", "1000", "1200",
    ],
}

if __name__ == "__main__":
    total = sum(len(v) for v in LABELS.values())
    for fig, labs in LABELS.items():
        dupes = [l for l in set(labs) if labs.count(l) > 1]
        assert not dupes, f"{fig} has duplicate labels: {dupes}"
        print(f"{fig}: {len(labs)}")
    print(f"TOTAL: {total} labels across {len(LABELS)} figures")
