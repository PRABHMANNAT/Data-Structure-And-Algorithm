import {el, button} from './dom.js';
import {lessons} from './lessons.js';
import {icon} from './icons.js';

export function artwork(project, large = false) {
  const topic = lessons[project.id]?.topic || '';
  const kind = project.id==='crossword' ? 'crossword' : /graph|routing|path|trees/i.test(topic) ? 'network' : /bit|binary|number/i.test(topic) ? 'bits' : /word|text|pattern|fingerprint|retrieval|trie/i.test(topic) ? 'type' : 'bars';
  const canvas = el('div', {class:`project-art art-${kind}${large?' large':''}`, 'aria-hidden':'true'});
  if (kind === 'network') {
    const svg = document.createElementNS('http://www.w3.org/2000/svg','svg');
    svg.setAttribute('viewBox','0 0 320 130');
    for (const [x1,y1,x2,y2] of [[40,65,110,25],[40,65,110,105],[110,25,205,65],[110,105,205,65],[205,65,280,25],[205,65,280,105]]) {
      const line = document.createElementNS(svg.namespaceURI,'line');
      for(const [key,value] of Object.entries({x1,y1,x2,y2,stroke:'currentColor','stroke-width':2}))line.setAttribute(key,value);
      svg.append(line);
    }
    for(const [cx,cy] of [[40,65],[110,25],[110,105],[205,65],[280,25],[280,105]]){
      const dot=document.createElementNS(svg.namespaceURI,'circle');
      for(const [key,value] of Object.entries({cx,cy,r:7,fill:'currentColor'}))dot.setAttribute(key,value);
      svg.append(dot);
    }
    canvas.append(svg);
  } else if (kind === 'crossword') {
    canvas.append(el('div',{class:'mini-crossword'},[...['##C##','#ART#','##O##','##S##','##S##'].join('')].map(letter=>el('span',{class:letter==='#'?'blocked':''},letter==='#'?'':letter))));
  } else if (kind === 'bits') canvas.append(el('span',{},'0 1 0 0'),el('strong',{},'1 0 1 1'));
  else if (kind === 'type') canvas.append(el('span',{},project.id==='crossword'?'C R O S S':'a b a b a'),el('strong',{},project.id==='crossword'?'W O R D S':'    └─┬─┘'));
  else [36,70,48,92,60,110,80,126].forEach((height,i)=>canvas.append(el('i',{style:`height:${height/1.5}px`,class:i===5?'accent':''})));
  return canvas;
}

export function learningPanel(project, section) {
  const data=lessons[project.id];
  const page=el('div',{class:'lesson-layout'});
  const content=el('article',{class:'lesson-body'});
  if(section==='logic') {
    content.append(el('p',{class:'eyebrow'},'01 / THE IDEA'),el('h2',{},data.topic),el('p',{class:'lesson-lead'},data.idea),el('h3',{},'From input to answer'),el('ol',{class:'logic-steps'},data.steps.map((step,i)=>el('li',{},el('span',{},String(i+1).padStart(2,'0')),el('p',{},step)))),el('section',{class:'worked-example'},el('p',{class:'eyebrow'},'A WORKED EXAMPLE'),el('p',{},data.example)),el('h3',{},'Cost & boundaries'),el('p',{},data.cost));
  } else {
    content.append(el('p',{class:'eyebrow'},'02 / STUDY NOTES'),el('h2',{},'Three ideas to take away'),el('dl',{class:'concept-list'},data.concepts.map(([term,meaning])=>el('div',{},el('dt',{},term),el('dd',{},meaning)))));
    const answer=el('div',{class:'answer',hidden:true},el('strong',{},'The explanation'),el('p',{},data.answer));
    const reveal=button('Show the answer',()=>{answer.hidden=!answer.hidden;reveal.textContent=answer.hidden?'Show the answer':'Hide the answer';reveal.setAttribute('aria-expanded',String(!answer.hidden));});
    reveal.setAttribute('aria-expanded','false');
    content.append(el('section',{class:'question-block'},el('p',{class:'eyebrow'},'CHECK YOUR UNDERSTANDING'),el('h3',{},data.question),el('p',{},'Form your own answer first, then compare the reasoning.'),reveal,answer));
  }
  const folder=project.folder || (project.id==='routelab'?'11-map-routing-pathfinding-visualizer/01-source':'12-crossword-puzzle-game');
  page.append(content,el('aside',{class:'lesson-margin'},artwork(project),el('p',{class:'eyebrow'},'TRY THIS NEXT'),el('h3',{},'Change one thing.'),el('p',{},data.challenge),el('a',{href:`#project/${project.id}/demo`,class:'lesson-demo-link'},'Go to the demo →'),el('hr'),el('p',{class:'eyebrow'},'READ THE IMPLEMENTATION'),el('a',{href:'https://github.com/PRABHMANNAT/Data-Structure-And-Algorithm/tree/main/'+folder.split('/').map(encodeURIComponent).join('/'),target:'_blank',rel:'noopener noreferrer'},'Browse project source ↗'),el('p',{class:'note'},'These notes describe the demo exposed here. The source project may include additional structures and commands.')));
  return page;
}

export function collectionIntro() {
  return el('section',{class:'collection-intro'},
    el('div',{class:'intro-copy'},el('p',{class:'eyebrow'},'THE ALGORITHM COLLECTION'),el('h1',{},'Algorithms, hands on.'),el('p',{class:'intro-dek'},'21 working projects. Run the demo, understand the idea, try something new.')),
    el('div',{class:'intro-actions'},el('a',{href:'https://github.com/PRABHMANNAT/Data-Structure-And-Algorithm',target:'_blank',rel:'noopener noreferrer',class:'github-star'},icon('star'),'Star on GitHub',el('span',{'aria-hidden':'true'},'↗')),el('span',{class:'intro-meta'},'Python · Go · C++ · JavaScript')));
}

export function studyRoutes() {
  const routes=[['01','Start with the building blocks','Numbers → bits → trees',['number-system','bitrealm','python-structures']],['02','Find a way through','Grid search → roads → timetables',['routelab','delivery','transit']],['03','Turn data into decisions','Search → streams → compression',['retrieval','streamshield','huffman']]];
  return el('section',{class:'study-routes','aria-label':'Suggested study routes'},...routes.map(([n,title,description,ids])=>el('article',{},el('span',{class:'eyebrow'},'STUDY ROUTE / '+n),el('h2',{},title),el('p',{},description),el('div',{},ids.map((id,index)=>el('a',{href:`#project/${id}/logic`,'aria-label':`${index+1}. ${lessons[id].topic}`},`${String(index+1).padStart(2,'0')} ${lessons[id].topic} ↗`))))));
}
