class Solution:
    def numRescueBoats(self, nums: List[int], limit: int) -> int:
        sol = 0
        nums.sort()
        r = len(nums)-1
        l = 0
        while l <= r:
            if nums[l]+nums[r] <= limit:
                sol+=1
                l+=1
                r-=1
            else:
                sol+=1
                r-=1
        return sol
