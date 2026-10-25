import {isOpen,keyFor} from './puzzle-utils.js';
import {currentWord} from './selectors.js';
export function renderBoard(state,onSelect,onInput,onKeydown){
  const board=document.querySelector('#crossword-board'),rows=state.puzzle.grid.length,cols=state.puzzle.grid[0].length;
  board.style.gridTemplateColumns=`repeat(${cols},1fr)`;board.style.aspectRatio=`${cols}/${rows}`;
  board.setAttribute('aria-rowcount',rows);board.setAttribute('aria-colcount',cols);board.replaceChildren();
  const numbers=new Map(state.words.map(word=>[word.cells[0].key,word.number]));
  for(let row=0;row<rows;row++)for(let col=0;col<cols;col++){
    const key=keyFor(row,col),cell=document.createElement('div');cell.className='cell';cell.dataset.key=key;cell.setAttribute('role','gridcell');
    if(!isOpen(state.puzzle,row,col)){cell.classList.add('is-block');cell.setAttribute('aria-label','Blocked square');board.append(cell);continue;}
    const number=numbers.get(key);
    if(number){const label=document.createElement('span');label.className='cell-number';label.textContent=number;label.setAttribute('aria-hidden','true');cell.append(label);}
    const input=document.createElement('input');input.maxLength=1;input.autocomplete='off';input.inputMode='text';input.spellcheck=false;input.dataset.key=key;
    input.setAttribute('aria-label',`${number?'Clue '+number+'. ':''}Row ${row+1}, column ${col+1}`);
    let alreadyFocused=false;
    input.addEventListener('pointerdown',()=>{alreadyFocused=document.activeElement===input;});
    input.addEventListener('focus',()=>onSelect(key,false));input.addEventListener('click',()=>onSelect(key,alreadyFocused));
    input.addEventListener('input',event=>onInput(event,key));input.addEventListener('keydown',onKeydown);
    cell.append(input);board.append(cell);
  }
  updateBoardState(state);
}
export function updateBoardState(state){
  const word=currentWord(state),related=new Set(word?.cells.map(cell=>cell.key)||[]);
  document.querySelectorAll('.cell:not(.is-block)').forEach(cell=>{
    const key=cell.dataset.key,input=cell.querySelector('input');
    cell.classList.toggle('is-active',key===state.selected);cell.classList.toggle('is-related',related.has(key));
    cell.classList.toggle('is-correct',state.marks[key]==='correct');cell.classList.toggle('is-wrong',state.marks[key]==='wrong');
    cell.setAttribute('aria-selected',String(key===state.selected));input.value=state.values[key]||'';
    input.tabIndex=key===state.selected?0:-1;input.disabled=state.paused;
    input.setAttribute('aria-invalid',String(state.marks[key]==='wrong'));
  });
  document.querySelector('#crossword-board').classList.toggle('paused',state.paused);
  const cover=document.querySelector('#pause-cover');if(cover)cover.hidden=!state.paused;
}
export const focusCell=key=>document.querySelector(`input[data-key="${key}"]`)?.focus();
