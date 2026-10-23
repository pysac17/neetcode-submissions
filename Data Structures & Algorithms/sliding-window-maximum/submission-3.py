class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxval, l, r = float("-inf"), 0, k-1
        res = [] 

        for i in range(k):
            if nums[i] > maxval:
                maxval = max(maxval,nums[i])
        res.append(maxval)

        while r+1<len(nums):
            leftval = nums[l]
            rightval = nums[r+1]
            l += 1
            r +=1

            if rightval>=maxval:
                maxval = rightval
                res.append(maxval)
            else:
                if leftval < maxval:
                    res.append(maxval)
                else:
                    newmaxval = float("-inf")
                    for i in range(l, r+1):
                        newmaxval = max(newmaxval, nums[i])
                    res.append(newmaxval)
                    maxval = newmaxval

        return res
        
        