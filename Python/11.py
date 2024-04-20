class Solution:
    def maxArea(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        sol = 0
        while l < r:
            water = (min(nums[l] , nums[r]) * (r-l))
            if nums[l] < nums[r]:
                l+=1
            else:
                r-=1
            sol = max(sol, water)
        return sol
