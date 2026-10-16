# Supported file formats

The extension map recognizes `.pdf`, `.docx`, `.txt`, `.md`, `.py`, `.js`, `.jsx`,
`.ts`, `.tsx`, `.java`, `.c`, `.h`, `.cpp`, `.cc`, `.hpp`, `.go`, and `.rs`.
PDF, DOCX, TXT, and Markdown share a prose comparison profile, so they can match
across formats. C headers use the C profile and C++ headers use the C++ profile.
Source files of different detected languages are not compared.

PDF text is extracted with `pypdf`; image-only scans need OCR before use.
DOCX text comes from the document's paragraphs and tables. Plain text and Markdown
use UTF-8 with a Windows-1252 fallback. Prose tokenization retains case-folded
words and ignores punctuation and formatting. Page layout, images, and styling
are not compared.

Python uses the standard-library tokenizer, preserving precise line and column
positions and Python keywords. Other languages use a lightweight lexical scanner.
That scanner strips `//`, `/* ... */`, and `#` comments, normalizes quoted strings,
numbers, and nonkeyword identifiers, and preserves punctuation. It does not parse
language syntax, macros, regex literals, or templates. This means language-specific
corner cases may be tokenized approximately. Inspect original source for any match.
