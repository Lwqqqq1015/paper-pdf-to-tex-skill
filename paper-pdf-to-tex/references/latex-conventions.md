# LaTeX Conventions for Image-Based Paper Conversion

## Math

- Use inline math delimiters as `$...$` when following this user's requested convention for inline symbols and equations.
- Use numbered displayed equations as:

```latex
\begin{equation}
...
\end{equation}
```

- Use unnumbered display equations only when the source clearly shows an unnumbered display:

```latex
\[
...
\]
```

- Preserve equation numbers from the PDF when visible by using `\tag{...}` only if LaTeX numbering would not match the source.
- Escape percent signs, underscores, ampersands, hashes, and dollar signs outside math mode.
- Prefer semantic commands for common notation: `\alpha`, `\beta`, `\times`, `\leq`, `\geq`, `\mathbb{R}`, `\mathbf{x}`, `\hat{\theta}`.

## Figures

Preserve figure mentions in the prose and preserve every visible figure caption, title, panel label, and note. Replace the actual figure graphic with a blank placeholder:

```latex
\begin{figure}[htbp]
  \centering
  \fbox{\rule{0pt}{1.15in}\rule{0.68\linewidth}{0pt}}
  \caption{Original figure caption transcribed from the page image.}
  \label{fig:short-descriptive-label}
\end{figure}
```

Use one placeholder per figure or per figure panel group, depending on how the source caption is structured. Keep placeholders compact by default; enlarge only if the user asks.

## Tables

Convert source tables to LaTeX table environments. Prefer:

- `tabular` with `booktabs` for normal tables.
- `tabularx` when columns need wrapping.
- `longtable` for tables spanning multiple pages.
- `threeparttable` when table notes, significance legends, or source notes are present.

Use this shape for ordinary tables:

```latex
\begin{table}[htbp]
  \centering
  \begin{threeparttable}
    \caption{Original table title.}
    \label{tab:short-descriptive-label}
    \begin{tabular}{lll}
      \toprule
      Column 1 & Column 2 & Column 3 \\
      \midrule
      ... & ... & ... \\
      \bottomrule
    \end{tabular}
    \begin{tablenotes}
      \small
      \item Note: Original table note.
    \end{tablenotes}
  \end{threeparttable}
\end{table}
```

Only use `tablenotes` inside `threeparttable`; otherwise place notes as `\caption*{...}` or a `minipage` under the table.

## Cleanup

Remove page-only material unless it carries article meaning:

- Standalone page numbers.
- Running headers and footers.
- Journal issue/date headers repeated on every page.
- Watermarks, download timestamps, database names, and copyright footers.

Keep article-level metadata when it appears as part of the paper's first page or final notes. Title any conversion-process note `Conversion Note`, not `Appendix A. Conversion Note`, unless the source paper itself has an appendix with that name.

