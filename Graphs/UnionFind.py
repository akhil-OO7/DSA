class UnionFind:
  def __init__(self, n):
    self.par = [i for i in range(n)]
    self.rank = [1] * n

  def Union(n1, n2):
    p1, p2 = find(n1), find(n2)
    if p1 == p2:
      return False
    if rank[p1] > rank[p2]:
      par[p2] = p1
      rank[p1] += rank[p2]
    else:
      par[p1] = p2
      rank[p2] += rank[p1]
    return True
      
  def find(node):
    res = par[node]
    while par[res] != res:
      par[res] = par[par[res]]
      res = par[res]
    return res
  
