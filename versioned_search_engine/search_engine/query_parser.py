from .errors import QuerySyntaxError
from .tokenizer import tokenize
def parse(query):
 tokens=query.replace("("," ( ").replace(")"," ) ").split();out=[]
 for token in tokens:
  upper=token.upper()
  if upper in {"AND","OR","NOT","(",")"}:out.append(upper)
  elif token:out.extend(tokenize(token))
 if not out:raise QuerySyntaxError("query is empty")
 return tuple(out)
