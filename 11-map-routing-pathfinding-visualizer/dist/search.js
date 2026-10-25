import {MinHeap} from './heap.js';
export const key = point => `${point.x},${point.y}`;
export const point = value => {const [x,y]=value.split(',').map(Number);return {x,y};};
export function search(map,algorithm='astar') {
  const started=performance.now();
  const queue=new MinHeap(),distance=new Map([[key(map.start),0]]),previous=new Map(),closed=new Set(),frontier=new Set([key(map.start)]),frames=[];
  const heuristic=p=>algorithm==='astar'?Math.abs(p.x-map.end.x)+Math.abs(p.y-map.end.y):0;
  queue.push(key(map.start),heuristic(map.start));
  let peak=1;
  while(queue.size){
    const current=queue.pop();if(closed.has(current))continue;
    closed.add(current);frontier.delete(current);
    if(current!==key(map.end)){
      const p=point(current);
      for(const [dx,dy] of [[1,0],[0,1],[-1,0],[0,-1]]){
        const next={x:p.x+dx,y:p.y+dy},nextKey=key(next);
        if(next.x<0||next.y<0||next.x>=map.cols||next.y>=map.rows||map.walls.has(nextKey)||closed.has(nextKey))continue;
        const candidate=distance.get(current)+1;
        if(candidate<(distance.get(nextKey)??Infinity)){
          distance.set(nextKey,candidate);previous.set(nextKey,current);
          queue.push(nextKey,candidate+heuristic(next));frontier.add(nextKey);
        }
      }
    }
    peak=Math.max(peak,frontier.size);
    frames.push({current,frontier:[...frontier],visited:closed.size});
    if(current===key(map.end))break;
  }
  const path=[];
  if(closed.has(key(map.end))){let cursor=key(map.end);while(cursor!=null){path.unshift(cursor);cursor=previous.get(cursor);}}
  return {frames,path,explored:closed.size,peak,elapsed:performance.now()-started,algorithm};
}
