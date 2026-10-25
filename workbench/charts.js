import {el} from './dom.js';
const NS = 'http://www.w3.org/2000/svg';
function svgNode(tag, attrs = {}, text) {
  const node = document.createElementNS(NS, tag);
  Object.entries(attrs).forEach(([key,value]) => node.setAttribute(key,value));
  if (text != null) node.textContent = text;
  return node;
}
export function bars(values, labels = values.map(String)) {
  const chart = el('div', {class:'bars', role:'img', 'aria-label':values.map((v,i) => `${labels[i]}: ${v}`).join(', ')});
  const max = Math.max(1, ...values.map(value => Math.abs(Number(value))));
  values.forEach((value, index) => {
    const bar = el('div', {class:'bar'});
    const fill = el('span', {class:Number(value) < 0 ? 'negative' : ''});
    fill.style.height = `${Math.max(2, Math.abs(Number(value)) / max * 115)}px`;
    bar.append(el('b', {}, value), fill, el('small', {}, labels[index])); chart.append(bar);
  });
  return chart;
}
export function graph(edges, route = [], directed = false) {
  const names = [...new Set(edges.flatMap(edge => edge.slice(0,2)))];
  const svg = svgNode('svg', {viewBox:'0 0 640 320', role:'img', 'aria-label':`Network of ${names.length} vertices. Route: ${route.join(' to ') || 'none'}.`});
  if(directed){const defs=svgNode('defs'),marker=svgNode('marker',{id:'network-arrow',viewBox:'0 0 10 10',refX:9,refY:5,markerWidth:7,markerHeight:7,orient:'auto-start-reverse'});marker.append(svgNode('path',{d:'M 0 0 L 10 5 L 0 10 z',fill:'#59624c'}));defs.append(marker);svg.append(defs);}
  const positions = new Map(names.map((name,index) => [name, [320 + Math.cos(index / names.length * 2 * Math.PI) * 240, 160 + Math.sin(index / names.length * 2 * Math.PI) * 115]]));
  edges.forEach(([from,to,weight]) => {
    const [x1,y1] = positions.get(from), [x2,y2] = positions.get(to);
    const selected = route.some((name,i) => name === from && route[i+1] === to || name === to && route[i+1] === from);
    const distance=Math.hypot(x2-x1,y2-y1)||1,offset=directed?25:0;
    const attributes={x1,y1,x2:x2-(x2-x1)/distance*offset,y2:y2-(y2-y1)/distance*offset,stroke:selected ? '#476b30' : '#c6c8c0','stroke-width':selected ? 4 : 1.5};
    if(directed)attributes['marker-end']='url(#network-arrow)';
    svg.append(svgNode('line', attributes));
    svg.append(svgNode('text', {x:(x1+x2)/2,y:(y1+y2)/2-7,'text-anchor':'middle',class:'edge-label'}, weight));
  });
  positions.forEach(([cx,cy], name) => {
    svg.append(svgNode('circle', {cx,cy,r:22,fill:route.includes(name)?'#d5ea91':'#f4f3ee',stroke:'#30352b'}));
    svg.append(svgNode('text', {x:cx,y:cy+4,'text-anchor':'middle',class:'node-label'}, name));
  });
  return el('div', {class:'network'}, svg);
}
export function bits(value, width = 8) {
  const binary = Math.abs(Number(value)).toString(2).padStart(width, '0');
  return el('div', {class:'bit-strip', role:'img', 'aria-label':`Binary: ${binary}`}, [...binary].map((bit,index) => el('div', {class:bit === '1' ? 'bit on' : 'bit'}, el('small', {}, 2 ** (binary.length-index-1)), el('strong', {}, bit))));
}
