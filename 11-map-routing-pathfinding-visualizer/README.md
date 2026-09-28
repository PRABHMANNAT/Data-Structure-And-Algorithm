# RouteLab — Map Routing & Pathfinding Visualizer

RouteLab is a browser-based canvas visualizer for shortest-path search on a spatial grid. Draw road closures, reposition the start and destination markers, and compare Dijkstra's algorithm with A* in real time.

## Highlights

- Interactive canvas map with click-and-drag barrier editing
- True adjacency-list graph construction for every search run
- Min-heap priority queue implementation
- Dijkstra and A* shortest-path search with Manhattan-distance heuristic
- Animated exploration, frontier, final route, and live performance metrics
- Responsive controls, keyboard shortcuts, randomized maze generator, and accessible labels

## Run locally

No dependencies are required. Serve the folder with a static file server, then open the displayed local URL:

```bash
cd 11-map-routing-pathfinding-visualizer/01-source
python -m http.server 8080
```

## Project structure

```text
11-map-routing-pathfinding-visualizer/
├── 01-source/          Interactive HTML, CSS, JavaScript, and favicon
├── 02-learning-notes/  Numbered algorithm and implementation notes
├── dist/               Static deployment bundle
├── .openai/            Hosting configuration
└── README.md           Setup, controls, and algorithm overview
```

`01-source` is the editable application. `dist` is the matching static bundle used for deployment.

## How the algorithms differ

| Algorithm | Priority | Characteristic |
| --- | --- | --- |
| Dijkstra | Lowest known route cost `g(n)` | Explores uniformly in all viable directions; always optimal for non-negative edge costs. |
| A* | `g(n) + h(n)` | Uses Manhattan distance `h(n)` to focus on the goal while retaining optimality on this grid. |

Both implementations use an adjacency list and a binary min-heap, with `O((V + E) log V)` time complexity on the generated graph.

## Guided notes

The [`02-learning-notes`](02-learning-notes) folder contains a 59-part learning guide that follows the implementation from grid modeling and heap mechanics through A*, rendering, accessibility, and validation.

## Controls

- **W / E** — draw barriers / erase barriers
- **S / D** — reposition start / destination
- **Space** — run the selected search
- **C** — clear current exploration
