import { keyFor } from "./puzzle-utils.js";
import { wordAt } from "./word-model.js";
import { selection } from "./state.js";
export const currentWord = state => { const [row,col]=selection(state); return wordAt(state.words,row,col,state.direction) ?? state.words.find(word=>word.cells.some(cell=>cell.key===keyFor(row,col))); };
export const valueCount = state => Object.values(state.values).filter(Boolean).length;
export const openCount = state => state.puzzle.grid.join("").replaceAll("#","").length;
export const percentComplete = state => Math.round(valueCount(state) / openCount(state) * 100);
export const isWordComplete = (state,word) => word.cells.every(cell=>state.values[cell.key]);
