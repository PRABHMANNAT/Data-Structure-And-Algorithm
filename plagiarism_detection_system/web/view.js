import {el, note, button, download} from '/workbench/dom.js';
import {metrics, table, sequence} from '/workbench/results.js';
import {bars, graph, bits} from '/workbench/charts.js';

export function render(host,data) {
  const match=data.matches[0];
  host.append(metrics([['Similarity',match?`${(match.score*100).toFixed(1)}%`:'No shared fingerprints'],['Original tokens',data.left_tokens],['Compared tokens',data.right_tokens]]));
  if (match) {
    host.append(table(['Signal','Value'],[['Containment',match.containment],['Jaccard',match.jaccard],['Sequence',match.sequence],['Shared fingerprints',match.shared_fingerprints]]));
    host.append(el('h3',{},'Matching evidence'),table(['Original line','Compared line','Token span'],match.evidence.map(item=>[item.left_line,item.right_line,item.length])));
  } else host.append(note('No fingerprint pair was found. Very short inputs can fall below the fingerprint window.'));
  const sources=el('details',{},el('summary',{},'Compare source text'),el('h3',{},'Original'),el('pre',{},data.left),el('h3',{},'Comparison'),el('pre',{},data.right));
  host.append(sources,note('Similarity is a review signal, not proof of plagiarism. Renaming identifiers can preserve token structure; shared boilerplate can also increase overlap.'));
}
