class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        maxprofit = 0

        while left<=right and right<len(prices):
            profit = prices[right]-prices[left]
            maxprofit = max(profit, maxprofit)
            if prices[right]<prices[left]:
                left+=1
            else:
                right+=1
        return maxprofit

        