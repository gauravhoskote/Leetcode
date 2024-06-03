class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        dd = Counter(nums)
        sol = 0
        for k,v in dd.items():
            if v == 2:
                sol = sol ^ k
        return sol
