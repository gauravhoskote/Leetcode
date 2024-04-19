import bisect
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        nums = sorted(set(nums))
        i = 0
        prev = 0
        sol = n-1
        while i < len(nums):
            index = bisect.bisect_left(nums, nums[i]+n)
            print(index)
            sol = min(sol, n-index+i)
            i+=1
        return sol
