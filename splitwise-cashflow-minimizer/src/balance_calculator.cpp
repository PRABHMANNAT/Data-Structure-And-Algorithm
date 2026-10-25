#include "cashflow/balance_calculator.hpp"
#include <stdexcept>
#include <algorithm>

namespace cashflow {
std::map<std::string, Cents> BalanceCalculator::calculate(const std::vector<Expense>& expenses) const {
  std::map<std::string, Cents> balances;
  for (const auto& expense : expenses) {
    if (expense.amount < 0 || expense.paid_by.empty() || expense.participants.empty()) throw std::invalid_argument("expense must have a payer, non-negative amount, and participants");
    auto people = expense.participants;
    std::sort(people.begin(), people.end());
    if (people.front().empty() || std::adjacent_find(people.begin(), people.end()) != people.end())
      throw std::invalid_argument("participants must be nonempty and unique");
    const auto share = expense.amount / static_cast<Cents>(people.size());
    const auto remainder = expense.amount % static_cast<Cents>(people.size());
    balances[expense.paid_by] += expense.amount;
    for (std::size_t i = 0; i < people.size(); ++i)
      balances[people[i]] -= share + (static_cast<Cents>(i) < remainder ? 1 : 0);
  }
  return balances;
}
}
