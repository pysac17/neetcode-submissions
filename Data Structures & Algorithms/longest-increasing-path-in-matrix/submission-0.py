class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dirs = [(0,1), (1,0), (-1,0), (0,-1)]
        rows = len(matrix)
        cols = len(matrix[0])
        dp = {}

        def dfs(i, j):
            if (i, j) in dp:
                return dp[(i, j)]

            count = 1
            
            for di, dj in dirs:
                nr, nc = di+i, dj+j
                if 0<=nr<rows and 0<=nc<cols and matrix[nr][nc] > matrix[i][j]:
                    count = max(count, 1 + dfs(nr, nc))

            dp[(i, j)] = count
            return count
        
        global_max = 0
        for r in range(rows):
            for c in range(cols):
                global_max = max(global_max, dfs(r, c))
                
        return global_max
        


    
        