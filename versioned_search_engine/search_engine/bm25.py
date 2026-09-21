import math
def score(index,document_id,terms,document_lengths,average_length,k1=1.2,b=0.75):
 total=len(document_lengths);length=document_lengths[document_id];value=0.0
 for term in terms:
  df=len(index.documents(term))
  if not df:continue
  tf=len(index.positions(term,document_id));idf=math.log(1+(total-df+.5)/(df+.5))
  value+=idf*(tf*(k1+1)/(tf+k1*(1-b+b*length/average_length)))
 return value
