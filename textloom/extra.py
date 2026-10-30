"""Checked patch application and inversion: edits are data, never executable."""

from .models import Edit


def apply(source, edits):
    cursor = 0
    output = []
    for edit in edits:
        if edit.kind not in {"equal", "delete", "insert"}:
            raise ValueError("Unknown edit kind")
        if edit.kind != "insert":
            if cursor >= len(source) or source[cursor] != edit.text:
                raise ValueError("Patch does not match source")
            cursor += 1
        if edit.kind != "delete":
            output.append(edit.text)
    if cursor != len(source):
        raise ValueError("Patch leaves unconsumed source lines")
    return output


def invert(edits):
    return [
        Edit({"equal": "equal", "insert": "delete", "delete": "insert"}[e.kind], e.text)
        for e in edits
    ]
