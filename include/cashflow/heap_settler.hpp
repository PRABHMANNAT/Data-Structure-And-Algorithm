#pragma once

#include "cashflow/types.hpp"
#include <map>

namespace cashflow {
class HeapSettler {
public:
  std::vector<Payment> settle(const std::map<std::string, Cents>& balances) const;
};
}
