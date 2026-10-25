export function blank(cols=28,rows=18){return {cols,rows,start:{x:3,y:Math.floor(rows/2)},end:{x:cols-4,y:Math.floor(rows/2)},walls:new Set()};}
export function preset(name,map,rng=Math.random){
  const result={...map,start:{...map.start},end:{...map.end},walls:new Set()};
  if(name==='random'){
    for(let y=0;y<map.rows;y++)for(let x=0;x<map.cols;x++)if(rng()<.28)result.walls.add(`${x},${y}`);
    // Carve a Manhattan corridor so this example always has a solution.
    let {x,y}=map.start;while(x!==map.end.x){result.walls.delete(`${x},${y}`);x+=Math.sign(map.end.x-x);}while(y!==map.end.y){result.walls.delete(`${x},${y}`);y+=Math.sign(map.end.y-y);}
  }else if(name==='corridor'){
    for(let x=6;x<map.cols-4;x+=5)for(let y=0;y<map.rows;y++)if(y!==(Math.floor(x/5)%2?2:map.rows-3))result.walls.add(`${x},${y}`);
  }
  result.walls.delete(`${map.start.x},${map.start.y}`);result.walls.delete(`${map.end.x},${map.end.y}`);
  return result;
}
