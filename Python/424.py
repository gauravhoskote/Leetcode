class Solution:
    def characterReplacement(self, nums: str, k: int) -> int:
        l = 0
        dd = {}
        sol = 0
        mm = float('-inf')
        for r in range(len(nums)):
            dd[nums[r]] = dd.get(nums[r],0)+1
            mm = max(mm, dd[nums[r]])
            while r - l + 1 - mm > k:
                if dd[nums[l]] == 1:
                    del dd[nums[l]]
                else:
                    dd[nums[l]] -= 1
                l+=1
            sol = max(sol, (r-l+1))
        return sol
