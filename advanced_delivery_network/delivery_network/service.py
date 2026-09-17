from .lru_cache import LRUCache
from .route_planner import RoutePlanner

class DeliveryService:
    def __init__(self, graph, cache_size=32):
        self.planner = RoutePlanner(graph); self.cache = LRUCache(cache_size)
    def plan(self, origin, destination):
        key = (origin, destination); route = self.cache.get(key)
        if route is None: route = self.planner.shortest_path(origin, destination); self.cache.set(key, route)
        return route
