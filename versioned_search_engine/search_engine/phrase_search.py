from .tokenizer import tokenize
def phrase_matches(index,phrase):
 terms=tokenize(phrase)
 if not terms:return ()
 candidates=set(index.documents(terms[0]))
 for term in terms[1:]:candidates&=set(index.documents(term))
 matches=[]
 for document_id in candidates:
  starts=set(index.positions(terms[0],document_id))
  for offset,term in enumerate(terms[1:],1):starts&={spot-offset for spot in index.positions(term,document_id)}
  if starts:matches.append(document_id)
 return tuple(sorted(matches))
