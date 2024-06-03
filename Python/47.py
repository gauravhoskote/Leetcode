class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        nums.sort()
        temp = nums.copy()
        sol = []
        while True:
            def f(nums):
                i = len(nums)-2
                j = len(nums)-1
                while i >= 0 and nums[i]>=nums[i+1]:
                    i-=1
                if i >=0:
                    while j > i and nums[i]>= nums[j]:
                        j-=1
                    nums[i],nums[j] = nums[j],nums[i]
                ii = i
                i+=1
                j = len(nums)-1
                while j > i:
                    nums[i],nums[j] = nums[j],nums[i]
                    j-=1
                    i+=1
                return ii<0
            if f(nums):
                sol.append(temp)
                return sol
            else:
                if nums != temp:
                    sol.append(temp)
                    temp = nums.copy()
