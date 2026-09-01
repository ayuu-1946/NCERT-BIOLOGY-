"""Gate 3 condition 5 (reproducibility) + Gate 3(b) reading material dump.

Rebuilds the PDF from the committed script into a scratch copy of the chapter
folder (so the committed deliverable is never touched), compares content
fingerprints, and dumps the full source text layer page by page for the
bidirectional read.
"""
import hashlib
import os
import re
import shutil
import subprocess
import sys

import pymupdf

REPO = "/vercel/share/v0-project"
CH = os.path.join(REPO, "notes/class 11/Ch19_ChemicalCoordinationAndIntegration")
NAME = "Ch19_ChemicalCoordinationAndIntegration"
SRC = os.path.join(REPO, "Chapter/class 11/Chapter 19 - Chemical Coordination and Integration.pdf")
WORK = os.path.join(REPO, "scratch/ch19_gate3b/rebuild")


def fp(path):
    doc = pymupdf.open(path)
    text = "".join(p.get_text() for p in doc)
    out = dict(
        pages=doc.page_count,
        chars=len(text),
        images=sum(len(p.get_images(full=True)) for p in doc),
        sha=hashlib.sha256(text.encode()).hexdigest()[:16],
    )
    doc.close()
    return out


def main():
    if "--dump-only" not in sys.argv:
        print("== REPRODUCIBILITY ==")
        if os.path.exists(WORK):
            shutil.rmtree(WORK)
        os.makedirs(WORK)
        shutil.copy(os.path.join(CH, NAME + ".py"), WORK)
        shutil.copytree(os.path.join(CH, "assets"), os.path.join(WORK, "assets"))
        shutil.copy(os.path.join(REPO, "neet_template.py"), WORK)
        r = subprocess.run([sys.executable, NAME + ".py"], cwd=WORK,
                           capture_output=True, text=True)
        print("  rc:", r.returncode)
        if r.returncode:
            print(r.stdout[-2000:], r.stderr[-2000:])
            return
        committed = fp(os.path.join(CH, NAME + ".pdf"))
        rebuilt = fp(os.path.join(WORK, NAME + ".pdf"))
        print("  committed:", committed)
        print("  rebuilt  :", rebuilt)
        print("  CONTENT-IDENTICAL:", committed == rebuilt)

    print("\n== SOURCE TEXT DUMP ==")
    doc = pymupdf.open(SRC)
    for i, page in enumerate(doc, 1):
        txt = page.get_text()
        out = os.path.join(REPO, f"scratch/ch19_gate3b/src_p{i:02d}.txt")
        with open(out, "w", encoding="utf-8") as f:
            f.write(txt)
        print(f"  p{i:02d}: {len(txt)} chars -> {os.path.basename(out)}")
    doc.close()


if __name__ == "__main__":
    main()
