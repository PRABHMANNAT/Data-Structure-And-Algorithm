#pragma once
#include <string_view>
#include <vector>
namespace dsa { inline std::vector<int>kmp(std::string_view text,std::string_view pattern){if(pattern.empty())return{0};std::vector<int>prefix(pattern.size());for(std::size_t i=1,j=0;i<pattern.size();++i){while(j&&pattern[i]!=pattern[j])j=prefix[j-1];if(pattern[i]==pattern[j])prefix[i]=static_cast<int>(++j);}std::vector<int>out;for(std::size_t i=0,j=0;i<text.size();++i){while(j&&text[i]!=pattern[j])j=prefix[j-1];if(text[i]==pattern[j]&&++j==pattern.size()){out.push_back(static_cast<int>(i-j+1));j=prefix[j-1];}}return out;} }
