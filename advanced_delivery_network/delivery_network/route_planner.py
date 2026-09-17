from .errors import PathNotFoundError
from .indexed_priority_queue import IndexedPriorityQueue
from .models import Route

class RoutePlanner:
    def __init__(self, graph): self.graph = graph
    def shortest_path(self, origin, destination):
        self.graph.stop(origin); self.graph.stop(destination)
        queue, cost, previous = IndexedPriorityQueue(), {origin: 0}, {}
        queue.push_or_decrease(origin, 0)
        while queue:
            current_cost, current = queue.pop()
            if current == destination: break
            for edge in self.graph.neighbors(current):
                candidate = current_cost + edge.minutes
                if candidate < cost.get(edge.destination, float("inf")):
                    cost[edge.destination] = candidate; previous[edge.destination] = current
                    queue.push_or_decrease(edge.destination, candidate)
        if destination not in cost: raise PathNotFoundError(f"{origin} -> {destination}")
        path = [destination]
        while path[-1] != origin: path.append(previous[path[-1]])
        return Route(tuple(reversed(path)), cost[destination])
