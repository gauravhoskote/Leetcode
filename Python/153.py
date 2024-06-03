class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        sol = nums[0]
        while l < r:
            m = l + ((r - l)//2)
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
            sol = min(sol, nums[m])
        return nums[l]
