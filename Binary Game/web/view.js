import {el, note, button, download} from '/workbench/dom.js';
import {metrics, table, sequence} from '/workbench/results.js';
import {bars, graph, bits} from '/workbench/charts.js';

export function render(host,data) {
  host.append(metrics([['Decimal',data.decimal],['Binary',data.binary],['Set bits',[...data.binary].filter(b=>b==='1').length]]));
  host.append(el('h3',{},data.correct?'Correct. Every bit counts.':'Try again — inspect the remainders below.'));
  host.append(bits(data.decimal,Math.max(8,data.binary.replace('-','').length)));
  host.append(table(['Dividend','Quotient','Remainder'],data.steps.map(s=>[s[0],s[1],s[2]])));
  host.append(note('Read the remainders from bottom to top. Negative inputs use a minus sign and magnitude; the diagram shows the magnitude bits.'));
}
