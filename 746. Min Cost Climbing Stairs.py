class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp1 = 0
        dp2 = 0
        for i in range(len(cost)):
            dp0 = cost[i] + min(dp1, dp2)
            dp2 = dp1
            dp1 = dp0
        return min(dp1, dp2)
