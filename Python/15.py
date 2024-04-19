class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sol = []
        i = 0
        while i < len(nums)-2:
            l = i+1
            r = len(nums)-1
            while l < r:
                if nums[l]+nums[r]+nums[i] < 0:
                    l+=1
                elif nums[l]+nums[r]+nums[i] > 0:
                    r-=1
                else:
                    sol.append([nums[i], nums[l], nums[r]])
                    x = nums[l]
                    y = nums[r]
                    while l < r and nums[l] == x:
                        l+=1
                    while l < r and nums[r] == y:
                        r-=1
            prev = nums[i]
            while i < len(nums)-2 and nums[i] == prev:
                i+=1
        return sol
