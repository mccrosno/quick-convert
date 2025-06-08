from pathlib import Path
import pypandoc

EXTENSION_TO_FORMAT = {
    ".md": "markdown",
    ".markdown": "markdown",
    ".txt": "markdown",
    ".pdf": "pdf",
    ".html": "html",
    ".htm": "html",
    ".docx": "docx",
    ".odt": "odt",
    ".rtf": "rtf",
    ".epub": "epub",
    ".tex": "latex",
    ".bib": "bibtex",
    ".biblatex": "biblatex",
    ".org": "org",
    ".rst": "rst",
    ".csv": "csv",
    ".tsv": "tsv",
    ".ipynb": "ipynb",
    ".json": "json"
}

FORMAT_TO_EXTENSIONS = {
    "markdown": [".md", ".markdown", ".txt", ".pdf", ".html", ".docx", ".odt"],
    "html": [".html", ".htm", ".pdf", ".docx", ".odt", ".txt"],
    "docx": [".docx", ".pdf", ".html", ".md", ".txt"],
    "odt": [".odt", ".pdf", ".html", ".docx", ".txt"],
    "rtf": [".rtf", ".pdf", ".docx", ".odt", ".txt"],
    "latex": [".tex", ".pdf", ".html", ".md", ".docx"],
    "bibtex": [".bib", ".pdf", ".md", ".html"],
    "biblatex": [".biblatex", ".pdf", ".md", ".html"],
    "org": [".org", ".pdf", ".md", ".html"],
    "rst": [".rst", ".pdf", ".md", ".html"],
    "csv": [".csv", ".pdf", ".md", ".html"],
    "tsv": [".tsv", ".pdf", ".md", ".html"],
    "ipynb": [".ipynb", ".pdf", ".md", ".html"],
    "pdf": [".pdf"],
    "plain": [".txt", ".pdf"],
    "epub": [".epub"],
    "json": [".json"]
}

def get_format_from_extension(ext: str) -> str | None:
    return EXTENSION_TO_FORMAT.get(ext)

def get_extensions_from_format(fmt: str) -> list[str]:
    return FORMAT_TO_EXTENSIONS.get(fmt, [])

def convert_file(file_path: Path, output_type: str) -> Path:
    if not ("." + output_type) in get_extensions_from_format(get_format_from_extension(file_path.suffix)): return
    pypandoc.convert_file(
        source_file=str(file_path),
        to=output_type,
        format=get_format_from_extension(file_path.suffix.lower()),
        outputfile=str(file_path.with_suffix("." + output_type))
    )