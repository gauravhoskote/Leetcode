class Solution:
    
    def f(self, sol, curr, ind, nums):
        if ind < len(nums)-1:
            self.f(sol, curr.copy(), ind+1, nums)
            curr.append(nums[ind])
            self.f(sol, curr.copy(), ind+1, nums)
        else:
            sol.append(curr.copy())
            curr.append(nums[ind])
            sol.append(curr.copy())

    def subsets(self, nums: List[int]) -> List[List[int]]:
        sol = []
        self.f(sol, [], 0, nums)
        return sol
