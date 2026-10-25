import {STORAGE_KEY} from './config.js';
const KEY='daily-grid.sessions.v2';
function read(){try{const value=JSON.parse(localStorage.getItem(KEY));return value&&typeof value==='object'&&!Array.isArray(value)?value:{};}catch{return {};}}
export function loadSession(puzzleId){
  const all=read();
  if(puzzleId)return all.puzzles?.[puzzleId]??{};
  if(all.active)return {puzzleId:all.active};
  try{const old=JSON.parse(localStorage.getItem(STORAGE_KEY));return old&&typeof old==='object'?old:{};}catch{return {};}
}
export function saveSession(state){
  const session={puzzleId:state.puzzle.id,values:state.values,selected:state.selected,direction:state.direction,activeTab:state.activeTab,elapsed:state.elapsed,theme:state.theme,marks:state.marks,assisted:state.assisted,checks:state.checks};
  const all=read();all.active=state.puzzle.id;all.puzzles={...(all.puzzles||{}),[state.puzzle.id]:session};
  try{localStorage.setItem(KEY,JSON.stringify(all));return true;}catch{return false;}
}
export function clearSession(puzzleId){
  try{const all=read();if(puzzleId){delete all.puzzles?.[puzzleId];localStorage.setItem(KEY,JSON.stringify(all));}else localStorage.removeItem(KEY);}catch{/* Storage may be disabled. */}
}
