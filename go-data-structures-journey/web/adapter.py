import json
from workbench.native import execute
from workbench.validation import numbers

def run(data):
    values=numbers(data)
    ordered=json.loads(execute('go-data-structures-journey',json.dumps(dict(values=values))))
    return dict(original=values,ordered=ordered,note='Follow a divide-and-conquer merge sort with duplicate and negative-value inputs.')
