class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = {i: [] for i in range(n)}
        for s, d, w in edges:
            adj[s].append([d, w])
        
        res = {}
        minH = [(0, src)]
        while minH:
            w1, n1 = heapq.heappop(minH)
            if n1 in res:
                continue
            res[n1] = w1
            for n2, w2 in adj[n1]:
                if n2 not in res:
                    heapq.heappush(minH, (w1 + w2, n2))

        for i in range(n):
            if i not in res:
                res[i] = -1
        
        return res
