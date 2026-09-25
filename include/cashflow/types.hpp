#pragma once

#include <cstdint>
#include <string>
#include <vector>

namespace cashflow {
using Cents = std::int64_t;
struct Expense { std::string paid_by; Cents amount; std::vector<std::string> participants; };
struct Payment { std::string from; std::string to; Cents amount; };
}
