from collections.abc import Callable

def checked(heuristic: Callable[[str], float]) -> Callable[[str], float]:
    def evaluate(vertex: str) -> float:
        value = heuristic(vertex)
        if value < 0: raise ValueError("A* heuristics must be non-negative")
        return value
    return evaluate
