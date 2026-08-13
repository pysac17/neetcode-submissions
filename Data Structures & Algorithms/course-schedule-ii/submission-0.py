from collections import defaultdict
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        for crs, pre in prerequisites:
            g[crs].append(pre)

        res = []

        unvisited = 0
        visiting = 1
        visited = 2
        state = [0]*numCourses

        def dfs(crs):
            if state[crs] == visited: 
                return True
            elif state[crs] == visiting:
                return False

            state[crs] = visiting
            for nei in g[crs]:
                if not dfs(nei):
                    return False
            res.append(crs)
            state[crs] = visited
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
            
        return res



        