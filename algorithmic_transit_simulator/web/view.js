import {el, note, button, download} from '/workbench/dom.js';
import {metrics, table, sequence} from '/workbench/results.js';
import {bars, graph, bits} from '/workbench/charts.js';

const clock = value => value==null?'No service':`${String(Math.floor(value/60)).padStart(2,'0')}:${String(value%60).padStart(2,'0')}`;
export function render(host,data) {
  host.append(metrics([['Arrival',clock(data.arrival)],['Fare (cents)',data.fare],['Transfers',Math.max(0,data.connections.length-1)]]));
  if (data.arrival==null) {host.append(note('No service meets this departure time and transfer buffer. Try an earlier departure or a smaller buffer.'));return;}
  let time=data.departure;
  const list=el('ol',{class:'route-steps'});
  for (const leg of data.connections) {
    list.append(el('li',{},`${clock(leg.departure)} ${leg.origin} → ${clock(leg.arrival)} ${leg.destination}`,el('small',{},`${leg.line} · wait ${leg.departure-time} min · ride ${leg.arrival-leg.departure} min`)));
    time=leg.arrival;
  }
  host.append(list,table(['Service','From','To','Fare'],data.connections.map(c=>[c.line,c.origin,c.destination,c.fare])));
  host.append(note(`Total journey: ${data.arrival-data.departure} minutes, including waiting. Times above 23:59 continue into the next day.`));
}
