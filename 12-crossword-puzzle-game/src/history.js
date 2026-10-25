/** Edit history excludes navigation and timer ticks. No storage or DOM required. */
function snapshot(state){return {values:{...state.values},marks:{...state.marks},selected:state.selected,direction:state.direction,activeTab:state.activeTab,completed:state.completed,assisted:state.assisted,checks:state.checks};}
function restore(state,value){const assisted=state.assisted,checks=state.checks;Object.assign(state,value,{values:{...value.values},marks:{...value.marks}});state.assisted=assisted||value.assisted;state.checks=Math.max(checks,value.checks);}
export class EditHistory{
  constructor(){this.past=[];this.future=[];}
  get canUndo(){return this.past.length>0;}
  get canRedo(){return this.future.length>0;}
  push(state){this.past.push(snapshot(state));this.past=this.past.slice(-80);this.future=[];}
  undo(state){if(!this.canUndo)return false;this.future.push(snapshot(state));restore(state,this.past.pop());return true;}
  redo(state){if(!this.canRedo)return false;this.past.push(snapshot(state));restore(state,this.future.pop());return true;}
}
