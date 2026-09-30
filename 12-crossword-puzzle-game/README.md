# Crossword Lab

Crossword Lab is a dependency-free, browser-based crossword game that connects wordplay to approachable data-structure ideas. It ships with three small puzzles, keyboard-first play, checking and reveal controls, a timer, saved progress, and a high-contrast day/night theme.

## Play locally

Open `index.html` in a modern browser. No build step or web server is required.

## Features

- Matrix-backed crossword grids with generated across/down word models.
- Click, touch, or keyboard navigation with live clue highlighting.
- Cell, word, and puzzle-level checking and revealing.
- Local browser persistence for an interrupted session.
- Responsive, accessible controls and an in-app shortcut guide.

## Project structure

```text
index.html       Accessible game shell
styles.css       Responsive visual system
src/             Puzzle model, rendering, state, and interactions
docs/            Focused implementation and learning notes
```

## Keyboard controls

Type letters to fill cells. Use the arrow keys to move, Space to switch between Across and Down, Backspace to clear the prior cell, and Tab/Enter to move through clue controls.

## Data structures in use

The grid is a two-dimensional matrix. Coordinate keys index individual cells, arrays retain word order, and maps/objects give constant-time access to entered values, validation markers, and persisted session state.
