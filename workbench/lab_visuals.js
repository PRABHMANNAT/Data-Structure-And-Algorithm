import {el,button,note} from './dom.js';
export const format=value=>Number(value).toLocaleString(undefined,{maximumSignificantDigits:7});

export function tracePlayer(trace,render){
  if(!trace.length)return note('No algorithm phases were needed for this input.');
  let index=0;const stage=el('div',{class:'trace-stage'}),position=el('output',{'aria-live':'polite'});
  const previous=button('← Previous',()=>{index--;draw();},'trace-button'),next=button('Next →',()=>{index++;draw();},'trace-button');
  const slider=el('input',{type:'range',min:0,max:trace.length-1,value:0,'aria-label':'Inspect algorithm step'});
  slider.addEventListener('input',()=>{index=Number(slider.value);draw();});
  function draw(){stage.replaceChildren(render(trace[index]));position.textContent=`Step ${index+1} / ${trace.length}`;slider.value=index;previous.disabled=index===0;next.disabled=index===trace.length-1;}
  draw();return el('section',{class:'trace-player'},el('div',{class:'trace-controls'},previous,position,next),slider,stage);
}

export function timeline(rows){
  const max=Math.max(1,...rows.map(r=>r.end));
  return el('section',{class:'lab-timeline','aria-label':'Schedule timeline'},rows.map(row=>el('div',{class:'lab-track'},el('span',{},row.task||row.name),el('div',{class:'lab-track-space'},el('div',{class:'lab-track-fill',style:`margin-left:${row.start/max*100}%;width:${Math.max(.3,(row.end-row.start)/max*100)}%`},`${row.start}–${row.end}`)),el('small',{},String(row.worker)))));
}
const NS='http://www.w3.org/2000/svg';
function svg(tag,attrs,text){const node=document.createElementNS(NS,tag);for(const [k,v]of Object.entries(attrs))node.setAttribute(k,v);if(text!==undefined)node.textContent=text;return node;}
export function scatter(points,query,selected,radius){
  const xs=[...points.map(p=>p[1]),query[0]-radius,query[0]+radius],ys=[...points.map(p=>p[2]),query[1]-radius,query[1]+radius];
  const lowX=Math.min(...xs),lowY=Math.min(...ys),span=Math.max(1,Math.max(...xs)-lowX,Math.max(...ys)-lowY);
  const x=v=>35+(v-lowX)/span*330,y=v=>365-(v-lowY)/span*330;
  const chart=svg('svg',{viewBox:'0 0 400 400',role:'img','aria-label':'Cartesian locations; selected nearest neighbors are dark green. The query is a cross.'});
  chart.append(svg('circle',{cx:x(query[0]),cy:y(query[1]),r:radius/span*330,fill:'#dbe8cc','fill-opacity':.6,stroke:'#95aa80'}));
  for(const [name,px,py]of points){chart.append(svg('circle',{cx:x(px),cy:y(py),r:5,fill:selected.includes(name)?'#35522b':'#9ba98c'}));chart.append(svg('text',{x:x(px)+7,y:y(py)-7,'font-size':11,fill:'#35422c'},name));}
  chart.append(svg('path',{d:`M${x(query[0])-7} ${y(query[1])}h14 M${x(query[0])} ${y(query[1])-7}v14`,stroke:'#985d42','stroke-width':2}));return el('div',{class:'lab-scatter'},chart);
}
export function diffView(edits){
  let left=0,right=0;
  return el('div',{class:'lab-diff','aria-label':'Line edit script'},edits.map(edit=>{const a=edit.kind==='insert'?'':++left,b=edit.kind==='delete'?'':++right;return el('div',{class:'diff-line '+edit.kind},el('small',{},a),el('small',{},b),el('span',{},edit.kind==='insert'?'+':edit.kind==='delete'?'−':' '),el('code',{},edit.text||' '));}));
}
export function sparkline(trace){
  const values=trace.flatMap(r=>[r.value,r.median,r.q1,r.q3]),lo=Math.min(...values),hi=Math.max(...values),span=Math.max(1,hi-lo);
  const x=i=>20+i/Math.max(1,trace.length-1)*600,y=v=>160-(v-lo)/span*135;
  const chart=svg('svg',{viewBox:'0 0 640 190',role:'img','aria-label':'Rolling sample values in grey and median in green; outlier signals are orange.'});
  for(const [key,color]of [['value','#a5ac9d'],['median','#476b30']])chart.append(svg('polyline',{points:trace.map((r,i)=>`${x(i)},${y(r[key])}`).join(' '),fill:'none',stroke:color,'stroke-width':2}));
  trace.forEach((r,i)=>{if(r.outlier)chart.append(svg('circle',{cx:x(i),cy:y(r.value),r:4,fill:'#a36c47'}));});
  chart.append(svg('text',{x:20,y:185,'font-size':10,fill:'#6a765d'},`Samples 0–${trace.length-1} · value / rolling median`));return el('div',{class:'lab-sparkline'},chart);
}
export function bitgrid(bits){return el('div',{class:'lab-bitgrid',role:'img','aria-label':`${bits.filter(Boolean).length} of ${bits.length} Bloom bits set`},bits.map((v,i)=>el('i',{class:v?'set':'',title:`Bit ${i}: ${v}`})));}
export function matrix(rows){const max=Math.max(1,...rows.flat());return el('div',{class:'lab-matrix'},rows.map((row,i)=>el('div',{'aria-label':'Counter row '+i},row.map((v,j)=>el('span',{style:`background:rgba(87,120,62,${.08+.8*v/max})`,title:`${i},${j}: ${v}`},v)))));}
export function ring(tokens){
  const chart=svg('svg',{viewBox:'0 0 400 240',role:'img','aria-label':`${tokens.length} virtual hash tokens on a ring`});chart.append(svg('circle',{cx:200,cy:115,r:90,fill:'none',stroke:'#cbd7c0'}));
  const owners=[...new Set(tokens.map(t=>t[1]))];
  for(const [position,name]of tokens){const angle=position*2*Math.PI;chart.append(svg('circle',{cx:200+Math.cos(angle)*90,cy:115+Math.sin(angle)*90,r:3,fill:`hsl(${70+owners.indexOf(name)*53} 25% 40%)`}));}
  chart.append(svg('text',{x:200,y:120,'text-anchor':'middle',fill:'#5e7350','font-size':12},'Virtual-node ownership'));
  return el('div',{class:'lab-ring'},chart,note(owners.join(' / ')));
}
