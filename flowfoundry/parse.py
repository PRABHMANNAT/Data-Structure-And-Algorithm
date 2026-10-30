from workbench.lab_inputs import rows, whole
from workbench.validation import text
from .models import Arc


def parse(data):
    arcs = [Arc(a, b, whole(c, 0, 10000)) for a, b, c in rows(data, "edges", 3, 80)]
    vertices = {v for arc in arcs for v in (arc.source, arc.target)}
    source = text(data, "source")
    sink = text(data, "sink")
    if source == sink or source not in vertices or sink not in vertices:
        raise ValueError("Choose distinct source and sink names present in the network")
    if any(a.source == a.target for a in arcs) or len(vertices) > 40:
        raise ValueError("No self loops; use at most 40 vertices")
    return arcs, source, sink
