class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = {}

        def dfs(i, j):
            if j == len(t):
                return 1
            if (i, j) in dp:
                return dp[(i, j)]

            count = 0
            if i<len(s) and j<len(t):
                if s[i] == t[j]:
                    count = dfs(i+1, j+1) 
                count += dfs(i+1, j)

            dp[(i, j)] = count
            return count
        return dfs(0,0)
                    

            
        