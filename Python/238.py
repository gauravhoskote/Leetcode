class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a1 = nums.copy()
        a2 = nums.copy()
        if len(nums) == 1:
            return nums
        for i in range(1, len(nums)):
            a1[i] = a1[i-1]* a1[i]
        for i in range(len(nums)-2, -1, -1):
            a2[i] = a2[i+1]* a2[i]
        sol = [1]*len(nums)
        for i in range(len(sol)):
            x = 1
            if i > 0:
                x = x * a1[i-1]
            if i < len(sol)-1:
                x = x * a2[i+1]
            sol[i] = x
        return sol
