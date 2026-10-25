# Algorithmic Transit Simulator

## Interactive workspace

From the **repository root**, start `python -m workbench.server`, then open
[the Departure board workspace](http://127.0.0.1:8765/algorithmic_transit_simulator/web/).

Find an earliest-arrival journey through a timetable. Explore missed transfers, waiting time, and fares.

The interface runs the Python implementation with your own input. Load an example from the input menu, edit the fields, and choose **Run experiment**. Results include a project-specific visual explanation, a raw-data inspector, JSON export, and comparison with the previous run. The last 12 runs and your unfinished inputs stay in this browser.

**Example scenarios:** Morning connection, Missed transfer.

Python 3.10+ is sufficient; no additional packages are required.

Run the integration checks from the repository root with `python scripts/verify.py --web`. Original command-line examples and library APIs remain available below.


A dependency-free Python project for planning resilient public-transit journeys.  It models a timetable as a directed weighted graph, applies service disruptions, finds routes, detects platform conflicts, and produces operations metrics.

## Run

```bash
python -m unittest discover -s algorithmic_transit_simulator/tests -t algorithmic_transit_simulator -v
python algorithmic_transit_simulator/examples/demo.py
```

Use the CLI from the project directory with the sample network:

```bash
cd algorithmic_transit_simulator
python -m transit_simulator.cli data/sample_network.json north harbor 470
```

The project is intentionally implemented with core data structures rather than third-party packages so the algorithms remain inspectable.

## Features

- Time-dependent earliest-arrival routing with transfer buffers
- Prefix stop search, platform conflict detection, and disruption-aware graphs
- Cached route queries, JSON import/export, metrics, and event simulation
- Unit tests for each algorithm and an included sample timetable
