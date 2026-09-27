from streamshield.heavy_hitters import MisraGries

def test_dominant_key_survives() -> None:
    tracker = MisraGries(2)
    for key in "aaaaabcc": tracker.add(key)
    assert "a" in tracker.candidates
