from collections import defaultdict
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for course, pre in prerequisites:
            graph[pre].append(course) 
        
        visited = set()   
        visiting = set()  
        
        def has_cycle(node) -> bool:
            if node in visiting:
                return True
            if node in visited:
                return False
                
            visiting.add(node)
            
            for neighbor in graph[node]:
                if has_cycle(neighbor):
                    return True
                    
            visiting.remove(node)
            visited.add(node)
            return False

        for course in range(numCourses):
            if has_cycle(course):
                return False 
                
        return True
