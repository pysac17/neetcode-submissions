class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        poss = set()
        poss.add(0)
        total = sum(nums)
        
        if total % 2 != 0:
            return False
            
        target = total // 2

        for i in range(len(nums)-1,-1,-1):
            nextdp = set()
            for j in poss:
                nextdp.add(nums[i]+j)
                nextdp.add(j)
                if nums[i]+j == target:
                    return True
            poss=nextdp
        return False

        