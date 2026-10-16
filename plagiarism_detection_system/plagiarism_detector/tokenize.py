"""Normalize formatting, comments, identifiers, and literal spelling."""

import io
import keyword
import re
from bisect import bisect_right
import token as py_token
import tokenize as py_tokenize

from .languages import KEYWORDS
from .models import Token

_LEX = re.compile(
    r"(?P<comment>//[^\n]*|/\*[\s\S]*?\*/|\#[^\n]*)"
    r"|(?P<string>\"(?:\\.|[^\"\\])*\"|'(?:\\.|[^'\\])*')"
    r"|(?P<number>\b(?:0[xX][0-9a-fA-F]+|\d+(?:\.\d+)?)\b)"
    r"|(?P<identifier>[A-Za-z_][A-Za-z_0-9]*)"
    r"|(?P<operator>==|!=|<=|>=|&&|\|\||=>|->|\+\+|--|[^\s])"
)


def _generic(text: str) -> list[Token]:
    result: list[Token] = []
    newlines = [index for index, char in enumerate(text) if char == "\n"]
    for match in _LEX.finditer(text):
        kind = match.lastgroup
        if kind == "comment":
            continue
        line = bisect_right(newlines, match.start()) + 1
        previous_newline = newlines[line - 2] if line > 1 else -1
        column = match.start() - previous_newline - 1
        raw = match.group()
        if kind == "identifier":
            value = raw if raw in KEYWORDS else "ID"
        elif kind == "number":
            value = "NUM"
        elif kind == "string":
            value = "STR"
        else:
            value = raw
        result.append(Token(value, line, column))
    return result


def _python(text: str) -> list[Token]:
    result: list[Token] = []
    try:
        stream = py_tokenize.generate_tokens(io.StringIO(text).readline)
        for item in stream:
            if item.type in {py_token.ENDMARKER, py_token.NEWLINE, py_token.NL,
                             py_token.INDENT, py_token.DEDENT, py_token.COMMENT,
                             py_token.ENCODING}:
                continue
            if item.type == py_token.NAME:
                value = item.string if keyword.iskeyword(item.string) else "ID"
            elif item.type == py_token.NUMBER:
                value = "NUM"
            elif item.type == py_token.STRING:
                value = "STR"
            else:
                value = item.string
            result.append(Token(value, item.start[0], item.start[1]))
    except (py_tokenize.TokenError, IndentationError) as exc:
        raise ValueError(f"invalid Python token stream: {exc}") from exc
    return result


def _text(text: str) -> list[Token]:
    """Keep actual prose words so unrelated documents do not all become ID."""
    newlines = [index for index, char in enumerate(text) if char == "\n"]
    result = []
    for match in re.finditer(r"\w+(?:['’]\w+)?", text, re.UNICODE):
        line = bisect_right(newlines, match.start()) + 1
        previous_newline = newlines[line - 2] if line > 1 else -1
        result.append(Token(match.group().casefold(), line, match.start() - previous_newline - 1))
    return result


def normalize_tokens(text: str, language: str) -> list[Token]:
    if language == "python":
        return _python(text)
    if language == "text":
        return _text(text)
    return _generic(text)
