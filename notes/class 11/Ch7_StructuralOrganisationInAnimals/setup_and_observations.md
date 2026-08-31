# Chapter 7 extraction setup and observations

The repository skill was installed with `npx skills add ayuu-1946/ncert-figure-extraction --agent codex --yes` after the installer’s interactive agent-selection prompt was handled non-interactively. The active interpreter is Python 3.12.3 in the writable `/home/ubuntu` environment. Verified packages: PyMuPDF 1.28.2, Pillow 12.3.0, NumPy 2.5.1, pdfplumber, and ReportLab 5.0.0. The project directory is writable.

Source PDF: `Chapter/class 11/Chapter 07 - Structural Organisation in Animals.pdf`; 19 pages. Artwork pages identified from the PDF text layer: 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, and 16. Mandatory 440-dpi, 5-point grid overlays were rendered under `scratch/ch7_figs/grid_4x/`; the page contact sheet is `scratch/ch7_figs/page_contact_sheet.png`.

Visual observation from PDF page 2: Figure 7.1 is a single four-panel composition with panels (a), (b), (c), and (d), plus the in-figure labels “Flattened cell”, “Cube-like cell”, and “Tall cell”. All four panels and labels remain in one crop; the crop stops before the printed caption and following prose. The high-density grid is the source of truth for final rectangle pinning. The final assets use 600 DPI, minimal whitespace, and strictly visible labels.

Visual observation from PDF page 3: Figure 7.2 is the upper-left two-panel glandular epithelium composition; it contains labels “unicellular gland” and “Multicellular gland” and panel markers (a)/(b). Figure 7.3 is the lower-left compound epithelium diagram with label “Multi-layered cells”. Both are cropped as complete artwork without the adjacent right prose column or printed captions, using approximately 10 pt safety margins.
