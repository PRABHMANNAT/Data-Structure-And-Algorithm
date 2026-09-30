import { DIRECTIONS } from "./config.js";
import { keyFor, isOpen } from "./puzzle-utils.js";
import { currentWord } from "./selectors.js";
export function move(state, rowDelta, colDelta) { const [row,col]=state.selected.split(":").map(Number); let nextRow=row+rowDelta,nextCol=col+colDelta; while(isOpen(state.puzzle,nextRow,nextCol)===false && nextRow>=0 && nextCol>=0 && nextRow<state.puzzle.grid.length && nextCol<state.puzzle.grid[0].length){ nextRow+=rowDelta; nextCol+=colDelta; } if(isOpen(state.puzzle,nextRow,nextCol)) state.selected=keyFor(nextRow,nextCol); }
export function advance(state, backwards=false) { const word=currentWord(state); if(!word)return; const index=word.cells.findIndex(cell=>cell.key===state.selected); const next=word.cells[index+(backwards?-1:1)]; if(next) state.selected=next.key; }
export function toggleDirection(state) { state.direction=state.direction===DIRECTIONS.ACROSS?DIRECTIONS.DOWN:DIRECTIONS.ACROSS; state.activeTab=state.direction; }
export function selectWord(state,word) { state.selected=word.cells[0].key; state.direction=word.direction; state.activeTab=word.direction; }
export function handleArrow(state,key) { const moves={ArrowLeft:[0,-1],ArrowRight:[0,1],ArrowUp:[-1,0],ArrowDown:[1,0]}; if(!moves[key])return false; move(state,...moves[key]); state.direction=["ArrowLeft","ArrowRight"].includes(key)?DIRECTIONS.ACROSS:DIRECTIONS.DOWN; state.activeTab=state.direction; return true; }
