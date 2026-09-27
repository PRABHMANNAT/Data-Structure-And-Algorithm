from streamshield.metrics import Metrics

def test_counter_accumulates() -> None:
    metrics = Metrics(); metrics.increment("ingest"); metrics.increment("ingest", 2)
    assert metrics.snapshot() == {"ingest": 3}
