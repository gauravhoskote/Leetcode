class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sol = nums[0]
        curr = nums[0]
        if len(nums) == 1:
            return sol
        for i in range(1, len(nums)):
            if curr + nums[i] < nums[i]:
                curr = nums[i]
            else:
                curr += nums[i]
            sol = max(sol, curr)
        return sol
