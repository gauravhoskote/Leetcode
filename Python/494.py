class Solution:
    def f(self, total, ind, nums, target,dp):
        if ind > len(nums):
            return 0
        if ind == len(nums):
            if total == target:
                return 1
            else:
                return 0
        if (ind, total) in dp:
            return dp[(ind, total)]
        
        dp[(ind, total)] = self.f(total + nums[ind], ind + 1, nums, target, dp) + self.f(total - nums[ind], ind + 1, nums, target, dp)
        return dp[(ind, total)]

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        return self.f(0,0,nums,target, dp)
