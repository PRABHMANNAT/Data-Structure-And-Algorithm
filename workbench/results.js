import {el, button, download, note} from './dom.js';
export function metrics(entries) {
  return el('dl', {class:'metrics'}, entries.map(([label,value]) => el('div', {}, el('dt', {}, label), el('dd', {}, value ?? '—'))));
}
export function table(headers, rows) {
  return el('div', {class:'table-scroll'}, el('table', {}, el('thead', {}, el('tr', {}, headers.map(item => el('th', {scope:'col'}, item)))), el('tbody', {}, rows.map(row => el('tr', {}, row.map(item => el('td', {}, item ?? '—')))))));
}
export function sequence(items, label = 'Sequence') {
  return el('div', {class:'sequence', 'aria-label':label}, items.map((item,index) => el('span', {}, el('small', {}, String(index).padStart(2,'0')), el('b', {}, item))));
}
export function inspector(value) {
  return el('details', {class:'inspector'}, el('summary', {}, 'Inspect raw result'), el('pre', {}, JSON.stringify(value, null, 2)));
}
export function resultShell(project, response, input, renderer) {
  const container = el('section', {class:'result-content'});
  container.append(el('div', {class:'section-label'}, el('h2', {}, '02 / Result'), el('span', {class:'mono'}, `${response.elapsed_ms.toFixed(2)} ms · ${project.language}`)));
  renderer(container, response.result, input);
  container.append(inspector(response.result), button('Export result ↓', () => download(project.id + '-result.json', {project:project.id, input, ...response}), 'text-button'));
  return container;
}
export function compare(previous, current) {
  const changes = [];
  for (const key of new Set([...Object.keys(previous), ...Object.keys(current)])) {
    if (JSON.stringify(previous[key]) !== JSON.stringify(current[key])) {
      changes.push([key, JSON.stringify(previous[key]) ?? '—', JSON.stringify(current[key]) ?? '—']);
    }
  }
  return el('section', {class:'comparison'}, el('h3', {}, 'Changes from the previous run'), changes.length ? table(['Field','Previous','Current'], changes) : note('The results are identical.'));
}
