class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self, node):
        while node != self.par[node]:
            self.par[node] = self.par[self.par[node]]
            node = self.par[node]
        return node
    
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        
        if p1 == p2:
            return False
        
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        
        return True
        
class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        edges = []
        for u in range(V):
            for v, w in adj[u]:
                edges.append([u, v, w])
        edges.sort(key = lambda x: x[2])
        uf = UnionFind(V)
        res = 0
        for u, v, w in edges:
            if uf.union(u, v):
                res += w
        
        return res
