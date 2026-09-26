#pragma once
#include <algorithm>
#include <vector>
namespace dsa { struct Interval{int start,end;};inline std::vector<Interval>merge_intervals(std::vector<Interval>v){if(v.empty())return{};std::sort(v.begin(),v.end(),[](auto a,auto b){return a.start<b.start;});std::vector<Interval>out{v.front()};for(auto x:std::vector<Interval>(v.begin()+1,v.end())){if(x.start<=out.back().end)out.back().end=std::max(out.back().end,x.end);else out.push_back(x);}return out;} }
