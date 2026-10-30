import {el,note} from '/workbench/dom.js';
import {metrics,table,sequence} from '/workbench/results.js';
import {bars,graph} from '/workbench/charts.js';
import {timeline,scatter,tracePlayer,diffView,sparkline,bitgrid,matrix,ring,format} from '/workbench/lab_visuals.js';
if(!document.querySelector('link[data-lab="bloomgate"]'))document.head.append(el('link',{rel:'stylesheet',href:'/bloomgate/web/style.css','data-lab':'bloomgate'}));
export function render(node,r){
  node.classList.add('advanced-result','lab-bloomgate');
  node.append(metrics(r.metrics),bitgrid(r.bits),table(['Key','Bloom','Truth','Estimate','Actual'],r.checks.map(t=>[t.key,t.maybe?'maybe':'absent',t.present?'present':'absent',t.estimate,t.actual])),el('div',{},el('h3',{},'Count-Min counter rows'),matrix(r.counters),note('Approximate modeled FPR: '+(r.estimated_fpr*100).toFixed(2)+'%; observed absent-query FPR: '+(r.observed_fpr===null?'not available':(r.observed_fpr*100).toFixed(2)+'%'))));
}
