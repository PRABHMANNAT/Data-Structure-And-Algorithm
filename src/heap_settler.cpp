#include "cashflow/heap_settler.hpp"
#include <queue>
#include <stdexcept>

namespace cashflow {
std::vector<Payment> HeapSettler::settle(const std::map<std::string, Cents>& balances) const {
  using Entry = std::pair<Cents, std::string>;
  std::priority_queue<Entry> creditors, debtors;
  Cents total = 0;
  for (const auto& [person, balance] : balances) { total += balance; if (balance > 0) creditors.push({balance, person}); if (balance < 0) debtors.push({-balance, person}); }
  if (total != 0) throw std::invalid_argument("balances must sum to zero");
  std::vector<Payment> payments;
  while (!creditors.empty()) {
    auto [credit, receiver] = creditors.top(); creditors.pop(); auto [debt, sender] = debtors.top(); debtors.pop();
    const auto amount = std::min(credit, debt); payments.push_back({sender, receiver, amount});
    if (credit > amount) creditors.push({credit - amount, receiver}); if (debt > amount) debtors.push({debt - amount, sender});
  }
  return payments;
}
}
