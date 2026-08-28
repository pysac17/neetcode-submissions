class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        maxcount = 1

        for i in range(1, len(nums)):
            for j in range(i-1,-1,-1):
                if nums[i]>nums[j]:
                    dp[i] = max(dp[i],1+dp[j])
                    maxcount = max(dp[i], maxcount)
        return maxcount


