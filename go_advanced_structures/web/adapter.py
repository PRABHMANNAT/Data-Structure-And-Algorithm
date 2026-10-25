import json
from workbench.native import execute
from workbench.validation import numbers, integer

def run(data):
    values=numbers(data);left=integer(data,'left',0,0,len(values)-1);right=integer(data,'right',len(values)-1,left,len(values)-1)
    result=json.loads(execute('go_advanced_structures',json.dumps(dict(values=values,left=left,right=right))))
    return dict(values=values,left=left,right=right,**result)
