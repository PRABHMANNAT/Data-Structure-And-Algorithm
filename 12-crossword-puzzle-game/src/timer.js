export const formatTime=seconds=>`${String(Math.floor(seconds/60)).padStart(2,'0')}:${String(seconds%60).padStart(2,'0')}`;
/** A getter prevents a puzzle switch from leaving the timer bound to old state. */
export function startTimer(getState,onTick,scheduler=window){
  const id=scheduler.setInterval(()=>{const state=typeof getState==='function'?getState():getState;if(!state.paused&&!state.completed){state.elapsed++;onTick(state);}},1000);
  return ()=>scheduler.clearInterval(id);
}
