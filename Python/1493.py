class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = 0
        ones = 0
        cl = 0
        sol = float('-inf')
        for r in range(len(nums)):
            cl += 1
            if nums[r]!= 1:
                ones += 1
            while ones > 1:
                if nums[l] != 1:
                    ones -=1
                l+=1
            sol = max(sol, r-l+1)
        return sol-1
