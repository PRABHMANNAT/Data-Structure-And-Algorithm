const PREFIX = 'fieldnotes.v1.';
export function read(key, fallback) {
  try {
    const value=JSON.parse(localStorage.getItem(PREFIX + key))??fallback;
    if(Array.isArray(fallback)&&!Array.isArray(value))return fallback;
    if(fallback&&typeof fallback==='object'&&!Array.isArray(fallback)&&(typeof value!=='object'||Array.isArray(value)))return fallback;
    return value;
  }
  catch { return fallback; }
}
export function write(key, value) {
  try { localStorage.setItem(PREFIX + key, JSON.stringify(value)); return true; }
  catch { return false; }
}
export function recordRun(project, input, output) {
  const history = read('runs.' + project, []);
  const run = {at:new Date().toISOString(), input, output};
  write('runs.' + project, [run, ...history].slice(0, 12));
  write('recent', project);
  return run;
}
export function history(project) {
  const value = read('runs.' + project, []);
  return Array.isArray(value) ? value.filter(item => item?.input && item?.output).slice(0, 12) : [];
}
export function favorite(id) {
  const favorites = read('favorites', []);
  const next = favorites.includes(id) ? favorites.filter(value => value !== id) : [...favorites, id];
  write('favorites', next);
  return next;
}
