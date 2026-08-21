class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return
        
        curr_max = 0
        prev_max = 0

        for num in nums:
            temp = curr_max
            curr_max = max(num+prev_max, curr_max)
            prev_max = temp

        return curr_max
