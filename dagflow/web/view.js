import {el,note} from '/workbench/dom.js';
import {metrics,table,sequence} from '/workbench/results.js';
import {bars,graph} from '/workbench/charts.js';
import {timeline,scatter,tracePlayer,diffView,sparkline,bitgrid,matrix,ring,format} from '/workbench/lab_visuals.js';
if(!document.querySelector('link[data-lab="dagflow"]'))document.head.append(el('link',{rel:'stylesheet',href:'/dagflow/web/style.css','data-lab':'dagflow'}));
export function render(node,r){
  node.classList.add('advanced-result','lab-dagflow');
  node.append(metrics(r.metrics),timeline(r.timeline),table(['Task','Earliest','Latest','Slack'],r.tasks.map(t=>[t.name,t.earliest,t.latest,t.slack])),sequence(r.order,'Topological order'));
}
