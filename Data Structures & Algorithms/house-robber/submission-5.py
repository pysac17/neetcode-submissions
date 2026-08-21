class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 

        prev, curr = 0, 0

        for num in nums:
            prev, curr = curr, max(prev+num, curr)

        return curr 