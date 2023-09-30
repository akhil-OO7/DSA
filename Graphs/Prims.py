import heapq
def prims(adj):              # adj[i]: [j, weight]
  res = 0
  minH = [(0, 0)]     # (cost, node)
  visit = set()

  while minH:
    cost, n1 = heapq.heappop(minH)
    if n1 in visit:
      continue
    res += cost
    visit.add(n1)

    for n2, w in adj[n1]:
      if n2 not in visit:
        heapq.heappush(minH, (w, n2))
        
  return res
