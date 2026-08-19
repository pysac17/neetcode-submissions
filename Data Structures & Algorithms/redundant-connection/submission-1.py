class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        parent = [i for i in range(N+1)]
        print(parent)
        
        def find(node):
            if node != parent[node]:
                parent[node] = find(parent[node])
            return parent[node]

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            print(p1, p2)
            if p1==p2:
                return False
            
            parent[p1] = p2
            return True

        for i, j in edges:
            if not union(i, j):
                return [i, j]