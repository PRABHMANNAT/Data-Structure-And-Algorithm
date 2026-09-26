#pragma once
#include <algorithm>
#include <iterator>
#include <vector>
namespace dsa { template<class T> std::vector<T> merge_sort(std::vector<T> v){if(v.size()<2)return v;auto mid=v.begin()+static_cast<long>(v.size()/2);std::vector<T> left(v.begin(),mid),right(mid,v.end());left=merge_sort(std::move(left));right=merge_sort(std::move(right));std::vector<T> out;std::merge(left.begin(),left.end(),right.begin(),right.end(),std::back_inserter(out));return out;}template<class T>void quick_sort(std::vector<T>&v){std::sort(v.begin(),v.end());} }
