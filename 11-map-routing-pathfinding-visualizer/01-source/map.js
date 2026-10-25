import {key,point} from './search.js';
export const palette={base:'#f8f8f2',grid:'#e7e9df',wall:'#363e33',visited:'#dce8ca',frontier:'#b6d4b9',path:'#9cbb57',start:'#3e6638',end:'#b35f3d'};
export function draw(canvas,map,visual,cursor=null){
  const rect=canvas.getBoundingClientRect(),ratio=window.devicePixelRatio||1;
  if(canvas.width!==Math.round(rect.width*ratio)||canvas.height!==Math.round(rect.height*ratio)){canvas.width=Math.round(rect.width*ratio);canvas.height=Math.round(rect.height*ratio);}
  const ctx=canvas.getContext('2d');ctx.setTransform(ratio,0,0,ratio,0,0);
  const w=rect.width/map.cols,h=rect.height/map.rows;
  ctx.fillStyle=palette.grid;ctx.fillRect(0,0,rect.width,rect.height);
  const visited=new Set(visual.visited),frontier=new Set(visual.frontier),route=new Set(visual.path);
  for(let y=0;y<map.rows;y++)for(let x=0;x<map.cols;x++){
    const name=key({x,y});ctx.fillStyle=map.walls.has(name)?palette.wall:route.has(name)?palette.path:frontier.has(name)?palette.frontier:visited.has(name)?palette.visited:palette.base;
    ctx.fillRect(x*w+.5,y*h+.5,w-1,h-1);
  }
  for(const [p,label,color] of [[map.start,'A',palette.start],[map.end,'B',palette.end]]){
    ctx.fillStyle=color;ctx.fillRect(p.x*w+2,p.y*h+2,w-4,h-4);ctx.fillStyle='#fffef6';ctx.font=`600 ${Math.max(10,Math.min(w,h)*.46)}px Arial`;ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillText(label,(p.x+.5)*w,(p.y+.5)*h);
  }
  if(cursor){ctx.strokeStyle='#252923';ctx.lineWidth=2;ctx.strokeRect(cursor.x*w+2,cursor.y*h+2,w-4,h-4);}
}
export function pointAt(canvas,map,event){const rect=canvas.getBoundingClientRect();return {x:Math.max(0,Math.min(map.cols-1,Math.floor((event.clientX-rect.left)/rect.width*map.cols))),y:Math.max(0,Math.min(map.rows-1,Math.floor((event.clientY-rect.top)/rect.height*map.rows)))};}
export function paint(map,p,tool){
  const name=key(p);
  if(tool==='start'&&name!==key(map.end)){map.start=p;map.walls.delete(name);}
  else if(tool==='end'&&name!==key(map.start)){map.end=p;map.walls.delete(name);}
  else if(tool==='erase')map.walls.delete(name);
  else if(tool==='wall'&&name!==key(map.start)&&name!==key(map.end))map.walls.add(name);
}
