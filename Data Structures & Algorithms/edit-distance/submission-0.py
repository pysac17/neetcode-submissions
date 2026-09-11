class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = {}

        def dfs(i, j):
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i
            if (i, j) in dp:
                return dp[(i, j)]

            if i<len(word1) and j<len(word2):
                if word1[i] == word2[j]:
                    dp[(i, j)] = dfs(i+1, j+1)
                else:
                    replace = 1 + dfs(i+1, j+1)
                    remove = 1 + dfs(i+1, j)
                    insert = 1 + dfs(i, j+1)
                    dp[(i, j)] = min(replace, remove, insert)
                    
            return dp[(i, j)]
        
        return dfs(0,0)
