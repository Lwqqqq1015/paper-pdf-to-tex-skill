# Paper PDF to TeX Skill

中文 | [English](#english)

## 中文

`paper-pdf-to-tex` 是一个用于 Codex 的本地 skill，用来把期刊论文 PDF 转换为单个可编译的 LaTeX `.tex` 文件。

这个 skill 的核心原则是：**先把 PDF 渲染成页面图片，再基于页面图片逐页识别和转写 LaTeX**。它不会依赖 PDF 内嵌文本层，不会走 `pdftotext`，不会把 PDF 先转成 `.txt`，也不会用 `\input` 或 `\include` 拼接页面片段。

## 主要功能

- 将学术论文 PDF 渲染为逐页 PNG 图片。
- 基于页面图像逐页识别正文、标题、作者、摘要、关键词、章节、脚注、公式、表格、图题和参考文献。
- 把所有页面内容直接粘贴式合并到一个总 `.tex` 文件中。
- 保留文中 figure 引用、figure 标题和注释；实际图像用较小的空白占位框替代。
- 将 table 转为 LaTeX 表格，而不是截图。
- 行内公式和符号使用 `$...$`。
- 有编号的行间公式使用 `\begin{equation}...\end{equation}`。
- 文内引用保持为论文可见的作者年份文本，例如 `(Aldy et al., 2008)`，不转换为 `\cite{}`、`\citep{}` 或 `\citet{}`。
- 默认输出文件名为 `<第一作者姓><年份>_p2t.tex`，例如 `Fischer2011_p2t.tex`。

## 安装

将仓库中的 `paper-pdf-to-tex` 文件夹复制到 Codex 的 skills 目录：

```powershell
Copy-Item -Recurse .\paper-pdf-to-tex "$env:USERPROFILE\.codex\skills\paper-pdf-to-tex"
```

如果你已经把本仓库克隆到本地，也可以手动复制：

```text
paper-pdf-to-tex-skill/
  paper-pdf-to-tex/  ->  C:\Users\<你的用户名>\.codex\skills\paper-pdf-to-tex
```

重启 Codex 或开启新会话后，skill 会出现在可用 skills 中。

## 使用示例

你可以这样对 Codex 说：

```text
使用 paper-pdf-to-tex skill，把 C:\path\to\paper.pdf 转成 tex
```

或者：

```text
把这个期刊论文 PDF 转成 LaTeX，先转图片再逐页识别，不要用 PDF 嵌入文本
```

## 仓库结构

```text
paper-pdf-to-tex/
  SKILL.md
  agents/
    openai.yaml
  references/
    latex-conventions.md
  scripts/
    render_pdf_pages.py
```

## 重要约束

- 不使用 PDF 文本层。
- 不使用 `pdftotext`。
- 不创建 `.txt` 中间文件。
- 不使用现有 PDF 转换类 skills 替代本流程。
- 不使用 `\input` 或 `\include` 组装最终文件。
- 表格必须转为 LaTeX 表格。
- 图像暂时可以不重建，但图题、注释和正文中的图描述必须保留。

## English

`paper-pdf-to-tex` is a local Codex skill for converting journal article PDFs into a single compilable LaTeX `.tex` file.

The central rule is: **render the PDF into page images first, then visually recognize each page image and write LaTeX page by page**. The workflow does not rely on embedded PDF text, does not use `pdftotext`, does not convert the PDF into `.txt`, and does not assemble the final source with `\input` or `\include`.

## Features

- Render academic paper PDFs into page-level PNG images.
- Visually reconstruct title, authors, abstract, keywords, sections, body text, footnotes, equations, tables, figure captions, and references from page images.
- Paste all converted page content into one master `.tex` file.
- Preserve in-text figure mentions, figure captions, and notes; replace actual figure graphics with compact blank placeholders.
- Convert tables into LaTeX tables instead of screenshots.
- Use `$...$` for inline math and symbols.
- Use `\begin{equation}...\end{equation}` for numbered display equations.
- Keep in-text citations as visible author-year prose, such as `(Aldy et al., 2008)`, instead of converting them into `\cite{}`, `\citep{}`, or `\citet{}`.
- Name the final output as `<FirstAuthorSurname><Year>_p2t.tex`, for example `Fischer2011_p2t.tex`.

## Installation

Copy the `paper-pdf-to-tex` folder into your Codex skills directory:

```powershell
Copy-Item -Recurse .\paper-pdf-to-tex "$env:USERPROFILE\.codex\skills\paper-pdf-to-tex"
```

After cloning this repository, the expected layout is:

```text
paper-pdf-to-tex-skill/
  paper-pdf-to-tex/  ->  C:\Users\<your-user-name>\.codex\skills\paper-pdf-to-tex
```

Restart Codex or open a new session so the skill can be discovered.

## Usage Example

Ask Codex:

```text
Use the paper-pdf-to-tex skill to convert C:\path\to\paper.pdf into TeX.
```

Or:

```text
Convert this journal article PDF to LaTeX by rendering pages to images first; do not use embedded PDF text.
```

## Repository Layout

```text
paper-pdf-to-tex/
  SKILL.md
  agents/
    openai.yaml
  references/
    latex-conventions.md
  scripts/
    render_pdf_pages.py
```

## Important Constraints

- Do not use the PDF text layer.
- Do not use `pdftotext`.
- Do not create `.txt` intermediate files.
- Do not replace this workflow with existing PDF conversion skills.
- Do not use `\input` or `\include` to assemble the final file.
- Convert tables into LaTeX tables.
- Figure graphics may be skipped temporarily, but figure captions, notes, and in-text descriptions must be preserved.
