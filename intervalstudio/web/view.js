import {el,note} from '/workbench/dom.js';
import {metrics,table,sequence} from '/workbench/results.js';
import {bars,graph} from '/workbench/charts.js';
import {timeline,scatter,tracePlayer,diffView,sparkline,bitgrid,matrix,ring,format} from '/workbench/lab_visuals.js';
if(!document.querySelector('link[data-lab="intervalstudio"]'))document.head.append(el('link',{rel:'stylesheet',href:'/intervalstudio/web/style.css','data-lab':'intervalstudio'}));
export function render(node,r){
  node.classList.add('advanced-result','lab-intervalstudio');
  node.append(metrics(r.metrics),timeline(r.bookings.map(j=>({...j,task:j.name,worker:r.chosen.includes(j.name)?'selected':'excluded'}))),table(['Booking','Value','Optimal set','Overlaps query'],r.bookings.map(j=>[j.name,j.value,r.chosen.includes(j.name)?'yes':'no',r.conflicts.includes(j.name)?'yes':'no'])),bars(r.dp,r.dp.map((_,i)=>'prefix '+i)));
}
