class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        prev = cost[0]
        nxt = cost[1]
        curr = min(prev,nxt)

        for i in range(2, n):
            curr = cost[i] + min(prev, nxt)
            prev = nxt
            nxt = curr

        return min(prev, curr)
        