from .bm25 import score
from .document_store import DocumentStore
from .inverted_index import InvertedIndex
from .lru_cache import LRUCache
from .models import SearchHit
from .tokenizer import tokenize
from .trie import TermTrie
class SearchEngine:
 def __init__(self):self.store=DocumentStore();self.index=InvertedIndex();self.trie=TermTrie();self.cache=LRUCache()
 def add(self,document):
  self.store.put(document);self.index.add(document.id,document.title+" "+document.body)
  for term in self.index.doc_terms[document.id]:self.trie.insert(term)
  self.cache.clear()
 def search(self,query,limit=10):
  key=(self.store.revision,query,limit);cached=self.cache.get(key)
  if cached is not None:return cached
  terms=tokenize(query);lengths={doc_id:sum(len(x) for x in terms_) for doc_id,terms_ in self.index.doc_terms.items()};avg=sum(lengths.values())/len(lengths) if lengths else 1
  candidates=set().union(*(self.index.documents(term) for term in terms)) if terms else set()
  hits=tuple(sorted((SearchHit(doc_id,score(self.index,doc_id,terms,lengths,avg),tuple(terms)) for doc_id in candidates),key=lambda item:(-item.score,item.document_id))[:limit]);self.cache.put(key,hits);return hits
