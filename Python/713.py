class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l = 0
        if k == 0:
            return 0
        prd = 1
        ctr = 0
        for r in range(len(nums)):
            prd *= nums[r]
            while l <= r and prd >= k:
                prd /= nums[l]
                l+=1
            ctr+=(r-l+1)
        return ctr
