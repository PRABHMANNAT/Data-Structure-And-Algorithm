class PostingList:
 def __init__(self):self._positions={}
 def add(self,document_id,positions):self._positions[document_id]=tuple(positions)
 def remove(self,document_id):self._positions.pop(document_id,None)
 def documents(self):return tuple(sorted(self._positions))
 def positions(self,document_id):return self._positions.get(document_id,())
 def __len__(self):return len(self._positions)
