# Algorithmic Transit Simulator

A dependency-free Python project for planning resilient public-transit journeys.  It models a timetable as a directed weighted graph, applies service disruptions, finds routes, detects platform conflicts, and produces operations metrics.

## Run

```bash
python -m unittest discover -s algorithmic_transit_simulator/tests -v
python algorithmic_transit_simulator/examples/demo.py
```

The project is intentionally implemented with core data structures rather than third-party packages so the algorithms remain inspectable.

## Features

- Time-dependent earliest-arrival routing with transfer buffers
- Prefix stop search, platform conflict detection, and disruption-aware graphs
- Cached route queries, JSON import/export, metrics, and event simulation
- Unit tests for each algorithm and an included sample timetable
