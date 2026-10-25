import assert from "node:assert/strict";
import { puzzles } from "../src/puzzles.js";
import { buildWords } from "../src/word-model.js";

for (const puzzle of puzzles) {
  const words = buildWords(puzzle);
  assert.ok(words.length > 0, `${puzzle.id} must create at least one word`);
  const covered=new Set(words.flatMap(word=>word.cells.map(cell=>cell.key)));
  for(let row=0;row<puzzle.grid.length;row++)for(let col=0;col<puzzle.grid[row].length;col++){
    if(puzzle.grid[row][col]!=='#')assert.ok(covered.has(`${row}:${col}`),`${puzzle.id}: every open square needs a clue at ${row}:${col}`);
  }
  for (const word of words) {
    assert.ok(puzzle.clues[word.answer], `${puzzle.id} is missing a clue for ${word.answer}`);
    assert.ok(word.cells.length > 1, `${word.answer} should not be a one-cell word`);
  }
}

console.log(`Validated ${puzzles.length} puzzles.`);

const {createState}=await import('../src/state.js');
const {EditHistory}=await import('../src/history.js');
const {startTimer}=await import('../src/timer.js');
const {loadSession,saveSession}=await import('../src/storage.js');
const {recordCompletion,journal}=await import('../src/stats.js');
const {checkCompletion,clearWord}=await import('../src/actions.js');
const words=buildWords(puzzles[0]),first=words[0].cells[0].key;
const state=createState(puzzles[0],words,{values:{[first]:'A','999:9':'Z'},selected:'bad',elapsed:-10,theme:'evil',marks:{'999:9':'wrong'}});
assert.deepEqual(state.values,{[first]:'A'});assert.equal(state.selected,first);assert.equal(state.elapsed,0);assert.equal(state.theme,'day');assert.deepEqual(state.marks,{});
const edits=new EditHistory();edits.push(state);state.values[first]='B';edits.undo(state);assert.equal(state.values[first],'A');edits.redo(state);assert.equal(state.values[first],'B');
edits.push(state);state.assisted=true;state.values[first]='C';edits.undo(state);assert.equal(state.assisted,true,'undo must retain assistance history');
let active=state,callback,cleared=false;
const stop=startTimer(()=>active,()=>{}, {setInterval(fn){callback=fn;return 4;},clearInterval(id){cleared=id===4;}});
callback();assert.equal(state.elapsed,1);
const second=createState(puzzles[1],buildWords(puzzles[1]));active=second;callback();assert.equal(second.elapsed,1);assert.equal(state.elapsed,1,'old puzzle timer must stop');
second.paused=true;callback();assert.equal(second.elapsed,1);stop();assert.equal(cleared,true);
const memory=new Map();globalThis.localStorage={getItem:key=>memory.get(key)??null,setItem:(key,value)=>memory.set(key,value),removeItem:key=>memory.delete(key)};
saveSession(state);saveSession(second);assert.equal(loadSession(puzzles[0].id).values[first],'B');assert.equal(loadSession().puzzleId,puzzles[1].id);
globalThis.document={querySelector:()=>({textContent:''})};
for(const word of state.words)for(const cell of word.cells)state.values[cell.key]=cell.answer;
assert.equal(checkCompletion(state),true);state.elapsed=40;recordCompletion(state);recordCompletion(state);assert.equal(journal()[state.puzzle.id].solves,1);
clearWord(state);assert.equal(state.completed,false);
globalThis.localStorage={getItem(){throw new Error('blocked');},setItem(){throw new Error('blocked');}};
assert.deepEqual(loadSession(),{});assert.equal(saveSession(state),false);
console.log('Verified restoration, history, timer switching, per-puzzle storage, completion, and private-mode handling.');
