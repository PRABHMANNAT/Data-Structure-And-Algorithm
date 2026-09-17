import argparse
from pathlib import Path
from .json_io import load_graph
from .route_planner import RoutePlanner

def build_parser():
    parser = argparse.ArgumentParser(description="Plan a delivery route")
    parser.add_argument("network", type=Path); parser.add_argument("origin"); parser.add_argument("destination")
    return parser

def main(argv=None):
    arguments = build_parser().parse_args(argv)
    route = RoutePlanner(load_graph(arguments.network)).shortest_path(arguments.origin, arguments.destination)
    print(" -> ".join(route.stops), f"({route.minutes} min)")
