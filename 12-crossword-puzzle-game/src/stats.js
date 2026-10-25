import {formatTime} from './timer.js';
const KEY='daily-grid.journal.v1';
export function journal(){try{const value=JSON.parse(localStorage.getItem(KEY));return value&&typeof value==='object'&&!Array.isArray(value)?value:{};}catch{return {};}}
export function recordCompletion(state){
  if(!state.completed)return;
  const all=journal(),previous=all[state.puzzle.id]||{solves:0,best:null};
  const signature=JSON.stringify([state.values,state.elapsed]);
  if(previous.signature===signature)return;
  all[state.puzzle.id]={solves:previous.solves+1,best:!state.assisted?Math.min(previous.best??Infinity,state.elapsed):previous.best,signature,assisted:state.assisted};
  try{localStorage.setItem(KEY,JSON.stringify(all));}catch{/* A journal is optional. */}
}
export function statsText(state){
  const entry=journal()[state.puzzle.id];
  if(!entry)return 'Your first solve starts here. Progress is saved as you go.';
  return `${entry.solves} completed ${entry.solves===1?'grid':'grids'} · ${entry.best==null?'No unassisted time yet':'Best unassisted: '+formatTime(entry.best)}${state.assisted?' · Current grid uses reveals':''}`;
}
