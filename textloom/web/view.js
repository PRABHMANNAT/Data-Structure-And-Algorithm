import {el,note} from '/workbench/dom.js';
import {metrics,table,sequence} from '/workbench/results.js';
import {bars,graph} from '/workbench/charts.js';
import {timeline,scatter,tracePlayer,diffView,sparkline,bitgrid,matrix,ring,format} from '/workbench/lab_visuals.js';
if(!document.querySelector('link[data-lab="textloom"]'))document.head.append(el('link',{rel:'stylesheet',href:'/textloom/web/style.css','data-lab':'textloom'}));
export function render(node,r){
  node.classList.add('advanced-result','lab-textloom');
  node.append(metrics(r.metrics),diffView(r.edits),el('p',{class:'lab-verification'},r.verified?'Forward and inverse patches verified.':'Verification failed.'),el('details',{},el('summary',{},'Patched document'),el('pre',{},r.patched)));
}
