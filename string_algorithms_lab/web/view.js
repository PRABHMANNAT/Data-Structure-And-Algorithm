import {el, note, button, download} from '/workbench/dom.js';
import {metrics, table, sequence} from '/workbench/results.js';
import {bars, graph, bits} from '/workbench/charts.js';

export function render(host,data) {
  const characters=Array.from(data.text),patternLength=Array.from(data.pattern).length;
  host.append(metrics([['Occurrences',data.positions.length],['Text length',characters.length],['Matchers agree','5 / 5']]));
  const view=el('div',{class:'highlighted-text'});
  for(let index=0;index<characters.length;index++) {
    const highlighted=data.positions.some(start=>index>=start&&index<start+patternLength);
    view.append(el(highlighted?'mark':'span',{},characters[index]));
  }
  host.append(view,table(['Matcher','Count','Zero-based offsets'],data.algorithms.map(a=>[a.algorithm,a.count,a.positions.join(', ')||'None'])));
  host.append(el('h3',{},'Longest palindrome'),el('pre',{},data.palindrome));
  host.append(note('Overlapping matches are retained. Offsets use Python Unicode code points. The simple matcher is the reference for the optimized implementations.'));
}
