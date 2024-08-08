class Solution:
    
    def f(self, ind, nums, l, dp):
        if ind >= len(nums):
            return 0
        x = (ind,(ind - l )%2)
        if x in dp:
            return dp[x]
        
        if (ind - l )%2 == 0:
            curr = nums[ind]
        else:
            curr = -nums[ind]
        r1 = curr + self.f(ind+1, nums, l, dp)
        r2 = curr + self.f(ind+1, nums, ind+1, dp)
        dp[x] = max(r1,r2)
        return dp[x]
    
    def maximumTotalCost(self, nums: List[int]) -> int:
        dp = {}
        return self.f(0, nums,0, dp)
