# Requested asset reformat observations

The inspected source assets showed the following layouts: Figure 7.14 is a broad cockroach external-anatomy plate with a residual prose strip at the top; Figures 7.17 and 7.20 are tall labeled plates; Figure 7.18 contains vertically arranged male and female panels; Figure 7.5 contains two vertically arranged dense-connective-tissue panels; Figure 7.6 contains cartilage and bone above blood. The reformat script crops the unwanted prose/margins, horizontally stacks the two-part plates, keeps the labels and panel markers, and writes Figure 7.6(c) to `fig_7_6c.png` while leaving `(a)+(b)` together in `fig_7_6.png`.

The output dimensions confirm the intended horizontal layouts: 7.18 = 6303x1843, 7.17 = 2815x1266, 7.20 = 5672x1381, 7.5 = 3125x1551, 7.6(a+b) = 3270x1116, and 7.6(c) = 1430x967. Figure 7.14 is trimmed to 3792x1749.

Follow-up visual review found that the first Figure 7.18 recomposition clipped the upper Titillator marker and left-side female labels. The corrected pass re-renders the source PDF directly for each half with overlap margins and avoids trimming label-bearing edges.

The source-direct Figure 7.18 stack restored the Titillator marker but still clipped the left female-panel label because the right half inherited the original narrow x-boundary. Figure 7.17 also clipped the right-side label text at x=475. The next pass expands the female half leftward and both Figure 7.17 halves rightward to the page-safe boundary.
