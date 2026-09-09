class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cols = len(text1)
        rows = len(text2)
        dp = [[0 for _ in range(cols+1)] for _ in range(rows+1)]
        
        for i1, c1 in enumerate(text2):
            for i2, c2 in enumerate(text1):
                if c1 == c2:
                    dp[i1+1][i2+1] = dp[i1][i2] + 1
                else:
                    dp[i1+1][i2+1] = max(dp[i1][i2+1], dp[i1+1][i2])
        return dp[rows][cols]



