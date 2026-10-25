#include "dsa/sorting.hpp"
#include <iostream>
#include <string>
int main(){std::string method;std::cin>>method;std::vector<int> values;int value;while(std::cin>>value)values.push_back(value);if(method=="merge")values=dsa::merge_sort(values);else if(method=="quick")dsa::quick_sort(values);else return 2;for(int item:values)std::cout<<item<<' ';}
