export const formatTime = seconds => `${String(Math.floor(seconds/60)).padStart(2,"0")}:${String(seconds%60).padStart(2,"0")}`;
export function startTimer(state, onTick) { return window.setInterval(()=>{ if(!state.paused&&!state.completed) { state.elapsed++; onTick(); } },1000); }
