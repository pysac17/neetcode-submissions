class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n<=1:
            return nums[0]
        elif n==2:
            return max(nums[0], nums[1])

        dp = [0] * n
        dp[0], dp[1], dp[2] = nums[0], nums[1], nums[0] + nums[2]
        maxAmount = max(dp[0], dp[1], dp[2])

        for i in range(3, n):
            dp[i] = max(dp[i-2],dp[i-3]) + nums[i]  
            maxAmount = max(maxAmount, dp[i])

        return maxAmount 