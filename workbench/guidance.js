import {el} from './dom.js';

/** Introductions describe the actual public demo, in everyday language. */
export const introductions={
  routelab:['A route-finding canvas where open squares form a network and barriers block movement. Compare how A* and Dijkstra search for the shortest way across the same map.','An animated search, the final route, and counts of explored cells and route steps.'],
  crossword:['A playable crossword made from authored puzzles. Across and down clues share letters at their crossings, with tools for checking, revealing and revisiting your edits.','Your filled grid, clue progress, elapsed time and a saved puzzle journal.'],
  delivery:['A delivery planner for a network of roads with different travel times. It finds the route with the lowest total time between two stops.','The chosen stops highlighted on the network and the total travel time, or an unreachable result.'],
  graphforge:['A directed road network with a history. Ask for a route at an earlier revision to see how adding connections changes the answer.','The connections available at that revision, the route and its total cost.'],
  transit:['A timetable planner that works with real departure and arrival times. It finds an earliest-arrival journey while respecting the time needed to change services.','An itinerary with connection times, waiting and the total fare; the earliest arrival is the optimization goal.'],
  retrieval:['A small search engine for documents you supply. It ranks matching documents with BM25 and separately suggests words beginning with your chosen prefix.','Ranked document matches, their matched terms and scores, plus prefix suggestions.'],
  strings:['A text-search bench that runs five exact pattern matchers on the same input. It also finds the longest palindromic substring in your text.','All matching start positions, including overlaps, algorithm reports and the palindrome result.'],
  similarity:['A source-code comparison tool that looks for shared structure after normalizing tokens. It combines fingerprints and token-sequence overlap to help you inspect similarities.','A similarity score, token counts and matching source evidence. The score describes overlap and cannot establish who wrote the code.'],
  streamshield:['An event-stream simulator for data that can arrive out of order. A watermark controls late-event acceptance while a sliding window keeps a recent numeric total.','An event-by-event acceptance timeline, watermark changes, window totals and approximate frequency leaders.'],
  'go-collections':['A priority queue demonstration using the repository’s Go min-heap. Values go into the heap and come out one at a time from smallest to largest.','The original sequence and the complete minimum-extraction order, including duplicate values.'],
  'go-journey':['A sorting demonstration using the repository’s Go merge sort. It splits the input into smaller runs and combines the sorted runs into one ordered sequence.','The original and sorted sequences with a visual comparison of their values.'],
  'go-workbench':['A sorting demonstration using the repository’s Go quicksort. It partitions values around a pivot and sorts the resulting regions.','The original and sorted sequences so you can check the result on your own inputs.'],
  'go-ranges':['A range-sum calculator that builds a Fenwick tree and a segment tree over the same array. Both answer the same inclusive interval query.','Both sums and the prefix totals behind the interval, making it easy to cross-check their answers.'],
  'go-prefix':['An autocomplete index using a Go trie. Words share their starting paths, so a prefix query can walk straight to the relevant part of the vocabulary.','Unique indexed words and a limited list of lexicographically ordered completions.'],
  'cpp-toolkit':['A C++ sorting desk with two existing API choices. Merge uses the repository implementation; the current quick-sort entry point delegates to std::sort.','The original and sorted values, with the active implementation identified.'],
  'number-system':['A decimal-to-binary converter using the existing C++ code. The division trail explains how powers of two represent the same integer in a different base.','The binary representation and every division/remainder step. Negative values use a minus sign.'],
  'binary-quest':['A binary practice exercise where you predict the answer before checking it. Your binary input is compared numerically with the decimal target.','Correctness feedback, the expected binary representation and a division trail you can learn from.'],
  bitrealm:['An eight-bit operations bench using the original C++ bit functions. Combine two byte values, flip bits, shift them or rotate them around the byte.','The resulting byte, individual bit positions and how many bits changed from the first value.'],
  cashflow:['A shared-expense calculator that turns purchases into net balances and a settlement plan. Integer cents and a fixed remainder rule keep every split exact.','Who owes or receives money, suggested payments and an exportable settlement table.'],
  huffman:['A lossless text-compression demo using the C++ Huffman codec. It creates a real archive, decodes it and verifies that the restored bytes match the input.','Original and archive sizes, byte frequencies, a round-trip check and a downloadable .huf file.'],
};

export function projectIntroduction(project) {
  const [about,outcome]=introductions[project.id];
  return el('div',{class:'project-introduction'},el('p',{},about),el('p',{class:'project-outcome'},el('strong',{},'What you’ll see'),outcome));
}
