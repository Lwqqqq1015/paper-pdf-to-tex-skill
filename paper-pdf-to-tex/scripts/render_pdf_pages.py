#!/usr/bin/env python3
"""Render a PDF to one PNG image per page for image-based TeX conversion."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


def render_with_pymupdf(pdf_path: Path, output_dir: Path, dpi: int, prefix: str) -> bool:
    try:
        import fitz  # type: ignore
    except Exception:
        return False

    doc = fitz.open(str(pdf_path))
    scale = dpi / 72.0
    matrix = fitz.Matrix(scale, scale)
    for page_index in range(doc.page_count):
        page = doc.load_page(page_index)
        pix = page.get_pixmap(matrix=matrix, alpha=False)
        out = output_dir / f"{prefix}-{page_index + 1:04d}.png"
        pix.save(str(out))
    doc.close()
    return True


def render_with_pdftoppm(pdf_path: Path, output_dir: Path, dpi: int, prefix: str) -> bool:
    exe = shutil.which("pdftoppm")
    if not exe:
        return False

    output_prefix = output_dir / prefix
    cmd = [
        exe,
        "-r",
        str(dpi),
        "-png",
        str(pdf_path),
        str(output_prefix),
    ]
    subprocess.run(cmd, check=True)

    for image_path in output_dir.glob(f"{prefix}-*.png"):
        parts = image_path.stem.rsplit("-", 1)
        if len(parts) == 2 and parts[1].isdigit():
            padded = output_dir / f"{prefix}-{int(parts[1]):04d}.png"
            if padded != image_path:
                image_path.rename(padded)
    return True


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Render a PDF into page PNGs without extracting embedded text."
    )
    parser.add_argument("pdf", type=Path, help="Input PDF file")
    parser.add_argument(
        "-o",
        "--output-dir",
        type=Path,
        default=None,
        help="Output directory for page images",
    )
    parser.add_argument("--dpi", type=int, default=350, help="Render DPI")
    parser.add_argument("--prefix", default="page", help="Output image prefix")
    args = parser.parse_args()

    pdf_path = args.pdf.expanduser().resolve()
    if not pdf_path.is_file():
        parser.error(f"PDF not found: {pdf_path}")

    output_dir = args.output_dir or pdf_path.with_suffix("").parent / f"{pdf_path.stem}_page_images"
    output_dir = output_dir.expanduser().resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    if render_with_pymupdf(pdf_path, output_dir, args.dpi, args.prefix):
        print(output_dir)
        return 0

    if render_with_pdftoppm(pdf_path, output_dir, args.dpi, args.prefix):
        print(output_dir)
        return 0

    print(
        "Could not render PDF. Install PyMuPDF (`pip install pymupdf`) or provide `pdftoppm`.",
        file=sys.stderr,
    )
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
