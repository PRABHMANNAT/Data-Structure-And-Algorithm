cmake_minimum_required(VERSION 3.20)
project(cpp_dsa_toolkit LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

add_library(dsa INTERFACE)
target_include_directories(dsa INTERFACE include)

add_executable(dsa_demo src/main.cpp)
target_link_libraries(dsa_demo PRIVATE dsa)

add_executable(structures_tests tests/structures_tests.cpp)
target_link_libraries(structures_tests PRIVATE dsa)
add_executable(algorithms_tests tests/algorithms_tests.cpp)
target_link_libraries(algorithms_tests PRIVATE dsa)

enable_testing()
add_test(NAME structures_tests COMMAND structures_tests)
add_test(NAME algorithms_tests COMMAND algorithms_tests)
