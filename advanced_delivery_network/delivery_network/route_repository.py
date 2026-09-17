class RouteRepository:
    """In-memory route history keyed by a delivery identifier."""
    def __init__(self): self._routes = {}
    def save(self, delivery_id, route): self._routes[delivery_id] = route
    def get(self, delivery_id): return self._routes.get(delivery_id)
    def all_ids(self): return tuple(self._routes)
