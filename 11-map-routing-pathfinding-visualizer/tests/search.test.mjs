import test from 'node:test';
import assert from 'node:assert/strict';
import {MinHeap} from '../01-source/heap.js';
import {search} from '../01-source/search.js';
import {blank,preset} from '../01-source/presets.js';
import {validate,serialize,MapHistory} from '../01-source/persistence.js';

test('heap preserves priorities and stable ties',()=>{const heap=new MinHeap();heap.push('last',4);heap.push('first',1);heap.push('second',1);assert.equal(heap.pop(),'first');assert.equal(heap.pop(),'second');assert.equal(heap.pop(),'last');assert.equal(heap.pop(),null);});
test('A* and Dijkstra agree on shortest distance across deterministic terrains',()=>{let seed=19;const rng=()=>((seed=(seed*1664525+1013904223)>>>0)/2**32);for(let i=0;i<30;i++){const map=preset('random',blank(),rng),a=search(map),d=search(map,'dijkstra');assert.equal(a.path.length,d.path.length);assert.ok(a.path.length>0);for(let j=1;j<a.path.length;j++){const [x,y]=a.path[j].split(',').map(Number),[px,py]=a.path[j-1].split(',').map(Number);assert.equal(Math.abs(x-px)+Math.abs(y-py),1);assert.ok(!map.walls.has(a.path[j]));}assert.ok(a.peak<=map.cols*map.rows);}});
test('blocked destination returns no route',()=>{const map=blank();for(let y=0;y<map.rows;y++)map.walls.add(`10,${y}`);assert.equal(search(map).path.length,0);});
test('start equals destination has a zero-step path',()=>{const map=blank();map.end={...map.start};assert.equal(search(map).path.length,1);});
test('saved maps reject invalid dimensions and markers',()=>{const raw=serialize(blank());assert.throws(()=>validate({...raw,cols:100000}));assert.throws(()=>validate({...raw,walls:['-1,0']}));assert.throws(()=>validate({...raw,start:raw.end}));assert.deepEqual(serialize(validate(raw)),raw);});
test('undo and redo restore independent maps',()=>{const map=blank(),history=new MapHistory();history.push(map);map.walls.add('1,1');const before=history.undo(map);assert.equal(before.walls.size,0);assert.equal(history.redo(before).walls.size,1);});
