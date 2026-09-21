# Algorithmic Transit Simulator

A dependency-free Python project for planning resilient public-transit journeys.  It models a timetable as a directed weighted graph, applies service disruptions, finds routes, detects platform conflicts, and produces operations metrics.

## Run

```bash
python -m unittest discover -s algorithmic_transit_simulator/tests -v
python algorithmic_transit_simulator/examples/demo.py
```

The project is intentionally implemented with core data structures rather than third-party packages so the algorithms remain inspectable.
