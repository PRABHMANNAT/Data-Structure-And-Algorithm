from workbench.lab_inputs import rows, whole, names, words
from workbench.validation import text
from .models import Server


def parse(data):
    servers = [Server(n, whole(w, 1, 5)) for n, w in rows(data, "servers", 2, 12)]
    names([s.name for s in servers])
    added = text(data, "added").strip()
    if (
        not added
        or any(c.isspace() for c in added)
        or len(added) > 40
        or added in {s.name for s in servers}
    ):
        raise ValueError("Added server needs a new, nonempty name without whitespace")
    return (
        servers,
        Server(added, 1),
        words(data, "keys"),
        whole(data.get("replicas", 16), 1, 64),
    )
