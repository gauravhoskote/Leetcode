class Solution:
    def f(self, nums, k):
        l = 0
        ones = 0
        sol = 0
        for r in range(len(nums)):
            if nums[r]%2:
                ones += 1
            while ones > k:
                if nums[l] % 2:
                    ones-=1
                l+=1
            sol += (r-l+1)
        return sol
            
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return self.f(nums,k) - self.f(nums,k-1)
