#include "cashflow/balance_calculator.hpp"
#include "cashflow/heap_settler.hpp"
#include <cassert>

int main() { cashflow::BalanceCalculator calculator; auto balances=calculator.calculate({{"Ana",900,{"Ana","Ben","Cy"}}}); assert(balances.at("Ana")==600); assert(balances.at("Ben")==-300); auto payments=cashflow::HeapSettler{}.settle(balances); assert(payments.size()==2); assert(payments[0].amount==300); }
