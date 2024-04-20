class Solution:
    def mySqrt(self, x: int) -> int:
        def condition(value):
            return value * value > x
        
        l = 0
        r = x+1
        while l < r:
            m = l + (r-l)//2
            if condition(m):
                r = m
            else:
                l = m+1
        return l-1
