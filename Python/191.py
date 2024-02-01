class Solution:
    def hammingWeight(self, n: int) -> int:
        sol = 0
        while n != 0:
            sol += n%2
            n = n// 2
        return sol
