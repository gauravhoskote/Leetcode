class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        sol = float('-inf')
        l = 0
        r = len(nums)-1
        while l < r:
            sol = max(sol, nums[l]+nums[r])
            l+=1
            r-=1
        return sol
