class Solution:
    def f(self, i, cost, dp):
        if i >= len(cost):
            return 0
        if i in dp:
            return dp[i]
        dp[i] = min(cost[i] + self.f(i+1,cost, dp), cost[i] + self.f(i+2,cost, dp))
        return dp[i]

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = {}
        return min(self.f(0,cost, dp), self.f(1,cost, dp))
