from .parse import parse
from .core import Network
from .extra import maximum


def run(data):
    arcs, source, sink = parse(data)
    network = Network(arcs)
    value, phases = maximum(network, source, sink)
    left = network.reachable(source)
    cut = [a for a in arcs if a.source in left and a.target not in left]
    return dict(
        metrics=[
            ["Maximum flow", value],
            ["Minimum cut", sum(a.capacity for a in cut)],
            ["BFS phases", len(phases)],
        ],
        source=source,
        sink=sink,
        phases=phases,
        reachable=sorted(left),
        flows=[
            dict(
                source=a.source,
                target=a.target,
                capacity=a.capacity,
                flow=a.capacity - network.adj[a.source][i].remaining,
            )
            for a, i in network.original
        ],
        cut=[[a.source, a.target, a.capacity] for a in cut],
    )
