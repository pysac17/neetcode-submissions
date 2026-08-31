class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = 0
        maxSum = nums[0]

        for n in nums:
            curr_sum = max(n, curr_sum+n)
            maxSum = max(maxSum, curr_sum)

        return maxSum
