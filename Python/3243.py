class Solution:

    def f(self, ind, nums, dp, target):
        if ind == len(nums)-1:
            return 0
        dpind = ind

        if dpind in dp:
            return dp[dpind]

        sol = float('inf')
        for v in nums[ind]:
            loc = self.f(v, nums, dp, target)
            sol = min(loc, sol)
        dp[dpind] = 1 + sol
        return dp[dpind]

    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:

        nums = [[i+1] for i in range(n)]
        sol = []
        for q in queries:
            u = q[0]
            v = q[1]
            nums[u].append(v)
            dp = {}
            sol.append(self.f(0, nums, dp, len(nums)-1))
        return sol
