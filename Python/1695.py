class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l = 0
        summ = 0
        sol = 0
        ss = set()
        for r in range(len(nums)):
            summ += nums[r]
            while nums[r] in ss:
                ss.remove(nums[l])
                summ -= nums[l]
                l+=1
            ss.add(nums[r])
            sol = max(sol, summ)
        return sol
