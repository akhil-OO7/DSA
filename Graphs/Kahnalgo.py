from collections import deque
def topo(V, adj):
  indegree = [0] * V
  for u in range(V):
    for v in adj[u]:
      indegree[v] += 1

  q = deque()
  for i in range(V):
    if indegree[i] == 0:
      q.append(i)

  res = []
  while q:
    n1 = q.popleft()
    res.add(n1)
    for nxt in adj[n1]:
      indegree[nxt] -= 1
      if indegree[nxt] == 0:
        q.append(nxt)

  return res
