class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        prod_without_0 = 1
        count = 0
        for num in nums:
            if num != 0:
                prod *= num
            if num == 0:
                count += 1
            
        arr = [0]*(len(nums))

        for i in range(len(nums)):
            if nums[i] != 0 and count < 1:
                arr[i] = prod//nums[i]
            else:
                arr[i] = 0

            if nums[i] == 0 and count <= 1:
                arr[i] = prod

        return arr


        