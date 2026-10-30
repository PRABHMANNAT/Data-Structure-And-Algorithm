import {el,note} from '/workbench/dom.js';
import {metrics,table,sequence} from '/workbench/results.js';
import {bars,graph} from '/workbench/charts.js';
import {timeline,scatter,tracePlayer,diffView,sparkline,bitgrid,matrix,ring,format} from '/workbench/lab_visuals.js';
if(!document.querySelector('link[data-lab="flowfoundry"]'))document.head.append(el('link',{rel:'stylesheet',href:'/flowfoundry/web/style.css','data-lab':'flowfoundry'}));
export function render(node,r){
  node.classList.add('advanced-result','lab-flowfoundry');
  node.append(metrics(r.metrics),graph(r.flows.map(e=>[e.source,e.target,e.flow+'/'+e.capacity]),[],true),table(['From','To','Flow','Capacity'],r.flows.map(e=>[e.source,e.target,e.flow,e.capacity])),tracePlayer(r.phases,p=>el('div',{},el('h3',{},'Blocking flow: '+p.pushed),table(['Vertex','Level'],Object.entries(p.levels)))));
}
