from workbench.native import execute
from workbench.validation import integer, text

def run(data):
    value=integer(data,'decimal',42,0,1000000)
    binary=execute('Binary Game',str(value))
    remaining=abs(value);steps=[]
    while remaining:
        steps.append([remaining,remaining//2,remaining%2]);remaining//=2
    if not steps:steps=[[0,0,0]]
    result=dict(decimal=value,binary=binary,steps=steps)
    answer=text(data,'answer').strip()
    if not answer or any(ch not in '01' for ch in answer):raise ValueError('Your answer must contain only binary digits')
    result.update(answer=answer,correct=int(answer,2)==value)
    return result
