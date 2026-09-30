import { STORAGE_KEY } from "./config.js";
export function loadSession() { try { return JSON.parse(localStorage.getItem(STORAGE_KEY)) ?? {}; } catch { return {}; } }
export function saveSession(state) { const session={ puzzleId:state.puzzle.id, values:state.values, selected:state.selected, direction:state.direction, activeTab:state.activeTab, elapsed:state.elapsed, theme:state.theme, marks:state.marks }; localStorage.setItem(STORAGE_KEY,JSON.stringify(session)); }
export function clearSession() { localStorage.removeItem(STORAGE_KEY); }
