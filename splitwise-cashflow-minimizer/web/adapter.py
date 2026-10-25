import re
from workbench.native import execute
from workbench.validation import lines, integer

def run(data):
    expenses=[];payload=[];total=0
    for row in lines(data,'expenses',80):
        fields=[part.strip() for part in row.split(',')]
        if len(fields)!=3:raise ValueError('Use payer, cents, participant|participant')
        payer,amount,members=fields;participants=members.split('|')
        if not all(re.fullmatch(r'[A-Za-z0-9_-]{1,30}',name) for name in [payer,*participants]):raise ValueError('Use names with letters, digits, underscores or hyphens')
        if len(set(participants))!=len(participants):raise ValueError('Participants must not be repeated within one expense')
        cents=integer({'v':amount},'v',minimum=1,maximum=100000000)
        total+=cents;expenses.append(dict(payer=payer,cents=cents,participants=participants))
        payload.append(f'{payer} {cents} '+members)
    raw=execute('splitwise-cashflow-minimizer','\n'.join(payload),sources=['src/balance_calculator.cpp','src/heap_settler.cpp'])
    balances=[];payments=[]
    for row in raw.splitlines():
        fields=row.split()
        if fields[0]=='B':balances.append([fields[1],int(fields[2])])
        else:payments.append(dict(source=fields[1],target=fields[2],cents=int(fields[3])))
    return dict(balances=balances,payments=payments,total=total,expenses=expenses)
