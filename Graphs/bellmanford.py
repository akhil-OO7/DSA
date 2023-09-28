def bellmandford(n, src, edges):
  dist = [float("inf")] * n
  dist[src] = 0
  for _ in range(n - 1):
    for s, d, w in edges:
      if dist[s] != float("inf") and dist[s] + w < dist[d]:
        dist[d] = dist[s] + w

  return dist
