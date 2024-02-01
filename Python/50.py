class Solution:
    def myPow(self, x: float, n: int) -> float:
        sol = 1
        if n == 0:
            return 1
        flag = False
        if n < 0:
            n = -n
            flag = True

        while n:
            if n % 2 == 1:
                if flag:
                    sol = sol / x
                else:
                    sol = sol * x
            x = x * x
            n = n//2
        return sol
