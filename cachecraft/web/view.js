import {el,note} from '/workbench/dom.js';
import {metrics,table,sequence} from '/workbench/results.js';
import {bars,graph} from '/workbench/charts.js';
import {timeline,scatter,tracePlayer,diffView,sparkline,bitgrid,matrix,ring,format} from '/workbench/lab_visuals.js';
if(!document.querySelector('link[data-lab="cachecraft"]'))document.head.append(el('link',{rel:'stylesheet',href:'/cachecraft/web/style.css','data-lab':'cachecraft'}));
export function render(node,r){
  node.classList.add('advanced-result','lab-cachecraft');
  node.append(metrics(r.metrics),bars(r.hits,['LRU','LFU']),table(['Step','Key','LRU','LFU','LRU eviction','LFU eviction'],r.trace.map(t=>[t.step,t.key,t.lru_hit?'hit':'miss',t.lfu_hit?'hit':'miss',t.lru_evicted,t.lfu_evicted])),tracePlayer(r.trace,t=>el('div',{},el('h3',{},'Request '+t.key),sequence(t.lru,'LRU oldest → newest'),table(['LFU key','Frequency'],t.lfu))));
}
