from streamshield.engine import StreamEngine
from streamshield.model import Event
from streamshield.snapshot import load_stats, save_stats

def test_snapshot_roundtrip(tmp_path) -> None:
    engine = StreamEngine(); engine.ingest(Event("a", 1)); target = tmp_path / "stats.json"
    save_stats(engine, target)
    assert load_stats(target)["accepted"] == 1
