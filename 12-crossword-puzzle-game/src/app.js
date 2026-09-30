import { LETTER, DIRECTIONS } from "./config.js";
import { puzzles } from "./puzzles.js";
import { buildWords } from "./word-model.js";
import { createState } from "./state.js";
import { loadSession, saveSession, clearSession } from "./storage.js";
import { startTimer } from "./timer.js";
import { renderBoard, updateBoardState, focusCell } from "./board.js";
import { renderClues, updateCurrentClue } from "./clues.js";
import { renderStatus } from "./status.js";
import { advance, handleArrow, selectWord, toggleDirection } from "./navigation.js";
import { clearWord, resetPuzzle, checkCells, checkPuzzle, revealCells, revealPuzzle, checkCompletion } from "./actions.js";
import { currentWord } from "./selectors.js";
import { announcement } from "./dom.js";

let state; const picker=document.querySelector("#puzzle-picker");
function makeState(puzzleId) { const saved=loadSession(); const puzzle=puzzles.find(item=>item.id===puzzleId)??puzzles[0]; state=createState(puzzle,buildWords(puzzle),saved.puzzleId===puzzle.id?saved:{}); document.documentElement.dataset.theme=state.theme; }
function persist(){saveSession(state);} function redraw({board=false}={}){ if(board)renderBoard(state,selectCell,writeCell,keydown);else updateBoardState(state); renderClues(state,word=>{selectWord(state,word);redraw();focusCell(state.selected);});updateCurrentClue(state);renderStatus(state);persist(); }
function selectCell(key,shouldToggle=false){ if(state.selected===key&&shouldToggle){toggleDirection(state);}else state.selected=key;redraw(); }
function writeCell(event,key){const value=event.target.value.toUpperCase().replace(/[^A-Z]/g,"").slice(-1);event.target.value=value;state.values[key]=value;delete state.marks[key];if(value)advance(state);checkCompletion(state);redraw();focusCell(state.selected);}
function keydown(event){if(event.key===" "){event.preventDefault();toggleDirection(state);redraw();return;}if(handleArrow(state,event.key)){event.preventDefault();redraw();focusCell(state.selected);return;}if(event.key==="Backspace"&&!event.currentTarget.value){event.preventDefault();advance(state,true);delete state.values[state.selected];redraw();focusCell(state.selected);}}
function applyAction(action){const word=currentWord(state);if(action==="clear-word")clearWord(state);if(action==="reset")resetPuzzle(state);if(action==="check-cell")checkCells(state,word?.cells.filter(cell=>cell.key===state.selected)??[]);if(action==="check-word")checkCells(state,word?.cells??[]);if(action==="check-puzzle")checkPuzzle(state);if(action==="reveal-cell")revealCells(state,word?.cells.filter(cell=>cell.key===state.selected)??[]);if(action==="reveal-word")revealCells(state,word?.cells??[]);if(action==="reveal-puzzle")revealPuzzle(state);if(action==="help")document.querySelector("#help-dialog").showModal();checkCompletion(state);redraw();}
function init(){puzzles.forEach(puzzle=>picker.add(new Option(`${puzzle.title} (${puzzle.difficulty})`,puzzle.id)));const saved=loadSession();picker.value=saved.puzzleId??puzzles[0].id;makeState(picker.value);picker.addEventListener("change",()=>{makeState(picker.value);announcement("New puzzle loaded.");redraw({board:true});});document.querySelector("#theme-toggle").addEventListener("click",()=>{state.theme=state.theme==="night"?"day":"night";document.documentElement.dataset.theme=state.theme;redraw();});document.querySelector("#pause-button").addEventListener("click",()=>{state.paused=!state.paused;announcement(state.paused?"Timer paused.":"Timer resumed.");redraw();});document.querySelectorAll("[data-action]").forEach(button=>button.addEventListener("click",()=>applyAction(button.dataset.action)));document.querySelector("#across-tab").addEventListener("click",()=>{state.activeTab=DIRECTIONS.ACROSS;redraw();});document.querySelector("#down-tab").addEventListener("click",()=>{state.activeTab=DIRECTIONS.DOWN;redraw();});window.addEventListener("beforeunload",persist);redraw({board:true});startTimer(state,()=>{renderStatus(state);persist();});}
init();
