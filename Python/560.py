class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dd = {}
        dd[0] = 1
        cs = 0
        sol = 0
        for x in nums:
            cs += x
            sol += dd.get(cs-k, 0)
            dd[cs] = dd.get(cs, 0)+1
        return sol
