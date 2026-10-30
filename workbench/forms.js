import {el, button, announce} from './dom.js';
import {read, write} from './storage.js';

export function createForm(project, onRun) {
  const draft = read('draft.' + project.id, project.presets[0].input);
  const fields = new Map();
  const form = el('form', {class:'input-form'});
  const preset = el('select', {'aria-label':'Load an example scenario'}, el('option', {value:''}, 'Load an example…'));
  project.presets.forEach((item, index) => preset.append(el('option', {value:index}, item.name)));
  form.append(el('div', {class:'section-label'}, el('h2', {}, '01 / Input'), preset));
  for (const field of project.fields) {
    const id = 'field-' + field.key;
    const input = field.type === 'textarea'
      ? el('textarea', {id, name:field.key, rows:field.rows || 5, spellcheck:'false', required:field.required!==false, maxlength:12000})
      : field.type === 'select'
        ? el('select', {id, name:field.key}, field.options.map(value => el('option', {value}, value)))
        : el('input', {id, name:field.key, type:field.type || 'text', required:field.required!==false, maxlength:12000, min:field.min, max:field.max, step:field.step||1});
    input.value = draft[field.key] ?? project.presets[0].input[field.key] ?? '';
    fields.set(field.key, input);
    input.setAttribute('aria-describedby',id+'-hint');
    form.append(el('div', {class:'field'}, el('label', {for:id}, field.label), input, el('small', {id:id+'-hint'}, field.hint || '')));
  }
  const error = el('p', {class:'form-error', role:'alert', hidden:true});
  const submit = el('button', {type:'submit', class:'primary'}, 'Run experiment', el('span', {'aria-hidden':true}, '↗'));
  form.append(error, el('div', {class:'form-actions'}, submit, button('Reset', () => load(project.presets[0].input))));
  const values = () => Object.fromEntries([...fields].map(([key, node]) => [key, node.value]));
  function load(input) {
    fields.forEach((node, key) => { node.value = input[key] ?? ''; });
    write('draft.' + project.id, values());
    error.hidden = true;
    announce('Example loaded. Ready to run.');
  }
  preset.addEventListener('change', () => {
    if (preset.value !== '') load(project.presets[Number(preset.value)].input);
    preset.value = '';
  });
  form.addEventListener('input', () => write('draft.' + project.id, values()));
  form.addEventListener('submit', async event => {
    event.preventDefault();
    if (submit.disabled) return;
    submit.disabled = true; submit.textContent = 'Running…'; error.hidden = true;
    try { await onRun(values()); }
    catch (failure) { error.textContent = failure.message; error.hidden = false; announce('Could not run: ' + failure.message); }
    finally { submit.disabled = false; submit.replaceChildren('Run experiment', el('span', {'aria-hidden':true}, '↗')); }
  });
  return {node:form, load, values};
}
