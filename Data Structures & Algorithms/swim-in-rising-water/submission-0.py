class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        seen = set()
        minheap = [(grid[0][0],(0,0))]
        water = 0
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]

        while True:
            height, idx = heapq.heappop(minheap)   
            if idx == (n-1, n-1):
                return max(height, water)
            if idx in seen:
                continue
            seen.add(idx)
            water = max(height, water)
            xi, yi = idx

            for dx, dy in dirs:
                x, y = xi+dx, yi+dy
                if (x, y) not in seen and 0<=x<n and 0<=y<n:
                    heapq.heappush(minheap, (grid[x][y], (x, y)))



