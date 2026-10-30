import {el,note} from '/workbench/dom.js';
import {metrics,table,sequence} from '/workbench/results.js';
import {bars,graph} from '/workbench/charts.js';
import {timeline,scatter,tracePlayer,diffView,sparkline,bitgrid,matrix,ring,format} from '/workbench/lab_visuals.js';
if(!document.querySelector('link[data-lab="quantilewatch"]'))document.head.append(el('link',{rel:'stylesheet',href:'/quantilewatch/web/style.css','data-lab':'quantilewatch'}));
export function render(node,r){
  node.classList.add('advanced-result','lab-quantilewatch');
  node.append(metrics(r.metrics),sparkline(r.trace),table(['Index','Value','Median','Q1','Q3','Prior-window outlier'],r.trace.map(t=>[t.index,t.value,t.median,t.q1,t.q3,t.outlier?'flagged':'—'])),tracePlayer(r.trace,t=>metrics([['Value',t.value],['Active count',t.count],['Median',t.median],['Range',t.minimum+' … '+t.maximum]])));
}
