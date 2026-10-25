from workbench.native import execute
from workbench.validation import numbers, text

def run(data):
    values=numbers(data);algorithm=text(data,'algorithm','merge')
    if algorithm not in {'merge','quick'}:raise ValueError('Choose merge or quick')
    raw=execute('cpp-dsa-toolkit',algorithm+'\n'+' '.join(map(str,values)))
    return dict(original=values,ordered=list(map(int,raw.split())),note='Merge sort uses the repository implementation. The quick-sort API currently delegates to std::sort.',algorithm=algorithm)
