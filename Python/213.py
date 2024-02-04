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
        if len(nums) == 1:
            return nums[0]
        a1 = nums[1:]
        a2 = nums[:-1]
        dp1 = [-1]*len(a1)
        dp2 = [-1]*len(a1)
        return max(self.f(len(a1)-1, a1, dp1), self.f(len(a2)-1, a2, dp2))
