class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        direction = [[1,0], [-1,0], [0,1], [0,-1]]
        maxArea = 0
        rows,cols = len(grid), len(grid[0])

        def bfs(r,c):
            q = deque()
            grid[r][c] = 0
            q.append((r,c))
            area = 1

            while q:
                row,col = q.popleft()
                for dr, dc in direction:
                    nr = row+dr
                    nc = col+dc
                    if (nr<0 or nc<0 or nr>=rows or nc>=cols or grid[nr][nc] == 0):
                        continue

                    q.append((nr,nc))
                    grid[nr][nc] = 0
                    area+=1
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    maxArea = max(bfs(r,c), maxArea)

        return maxArea