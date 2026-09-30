import { DIRECTIONS } from "./config.js";
export function createState(puzzle, words, saved={}) { return { puzzle, words, values:saved.values ?? {}, selected:saved.selected ?? words[0]?.cells[0]?.key, direction:saved.direction ?? DIRECTIONS.ACROSS, activeTab:saved.activeTab ?? DIRECTIONS.ACROSS, startedAt:Date.now(), elapsed:saved.elapsed ?? 0, paused:false, theme:saved.theme ?? "day", marks:saved.marks ?? {}, completed:false }; }
export const selection = state => state.selected?.split(":").map(Number) ?? [0,0];
