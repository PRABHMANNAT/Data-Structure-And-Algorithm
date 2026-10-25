#define main original_console_main
#include "../binary_quest.cpp"
#undef main
int main(){long long value;if(!(std::cin>>value))return 2;std::cout<<decimalToBinary(static_cast<int>(value))<<'\n';return 0;}
