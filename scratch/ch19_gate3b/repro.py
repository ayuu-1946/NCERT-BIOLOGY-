"""Rebuild Ch19 from the COMMITTED script in an isolated copy and compare with
the committed PDF. Never rebuild in place: a failed rebuild must not be able to
destroy the committed artefact.

Also tests the specific hypothesis for the stale Gate 2 fingerprint:
  31,137 (Gate 2 record) + 12 == 31,149 (now), where +12 is exactly the two
  Pass 3(a) D1 string fixes  "SS19.2"->"Section 19.2"  and
  "SS19.2.5"->"Section 19.2.5"  (+6 chars each).
"""
import hashlib
import os
import shutil
import subprocess
import tempfile

import pymupdf

REPO = "/vercel/share/v0-project"
CHDIR = os.path.join(REPO, "notes/class 11/Ch19_ChemicalCoordinationAndIntegration")
NAME = "Ch19_ChemicalCoordinationAndIntegration"
PY = os.path.join(CHDIR, NAME + ".py")
PDF = os.path.join(CHDIR, NAME + ".pdf")


def fingerprint(path):
    doc = pymupdf.open(path)
    text = "".join(p.get_text() for p in doc)
    fp = dict(
        pages=doc.page_count,
        chars=len(text),
        images=sum(len(p.get_images(full=True)) for p in doc),
        sha=hashlib.sha256(text.encode()).hexdigest()[:16],
        sizes=sorted({(round(p.rect.width), round(p.rect.height)) for p in doc}),
    )
    doc.close()
    return fp


committed = fingerprint(PDF)
committed_bytes = hashlib.sha256(open(PDF, "rb").read()).hexdigest()[:16]

work = tempfile.mkdtemp(prefix="ch19_repro_")
dest = os.path.join(work, "chapter")
shutil.copytree(CHDIR, dest)
os.remove(os.path.join(dest, NAME + ".pdf"))          # force a real build
# the script imports the repo-level template, so run with REPO on the path
env = dict(os.environ, PYTHONPATH=REPO)
res = subprocess.run(["/vercel/share/neetenv/bin/python", NAME + ".py"],
                     cwd=dest, capture_output=True, text=True, env=env)
print("build exit:", res.returncode)
if res.returncode != 0:
    print("STDOUT:", res.stdout[-2000:])
    print("STDERR:", res.stderr[-3000:])
    raise SystemExit("rebuild failed — cannot assert reproducibility")

rebuilt_path = os.path.join(dest, NAME + ".pdf")
rebuilt = fingerprint(rebuilt_path)

print()
print(f"{'field':10} {'committed':>22} {'rebuilt':>22}  match")
for k in ("pages", "chars", "images", "sha", "sizes"):
    a, b = committed[k], rebuilt[k]
    print(f"{k:10} {str(a):>22} {str(b):>22}  {'OK' if a == b else 'DIFFER'}")

identical = all(committed[k] == rebuilt[k] for k in committed)
print()
print("CONTENT-IDENTICAL:" , "YES" if identical else "NO")
print("committed PDF byte SHA[:16]:", committed_bytes,
      "(unchanged on disk:", hashlib.sha256(open(PDF, 'rb').read()).hexdigest()[:16] == committed_bytes, ")")

print()
print("--- stale-fingerprint hypothesis ---")
print("Gate 2 record chars: 31137   now:", committed["chars"],
      "  delta:", committed["chars"] - 31137)
print("two Pass 3(a) D1 fixes add: len('Section 19.2')-len('SS19.2') +"
      " len('Section 19.2.5')-len('SS19.2.5') =",
      (len("Section 19.2") - len("SS19.2")) + (len("Section 19.2.5") - len("SS19.2.5")))
print("hypothesis holds:",
      committed["chars"] - 31137 == (len("Section 19.2") - len("SS19.2"))
      + (len("Section 19.2.5") - len("SS19.2.5")))
# the leaked token must be gone from the delivered text
doc = pymupdf.open(PDF)
delivered = "".join(p.get_text() for p in doc)
doc.close()
print("literal 'SS19.' still in delivered text:", "SS19." in delivered)
print("'Section 19.2 uses them' present:", "Section 19.2 uses them" in delivered.replace("\n", " "))

shutil.rmtree(work, ignore_errors=True)
