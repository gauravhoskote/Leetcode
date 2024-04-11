class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        mm = float('inf')
        pfsm = 0
        for x in nums:
            pfsm += x
            mm = min(mm, pfsm)
        if mm >= 0:
            return 1
        else:
            return -mm + 1
