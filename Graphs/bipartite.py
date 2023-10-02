# DFS
class Solution:
	def isBipartite(self, V, adj):
		#code here
		color = [-1] * V
		
		def dfs(cur, curCol):
		    color[cur] = curCol
		    for nxt in adj[cur]:
		        if color[nxt] == color[cur]:
		            return False
		        if color[nxt] == -1:
		            nxtCol = 1 - curCol
		            if not dfs(nxt, nxtCol):
		                return False
		    return True
		
		
		for i in range(V):
		    if color[i] == -1:
		        if not dfs(i, 1):
		            return False
		 
        return True

# BFS
class Solution:
  def isBipartite(self, graph: List[List[int]]) -> bool:
      n = len(graph)

      color = [-1] * n
      q = deque()
      def bfs(cur, curCol):
          q.append(cur)
          color[cur] = curCol
          while q:
              node = q.popleft()
              for nxt in graph[node]:
                  if color[nxt] == color[node]:
                      return False
                  if color[nxt] == -1:
                      color[nxt] = 1 - color[node]
                      q.append(nxt)
          return True
      

      for i in range(n):
          if color[i] == -1:
              if not bfs(i, 1):
                  return False
      
      return True
        
