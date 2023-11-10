class Solution:
    def isConnected(self, V, adj):
        visited = [False] * V
        nonZeroDegreeVertex = -1
        
        for i in range(V):
            if len(adj[i]) != 0:
                nonZeroDegreeVertex = i
                break
            
        self.dfs(nonZeroDegreeVertex, visited, adj)
        
        for i in range(V):
            if visited[i] == False and len(adj[i]) > 0:
                return False
                
        return True
        
    def dfs(self, n, visited, adj):
        visited[n] = True
        for nxt in adj[n]:
            if visited[nxt] == False:
                self.dfs(nxt, visited, adj)
                
	def isEularCircuitExist(self, V, adj):
	    
        if self.isConnected(V, adj) == False:
	       return 0
	        
        oddCount = 0
        for i in range(V):
            if len(adj[i]) % 2 != 0:
                oddCount += 1
                
        if oddCount > 2:
            return 0
            
        if oddCount == 2:
            return 1        # Eulerian Path
            
        if oddCount == 0:
            return 2 
