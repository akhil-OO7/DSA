class Solution:
    
    def topo(self, adj, node, visit, stack):
        visit.add(node)
        for nxt in adj[node]:
            if nxt not in visit:
                self.topo(adj, nxt, visit, stack)
        stack.append(node)
    
    def dfs(self, node, visit2, adjT):
        visit2.add(node)
        for nxt in adjT[node]:
            if nxt not in visit2:
                self.dfs(nxt, visit2, adjT)
            
    #Function to find number of strongly connected components in the graph.
    def kosaraju(self, V, adj):
        
        # Building Topological sort
        visit = set()
        stack = []
        for i in range(V):
            if i not in visit:
                self.topo(adj, i, visit, stack)
                
        # Building Transpose
        adjT = { i: [] for i in range(V)}
        for u in range(V):
            for v in adj[u]:
                adjT[v].append(u)
        
        # counting SCC
        countScc = 0
        visit2 = set()
        while stack:
            i = stack.pop()
            if i not in visit2:
                self.dfs(i, visit2, adjT)
                countScc += 1
        
        return countScc
