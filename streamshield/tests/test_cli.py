from streamshield.cli import main

def test_cli_accepts_empty_input(monkeypatch) -> None:
    monkeypatch.setattr("sys.stdin", [])
    assert main([]) == 0
