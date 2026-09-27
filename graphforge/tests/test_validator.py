import pytest
from graphforge.graph import DirectedGraph
from graphforge.model import Edge
from graphforge.validator import validate

def test_vertex_limit() -> None:
    with pytest.raises(ValueError): validate(DirectedGraph([Edge("a", "b", 1)]), 1)
