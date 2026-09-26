#pragma once
#include <queue>
#include <optional>
#include "graph.hpp"
namespace dsa { inline std::optional<std::vector<int>>topological_sort(const Graph&g){std::unordered_map<int,int>degree;for(auto const&[v,edges]:g){degree.try_emplace(v);for(auto e:edges)++degree[e.to];}std::queue<int>q;for(auto[v,d]:degree)if(!d)q.push(v);std::vector<int>out;while(!q.empty()){int v=q.front();q.pop();out.push_back(v);for(auto e:g.at(v))if(!--degree[e.to])q.push(e.to);}if(out.size()!=degree.size())return {};return out;} }
