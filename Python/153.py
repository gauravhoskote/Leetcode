class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        sol = 100000
        while l <= r:
            m = l + ((r - l)//2)
            if nums[l] < nums[r]:
                if nums[m] >= nums[l]:
                    r = m-1
                else:
                    l = m+1
            else:
                if nums[m] >= nums[l]:
                    l = m+1
                else:
                    r = m-1
            sol = min(sol, nums[m])
        return sol
