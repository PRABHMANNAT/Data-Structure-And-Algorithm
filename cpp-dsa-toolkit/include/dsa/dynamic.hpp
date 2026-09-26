#pragma once
#include <algorithm>
#include <vector>
namespace dsa { inline int knapsack01(const std::vector<int>&w,const std::vector<int>&v,int capacity){std::vector<int>dp(capacity+1);for(std::size_t i=0;i<w.size();++i)for(int c=capacity;c>=w[i];--c)dp[c]=std::max(dp[c],dp[c-w[i]]+v[i]);return dp[capacity];}inline int lis_length(const std::vector<int>&v){std::vector<int>tails;for(int x:v){auto it=std::lower_bound(tails.begin(),tails.end(),x);if(it==tails.end())tails.push_back(x);else*it=x;}return static_cast<int>(tails.size());} }
