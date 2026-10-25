from search_engine.engine import SearchEngine
from search_engine.models import Document
from workbench.validation import lines, text, integer

def run(data):
    engine=SearchEngine();documents=[]
    for index,row in enumerate(lines(data,'documents')):
        if '|' not in row:raise ValueError('Each document needs a title | body separator')
        title,body=(part.strip() for part in row.split('|',1))
        if not title or not body:raise ValueError('Document title and body cannot be empty')
        document=Document(str(index+1),title,body);documents.append(document);engine.add(document)
    query=text(data,'query');prefix=text(data,'prefix')
    limit=integer(data,'limit',5,1,30)
    hits=engine.search(query,limit)
    results=[dict(id=hit.document_id,title=documents[int(hit.document_id)-1].title,
                  body=documents[int(hit.document_id)-1].body,score=round(hit.score,4),terms=list(hit.matched_terms)) for hit in hits]
    return dict(hits=results,suggestions=list(engine.trie.complete(prefix.lower(),10)),documents=len(documents),revision=engine.store.revision)
