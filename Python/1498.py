class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        l = 0
        r = len(nums)-1
        sol = 0
        while l <= r:
            if nums[l]+nums[r] > target:
                r-=1
            else:
                sol += pow(2, (r-l), 1000000007)
                l+=1
        return sol
