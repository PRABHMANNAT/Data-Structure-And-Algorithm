#pragma once
#include <stdexcept>
#include <vector>
namespace dsa { class PrefixSum {std::vector<long long>sum_{0};public:explicit PrefixSum(const std::vector<int>&v){for(int x:v)sum_.push_back(sum_.back()+x);}long long range(int left,int right)const{if(left<0||right<left||right>=static_cast<int>(sum_.size()))throw std::out_of_range("invalid range");return sum_[right]-sum_[left];}}; }
