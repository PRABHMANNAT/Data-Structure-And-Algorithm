import {el, button} from './dom.js';
import {lessons} from './lessons.js';
import {icon} from './icons.js';

export function artwork(project, large = false) {
  return el('div',{class:'project-art generated-cover'+(large?' large':''),'aria-hidden':'true'},
    el('img',{class:'cover-image',src:project.cover||'/workbench/assets/covers/'+project.id+'.webp',alt:'',width:960,height:640,loading:'lazy',decoding:'async'}));
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

export function collectionIntro(total = 31) {
  return el('section',{class:'collection-intro'},
    el('div',{class:'intro-copy'},el('p',{class:'eyebrow'},'THE ALGORITHM COLLECTION'),el('h1',{},'Algorithms, hands on.'),el('p',{class:'intro-dek'},`${total} working projects. Run the demo, understand the idea, try something new.`)),
    el('div',{class:'intro-actions'},el('a',{href:'https://github.com/PRABHMANNAT/Data-Structure-And-Algorithm',target:'_blank',rel:'noopener noreferrer',class:'github-star'},icon('star'),'Star on GitHub',el('span',{'aria-hidden':'true'},'↗')),el('span',{class:'intro-meta'},'Python · Go · C++ · JavaScript')));
}

