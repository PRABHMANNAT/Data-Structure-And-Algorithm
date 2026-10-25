import json
from workbench.native import execute
from workbench.validation import numbers

def run(data):
    values=numbers(data)
    ordered=json.loads(execute('go-algorithm-workbench',json.dumps(dict(values=values))))
    return dict(original=values,ordered=ordered,note='Run an in-place quicksort and compare its ordered output with the input sequence.')
