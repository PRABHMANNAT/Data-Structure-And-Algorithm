import assert from 'node:assert/strict';
import {readFileSync, readdirSync, existsSync} from 'node:fs';
import {fileURLToPath} from 'node:url';
import {resolve} from 'node:path';
import {createHash} from 'node:crypto';
const root=fileURLToPath(new URL('../../',import.meta.url));
const source=readFileSync(resolve(root,'workbench/lessons.js'),'utf8');
const {lessons}=await import('data:text/javascript;base64,'+Buffer.from(source).toString('base64'));
const folders=readdirSync(root).map(name=>resolve(root,name));
folders.push(...readdirSync(resolve(root,'Number System')).map(name=>resolve(root,'Number System',name)));
const ids=['routelab','crossword'],records=[];
for(const folder of folders){const manifest=resolve(folder,'web/project.json');if(existsSync(manifest)){const record=JSON.parse(readFileSync(manifest,'utf8'));records.push({...record,folder});ids.push(record.id);const lessonFile=resolve(folder,'web/lesson.json');if(existsSync(lessonFile))lessons[record.id]=JSON.parse(readFileSync(lessonFile,'utf8'));}}
assert.deepEqual(Object.keys(lessons).sort(),ids.sort(),'Every reachable project needs a matching lesson');
for(const [id,lesson] of Object.entries(lessons)){
  for(const field of ['topic','idea','example','question','answer','challenge','cost'])assert.ok(typeof lesson[field]==='string'&&lesson[field].trim(),`${id}: missing ${field}`);
  assert.equal(lesson.steps.length,3,id);
  assert.equal(lesson.concepts.length,3,id);
  for(const pair of lesson.concepts)assert.ok(pair.length===2&&pair.every(value=>typeof value==='string'&&value.trim()),id);
}
const guidance=readFileSync(resolve(root,'workbench/guidance.js'),'utf8').replace(/^import .*;\r?\n/gm,'');
const {introductions,demoInstructions}=await import('data:text/javascript;base64,'+Buffer.from(guidance).toString('base64'));
const provenance=JSON.parse(readFileSync(resolve(root,'workbench/assets/covers/provenance.json'),'utf8'));
for(const record of records){const file=resolve(record.folder,'web/guide.json');if(existsSync(file)){const guide=JSON.parse(readFileSync(file,'utf8'));introductions[record.id]=[guide.about,guide.outcome];demoInstructions[record.id]=guide.instructions;}}
for(const content of [introductions,demoInstructions])assert.deepEqual(Object.keys(content).sort(),ids,'All projects need introductions, demo steps and generated covers');
const hashes=new Set();
for(const id of ids){
  assert.equal(introductions[id].length,2,id);
  assert.equal(demoInstructions[id].length,3,id);
  assert.ok([...introductions[id],...demoInstructions[id]].every(text=>typeof text==='string'&&text.trim()),id);
  const record=records.find(record=>record.id===id);
  if(record?.cover){const file=readFileSync(resolve(root,record.cover.slice(1)),'utf8');assert.ok(file.startsWith('<svg'),id);hashes.add(createHash('sha256').update(file).digest('hex'));continue;}
  const file=readFileSync(resolve(root,'workbench/assets/covers',provenance.covers[id].file));
  assert.equal(file.subarray(0,4).toString(),'RIFF',id);
  assert.equal(file.subarray(8,12).toString(),'WEBP',id);
  assert.ok(file.length<200000,`${id}: cover should stay compact`);
  hashes.add(createHash('sha256').update(file).digest('hex'));
}
assert.equal(hashes.size,ids.length,'Every project gets its own distinct cover');
console.log(`Lessons, introductions, demo instructions and distinct optimized covers passed for ${ids.length} projects.`);
