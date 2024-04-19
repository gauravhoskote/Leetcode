class Solution:
    def myPow(self, x: float, n: int) -> float:
        sol = 1
        flag = False
        if n < 0:
            flag = True
        
        n = abs(n)
        t = x
        while n:
            if n%2 == 1:
                if flag:
                    sol = sol / t
                else:
                    sol = sol * t
            t = t * t
            n = n//2
        return sol
