# Supported source files

The extension map recognizes `.py`, `.js`, `.jsx`, `.ts`, `.tsx`, `.java`, `.c`,
`.h`, `.cpp`, `.cc`, `.hpp`, `.go`, and `.rs`. C headers use the C profile and C++
headers use the C++ profile. Files of different detected languages are not compared.

Python uses the standard-library tokenizer, preserving precise line and column
positions and Python keywords. Other languages use a lightweight lexical scanner.
That scanner strips `//`, `/* ... */`, and `#` comments, normalizes quoted strings,
numbers, and nonkeyword identifiers, and preserves punctuation. It does not parse
language syntax, macros, regex literals, or templates. This means language-specific
corner cases may be tokenized approximately. Inspect original source for any match.
