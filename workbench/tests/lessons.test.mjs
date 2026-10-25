import assert from 'node:assert/strict';
import {readFileSync, readdirSync, existsSync} from 'node:fs';
import {fileURLToPath} from 'node:url';
import {resolve} from 'node:path';
const root=fileURLToPath(new URL('../../',import.meta.url));
const source=readFileSync(resolve(root,'workbench/lessons.js'),'utf8');
const {lessons}=await import('data:text/javascript;base64,'+Buffer.from(source).toString('base64'));
const folders=readdirSync(root).map(name=>resolve(root,name));
folders.push(...readdirSync(resolve(root,'Number System')).map(name=>resolve(root,'Number System',name)));
const ids=['routelab','crossword'];
for(const folder of folders){const manifest=resolve(folder,'web/project.json');if(existsSync(manifest))ids.push(JSON.parse(readFileSync(manifest,'utf8')).id);}
assert.deepEqual(Object.keys(lessons).sort(),ids.sort(),'Every reachable project needs a matching lesson');
for(const [id,lesson] of Object.entries(lessons)){
  for(const field of ['topic','idea','example','question','answer','challenge','cost'])assert.ok(typeof lesson[field]==='string'&&lesson[field].trim(),`${id}: missing ${field}`);
  assert.equal(lesson.steps.length,3,id);
  assert.equal(lesson.concepts.length,3,id);
  for(const pair of lesson.concepts)assert.ok(pair.length===2&&pair.every(value=>typeof value==='string'&&value.trim()),id);
}
console.log(`Learning content contracts passed for ${ids.length} projects.`);
