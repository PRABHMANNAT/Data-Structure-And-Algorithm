import {el, note, button, download} from '/workbench/dom.js';
import {metrics, table, sequence} from '/workbench/results.js';
import {bars, graph, bits} from '/workbench/charts.js';

export function render(host, data) {
  host.append(metrics([['Nodes',data.ordered.length],['Height',data.height],['Found '+data.target,data.found?'Yes':'No']]));
  host.append(el('h3',{},'In-order traversal'),sequence(data.ordered),bars(data.values));
  const rows=[];
  function visit(node, depth=0, side='Root') {
    if (!node) return;
    rows.push([depth,side,node.value]); visit(node.left,depth+1,'Left'); visit(node.right,depth+1,'Right');
  }
  visit(data.tree);
  host.append(el('h3',{},'Branch inspection'),table(['Depth','Branch','Value'],rows));
  host.append(note('Insertion order controls the shape. Try a sorted sequence and compare the height. Duplicate keys take the right branch.'));
}
