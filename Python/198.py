class Solution:
    def f(self, ind, nums, dp):
        if ind < 0:
            return 0
        if dp[ind] != -1:
            return dp[ind]
        # take 
        take = nums[ind] + self.f(ind - 2, nums, dp)
        not_take = self.f(ind-1, nums, dp)
        dp[ind] = max(take, not_take)
        return dp[ind]

    def rob(self, nums: List[int]) -> int:
        dp = [-1]* len(nums)
        return self.f(len(nums)-1, nums, dp)
