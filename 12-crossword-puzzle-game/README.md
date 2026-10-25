# The Daily Grid

A newspaper-inspired crossword workspace with a focused grid, readable clues, quiet colors, and full keyboard control. Three small puzzles introduce word navigation and grid modeling.

## Open the puzzle

From the repository root, run `python -m workbench.server` and visit [The Daily Grid](http://127.0.0.1:8765/12-crossword-puzzle-game/). Any static HTTP server also works. No dependencies or build step are required.

## What changed

- A paper-and-ink interface with a serif masthead, compact tools, and a real dark theme.
- Separate saved progress for every puzzle, with validation when sessions are restored.
- Undo and redo for 80 edits. Assistance records remain accurate when reveals are undone.
- A timer that follows the active puzzle correctly when you switch grids.
- Pausing hides the letters and disables grid input. Leaving the browser tab pauses automatically.
- A local journal tracks completed grids and best times without reveals.
- Reset and whole-grid reveal ask before changing the puzzle. Printing produces a clean blank grid with clues.
- Mobile layouts keep the board full-width and put clues below it.

## Keyboard

Type letters to fill the grid. Arrow keys move between open cells. Space switches direction. Tab and Shift+Tab move through clues while inside the grid. Escape exits to the pause control. Backspace clears the current letter, or moves back if empty. Ctrl/⌘ Z undoes; add Shift to redo. Across and Down tabs support arrow navigation.

## Verify

```sh
cd 12-crossword-puzzle-game
npm test
```

Tests cover puzzle clues, restoration of malformed saved state, undo/redo isolation, assistance retention, zero-based selections, timer switching, and storage failures. All progress and journal data stay in this browser; private browsing can discard them.
