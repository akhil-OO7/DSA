from typing import List
class Solution:
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V : int , adj : List[List[int]]) -> bool :
        visit, cur = set(), set()
        
        def dfs(node):
            visit.add(node)
            cur.add(node)
            for nxt in adj[node]:
                if nxt not in visit and dfs(nxt):
                    return True
                if nxt in cur:
                    return True
            cur.remove(node)
            return False
            
        for i in range(V):
            if i not in visit:
                if dfs(i):
                    return True
        return False

#Using Kahn's Algorithm (BFS)
from typing import List
from collections import deque
class Solution:
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V : int , adj : List[List[int]]) -> bool :
        indegree = [0] * V
        for u in range(V):
            for v in adj[u]:
                indegree[v] += 1
        q = deque()
        for i in range(V):
            if indegree[i] == 0:
                q.append(i)
        
        n = 0
        while q:
            node = q.popleft()
            n += 1
            for nxt in adj[node]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)
        
        return not(n == V)
