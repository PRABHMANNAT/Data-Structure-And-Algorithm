#include <iostream>
#include <string_view>
#include <vector>
#include "dsa/shortest_paths.hpp"
#include "dsa/sorting.hpp"
#include "dsa/strings.hpp"
int main(int argc,char**argv){std::string_view demo=argc>1?argv[1]:"dijkstra";if(demo=="dijkstra"){dsa::Graph g;dsa::add_edge(g,1,2,4);dsa::add_edge(g,1,3,1);dsa::add_edge(g,3,2,2);std::cout<<dsa::dijkstra(g,1).at(2)<<'\n';}else if(demo=="sort"){auto v=dsa::merge_sort(std::vector<int>{5,1,4,1});for(int x:v)std::cout<<x<<' ';std::cout<<'\n';}else if(demo=="kmp"){for(int x:dsa::kmp("bananana","ana"))std::cout<<x<<' ';std::cout<<'\n';}else return 2;}
