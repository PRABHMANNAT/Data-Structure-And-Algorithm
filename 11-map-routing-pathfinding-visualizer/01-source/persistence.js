export function serialize(map){return {version:1,cols:map.cols,rows:map.rows,start:{...map.start},end:{...map.end},walls:[...map.walls]};}
export function validate(raw){
  if(!raw||raw.version!==1||!Number.isInteger(raw.cols)||raw.cols<8||raw.cols>40||!Number.isInteger(raw.rows)||raw.rows<6||raw.rows>30)throw new Error('Map dimensions must be 8–40 columns and 6–30 rows.');
  const valid=p=>p&&Number.isInteger(p.x)&&Number.isInteger(p.y)&&p.x>=0&&p.y>=0&&p.x<raw.cols&&p.y<raw.rows;
  if(!valid(raw.start)||!valid(raw.end)||raw.start.x===raw.end.x&&raw.start.y===raw.end.y)throw new Error('The two markers must occupy different cells within the map.');
  if(!Array.isArray(raw.walls)||raw.walls.length>raw.cols*raw.rows)throw new Error('Invalid barriers.');
  const walls=new Set();
  for(const item of raw.walls){if(typeof item!=='string'||!/^\d+,\d+$/.test(item))throw new Error('Invalid barrier coordinates.');const [x,y]=item.split(',').map(Number);if(!valid({x,y}))throw new Error('A barrier falls outside the map.');walls.add(item);}
  walls.delete(`${raw.start.x},${raw.start.y}`);walls.delete(`${raw.end.x},${raw.end.y}`);
  return {cols:raw.cols,rows:raw.rows,start:{...raw.start},end:{...raw.end},walls};
}
export function save(map){try{localStorage.setItem('routelab.map.v2',JSON.stringify(serialize(map)));}catch{/* Private mode may disable storage. */}}
export function restore(fallback){try{return validate(JSON.parse(localStorage.getItem('routelab.map.v2')));}catch{return fallback();}}
export class MapHistory {
  constructor(){this.undoStack=[];this.redoStack=[];}
  push(map){this.undoStack.push(serialize(map));this.undoStack=this.undoStack.slice(-40);this.redoStack=[];}
  undo(map){if(!this.undoStack.length)return null;this.redoStack.push(serialize(map));return validate(this.undoStack.pop());}
  redo(map){if(!this.redoStack.length)return null;this.undoStack.push(serialize(map));return validate(this.redoStack.pop());}
}
