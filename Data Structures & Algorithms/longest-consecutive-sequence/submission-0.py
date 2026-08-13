class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        longest = 0
        for i in nums:
            if i-1 not in set_nums:
                length = 0
                while (i+length) in set_nums:
                    length += 1
                longest = max(length, longest)
        return longest    
        