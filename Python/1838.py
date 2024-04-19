class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        ss = 0
        sol = float('-inf')
        for r in range(0, len(nums)):
            ss += nums[r]
            while (r - l + 1)*nums[r]-ss > k:
                ss -= nums[l]
                l+=1
            sol = max(sol, (r-l+1))
        return sol
