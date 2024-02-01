class Solution:
    def climbStairs(self, n: int) -> int:
        f = 1
        s = 2
        if n == 1:
            return f
        if n == 2:
            return s
        else:
            sol = 0
            for i in range(3, n+1):
                sol = f + s
                f = s
                s = sol
            return sol
