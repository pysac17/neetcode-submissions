class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        min_time = {}
        min_heap = [(0, k)]
        heapq.heapify(min_heap)

        graph = defaultdict(list)
        for u,v,w in times:
            graph[u].append((v, w))

        while min_heap:
            dist, node = heapq.heappop(min_heap)
            if node in min_time:
                continue
            
            min_time[node] = dist

            for u, v in graph[node]:
                if u not in min_time:
                    heapq.heappush(min_heap, (dist+v, u))

        if len(min_time) == n:
            return max(min_time.values())
        else:
            return -1

            
            
        