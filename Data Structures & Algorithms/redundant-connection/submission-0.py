class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        g = defaultdict(list)

        def has_path(source, target, visited):
            if source == target:
                return True
            visited.add(source)
            for nei in g[source]:
                if nei not in visited:
                    if has_path(nei, target, visited):
                        return True
            return False

        for u, v in edges:
            if u in g and v in g and has_path(u, v, set()):
                return [u, v]
            
            g[u].append(v)
            g[v].append(u)
