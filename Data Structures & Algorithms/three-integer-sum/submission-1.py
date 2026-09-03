class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l = 0
        r = len(nums)-1
        res = []
        nums.sort()

        for i in range(len(nums)):
            l = i+1
            r = len(nums)-1
            while l<r:
                total = nums[l] + nums[r] + nums[i]
                if total == 0:
                    if [nums[l], nums[r], nums[i]] not in res:
                        res.append([nums[l], nums[r], nums[i]])
                if total > 0:
                    r -= 1
                else:
                    l += 1

        return res





        