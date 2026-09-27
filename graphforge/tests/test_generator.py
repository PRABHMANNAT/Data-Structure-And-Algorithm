from graphforge.generator import line_graph

def test_line_graph() -> None: assert len(line_graph(4).edges()) == 3
