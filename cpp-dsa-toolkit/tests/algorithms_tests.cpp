#include <cassert>
#include "dsa/backtracking.hpp"
#include "dsa/dynamic.hpp"
#include "dsa/shortest_paths.hpp"
#include "dsa/sorting.hpp"
#include "dsa/strings.hpp"
int main(){assert((dsa::merge_sort(std::vector<int>{3,1,2})==std::vector<int>{1,2,3}));assert(dsa::lis_length({10,9,2,5,3,7})==3);assert(dsa::knapsack01({1,3,4},{15,20,30},4)==35);assert(dsa::n_queens(4)==2);assert((dsa::kmp("ababa","aba")==std::vector<int>{0,2}));dsa::Graph g;dsa::add_edge(g,1,2,1);assert(dsa::dijkstra(g,1).at(2)==1);}
