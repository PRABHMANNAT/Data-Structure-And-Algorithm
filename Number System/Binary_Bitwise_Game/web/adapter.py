from workbench.native import execute
from workbench.validation import integer, text

def run(data):
    a=integer(data,'a',0,0,255);b=integer(data,'b',0,0,255);operation=text(data,'operation','AND')
    if operation not in {'AND','OR','XOR','NOT','SHL','SHR','ROTL','ROTR'}:raise ValueError('Unknown bit operation')
    if operation in {'SHL','SHR','ROTL','ROTR'} and b>7:raise ValueError('Shift counts must be 0–7')
    value=int(execute('Number System/Binary_Bitwise_Game',f'{operation} {a} {b}',sources=['src/bitops.cpp']))
    return dict(a=a,b=b,operation=operation,value=value,changed=(a^value).bit_count())
