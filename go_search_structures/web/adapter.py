import json
from workbench.native import execute
from workbench.validation import lines, text, integer

def run(data):
    words=lines(data,'words');prefix=text(data,'prefix');limit=integer(data,'limit',10,1,100)
    matches=json.loads(execute('go_search_structures',json.dumps(dict(words=words,prefix=prefix,limit=limit)))) or []
    return dict(words=sorted(set(words)),prefix=prefix,matches=matches,limit=limit)
