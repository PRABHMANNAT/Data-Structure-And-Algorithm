from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from delivery_network.json_io import load_graph
from delivery_network.route_planner import RoutePlanner

network = load_graph(Path(__file__).resolve().parents[1] / "data" / "city_network.json")
route = RoutePlanner(network).shortest_path("WH", "CU")
print("Fastest route:", " -> ".join(route.stops), f"({route.minutes} min)")
