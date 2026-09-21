from .models import Document
class DocumentStore:
 def __init__(self): self._documents={};self.revision=0
 def put(self,document:Document): self._documents[document.id]=document;self.revision+=1
 def get(self,document_id): return self._documents.get(document_id)
 def remove(self,document_id):
  if document_id in self._documents: del self._documents[document_id];self.revision+=1;return True
  return False
 def values(self): return tuple(self._documents.values())
 def __len__(self):return len(self._documents)
