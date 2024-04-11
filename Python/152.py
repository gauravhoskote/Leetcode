class Solution:
    def f(self,cp, sol, nums, index, dp):
        if index >= len(nums):
            return
        
        if (index, cp) in dp:
            return

        if cp * nums[index] > sol[0]:
            sol[0] = cp * nums[index]
        
        dp[(index, cp)] = 1
        self.f(cp*nums[index], sol, nums, index+1, dp)
        if nums[index]<= 0:
            self.f(1, sol, nums, index+1, dp)

    def maxProduct(self, nums: List[int]) -> int:
        dp = {}
        sol = [float('-inf')]
        _ = self.f(1, sol, nums, 0, dp)
        return sol[0]
