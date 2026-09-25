cmake_minimum_required(VERSION 3.20)
project(splitwise_cashflow_minimizer LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

add_library(cashflow
  src/balance_calculator.cpp
  src/heap_settler.cpp
)
target_include_directories(cashflow PUBLIC include)

add_executable(splitwise src/main.cpp)
target_link_libraries(splitwise PRIVATE cashflow)

enable_testing()
