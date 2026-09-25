#include "cashflow/balance_calculator.hpp"
#include <stdexcept>

namespace cashflow {
std::map<std::string, Cents> BalanceCalculator::calculate(const std::vector<Expense>& expenses) const {
  std::map<std::string, Cents> balances;
  for (const auto& expense : expenses) {
    if (expense.amount < 0 || expense.paid_by.empty() || expense.participants.empty()) throw std::invalid_argument("expense must have a payer, non-negative amount, and participants");
    if (expense.amount % static_cast<Cents>(expense.participants.size()) != 0) throw std::invalid_argument("amount must divide equally into cents");
    const auto share = expense.amount / static_cast<Cents>(expense.participants.size());
    balances[expense.paid_by] += expense.amount;
    for (const auto& person : expense.participants) { if (person.empty()) throw std::invalid_argument("participant cannot be empty"); balances[person] -= share; }
  }
  return balances;
}
}
