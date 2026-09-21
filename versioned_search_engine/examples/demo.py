import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]))
from search_engine.engine import SearchEngine
from search_engine.json_io import load_documents
engine=SearchEngine()
for doc in load_documents(Path(__file__).parents[1]/"data"/"sample_documents.json"):engine.add(doc)
print([(hit.document_id,round(hit.score,2)) for hit in engine.search("rail")])
