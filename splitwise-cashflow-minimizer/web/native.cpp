#include "cashflow/balance_calculator.hpp"
    #include "cashflow/heap_settler.hpp"
    #include <iostream>
    #include <sstream>
    int main(){try{std::vector<cashflow::Expense> expenses;std::string payer,members;long long cents;while(std::cin>>payer>>cents>>members){std::vector<std::string> people;std::stringstream group(members);std::string person;while(std::getline(group,person,'|'))people.push_back(person);expenses.push_back({payer,cents,people});}auto balances=cashflow::BalanceCalculator().calculate(expenses);for(const auto& [name,value]:balances)std::cout<<"B "<<name<<' '<<value<<'\n';for(const auto& p:cashflow::HeapSettler().settle(balances))std::cout<<"P "<<p.from<<' '<<p.to<<' '<<p.amount<<'\n';}catch(const std::exception& error){std::cerr<<error.what();return 2;}}
