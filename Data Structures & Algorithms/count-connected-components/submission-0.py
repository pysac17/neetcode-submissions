class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        g = defaultdict(list)
        count = 1

        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        visited = set()

        def dfs(node):
            visited.add(node)
            for nei in g[node]:
                if nei not in visited:
                    dfs(nei)
            

        dfs(0)

        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i)

        return count




        
                




        