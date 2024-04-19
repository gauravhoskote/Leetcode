class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        i = 0
        sol = []
        while i < len(nums)-3:
            j = i+1
            while j < len(nums)-2:
                l = j+1
                r = len(nums)-1
                while l < r:
                    if nums[i]+nums[j]+nums[l]+nums[r] > target:
                        r-=1
                    elif nums[i]+nums[j]+nums[l]+nums[r] < target:
                        l+=1
                    else:
                        sol.append([nums[i], nums[j], nums[l], nums[r]])
                        x = nums[l]
                        while l < r and nums[l] == x:
                            l+=1
                        y = nums[r]
                        while l < r and nums[r] == y:
                            r-=1
                prevj = nums[j]
                while j < len(nums)-2 and nums[j] == prevj:
                    j+=1
            previ = nums[i]
            while i < len(nums)-3 and nums[i] == previ:
                i+=1
        return sol
