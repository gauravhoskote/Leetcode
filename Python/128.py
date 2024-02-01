class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        if len(nums) == 1 or len(nums) == 0:
            return len(nums)
        last = nums[0]
        ctr = 1
        sol = 1 
        for i in range(1, len(nums)):
            if last + 1 == nums[i]:
                ctr = ctr + 1
                last = nums[i]
            elif last == nums[i]:
                continue
            else:
                sol = max(sol, ctr)
                ctr = 1
                last = nums[i]
        sol = max(ctr, sol)
        return sol
