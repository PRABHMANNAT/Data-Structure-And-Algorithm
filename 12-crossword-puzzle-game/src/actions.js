import {currentWord,percentComplete} from './selectors.js';
import {announcement} from './dom.js';
const uniqueCells=state=>[...new Map(state.words.flatMap(word=>word.cells).map(cell=>[cell.key,cell])).values()];
export function clearWord(state){currentWord(state)?.cells.forEach(cell=>{delete state.values[cell.key];delete state.marks[cell.key];});state.completed=false;announcement('Current word cleared.');}
export function resetPuzzle(state){state.values={};state.marks={};state.elapsed=0;state.completed=false;state.paused=false;state.assisted=false;state.checks=0;announcement('Puzzle reset.');}
export function checkCells(state,cells){let right=0;state.checks++;cells.forEach(cell=>{if(!state.values[cell.key])return;state.marks[cell.key]=state.values[cell.key]===cell.answer?'correct':'wrong';if(state.marks[cell.key]==='correct')right++;});announcement(`${right} filled ${right===1?'letter is':'letters are'} correct.`);}
export function revealCells(state,cells){state.assisted=true;cells.forEach(cell=>{state.values[cell.key]=cell.answer;state.marks[cell.key]='correct';});announcement('Answer revealed.');}
export function checkPuzzle(state){checkCells(state,uniqueCells(state));}
export function revealPuzzle(state){revealCells(state,uniqueCells(state));announcement('Grid revealed.');}
export function checkCompletion(state){
  const completed=percentComplete(state)===100&&uniqueCells(state).every(cell=>state.values[cell.key]===cell.answer);
  if(completed&&!state.completed)announcement(`Puzzle complete in ${Math.floor(state.elapsed/60)} minutes and ${state.elapsed%60} seconds.`);
  state.completed=completed;return completed;
}
