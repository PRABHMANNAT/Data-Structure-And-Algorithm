#include <iostream>
#include "dsa/shortest_paths.hpp"
int main(){dsa::Graph g;dsa::add_edge(g,0,1,5);dsa::add_edge(g,0,2,1);dsa::add_edge(g,2,1,1);std::cout<<dsa::dijkstra(g,0).at(1)<<'\n';}
