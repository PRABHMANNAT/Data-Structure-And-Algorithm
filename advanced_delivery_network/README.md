# Advanced Delivery Network Planner

## Interactive workspace

From the **repository root**, start `python -m workbench.server`, then open
[the Dispatch desk workspace](http://127.0.0.1:8765/advanced_delivery_network/web/).

Plan the shortest delivery route across a weighted network. Change a road cost and see the route respond.

The interface runs the Python implementation with your own input. Load an example from the input menu, edit the fields, and choose **Run experiment**. Results include a project-specific visual explanation, a raw-data inspector, JSON export, and comparison with the previous run. The last 12 runs and your unfinished inputs stay in this browser.

**Example scenarios:** Across town, An isolated destination.

Python 3.10+ is sufficient; no additional packages are required.

Run the integration checks from the repository root with `python scripts/verify.py --web`. Original command-line examples and library APIs remain available below.


A dependency-free Python project that models a delivery network and finds efficient routes. It combines a weighted graph, Dijkstra's algorithm, an indexed priority queue, prefix search, connectivity analysis, caching, and streaming-support data structures.

## Run

```bash
python -m unittest discover -s advanced_delivery_network/tests -v
python advanced_delivery_network/examples/demo.py
```

The code targets Python 3.10+ and uses only the standard library.
