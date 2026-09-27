from graphforge.engine import RouteEngine
from graphforge.model import Edge
def test_engine_route() -> None:
    engine = RouteEngine(); engine.add(Edge("a", "b", 1)); assert engine.route("a", "b").cost == 1
