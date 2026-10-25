from workbench.native import execute
from workbench.validation import integer, text

def run(data):
    value=integer(data,'decimal',42,-1000000,1000000)
    binary=execute('Number System',str(value))
    remaining=abs(value);steps=[]
    while remaining:
        steps.append([remaining,remaining//2,remaining%2]);remaining//=2
    if not steps:steps=[[0,0,0]]
    result=dict(decimal=value,binary=binary,steps=steps)
    return result
