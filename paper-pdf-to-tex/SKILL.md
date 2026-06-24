---
name: paper-pdf-to-tex
description: Convert journal article PDFs into a single LaTeX .tex source by rendering the PDF to page images first, visually recognizing each page image, writing page-level LaTeX, and pasting all page LaTeX into one master .tex file. Use when the user asks to convert an academic or journal paper PDF to TeX/LaTeX while preserving text, equations, symbols, table structure, figure captions, figure references, and figure placeholders. Do not use text extraction, embedded PDF text, OCR-to-txt pipelines, existing PDF/document conversion skills, or \input-based assembly for this workflow.
---

# Paper PDF to TeX

## Core Rule

Convert from images only. Never rely on embedded PDF text, copied selectable text, text-layer extraction, `pdftotext`, OCR-to-plain-text output, or existing PDF/document conversion skills. Render the PDF into one image per page, inspect each image, convert each page into LaTeX, then paste the page LaTeX blocks into one final `.tex` file.

Use `scripts/render_pdf_pages.py` to create page images when useful. Read `references/latex-conventions.md` before writing the final `.tex`.

## Workflow

1. Create a working directory next to the input PDF or in the user's requested output folder.
2. Render the PDF to page images at 300-400 DPI. Prefer PNG. Use `scripts/render_pdf_pages.py` or another image-rendering method, but keep the source of truth as images.
3. Review page images in order. For each page, create a page-level LaTeX block from visual recognition of the image.
4. Remove unnecessary running headers, footers, standalone page numbers, publisher watermarks, download banners, and repeated journal metadata unless they are part of the article content.
5. Preserve article title, author line, abstract, keywords, section headings, body text, citations, footnotes/endnotes visible in the paper, equation references, figure references, table references, acknowledgements, appendices, and references if visible. Do not convert in-text citations into LaTeX citation commands such as \cite{}, \citep{}, or \citet{}; transcribe them as visible author-year prose, e.g. `(Aldy et al., 2008)` or `Newell and Pizer (2008)`.
6. Preserve figure mentions in the body. Preserve figure captions and notes. Replace each actual figure graphic with a compact blank placeholder image command or boxed placeholder, not with omitted content. Default boxed placeholders should be small, about `1.15in` high and `0.68\linewidth` wide, unless the user asks for a different size.
7. Convert tables into LaTeX tables, using `tabular`, `tabularx`, `longtable`, or `threeparttable` as appropriate. Do not replace tables with images.
8. Convert mathematical notation carefully. For this skill, wrap inline mathematical symbols and formulas with `$...$` according to the user's requested convention. Use `\begin{equation}...\end{equation}` for numbered display equations.
9. Paste all page-level LaTeX directly into one master `.tex` file. Do not assemble with `\input`, `\include`, external fragment files, or generated include directives.
10. Compile or syntax-check the final `.tex` when a LaTeX engine is available. Fix obvious escaping, table alignment, math delimiter, and environment errors.

## Page Conversion

For each rendered page image:

- Work top to bottom and left to right, respecting multi-column layout.
- Mark page boundaries in comments only while drafting, then remove page comments from the final `.tex` unless the user asks to keep them.
- Join hyphenated line breaks when the word continues across a line.
- Preserve paragraph order over visual line breaks.
- Normalize ligatures and OCR-like artifacts after visual recognition.
- Keep uncertain text with a `% TODO verify:` comment only when confidence is genuinely low.

Do not create a `.txt` intermediate. Temporary `.tex` page drafts are acceptable during work, but the delivered article source must contain all content pasted into one final `.tex`.

## Output Shape

Create one compilable LaTeX file unless the user asks for a fragment. Unless the user specifies another name, name the final file `<FirstAuthorSurname><PublicationYear>_p2t.tex`, for example `Fischer2011_p2t.tex`. Use a conventional article preamble:

```latex
\documentclass[11pt]{article}
\usepackage[margin=1in]{geometry}
\usepackage{amsmath,amssymb}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{tabularx}
\usepackage{longtable}
\usepackage{threeparttable}
\usepackage{caption}
\usepackage{hyperref}

\begin{document}
...
\end{document}
```

Add packages only when the converted content needs them. Keep the final `.tex` self-contained except for optional placeholder figure image files if the chosen placeholder command requires an asset. If adding a process note at the end, title it `Conversion Note`; do not prefix it with `Appendix A.` unless the source paper itself has such an appendix.

## Quality Checks

Before finishing:

- Confirm every rendered page has been inspected.
- Confirm tables are LaTeX tables, not screenshots.
- Confirm figure captions and notes are present even when the figure image is blank.
- Confirm no `\input` or `\include` commands are used for page assembly.
- Confirm no text-extraction artifacts or `.txt` pipeline outputs are used as source material.
- Compile with `pdflatex` or another available LaTeX engine when feasible, then fix reported errors that affect compilation.


