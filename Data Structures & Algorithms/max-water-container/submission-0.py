class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        rigth = len(height)-1
        maxArea = 0

        while left < rigth:
            currArea = min(height[left], height[rigth]) * (rigth-left)
            maxArea = max(maxArea, currArea)
            if height[left] < height[rigth]:
                left += 1
            else:
                rigth -= 1
        return maxArea
            



