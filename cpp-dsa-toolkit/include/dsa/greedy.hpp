#pragma once
#include <algorithm>
#include <limits>
#include <vector>
namespace dsa { struct Activity{int start,end;};inline std::vector<Activity>select_activities(std::vector<Activity>a){std::sort(a.begin(),a.end(),[](auto x,auto y){return x.end<y.end;});std::vector<Activity>out;int last=std::numeric_limits<int>::min();for(auto x:a)if(x.start>=last){out.push_back(x);last=x.end;}return out;} }
