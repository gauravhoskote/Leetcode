class Solution:
    def f(self, ind, nums, target, dp):
        dpind = (ind, target)

        if dpind in dp:
            return dp[dpind]

        if ind == len(nums):
            if target == 0:
                return 1
            else:
                return 0

        res1 = self.f(ind+1, nums, target + nums[ind], dp)
        res2 = self.f(ind+1, nums, target - nums[ind], dp)

        dp[dpind] = res1 + res2
        return dp[dpind]

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        return self.f(0, nums, target, dp)
