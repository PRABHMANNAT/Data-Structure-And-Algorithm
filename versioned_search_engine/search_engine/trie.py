class Node:
 def __init__(self):self.children={};self.terminal=False
class TermTrie:
 def __init__(self):self.root=Node()
 def insert(self,term):
  node=self.root
  for char in term:node=node.children.setdefault(char,Node())
  node.terminal=True
 def complete(self,prefix,limit=10):
  node=self.root
  for char in prefix:
   if char not in node.children:return ()
   node=node.children[char]
  out=[]
  def walk(current,suffix):
   if len(out)>=limit:return
   if current.terminal:out.append(prefix+suffix)
   for char in sorted(current.children):walk(current.children[char],suffix+char)
  walk(node,"");return tuple(out)
