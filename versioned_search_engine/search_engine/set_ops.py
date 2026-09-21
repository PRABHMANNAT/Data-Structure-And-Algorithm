def intersect(left,right):return tuple(sorted(set(left)&set(right)))
def union(left,right):return tuple(sorted(set(left)|set(right)))
def difference(left,right):return tuple(sorted(set(left)-set(right)))
