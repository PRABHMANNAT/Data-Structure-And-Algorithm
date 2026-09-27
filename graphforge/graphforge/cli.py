from __future__ import annotations
import argparse, json
from .engine import RouteEngine
from .model import Edge

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Find a route from JSON edges")
    parser.add_argument("source"); parser.add_argument("target"); args = parser.parse_args(argv)
    engine = RouteEngine()
    for line in __import__("sys").stdin: engine.add(Edge(**json.loads(line)))
    route = engine.route(args.source, args.target)
    print(json.dumps(None if route is None else {"vertices": route.vertices, "cost": route.cost})); return 0

if __name__ == "__main__": raise SystemExit(main())
