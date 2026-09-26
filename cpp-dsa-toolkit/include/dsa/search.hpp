#pragma once
#include <algorithm>
#include <vector>
namespace dsa { template<class T>int binary_search(const std::vector<T>&v,const T&target){auto it=std::lower_bound(v.begin(),v.end(),target);return it!=v.end()&&*it==target?static_cast<int>(it-v.begin()):-1;}template<class T>int lower_bound_index(const std::vector<T>&v,const T&target){return static_cast<int>(std::lower_bound(v.begin(),v.end(),target)-v.begin());} }
