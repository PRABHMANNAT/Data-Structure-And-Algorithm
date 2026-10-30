from dataclasses import asdict
from .parse import parse
from .core import diff
from .extra import apply, invert


def run(data):
    old, new = parse(data)
    a = old.splitlines(keepends=True)
    b = new.splitlines(keepends=True)
    edits = diff(a, b)
    patched = "".join(apply(a, edits))
    restored = "".join(apply(b, invert(edits)))
    added = sum(e.kind == "insert" for e in edits)
    removed = sum(e.kind == "delete" for e in edits)
    return dict(
        metrics=[
            ["Inserted lines", added],
            ["Deleted lines", removed],
            ["Edit distance", added + removed],
            [
                "Round trip",
                "Verified" if patched == new and restored == old else "Failed",
            ],
        ],
        edits=[asdict(e) for e in edits],
        patched=patched,
        restored=restored,
        verified=patched == new and restored == old,
    )
