from pathlib import Path
import json
from streamshield import Event, StreamEngine

engine = StreamEngine()
for line in Path("events.jsonl").read_text().splitlines():
    engine.ingest(Event(**json.loads(line)))
print(engine.leaders())
