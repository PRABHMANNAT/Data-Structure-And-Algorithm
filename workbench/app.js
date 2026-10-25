import {el, button, note, announce} from './dom.js';
import {read, write, favorite, recordRun, history} from './storage.js';
import {createForm} from './forms.js';
import {resultShell, compare} from './results.js';
import {collectionIntro, artwork, learningPanel} from './learning.js';
import {lessons} from './lessons.js';
import {searchBox,languageFilters} from './controls.js';
import {icon} from './icons.js';

const browserProjects = [
  {id:'routelab',title:'RouteLab',description:'Draw a map. Watch Dijkstra and A* find their way through it.',language:'JavaScript',category:'Graph algorithms',href:'/11-map-routing-pathfinding-visualizer/01-source/'},
  {id:'crossword',title:'The Daily Grid',description:'A quiet word puzzle, with a keyboard-first grid and a little computer science.',language:'JavaScript',category:'Word games',href:'/12-crossword-puzzle-game/'}
];
let projects = [], filter = 'All', query = '', onlyFavorites = false, routeVersion = 0;
const root = document.querySelector('#app');
function shell() {
  const rail = el('aside', {class:'rail'},
    el('a', {class:'wordmark',href:'#'},el('span',{class:'mark','aria-hidden':true},'fn'),el('span',{},'Fieldnotes',el('small',{},'An algorithm collection'))),
    el('p',{class:'rail-caption'},'YOUR WORKBENCH'),
    el('nav',{'aria-label':'Main navigation'},
      el('a',{href:'#',class:'active',id:'all-link'},icon('grid'),el('span',{},'All experiments'),el('span',{class:'nav-count',id:'all-count'},'21')),
      el('a',{href:'#favorites',id:'favorites-link'},icon('bookmark'),el('span',{},'Saved collection'),el('span',{class:'nav-count',id:'saved-count'},'0'))),
    el('div',{class:'rail-note'},el('span',{class:'rail-dot','aria-hidden':'true'}),el('span',{},'A little theory.',el('br'),'A lot of trying things.')),
    el('div',{class:'rail-bottom'},el('a',{href:'https://github.com/PRABHMANNAT/Data-Structure-And-Algorithm',target:'_blank',rel:'noopener noreferrer'},icon('code'),'Explore the source ↗'),el('p',{},'Python / Go / C++ / Web')));
  const main = el('main', {id:'main',class:'main',tabindex:'-1'});
  root.replaceChildren(el('div', {class:'shell'}, rail, main), el('p', {id:'live',class:'sr-only','aria-live':'polite'}));
  return main;
}
const main = shell();
function updateRail(){
  const saved=read('favorites',[]);
  document.querySelector('#saved-count').textContent=projects.filter(project=>saved.includes(project.id)).length;
  document.querySelector('#all-count').textContent=projects.length;
  for(const [id,active] of [['all-link',!onlyFavorites],['favorites-link',onlyFavorites]]){
    const link=document.getElementById(id);link.classList.toggle('active',active);
    if(active)link.setAttribute('aria-current','page');else link.removeAttribute('aria-current');
  }
}

