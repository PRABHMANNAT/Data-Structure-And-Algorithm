from __future__ import annotations

from .binary_heap import MinHeap
from .graph import TransitGraph
from .models import Journey


class EarliestArrivalRouter:
    """Time-dependent Dijkstra search with a configurable transfer buffer."""

    def __init__(self, graph: TransitGraph, transfer_buffer: int = 2) -> None:
        self.graph = graph
        self.transfer_buffer = transfer_buffer

    def route(self, origin: str, destination: str, departure: int) -> Journey | None:
        if origin not in self.graph.stops or destination not in self.graph.stops:
            raise KeyError("origin and destination must exist")
        queue = MinHeap[str](); queue.push(departure, origin)
        arrival = {origin: departure}; previous = {}
        while queue:
            time, stop = queue.pop()
            if time != arrival[stop]:
                continue
            if stop == destination:
                break
            buffer = 0 if stop == origin else self.transfer_buffer
            for edge in self.graph.departures_from(stop, time + buffer):
                if edge.arrival < arrival.get(edge.destination, float("inf")):
                    arrival[edge.destination] = edge.arrival
                    previous[edge.destination] = edge
                    queue.push(edge.arrival, edge.destination)
        if destination not in arrival:
            return None
        edges = []
        while destination != origin:
            edge = previous[destination]; edges.append(edge); destination = edge.origin
        return Journey(tuple(reversed(edges)))
