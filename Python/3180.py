class Solution:
    
    def f(self, tsum, ss, nums, sol, dp):
        if tsum in dp:
            return
        mm = float('-inf')
        for i in range(len(nums)):
            if i not in ss and nums[i] > tsum:
                ss.add(i)
                self.f(tsum + nums[i], ss, nums, sol, dp)
                ss.remove(i)
        dp.add(tsum)
        sol[0] = max(sol[0], tsum)

    def maxTotalReward(self, nums: List[int]) -> int:
        tsum = sum(nums)
        ss = set()
        sol = [0]
        dp = set()
        self.f(0, ss, nums, sol, dp)
        return sol[0]
