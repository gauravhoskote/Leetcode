class Solution:

    def atmost(self,nums, k):
        l =0
        dd = {}
        sol = 0
        for r in range(len(nums)):
            dd[nums[r]] = dd.get(nums[r], 0)+1
            while len(dd.keys()) > k:
                if dd[nums[l]] == 1:
                    del dd[nums[l]]
                else:
                    dd[nums[l]] -= 1
                l+=1
            sol += (r-l+1)
        return sol

    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.atmost(nums, k) - self.atmost(nums, k-1)
