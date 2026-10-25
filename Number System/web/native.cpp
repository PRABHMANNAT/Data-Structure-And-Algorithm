#define main original_console_main
#include "../decimal_to_binary.cpp"
#undef main
int main(){long long value;if(!(std::cin>>value))return 2;std::cout<<decimalToBinary(value)<<'\n';return 0;}
