from graphforge.dsu import RollbackDSU
def test_rollback_restores_components() -> None:
    dsu = RollbackDSU(["a", "b"]); mark = dsu.snapshot(); dsu.union("a", "b"); dsu.rollback(mark); assert dsu.find("a") != dsu.find("b")
