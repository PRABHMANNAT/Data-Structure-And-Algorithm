#pragma once
#include <unordered_map>
#include <vector>
namespace dsa { struct Edge{int to,weight{1};};using Graph=std::unordered_map<int,std::vector<Edge>>;inline void add_edge(Graph&g,int from,int to,int weight=1){g[from].push_back({to,weight});g.try_emplace(to);} }
