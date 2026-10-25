import {el,button} from './dom.js';
import {icon} from './icons.js';

export function searchBox(value,onChange) {
  const input=el('input',{type:'search',placeholder:'Search projects, ideas, languages…','aria-label':'Search experiments',value,autocomplete:'off'});
  const shortcut=el('kbd',{'aria-hidden':'true'},'/');
  const clear=button(icon('close'),()=>{input.value='';update();input.focus();},'search-clear');
  clear.setAttribute('aria-label','Clear search');
  const update=()=>{clear.hidden=!input.value;shortcut.hidden=Boolean(input.value);onChange(input.value);};
  input.addEventListener('input',update);
  input.addEventListener('keydown',event=>{if(event.key==='Escape'){event.preventDefault();input.value='';update();}});
  clear.hidden=!value;shortcut.hidden=Boolean(value);
  return el('div',{class:'search-wrap'},icon('search'),input,shortcut,clear);
}

document.addEventListener('keydown',event=>{
  if(event.key!=='/'||event.ctrlKey||event.metaKey||event.altKey)return;
  const target=event.target;
  if(target instanceof HTMLElement && (target.matches('input,textarea,select')||target.isContentEditable))return;
  const input=document.querySelector('input[type="search"]');
  if(input){event.preventDefault();input.focus();}
});
