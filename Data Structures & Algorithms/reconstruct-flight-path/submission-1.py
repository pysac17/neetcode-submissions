class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(reverse = True)
        graph = defaultdict(list)
        for u, v in tickets:
            graph[u].append(v)

        res = []

        def dfs(node):
            while graph[node]:
                next_node = graph[node].pop()
                dfs(next_node)
            res.append(node)

        dfs("JFK")
        return res[::-1]
                
                

        