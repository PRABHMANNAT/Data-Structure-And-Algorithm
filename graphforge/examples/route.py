from graphforge import Edge, RouteEngine
engine = RouteEngine()
engine.add(Edge("a", "b", 2)); engine.add(Edge("b", "c", 3))
print(engine.route("a", "c"))
