import { DIRECTIONS } from "./config.js";
export const keyFor = (row, col) => `${row}:${col}`;
export const isOpen = (puzzle,row,col) => Boolean(puzzle.grid[row]?.[col] && puzzle.grid[row][col] !== "#");
export const startsWord = (puzzle,row,col,direction) => isOpen(puzzle,row,col) && (direction === DIRECTIONS.ACROSS ? !isOpen(puzzle,row,col-1) && isOpen(puzzle,row,col+1) : !isOpen(puzzle,row-1,col) && isOpen(puzzle,row+1,col));
export function cellsFor(puzzle,row,col,direction) { const cells=[]; const delta=direction === DIRECTIONS.ACROSS ? [0,1] : [1,0]; while(isOpen(puzzle,row,col)) { cells.push({row,col,key:keyFor(row,col),answer:puzzle.grid[row][col]}); row += delta[0]; col += delta[1]; } return cells; }
