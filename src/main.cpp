#include "cashflow/balance_calculator.hpp"
#include "cashflow/heap_settler.hpp"
#include <fstream>
#include <iomanip>
#include <iostream>
#include <sstream>

int main(int argc, char** argv) {
  if (argc != 2) { std::cerr << "usage: splitwise <expenses.csv>\n"; return 1; }
  std::ifstream input(argv[1]); if (!input) { std::cerr << "cannot open input\n"; return 1; }
  std::vector<cashflow::Expense> expenses; std::string line;
  while (std::getline(input, line)) { if (line.empty() || line.starts_with("payer,")) continue; std::stringstream row(line); std::string payer, cents, members; std::getline(row,payer,','); std::getline(row,cents,','); std::getline(row,members); std::vector<std::string> participants; std::stringstream group(members); std::string person; while(std::getline(group,person,'|')) participants.push_back(person); expenses.push_back({payer, std::stoll(cents), participants}); }
  try { cashflow::BalanceCalculator calculator; cashflow::HeapSettler settler; for (const auto& payment : settler.settle(calculator.calculate(expenses))) std::cout << payment.from << " pays " << payment.to << " $" << std::fixed << std::setprecision(2) << payment.amount / 100.0 << "\n"; }
  catch (const std::exception& error) { std::cerr << "error: " << error.what() << "\n"; return 2; }
}
