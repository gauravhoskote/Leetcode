class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        cs = 0
        dd = {}
        dd[0] = 1
        sol = 0
        for x in nums:
            cs = cs + x
            sol += dd.get(cs-goal, 0)
            dd[cs] = dd.get(cs,0)+1
        return sol
