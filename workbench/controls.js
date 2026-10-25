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

export function languageFilters(onSelect) {
  const node=el('div',{class:'filters',role:'group','aria-label':'Filter by language'});
  const controls=new Map();
  for(const language of ['All','Python','Go','C++','JavaScript']) {
    const count=el('span',{class:'filter-count','aria-hidden':'true'},'0');
    const control=button([el('span',{},language),count],()=>onSelect(language),'language-filter');
    control.dataset.language=language;node.append(control);controls.set(language,{control,count});
  }
  return {node,update(active,projects){
    for(const [language,{control,count}] of controls){
      const total=projects.filter(project=>language==='All'||project.language===language).length;
      count.textContent=total;control.setAttribute('aria-pressed',String(active===language));
      control.setAttribute('aria-label',`${language}, ${total} ${total===1?'project':'projects'}`);
    }
  }};
}

export function projectSwitcher(projects,current,getSection) {
  const abort=new AbortController();
  const details=el('details',{class:'project-switcher'});
  const summary=el('summary',{'aria-label':'Switch project'},el('span',{},el('small',{},'PROJECT'),el('strong',{},current.title)),icon('chevron'));
  const input=el('input',{type:'search',placeholder:'Find a project…','aria-label':'Find a project',autocomplete:'off'});
  const list=el('div',{class:'switcher-results'});
  const menu=el('div',{class:'switcher-menu'},el('div',{class:'switcher-search'},icon('search'),input),list);
  function render(){
    const query=input.value.trim().toLowerCase();
    const visible=projects.filter(project=>`${project.title} ${project.language} ${project.category}`.toLowerCase().includes(query));
    list.replaceChildren(...visible.map(project=>el('a',{href:`#project/${project.id}/${getSection()||'demo'}`,class:project.id===current.id?'selected':'',...(project.id===current.id?{'aria-current':'page'}:{})},el('span',{},project.title),el('small',{},project.language))));
    if(!visible.length)list.append(el('p',{class:'switcher-empty'},'No matching projects. Try a different word.'));
  }
  const close=()=>{details.open=false;summary.focus();};
  details.addEventListener('toggle',()=>{if(details.open){render();input.focus();}});
  input.addEventListener('input',render);
  input.addEventListener('keydown',event=>{if(event.key==='ArrowDown'){event.preventDefault();list.querySelector('a')?.focus();}});
  details.addEventListener('keydown',event=>{
    if(event.key==='Escape'){event.preventDefault();event.stopPropagation();close();return;}
    if(!event.target.matches('.switcher-results a'))return;
    const links=[...list.querySelectorAll('a')],index=links.indexOf(event.target);
    const next=event.key==='ArrowDown'?index+1:event.key==='ArrowUp'?index-1:event.key==='Home'?0:event.key==='End'?links.length-1:null;
    if(next!==null){event.preventDefault();links[(next+links.length)%links.length]?.focus();}
  });
  details.addEventListener('focusout',event=>{if(event.relatedTarget&&!details.contains(event.relatedTarget))details.open=false;});
  document.addEventListener('pointerdown',event=>{if(details.open&&!details.contains(event.target))details.open=false;},{signal:abort.signal});
  details.append(summary,menu);render();
  return {node:details,dispose:()=>abort.abort()};
}

document.addEventListener('keydown',event=>{
  if(event.key!=='/'||event.ctrlKey||event.metaKey||event.altKey)return;
  const target=event.target;
  if(target instanceof HTMLElement && (target.matches('input,textarea,select')||target.isContentEditable))return;
  const input=document.querySelector('input[aria-label="Search experiments"]');
  if(input){event.preventDefault();input.focus();}
});
