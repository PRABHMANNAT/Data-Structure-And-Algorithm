import { currentWord, percentComplete } from "./selectors.js";
import { announcement } from "./dom.js";
export function clearWord(state) { const word=currentWord(state); word?.cells.forEach(cell=>{delete state.values[cell.key];delete state.marks[cell.key];}); announcement("Current word cleared."); }
export function resetPuzzle(state) { state.values={};state.marks={};state.elapsed=0;state.completed=false;state.paused=false;announcement("Puzzle reset."); }
export function checkCells(state,cells) { let right=0; cells.forEach(cell=>{if(!state.values[cell.key])return; state.marks[cell.key]=state.values[cell.key]===cell.answer?"correct":"wrong"; if(state.marks[cell.key]==="correct")right++;}); announcement(`${right} filled ${right===1?"cell is":"cells are"} correct.`); }
export function revealCells(state,cells) { cells.forEach(cell=>{state.values[cell.key]=cell.answer;state.marks[cell.key]="correct";}); announcement("Answer revealed."); }
export function checkPuzzle(state) { checkCells(state,state.words.flatMap(word=>word.cells).filter((cell,index,cells)=>cells.findIndex(other=>other.key===cell.key)===index)); }
export function revealPuzzle(state) { revealCells(state,state.words.flatMap(word=>word.cells).filter((cell,index,cells)=>cells.findIndex(other=>other.key===cell.key)===index)); state.completed=true; announcement("Puzzle revealed."); }
export function checkCompletion(state) { if(percentComplete(state)!==100)return false; const cells=state.words.flatMap(word=>word.cells).filter((cell,index,all)=>all.findIndex(other=>other.key===cell.key)===index); if(cells.every(cell=>state.values[cell.key]===cell.answer)){state.completed=true;announcement(`Puzzle complete in ${Math.floor(state.elapsed/60)} minutes and ${state.elapsed%60} seconds!`);return true;} return false; }
