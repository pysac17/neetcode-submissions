from collections import defaultdict
from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        g = defaultdict(list)
        for i, j in edges:
            g[i].append(j)
            g[j].append(i)

        unvisited = 0
        visiting = 1
        visited = 2
        
        state = [unvisited] * n

        def dfs(node, parent):
            if state[node] == visited:
                return True
            
            state[node] = visiting
            
            for nei in g[node]:
                if nei == parent:
                    continue
                if state[nei] == visiting:
                    return False
                if not dfs(nei, node):
                    return False
                    
            state[node] = visited
            return True

        if not dfs(0, -1):
            return False
            
        return all(s == visited for s in state)
