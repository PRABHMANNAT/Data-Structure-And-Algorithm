import argparse
from .engine import SearchEngine
from .json_io import load_documents
def main(argv=None):
 parser=argparse.ArgumentParser();parser.add_argument("data");parser.add_argument("query");args=parser.parse_args(argv)
 engine=SearchEngine()
 for document in load_documents(args.data):engine.add(document)
 for hit in engine.search(args.query):print(f"{hit.document_id}\t{hit.score:.3f}")
 return 0
if __name__=="__main__":raise SystemExit(main())
