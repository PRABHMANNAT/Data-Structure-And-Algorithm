import {el,note} from '/workbench/dom.js';
import {metrics,table,sequence} from '/workbench/results.js';
import {bars,graph} from '/workbench/charts.js';
import {timeline,scatter,tracePlayer,diffView,sparkline,bitgrid,matrix,ring,format} from '/workbench/lab_visuals.js';
if(!document.querySelector('link[data-lab="spatialdesk"]'))document.head.append(el('link',{rel:'stylesheet',href:'/spatialdesk/web/style.css','data-lab':'spatialdesk'}));
export function render(node,r){
  node.classList.add('advanced-result','lab-spatialdesk');
  node.append(metrics(r.metrics),scatter(r.points,r.query,r.neighbors.map(n=>n[0]),r.radius),table(['Neighbor','Distance'],r.neighbors),el('div',{},el('h3',{},'Within the radius'),sequence(r.inside),el('h3',{},'Visited in kNN order'),sequence(r.visited)));
}
