import {el, note, button, download} from '/workbench/dom.js';
import {metrics, table, sequence} from '/workbench/results.js';
import {bars, graph, bits} from '/workbench/charts.js';

const money=cents=>(cents/100).toFixed(2);
export function render(host,data) {
  host.append(metrics([['Total expenses',money(data.total)],['Transfers',data.payments.length],['People',data.balances.length]]));
  host.append(bars(data.balances.map(row=>row[1]),data.balances.map(row=>row[0])));
  host.append(table(['Person','Net balance','Meaning'],data.balances.map(([name,value])=>[name,money(value),value>0?'Receives':value<0?'Pays':'Settled'])));
  host.append(el('h3',{},'Settlement plan'),data.payments.length?table(['From','To','Amount'],data.payments.map(p=>[p.source,p.target,money(p.cents)])):note('Everyone is already settled.'));
  host.append(button('Export settlements as CSV ↓',()=>download('settlements.csv','from,to,cents\n'+data.payments.map(p=>`${p.source},${p.target},${p.cents}`).join('\n'),'text/csv'),'text-button'));
  host.append(note('The max-heap greedy method reduces transfers but does not guarantee a globally minimum count. Remainder cents follow the library’s deterministic split order.'));
}
