import {el, note, button, download} from '/workbench/dom.js';
import {metrics, table, sequence} from '/workbench/results.js';
import {bars, graph, bits} from '/workbench/charts.js';

export function render(host,data) {
  host.append(metrics([['Fenwick sum',data.fenwick],['Segment sum',data.segment],['Inclusive range',`${data.left}…${data.right}`]]));
  host.append(bars(data.values,data.values.map((_,i)=>i)));
  host.append(table(['Index','Value','Prefix total','In range'],data.values.map((v,i)=>[i,v,data.prefix[i],i>=data.left&&i<=data.right?'Yes':'—'])));
  host.append(note('Both structures answer the same sum query. Fenwick trees store partial prefix sums; segment trees divide the array into intervals. Try a single-element range or the full array.'));
}
