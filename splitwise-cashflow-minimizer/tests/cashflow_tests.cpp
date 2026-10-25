#include "cashflow/balance_calculator.hpp"
#include "cashflow/heap_settler.hpp"
#include <cassert>
#include <stdexcept>

int main() {
  cashflow::BalanceCalculator calculator;
  auto balances=calculator.calculate({{"Ana",900,{"Ana","Ben","Cy"}}});
  assert(balances.at("Ana")==600); assert(balances.at("Ben")==-300);
  auto payments=cashflow::HeapSettler{}.settle(balances);
  assert(payments.size()==2); assert(payments[0].amount==300);
  auto uneven=calculator.calculate({{"Ana",100,{"Cy","Ana","Ben"}}});
  assert(uneven.at("Ana")==66);assert(uneven.at("Ben")==-33);assert(uneven.at("Cy")==-33);
  assert(calculator.calculate({{"Ana",100,{"Ana","Ben","Cy"}}})==uneven);
  bool rejected=false;
  try {calculator.calculate({{"Ana",100,{"Ana","Ana"}}});}catch(const std::invalid_argument&){rejected=true;}
  assert(rejected);
}
