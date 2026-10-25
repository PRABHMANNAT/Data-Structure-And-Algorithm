import json
from workbench.native import execute
from workbench.validation import numbers

def run(data):
    values=numbers(data)
    ordered=json.loads(execute('go_data_structures_lab',json.dumps(dict(values=values))))
    return dict(original=values,ordered=ordered,note='Min-heap extraction with a custom comparator. Every output value comes from the repository heap.')
