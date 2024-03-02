class Solution:

    def f(self, ind, nums, csol, sol):
        if ind == len(nums):
            if csol not in sol:
                sol.append(csol.copy())
            return
        
        self.f(ind+1, nums, csol.copy(), sol)
        csol.append(nums[ind])
        self.f(ind+1, nums, csol.copy(), sol)


    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        sol = []
        nums.sort()
        self.f(0,nums, [], sol)
        return sol
