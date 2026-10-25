#include "bitops.h"
    #include <iostream>
    #include <string>
    int main(){std::string op;int a,b;if(!(std::cin>>op>>a>>b))return 2;uint8_t value=0;if(op=="AND")value=br::bAnd(a,b);else if(op=="OR")value=br::bOr(a,b);else if(op=="XOR")value=br::bXor(a,b);else if(op=="NOT")value=br::bNot(a);else if(op=="SHL")value=br::bShl(a,b);else if(op=="SHR")value=br::bShr(a,b);else if(op=="ROTL")value=br::bRotL(a,b);else if(op=="ROTR")value=br::bRotR(a,b);else return 2;std::cout<<static_cast<int>(value)<<'\n';}
