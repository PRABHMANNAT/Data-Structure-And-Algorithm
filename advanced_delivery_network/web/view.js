import {el, note, button, download} from '/workbench/dom.js';
import {metrics, table, sequence} from '/workbench/results.js';
import {bars, graph, bits} from '/workbench/charts.js';

export function render(host, data) {
  host.append(metrics([['Route cost',data.cost??'No route'],['Vertices',data.vertices.length],['Connections',data.edges.length]]));
  host.append(graph(data.edges,data.vertices));
  if (data.vertices.length) host.append(sequence(data.vertices,'Shortest route'));
  else host.append(note('No traversable route connects these endpoints. Add a connection or change the destination.'));
  host.append(table(['From','To','Cost'],data.edges));
  host.append(note(data.directed?'Connections are directed; reversing an edge changes the possible journeys.':'Connections are bidirectional. The highlighted route minimizes the sum of edge weights.'));
}
