import {el, note, button, download} from '/workbench/dom.js';
import {metrics, table, sequence} from '/workbench/results.js';
import {bars, graph, bits} from '/workbench/charts.js';

export function render(host,data) {
  host.append(metrics([['Values',data.original.length],['Minimum',Math.min(...data.ordered)],['Maximum',Math.max(...data.ordered)]]));
  host.append(el('h3',{},'Input order'),bars(data.original));
  host.append(el('h3',{},'Ordered output'),sequence(data.ordered));
  const rows=data.ordered.map((value,index)=>[index,value,index?value-data.ordered[index-1]:'—']);
  host.append(table(['Position','Value','Gap from previous'],rows));
  host.append(note(data.note));
}
