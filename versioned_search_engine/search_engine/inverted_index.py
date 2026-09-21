from .postings import PostingList
from .tokenizer import term_positions
class InvertedIndex:
 def __init__(self):self.terms={};self.doc_terms={}
 def add(self,document_id,text):
  self.remove(document_id); positions=term_positions(text);self.doc_terms[document_id]=positions
  for term,spots in positions.items():self.terms.setdefault(term,PostingList()).add(document_id,spots)
 def remove(self,document_id):
  for term in self.doc_terms.pop(document_id,{}):
   posting=self.terms[term];posting.remove(document_id)
   if not posting:self.terms.pop(term)
 def documents(self,term):return self.terms.get(term,PostingList()).documents()
 def positions(self,term,document_id):return self.terms.get(term,PostingList()).positions(document_id)
