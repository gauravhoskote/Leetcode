class Solution:
    def reverseBits(self, n: int) -> int:
        sol = 0
        for i in reversed(range(32)):
            sol = sol + ((n % 2) * (2**i))
            n = n // 2
        return sol
