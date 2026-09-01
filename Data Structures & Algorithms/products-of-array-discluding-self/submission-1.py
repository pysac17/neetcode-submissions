class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        res = [0] * len(nums)
        zeroCount = 0

        for n in nums:
            if n!=0:
                product*=n
            else:
                zeroCount += 1
        
        for i in range(len(nums)):
            if nums[i] == 0 and zeroCount < 2:
                res[i] = int(product)
            elif nums[i]!= 0 and zeroCount == 0:
                res[i] = int(product/nums[i])

        return res