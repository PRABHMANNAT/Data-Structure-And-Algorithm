# RouteLab

A quiet, interactive workspace for shortest-path algorithms. Draw barriers on a grid, place two endpoints, and inspect how A* and Dijkstra search the same terrain.

## Open it

From the repository root, run `python -m workbench.server` and visit [RouteLab](http://127.0.0.1:8765/11-map-routing-pathfinding-visualizer/01-source/). Both `01-source/` and the matching `dist/` build also work on a static HTTP server. ES modules require HTTP rather than `file://`.

## Working with the map

- Draw or erase barriers by dragging. Place start A and destination B with their tools.
- Run continuously, pause, or advance one explored cell at a time.
- Compare A* and Dijkstra on identical terrain. Both find a shortest path with unit-cost orthogonal movement.
- Undo and redo up to 40 map edits. A pointer stroke counts as one edit.
- Choose an open field, switchbacks, or random barriers. Random terrain carves a guaranteed connection.
- Save and load validated JSON maps. Your latest terrain also persists on this device.
- Move a keyboard cursor with arrow keys and apply the selected tool with Enter.

`W/E` select barrier/erase, `S/D` move endpoints, `Space` runs or pauses, `C` clears the search, `?` opens help, and `Ctrl/⌘ Z` undoes an edit (`Shift` redoes).

The frontier metric reports the actual distinct frontier cells and its peak. Compute time excludes animation. Ties in the priority queue are stable, so the exploration order is reproducible. Path cells render above explored cells.

## Check the logic

```sh
node --test 11-map-routing-pathfinding-visualizer/tests/search.test.mjs
```

The tests compare both search methods across 30 deterministic random terrains, verify each route step, cover unreachable and zero-length routes, and test map validation plus undo/redo.

The original `02-learning-notes/` remain a useful conceptual companion. The current source separates search, heap, map rendering, persistence, presets, and file exchange so the algorithms can be tested without a browser.
