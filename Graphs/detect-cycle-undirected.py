from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        visit = set()
        def dfs(node, par):
            visit.add(node)
            for nxt in adj[node]:
                if nxt == par:
                    continue
                if nxt in visit:
                    return True
                if dfs(nxt, node):
                    return True
            return False
            
	    for i in range(V):
	        if i not in visit and dfs(i, -1):
	            return True
        return False

from typing import List
from collections import deque
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        visit = set()
        q = deque()
        def bfs(node):
            q.append((node, -1))
            visit.add(node)
            while q:
                node, par = q.popleft()
                for nxt in adj[node]:
                    if nxt == par:
                        continue
                    if nxt in visit:
                        return True
                    q.append((nxt, node))
                    visit.add(nxt)
            return False
            
	    for i in range(V):
	        if i not in visit and bfs(i):
	            return True
        return False
