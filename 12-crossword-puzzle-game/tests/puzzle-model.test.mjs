import assert from "node:assert/strict";
import { puzzles } from "../src/puzzles.js";
import { buildWords } from "../src/word-model.js";

for (const puzzle of puzzles) {
  const words = buildWords(puzzle);
  assert.ok(words.length > 0, `${puzzle.id} must create at least one word`);
  for (const word of words) {
    assert.ok(puzzle.clues[word.answer], `${puzzle.id} is missing a clue for ${word.answer}`);
    assert.ok(word.cells.length > 1, `${word.answer} should not be a one-cell word`);
  }
}

console.log(`Validated ${puzzles.length} puzzles.`);
