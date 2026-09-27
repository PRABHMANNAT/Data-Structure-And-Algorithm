from graphforge.model import Edge
from graphforge.versioned import VersionedGraph
def test_old_revision_is_isolated() -> None:
    store = VersionedGraph(); store.commit((Edge("a", "b", 1),)); old = store.head; store.commit((Edge("b", "c", 1),)); assert store.read(old).neighbors("b") == ()
