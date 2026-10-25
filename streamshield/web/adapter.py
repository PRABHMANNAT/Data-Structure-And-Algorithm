from dataclasses import asdict
from streamshield.engine import StreamEngine
from streamshield.model import Event
from streamshield.errors import LateEvent
from workbench.validation import lines, integer

def run(data):
    engine=StreamEngine(integer(data,'window',3000,1),integer(data,'lateness',500,0))
    timeline=[]
    for row in lines(data,'events'):
        parts=row.split()
        if len(parts)!=3:raise ValueError('Use: key timestamp value')
        key,timestamp,value=parts
        event=Event(key,integer({'v':timestamp},'v',minimum=0),integer({'v':value},'v'))
        accepted=True
        try:engine.ingest(event)
        except LateEvent:accepted=False
        timeline.append(dict(key=key,timestamp=event.timestamp,value=event.value,accepted=accepted,watermark=engine.stats().watermark,total=engine.window_total()))
    return dict(stats=asdict(engine.stats()),leaders=engine.leaders(),timeline=timeline,total=engine.window_total())
