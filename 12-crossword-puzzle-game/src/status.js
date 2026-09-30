import { percentComplete } from "./selectors.js";
import { formatTime } from "./timer.js";
export function renderStatus(state) { const percent=percentComplete(state); document.querySelector("#puzzle-title").textContent=`${state.puzzle.title} · ${state.puzzle.difficulty}`; document.querySelector("#progress-label").textContent=`${percent}%`; document.querySelector("#progress-bar").style.width=`${percent}%`; document.querySelector("#timer").textContent=formatTime(state.elapsed); document.querySelector("#pause-button").textContent=state.paused?"Resume":"Pause"; }
