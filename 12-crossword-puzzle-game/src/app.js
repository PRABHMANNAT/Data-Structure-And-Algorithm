import {DIRECTIONS} from './config.js';
import {puzzles} from './puzzles.js';
import {buildWords} from './word-model.js';
import {createState} from './state.js';
import {loadSession,saveSession} from './storage.js';
import {startTimer,formatTime} from './timer.js';
import {renderBoard,updateBoardState,focusCell} from './board.js';
import {renderClues,updateCurrentClue} from './clues.js';
import {renderStatus} from './status.js';
import {advance,handleArrow,selectWord,toggleDirection} from './navigation.js';
import {clearWord,resetPuzzle,checkCells,checkPuzzle,revealCells,revealPuzzle,checkCompletion} from './actions.js';
import {currentWord} from './selectors.js';
import {announcement} from './dom.js';
import {EditHistory} from './history.js';
import {recordCompletion,statsText} from './stats.js';
const $=selector=>document.querySelector(selector),picker=$('#puzzle-picker');
let state,edits=new EditHistory(),completionShown=false;
function makeState(id){
  const puzzle=puzzles.find(item=>item.id===id)||puzzles[0];
  const saved=loadSession(puzzle.id),legacy=loadSession();
  state=createState(puzzle,buildWords(puzzle),Object.keys(saved).length?saved:legacy.puzzleId===puzzle.id?legacy:{});
  picker.value=puzzle.id;document.documentElement.dataset.theme=state.theme;edits=new EditHistory();completionShown=state.completed;
}
function redraw(board=false){
  if(board)renderBoard(state,selectCell,writeCell,keydown);else updateBoardState(state);
  renderClues(state,word=>{if(state.paused)return;selectWord(state,word);redraw();focusCell(state.selected);});updateCurrentClue(state);renderStatus(state);
  $('#undo-button').disabled=!edits.canUndo||state.paused;$('#redo-button').disabled=!edits.canRedo||state.paused;
  for(const tab of ['across','down']){const node=$('#'+tab+'-tab');node.tabIndex=state.activeTab===tab?0:-1;}
  $('#clue-list').setAttribute('aria-labelledby',state.activeTab+'-tab');
  $('#personal-stats').textContent=statsText(state);saveSession(state);
}
function selectCell(key,toggle=false){if(state.paused)return;if(state.selected===key&&toggle)toggleDirection(state);else state.selected=key;const word=currentWord(state);if(word){state.direction=word.direction;state.activeTab=word.direction;}redraw();}
function completion(){if(checkCompletion(state)&&!completionShown){completionShown=true;recordCompletion(state);$('#completion-detail').textContent=`${state.puzzle.title} · ${formatTime(state.elapsed)} · ${state.assisted?'with a little help':'without reveals'}.`;$('#complete-dialog').showModal();}if(!state.completed)completionShown=false;}
function writeCell(event,key){
  if(state.paused)return;edits.push(state);
  const value=event.target.value.toUpperCase().replace(/[^A-Z]/g,'').slice(-1);state.values[key]=value;delete state.marks[key];
  if(value)advance(state);completion();redraw();focusCell(state.selected);
}
function keydown(event){
  if(state.paused)return;
  if((event.ctrlKey||event.metaKey)&&event.key.toLowerCase()==='z'){event.preventDefault();event.shiftKey?edits.redo(state):edits.undo(state);redraw();focusCell(state.selected);return;}
  if(!event.ctrlKey&&!event.metaKey&&!event.altKey&&/^[a-z]$/i.test(event.key)){event.preventDefault();writeCell({target:{value:event.key}},state.selected);return;}
  if(event.key===' '){event.preventDefault();toggleDirection(state);redraw();return;}
  if(handleArrow(state,event.key)){event.preventDefault();redraw();focusCell(state.selected);return;}
  if(event.key==='Tab'){
    event.preventDefault();const words=state.words,word=currentWord(state),index=words.findIndex(item=>item.id===word?.id);
    selectWord(state,words[(index+(event.shiftKey?-1:1)+words.length)%words.length]);redraw();focusCell(state.selected);return;
  }
  if(event.key==='Escape'){event.preventDefault();$('#pause-button').focus();return;}
  if(event.key==='Backspace'){
    event.preventDefault();edits.push(state);if(!state.values[state.selected])advance(state,true);
    delete state.values[state.selected];delete state.marks[state.selected];state.completed=false;completionShown=false;redraw();focusCell(state.selected);
  }
}
async function confirmAction(title,description){
  const dialog=$('#confirm-dialog');$('#confirm-title').textContent=title;$('#confirm-description').textContent=description;dialog.returnValue='';dialog.showModal();
  return new Promise(resolve=>dialog.addEventListener('close',()=>resolve(dialog.returnValue==='confirm'),{once:true}));
}
async function applyAction(action){
  if(action==='help'){$('#help-dialog').showModal();return;}if(state.paused)return;
  if(action==='reset'&&!await confirmAction('Start this grid again?','This clears all letters and resets the timer. Your puzzle journal stays saved.'))return;
  if(action==='reveal-puzzle'&&!await confirmAction('Reveal the whole grid?','This marks the solve as assisted. You can undo the letters, but the assistance record remains.'))return;
  const word=currentWord(state);edits.push(state);
  if(action==='clear-word')clearWord(state);if(action==='reset'){resetPuzzle(state);edits=new EditHistory();completionShown=false;}
  if(action==='check-cell')checkCells(state,word?.cells.filter(cell=>cell.key===state.selected)||[]);
  if(action==='check-word')checkCells(state,word?.cells||[]);if(action==='check-puzzle')checkPuzzle(state);
  if(action==='reveal-cell')revealCells(state,word?.cells.filter(cell=>cell.key===state.selected)||[]);
  if(action==='reveal-word')revealCells(state,word?.cells||[]);if(action==='reveal-puzzle')revealPuzzle(state);
  completion();redraw();
}
function pause(){state.paused=!state.paused;redraw();announcement(state.paused?'Grid and timer paused.':'Back to the puzzle.');if(state.paused)$('#resume-button').focus();else focusCell(state.selected);}
puzzles.forEach(puzzle=>picker.add(new Option(`${puzzle.title} / ${puzzle.difficulty}`,puzzle.id)));
makeState(loadSession().puzzleId||puzzles[0].id);
picker.addEventListener('change',()=>{saveSession(state);makeState(picker.value);redraw(true);announcement('Puzzle loaded. Your previous grid is saved.');});
$('#theme-toggle').addEventListener('click',()=>{state.theme=state.theme==='night'?'day':'night';document.documentElement.dataset.theme=state.theme;redraw();});
$('#pause-button').addEventListener('click',pause);$('#resume-button').addEventListener('click',pause);
document.querySelectorAll('[data-action]').forEach(button=>button.addEventListener('click',()=>applyAction(button.dataset.action)));
for(const direction of ['across','down']){
  const tab=$('#'+direction+'-tab');tab.addEventListener('click',()=>{if(state.paused)return;const word=state.words.find(word=>word.direction===direction&&word.cells.some(cell=>cell.key===state.selected))||state.words.find(word=>word.direction===direction);if(word)selectWord(state,word);redraw();});
  tab.addEventListener('keydown',event=>{if(['ArrowLeft','ArrowRight','Home','End'].includes(event.key)){event.preventDefault();const next=direction==='across'?'down':'across';$('#'+next+'-tab').click();$('#'+next+'-tab').focus();}});
}
$('#undo-button').addEventListener('click',()=>{edits.undo(state);redraw();});$('#redo-button').addEventListener('click',()=>{edits.redo(state);redraw();});
$('#print-button').addEventListener('click',()=>window.print());
window.addEventListener('beforeunload',()=>saveSession(state));
document.addEventListener('visibilitychange',()=>{if(document.hidden&&!state.paused&&!state.completed){state.paused=true;redraw();}});
redraw(true);startTimer(()=>state,()=>{renderStatus(state);saveSession(state);});
