class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        def dfs(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            if (i, total) in dp:
                return dp[(i, total)]
            
            if i<len(nums):
                take_plus = dfs(i+1, total+nums[i])
                take_minus = dfs(i+1, total-nums[i])

            dp[(i, total)] = take_plus + take_minus
            return dp[(i, total)]

        return dfs(0, 0)

        