import {el, note, button, download} from '/workbench/dom.js';
import {metrics, table, sequence} from '/workbench/results.js';
import {bars, graph, bits} from '/workbench/charts.js';

export function render(host,data) {
  host.append(metrics([['Unique words',data.words.length],['Suggestions',data.matches.length],['Prefix',data.prefix||'(root)']]));
  host.append(el('h3',{},'Completions'),data.matches.length?sequence(data.matches):note('This prefix has no completions in the vocabulary.'));
  host.append(table(['Word','Suffix after prefix'],data.matches.map(word=>[word,word.slice(data.prefix.length)||'(exact match)'])));
  const groups=new Map();
  for(const word of data.words){const first=[...word][0]||'';groups.set(first,(groups.get(first)||0)+1);}
  host.append(el('h3',{},'Root branches'),bars([...groups.values()],[...groups.keys()]));
  host.append(note('Completions are sorted before applying the limit, so repeated runs return the same suggestions. Matching is case-sensitive.'));
}
