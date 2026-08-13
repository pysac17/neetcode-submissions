class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        from collections import deque
        m, n = len(grid), len(grid[0])
        q = deque()
        water, treasure, INF=-1, 0, 2147483647

        for i in range(m):
            for j in range(n):
                if grid[i][j] == treasure:
                    q.append((i,j))
        
        nsteps = 0
        while q:
            q_size = len(q)
            nsteps+=1
            for _ in range(q_size):
                i,j = q.popleft()
                for r, c in [(i, j+1), (i+1, j), (i-1, j), (i, j-1)]:
                    if r>=0 and c>=0 and r<m and c<n and grid[r][c] == INF:
                        grid[r][c] = min(grid[r][c], nsteps)
                        q.append((r, c))

                        

                    
        