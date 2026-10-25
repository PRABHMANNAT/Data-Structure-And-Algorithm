import {DIRECTIONS} from './config.js';
export function createState(puzzle,words,saved={}){
  const cells=new Map(words.flatMap(word=>word.cells).map(cell=>[cell.key,cell]));
  const values={},marks={};
  if(saved.values&&typeof saved.values==='object')for(const [key,value] of Object.entries(saved.values))if(cells.has(key)&&typeof value==='string'&&/^[A-Z]$/.test(value))values[key]=value;
  if(saved.marks&&typeof saved.marks==='object')for(const [key,value] of Object.entries(saved.marks))if(cells.has(key)&&['correct','wrong'].includes(value))marks[key]=value;
  const direction=value=>Object.values(DIRECTIONS).includes(value)?value:(words[0]?.direction||DIRECTIONS.ACROSS);
  return {puzzle,words,values,marks,selected:cells.has(saved.selected)?saved.selected:words[0]?.cells[0]?.key,direction:direction(saved.direction),activeTab:direction(saved.activeTab),elapsed:Number.isSafeInteger(saved.elapsed)&&saved.elapsed>=0?saved.elapsed:0,paused:false,theme:saved.theme==='night'?'night':'day',assisted:saved.assisted===true,checks:Number.isSafeInteger(saved.checks)&&saved.checks>=0?saved.checks:0,completed:[...cells.values()].every(cell=>values[cell.key]===cell.answer)};
}
export const selection=state=>state.selected?.split(':').map(Number)??[0,0];
