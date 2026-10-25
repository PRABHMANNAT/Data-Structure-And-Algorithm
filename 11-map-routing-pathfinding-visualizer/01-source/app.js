import {search,key} from './search.js';
import {draw,pointAt,paint} from './map.js';
import {restore,save,serialize,MapHistory} from './persistence.js';
import {blank,preset} from './presets.js';
import {exportMap,importMap} from './export.js';
const $=s=>document.querySelector(s),canvas=$('#gridCanvas');
let map=restore(blank),algorithm='astar',tool='wall',speed=3,result=null,index=0,paused=false,timer=null,painting=false,cursor={x:0,y:0};
const edits=new MapHistory(),visual={visited:[],frontier:[],path:[]};
function status(text){$('#status').textContent=text;}
function redraw(){draw(canvas,map,visual,document.activeElement===canvas?cursor:null);$('#gridLabel').textContent=`${map.cols} × ${map.rows}`;$('#densityValue').textContent=`${map.cols} columns`;$('#densityRange').value=map.cols;$('#undoButton').disabled=!edits.undoStack.length;$('#redoButton').disabled=!edits.redoStack.length;}
function clear(){clearTimeout(timer);timer=null;result=null;index=0;paused=false;visual.visited=[];visual.frontier=[];visual.path=[];$('#exploredMetric').textContent='0';$('#routeMetric').textContent='—';$('#frontierMetric').textContent='0';$('#timeMetric').textContent='—';$('#pauseButton').disabled=true;$('#pauseButton').textContent='Pause';$('#runButton').disabled=false;$('#comparison').hidden=true;status('Ready. Start with a barrier or find a route.');redraw();}
function changed(){clear();save(map);cursor.x=Math.min(cursor.x,map.cols-1);cursor.y=Math.min(cursor.y,map.rows-1);redraw();}
function tick(){
  if(!result)return;
  const count=paused?1:[1,2,5,result.frames.length][speed-1];
  for(let n=0;n<count&&index<result.frames.length;n++,index++){const frame=result.frames[index];visual.visited.push(frame.current);visual.frontier=frame.frontier;}
  $('#exploredMetric').textContent=index;$('#frontierMetric').textContent=`${visual.frontier.length} / ${result.peak}`;
  if(index>=result.frames.length){
    visual.path=result.path;visual.frontier=[];$('#routeMetric').textContent=result.path.length?result.path.length-1:'—';$('#timeMetric').textContent=result.elapsed.toFixed(2)+' ms';$('#frontierMetric').textContent=`0 / ${result.peak}`;$('#pauseButton').disabled=true;$('#runButton').disabled=false;
    status(result.path.length?`Route found. ${result.path.length-1} steps, ${result.explored} cells explored.`:'No route. Try removing a barrier or changing the destination.');
  }else {status(`${paused?'Paused':'Searching'} at cell ${result.frames[index-1].current}. ${index} explored.`);if(!paused)timer=setTimeout(tick,[55,25,12,0][speed-1]);}
  redraw();
}
function run(step=false){
  if(!result||index>=result.frames.length){clear();result=search(map,algorithm);index=0;}
  clearTimeout(timer);paused=step;$('#runButton').disabled=!step;$('#pauseButton').disabled=false;$('#pauseButton').textContent=step?'Resume':'Pause';tick();
}
function pause(){if(!result||index>=result.frames.length)return;paused=!paused;clearTimeout(timer);$('#pauseButton').textContent=paused?'Resume':'Pause';$('#runButton').disabled=!paused;if(!paused)tick();else status(`Paused after ${index} explored cells. Step or resume to continue.`);}
function setTool(value){tool=value;document.querySelectorAll('[data-tool]').forEach(b=>b.setAttribute('aria-pressed',b.dataset.tool===tool));}
function edit(point){paint(map,point,tool);changed();}
canvas.addEventListener('pointerdown',event=>{if(event.button!==0)return;edits.push(map);painting=true;canvas.setPointerCapture(event.pointerId);edit(pointAt(canvas,map,event));});
canvas.addEventListener('pointermove',event=>{if(painting&&['wall','erase'].includes(tool))edit(pointAt(canvas,map,event));});
for(const type of ['pointerup','pointercancel','lostpointercapture'])canvas.addEventListener(type,()=>painting=false);
canvas.addEventListener('focus',redraw);canvas.addEventListener('blur',redraw);
canvas.addEventListener('keydown',event=>{const moves={ArrowLeft:[-1,0],ArrowRight:[1,0],ArrowUp:[0,-1],ArrowDown:[0,1]};if(moves[event.key]){event.preventDefault();const [dx,dy]=moves[event.key];cursor={x:Math.max(0,Math.min(map.cols-1,cursor.x+dx)),y:Math.max(0,Math.min(map.rows-1,cursor.y+dy))};status(`Cursor ${cursor.x+1}, ${cursor.y+1}. Tool: ${tool}.`);redraw();}else if(event.key==='Enter'){event.preventDefault();edits.push(map);edit({...cursor});}});
document.querySelectorAll('[data-tool]').forEach(button=>button.addEventListener('click',()=>setTool(button.dataset.tool)));
document.querySelectorAll('[data-algorithm]').forEach(button=>button.addEventListener('click',()=>{algorithm=button.dataset.algorithm;document.querySelectorAll('[data-algorithm]').forEach(b=>b.setAttribute('aria-pressed',b===button));$('#explanation').textContent=algorithm==='astar'?'A* uses distance traveled + Manhattan distance to the goal. Every move costs 1; diagonals are excluded.':'Dijkstra always expands the lowest-cost cell first. With unit costs it explores outward, guaranteeing a shortest path.';clear();}));
$('#runButton').addEventListener('click',()=>run());$('#stepButton').addEventListener('click',()=>run(true));$('#pauseButton').addEventListener('click',pause);$('#clearPathButton').addEventListener('click',clear);
$('#clearButton').addEventListener('click',()=>{edits.push(map);map.walls.clear();changed();});
$('#preset').addEventListener('change',event=>{edits.push(map);map=preset(event.target.value,map);changed();});
$('#densityRange').addEventListener('change',event=>{edits.push(map);const cols=Number(event.target.value);map=blank(cols,Math.round(cols/1.6));changed();});
$('#speedRange').addEventListener('input',event=>{speed=Number(event.target.value);$('#speedValue').textContent=['Slow','Steady','Fast','Instant'][speed-1];});
function undo(redo=false){const next=redo?edits.redo(map):edits.undo(map);if(next){map=next;changed();}}
$('#undoButton').addEventListener('click',()=>undo());$('#redoButton').addEventListener('click',()=>undo(true));
$('#exportButton').addEventListener('click',()=>exportMap(map));
$('#importFile').addEventListener('change',async event=>{try{const next=await importMap(event.target.files[0]);edits.push(map);map=next;changed();status('Map loaded. Ready to find a route.');}catch(error){status(error.message);}finally{event.target.value='';}});
$('#compareButton').addEventListener('click',()=>{
  const comparison=$('#comparison');comparison.replaceChildren();
  const heading=document.createElement('h3');heading.textContent='Same terrain. Two strategies.';comparison.append(heading);
  const table=document.createElement('table');
  const rows=[['Algorithm','Explored','Route steps','Time'],...['astar','dijkstra'].map(name=>{const r=search(map,name);return [name==='astar'?'A*':'Dijkstra',r.explored,r.path.length?r.path.length-1:'No route',r.elapsed.toFixed(2)+' ms'];})];
  rows.forEach((values,i)=>{const row=document.createElement('tr');values.forEach(value=>{const cell=document.createElement(i?'td':'th');cell.textContent=value;row.append(cell);});table.append(row);});comparison.append(table);comparison.hidden=false;
});
$('#helpButton').addEventListener('click',()=>$('#helpDialog').showModal());
document.addEventListener('keydown',event=>{
  if(event.target.matches('input,select,textarea,button,a')||$('#helpDialog').open)return;
  const value=event.key.toLowerCase();
  if((event.ctrlKey||event.metaKey)&&value==='z'){event.preventDefault();undo(event.shiftKey);return;}
  if(event.ctrlKey||event.metaKey||event.altKey)return;
  if(value===' '){event.preventDefault();result&&index<result.frames.length?pause():run();}
  else if({w:'wall',e:'erase',s:'start',d:'end'}[value])setTool({w:'wall',e:'erase',s:'start',d:'end'}[value]);
  else if(value==='c')clear();else if(value==='?')$('#helpDialog').showModal();
});
new ResizeObserver(redraw).observe(canvas);clear();
