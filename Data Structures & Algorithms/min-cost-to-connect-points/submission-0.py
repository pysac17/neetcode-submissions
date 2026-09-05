class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        seen = set()
        minheap =[(0,0)]
        totalcost = 0
        heapq.heapify(minheap)

        while len(seen) < n:
            dist, i = heapq.heappop(minheap)
            if i in seen:
                continue
            seen.add(i)
            totalcost += dist
            xi, yi = points[i]

            for j in range(n):
                if j not in seen:
                    xj, yj = points[j]
                    dist = abs(xi - xj) + abs(yi - yj)
                    heapq.heappush(minheap, (dist, j)) 
        return totalcost
