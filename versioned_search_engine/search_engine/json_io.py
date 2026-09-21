import json
from pathlib import Path
from .models import Document
def load_documents(path):
 return tuple(Document(**item) for item in json.loads(Path(path).read_text()))
def dump_documents(documents,path):
 Path(path).write_text(json.dumps([{"id":d.id,"title":d.title,"body":d.body,"links":d.links} for d in documents],indent=2))
