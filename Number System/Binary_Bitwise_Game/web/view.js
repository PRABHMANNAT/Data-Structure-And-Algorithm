import {el, note, button, download} from '/workbench/dom.js';
import {metrics, table, sequence} from '/workbench/results.js';
import {bars, graph, bits} from '/workbench/charts.js';

export function render(host,data) {
  host.append(metrics([['Result',data.value],['Hex','0x'+data.value.toString(16).toUpperCase().padStart(2,'0')],['Changed bits',data.changed]]));
  host.append(el('h3',{},'Register A'),bits(data.a));
  if(!['NOT','SHL','SHR','ROTL','ROTR'].includes(data.operation))host.append(el('h3',{},'Register B'),bits(data.b));
  host.append(el('h3',{},`${data.operation} → result`),bits(data.value));
  host.append(table(['Bit position','Before','After'],Array.from({length:8},(_,i)=>[7-i,(data.a>>(7-i))&1,(data.value>>(7-i))&1])));
  host.append(note('All operations use the original game’s uint8_t wrappers. Left shifts discard overflow bits; rotations wrap them to the other end.'));
}
