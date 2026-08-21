class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return nums[0]

        def robHouse(nums):
            prev, curr = 0, 0
            for num in nums:
                prev, curr = curr, max(curr, prev+num)
            return curr

        return max(robHouse(nums[1:]), robHouse(nums[:-1]))


        