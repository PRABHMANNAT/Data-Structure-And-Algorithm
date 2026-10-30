import {el,note} from '/workbench/dom.js';
import {metrics,table,sequence} from '/workbench/results.js';
import {bars,graph} from '/workbench/charts.js';
import {timeline,scatter,tracePlayer,diffView,sparkline,bitgrid,matrix,ring,format} from '/workbench/lab_visuals.js';
if(!document.querySelector('link[data-lab="joinery"]'))document.head.append(el('link',{rel:'stylesheet',href:'/joinery/web/style.css','data-lab':'joinery'}));
export function render(node,r){
  node.classList.add('advanced-result','lab-joinery');
  node.append(metrics(r.metrics),sequence(r.order,'Optimal left-deep join order'),table(['Append relation','Estimated rows','Step cost','Cumulative'],r.ledger.map(t=>[t.added,format(t.rows),format(t.step_cost),format(t.total)])),el('div',{},note(r.note),el('details',{},el('summary',{},'Inspect enumerated subsets'),table(['Subset','Estimated rows','Best cost','Order'],r.states.map(t=>[t.tables.join(', '),format(t.rows),format(t.cost),t.order.join(' → ')])))));
}
