class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {} 
        count = 0

        def dfs(i, total):
            if total > amount or i>len(coins)-1:
                return 0
            if total == amount:
                return 1
            if (i, total) in dp:
                return dp[(i, total)]
            
            
            take_coin = dfs(i, total+coins[i])
            dont_take_coin = dfs(i+1, total)
            
            dp[(i, total)] = take_coin + dont_take_coin
            return dp[(i, total)]

        return dfs(0, 0)



        