import {el,note} from '/workbench/dom.js';
import {metrics,table,sequence} from '/workbench/results.js';
import {bars,graph} from '/workbench/charts.js';
import {timeline,scatter,tracePlayer,diffView,sparkline,bitgrid,matrix,ring,format} from '/workbench/lab_visuals.js';
if(!document.querySelector('link[data-lab="shardring"]'))document.head.append(el('link',{rel:'stylesheet',href:'/shardring/web/style.css','data-lab':'shardring'}));
export function render(node,r){
  node.classList.add('advanced-result','lab-shardring');
  node.append(metrics(r.metrics),bars(r.distribution.map(t=>t[1]),r.distribution.map(t=>t[0])),table(['Key','Ring before','Ring after','Moved','Rendezvous after'],r.assignments.map(t=>[t.key,t.before,t.after,t.moved?'yes':'no',t.rendezvous_after])),ring(r.ring));
}
