from copy import deepcopy
class SnapshotStore:
 def __init__(self):self._snapshots=[]
 def save(self,state):self._snapshots.append(deepcopy(state));return len(self._snapshots)-1
 def restore(self,revision):return deepcopy(self._snapshots[revision])
 def __len__(self):return len(self._snapshots)
