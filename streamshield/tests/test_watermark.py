from streamshield.watermark import Watermark

def test_watermark_never_moves_back() -> None:
    w = Watermark(5); w.observe(20); w.observe(10)
    assert w.value == 15
