from .set_ops import difference,intersect,union
def evaluate(index,tokens,universe):
 current=None;op="AND";negate=False
 for token in tokens:
  if token in {"AND","OR"}:op=token;continue
  if token=="NOT":negate=True;continue
  if token in {"(",")"}:continue
  found=index.documents(token);found=difference(universe,found) if negate else found;negate=False
  current=found if current is None else (intersect(current,found) if op=="AND" else union(current,found))
 return current or ()
