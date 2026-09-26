#pragma once
#include <vector>
#include <stdexcept>
#include <utility>
namespace dsa { template<class T> class RingBuffer {std::vector<T> data_;std::size_t start_{},count_{};public:explicit RingBuffer(std::size_t capacity):data_(capacity){if(!capacity)throw std::invalid_argument("capacity must be positive");}void add(T v){if(count_<data_.size()){data_[(start_+count_)%data_.size()]=std::move(v);++count_;}else{data_[start_]=std::move(v);start_=(start_+1)%data_.size();}}std::vector<T> values()const{std::vector<T> out;for(std::size_t i=0;i<count_;++i)out.push_back(data_[(start_+i)%data_.size()]);return out;}}; }
