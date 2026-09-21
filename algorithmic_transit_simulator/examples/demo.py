import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1]))
from transit_simulator.json_io import load_network
from transit_simulator.router import EarliestArrivalRouter

network=Path(__file__).parents[1]/"data"/"sample_network.json"
journey=EarliestArrivalRouter(load_network(network)).route("north","harbor",470)
print(" -> ".join(edge.destination for edge in journey.connections), f"arrives at {journey.arrival}")
