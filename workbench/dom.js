/** DOM-only rendering keeps algorithm input out of HTML strings. */
export function el(tag, attributes = {}, ...children) {
  const node = document.createElement(tag);
  for (const [name, value] of Object.entries(attributes)) {
    if (name.startsWith('on')) node.addEventListener(name.slice(2).toLowerCase(), value);
    else if (name === 'class') node.className = value;
    else if (name === 'text') node.textContent = value;
    else if (value !== false && value != null) node.setAttribute(name, String(value));
  }
  for (const child of children.flat(Infinity)) {
    if (child != null) node.append(child instanceof Node ? child : document.createTextNode(String(child)));
  }
  return node;
}
export const button = (label, action, className = '') => el('button', {type:'button', class:className, onclick:action}, label);
export function download(name, value, mime = 'application/json') {
  const url = URL.createObjectURL(new Blob([typeof value === 'string' ? value : JSON.stringify(value, null, 2)], {type:mime}));
  const link = el('a', {href:url, download:name});
  document.body.append(link); link.click(); link.remove();
  setTimeout(() => URL.revokeObjectURL(url), 1000);
}
export const note = text => el('p', {class:'note'}, text);
export function announce(message) {
  const live = document.querySelector('#live');
  if (live) live.textContent = message;
}
