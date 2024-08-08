class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        sol = []
        for i in range(len(nums)//2):
            x = nums[i]
            y = nums[len(nums)-1-i]
            sol.append((x+y)/2)
        return min(sol)
