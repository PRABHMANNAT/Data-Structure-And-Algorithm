#pragma once
#include <bit>
namespace dsa { inline int pop_count(unsigned value){return std::popcount(value);}inline bool power_of_two(unsigned value){return value&&!(value&(value-1));} }
