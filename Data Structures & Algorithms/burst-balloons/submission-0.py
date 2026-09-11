class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        dp = {}
        A = [1] + nums + [1]

        def dfs(i, j):
            if i>j:
                return 0
            if (i,j) in dp:
                return dp[(i, j)]

            max_coins = 0
            for k in range(i, j+1):
                coins = (A[i - 1] * A[k] * A[j + 1]) + dfs(i, k - 1) + dfs(k + 1, j)
                max_coins = max(max_coins, coins)


            dp[(i,j)] = max_coins
            return max_coins
        return dfs(1, len(nums))