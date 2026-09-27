from streamshield.sketch import CountMinSketch

def test_estimate_never_undercounts() -> None:
    sketch = CountMinSketch(); [sketch.add("x") for _ in range(5)]
    assert sketch.estimate("x") >= 5
