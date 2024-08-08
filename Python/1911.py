class Solution:
    
    def f(self, i, nums, even, dp):
        dpi = (i, even)
        if dpi in dp:
            return dp[dpi]

        if i >= len(nums):
            return 0

        if even:
            # take
            res1 = nums[i] + self.f(i+1, nums, False, dp)
            # not take
            res2 = self.f(i+1, nums, True, dp)

            dp[dpi] = max(res1, res2)
            return dp[dpi]
        else:
            # take
            res1 = self.f(i+1, nums, True, dp) - nums[i]
            # not take
            res2 = self.f(i+1, nums, False, dp)

            dp[dpi] = max(res1, res2)
            return dp[dpi]
    
    def maxAlternatingSum(self, nums: List[int]) -> int:
        dp = {}
        return self.f(0, nums, True, dp)
