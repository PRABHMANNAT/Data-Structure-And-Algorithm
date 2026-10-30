from workbench.validation import text


def parse(data):
    old = text(data, "old", limit=6000)
    new = text(data, "new", limit=6000)
    if max(len(old.splitlines()), len(new.splitlines())) > 120:
        raise ValueError("Use at most 120 lines per document")
    return old, new
