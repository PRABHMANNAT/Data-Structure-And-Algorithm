#pragma once
#include <limits>
#include <functional>
#include <queue>
#include <unordered_map>
#include "graph.hpp"
namespace dsa { inline std::unordered_map<int,int>dijkstra(const Graph&g,int source){using State=std::pair<int,int>;std::priority_queue<State,std::vector<State>,std::greater<>>q;std::unordered_map<int,int>d;for(auto const&[v,_]:g)d[v]=std::numeric_limits<int>::max();d[source]=0;q.push({0,source});while(!q.empty()){auto[dist,v]=q.top();q.pop();if(dist!=d[v])continue;for(auto e:g.at(v))if(dist<=std::numeric_limits<int>::max()-e.weight&&dist+e.weight<d[e.to]){d[e.to]=dist+e.weight;q.push({d[e.to],e.to});}}return d;} }
