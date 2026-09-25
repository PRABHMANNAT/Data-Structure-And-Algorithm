#pragma once

#include "cashflow/types.hpp"
#include <map>

namespace cashflow {
class BalanceCalculator {
public:
  std::map<std::string, Cents> calculate(const std::vector<Expense>& expenses) const;
};
}
