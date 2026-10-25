import {el, note, button, download} from '/workbench/dom.js';
import {metrics, table, sequence} from '/workbench/results.js';
import {bars, graph, bits} from '/workbench/charts.js';

export function render(host,data) {
  host.append(metrics([['Documents',data.documents],['Matches',data.hits.length],['Revision',data.revision]]));
  if (!data.hits.length) host.append(note('No indexed terms match this query. Try a word from the document bodies.'));
  for (const hit of data.hits) {
    const article=el('article',{class:'search-hit'},el('h3',{},hit.title),el('p',{class:'note'},hit.body));
    article.append(el('p',{class:'mono'},`BM25 ${hit.score} / terms: ${hit.terms.join(', ')}`));host.append(article);
  }
  if (data.hits.length) host.append(bars(data.hits.map(h=>h.score),data.hits.map(h=>h.title)));
  host.append(el('h3',{},'Vocabulary suggestions'),data.suggestions.length?sequence(data.suggestions):note('No terms begin with this prefix.'));
  host.append(note('BM25 ranks terms by frequency and rarity while accounting for document length. Scores are relative to this collection.'));
}