function topline(text = 'A practical study of data & decisions') {
  return el('div', {class:'topline'}, el('span', {}, text), el('a', {href:'https://github.com/PRABHMANNAT/Data-Structure-And-Algorithm',target:'_blank',rel:'noopener noreferrer'}, 'View source ↗'));
}
function footer() { return el('footer', {class:'footnote'}, el('span', {}, 'FIELDNOTES / DATA STRUCTURES & ALGORITHMS'), el('span', {}, 'Made for the curious.')); }
function collection() {
  main.replaceChildren(topline(), collectionIntro(), el('div', {class:'catalogue-heading',id:'catalogue'}, el('div',{},el('p',{class:'eyebrow'},'THE COMPLETE INDEX'),el('h2',{},'Choose your next experiment.')),el('p',{},'Run it. Understand it. Make it your own.')));
  const search = searchBox(query, value => {query=value;renderRows();});
  const filters=languageFilters(language=>{filter=language;renderRows();});
  main.append(el('div', {class:'collection-tools'},search,filters.node));
  const count = el('p', {class:'collection-count','aria-live':'polite'}), list = el('div', {class:'project-list'});
  main.append(count, list, footer());
  function renderRows() {
    const favorites = read('favorites', []);
    updateRail();
    const available=projects.filter(p=>(!onlyFavorites||favorites.includes(p.id))&&`${p.title} ${p.description} ${p.category} ${p.language} ${lessons[p.id].topic}`.toLowerCase().includes(query.trim().toLowerCase()));
    const matched=available.filter(p=>filter==='All'||p.language===filter);
    filters.update(filter,available);
    count.textContent = `${String(matched.length).padStart(2,'0')} ${matched.length===1?'project':'projects'}${onlyFavorites?' in your saved collection':''}`;
    list.replaceChildren();
    matched.forEach(project => {
      const saved = favorites.includes(project.id);
      const star = button(saved?'★':'☆', () => {favorite(project.id); renderRows();}, 'star');
      star.setAttribute('aria-label', `${saved?'Unsave':'Save'} ${project.title}`); star.setAttribute('aria-pressed', saved);
      list.append(el('article', {class:'project-card'}, el('a',{href:'#project/'+project.id+'/demo',class:'art-link','aria-label':'Open '+project.title},artwork(project)),el('div',{class:'card-body'},el('div',{class:'card-meta'},el('span',{},String(projects.indexOf(project)+1).padStart(2,'0')+' / '+lessons[project.id].topic),el('span',{class:'language'},project.language)),el('a', {class:'project-link',href:'#project/'+project.id+'/demo'}, el('strong', {}, project.title), el('p', {}, project.description)),el('div',{class:'card-links'},el('a',{href:'#project/'+project.id+'/demo'},'Open demo ↗'),el('a',{href:'#project/'+project.id+'/logic'},'How it works'),star))));
    });
    if (!matched.length) list.append(el('p', {class:'empty'}, onlyFavorites?'Save an experiment with the star to find it here.':'No experiments found. Try another search or language.'));
  }
  renderRows();
}
async function workspace(id, version, section = 'demo') {
  const project = projects.find(item => item.id===id);
  if (!project) {main.replaceChildren(topline(), el('h1', {}, 'Experiment not found.'), el('a', {href:'#'}, 'Return to the collection')); return;}
  main.replaceChildren(topline('Collection / ' + project.title), el('header', {class:'workspace-title'}, el('a', {class:'eyebrow',href:'#'}, '← ALL EXPERIMENTS'), el('h1', {}, project.title), el('p', {}, project.description)));
  const demoPanel=el('section',{id:'panel-demo',class:'workspace-panel','aria-label':'Implementation demo'});
  const panels={demo:demoPanel,logic:el('section',{id:'panel-logic',class:'workspace-panel','aria-label':'How it works'},learningPanel(project,'logic')),notes:el('section',{id:'panel-notes',class:'workspace-panel','aria-label':'Study notes'},learningPanel(project,'notes'))};
  const nav=el('nav',{class:'workspace-nav','aria-label':'Project sections'});
  for(const [key,label] of [['demo','Demo'],['logic','How it works'],['notes','Study notes']]) {
    const link=el('a',{href:`#project/${id}/${key}`},icon(key==='demo'?'code':key==='logic'?'search':'bookmark'),label);
    nav.append(link);
  }
  const picker=el('select',{'aria-label':'Switch project'},projects.map(p=>el('option',{value:p.id,selected:p.id===id},p.title)));
  picker.addEventListener('change',()=>{location.hash='#project/'+picker.value+'/demo';});
  main.append(el('div',{class:'workspace-navigation'},nav,picker),...Object.values(panels));
  function showSection(selected) {
    const current=panels[selected]?selected:'demo';
    const previous=main.dataset.section;
    main.dataset.section=current;
    for(const [key,panel] of Object.entries(panels))panel.hidden=key!==current;
    nav.style.setProperty('--active-index',String(['demo','logic','notes'].indexOf(current)));
    if(previous!==current&&!window.matchMedia('(prefers-reduced-motion: reduce)').matches){
      panels[current].getAnimations().forEach(animation=>animation.cancel());
      panels[current].animate([{opacity:0,transform:'translateY(6px)'},{opacity:1,transform:'translateY(0)'}],{duration:180,easing:'ease-out'});
    }
    for(const link of nav.querySelectorAll('a')) {if(link.hash.endsWith('/'+current))link.setAttribute('aria-current','page');else link.removeAttribute('aria-current');}
  }
  main.dataset.project=id;
  main.showSection=showSection;
  showSection(section);
  if(project.href){
    demoPanel.append(el('div',{class:'browser-launch'},artwork(project,true),el('div',{},el('p',{class:'eyebrow'},'THE INTERACTIVE WORKSPACE'),el('h2',{},project.title),el('p',{},project.description),el('a',{href:project.href,class:'solid-link'},'Launch full workspace ↗'),el('p',{class:'note'},'The workspace opens on its own page, with room for the full canvas. Use its learning links to return to the explanations.'))));
    main.append(footer());return;
  }
  const output = el('div', {class:'output','aria-live':'polite'});
  output.append(el('div', {class:'placeholder'}, el('div', {class:'diagram','aria-hidden':true}, project.glyph || '[→]'), el('h2', {}, 'Start with a question.'), el('p', {}, project.prompt || 'Adjust the input or load an example. Run the experiment to inspect the result.')));
  const historyNode = el('section', {class:'history','aria-label':'Recent runs'});
  let renderer;
  const form = createForm(project, async input => {
    const response = await fetch('/api/run/'+id, {method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(input)});
    const payload = await response.json();
    if (!response.ok) throw new Error(payload.error || 'The server could not run this experiment.');
    if (version !== routeVersion) return;
    const previous = history(id)[0];
    output.replaceChildren(resultShell(project,payload,input,renderer));
    if (previous) output.append(button('Compare with previous run', () => {output.querySelector('.comparison')?.remove(); output.append(compare(previous.output.result,payload.result));},'text-button'));
    recordRun(id,input,payload); renderHistory(); announce('Experiment complete. Results are ready.');
  });
  form.node.querySelector('button[type="submit"]').disabled=true;
  demoPanel.append(el('div', {class:'workspace'}, form.node, output), historyNode, note(project.note || 'Runs execute locally using the project implementation. Inputs and run history are saved in this browser.'));
  main.append(footer());
  try {
    const module = await import('/'+project.folder+'/web/view.js');
    if (version !== routeVersion) return;
    renderer = module.render;
    form.node.querySelector('button[type="submit"]').disabled=false;
  } catch (error) {output.replaceChildren(note('The result view could not load. Refresh the page to try again.')); return;}
  function renderHistory() {
    const runs = history(id);
    historyNode.replaceChildren(el('div', {class:'history-head'}, el('h2', {}, 'Your recent runs'), button('Clear history', () => {write('runs.'+id,[]);renderHistory();},'text-button')));
    if (!runs.length) {historyNode.append(note('Your last 12 runs will appear here.'));return;}
    historyNode.append(el('div', {class:'history-list'}, runs.map((run,index) => button(`${String(index+1).padStart(2,'0')} · ${new Date(run.at).toLocaleTimeString([], {hour:'2-digit',minute:'2-digit'})}`, () => {form.load(run.input); output.replaceChildren(resultShell(project,run.output,run.input,renderer)); announce('Saved run restored.');}))));
  }
  renderHistory();
}
function route() {
  if(location.hash==='#main'){main.focus();return;}
  if(location.hash==='#catalogue' && document.querySelector('#catalogue')){document.querySelector('#catalogue').scrollIntoView({behavior:'smooth'});return;}
  const [hashId,section='demo']=location.hash.slice(9).split('/');
  const id = location.hash.startsWith('#project/') ? hashId : document.body.dataset.project;
  if(id && main.dataset.project===id && main.showSection){main.showSection(section);return;}
  main.dataset.project='';main.showSection=null;
  const version = ++routeVersion;
  const selected=projects.find(project=>project.id===id);
  document.title=selected?selected.title+' / Fieldnotes':'Fieldnotes — Algorithms, made tangible.';
  onlyFavorites = location.hash === '#favorites';
  updateRail();
  if (id && location.hash !== '#' && location.hash !== '#favorites') workspace(id,version,section);
  else collection();
  if(location.hash==='#catalogue')document.querySelector('#catalogue')?.scrollIntoView();
  else window.scrollTo(0,0);
}
try {
  const response = await fetch('/api/projects');
  if (!response.ok) throw new Error('Server unavailable');
  projects = [...browserProjects,...await response.json()];
  window.addEventListener('hashchange',route); route();
} catch {
  main.replaceChildren(topline(), el('header', {class:'workspace-title'}, el('h1', {}, 'Open your local workbench.'), el('p', {}, 'Start the server from the repository root, then open the address below.'), el('pre', {}, 'python -m workbench.server\nhttp://127.0.0.1:8765'), note('RouteLab and The Daily Grid also work with any static HTTP server.'), el('a', {href:browserProjects[0].href}, 'Open RouteLab ↗'), el('br'), el('br'), el('a', {href:browserProjects[1].href}, 'Open The Daily Grid ↗')));
}
