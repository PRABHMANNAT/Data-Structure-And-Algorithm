class GraphForgeError(Exception): pass
class NegativeWeight(GraphForgeError): pass
class UnknownVertex(GraphForgeError): pass
class CycleDetected(GraphForgeError): pass
class InvalidRevision(GraphForgeError): pass
